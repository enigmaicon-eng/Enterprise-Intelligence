"""
Knowledge search — graph-aware ranked retrieval for the P17 compounding system.

Applies the scoring algorithm from architecture/RETRIEVAL-INTELLIGENCE.md.
Called conceptually by /recall and /knowledge-graph skills.
Also tracks access_count and last_accessed in the graph.

Usage:
    python scripts/knowledge_search.py "product strategy"
    python scripts/knowledge_search.py --domain pm "growth"
    python scripts/knowledge_search.py --type cluster "ai systems"
    python scripts/knowledge_search.py --stats        # access frequency report
    python scripts/knowledge_search.py --gaps         # never-accessed entries
    python scripts/knowledge_search.py --no-track "query"   # read-only, no access update
"""

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

WORKSPACE = Path(__file__).parent.parent
KNOWLEDGE_DIR = WORKSPACE / "knowledge"
GRAPH_PATH = KNOWLEDGE_DIR / "KNOWLEDGE-GRAPH.json"

CONFIDENCE_SCORE = {"high": 1.0, "medium": 0.7, "low": 0.3}

# Scoring weights
W_KEYWORD = 0.45
W_CONFIDENCE = 0.20
W_RECENCY = 0.15
W_CONNECTION = 0.10
W_TAG = 0.10


def load_graph() -> dict:
    if not GRAPH_PATH.exists():
        print("KNOWLEDGE-GRAPH.json not found. Run: python scripts/knowledge_index.py")
        sys.exit(1)
    return json.loads(GRAPH_PATH.read_text(encoding="utf-8"))


def save_graph(graph: dict) -> None:
    GRAPH_PATH.write_text(json.dumps(graph, indent=2), encoding="utf-8")


def tokenize(text: str) -> set[str]:
    return set(re.findall(r"\b[a-z]{3,}\b", text.lower()))


def keyword_score(query_tokens: set[str], node: dict) -> float:
    title_tokens = tokenize(node.get("title", ""))
    tags = set(t.lower() for t in node.get("tags", []))

    title_overlap = len(query_tokens & title_tokens) / max(len(query_tokens), 1)
    tag_overlap = len(query_tokens & tags) / max(len(query_tokens), 1)

    if title_overlap >= 0.8:
        return 1.0
    if title_overlap >= 0.4:
        return 0.7
    if tag_overlap >= 0.3:
        return 0.4
    if title_overlap > 0 or tag_overlap > 0:
        return 0.3
    return 0.0


def recency_score(reviewed: str) -> float:
    if not reviewed:
        return 0.5  # unknown = neutral
    try:
        reviewed_date = datetime.strptime(reviewed[:10], "%Y-%m-%d")
        days_old = (datetime.now() - reviewed_date).days
        if days_old <= 30:
            return 1.0
        if days_old <= 90:
            return 0.8
        if days_old <= 180:
            return 0.6
        if days_old <= 365:
            return 0.4
        return 0.3
    except ValueError:
        return 0.5


def connection_density_score(node_id: str, edges: list[dict]) -> float:
    count = sum(1 for e in edges if e["from"] == node_id or e["to"] == node_id)
    return min(count * 0.04, 0.20)


def tag_match_score(query_tokens: set[str], node: dict) -> float:
    tags = set(t.lower() for t in node.get("tags", []))
    overlap = len(query_tokens & tags)
    if overlap >= 3:
        return 1.0
    if overlap == 2:
        return 0.7
    if overlap == 1:
        return 0.4
    return 0.0


def score_node(node: dict, query_tokens: set[str], edges: list[dict]) -> float:
    kw = keyword_score(query_tokens, node)
    if kw == 0.0:
        return 0.0  # Early exit: no keyword match = no result

    conf = CONFIDENCE_SCORE.get(node.get("confidence", "medium"), 0.7)
    rec = recency_score(node.get("reviewed", ""))
    conn = connection_density_score(node["id"], edges)
    tag = tag_match_score(query_tokens, node)

    return (kw * W_KEYWORD + conf * W_CONFIDENCE + rec * W_RECENCY
            + conn * W_CONNECTION + tag * W_TAG)


