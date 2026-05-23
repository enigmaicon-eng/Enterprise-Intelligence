---
name: exec-allocation
description: >-
  Work allocation analytics — analyzes how actual execution time is distributed
  across work types (strategic, productive, reflective, reactive, overhead) and
  surfaces whether the distribution matches intention. Reads trace session types
  and journal entries. Distinct from /skill-stats (which counts skill invocations)
  and /exec-throughput (which measures completion rates). Answers "Where is my
  execution time actually going?" Run monthly. Requires session type tags in
  traces to be meaningful.
version: "1.0"
changed: "2026-05-23 — initial"
output: inline (allocation report)
---

# /exec-allocation — Work Allocation Analytics

## When to Use

- Monthly check on whether actual work distribution matches intended priorities
- Sense that reactive/overhead work is crowding out strategic work
- Planning a work-mode change and want a baseline
- Preceding a quarterly review to surface how time was actually spent

**Do NOT use for:**
- Throughput trend (is execution improving?) → `/exec-throughput`
- Skill invocation frequency → `/skill-stats`
- Friction and blocker patterns → `/exec-friction`
- Failure root causes → `/failure-review`

**Requires session type tags in traces to be meaningful.** If traces lack type metadata, the report will note this and the analysis will be limited to goal-keyword inference only.

---

## Input

```
/exec-allocation              ← Last 60 days (default)
/exec-allocation --30         ← Last 30 days only
/exec-allocation --90         ← Last 90 days
```

---

## Process

### Step 1 — Read traces

Read `traces/TRACE-INDEX.md`. For each episode in the target period, extract:
- Session type tag(s)
- Duration (if recorded)
- Outcome
- Goal keywords

Also scan `traces/journal/` for workflow journal entries in the target period. Journal entries may state intended work type for the day.

### Step 2 — Map to work categories

Map each session type tag to a work category using the allocation model:

| Session Type Tags | Work Category |
|------------------|---------------|
| planning, strategy, horizon, bet | Proactive / Strategic |
| execution, build, implement, write, develop | Productive / Output |
| review, retrospective, audit, qa, inspect | Reflective / Maintenance |
| research, learn, explore, read, study | Generative / Input |
| reactive, urgent, interrupt, unplanned, escalation | Reactive / Unplanned |
| support, meeting, admin, coordination, comms | Overhead / Coordination |

Sessions with multiple tags are classified by the first tag that matches a category (priority order as listed above). Untagged sessions are grouped as "Unclassified."

### Step 3 — Compute distribution

For each work category, compute:
- Session count
- % of total sessions
- % of completed sessions (outcome = completed)

Calculate:
- **Reactive ratio** = Reactive/Unplanned sessions ÷ total sessions
- **Strategic ratio** = Proactive/Strategic sessions ÷ total sessions
- **Overhead ratio** = Overhead/Coordination sessions ÷ total sessions

### Step 4 — Derive intention proxy (if available)

Scan journal entries for language indicating intended work type ("planning to...", "focus on...", "priority is...", "deep work on..."). Where found, note the intended category and compare against actual distribution for that period.

If no journal entries exist for the period: note "No intention proxy available — comparison limited to absolute distribution."

### Step 5 — Apply allocation health thresholds

Flag structural imbalance if:

| Condition | Flag |
|-----------|------|
| Reactive ratio >30% | HIGH REACTIVE: execution agenda is being set by interrupts |
| Strategic ratio <10% | LOW STRATEGIC: insufficient forward-looking work |
| Overhead ratio >25% | HIGH OVERHEAD: coordination is crowding out output |
| Unclassified >30% | POOR TAGGING: session type metadata missing; analysis unreliable |

---

## Output Format

```
WORK ALLOCATION
Period: [date range]  |  [N] sessions analyzed

DISTRIBUTION

Category              | Sessions | % of Total | Completion Rate
----------------------|----------|------------|----------------
Proactive / Strategic |   [N]    |    [X]%    |     [X]%
Productive / Output   |   [N]    |    [X]%    |     [X]%
Reflective / Maint.   |   [N]    |    [X]%    |     [X]%
Generative / Input    |   [N]    |    [X]%    |     [X]%
Reactive / Unplanned  |   [N]    |    [X]%    |     [X]%
Overhead / Coord.     |   [N]    |    [X]%    |     [X]%
Unclassified          |   [N]    |    [X]%    |     [X]%

KEY RATIOS
Reactive ratio:  [X]%   [HIGH / normal]
Strategic ratio: [X]%   [LOW / normal]
Overhead ratio:  [X]%   [HIGH / normal]

INTENTION VS ACTUAL [omit section if no journal data]
Intended: [inferred from journal entries]
Actual:   [dominant category from distribution]
Gap: [specific mismatch if found, or "aligned"]

FLAGS
[For each threshold crossed:]
⚠  [FLAG NAME]: [specific count and context]
[If none:]
✓  No allocation imbalance flags.

INTERPRETATION
[1-2 sentences: what the distribution reveals about actual vs intended work mode, and
 the single structural change that would most improve alignment]
```

---

## Quality Gate

Before outputting:
- [ ] Traces read from TRACE-INDEX.md for the target period
- [ ] Category mapping applied consistently from the allocation model table
- [ ] Reactive ratio computed from actual tag counts, not inferred
- [ ] If >30% of sessions are Unclassified: flag POOR TAGGING and note analysis is unreliable
- [ ] Intention proxy clearly labeled as estimate from journal keywords, not ground truth
- [ ] If <5 sessions in period: note insufficient volume for meaningful distribution
- [ ] Interpretation names ONE structural change, not a list of improvements
