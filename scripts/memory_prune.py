"""
Memory pruning manifest generator — surfaces candidates for archival or deletion.

Does NOT modify any files. Generates a human-readable manifest that the operator
reviews and executes manually (or via /mem-hygiene).

Usage:
    python scripts/memory_prune.py            # generate prune manifest
    python scripts/memory_prune.py --preview  # print to stdout, no file write
"""

import json
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

WORKSPACE = Path(__file__).parent.parent
MEMORY_DIR = WORKSPACE / "memory"
INDEX_PATH = MEMORY_DIR / "RETRIEVAL-INDEX.json"
ARCHIVE_LOG = MEMORY_DIR / "archive" / "ARCHIVE-LOG.md"

# Pruning thresholds
EPISODIC_ARCHIVE_DAYS = 90     # Unlinked episodic > 90d → archive candidate
SEMANTIC_ARCHIVE_DAYS = 60     # confidence=low + no update > 60d → archive candidate
FAILURE_ARCHIVE_DAYS = 90      # recurrence=0 + first_seen > 90d → archive candidate
CONTEXT_REGEN_DAYS = 30        # Context reconstruction > 30d on active topic → regen needed
OVERDUE_THRESHOLD_DAYS = 14    # Past review_date by > 14d → flag


def load_index() -> dict:
    if not INDEX_PATH.exists():
        print("RETRIEVAL-INDEX.json not found. Run: python scripts/memory_index.py")
        sys.exit(1)
    return json.loads(INDEX_PATH.read_text(encoding="utf-8"))


def days_ago(date_str: str) -> int | None:
    if not date_str:
        return None
    try:
        dt = datetime.strptime(date_str[:10], "%Y-%m-%d")
        return (datetime.now() - dt).days
    except ValueError:
        return None


def generate_manifest(entries: list[dict]) -> dict:
    today = datetime.now(timezone.utc).date()
    candidates: list[dict] = []
    overdue: list[dict] = []
    regen_needed: list[dict] = []
    promotion_candidates: list[dict] = []

    for e in entries:
        etype = e["type"]
        links = e.get("linked_to", [])
        rd_str = e.get("review_date", "")

        # --- Overdue reviews ---
        if rd_str:
            try:
                rd = datetime.strptime(rd_str[:10], "%Y-%m-%d").date()
                if (today - rd).days > OVERDUE_THRESHOLD_DAYS:
                    overdue.append({
                        "id": e["id"],
                        "type": etype,
                        "title": e["title"],
                        "review_date": rd_str,
                        "days_overdue": (today - rd).days,
                        "file": e["file"],
                    })
            except ValueError:
                pass

        # --- Episodic: unlinked + old ---
        if etype == "episodic":
            age = days_ago(e.get("timestamp", ""))
            if age and age > EPISODIC_ARCHIVE_DAYS and not links:
                candidates.append({
                    "id": e["id"],
                    "type": etype,
                    "title": e["title"],
                    "reason": f"Unlinked episodic entry, {age} days old",
                    "suggested_action": "archive",
                    "file": e["file"],
                })

        # --- Semantic: low confidence + old ---
        elif etype == "semantic":
            if e.get("confidence") == "low":
                age = days_ago(e.get("timestamp", ""))
                if age and age > SEMANTIC_ARCHIVE_DAYS:
                    candidates.append({
                        "id": e["id"],
                        "type": etype,
                        "title": e["title"],
                        "reason": f"confidence=low, {age} days since update",
                        "suggested_action": "archive or delete",
                        "file": e["file"],
                    })
            # Promotion candidates
            if e.get("promote_candidate"):
                promotion_candidates.append({
                    "id": e["id"],
                    "title": e["title"],
                    "file": e["file"],
                    "action": "promote to knowledge/<domain>/",
                })

        # --- Failure: recurrence=0 + old ---
        elif etype == "failure":
            recurrence = e.get("recurrence_count", 1)
            age = days_ago(e.get("timestamp", ""))
            if recurrence == 1 and age and age > FAILURE_ARCHIVE_DAYS:
                candidates.append({
                    "id": e["id"],
                    "type": etype,
                    "title": e["title"],
                    "reason": f"Single occurrence, {age} days old — may not be a real pattern",
                    "suggested_action": "archive",
                    "file": e["file"],
                })

        # --- Context: old on active topic ---
        elif etype == "context":
            topic_status = e.get("topic_status", "active")
            age = days_ago(e.get("timestamp", ""))
            if topic_status == "active" and age and age > CONTEXT_REGEN_DAYS:
                regen_needed.append({
                    "id": e["id"],
                    "title": e["title"],
                    "age_days": age,
                    "file": e["file"],
                    "action": "run /mem-reconstruct to regenerate",
                })

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "overdue_reviews": overdue,
        "archive_candidates": candidates,
        "regen_needed": regen_needed,
        "promotion_candidates": promotion_candidates,
        "totals": {
            "overdue": len(overdue),
            "archive_candidates": len(candidates),
            "regen_needed": len(regen_needed),
            "promotion_candidates": len(promotion_candidates),
        },
    }


