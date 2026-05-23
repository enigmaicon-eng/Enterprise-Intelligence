"""
Knowledge review scheduler — spaced repetition surface for P17.

Applies the review schedule from architecture/RETRIEVAL-INTELLIGENCE.md.
Surfaces entries overdue for review, prioritized by: confidence, connection density, days overdue.

Usage:
    python scripts/knowledge_review.py              # show overdue entries
    python scripts/knowledge_review.py --all        # show full review schedule
    python scripts/knowledge_review.py --domain pm  # filter by domain
    python scripts/knowledge_review.py --mark-reviewed pm/product-strategy  # update reviewed date
"""

import json
import sys
from datetime import datetime, date, timezone
from pathlib import Path

WORKSPACE = Path(__file__).parent.parent
KNOWLEDGE_DIR = WORKSPACE / "knowledge"
GRAPH_PATH = KNOWLEDGE_DIR / "KNOWLEDGE-GRAPH.json"

CONFIDENCE_WEIGHT = {"high": 1.0, "medium": 2.0, "low": 3.0}  # Higher = more urgent

# Review intervals by (confidence, has_many_connections)
REVIEW_INTERVALS: dict[tuple, int] = {
    ("high", True): 90,
    ("high", False): 60,
    ("medium", True): 30,
    ("medium", False): 21,
    ("low", True): 14,
    ("low", False): 7,
}


def load_graph() -> dict:
    if not GRAPH_PATH.exists():
        print("KNOWLEDGE-GRAPH.json not found. Run: python scripts/knowledge_index.py")
        sys.exit(1)
    return json.loads(GRAPH_PATH.read_text(encoding="utf-8"))


def save_graph(graph: dict) -> None:
    GRAPH_PATH.write_text(json.dumps(graph, indent=2), encoding="utf-8")


def connection_count(node_id: str, edges: list[dict]) -> int:
    return sum(1 for e in edges if e["from"] == node_id or e["to"] == node_id)


def days_since_reviewed(reviewed_str: str) -> int | None:
    if not reviewed_str:
        return None
    try:
        reviewed = datetime.strptime(reviewed_str[:10], "%Y-%m-%d").date()
        return (date.today() - reviewed).days
    except ValueError:
        return None


def review_interval(node: dict, edges: list[dict]) -> int:
    conf = node.get("confidence", "medium")
    if conf not in ("high", "medium", "low"):
        conf = "medium"
    many_connections = connection_count(node["id"], edges) >= 5
    return REVIEW_INTERVALS.get((conf, many_connections), 30)


def priority_score(node: dict, days_overdue: int, edges: list[dict]) -> float:
    conf_w = CONFIDENCE_WEIGHT.get(node.get("confidence", "medium"), 2.0)
    conn_count = connection_count(node["id"], edges)
    return days_overdue * conf_w * max(conn_count * 0.1, 1.0)


def get_review_schedule(graph: dict, domain_filter: str | None = None) -> list[dict]:
    nodes = graph["nodes"]
    edges = graph["edges"]
    today = date.today()
    schedule = []

    for node in nodes:
        if domain_filter and node.get("domain") != domain_filter:
            continue

        days_ago = days_since_reviewed(node.get("reviewed", ""))
        interval = review_interval(node, edges)

        if days_ago is None:
            days_overdue = 999  # Never reviewed = very overdue
        else:
            days_overdue = days_ago - interval

        next_review = None
        if days_ago is not None:
            from datetime import timedelta
            reviewed_date = datetime.strptime(node.get("reviewed", "")[:10], "%Y-%m-%d").date()
            next_review = reviewed_date + __import__("datetime").timedelta(days=interval)

        schedule.append({
            "node": node,
            "days_ago": days_ago,
            "interval": interval,
            "days_overdue": days_overdue,
            "next_review": str(next_review) if next_review else None,
            "priority": priority_score(node, max(days_overdue, 0), edges),
            "overdue": days_overdue > 0,
            "conn_count": connection_count(node["id"], edges),
        })

    return sorted(schedule, key=lambda x: x["priority"], reverse=True)


def mark_reviewed(graph: dict, node_id: str) -> bool:
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    for node in graph["nodes"]:
        if node["id"] == node_id:
            node["reviewed"] = today
            save_graph(graph)
            return True
    return False


def main() -> int:
    args = sys.argv[1:]

    if "--mark-reviewed" in args:
        idx = args.index("--mark-reviewed")
        if idx + 1 >= len(args):
            print("--mark-reviewed requires a node_id (e.g., pm/product-strategy)")
            return 1
        node_id = args[idx + 1]
        graph = load_graph()
        ok = mark_reviewed(graph, node_id)
        if ok:
            print(f"  [OK] Marked as reviewed: {node_id} ({datetime.now().strftime('%Y-%m-%d')})")
        else:
            print(f"  [FAIL] Node not found: {node_id}")
        return 0 if ok else 1

    domain = None
    if "--domain" in args:
        idx = args.index("--domain")
        if idx + 1 < len(args):
            domain = args[idx + 1]

    show_all = "--all" in args
    graph = load_graph()
    schedule = get_review_schedule(graph, domain_filter=domain)

    overdue = [s for s in schedule if s["overdue"]]
    upcoming = [s for s in schedule if not s["overdue"]]

    print(f"\nKnowledge Review Schedule")
    print("=" * 55)

    if not overdue:
        print("  No entries overdue for review.")
    else:
        print(f"\n  OVERDUE ({len(overdue)} entries)")
        print("  " + "-" * 50)
        for s in overdue[:10]:
            n = s["node"]
            conf = n.get("confidence", "?")
            days_str = f"{s['days_overdue']}d overdue" if s["days_ago"] is not None else "never reviewed"
            print(f"  [{conf:<6}] {n['title']:<40} {days_str}")
            print(f"           {n['file']}  (interval: {s['interval']}d, connections: {s['conn_count']})")

        if len(overdue) > 10:
            print(f"  ... and {len(overdue) - 10} more")

    if show_all and upcoming:
        print(f"\n  UPCOMING ({len(upcoming)} entries)")
        print("  " + "-" * 50)
        for s in upcoming[:10]:
            n = s["node"]
            print(f"  {n['title']:<42} next: {s['next_review']}")

    print(f"\n  Total: {len(overdue)} overdue, {len(upcoming)} upcoming")
    print(f"  To mark as reviewed: python knowledge_review.py --mark-reviewed <node_id>")
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
