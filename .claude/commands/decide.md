---
name: decide
description: >-
  Logs a decision with structured rationale — options considered, chosen option,
  reasoning, assumptions, and a review date. Appends to
  decision-frameworks/decisions-log.md. Trigger on: "log this decision", "I
  decided to...", "/decide <decision context>". Do NOT use for action items
  (use /capture with type=action) or for strategic bets (those live in
  strategy/active-bets.md).
---

# Decision Log

Make decisions explicit, reasoned, and reviewable.

## Inputs Required

1. The decision context from the user (inline text).
2. `decision-frameworks/decisions-log.md` — to append the new entry.

## When to Log a Decision

Log any decision that:
- Would be hard to explain later without the reasoning
- Involves real trade-offs between options
- Commits meaningful time, resources, or direction
- Could be revisited in 90 days and be worth reviewing

Do NOT log: trivial choices, implementation details, or anything reversible in <5 minutes.

## Workflow

1. Read the decision context from the user.
2. Identify: what was the decision? What options were in play? What was chosen and why?
3. If options are unclear, ask one targeted clarifying question — not a questionnaire. Default to what's stated.
4. Set `review_date` to 90 days from today unless the decision itself implies a different horizon.
5. Determine reversibility: high (easy to undo) / medium / low (significant rework to undo) / irreversible.
6. Append the structured entry to `decision-frameworks/decisions-log.md`.
7. Report: decision logged, review date set.

## Output Format — Decision Entry

Appended as a new section to `decision-frameworks/decisions-log.md`:

```markdown
---
decision: [Short description — what was decided, in one phrase]
date: YYYY-MM-DD
options_considered:
  - [option 1]
  - [option 2]
chosen: [option chosen]
rationale: [why this option, in 1-3 sentences]
assumptions:
  - [assumption that could be wrong]
reversibility: high | medium | low | irreversible
review_date: YYYY-MM-DD
outcome: pending
---

[Optional: 1-2 sentences of additional context if the frontmatter doesn't capture it.]

---
```

## Quality Gate

- [ ] Entry appended to `decision-frameworks/decisions-log.md`
- [ ] At least two options listed (even if one was "do nothing")
- [ ] Rationale states WHY this option, not just WHAT was chosen
- [ ] At least one assumption listed
- [ ] `review_date` set and reasonable (default 90 days)
- [ ] `reversibility` assessed honestly — don't default to "high" without evidence
