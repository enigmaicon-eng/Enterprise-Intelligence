---
name: retrieval-diag
description: >-
  Diagnostics for the execution trace retrieval system and memory recall layer.
  Reads TRACE-INDEX.md and surfaces: index health, temporal coverage gaps, pattern
  confidence distribution, recall readiness score, open pattern candidates, and
  journal continuity. Trigger on: "retrieval diagnostics", "is my trace index
  healthy", "check retrieval system", "recall readiness", "pattern coverage",
  "memory recall diagnostics", "trace index health". Do NOT use for context layer
  health (use /context-audit) or API/cost diagnostics (use /observe).
version: 1.0
output: terminal
---

# /retrieval-diag

Diagnose the health of the execution trace retrieval system. Answers: "Can /trace-recall actually help me? Is the index complete? Are patterns being built from the evidence?"

## When to Use

- When `/trace-recall` returns no relevant results and you suspect coverage gaps
- Monthly as part of the workspace health ritual
- After a batch of new traces to verify they're indexed correctly
- Before starting a `/pattern-mine` session to see what's ready to codify

**Do NOT use for:**
- Context engineering layer health → `/context-audit`
- API cost and cache diagnostics → `/observe`
- Searching for specific traces → `/trace-search`

## Workflow

**Step 1 — Read TRACE-INDEX.md.**

Parse all four tables:
- Execution Episodes (ID, Date, Type, Goal, Outcome, Reuse, Tags)
- Journal Entries (Date, Focus, Insight, Tags)
- Patterns (ID, Name, Type, Confidence, Instances, Tags)
- Primitives (ID, Name, Type, Duration, Tags)

**Step 2 — Diagnose the Execution Episodes table.**

- Total count
- Date range (earliest to latest)
- Gap detection: sort episodes by date; identify any consecutive gap > 14 days. Record the gap date range.
- Type distribution: which of the 6 types (workflow/debug/architecture/pm-session/synthesis/build) are present vs. absent
- Outcome distribution: count completed / partial / abandoned / failed
- Reuse potential distribution: count high / medium / low

Recall readiness classification:
- 0–2 episodes → "Insufficient: /trace-recall will not find meaningful matches"
- 3–9 episodes → "Minimal: recall works but coverage is narrow"
- 10–29 episodes → "Adequate: good recall coverage"
- 30+ episodes → "Rich: strong recall and pattern mining potential"

**Step 3 — Diagnose the Journal Entries table.**

- Total count
- Last entry date
- Days since last entry
- Gap flag: >7 days → Stale; >30 days → Absent

**Step 4 — Diagnose the Patterns table.**

- Total patterns
- Confidence distribution: count emerging / confirmed / high
- Instances range: min to max instances across patterns
- Orphan check: any pattern with instances = 0 or source_traces not populated

**Step 5 — Diagnose the Primitives table.**

- Total primitives
- Types represented
- Duration range (if parseable)

**Step 6 — Check for open pattern candidates.**

Read up to the 10 most recent trace files from `traces/executions/`. For each, check the Pattern Candidates section for unchecked `[ ]` items. Count total open candidates across loaded files.

**Step 7 — Surface the diagnostic.**

```
Retrieval Diagnostics — [YYYY-MM-DD]
══════════════════════════════════════

Execution Index
  Total episodes     : [N]
  Date range         : [start] – [end]  ([N] days span)
  Coverage gaps      : [N gap(s) >14 days — or "none detected"]
                       [For each gap:] [start date] – [end date] ([N days])
  Types indexed      : [list present]
  Types missing      : [list absent — or "none"]
  Outcome split      : [N] completed  [N] partial  [N] failed  [N] abandoned
  Recall readiness   : [Insufficient | Minimal | Adequate | Rich]

Journal Coverage
  Total entries      : [N]
  Last entry         : [date]  ([N days ago])
  Status             : [Current (<7d) | Stale (7–30d) | Absent (>30d)]

Pattern Layer
  Patterns           : [N] total
    emerging         : [N]
    confirmed        : [N]
    high confidence  : [N]
  Orphan patterns    : [N with 0 instances — or "none"]
  Primitives         : [N] total

Open Candidates
  Unchecked in recent traces : [N]  (scanned last 10 episodes)

Overall Retrieval Health
  Index completeness : [Good | Partial | Sparse]
  Pattern coverage   : [Good (3+ patterns) | Building (1–2) | None]
  Journal continuity : [Current | Stale | Absent]
  Overall            : [Healthy | Building | Sparse]

Recommended Actions
  [1-3 specific skill invocations or actions]
  [E.g. "Run /trace-capture — last episode was [N] days ago"]
  [E.g. "Run /pattern-mine — [N] open candidates flagged"]
  [E.g. "Run /workflow-journal — [N] days since last entry"]
  [E.g. "Review [pattern-id] — shows 0 instances (possible orphan)"]
```

## Quality Gate

- [ ] All four TRACE-INDEX tables parsed — not just Execution Episodes
- [ ] Recall readiness classified by the 4-tier threshold, not qualitatively
- [ ] Coverage gaps reported with specific date ranges, not just "gaps found"
- [ ] Open candidates counted from actual loaded trace files — not inferred from index alone
- [ ] Orphan patterns flagged (patterns with 0 instances)
- [ ] Recommended actions are specific skill invocations — not vague advice
- [ ] If TRACE-INDEX tables are all empty: says so and exits — does not produce meaningless zeroes
