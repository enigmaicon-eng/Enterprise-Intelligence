---
name: ops-dashboard
description: >-
  Integrated operational dashboard combining execution trace history, runtime
  state, pattern coverage, and recommended next actions. Reads TRACE-INDEX.md
  and runtime/state/ files. Terminal output only. Trigger on: "ops dashboard",
  "operational overview", "how are things going operationally", "execution
  health", "operational status", "what should I do next". Do NOT use for API
  cost analysis (use /observe), active workflow status (use /runtime-status),
  or context health (use /context-audit).
version: 1.0
output: terminal
---

# /ops-dashboard

Integrated operational view: execution history health, runtime state, pattern coverage, and next best actions. One command to understand where the workspace stands operationally.

## When to Use

- Start of a week or work block to orient
- After returning from a break (>3 days) to re-establish operational picture
- Before running `/weekly` to pre-populate context
- When you want to know: "Am I capturing enough? Are patterns building? What's failing?"

**Do NOT use for:**
- API cost and cache rate analysis → `/observe`
- Active workflow status → `/runtime-status`
- Context health audit → `/context-audit`

## Workflow

**Step 1 — Read state files in parallel.**

Read:
- `traces/TRACE-INDEX.md`
- `runtime/state/active-workflows.json`
- `runtime/state/workflow-history.json`

**Step 2 — Compute metrics from TRACE-INDEX.md.**

Execution Episodes table:
- Total row count
- Rows from last 30 days: count by outcome (completed / partial / abandoned / failed)
- Reuse potential distribution: count high / medium / low
- Last episode date

Patterns table:
- Total count by confidence level (emerging / confirmed / high)

Primitives table:
- Total count

Journal Entries table:
- Count for last 7 days
- Last entry date

**Step 3 — Compute runtime metrics.**

From active-workflows.json: count active workflows by status.
From workflow-history.json: count completed, failed, abandoned in last 7 days; identify last completed workflow.

**Step 4 — Assess operational signals.**

Fire each flag if condition is true:

| Flag | Condition |
|------|-----------|
| LOW CAPTURE | Last trace episode > 7 days ago |
| PATTERN DEBT | 5+ total episodes AND 0 patterns codified |
| FAILURE DENSITY | >30% of last-30-day episodes are failed or partial |
| SPARSE HISTORY | <3 total episodes (recall not yet useful) |
| JOURNAL GAP | 0 journal entries in last 7 days |
| STALE JOURNAL | Last journal entry > 14 days ago |

**Step 5 — Surface the dashboard.**

```
Operational Dashboard — [YYYY-MM-DD]
══════════════════════════════════════

Runtime
  Active workflows : [N]  ([STATUS breakdown if any active])
  Last completed   : [workflow name or "none"]  ([date or "—"])
  7-day history    : [N] completed  [N] failed/abandoned

Execution Trace History
  Total episodes   : [N]  (since [earliest date or "none"])
  Last 30 days     : [N] completed  [N] partial  [N] failed  [N] abandoned
  High-reuse       : [N] captured
  Journal entries  : [N] this week  (last: [date or "—"])

Pattern Coverage
  Patterns         : [N]  ([N] emerging / [N] confirmed / [N] high)
  Primitives       : [N]

Operational Signals
  [For each flag that fired:]
  ⚠  [FLAG NAME]: [specific description with dates/counts]
  [If no flags:]
  ✓  No operational flags.

Recommended Actions
  [1-3 specific next actions based on what was found]
  [E.g. "Run /trace-capture — last episode was 12 days ago"]
  [E.g. "Run /pattern-mine — 5 episodes with 0 patterns"]
  [E.g. "Run /workflow-journal — 9 days since last entry"]
```

**Step 6 — Offer drill-down.**

```
Drill down:
  /exec-inspect <exec-id>  — inspect a specific trace
  /failure-review          — analyze failure patterns
  /retrieval-diag          — check retrieval system health
  /skill-stats             — session type and tag distribution
```

## Quality Gate

- [ ] TRACE-INDEX.md and both runtime state files read before any metrics computed
- [ ] Metrics show "0" or "none" when tables are empty — never left blank
- [ ] Flags fired only when thresholds actually crossed — not preemptively
- [ ] Recommended actions are specific (a verb phrase naming a skill or file)
- [ ] Output fits in terminal — no raw file dumps
- [ ] Last date shown wherever "never recorded" is a meaningful signal
