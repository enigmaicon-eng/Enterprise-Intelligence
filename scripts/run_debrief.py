"""
Meeting Debrief Runner — W03
Usage: python scripts/run_debrief.py <meeting-file-name>
Example: python scripts/run_debrief.py 2026-05-21-product-sync.md

Input: meeting-intelligence/raw/<file>
Outputs:
  - meeting-intelligence/processed/<file>
  - Appends to execution/action-items.md
  - Appends to decision-frameworks/decisions-log.md
"""

import os
import sys
from datetime import date
from pathlib import Path

WORKSPACE = Path(__file__).parent.parent
sys.path.insert(0, str(WORKSPACE))

from production_ai.claude_client import workspace, log_workflow

RAW_DIR = WORKSPACE / "meeting-intelligence" / "raw"
PROCESSED_DIR = WORKSPACE / "meeting-intelligence" / "processed"
ACTION_ITEMS = WORKSPACE / "execution" / "action-items.md"
DECISIONS_LOG = WORKSPACE / "decision-frameworks" / "decisions-log.md"


def main() -> None:
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY not set.")
        sys.exit(1)

    if len(sys.argv) < 2:
        print("Usage: python scripts/run_debrief.py <meeting-file-name>")
        print("Example: python scripts/run_debrief.py 2026-05-21-product-sync.md")
        sys.exit(1)

    filename = sys.argv[1]
    raw_path = RAW_DIR / filename

    if not raw_path.exists():
        raw_files = list(RAW_DIR.glob("*.md"))
        print(f"ERROR: {raw_path} not found.")
        if raw_files:
            print(f"Available files in meeting-intelligence/raw/:")
            for f in sorted(raw_files)[-5:]:
                print(f"  {f.name}")
        sys.exit(1)

    content = raw_path.read_text(encoding="utf-8")
    log_workflow("meeting-debrief", "started", {"file": filename})
    print(f"Processing: {filename}")

    # Stage 1: Structure with Haiku (fast pass)
    print("  Stage 1/2: Structuring transcript (Haiku)...")
    structured = workspace.call(
        user_message=f"Structure this meeting transcript:\n\n{content}",
        tier="capture",
        workflow="meeting-structure",
        prompt_name="workflows/meeting-structure",
        include_memory=False,
        max_tokens=2048,
    )

    # Stage 2: Deep analysis with Sonnet
    print("  Stage 2/2: Analyzing and extracting intelligence (Sonnet)...")
    analysis = workspace.call(
        user_message=structured,
        tier="analysis",
        workflow="meeting-debrief",
        prompt_name="workflows/meeting-debrief",
        memory_files=["user_profile.md"],
        max_tokens=3000,
    )

    # Write processed output
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    output_path = PROCESSED_DIR / filename
    output_path.write_text(analysis, encoding="utf-8")
    print(f"  Written: meeting-intelligence/processed/{filename}")

    # Mark raw file as processed
    updated_raw = f"<!-- processed: {date.today().isoformat()} -->\n{content}"
    raw_path.write_text(updated_raw, encoding="utf-8")

    # Extract and append action items (simple heuristic: lines with "- [ ]")
    action_lines = [ln for ln in analysis.splitlines() if "- [ ]" in ln]
    if action_lines:
        ACTION_ITEMS.parent.mkdir(parents=True, exist_ok=True)
        with open(ACTION_ITEMS, "a", encoding="utf-8") as f:
            f.write(f"\n\n### From {filename} ({date.today().isoformat()})\n")
            f.write("\n".join(action_lines) + "\n")
        print(f"  Appended {len(action_lines)} action items to execution/action-items.md")

    log_workflow("meeting-debrief", "completed", {"file": filename, "action_items": len(action_lines)})
    print("\nDebrief complete. Review: meeting-intelligence/processed/" + filename)


if __name__ == "__main__":
    main()
