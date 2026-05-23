"""
Observability Report Runner — W10
Usage: python scripts/run_observe.py

Reads: telemetry/api-log.jsonl, telemetry/workflow-log.jsonl, observability/quality.jsonl
Outputs: observability/dashboard.md
"""

import json
import os
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

WORKSPACE = Path(__file__).parent.parent
sys.path.insert(0, str(WORKSPACE))

from production_ai.claude_client import workspace, log_workflow

TELEMETRY_DIR = WORKSPACE / "telemetry"
OBS_DIR = WORKSPACE / "observability"
API_LOG = TELEMETRY_DIR / "api-log.jsonl"
WORKFLOW_LOG = TELEMETRY_DIR / "workflow-log.jsonl"
QUALITY_LOG = OBS_DIR / "quality.jsonl"
DASHBOARD = OBS_DIR / "dashboard.md"


def load_jsonl(path: Path, days: int = 7) -> list[dict]:
    if not path.exists():
        return []
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    records = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            rec = json.loads(line)
            ts = datetime.fromisoformat(rec.get("ts", "2000-01-01T00:00:00+00:00"))
            if ts.tzinfo is None:
                ts = ts.replace(tzinfo=timezone.utc)
            if ts >= cutoff:
                records.append(rec)
        except (json.JSONDecodeError, ValueError):
            pass
    return records


def compute_stats(api_records: list[dict]) -> dict:
    if not api_records:
        return {}

    by_workflow: dict[str, dict] = defaultdict(lambda: {
        "calls": 0, "input_tokens": 0, "output_tokens": 0,
        "cache_read": 0, "cache_write": 0, "latency_ms": 0,
    })

    for r in api_records:
        wf = r.get("workflow", "unknown")
        by_workflow[wf]["calls"] += 1
        by_workflow[wf]["input_tokens"] += r.get("input_tokens", 0)
        by_workflow[wf]["output_tokens"] += r.get("output_tokens", 0)
        by_workflow[wf]["cache_read"] += r.get("cache_read_tokens", 0)
        by_workflow[wf]["cache_write"] += r.get("cache_write_tokens", 0)
        by_workflow[wf]["latency_ms"] += r.get("latency_ms", 0)

    total_input = sum(r.get("input_tokens", 0) for r in api_records)
    total_cache_read = sum(r.get("cache_read_tokens", 0) for r in api_records)
    cache_hit_rate = total_cache_read / max(total_input, 1)

    return {
        "total_calls": len(api_records),
        "cache_hit_rate": cache_hit_rate,
        "by_workflow": dict(by_workflow),
        "total_tokens": total_input + sum(r.get("output_tokens", 0) for r in api_records),
    }


def build_observe_input(api_records: list[dict], wf_records: list[dict], quality_records: list[dict]) -> str:
    stats = compute_stats(api_records)

    lines = [f"Observability Report Input — Week ending {date.today().isoformat()}\n"]

    lines.append(f"## API Telemetry (last 7 days)")
    lines.append(f"Total calls: {stats.get('total_calls', 0)}")
    lines.append(f"Cache hit rate: {stats.get('cache_hit_rate', 0):.1%}")
    lines.append(f"Total tokens: {stats.get('total_tokens', 0):,}")

    if stats.get("by_workflow"):
        lines.append("\n### Calls by workflow:")
        for wf, data in sorted(stats["by_workflow"].items(), key=lambda x: -x[1]["calls"]):
            avg_latency = data["latency_ms"] // max(data["calls"], 1)
            lines.append(f"  {wf}: {data['calls']} calls, {data['input_tokens']:,} input tokens, {avg_latency}ms avg")

    lines.append(f"\n## Workflow Events (last 7 days)")
    if wf_records:
        wf_counts = defaultdict(int)
        for r in wf_records:
            wf_counts[r.get("workflow", "unknown")] += 1
        for wf, count in sorted(wf_counts.items(), key=lambda x: -x[1]):
            lines.append(f"  {wf}: {count} events")
    else:
        lines.append("  (no workflow events logged)")

    lines.append(f"\n## Quality Ratings")
    if quality_records:
        for r in quality_records[-20:]:
            lines.append(f"  {r.get('prompt', '?')} v{r.get('version', '?')}: {r.get('score', '?')}/5 — {r.get('note', '')}")
    else:
        lines.append("  (no quality ratings logged this week)")

    return "\n".join(lines)


def main() -> None:
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY not set.")
        sys.exit(1)

    print("Running observability report...")
    log_workflow("observe", "started")

    api_records = load_jsonl(API_LOG)
    wf_records = load_jsonl(WORKFLOW_LOG)
    quality_records = load_jsonl(QUALITY_LOG, days=7)

    observe_input = build_observe_input(api_records, wf_records, quality_records)

    dashboard = workspace.call(
        user_message=observe_input,
        tier="analysis",
        workflow="observe",
        prompt_name="system/analyst",
        include_memory=False,
        max_tokens=2000,
        extra_system="""Generate the observability dashboard. Include:
1. Health summary (1 sentence)
2. Token cost by workflow (table)
3. Cache hit rate (status: good >60%, warn 40-60%, bad <40%)
4. Latency outliers (workflows >5s average)
5. Quality issues (prompts scoring <3.5/5)
6. Dead workflows (not run in 7+ days)
7. Action items (prioritized list of what to fix)

Format as markdown. Be specific — name the workflows and numbers.""",
    )

    OBS_DIR.mkdir(parents=True, exist_ok=True)
    DASHBOARD.write_text(dashboard, encoding="utf-8")
    print(f"Written: observability/dashboard.md")

    log_workflow("observe", "completed", {"api_calls_analyzed": len(api_records)})
    print("\nObservability report complete.")


if __name__ == "__main__":
    main()
