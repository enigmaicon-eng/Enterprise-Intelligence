# Operational Rituals
## Cadence, Triggers, and Outputs

Rituals are repeatable operational sequences with defined triggers, inputs, outputs, and time budgets. A ritual that doesn't produce a concrete output isn't a ritual — it's a habit without accountability.

## Three-Tier Model

**Tier 1 — Required (never skip):** Daily briefing, daily shutdown, weekly review.
**Tier 2 — High-value (use when relevant):** Daily plan, focus framing, meeting prep, monthly retro + strategy review.
**Tier 3 — Situational (event-triggered, not cadence):** Everything else.

Adding a new ritual requires removing or downgrading an existing one. The ritual stack is not a backlog.

---

## Ritual Cadence

### Daily — Session Orientation (≤2 min, required)
**Trigger**: First session of each work day
**Sequence**:
1. `/briefing` — critical items, today's focus, heads-up

**Output**: Clear first action for the session. Nothing written.
**Failure signal**: You skip this and the first thing you do is react to something that arrived overnight.

---

### Daily — Morning Planning (≤10 min, optional)
**Trigger**: When `/briefing` isn't enough — competing priorities, unclear direction, or the week has changed
**Sequence**:
1. `/plan` — set today's theme, name top 3 commitments, flag one risk

**Output**: Theme + 3 commitments (terminal only, not filed unless useful).
**Failure signal**: You run `/plan` but do something entirely different. Stop running it if you don't use the output.

---

### Daily — Deep Work Session (≤5 min to frame)
**Trigger**: Before any session requiring sustained concentration
**Sequence**:
1. `/focus [problem]` — name the problem, set done condition, load 1-3 files

**Output**: Session frame (terminal). Do not start the work without a named done condition.
**Failure signal**: You start without a done condition and work for 2 hours without clear output.

---

### Daily — Meeting Preparation (≤10 min, selective)
**Trigger**: 15-30 min before any meeting where preparation changes the outcome
**Sequence**:
1. `/prep [meeting name]` — pre-read, your role, the decision to make

**Output**: Prep brief (terminal). Run only when stakes warrant it.
**Failure signal**: You prepare for every meeting, diluting the attention that high-stakes prep deserves.

---

### Daily — End of Day Closure (≤10 min, required)
**Trigger**: Last action before closing the workspace
**Sequence**:
1. `/shutdown` — sweep opens, log decisions, seed tomorrow's first action
2. `/shutdown friday` — Friday variant with week summary

**Output**: EOD capture (filed or discarded) + tomorrow seed.
**Failure signal**: You skip this consistently. Open loops accumulate overnight; next-session startup cost grows.
**Note**: This is the one non-negotiable daily ritual. Everything else is optional.

---

### Weekly — Execution Review (≤15 min)
**Trigger**: Monday morning, or start of first session of the week
**Sequence**:
1. `/exec-review weekly` — initiative health scan, action item audit, next-week top 5
2. Update `execution/active-initiatives.md` — correct any stale status values
3. `/exec-risk review` — scan for triggered or stale risks

**Output**: `reviews/weekly/[YYYY-WW]-exec.md` + updated initiative statuses
**Failure signal**: You start work without knowing what slipped last week.

---

### Weekly — Knowledge Review (≤15 min)
**Trigger**: Monday morning, after execution review
**Sequence**:
1. `/weekly` — processed meetings → patterns → next week priorities (knowledge lens)
2. Any `/promote` candidates from the week's notes

**Output**: `reviews/weekly/[YYYY-WW].md`
**Note**: This is distinct from execution review. Execution review asks "what are we doing?" Knowledge review asks "what did we learn?"

---

### Per-Milestone — Strategic Checkpoint (≤20 min)
**Trigger**: Milestone marked complete in `execution/active-initiatives.md`
**Sequence**:
1. `/exec-checkpoint [initiative-id]` — 3-question gate: goal still right? approach still right? assumptions still valid?
2. Record decision in checkpoint log (continue / pivot / stop)

**Output**: `execution/checkpoints/[initiative-id]/[date]-[milestone].md`
**Failure signal**: You complete a milestone and immediately start the next one without checking alignment.

---

### Monthly — Operational Retrospective (≤30 min)
**Trigger**: Last working day of each month
**Sequence**:
1. Read the month's 4 weekly exec reviews
2. Complete `templates/operational-retro.md`
3. Update `knowledge/operations/work-patterns.md` with confirmed patterns
4. Update `knowledge/operations/friction-points.md` with new friction observed
5. Close or archive stale risks in `execution/risks.md`

**Output**: `reviews/monthly/[YYYY-MM]-retro.md` + updated operations knowledge
**Failure signal**: You write a retro but don't change anything as a result.

---

### Monthly — Strategy Review (≤45 min)
**Trigger**: First Monday of each month
**Sequence**:
1. `/synthesize` — cross-domain synthesis from the month
2. Run monthly strategy with Opus (W06 workflow)
3. Review active bets in `strategy/active-bets.md`
4. `/exec-checkpoint [initiative-id] strategic` on any initiative in flight for 60+ days

**Output**: `strategy/monthly/[YYYY-MM].md`
**Failure signal**: You review strategy without updating what you're working on.

---

### Quarterly — Portfolio Review (≤45 min)
**Trigger**: End of each quarter
**Sequence**:
1. Review all initiatives completed/stopped in the quarter
2. `/exec-checkpoint` strategic review on any surviving initiative
3. Capture 3 execution learnings in `knowledge/operations/execution-intelligence.md`
4. Reset `execution/active-initiatives.md` — archive complete/stopped, renew active

**Output**: `reviews/quarterly/[YYYY-QN].md`
**Failure signal**: You start the next quarter carrying the same blocked initiative without a decision.

---

## Anti-Ritual Signals

These behaviors indicate rituals have become theater:

| Signal | What It Means |
|--------|--------------|
| Exec review with no status changes | Either nothing happened, or you're not looking honestly |
| Checkpoints always produce "Continue" | Criteria are too vague to generate signal |
| Retro with no "One Change to Make" completed | Retros are observation, not improvement |
| Risk register with 0 entries for 4+ weeks | Risks exist; you're not surfacing them |
| Briefing skipped more than 2× per week | The briefing is too slow or too noisy — fix it, don't skip it |

---

## Ritual Stack Map

```
Session Start
└── /briefing (required, 2 min)
    └── /plan (optional, 5-10 min — when direction is unclear)

Deep Work Block
└── /focus [problem] (5 min — frame before concentrating)

Pre-Meeting (selective)
└── /prep [meeting] (5-10 min — when preparation changes outcome)

Post-Meeting
└── /debrief [file] (10-15 min — when meeting produced decisions or actions)

Session End
└── /shutdown (required, 5-10 min)

Week Start
├── /plan weekly (10-15 min)
├── /exec-review weekly (execution lens)
└── /weekly (knowledge lens)

Week End
└── /shutdown friday (10-12 min)

Milestone Reached
└── /exec-checkpoint [initiative]

Month End
├── Operational retro
├── Strategy review
└── Cognitive review (playbooks/cognitive-review.md)

Quarter End
└── Portfolio review + knowledge capture
```