def get_neighbors(node_id: str, edges: list[dict], nodes: list[dict]) -> list[dict]:
    """Return 1-hop neighbors with edge type, sorted by their own confidence."""
    node_map = {n["id"]: n for n in nodes}
    neighbors = []
    for e in edges:
        if e["from"] == node_id:
            target = e["to"]
        elif e["to"] == node_id:
            target = e["from"]
        else:
            continue
        if target in node_map:
            neighbors.append({
                "node": node_map[target],
                "edge_type": e["type"],
                "weight": e.get("weight", 0.5),
            })
    # Sort by confidence, then weight
    neighbors.sort(key=lambda x: (CONFIDENCE_SCORE.get(x["node"].get("confidence"), 0.7), x["weight"]), reverse=True)
    return neighbors[:5]  # Cap at 5 neighbors shown


def update_access(graph: dict, node_id: str) -> None:
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    for node in graph["nodes"]:
        if node["id"] == node_id:
            node["last_accessed"] = today
            node["access_count"] = node.get("access_count", 0) + 1
            break


def search(query: str, domain_filter: str | None = None, type_filter: str | None = None,
           track: bool = True, top_n: int = 5) -> list[dict]:
    graph = load_graph()
    nodes = graph["nodes"]
    edges = graph["edges"]

    query_tokens = tokenize(query)

    scored = []
    for node in nodes:
        if domain_filter and node.get("domain") != domain_filter:
            continue
        if type_filter == "cluster" and node.get("domain") != "clusters":
            continue
        s = score_node(node, query_tokens, edges)
        if s > 0.0:
            scored.append((s, node))

    scored.sort(key=lambda x: x[0], reverse=True)
    results = []
    for score, node in scored[:top_n]:
        neighbors = get_neighbors(node["id"], edges, nodes)
        results.append({
            "score": round(score, 3),
            "node": node,
            "neighbors": neighbors,
        })
        if track:
            update_access(graph, node["id"])

    if track and results:
        save_graph(graph)

    return results


def format_results(results: list[dict], query: str) -> str:
    if not results:
        return (
            f"\n  No results for: \"{query}\"\n"
            "  → Use /learn to capture this as new knowledge.\n"
            "  → Use /knowledge-connect --discover to find related entries.\n"
        )

    lines = [f"\nKnowledge Retrieval — \"{query}\"", "=" * 55]
    for i, r in enumerate(results, 1):
        node = r["node"]
        conf_flag = " ⚠" if node.get("confidence") == "low" else ""
        reviewed = node.get("reviewed", "unknown")
        lines.append(
            f"\n  {i}. [{node['domain']:<12}] {node['title']}{conf_flag}"
        )
        lines.append(f"     Score: {r['score']:.2f}  |  Confidence: {node.get('confidence', '?')}  |  Reviewed: {reviewed}")
        lines.append(f"     File: {node['file']}")

        if r["neighbors"]:
            lines.append("     Also see:")
            for nb in r["neighbors"][:3]:
                n = nb["node"]
                lines.append(f"       [{nb['edge_type']:<12}] {n['title']}  ({n['domain']})")

    lines.append("")
    return "\n".join(lines)


def main() -> int:
    args = sys.argv[1:]
    if not args:
        print("Usage: python knowledge_search.py [--domain D] [--type cluster] [--stats] [--gaps] [--no-track] <query>")
        return 1

    if "--stats" in args:
        graph = load_graph()
        nodes = sorted(graph["nodes"], key=lambda n: n.get("access_count", 0), reverse=True)
        print("\nKnowledge Access Frequency")
        print("=" * 45)
        for n in nodes[:15]:
            count = n.get("access_count", 0)
            last = n.get("last_accessed", "never")
            print(f"  {count:>4}x  {n['title']:<40}  ({last})")
        print()
        return 0

    if "--gaps" in args:
        graph = load_graph()
        never = [n for n in graph["nodes"] if not n.get("last_accessed")]
        print(f"\n  Never-accessed entries ({len(never)}):")
        for n in never:
            print(f"    [{n['domain']:<12}] {n['title']}")
        print()
        return 0

    domain = None
    if "--domain" in args:
        idx = args.index("--domain")
        if idx + 1 < len(args):
            domain = args[idx + 1]
            args = args[:idx] + args[idx + 2:]

    type_filter = None
    if "--type" in args:
        idx = args.index("--type")
        if idx + 1 < len(args):
            type_filter = args[idx + 1]
            args = args[:idx] + args[idx + 2:]

    track = "--no-track" not in args
    if not track:
        args = [a for a in args if a != "--no-track"]

    query = " ".join(a for a in args if not a.startswith("--"))
    if not query:
        print("Provide a query.")
        return 1

    results = search(query, domain_filter=domain, type_filter=type_filter, track=track)
    print(format_results(results, query))
    return 0


if __name__ == "__main__":
    sys.exit(main())
