"""
Memory index generator — scans all P16 typed memory files and builds RETRIEVAL-INDEX.json.

Run after adding, modifying, or archiving any memory file.
Also regenerates the index after /mem-reconstruct creates new context files.

Usage:
    python scripts/memory_index.py           # full rebuild
    python scripts/memory_index.py --check   # check for unindexed files, no write
    python scripts/memory_index.py --stats   # show counts by type
"""

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

WORKSPACE = Path(__file__).parent.parent
MEMORY_DIR = WORKSPACE / "memory"
INDEX_PATH = MEMORY_DIR / "RETRIEVAL-INDEX.json"

TYPED_DIRS = {
    "episodic":  (MEMORY_DIR / "episodic",  "ep_"),
    "semantic":  (MEMORY_DIR / "semantic",  "sem_"),
    "decision":  (MEMORY_DIR / "decisions", "dec_"),
    "execution": (MEMORY_DIR / "execution", "exec_"),
    "failure":   (MEMORY_DIR / "failures",  "fail_"),
    "insight":   (MEMORY_DIR / "insights",  "ins_"),
    "context":   (MEMORY_DIR / "context",   "ctx_"),
}

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)


def parse_frontmatter(text: str) -> dict:
    """Extract YAML-like frontmatter fields into a dict (simple key: value parser)."""
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}
    block = match.group(1)
    result: dict = {}
    list_key = None
    list_items: list = []

    for line in block.splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        # List item
        if line.startswith("- ") and list_key:
            list_items.append(line[2:].strip())
            continue
        # New key
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


def extract_title(text: str, frontmatter: dict) -> str:
    """Extract title from frontmatter or first H1/H2 heading."""
    if frontmatter.get("title"):
        return frontmatter["title"]
    if frontmatter.get("topic"):
        return frontmatter["topic"]
    if frontmatter.get("claim"):
        return frontmatter["claim"]
    if frontmatter.get("task_type"):
        return frontmatter["task_type"]
    # First markdown heading
    for line in text.splitlines():
        if line.startswith("## ") and not line.startswith("### "):
            return line[3:].strip()
        if line.startswith("# "):
            return line[2:].strip()
    return "(no title)"


def scan_typed_dirs() -> list[dict]:
    """Scan all typed memory directories and return index entries."""
    entries = []
    for mem_type, (dir_path, prefix) in TYPED_DIRS.items():
        if not dir_path.exists():
            continue
        for file in sorted(dir_path.glob("*.md")):
            if file.name == "README.md":
                continue
            try:
                text = file.read_text(encoding="utf-8")
            except OSError:
                continue

            fm = parse_frontmatter(text)
            if fm.get("archived"):
                continue  # Skip archived entries

            # Determine timestamp field by type
            timestamp_key = {
                "episodic": "timestamp",
                "semantic": "last_updated",
                "decision": "date",
                "execution": "last_updated",
                "failure": "last_seen",
                "insight": "last_validated",
                "context": "as_of",
            }.get(mem_type, "")

            entry = {
                "id": fm.get("id", file.stem),
                "type": mem_type,
                "title": extract_title(text, fm),
                "tags": fm.get("tags", []) if isinstance(fm.get("tags"), list) else [],
                "timestamp": fm.get(timestamp_key, ""),
                "linked_to": fm.get("linked_to", []) if isinstance(fm.get("linked_to"), list) else [],
                "review_date": fm.get("review_date", ""),
                "file": str(file.relative_to(WORKSPACE)).replace("\\", "/"),
            }

            # Type-specific fields
            if mem_type == "semantic":
                entry["confidence"] = fm.get("confidence", "")
                entry["promote_candidate"] = fm.get("promote_candidate", "false") == "true"
            elif mem_type == "decision":
                entry["status"] = fm.get("status", "active")
            elif mem_type == "failure":
                entry["recurrence_count"] = int(fm.get("recurrence_count", "1"))
            elif mem_type == "insight":
                entry["insight_status"] = fm.get("status", "active")
            elif mem_type == "context":
                entry["topic_status"] = fm.get("status", "active")

            entries.append(entry)

    return entries


def build_index(entries: list[dict]) -> dict:
    by_type: dict[str, int] = {k: 0 for k in TYPED_DIRS}
    for e in entries:
        by_type[e["type"]] = by_type.get(e["type"], 0) + 1

    return {
        "_schema": "P16 Memory Retrieval Index v1.0",
        "_note": "Generated by scripts/memory_index.py. Do not edit manually.",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_entries": len(entries),
        "by_type": by_type,
        "entries": entries,
    }


def find_unindexed(entries: list[dict]) -> list[Path]:
    """Find .md files in typed dirs not present in the index."""
    indexed_files = {e["file"] for e in entries}
    unindexed = []
    for mem_type, (dir_path, _) in TYPED_DIRS.items():
        if not dir_path.exists():
            continue
        for file in dir_path.glob("*.md"):
            if file.name == "README.md":
                continue
            rel = str(file.relative_to(WORKSPACE)).replace("\\", "/")
            if rel not in indexed_files:
                unindexed.append(file)
    return unindexed


def find_past_due(entries: list[dict]) -> list[dict]:
    """Return entries whose review_date is in the past."""
    today = datetime.now(timezone.utc).date()
    overdue = []
    for e in entries:
        rd = e.get("review_date", "")
        if not rd:
            continue
        try:
            due = datetime.strptime(rd[:10], "%Y-%m-%d").date()
            if due < today:
                overdue.append(e)
        except ValueError:
            pass
    return overdue


def main() -> int:
    args = sys.argv[1:]

    entries = scan_typed_dirs()

    if "--stats" in args:
        index = build_index(entries)
        print("\nMemory Index Stats")
        print("=" * 35)
        for mtype, count in index["by_type"].items():
            print(f"  {mtype:<12} {count:>3} entries")
        print(f"  {'TOTAL':<12} {index['total_entries']:>3} entries")
        past_due = find_past_due(entries)
        if past_due:
            print(f"\n  Past review date: {len(past_due)}")
            for e in past_due[:5]:
                print(f"    [{e['type']:<10}] {e['id']}  due {e['review_date']}")
            if len(past_due) > 5:
                print(f"    ... and {len(past_due) - 5} more")
        print()
        return 0

    if "--check" in args:
        unindexed = find_unindexed(entries)
        if unindexed:
            print(f"\n  {len(unindexed)} unindexed file(s):")
            for f in unindexed:
                print(f"    {f.relative_to(WORKSPACE)}")
            print("\n  Run without --check to rebuild the index.\n")
            return 1
        print(f"  [OK] All {len(entries)} memory files are indexed.")
        return 0

    # Full rebuild
    index = build_index(entries)
    INDEX_PATH.write_text(json.dumps(index, indent=2), encoding="utf-8")

    past_due = find_past_due(entries)
    print(f"\n  [OK] RETRIEVAL-INDEX.json rebuilt: {len(entries)} entries")
    if past_due:
        print(f"  [WARN] {len(past_due)} entries past review date — run /mem-hygiene")
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
