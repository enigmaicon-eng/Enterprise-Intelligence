"""
Knowledge graph index builder — scans all knowledge entries and builds KNOWLEDGE-GRAPH.json.

Run after adding knowledge entries, creating connections, or synthesizing clusters.
Also run after /learn creates a new entry to surface connection candidates.

Usage:
    python scripts/knowledge_index.py              # full rebuild
    python scripts/knowledge_index.py --check      # verify index is current
    python scripts/knowledge_index.py --stats      # graph statistics
    python scripts/knowledge_index.py --orphans    # list entries with 0 connections
    python scripts/knowledge_index.py --candidates # list cluster synthesis candidates (≥5 nodes)
"""

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

WORKSPACE = Path(__file__).parent.parent
KNOWLEDGE_DIR = WORKSPACE / "knowledge"
GRAPH_PATH = KNOWLEDGE_DIR / "KNOWLEDGE-GRAPH.json"

# Domains to scan for knowledge entries
KNOWLEDGE_DOMAINS = [
    "pm", "strategy", "systems", "technical", "operations", "patterns",
    "decisions", "clusters",
]

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
CONFIDENCE_WEIGHT = {"high": 1.0, "medium": 0.7, "low": 0.3}


def parse_frontmatter(text: str) -> dict:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}
    block = match.group(1)
    result: dict = {}
    list_key = None
    list_items: list = []

    for line in block.splitlines():
        if not line.strip():
            continue
        if line.startswith("- ") and list_key:
            list_items.append(line[2:].strip())
            continue
        if ":" in line and not line.startswith(" "):
            if list_key and list_items:
                result[list_key] = list_items
            kv = line.split(":", 1)
            key = kv[0].strip()
            val = kv[1].strip() if len(kv) > 1 else ""
            if val == "":
                list_key = key
                list_items = []
            elif val.startswith("[") and val.endswith("]"):
                inner = val[1:-1].strip()
                result[key] = [x.strip() for x in inner.split(",") if x.strip()] if inner else []
                list_key = None
            else:
                result[key] = val
                list_key = None
        else:
            list_key = None

    if list_key and list_items:
        result[list_key] = list_items
    return result


def extract_title(text: str, fm: dict, filepath: Path) -> str:
    for field in ("title", "name", "topic"):
        if fm.get(field):
            return fm[field]
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return filepath.stem.replace("-", " ").title()


def extract_tags(fm: dict) -> list[str]:
    tags = fm.get("tags", [])
    if isinstance(tags, str):
        return [t.strip() for t in tags.split(",") if t.strip()]
    return tags if isinstance(tags, list) else []


def scan_knowledge_entries() -> list[dict]:
    """Scan all knowledge directories and return node dicts."""
    nodes = []
    for domain in KNOWLEDGE_DOMAINS:
        domain_dir = KNOWLEDGE_DIR / domain
        if not domain_dir.exists():
            continue
        for filepath in sorted(domain_dir.glob("*.md")):
            if filepath.name in ("README.md", "index.md"):
                continue
            try:
                text = filepath.read_text(encoding="utf-8")
            except OSError:
                continue

            fm = parse_frontmatter(text)
            node_id = f"{domain}/{filepath.stem}"
            rel_path = str(filepath.relative_to(WORKSPACE)).replace("\\", "/")

            # Collect explicit connections from frontmatter if present
            related = fm.get("related_to", [])
            builds_on = fm.get("builds_on", [])
            contradicts = fm.get("contradicts", [])

            nodes.append({
                "id": node_id,
                "title": extract_title(text, fm, filepath),
                "domain": domain,
                "file": rel_path,
                "confidence": fm.get("confidence", "medium"),
                "reviewed": fm.get("reviewed", fm.get("last_updated", "")),
                "last_accessed": fm.get("last_accessed", ""),
                "access_count": int(fm.get("access_count", "0")) if str(fm.get("access_count", "0")).isdigit() else 0,
                "compound_events": int(fm.get("compound_events", "0")) if str(fm.get("compound_events", "0")).isdigit() else 0,
                "cluster": fm.get("cluster", []) if isinstance(fm.get("cluster"), list) else [],
                "tags": extract_tags(fm),
                "_raw_related": related,
                "_raw_builds_on": builds_on,
                "_raw_contradicts": contradicts,
            })
    return nodes


def extract_edges_from_nodes(nodes: list[dict]) -> list[dict]:
    """Build edges from frontmatter connection fields in nodes."""
    node_ids = {n["id"] for n in nodes}
    edges = []
    today = datetime.now().strftime("%Y-%m-%d")

    for node in nodes:
        for rel in node.get("_raw_related", []):
            if rel in node_ids:
                edges.append({
                    "from": node["id"], "to": rel,
                    "type": "related_to", "weight": 0.7,
                    "created_at": today, "note": ""
                })
        for dep in node.get("_raw_builds_on", []):
            if dep in node_ids:
                edges.append({
                    "from": node["id"], "to": dep,
                    "type": "builds_on", "weight": 0.9,
                    "created_at": today, "note": ""
                })
        for contra in node.get("_raw_contradicts", []):
            if contra in node_ids:
                edges.append({
                    "from": node["id"], "to": contra,
                    "type": "contradicts", "weight": 0.8,
                    "created_at": today, "note": ""
                })

    # Deduplicate edges
    seen = set()
    unique_edges = []
    for e in edges:
        key = (e["from"], e["to"], e["type"])
        rev_key = (e["to"], e["from"], e["type"])
        if key not in seen and rev_key not in seen:
            seen.add(key)
            unique_edges.append(e)

    return unique_edges


