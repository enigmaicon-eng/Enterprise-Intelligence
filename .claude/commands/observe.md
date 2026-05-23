---
name: observe
description: >-
  Generates the workspace observability dashboard: token costs by workflow,
  cache hit rates, quality scores, dead workflows, stale files, and a prioritized
  action list. Reads telemetry JSONLs and quality ratings. Writes to
  observability/dashboard.md. Trigger on: "observe", "workspace health",
  "system health", "how is the workspace doing", "/observe". Do NOT use for
  meeting review (use /weekly) or strategic assessment (use /synthesize).
---

# Observability Dashboard

Surface what the telemetry knows about how the workspace is performing.

## Inputs Required

1. `telemetry/api-log.jsonl` — all entries (or last 30 days if large)
2. `telemetry/workflow-log.jsonl` — same
3. `observability/quality.jsonl` — human quality ratings
4. `memory/MEMORY.md` → check when memory files were last updated
5. `knowledge/KNOWLEDGE-INDEX.md` → check `reviewed:` dates

## Workflow

1. Read all telemetry files. Parse JSONL line by line.
2. Compute metrics (see Output Format for each metric's definition).
3. Identify flags: any metric outside acceptable thresholds (see Thresholds table below).
4. Rank flags by impact (cost > quality > utilization > hygiene).
5. Write dashboard to `observability/dashboard.md`.
6. Report: file written, number of flags raised.

## Thresholds

| Metric | Warning | Critical |
|--------|---------|---------|
| Cache hit rate | <60% | <40% |
| Sonnet cost/week | >$15 | >$25 |
| Opus cost/week | >$30 | >$50 |
| Prompt quality avg | <3.5 | <3.0 |
| Workflow dead time | >14 days | >30 days |
| Knowledge decay | >90 days no review | >180 days |
| Memory staleness | >30 days (projects) | >90 days (others) |

## Output Format

Write to `observability/dashboard.md`:

```markdown
# Workspace Dashboard — Week YYYY-WW
Generated: YYYY-MM-DD

## Cost Summary
- Total API cost (7 days): $X.XX
  - Haiku: $X.XX | Sonnet: $X.XX | Opus: $X.XX
- Cache hit rate: X% [target: >60%]
- vs. prior week: [+/-X% or "first measurement"]

## Workflow Utilization
| Workflow | Runs (7d) | Avg Duration | Avg Tokens | Status |
|----------|-----------|-------------|------------|--------|
| /briefing | X | Xs | X | Active |
| /debrief | X | Xs | X | Active |
| /capture | X | Xs | X | Active |
| /weekly | X | Xs | X | Active |
| /promote | X | Xs | X | [Active|Idle] |
| /decide | X | Xs | X | [Active|Idle] |
| /observe | X | Xs | X | Active |
| /synthesize | X | Xs | X | [Active|Idle] |

## Quality Scores (human-rated outputs)
| Prompt | Version | Avg Score (7d) | Trend | Status |
|--------|---------|---------------|-------|--------|
[one row per rated prompt]

## Flags
[Ranked by impact. Each flag has a disposition field for the weekly review.]
- [ ] [COST] ...
- [ ] [QUALITY] ...
- [ ] [DEAD] ...
- [ ] [DECAY] ...
- [ ] [HYGIENE] ...

## Recommended Actions
[Top 3 actions to take this week based on flags, ranked by impact.]
1. 
2. 
3. 
```

## Quality Gate

- [ ] Dashboard written to `observability/dashboard.md`
- [ ] All 5 input sources read
- [ ] Metrics labeled as "estimated" where precision is limited
- [ ] Every flag has enough context to act on it (which file, which metric, which threshold)
- [ ] Recommendations are specific and actionable (not "consider improving X")
- [ ] No flag left without a recommended disposition
