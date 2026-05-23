---
name: exec-throughput
description: >-
  Execution throughput trend analytics — tracks completion rate and output
  velocity over time. Reads TRACE-INDEX.md time-series to classify execution
  momentum as Improving / Stable / Declining / Insufficient. Distinct from
  /ops-dashboard (30-day snapshot and health flags) and /failure-review
  (failure root causes). Answers "Is my execution output getting better or
  worse?" Run weekly or when execution feels stalled. Requires ≥10 episodes.
version: "1.0"
changed: "2026-05-23 — initial"
output: inline (trend report)
---

# /exec-throughput — Execution Throughput Analytics

## When to Use

- Weekly check on execution momentum
- After a difficult period: confirm whether slowdown is real or perceived
- Before a `/strategy-review` or `/exec-checkpoint`: get the throughput context
- When setting execution goals and need a baseline

**Do NOT use for:**
- Overall workspace health status → `/ops-dashboard`
- Failure root causes → `/failure-review`
- Work type distribution → `/exec-allocation`
- Friction and blocker patterns → `/exec-friction`
- Single trace analysis → `/exec-inspect`

---

## Input

```
/exec-throughput           ← Full trend report (default: last 90 days)
/exec-throughput --30      ← Last 30 days only
/exec-throughput --type <session-type>   ← Filter to one session type
```

---

## Process

### Step 1 — Read TRACE-INDEX.md

Read `traces/TRACE-INDEX.md`. Extract all execution episode rows:
- Episode ID
- Date
- Outcome (completed / partial / failed / abandoned)
- Session type / tags
- Duration (if recorded)

If total episodes < 10: report "Insufficient trace history for trend analysis. Capture ≥10 episodes before running throughput analytics." Do not fabricate a trend.

### Step 2 — Divide into time windows

Compute:
- **This period** (last 30 days): all episodes with date ≥ 30 days ago
- **Prior period** (31–60 days ago): all episodes in that window
- **90-day view**: full 90-day picture by 2-week buckets

For each window, compute:
- Total episodes
- Completed count (outcome = completed)
- **Completion rate** = completed ÷ total
- **Weekly output rate** = completed ÷ weeks in window

### Step 3 — Classify throughput momentum

| Classification | Condition |
|---------------|-----------|
| **Improving** | This-period completion rate > prior-period by ≥10 percentage points |
| **Stable** | Completion rate within 10pp in both periods |
| **Declining** | This-period completion rate < prior-period by ≥10pp |
| **Recovery** | Prior period declined, this period has improved back toward baseline |
| **Insufficient** | Either window has <3 episodes (too sparse for classification) |

### Step 4 — Session type breakdown

For the last 30 days, show completion rate by session type (if type tags present in traces). This surfaces whether decline is type-specific (e.g., only planning sessions are failing) vs global.

### Step 5 — Surface notable signals

- Best and worst 2-week bucket in the 90-day view
- Session type with the lowest completion rate (if types present)
- Longest gap between completed sessions (signals an execution drought)

---

## Output Format

```
EXECUTION THROUGHPUT
Period: last 90 days  |  Total episodes: [N]

MOMENTUM: [IMPROVING / STABLE / DECLINING / RECOVERY / INSUFFICIENT]

COMPLETION RATES
This period (last 30d):  [N] episodes → [N] completed → [X]%
Prior period (31-60d):   [N] episodes → [N] completed → [X]%
Change: [+X pp / −X pp]

WEEKLY OUTPUT RATE
This period:  [N] completed sessions/week
Prior period: [N] completed sessions/week

90-DAY TREND (2-week buckets)
[date range]: [N] completed / [N] total ([X]%)
[date range]: [N] completed / [N] total ([X]%)
[date range]: [N] completed / [N] total ([X]%)
[date range]: [N] completed / [N] total ([X]%)

SESSION TYPE BREAKDOWN (last 30d)
[type]: [N] completed / [N] total ([X]%)
[type]: [N] completed / [N] total ([X]%)

SIGNALS
Best 2-week window: [date range] ([X]% completion)
Lowest completion type: [type] ([X]%) [or "type tags unavailable"]
Longest completion gap: [N] days between [date] and [date]

INTERPRETATION
[1-2 sentences: what the trend means operationally and the single most relevant action]
[If declining: suggest /exec-friction to diagnose. If improving: note what changed.]
```

---

## Quality Gate

Before outputting:
- [ ] TRACE-INDEX.md read before any metrics computed
- [ ] Momentum classification uses actual pp difference, not subjective impression
- [ ] If <10 episodes: exit early with clear explanation, do not produce spurious trend
- [ ] Completion rate = completed ÷ total (not completed ÷ scheduled or planned)
- [ ] Session type breakdown only shown if type metadata present in traces
- [ ] Interpretation names ONE specific action, not a list
- [ ] "Insufficient" returned when either time window has <3 episodes
