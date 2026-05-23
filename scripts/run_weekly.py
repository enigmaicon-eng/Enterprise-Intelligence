"""
Weekly Review Runner — W05
Usage: python scripts/run_weekly.py [--force]

Reads: processed meetings (this week), action items, decisions, knowledge index, memory
Outputs: reviews/weekly/YYYY-WW.md
Optional: synthesis/weekly-insights/YYYY-WW.md (if synthesis_needed flagged in output)
"""

import os
import sys
from datetime import date, timedelta
from pathlib import Path

WORKSPACE = Path(__file__).parent.parent
sys.path.insert(0, str(WORKSPACE))

from production_ai.claude_client import workspace, log_workflow

PROCESSED_DIR = WORKSPACE / "meeting-intelligence" / "processed"
REVIEWS_DIR = WORKSPACE / "reviews" / "weekly"
SYNTHESIS_DIR = WORKSPACE / "synthesis" / "weekly-insights"
ACTION_ITEMS = WORKSPACE / "execution" / "action-items.md"
DECISIONS_LOG = WORKSPACE / "decision-frameworks" / "decisions-log.md"
KNOWLEDGE_INDEX = WORKSPACE / "knowledge" / "KNOWLEDGE-INDEX.md"


def get_week_range() -> tuple[date, date]:
    today = date.today()
    start = today - timedelta(days=today.weekday())  # Monday
    end = start + timedelta(days=6)
    return start, end


def load_this_weeks_meetings(start: date, end: date) -> str:
    parts = []
    for path in sorted(PROCESSED_DIR.glob("*.md")):
        name = path.stem
        if len(name) >= 10:
            try:
                file_date = date.fromisoformat(name[:10])
                if start <= file_date <= end:
                    parts.append(f"### {name}\n{path.read_text(encoding='utf-8')}")
            except ValueError:
                pass

    return "\n\n---\n\n".join(parts) if parts else "(no meetings this week)"


def build_weekly_input(start: date, end: date) -> str:
    meetings = load_this_weeks_meetings(start, end)

    action_items = ""
    if ACTION_ITEMS.exists():
        action_items = ACTION_ITEMS.read_text(encoding="utf-8")

    decisions = ""
    if DECISIONS_LOG.exists():
        decisions = DECISIONS_LOG.read_text(encoding="utf-8")

    knowledge = ""
    if KNOWLEDGE_INDEX.exists():
        knowledge = KNOWLEDGE_INDEX.read_text(encoding="utf-8")

    return f"""Week: {start.isoformat()} to {end.isoformat()}

## Meetings This Week
{meetings}

## Action Items (all open)
{action_items if action_items else "(none)"}

## Decisions This Week
{decisions if decisions else "(none logged)"}

## Knowledge Index (entries added this week)
{knowledge if knowledge else "(none)"}

Generate the weekly review. Follow the output format from the prompt exactly. Include synthesis_needed: true at the end if cross-domain synthesis is warranted."""


def main() -> None:
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY not set.")
        sys.exit(1)

    start, end = get_week_range()
    iso_week = f"{start.year}-{start.isocalendar()[1]:02d}"

    output_path = REVIEWS_DIR / f"{iso_week}.md"
    if output_path.exists() and "--force" not in sys.argv:
        print(f"Weekly review already exists: reviews/weekly/{iso_week}.md")
        print("Run with --force to regenerate.")
        sys.exit(0)

    print(f"Running weekly review for week {iso_week} ({start} – {end})...")
    log_workflow("weekly-review", "started", {"week": iso_week})

    review = workspace.call(
        user_message=build_weekly_input(start, end),
        tier="analysis",
        workflow="weekly-review",
        prompt_name="workflows/weekly-review",
        memory_files=["user_profile.md", f"project_workspace_blueprint.md"],
        max_tokens=5000,
    )

    REVIEWS_DIR.mkdir(parents=True, exist_ok=True)
    output_path.write_text(review, encoding="utf-8")
    print(f"Written: reviews/weekly/{iso_week}.md")

    # Check if synthesis is warranted
    if "synthesis_needed: true" in review.lower():
        print("\nSynthesis flagged. Running weekly synthesis (Opus)...")
        synthesis = workspace.call_with_thinking(
            user_message=review,
            budget_tokens=8000,
            workflow="weekly-synthesis",
        )
        SYNTHESIS_DIR.mkdir(parents=True, exist_ok=True)
        synth_path = SYNTHESIS_DIR / f"{iso_week}.md"
        synth_path.write_text(synthesis, encoding="utf-8")
        print(f"Written: synthesis/weekly-insights/{iso_week}.md")

    log_workflow("weekly-review", "completed", {"week": iso_week})
    print("\nWeekly review complete.")


if __name__ == "__main__":
    main()
