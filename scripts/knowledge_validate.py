"""
Knowledge entry validator — structural quality, confidence calibration, and graph integrity checks.

Runs the P18 validation pipeline on individual entries or full domains.
Does not require LLM reasoning; operates entirely on metadata and graph topology.

Usage:
    python scripts/knowledge_validate.py pm/product-strategy        # validate one entry
    python scripts/knowledge_validate.py --domain pm                # validate all in domain
    python scripts/knowledge_validate.py --all                      # validate all entries
    python scripts/knowledge_validate.py --stale                    # high-confidence + reviewed >180d
    python scripts/knowledge_validate.py --uncalibrated             # calibration flag candidates
    python scripts/knowledge_validate.py --dead-links               # graph integrity check
"""

import json
import re
import sys
from datetime import datetime, date
from pathlib import Path

WORKSPACE = Path(__file__).parent.parent
KNOWLEDGE_DIR = WORKSPACE / "knowledge"
GRAPH_PATH = KNOWLEDGE_DIR / "KNOWLEDGE-GRAPH.json"

KNOWLEDGE_DOMAINS = [
    "pm", "strategy", "systems", "technical", "operations", "patterns",
    "decisions", "clusters",
]

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)

# Quality scoring weights
SCORE_TITLE = 10
SCORE_CONFIDENCE = 10
SCORE_REVIEWED = 10
SCORE_TAGS = 10
SCORE_CONNECTIONS = 15
SCORE_RECENCY = 15
SCORE_CONTENT_MED = 10
SCORE_CONTENT_RICH = 10
MAX_SCORE = 90

STALE_DAYS = 180
LOW_MATURE_REVIEWS = 3


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


def body_length(text: str) -> int:
    """Character count of content after the frontmatter block."""
    match = FRONTMATTER_RE.match(text)
    if not match:
        return len(text.strip())
    return len(text[match.end():].strip())


def days_since(date_str: str) -> int | None:
    if not date_str:
        return None
    try:
        d = datetime.strptime(date_str[:10], "%Y-%m-%d").date()
        return (date.today() - d).days
    except ValueError:
        return None


