---
name: cognitive-load
description: >-
  Aggregate cognitive load assessment across the full workspace. Reads all six
  load sources, computes a total load level (Clear/Moderate/High/Overloaded),
  and recommends a work mode (Deep Focus/Focused Work/Reduction Mode/
  Maintenance Only). Distinct from /briefing (today's priorities), /plan
  (today's commitments), and /ops-dashboard (execution health). Answers "Is
  the workspace clear enough for the work I'm planning to do?" Run at session
  start or when work feels scattered.
version: "1.0"
changed: "2026-05-23 — initial"
output: inline (load profile + work mode recommendation)
---

# /cognitive-load — Cognitive Load Assessment

## When to Use

- Session start: before deciding what type of work to attempt
- When planning deep work: confirm the workspace is clear enough
- When feeling scattered despite knowing what to work on
- After a high-interrupt period to assess accumulated load
- Weekly: check whether load has been building over time

**Do NOT use for:**
- Today's specific priority ranking → `/briefing`
- Seeing exactly what's in each category → `/open-loops`
- What type of work you've been doing → `/exec-allocation`
- Strategic attention gap → `/attention-debt`

---

## Input

```
/cognitive-load           ← Full assessment with work mode recommendation
/cognitive-load --quick   ← Load level and work mode only (no per-category detail)
```

---

## Process

### Step 1 — Read all load sources

Read (attempt all; skip with "unavailable" note if file missing):

1. `notes/raw/` — count files
2. `meeting-intelligence/raw/` — count unprocessed meeting files
3. `strategy/signals/[YYYY-MM].md` — count unreviewed signals (current + last month)
4. `decision-frameworks/decisions-log.md` — count entries where outcome = pending
5. `knowledge/KNOWLEDGE-GRAPH.json` — count contradicts edges with unresolved status
6. `runtime/state/active-workflows.json` — count workflows in GATE or PAUSED status

### Step 2 — Compute stale counts

For each source, separate total items from stale items (past staleness threshold):
- Raw captures stale: >7 days
- Meetings stale: >2 days
- Signals stale: >7 days
- Decisions stale: >30 days in pending
- Contradictions: all unresolved treated as stale (no reliable timestamp in all cases)
- Stalled workflows: GATE/PAUSED >3 days

**Total open items** = sum of all counts (stale items count double toward load — they've been deferred).

Load scoring: each item = 1 point. Each stale item = 2 points (lingering = higher mental cost than fresh).

### Step 3 — Determine load level

| Load Level | Score Range | Meaning |
|-----------|-------------|---------|
| **Clear** | 0–8 | Workspace is clean; full mental bandwidth available |
| **Moderate** | 9–20 | Normal operational load; some background processing |
| **High** | 21–40 | Load accumulating; attention fragmenting |
| **Overloaded** | 41+ | Capacity compromised; reduction required before other work |

### Step 4 — Determine work mode

| Load Level | Work Mode | What It Means |
|-----------|-----------|--------------|
| Clear | **Deep Focus** | Complex synthesis, strategy, architectural decisions — full bandwidth available |
| Moderate | **Focused Work** | Implementation, analysis, productive output — working effectively |
| High | **Reduction Mode** | Spend 20–30 min on /open-loops before deep work; inbox processing takes priority |
| Overloaded | **Maintenance Only** | Process inbox, advance stalled workflows, defer new work — do not attempt complex tasks |

### Step 5 — Identify load drivers and quick wins

**Primary load driver**: the source contributing the most to the total score.

**Quick wins**: sources where routing takes <10 min per item (meetings → /debrief; raw captures → /promote or delete).

**Deferral candidates**: sources where routing requires substantial time (pending decisions → /pre-decide).

### Step 6 — Generate reduction path

If load level = High or Overloaded: provide a 3-step reduction path — the specific actions that would bring load down to Moderate in the least time.

---

## Output Format

```
COGNITIVE LOAD — [YYYY-MM-DD]

Load Level:  [CLEAR / MODERATE / HIGH / OVERLOADED]
Load Score:  [N] points ([N] items × 1pt + [N] stale items × 2pt)
Work Mode:   [Deep Focus / Focused Work / Reduction Mode / Maintenance Only]

LOAD PROFILE

Source                 | Items | Stale | Points
-----------------------|-------|-------|-------
Raw captures           |  [N]  |  [N]  |  [N]
Unprocessed meetings   |  [N]  |  [N]  |  [N]
Unreviewed signals     |  [N]  |  [N]  |  [N]
Pending decisions      |  [N]  |  [N]  |  [N]
Unresolved contradictions |[N] |  [N]  |  [N]
Stalled workflows      |  [N]  |  [N]  |  [N]
─────────────────────────────────────────────
TOTAL                  |  [N]  |  [N]  |  [N]

Primary load driver:  [source with highest points]
Quick wins:           [sources with low time-to-close]

[If High or Overloaded:]
REDUCTION PATH (to reach Moderate)
Step 1: [specific action + estimated time]
Step 2: [specific action + estimated time]
Step 3: [specific action + estimated time]
Estimated reduction: [N] points → [projected load level after]

[If Clear or Moderate:]
✓ Load is manageable. Proceed with [work mode].

→ /open-loops for full item inventory
→ /attention-debt to check strategic attention alignment
```

---

## Quality Gate

Before outputting:
- [ ] All 6 sources read (note "unavailable" per source, not silent skip)
- [ ] Score computed using the 1pt/2pt formula, not a flat item count
- [ ] Load level determined from actual score against the threshold table
- [ ] Work mode matches the load level — not hardcoded
- [ ] Reduction path given ONLY when load = High or Overloaded
- [ ] Reduction path steps are specific (name the skill + category) with time estimate
- [ ] If all sources read 0: output "Clear" without hedging — clean workspace is a valid state