def load_existing_graph() -> dict:
    if not GRAPH_PATH.exists():
        return {"edges": [], "clusters": []}
    try:
        return json.loads(GRAPH_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {"edges": [], "clusters": []}


def build_graph(nodes: list[dict], edges: list[dict], clusters: list[dict]) -> dict:
    # Clean node dicts (remove raw fields used for edge extraction)
    clean_nodes = []
    for n in nodes:
        clean = {k: v for k, v in n.items() if not k.startswith("_")}
        clean_nodes.append(clean)

    # Compute connection counts
    connection_map: dict[str, int] = {}
    for e in edges:
        connection_map[e["from"]] = connection_map.get(e["from"], 0) + 1
        connection_map[e["to"]] = connection_map.get(e["to"], 0) + 1

    total_nodes = len(clean_nodes)
    total_edges = len(edges)
    avg = round(sum(connection_map.values()) / total_nodes, 2) if total_nodes else 0
    isolated = sum(1 for n in clean_nodes if n["id"] not in connection_map)

    return {
        "_schema": "P17 Knowledge Graph v1.0",
        "_note": "Generated by scripts/knowledge_index.py. Do not edit manually.",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "stats": {
            "total_nodes": total_nodes,
            "total_edges": total_edges,
            "total_clusters": len(clusters),
            "avg_connections_per_node": avg,
            "isolated_nodes": isolated,
        },
        "nodes": clean_nodes,
        "edges": edges,
        "clusters": clusters,
    }


def find_cluster_candidates(nodes: list[dict], edges: list[dict]) -> list[dict]:
    """Find groups of ≥5 nodes with high connectivity — synthesis candidates."""
    connection_map: dict[str, set] = {}
    for e in edges:
        connection_map.setdefault(e["from"], set()).add(e["to"])
        connection_map.setdefault(e["to"], set()).add(e["from"])

    candidates = []
    for node in nodes:
        neighbors = connection_map.get(node["id"], set())
        if len(neighbors) >= 4:  # this node + 4 neighbors = 5-node cluster candidate
            candidates.append({
                "center": node["id"],
                "title": node["title"],
                "neighbor_count": len(neighbors),
                "neighbors": list(neighbors),
            })

    return sorted(candidates, key=lambda x: x["neighbor_count"], reverse=True)


def main() -> int:
    args = sys.argv[1:]
    nodes = scan_knowledge_entries()
    new_edges = extract_edges_from_nodes(nodes)
    existing = load_existing_graph()

    # Merge: keep manually-added edges that aren't from frontmatter
    existing_edges = existing.get("edges", [])
    frontmatter_keys = {(e["from"], e["to"], e["type"]) for e in new_edges}
    manual_edges = [
        e for e in existing_edges
        if (e["from"], e["to"], e["type"]) not in frontmatter_keys
    ]
    all_edges = new_edges + manual_edges
    clusters = existing.get("clusters", [])

    if "--stats" in args:
        connection_map: dict[str, int] = {}
        for e in all_edges:
            connection_map[e["from"]] = connection_map.get(e["from"], 0) + 1
            connection_map[e["to"]] = connection_map.get(e["to"], 0) + 1
        print(f"\nKnowledge Graph Stats")
        print("=" * 40)
        print(f"  Nodes     : {len(nodes)}")
        print(f"  Edges     : {len(all_edges)}")
        print(f"  Clusters  : {len(clusters)}")
        isolated = sum(1 for n in nodes if n["id"] not in connection_map)
        print(f"  Isolated  : {isolated}")
        if nodes:
            avg = sum(connection_map.values()) / len(nodes)
            print(f"  Avg edges : {avg:.1f}")
        print()
        return 0

    if "--orphans" in args:
        connected = set()
        for e in all_edges:
            connected.add(e["from"])
            connected.add(e["to"])
        orphans = [n for n in nodes if n["id"] not in connected]
        if not orphans:
            print("  No isolated nodes.")
        else:
            print(f"\n  {len(orphans)} isolated node(s):")
            for n in orphans:
                print(f"    [{n['domain']:<12}] {n['id']}  — {n['title']}")
        return 0

    if "--candidates" in args:
        candidates = find_cluster_candidates(nodes, all_edges)
        if not candidates:
            print("  No cluster synthesis candidates yet (need ≥5 connected entries).")
        else:
            print(f"\n  Cluster synthesis candidates:")
            for c in candidates[:5]:
                print(f"    {c['center']}  ({c['neighbor_count']} neighbors)  — {c['title']}")
        return 0

    if "--check" in args:
        if not GRAPH_PATH.exists():
            print("  KNOWLEDGE-GRAPH.json not found. Run without --check to build.")
            return 1
        existing_graph = json.loads(GRAPH_PATH.read_text(encoding="utf-8"))
        existing_count = existing_graph.get("stats", {}).get("total_nodes", 0)
        if existing_count != len(nodes):
            print(f"  [STALE] Index has {existing_count} nodes; {len(nodes)} found on disk.")
            return 1
        print(f"  [OK] Graph is current: {len(nodes)} nodes, {len(all_edges)} edges.")
        return 0

    # Full rebuild
    graph = build_graph(nodes, all_edges, clusters)
    GRAPH_PATH.write_text(json.dumps(graph, indent=2), encoding="utf-8")
    s = graph["stats"]
    print(f"\n  [OK] KNOWLEDGE-GRAPH.json rebuilt")
    print(f"       Nodes: {s['total_nodes']}  |  Edges: {s['total_edges']}  |  Isolated: {s['isolated_nodes']}")
    if s["isolated_nodes"] > 0:
        print(f"  [HINT] {s['isolated_nodes']} isolated nodes — run /knowledge-connect to add connections")
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