def load_graph() -> dict:
    if not GRAPH_PATH.exists():
        return {"nodes": [], "edges": []}
    try:
        return json.loads(GRAPH_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {"nodes": [], "edges": []}


def connection_count(node_id: str, edges: list[dict]) -> int:
    return sum(1 for e in edges if e["from"] == node_id or e["to"] == node_id)


def validate_entry(node_id: str, graph: dict) -> dict:
    """Validate a single entry by node_id. Returns a quality report dict."""
    nodes = {n["id"]: n for n in graph["nodes"]}
    edges = graph["edges"]
    node = nodes.get(node_id)

    if node is None:
        return {
            "node_id": node_id,
            "error": "Node not found in graph. Run: python scripts/knowledge_index.py",
            "score": 0,
            "band": "Critical",
        }

    file_path = WORKSPACE / node["file"]
    if not file_path.exists():
        return {
            "node_id": node_id,
            "error": f"File not found on disk: {node['file']}",
            "score": 0,
            "band": "Critical",
        }

    text = file_path.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    score = 0
    issues: list[str] = []
    calibration_flags: list[str] = []
    integrity_flags: list[str] = []
    recommendations: list[str] = []

    # --- Structural completeness ---
    title = fm.get("title") or fm.get("name") or fm.get("topic")
    if title:
        score += SCORE_TITLE
    else:
        issues.append("Missing title field in frontmatter")
        recommendations.append("Add: title: [Entry Title]")

    confidence = fm.get("confidence", "")
    if confidence in ("high", "medium", "low"):
        score += SCORE_CONFIDENCE
    else:
        issues.append(f"Missing or invalid confidence field (got: '{confidence}')")
        calibration_flags.append("CONFIDENCE_MISSING")
        recommendations.append("Add: confidence: medium  (or high/low)")

    reviewed = fm.get("reviewed", fm.get("last_updated", ""))
    if reviewed:
        score += SCORE_REVIEWED
    else:
        issues.append("Missing reviewed date")
        recommendations.append("Add: reviewed: YYYY-MM-DD")

    tags = fm.get("tags", [])
    if isinstance(tags, str):
        tags = [t.strip() for t in tags.split(",") if t.strip()]
    if len(tags) >= 2:
        score += SCORE_TAGS
    elif len(tags) == 1:
        issues.append("Only 1 tag — tag_match retrieval score is reduced")
        recommendations.append("Add ≥2 tags for effective tag-based retrieval")
    else:
        issues.append("No tags — entry cannot participate in tag-match retrieval")
        recommendations.append("Add tags matching the domain concepts in this entry")

    # --- Retrieval readiness ---
    conn = connection_count(node_id, edges)
    if conn >= 1:
        score += SCORE_CONNECTIONS
    else:
        issues.append("No connections — isolated entry has lowest retrieval score")
        recommendations.append("Use /knowledge-connect to add at least 1 edge")

    age = days_since(reviewed) if reviewed else None
    if age is not None and age <= STALE_DAYS:
        score += SCORE_RECENCY
    elif age is None:
        issues.append("No reviewed date — recency score defaults to 0.5 (neutral)")
    else:
        issues.append(f"Last reviewed {age} days ago — recency score degraded")
        recommendations.append("Schedule a review: /knowledge-review " + node_id)

    # --- Content richness ---
    body = body_length(text)
    if body >= 800:
        score += SCORE_CONTENT_MED + SCORE_CONTENT_RICH
    elif body >= 300:
        score += SCORE_CONTENT_MED
        issues.append(f"Entry body is {body} chars — consider expanding for richer retrieval")
    else:
        issues.append(f"Thin entry: {body} chars body — minimal retrieval value")
        recommendations.append("Expand the entry with key claims, context, or examples")

    # --- Confidence calibration flags ---
    if confidence == "high":
        if conn == 0 and (age is None or age > 90):
            calibration_flags.append("HIGH_NO_CORROBORATION")
            recommendations.append(
                "High confidence but isolated and unreviewed in 90+ days — "
                "add connections or re-review to corroborate"
            )
        if age is not None and age > STALE_DAYS:
            calibration_flags.append("HIGH_STALE")
            recommendations.append(
                f"High confidence entry is {age} days since last review — "
                "high confidence may no longer be warranted"
            )

    access_count = node.get("access_count", 0)
    if confidence == "low" and access_count >= LOW_MATURE_REVIEWS:
        calibration_flags.append("LOW_MATURE")
        recommendations.append(
            f"Low confidence entry has been accessed {access_count}× — "
            "consider promoting to medium or removing if still uncertain"
        )

    # --- Graph integrity ---
    for edge in edges:
        if edge["from"] == node_id or edge["to"] == node_id:
            # Check self-reference
            if edge["from"] == edge["to"]:
                integrity_flags.append(f"SELF_REFERENCE: edge {edge['from']} → {edge['to']}")

            # Check dead links
            other_id = edge["to"] if edge["from"] == node_id else edge["from"]
            other_node = nodes.get(other_id)
            if other_node:
                other_file = WORKSPACE / other_node["file"]
                if not other_file.exists():
                    integrity_flags.append(f"DEAD_LINK: edge to {other_id} — file missing: {other_node['file']}")
            else:
                integrity_flags.append(f"DEAD_LINK: edge to {other_id} — node not in graph")

        # Check asymmetric contradictions
        if edge["type"] == "contradicts" and edge["from"] == node_id:
            reverse = any(
                e["from"] == edge["to"] and e["to"] == node_id and e["type"] == "contradicts"
                for e in edges
            )
            if not reverse:
                integrity_flags.append(
                    f"ASYMMETRIC_CONTRADICTION: {node_id} contradicts {edge['to']} "
                    f"but {edge['to']} has no contradicts edge back"
                )

    # --- Final score and band ---
    if integrity_flags:
        recommendations.insert(0, "Fix integrity flags first — they cause silent retrieval failures")

    if score >= 80:
        band = "Strong"
    elif score >= 60:
        band = "Adequate"
    elif score >= 40:
        band = "Weak"
    else:
        band = "Critical"

    return {
        "node_id": node_id,
        "title": node.get("title", node_id),
        "domain": node.get("domain", "?"),
        "score": score,
        "max_score": MAX_SCORE,
        "band": band,
        "confidence": confidence,
        "connections": conn,
        "reviewed": reviewed,
        "body_chars": body,
        "tags_count": len(tags),
        "issues": issues,
        "calibration_flags": calibration_flags,
        "integrity_flags": integrity_flags,
        "recommendations": recommendations,
    }


def scan_all_entries(domain_filter: str | None = None) -> list[str]:
    """Return all node_ids from scanned domain directories."""
    ids = []
    for domain in KNOWLEDGE_DOMAINS:
        if domain_filter and domain != domain_filter:
            continue
        domain_dir = KNOWLEDGE_DIR / domain
        if not domain_dir.exists():
            continue
        for f in sorted(domain_dir.glob("*.md")):
            if f.name not in ("README.md", "index.md"):
                ids.append(f"{domain}/{f.stem}")
    return ids


def format_report(result: dict) -> str:
    lines = []
    status_icon = {"Strong": "✓", "Adequate": "~", "Weak": "!", "Critical": "✗"}.get(result.get("band", "?"), "?")
    lines.append(
        f"\n  [{status_icon}] {result.get('title', result['node_id'])}  "
        f"({result.get('domain', '?')})"
    )
    if "error" in result:
        lines.append(f"      ERROR: {result['error']}")
        return "\n".join(lines)

    lines.append(
        f"      Score: {result['score']}/{result['max_score']}  |  Band: {result['band']}  |  "
        f"Confidence: {result['confidence']}  |  Connections: {result['connections']}  |  "
        f"Tags: {result['tags_count']}  |  Body: {result['body_chars']}c"
    )

    if result["issues"]:
        lines.append("      Issues:")
        for issue in result["issues"]:
            lines.append(f"        • {issue}")

    if result["calibration_flags"]:
        lines.append(f"      Calibration: {', '.join(result['calibration_flags'])}")

    if result["integrity_flags"]:
        lines.append("      Integrity:")
        for flag in result["integrity_flags"]:
            lines.append(f"        ⚠ {flag}")

    if result["recommendations"]:
        lines.append("      Recommended:")
        for rec in result["recommendations"][:3]:
            lines.append(f"        → {rec}")

    return "\n".join(lines)


def main() -> int:
    args = sys.argv[1:]

    graph = load_graph()

    # --dead-links: scan all edges for integrity issues
    if "--dead-links" in args:
        nodes = {n["id"]: n for n in graph["nodes"]}
        edges = graph["edges"]
        dead = []
        for e in edges:
            for side in ("from", "to"):
                nid = e[side]
                node = nodes.get(nid)
                if node:
                    fpath = WORKSPACE / node["file"]
                    if not fpath.exists():
                        dead.append(f"  DEAD: {e['from']} → {e['to']} ({e['type']}) — {side} file missing")
                else:
                    dead.append(f"  DEAD: {e['from']} → {e['to']} ({e['type']}) — {side} node not in graph")

        if dead:
            print(f"\n  Dead links ({len(dead)}):")
            for d in dead:
                print(d)
        else:
            print("\n  No dead links found. Graph integrity OK.")
        print()
        return 0

    # --stale: high-confidence entries with reviewed > STALE_DAYS
    if "--stale" in args:
        today = date.today()
        stale = []
        for node in graph["nodes"]:
            if node.get("confidence") != "high":
                continue
            reviewed = node.get("reviewed", "")
            age = days_since(reviewed)
            if age is None or age > STALE_DAYS:
                stale.append((age or 9999, node))
        stale.sort(key=lambda x: x[0], reverse=True)
        print(f"\n  High-confidence entries with stale review (>{STALE_DAYS}d): {len(stale)}")
        for age, node in stale[:15]:
            age_str = f"{age}d ago" if age < 9999 else "never reviewed"
            print(f"    {node['id']:<40} {age_str}")
        print()
        return 0

    # --uncalibrated: show calibration flag candidates
    if "--uncalibrated" in args:
        results = []
        node_ids = [n["id"] for n in graph["nodes"]]
        for nid in node_ids:
            r = validate_entry(nid, graph)
            if r.get("calibration_flags"):
                results.append(r)
        results.sort(key=lambda x: len(x["calibration_flags"]), reverse=True)
        print(f"\n  Calibration issues ({len(results)} entries):")
        for r in results[:20]:
            print(f"    {r['node_id']:<40} {', '.join(r['calibration_flags'])}")
        print()
        return 0

    # --all or --domain: batch validation
    if "--all" in args or "--domain" in args:
        domain = None
        if "--domain" in args:
            idx = args.index("--domain")
            if idx + 1 < len(args):
                domain = args[idx + 1]

        node_ids = scan_all_entries(domain)
        if not node_ids:
            print("  No entries found.")
            return 0

        results = [validate_entry(nid, graph) for nid in node_ids]
        results.sort(key=lambda x: x.get("score", 0))

        band_counts = {"Critical": 0, "Weak": 0, "Adequate": 0, "Strong": 0}
        for r in results:
            band_counts[r.get("band", "Critical")] += 1

        scope = f"domain={domain}" if domain else "all entries"
        print(f"\nKnowledge Validation — {scope}")
        print("=" * 55)
        print(f"  Entries: {len(results)}")
        print(f"  Strong: {band_counts['Strong']}  |  Adequate: {band_counts['Adequate']}  "
              f"|  Weak: {band_counts['Weak']}  |  Critical: {band_counts['Critical']}")

        # Show worst entries first
        critical = [r for r in results if r.get("band") in ("Critical", "Weak")]
        if critical:
            print(f"\n  Entries needing attention ({len(critical)}):")
            for r in critical[:10]:
                print(format_report(r))

        if len(results) - len(critical) > 0:
            passing = [r for r in results if r.get("band") in ("Strong", "Adequate")]
            avg = sum(r["score"] for r in passing) / len(passing)
            print(f"\n  Passing ({len(passing)} entries, avg score: {avg:.0f})")

        print(f"\n  Run /knowledge-qa for the full aggregate report.")
        print()
        return 0

    # Single entry validation
    if args and not args[0].startswith("--"):
        node_id = args[0]
        result = validate_entry(node_id, graph)
        print(f"\nValidation: {node_id}")
        print("=" * 55)
        print(format_report(result))
        if result.get("recommendations"):
            print("\n  All recommendations:")
            for rec in result["recommendations"]:
                print(f"    → {rec}")
        print()
        return 0 if result.get("band") in ("Strong", "Adequate") else 1

    print("Usage: python knowledge_validate.py [node_id | --domain D | --all | --stale | --uncalibrated | --dead-links]")
    return 1


if __name__ == "__main__":
    sys.exit(main())
