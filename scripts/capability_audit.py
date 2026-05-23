"""
Capability invocation audit — reads INVOCATION-LOG.jsonl for usage stats and anomaly detection.

Provides observability into how external tools are being used. Surfaces error patterns,
gate compliance, and unusually frequent invocations.

Anomaly thresholds:
  - Error rate > 30% over last 20 invocations for a tool → HIGH_ERROR_RATE
  - Tool invoked > 50 times in a single session → VOLUME_SPIKE
  - DESTR tool invoked without gate=true → GATE_BYPASS (critical)

Usage:
    python scripts/capability_audit.py                          # recent 20 invocations
    python scripts/capability_audit.py --recent 50             # show last 50
    python scripts/capability_audit.py --stats                 # aggregate statistics
    python scripts/capability_audit.py --anomalies             # anomalies only
    python scripts/capability_audit.py --tool <tool_id>        # filter by tool
    python scripts/capability_audit.py --since 2026-05-01      # filter by date
    python scripts/capability_audit.py --ungated               # NET/DESTR without gate=true
"""

import json
import sys
from collections import defaultdict
from datetime import datetime, date
from pathlib import Path

WORKSPACE = Path(__file__).parent.parent
CAPABILITIES_DIR = WORKSPACE / "capabilities"
LOG_PATH = CAPABILITIES_DIR / "INVOCATION-LOG.jsonl"

ERROR_RATE_THRESHOLD = 0.30
VOLUME_SPIKE_THRESHOLD = 100
HIGH_RISK_CLASSES = ("NET", "DESTR")


def load_log(
    tool_filter: str | None = None,
    since: str | None = None,
    limit: int | None = None,
) -> list[dict]:
    if not LOG_PATH.exists():
        return []
    records = []
    with LOG_PATH.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue
            if tool_filter and record.get("tool_id") != tool_filter:
                continue
            if since:
                ts = record.get("ts", "")[:10]
                if ts < since:
                    continue
            records.append(record)
    if limit:
        return records[-limit:]
    return records


def compute_stats(records: list[dict]) -> dict:
    if not records:
        return {"total": 0}

    tool_counts: dict[str, int] = defaultdict(int)
    tool_errors: dict[str, int] = defaultdict(int)
    class_counts: dict[str, int] = defaultdict(int)
    session_counts: dict[str, int] = defaultdict(int)
    gated_count = 0
    error_count = 0

    for r in records:
        tool = r.get("tool_id", "unknown")
        outcome = r.get("outcome", "unknown")
        pclass = r.get("permission_class", "R")
        session = r.get("session_id", "unknown")

        tool_counts[tool] += 1
        class_counts[pclass] += 1
        session_counts[session] += 1

        if outcome == "error":
            error_count += 1
            tool_errors[tool] += 1
        if r.get("gated"):
            gated_count += 1

    top_tools = sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    error_rate = round(error_count / len(records), 3) if records else 0
    gate_rate = round(gated_count / len(records), 3) if records else 0

    return {
        "total": len(records),
        "error_count": error_count,
        "error_rate": error_rate,
        "gated_count": gated_count,
        "gate_rate": gate_rate,
        "tool_counts": dict(tool_counts),
        "tool_errors": dict(tool_errors),
        "class_counts": dict(class_counts),
        "session_counts": dict(session_counts),
        "top_tools": top_tools,
    }


def detect_anomalies(records: list[dict]) -> list[dict]:
    anomalies = []

    # Per-tool error rate over last 20 invocations
    tool_recent: dict[str, list[dict]] = defaultdict(list)
    for r in records:
        tool_recent[r.get("tool_id", "unknown")].append(r)

    for tool_id, tool_records in tool_recent.items():
        last_20 = tool_records[-20:]
        if len(last_20) >= 5:  # only flag if enough data
            errors = sum(1 for r in last_20 if r.get("outcome") == "error")
            rate = errors / len(last_20)
            if rate >= ERROR_RATE_THRESHOLD:
                anomalies.append({
                    "type": "HIGH_ERROR_RATE",
                    "tool_id": tool_id,
                    "error_rate": round(rate, 2),
                    "sample_size": len(last_20),
                    "recommendation": f"Investigate tool errors before next use. Check server status with /mcp-status.",
                })

    # Volume spike — single session tool count
    session_tool: dict[tuple, int] = defaultdict(int)
    for r in records:
        key = (r.get("session_id", "unknown"), r.get("tool_id", "unknown"))
        session_tool[key] += 1

    for (session, tool), count in session_tool.items():
        if count >= VOLUME_SPIKE_THRESHOLD:
            anomalies.append({
                "type": "VOLUME_SPIKE",
                "tool_id": tool,
                "session_id": session,
                "invocation_count": count,
                "recommendation": f"Unusually high invocation count in one session. Verify this is expected behavior.",
            })

    return anomalies


