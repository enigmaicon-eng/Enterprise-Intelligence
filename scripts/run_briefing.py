"""
Daily Briefing Runner — W01
Run at session start or on demand: python scripts/run_briefing.py

Reads: execution/action-items.md, execution/follow-ups.md, memory context
Produces: 3-section briefing printed to terminal (ephemeral)
"""

import os
import sys
from datetime import date
from pathlib import Path

WORKSPACE = Path(__file__).parent.parent
sys.path.insert(0, str(WORKSPACE))

from production_ai.claude_client import workspace, load_file, log_workflow


def build_briefing_input() -> str:
    today = date.today().isoformat()
    actions = load_file("execution/action-items.md")
    followups = load_file("execution/follow-ups.md")
    return f"""Today's date: {today}

## Action Items
{actions if actions else "(none logged)"}

## Follow-Ups
{followups if followups else "(none logged)"}

Generate the daily briefing for today. Focus on: overdue and due-today items as Critical, top 3 by importance as Focus, pending follow-ups as Heads-Up."""


def main() -> None:
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY not set.")
        print("Set it with: $env:ANTHROPIC_API_KEY='sk-ant-...'")
        sys.exit(1)

    print("Generating briefing...")
    log_workflow("daily-briefing", "started")

    briefing = workspace.call(
        user_message=build_briefing_input(),
        tier="analysis",
        workflow="daily-briefing",
        prompt_name="workflows/daily-briefing",
        memory_files=["user_profile.md"],
        max_tokens=1024,
    )

    print("\n" + "=" * 50)
    print(briefing)
    print("=" * 50 + "\n")
    log_workflow("daily-briefing", "completed")


if __name__ == "__main__":
    main()
