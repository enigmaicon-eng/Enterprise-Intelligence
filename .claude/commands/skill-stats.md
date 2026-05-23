---
name: skill-stats
description: >-
  Skill invocation and session-type analytics from execution trace history.
  Reads TRACE-INDEX.md and surfaces: type distribution, tag frequency, outcome
  rates, reuse capture rate, uncaptured domains, and pattern mining opportunities.
  Trigger on: "skill stats", "invocation analytics", "which skills do I use most",
  "what work am I capturing", "session type distribution", "tag frequency".
  Do NOT use for permission/capability audit (use /capability-audit) or API cost
  metrics (use /observe).
version: 1.0
output: terminal
---

# /skill-stats

Surface skill invocation and execution patterns from trace history. Answers: "what work am I actually doing, and is it being captured and converted to patterns?"

## When to Use

- Monthly, as part of the workspace health ritual
- Before deciding which patterns to codify via `/pattern-mine`
- When you suspect certain work types are undercaptured or overrepresented

**Do NOT use for:**
- Skill permission and capability audit → `/capability-audit`
- API cost and quality metrics → `/observe`
- Runtime workflow status → `/runtime-status`

## Workflow

**Step 1 — Read TRACE-INDEX.md.**

Parse the Execution Episodes table. If fewer than 3 rows: report "Insufficient trace history for meaningful stats (< 3 episodes)" and exit.

**Step 2 — Compute type distribution.**

Known session types: `workflow`, `debug`, `architecture`, `pm-session`, `synthesis`, `build`.

Count episodes per type. Show 0 for types with no entries.

**Step 3 — Compute tag frequency.**

For each row's Tags field: split on commas, trim whitespace. Count total occurrences per unique tag across all rows. Sort descending. Show top 15.

**Step 4 — Compute outcome rates by type.**

For each session type with >0 episodes:
- Completed: count / total for that type
- Partial: count / total
- Failed + abandoned: count / total

**Step 5 — Compute reuse potential distribution.**

Count high / medium / low across all episodes. Compute high-reuse capture rate = high-reuse count / total.

**Step 6 — Compute monthly volume.**

Group episodes by YYYY-MM from the date field. Show most recent 6 months.

**Step 7 — Identify gaps and opportunities.**

- Types with 0 episodes: uncaptured domains
- Tags that appear in exactly 1 episode: singletons (low pattern value)
- Session types where >50% of episodes are non-completed: reliability signal
- Tags with 3+ episodes and no matching entry in the Patterns table: pattern mining candidates

**Step 8 — Surface the analysis.**

```
Skill Invocation Stats — [YYYY-MM-DD]
══════════════════════════════════════
Total episodes: [N]  (from [earliest date] to [latest date])

Session Types
  workflow      : [N]  ([%])
  debug         : [N]  ([%])
  architecture  : [N]  ([%])
  pm-session    : [N]  ([%])
  synthesis     : [N]  ([%])
  build         : [N]  ([%])

Top Tags (by frequency)
  [tag]              : [N] episodes
  [tag]              : [N] episodes
  ...  (top 15, or all if < 15 unique tags)

Outcome Rates by Type
  [type]  :  [N]% completed  [N]% partial  [N]% failed/abandoned
  ...

Reuse Potential
  High    : [N]  ([%] of total)
  Medium  : [N]  ([%])
  Low     : [N]  ([%])

Monthly Volume
  [YYYY-MM]  : [N] episodes
  [YYYY-MM]  : [N] episodes
  ...  (last 6 months)

Gaps and Signals
  Uncaptured types  : [list — or "none"]
  Reliability flags : [types with <50% completion — or "none"]
  Singleton tags    : [count] tags appear only once

Pattern Mining Opportunities
  [tag: N episodes, no matching pattern] ...
  [— or "No obvious candidates yet"]
```

## Quality Gate

- [ ] All 6 known session types shown — zero-count types displayed, not omitted
- [ ] Tags parsed from comma-separated fields — not counted as whole strings
- [ ] Outcome rates computed per-type — not as a single aggregate
- [ ] Gaps section surfaces absence, not just presence
- [ ] Pattern mining candidates cross-referenced against actual Patterns table
- [ ] If < 3 episodes total: exits with clear message rather than computing meaningless percentages
