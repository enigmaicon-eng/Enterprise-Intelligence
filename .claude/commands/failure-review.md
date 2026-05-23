---
name: failure-review
description: >-
  Dedicated failure analysis across execution trace history. Filters TRACE-INDEX.md
  for failed, partial, and abandoned outcomes, loads those traces, and surfaces a
  failure taxonomy with recurring failure modes. Feeds /pattern-mine for failure
  anti-pattern codification. Trigger on: "review failures", "what's been failing",
  "failure analysis", "what went wrong in my traces", "show abandoned traces",
  "failure patterns". Do NOT use for single trace inspection (use /exec-inspect)
  or runtime workflow recovery (use /runtime-recover).
version: 1.0
output: terminal
---

# /failure-review

Surface what has failed and why. Purpose: detect recurring failure modes — which deserve anti-pattern codification — not just generate individual post-mortems.

## When to Use

- When `/ops-dashboard` flags elevated failure density (>30% of recent episodes)
- Before a `/pattern-mine` session to identify failure anti-patterns worth codifying
- Monthly as part of the workspace health ritual
- After a difficult session where something went wrong

**Do NOT use for:**
- Single trace inspection → `/exec-inspect`
- Runtime workflow recovery → `/runtime-recover`
- All-trace keyword search → `/trace-search`

## Workflow

**Step 1 — Read TRACE-INDEX.md.**

Identify all rows with outcome = `failed`, `partial`, or `abandoned`.

If 0 matches: report "No failures in trace history" and exit cleanly.

**Step 2 — Load the failure traces.**

Sort matched rows by date descending. Load the most recent 8 trace files from `traces/executions/`. If more than 8 exist, note: "Showing [N] most recent of [total] non-completed episodes."

**Step 3 — Extract per-failure data.**

For each trace, extract:
- Goal
- Outcome
- Duration
- What Failed section content (exact text, not summarized)
- Stage at which failure occurred (which step in the Execution Sequence)
- Any pattern candidates flagged that relate to the failure mode

**Step 4 — Identify cross-failure patterns.**

Look across all loaded failures for:
- Repeated failure descriptions (same root cause language in 2+ traces)
- Repeated failure stage (same step number or step type fails in multiple traces)
- Repeated context (same tags or session type appears across failures)

A recurring mode requires 2+ instances. Do not invent patterns from a single trace.

**Step 5 — Surface the analysis.**

```
Failure Review — [YYYY-MM-DD]
══════════════════════════════

Summary
  Total non-completed : [N]  (failed: [N] / partial: [N] / abandoned: [N])
  Date range          : [earliest] – [latest]
  [If skipped:] Showing [N] most recent; [N] older not loaded.

Individual Failures
  [For each loaded trace:]

  [exec-id]  [YYYY-MM-DD]  [outcome]
    Goal    : [goal]
    Failed  : [what failed — or "⚠ 'What Failed' section is empty"]
    Stage   : [step or phase description — or "unknown"]
    Tags    : [tags]

Recurring Failure Modes
  [If 2+ share a failure mode:]
  • [Mode description]
    Seen in : [exec-id, exec-id, ...]  ([N] times)
    Stage   : [common stage — or "varies"]
    Tags    : [common tags — or "varies"]

  [If no recurring modes:]
  No recurring failure modes detected across loaded traces.

Recommended Actions
  [1-3 specific actions]
  [E.g. "Run /pattern-mine on '[mode]' — 2 instances qualify"]
  [E.g. "Update exec_YYYYMMDD_NNN — 'What Failed' section is blank"]
  [E.g. "Review [tag] traces — 3 failures in this domain"]
```

**Step 6 — Offer /pattern-mine.**

If any recurring failure mode was detected:

```
Recurring failure mode detected: "[mode description]"
Run /pattern-mine to codify as a failure anti-pattern.
Instances: [exec-id, exec-id]
```

## Quality Gate

- [ ] TRACE-INDEX.md read before any trace files loaded
- [ ] Only non-completed outcomes loaded (failed / partial / abandoned)
- [ ] "What Failed" shown as "⚠ section is empty" when blank — surfaces the documentation gap
- [ ] Recurring modes require 2+ instances — never inferred from a single trace
- [ ] At most 8 trace files loaded per invocation — not unbounded
- [ ] If 0 non-completed traces: says so and exits — does not produce an empty report
- [ ] Stage extraction attempts best-effort match; reports "unknown" rather than fabricating
