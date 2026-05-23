"""
run_recall.py — Grep-based knowledge retrieval for the workspace knowledge base.

Usage:
    python scripts/run_recall.py "query terms"
    python scripts/run_recall.py "query terms" --domain technical
    python scripts/run_recall.py "query terms" --domain pm --limit 5
"""

import argparse
import subprocess
import sys
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).parent.parent
KNOWLEDGE_DIR = WORKSPACE_ROOT / "knowledge"

DOMAINS = ["pm", "strategy", "systems", "technical", "operations", "patterns", "decisions", "clusters"]


def grep_knowledge(query: str, domain: str | None = None, limit: int = 10) -> list[dict]:
    search_path = KNOWLEDGE_DIR / domain if domain else KNOWLEDGE_DIR
    if not search_path.exists():
        print(f"[recall] Path not found: {search_path}")
        return []

    try:
        result = subprocess.run(
            ["rg", "--ignore-case", "--line-number", "--with-filename", query, str(search_path)],
            capture_output=True,
            text=True,
        )
        lines = result.stdout.strip().split("\n") if result.stdout.strip() else []
    except FileNotFoundError:
        result = subprocess.run(
            ["grep", "-rn", "-i", query, str(search_path)],
            capture_output=True,
            text=True,
        )
        lines = result.stdout.strip().split("\n") if result.stdout.strip() else []

    matches = []
    seen_files = set()

    for line in lines:
        if not line:
            continue
        parts = line.split(":", 2)
        if len(parts) < 3:
            continue
        file_path, line_num, content = parts[0], parts[1], parts[2].strip()
        rel_path = Path(file_path).relative_to(WORKSPACE_ROOT)

        if file_path not in seen_files:
            seen_files.add(file_path)

        matches.append({
            "file": str(rel_path),
            "line": line_num,
            "content": content,
        })

        if len(matches) >= limit * 3:
            break

    return matches[:limit]


def read_file_excerpt(file_path: str, target_line: int, context_lines: int = 5) -> str:
    full_path = WORKSPACE_ROOT / file_path
    try:
        lines = full_path.read_text(encoding="utf-8").split("\n")
        start = max(0, int(target_line) - 1 - context_lines)
        end = min(len(lines), int(target_line) + context_lines)
        excerpt_lines = lines[start:end]
        return "\n".join(excerpt_lines)
    except Exception:
        return ""


def check_index_first(query: str) -> list[str]:
    index_path = KNOWLEDGE_DIR / "KNOWLEDGE-INDEX.md"
    if not index_path.exists():
        return []

    content = index_path.read_text(encoding="utf-8").lower()
    query_terms = query.lower().split()
    matching_lines = []

    for line in index_path.read_text(encoding="utf-8").split("\n"):
        if any(term in line.lower() for term in query_terms):
            matching_lines.append(line.strip())

    return [l for l in matching_lines if l and not l.startswith("#")][:10]


def main():
    parser = argparse.ArgumentParser(description="Search the knowledge base")
    parser.add_argument("query", help="Search query — keywords, concept name, or question")
    parser.add_argument("--domain", choices=DOMAINS, help="Limit search to a specific domain")
    parser.add_argument("--limit", type=int, default=10, help="Maximum number of results (default: 10)")
    parser.add_argument("--excerpt", action="store_true", help="Show file excerpt around each match")
    args = parser.parse_args()

    print(f"\n[recall] Query: '{args.query}'")
    if args.domain:
        print(f"[recall] Domain filter: {args.domain}")
    print()

    index_hits = check_index_first(args.query)
    if index_hits:
        print("=== Index Matches ===")
        for hit in index_hits:
            print(f"  {hit}")
        print()

    matches = grep_knowledge(args.query, domain=args.domain, limit=args.limit)

    if not matches:
        print("[recall] No matches found in knowledge base.")
        print()
        print("Suggestions:")
        print("  - Try broader search terms")
        print("  - Check a different domain with --domain")
        print("  - Run /learn to capture this topic if it doesn't exist yet")
        return

    seen_files: dict[str, list] = {}
    for m in matches:
        seen_files.setdefault(m["file"], []).append(m)

    print(f"=== Matches ({len(matches)} results across {len(seen_files)} files) ===")
    print()

    for file_path, file_matches in seen_files.items():
        print(f"  {file_path}")
        for m in file_matches[:3]:
            print(f"    L{m['line']}: {m['content'][:120]}")
            if args.excerpt:
                excerpt = read_file_excerpt(m["file"], m["line"])
                if excerpt:
                    print()
                    for eline in excerpt.split("\n"):
                        print(f"      | {eline}")
                    print()
        print()

    print(f"[recall] To read a file: use the Read tool with the full path above.")
    print(f"[recall] To deepen: /synthesize on this topic, or /recall with --excerpt flag.")


if __name__ == "__main__":
    main()
