---
name: learning-velocity
description: >-
  Learning acquisition rate analytics — tracks how fast knowledge is being
  added over time, by domain, with momentum classification. Answers "Am I
  learning faster or slower? Which domains are growing?" Does NOT assess entry
  quality (use /knowledge-qa). Does NOT surface gaps (use /knowledge-gap).
  Does NOT attribute to sources (use /learning-source). Run monthly.
version: "1.0"
changed: "2026-05-23 — initial"
output: inline (analytics report)
---

# /learning-velocity — Learning Acquisition Analytics

## When to Use

- Monthly check on learning momentum
- Starting a new learning sprint and want to know where growth is happening
- Feeling like learning has stalled and want to confirm with data
- Setting learning goals and need a baseline rate

**Do NOT use for:**
- Entry quality → `/knowledge-qa`
- What domains are missing → `/knowledge-gap`
- Which sources are most valuable → `/learning-source`
- How much knowledge is being applied → `/knowledge-utilization`

---

## Input

```
/learning-velocity             ← Full report (all domains, last 90 days + trend)
/learning-velocity --domain <name>   ← Single domain deep view
/learning-velocity --90        ← Last 90 days only
/learning-velocity --30        ← Last 30 days only
```

---

## Process

### Step 1 — Read index

Read `knowledge/KNOWLEDGE-INDEX.md`. Extract for each entry:
- Domain
- Creation date (from entry frontmatter or index)
- Entry ID/title

Build a flat list: `[date, domain, entry_title]`

### Step 2 — Compute time windows

For each domain:
- **Total entries**: count all time
- **Last 30 days**: entries with creation date ≥ 30 days ago
- **Prior 30 days** (31–60 days ago): for momentum comparison
- **Last 90 days**: entries with creation date ≥ 90 days ago

For the whole base:
- **Weekly rate**: total entries last 30 days ÷ 4
- **All-time rate**: total entries ÷ weeks since first entry

### Step 3 — Classify domain momentum

For each domain, classify based on last 30 days vs prior 30 days:

| Momentum | Condition |
|----------|-----------|
| **Accelerating** | Last-30 count > 1.5× prior-30 count (and last-30 ≥ 2) |
| **Steady** | Last-30 count within 50% of prior-30 count |
| **Decelerating** | Last-30 count < 0.5× prior-30 count (and had prior activity) |
| **Stalled** | 0 new entries in last 90 days AND domain has ≥1 entry |
| **New** | First entry appeared in last 30 days |
| **Dormant** | 0 new entries in last 90 days AND domain has <3 entries |

### Step 4 — Surface notable signals

- Fastest-growing domain (last 30 days)
- Longest-stalled domain with strategic importance (>90 days no entries)
- Overall velocity trend (this month vs last month)

---

## Output Format

```
LEARNING VELOCITY
Period: last 90 days  |  Total base: [N] entries across [D] domains

OVERALL RATE
This month: [N] entries ([N/wk] per week)
Last month: [N] entries
Trend: [Accelerating / Steady / Decelerating]

DOMAIN BREAKDOWN

[domain] — [N] total entries
  Last 30d: [N]  |  Prior 30d: [N]  |  Momentum: [classification]

[domain] — [N] total entries
  Last 30d: [N]  |  Prior 30d: [N]  |  Momentum: [classification]

[...]

SIGNALS
Fastest growing: [domain] (+[N] this month)
Stalled domains: [list, or "none"]
New domains this period: [list, or "none"]

CONTEXT
[1-2 sentences interpreting the overall pattern]
[If stalled domains: suggest /knowledge-gap or /learn for top stalled domain]
```

---

## Quality Gate

Before outputting:
- [ ] Dates parsed from actual entry metadata, not estimated
- [ ] Each domain has a momentum classification with the specific counts supporting it
- [ ] Trend is calculated from actual this-month vs last-month counts, not assumed
- [ ] If <10 total entries: note velocity analytics are premature; recommend building the base
- [ ] Stalled domain flag only applied if domain truly has 0 new entries in 90 days
- [ ] Context section gives 1 interpretive insight, not a list of obvious restatements
