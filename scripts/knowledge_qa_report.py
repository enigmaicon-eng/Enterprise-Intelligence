"""
Knowledge QA report generator — aggregate quality analysis across the full graph.

Produces the P18 QA report: domain coverage, quality distribution, confidence calibration
summary, graph integrity, and missed connection candidates.

Usage:
    python scripts/knowledge_qa_report.py               # full report
    python scripts/knowledge_qa_report.py --domain pm   # domain-specific
    python scripts/knowledge_qa_report.py --coverage    # domain coverage only
    python scripts/knowledge_qa_report.py --missed      # missed connection candidates
    python scripts/knowledge_qa_report.py --promotions  # confidence promotion candidates
    python scripts/knowledge_qa_report.py --json        # machine-readable JSON output
"""

import json
import re
import sys
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path

WORKSPACE = Path(__file__).parent.parent
KNOWLEDGE_DIR = WORKSPACE / "knowledge"
GRAPH_PATH = KNOWLEDGE_DIR / "KNOWLEDGE-GRAPH.json"

KNOWLEDGE_DOMAINS = [
    "pm", "strategy", "systems", "technical", "operations", "patterns",
    "decisions", "clusters",
]

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
STALE_DAYS = 180
MIN_DOMAIN_ENTRIES = 3
MISSED_CONNECTION_TAG_THRESHOLD = 3


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


def days_since(date_str: str) -> int | None:
    if not date_str:
        return None
    try:
        d = datetime.strptime(date_str[:10], "%Y-%m-%d").date()
        return (date.today() - d).days
    except ValueError:
        return None


def body_length(text: str) -> int:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return len(text.strip())
    return len(text[match.end():].strip())