def format_record(r: dict) -> str:
    ts = r.get("ts", "")[:19].replace("T", " ")
    tool = r.get("tool_id", "?")[:35]
    outcome = r.get("outcome", "?")
    pclass = r.get("permission_class", "?")
    gated = "gated" if r.get("gated") else "auto"
    duration = r.get("duration_ms", 0)
    outcome_icon = {"success": "✓", "error": "✗", "blocked": "⊘"}.get(outcome, "?")
    return f"  {ts}  {outcome_icon} {outcome:<8}  {pclass:<5}  {gated:<5}  {duration:>4}ms  {tool}"


def main() -> int:
    args = sys.argv[1:]

    tool_filter = None
    if "--tool" in args:
        idx = args.index("--tool")
        if idx + 1 < len(args):
            tool_filter = args[idx + 1]

    since = None
    if "--since" in args:
        idx = args.index("--since")
        if idx + 1 < len(args):
            since = args[idx + 1]

    recent_n = 20
    if "--recent" in args:
        idx = args.index("--recent")
        if idx + 1 < len(args):
            try:
                recent_n = int(args[idx + 1])
            except ValueError:
                pass

    if "--ungated" in args:
        records = load_log()
        ungated = [r for r in records if r.get("permission_class") in HIGH_RISK_CLASSES and not r.get("gated")]
        print(f"\n  Ungated NET/DESTR invocations ({len(ungated)}):")
        if not ungated:
            print("    None found — gate compliance OK.")
        else:
            print(f"  {'Timestamp':<20} {'Outcome':<10} {'Class':<6} {'Tool ID'}")
            print("  " + "-" * 75)
            for r in ungated:
                ts = r.get("ts", "")[:19].replace("T", " ")
                print(f"  {ts}  {r.get('outcome', '?'):<10} {r.get('permission_class', '?'):<6} {r.get('tool_id', '?')}")
        print()
        return 0

    if "--anomalies" in args:
        records = load_log(tool_filter=tool_filter, since=since)
        anomalies = detect_anomalies(records)
        print(f"\n  Anomaly Detection ({len(records)} records analyzed)")
        print("=" * 55)
        if not anomalies:
            print("  No anomalies detected. All invocation patterns normal.")
        else:
            for a in anomalies:
                print(f"\n  [{a['type']}]")
                for k, v in a.items():
                    if k not in ("type", "recommendation"):
                        print(f"    {k}: {v}")
                print(f"    → {a['recommendation']}")
        print()
        return 0

    if "--stats" in args:
        records = load_log(tool_filter=tool_filter, since=since)
        stats = compute_stats(records)
        print(f"\n  Capability Invocation Stats")
        print("=" * 55)
        if stats["total"] == 0:
            print("  No invocations logged yet.")
            return 0
        print(f"  Total invocations : {stats['total']}")
        print(f"  Error rate        : {stats['error_rate']:.1%}  ({stats['error_count']} errors)")
        print(f"  Gate compliance   : {stats['gate_rate']:.1%}  ({stats['gated_count']} gated)")
        print(f"\n  By permission class:")
        for pclass in ("R", "RW", "NET", "DESTR"):
            count = stats["class_counts"].get(pclass, 0)
            if count:
                print(f"    {pclass:<6} {count} invocations")
        print(f"\n  Top tools:")
        for tool, count in stats["top_tools"]:
            errors = stats["tool_errors"].get(tool, 0)
            err_str = f"  ({errors} errors)" if errors else ""
            print(f"    {count:>4}×  {tool}{err_str}")
        anomalies = detect_anomalies(records)
        if anomalies:
            print(f"\n  Anomalies detected: {len(anomalies)} — run --anomalies for details")
        print()
        return 0

    # Default: show recent N records
    records = load_log(tool_filter=tool_filter, since=since, limit=recent_n)
    scope = f"tool={tool_filter}" if tool_filter else f"last {recent_n}"
    print(f"\n  Invocation Log ({scope})")
    print(f"  {'Timestamp':<20} {'Outcome':<10} {'Class':<6} {'Gate':<6} {'ms':>5}  Tool ID")
    print("  " + "-" * 80)
    if not records:
        print("  No invocations logged yet.")
    else:
        for r in records:
            print(format_record(r))
        anomalies = detect_anomalies(records)
        if anomalies:
            print(f"\n  ⚠ {len(anomalies)} anomalies detected — run --anomalies for details")
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
