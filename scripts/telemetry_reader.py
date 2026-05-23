"""
Telemetry Reader — quick analysis of api-log.jsonl and workflow-log.jsonl.
Usage: python scripts/telemetry_reader.py [--days N] [--workflow <name>]

Prints a summary to terminal. Does not call the API.
"""

import json
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

WORKSPACE = Path(__file__).parent.parent
API_LOG = WORKSPACE / "telemetry" / "api-log.jsonl"
WORKFLOW_LOG = WORKSPACE / "telemetry" / "workflow-log.jsonl"

# Approximate cost per 1M tokens (USD) as of 2026
COST_PER_M: dict[str, dict[str, float]] = {
    "claude-haiku-4-5-20251001": {"input": 0.80, "output": 4.00},
    "claude-sonnet-4-6":         {"input": 3.00, "output": 15.00},
    "claude-opus-4-7":           {"input": 15.00, "output": 75.00},
}


def parse_args() -> tuple[int, str | None]:
    days = 7
    workflow = None
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == "--days" and i + 1 < len(args):
            days = int(args[i + 1]); i += 2
        elif args[i] == "--workflow" and i + 1 < len(args):
            workflow = args[i + 1]; i += 2
        else:
            i += 1
    return days, workflow


def load_jsonl(path: Path, days: int, workflow_filter: str | None) -> list[dict]:
    if not path.exists():
        return []
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    records = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
            ts_str = rec.get("ts", "")
            ts = datetime.fromisoformat(ts_str)
            if ts.tzinfo is None:
                ts = ts.replace(tzinfo=timezone.utc)
            if ts < cutoff:
                continue
            if workflow_filter and rec.get("workflow") != workflow_filter:
                continue
            records.append(rec)
        except (json.JSONDecodeError, ValueError):
            pass
    return records


def compute_cost(model: str, input_tok: int, output_tok: int, cache_read: int) -> float:
    rates = COST_PER_M.get(model, {"input": 3.0, "output": 15.0})
    effective_input = max(0, input_tok - cache_read)
    cache_cost = cache_read * rates["input"] * 0.10 / 1_000_000  # cache read = 10% of input
    return (effective_input * rates["input"] + output_tok * rates["output"]) / 1_000_000 + cache_cost


def main() -> None:
    days, workflow_filter = parse_args()
    print(f"\n=== Telemetry Summary (last {days} days{' — ' + workflow_filter if workflow_filter else ''}) ===\n")

    api_records = load_jsonl(API_LOG, days, workflow_filter)

    if not api_records:
        print("  No API records found for this period.")
    else:
        by_workflow: dict[str, dict] = defaultdict(lambda: {
            "calls": 0, "input": 0, "output": 0,
            "cache_read": 0, "cache_write": 0, "latency": 0, "cost": 0.0,
        })

        for r in api_records:
            wf = r.get("workflow", "unknown")
            inp = r.get("input_tokens", 0)
            out = r.get("output_tokens", 0)
            cr = r.get("cache_read_tokens", 0)
            by_workflow[wf]["calls"] += 1
            by_workflow[wf]["input"] += inp
            by_workflow[wf]["output"] += out
            by_workflow[wf]["cache_read"] += cr
            by_workflow[wf]["cache_write"] += r.get("cache_write_tokens", 0)
            by_workflow[wf]["latency"] += r.get("latency_ms", 0)
            by_workflow[wf]["cost"] += compute_cost(r.get("model", ""), inp, out, cr)

        total_cost = sum(d["cost"] for d in by_workflow.values())
        total_input = sum(d["input"] for d in by_workflow.values())
        total_cache = sum(d["cache_read"] for d in by_workflow.values())
        hit_rate = total_cache / max(total_input, 1)

        print(f"  Total API calls:    {len(api_records)}")
        print(f"  Total input tokens: {total_input:,}")
        print(f"  Cache hit rate:     {hit_rate:.1%} (target: >60%)")
        print(f"  Estimated cost:     ${total_cost:.4f}")

        print(f"\n  By workflow:")
        for wf, d in sorted(by_workflow.items(), key=lambda x: -x[1]["cost"]):
            avg_lat = d["latency"] // max(d["calls"], 1)
            print(f"    {wf:<30} {d['calls']:>3} calls  ${d['cost']:.4f}  {avg_lat:>5}ms avg")

    # Workflow log
    wf_records = load_jsonl(WORKFLOW_LOG, days, workflow_filter)
    if wf_records:
        print(f"\n  Workflow events: {len(wf_records)}")
        failures = [r for r in wf_records if r.get("status") == "failed"]
        if failures:
            print(f"  FAILURES ({len(failures)}):")
            for f in failures:
                print(f"    {f.get('workflow')} — {f.get('error', 'unknown error')}")
    else:
        print(f"\n  No workflow events found.")

    print()


if __name__ == "__main__":
    main()