def load_graph() -> dict:
    if not GRAPH_PATH.exists():
        return {"nodes": [], "edges": [], "clusters": []}
    try:
        return json.loads(GRAPH_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {"nodes": [], "edges": [], "clusters": []}


def quality_score(node: dict, conn: int, text_body: int, tags_count: int) -> int:
    score = 0
    confidence = node.get("confidence", "")
    reviewed = node.get("reviewed", "")
    age = days_since(reviewed) if reviewed else None

    if node.get("title"):
        score += 10
    if confidence in ("high", "medium", "low"):
        score += 10
    if reviewed:
        score += 10
    if tags_count >= 2:
        score += 10
    if conn >= 1:
        score += 15
    if age is not None and age <= STALE_DAYS:
        score += 15
    if text_body >= 800:
        score += 20
    elif text_body >= 300:
        score += 10

    return score


def classify_band(score: int) -> str:
    if score >= 80:
        return "Strong"
    if score >= 60:
        return "Adequate"
    if score >= 40:
        return "Weak"
    return "Critical"


def find_missed_connections(nodes: list[dict], edges: list[dict]) -> list[dict]:
    """Find pairs in same domain with ≥3 shared tags but no edge between them."""
    edge_pairs: set[tuple] = set()
    for e in edges:
        edge_pairs.add((e["from"], e["to"]))
        edge_pairs.add((e["to"], e["from"]))

    by_domain: dict[str, list[dict]] = defaultdict(list)
    for n in nodes:
        by_domain[n["domain"]].append(n)

    candidates = []
    for domain, domain_nodes in by_domain.items():
        if domain == "clusters":
            continue
        for i, a in enumerate(domain_nodes):
            a_tags = set(t.lower() for t in a.get("tags", []))
            if not a_tags:
                continue
            for b in domain_nodes[i + 1:]:
                b_tags = set(t.lower() for t in b.get("tags", []))
                if not b_tags:
                    continue
                shared = a_tags & b_tags
                if len(shared) >= MISSED_CONNECTION_TAG_THRESHOLD:
                    if (a["id"], b["id"]) not in edge_pairs:
                        candidates.append({
                            "a": a["id"],
                            "b": b["id"],
                            "domain": domain,
                            "shared_tags": sorted(shared),
                            "overlap_count": len(shared),
                        })

    return sorted(candidates, key=lambda x: x["overlap_count"], reverse=True)


def find_dead_links(nodes: list[dict], edges: list[dict]) -> list[dict]:
    node_map = {n["id"]: n for n in nodes}
    dead = []
    for e in edges:
        for side in ("from", "to"):
            nid = e[side]
            n = node_map.get(nid)
            if n:
                fpath = WORKSPACE / n["file"]
                if not fpath.exists():
                    dead.append({"edge": e, "missing_side": side, "node_id": nid, "file": n["file"]})
            else:
                dead.append({"edge": e, "missing_side": side, "node_id": nid, "file": None})
    return dead


def find_promotion_candidates(node_results: list[dict]) -> list[dict]:
    """Entries that have earned a confidence bump based on access and connections."""
    candidates = []
    for r in node_results:
        node = r["node"]
        conf = node.get("confidence", "medium")
        conn = r["conn"]
        access = node.get("access_count", 0)
        reviewed_count = node.get("compound_events", 0)

        if conf == "low" and access >= 3 and conn >= 1:
            candidates.append({
                "node_id": node["id"],
                "title": node.get("title", node["id"]),
                "current": "low",
                "suggested": "medium",
                "reason": f"accessed {access}×, {conn} connections",
            })
        elif conf == "medium" and access >= 5 and conn >= 3 and reviewed_count >= 2:
            candidates.append({
                "node_id": node["id"],
                "title": node.get("title", node["id"]),
                "current": "medium",
                "suggested": "high",
                "reason": f"accessed {access}×, {conn} connections, {reviewed_count} compound events",
            })
    return sorted(candidates, key=lambda x: x["current"])


def build_report(nodes: list[dict], edges: list[dict], domain_filter: str | None = None) -> dict:
    if domain_filter:
        nodes = [n for n in nodes if n.get("domain") == domain_filter]

    conn_map: dict[str, int] = defaultdict(int)
    for e in edges:
        conn_map[e["from"]] += 1
        conn_map[e["to"]] += 1

    # Per-node enrichment
    node_results = []
    all_tags: dict[str, int] = defaultdict(int)
    domain_counts: dict[str, int] = defaultdict(int)
    band_counts: dict[str, int] = defaultdict(int)
    calibration_flags: dict[str, list] = defaultdict(list)

    for node in nodes:
        domain_counts[node.get("domain", "unknown")] += 1

        fpath = WORKSPACE / node["file"]
        if not fpath.exists():
            node_results.append({"node": node, "conn": conn_map.get(node["id"], 0),
                                  "score": 0, "band": "Critical", "body": 0, "tags": []})
            band_counts["Critical"] += 1
            continue

        text = fpath.read_text(encoding="utf-8", errors="replace")
        fm = parse_frontmatter(text)

        tags = fm.get("tags", [])
        if isinstance(tags, str):
            tags = [t.strip() for t in tags.split(",") if t.strip()]
        for t in tags:
            all_tags[t.lower()] += 1

        body = body_length(text)
        conn = conn_map.get(node["id"], 0)
        score = quality_score(node, conn, body, len(tags))
        band = classify_band(score)
        band_counts[band] += 1

        # Calibration
        conf = node.get("confidence", "")
        reviewed = node.get("reviewed", "")
        age = days_since(reviewed)
        access = node.get("access_count", 0)

        node_flags = []
        if conf == "high" and conn == 0 and (age is None or age > 90):
            node_flags.append("HIGH_NO_CORROBORATION")
        if conf == "high" and (age is None or age > STALE_DAYS):
            node_flags.append("HIGH_STALE")
        if conf == "low" and access >= 3:
            node_flags.append("LOW_MATURE")
        if not conf:
            node_flags.append("CONFIDENCE_MISSING")
        if node_flags:
            calibration_flags[node["id"]] = node_flags

        node_results.append({
            "node": node,
            "conn": conn,
            "score": score,
            "band": band,
            "body": body,
            "tags": tags,
        })

    # Aggregate metrics
    scores = [r["score"] for r in node_results]
    avg_score = round(sum(scores) / len(scores), 1) if scores else 0
    thin_domains = [d for d, c in domain_counts.items() if c < MIN_DOMAIN_ENTRIES and d != "clusters"]
    frequent_tags = sorted(all_tags.items(), key=lambda x: x[1], reverse=True)[:15]
    missed = find_missed_connections(nodes, edges) if not domain_filter else []
    dead = find_dead_links(nodes, edges) if not domain_filter else []
    promotions = find_promotion_candidates(node_results)

    return {
        "domain_filter": domain_filter,
        "total_nodes": len(nodes),
        "avg_score": avg_score,
        "band_counts": dict(band_counts),
        "domain_counts": dict(domain_counts),
        "thin_domains": thin_domains,
        "top_tags": frequent_tags,
        "calibration_flags": dict(calibration_flags),
        "missed_connections": missed[:10],
        "dead_links": dead,
        "promotion_candidates": promotions,
        "node_results": node_results,
    }


def print_report(report: dict) -> None:
    scope = f"domain={report['domain_filter']}" if report["domain_filter"] else "all domains"
    print(f"\nKnowledge QA Report — {scope}")
    print("=" * 60)
    print(f"  Entries analyzed: {report['total_nodes']}  |  Avg quality score: {report['avg_score']}/90")

    bc = report["band_counts"]
    print(f"  Strong: {bc.get('Strong', 0)}  |  Adequate: {bc.get('Adequate', 0)}  "
          f"|  Weak: {bc.get('Weak', 0)}  |  Critical: {bc.get('Critical', 0)}")

    print(f"\n  Coverage by domain:")
    for domain, count in sorted(report["domain_counts"].items(), key=lambda x: x[1], reverse=True):
        thin_marker = " ← THIN" if domain in report["thin_domains"] else ""
        print(f"    {domain:<15} {count} entries{thin_marker}")

    if report["thin_domains"]:
        print(f"\n  Thin domains (< {MIN_DOMAIN_ENTRIES} entries): {', '.join(report['thin_domains'])}")
        print("    → Use /learn to add entries to these areas")

    cf = report["calibration_flags"]
    if cf:
        print(f"\n  Confidence calibration issues ({len(cf)} entries):")
        flag_summary: dict[str, int] = defaultdict(int)
        for flags in cf.values():
            for f in flags:
                flag_summary[f] += 1
        for flag, count in sorted(flag_summary.items(), key=lambda x: x[1], reverse=True):
            print(f"    {flag}: {count} entries")
        print("    → Run: python knowledge_validate.py --uncalibrated")

    dl = report["dead_links"]
    if dl:
        print(f"\n  Dead links ({len(dl)}) — fix immediately:")
        for d in dl[:5]:
            e = d["edge"]
            print(f"    {e['from']} → {e['to']} ({e['type']}) — {d['missing_side']} missing")
        if len(dl) > 5:
            print(f"    ... and {len(dl) - 5} more. Run: python knowledge_validate.py --dead-links")
    else:
        print("\n  Graph integrity: OK (no dead links)")

    mc = report["missed_connections"]
    if mc:
        print(f"\n  Missed connection candidates ({len(mc)} pairs with ≥{MISSED_CONNECTION_TAG_THRESHOLD} shared tags):")
        for c in mc[:5]:
            tags_str = ", ".join(c["shared_tags"][:4])
            print(f"    {c['a']} ↔ {c['b']}  (shared: {tags_str})")
        print("    → Use /knowledge-connect to create edges, or confirm these are unrelated")

    pc = report["promotion_candidates"]
    if pc:
        print(f"\n  Confidence promotion candidates ({len(pc)}):")
        for p in pc[:5]:
            print(f"    {p['node_id']}  {p['current']} → {p['suggested']}  ({p['reason']})")
        print("    → Use /knowledge-validate [node_id] then update confidence in frontmatter")

    worst = [r for r in report["node_results"] if r["band"] in ("Critical", "Weak")]
    worst.sort(key=lambda x: x["score"])
    if worst:
        print(f"\n  Lowest quality entries ({len(worst)} weak/critical):")
        for r in worst[:8]:
            print(f"    [{r['band']:<8}] {r['node']['id']:<40} score: {r['score']}/90")
        print("    → Use /knowledge-validate [node_id] for detailed findings")

    print(f"\n  Next actions:")
    if report["dead_links"]:
        print("    1. Fix dead links (silent retrieval failures)")
    if bc.get("Critical", 0) > 0:
        print(f"    {2 if report['dead_links'] else 1}. Fix critical entries — run /knowledge-validate --all")
    if cf:
        print(f"    → Review calibration flags — run /knowledge-qa --promotions")
    print()


def main() -> int:
    args = sys.argv[1:]
    graph = load_graph()
    nodes = graph["nodes"]
    edges = graph["edges"]

    domain = None
    if "--domain" in args:
        idx = args.index("--domain")
        if idx + 1 < len(args):
            domain = args[idx + 1]

    if "--coverage" in args:
        counts: dict[str, int] = defaultdict(int)
        for n in nodes:
            if domain and n.get("domain") != domain:
                continue
            counts[n.get("domain", "unknown")] += 1
        print(f"\n  Knowledge coverage:")
        for d, c in sorted(counts.items(), key=lambda x: x[1], reverse=True):
            marker = " ← THIN" if c < MIN_DOMAIN_ENTRIES and d != "clusters" else ""
            print(f"    {d:<15} {c} entries{marker}")
        print()
        return 0

    if "--missed" in args:
        filtered = [n for n in nodes if not domain or n.get("domain") == domain]
        candidates = find_missed_connections(filtered, edges)
        print(f"\n  Missed connection candidates ({len(candidates)}):")
        for c in candidates[:15]:
            tags_str = ", ".join(c["shared_tags"])
            print(f"    {c['a']}")
            print(f"    ↔ {c['b']}")
            print(f"      shared tags: {tags_str}")
            print()
        if not candidates:
            print("    None found — all highly-overlapping entry pairs are already connected.")
        print()
        return 0

    if "--promotions" in args:
        report = build_report(nodes, edges, domain)
        pc = report["promotion_candidates"]
        print(f"\n  Confidence promotion candidates ({len(pc)}):")
        for p in pc:
            print(f"    {p['node_id']:<42} {p['current']} → {p['suggested']}  ({p['reason']})")
        if not pc:
            print("    No promotion candidates found.")
        print()
        return 0

    report = build_report(nodes, edges, domain)

    if "--json" in args:
        # Omit node_results (too verbose) from JSON output
        out = {k: v for k, v in report.items() if k != "node_results"}
        print(json.dumps(out, indent=2))
        return 0

    print_report(report)
    return 0


if __name__ == "__main__":
    sys.exit(main())