def format_manifest(m: dict) -> str:
    lines = [
        f"# Memory Prune Manifest",
        f"## Generated: {m['generated_at'][:10]}",
        "",
        "**Operator: review each section and take action manually.**",
        "This file does not modify anything. Run scripts after reviewing.",
        "",
        "---",
        "",
        f"## Summary",
        f"| Category | Count |",
        f"|----------|-------|",
        f"| Overdue reviews | {m['totals']['overdue']} |",
        f"| Archive candidates | {m['totals']['archive_candidates']} |",
        f"| Context reconstructions needing regen | {m['totals']['regen_needed']} |",
        f"| Semantic entries ready to promote | {m['totals']['promotion_candidates']} |",
        "",
    ]

    if m["overdue_reviews"]:
        lines += ["---", "", "## Overdue Reviews", ""]
        for e in m["overdue_reviews"]:
            lines.append(f"- **{e['id']}** ({e['type']}) — {e['title']}")
            lines.append(f"  Review date: {e['review_date']} ({e['days_overdue']} days overdue)")
            lines.append(f"  File: `{e['file']}`")
            lines.append("")

    if m["archive_candidates"]:
        lines += ["---", "", "## Archive Candidates", ""]
        for e in m["archive_candidates"]:
            lines.append(f"- **{e['id']}** ({e['type']}) — {e['title']}")
            lines.append(f"  Reason: {e['reason']}")
            lines.append(f"  Suggested: {e['suggested_action']}")
            lines.append(f"  File: `{e['file']}`")
            lines.append("")

    if m["regen_needed"]:
        lines += ["---", "", "## Context Reconstructions Needing Regeneration", ""]
        for e in m["regen_needed"]:
            lines.append(f"- **{e['id']}** — {e['title']} ({e['age_days']} days old)")
            lines.append(f"  Action: `{e['action']}`")
            lines.append(f"  File: `{e['file']}`")
            lines.append("")

    if m["promotion_candidates"]:
        lines += ["---", "", "## Semantic → Knowledge Promotion Candidates", ""]
        for e in m["promotion_candidates"]:
            lines.append(f"- **{e['id']}** — {e['title']}")
            lines.append(f"  Action: {e['action']}")
            lines.append(f"  File: `{e['file']}`")
            lines.append("")

    return "\n".join(lines)


def main() -> int:
    args = sys.argv[1:]
    index = load_index()
    entries = index.get("entries", [])
    manifest = generate_manifest(entries)
    formatted = format_manifest(manifest)

    if "--preview" in args or not entries:
        print(formatted)
        return 0

    # Write to archive dir
    archive_dir = MEMORY_DIR / "archive"
    archive_dir.mkdir(exist_ok=True)
    date_str = datetime.now().strftime("%Y%m%d")
    out_path = archive_dir / f"PRUNE-MANIFEST-{date_str}.md"
    out_path.write_text(formatted, encoding="utf-8")

    t = manifest["totals"]
    print(f"\n  [OK] Prune manifest written: {out_path.name}")
    print(f"       Overdue: {t['overdue']}  |  Archive candidates: {t['archive_candidates']}  |  Regen: {t['regen_needed']}  |  Promote: {t['promotion_candidates']}")
    print(f"\n  Review the manifest and take action manually.\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
