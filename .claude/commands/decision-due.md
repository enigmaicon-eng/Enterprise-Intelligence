---
name: decision-due
description: >-
  Surfaces decisions approaching their review date. Reads decisions-log.md,
  categorizes entries by urgency (overdue / due soon / upcoming), and prioritizes
  by reversibility. Hands off to /decision-review. Trigger on: "what decisions
  are due", "decision review queue", "which decisions need review", "show overdue
  decisions", "decision-due". Do NOT use for reviewing decision quality (use
  /decision-review) or for logging a new decision (use /decide).
version: 1.0
output: terminal
---

# /decision-due

Surface the decision review queue. Prevents review debt from silently accumulating — decisions that are never reviewed can never generate judgment rules.

## When to Use

- Weekly, as part of the workspace health ritual
- At the start of `/decision-review` to select which decisions to review
- When you suspect decisions are overdue but can't recall which ones

**Do NOT use for:**
- Reviewing decision quality → `/decision-review`
- Logging a new decision → `/decide`
- Pre-decision analysis → `/pre-decide`

## Inputs

- Optional: `--window [N]` — show decisions due within N days (default: 30)
- Optional: `--overdue` — show only overdue decisions

## Workflow

**Step 1 — Read decisions-log.md.**

Read `decision-frameworks/decisions-log.md`. Parse all entries. Extract: decision name, date logged, review_date, reversibility, outcome.

If the file is empty or has no entries: report "No decisions logged yet" and exit.

**Step 2 — Categorize by urgency.**

For each entry:
- **Overdue**: review_date < today
- **Due soon**: review_date is within 14 days from today
- **Upcoming**: review_date is 15–60 days from today
- **Later**: review_date > 60 days from today (omit unless `--window` is extended)

Skip entries where outcome is already set to something other than "pending" — those have been reviewed.

**Step 3 — Sort by priority within each category.**

Within each urgency tier, sort by reversibility (most irreversible first):
- irreversible → low → medium → high

Rationale: irreversible decisions carry more learning value and can't be corrected by delayed review.

**Step 4 — Surface the queue.**

```
Decision Review Queue — [YYYY-MM-DD]
══════════════════════════════════════

Overdue ([N])
  [N] decisions past their review date.

  • "[decision]"
    Due: [review_date]  ([N] days overdue)
    Reversibility: [level]
    Outcome: [current outcome field]

  • "[decision]"
    ...

Due Within 14 Days ([N])
  • "[decision]"
    Due: [review_date]  ([N] days)
    Reversibility: [level]
    Outcome: pending

  [— or "None due within 14 days."]

Upcoming — Next 15–60 Days ([N])
  • "[decision]"  due [date]  —  [reversibility]
  • "[decision]"  due [date]  —  [reversibility]
  [— or "None in this window."]

Total decisions logged : [N]
Pending review         : [N]
Already reviewed       : [N]  (outcome != "pending")
```

**Step 5 — Offer /decision-review.**

```
Start reviewing:
  /decision-review            — review the 5 most recent pending decisions
  /decision-review [decision] — review a specific decision
```

If overdue decisions include any irreversible ones:
```
⚠ [N] irreversible decision(s) are overdue for review. These carry the most learning value.
```

## Quality Gate

- [ ] decisions-log.md read before categorization
- [ ] Only "pending" outcome entries shown — reviewed decisions excluded
- [ ] Sort order: most irreversible first within each urgency tier
- [ ] Overdue count shown even if 0 — "None overdue" is useful confirmation
- [ ] If no decisions logged at all: says so and suggests /decide — does not produce an empty table
- [ ] `/decision-review` offered as next step with a specific invocation example
