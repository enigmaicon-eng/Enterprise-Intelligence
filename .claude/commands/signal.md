---
name: signal
description: >-
  Strategic signal capture and review between horizon scans. Logs environmental
  observations (threats, opportunities, noise) tagged to active bets, then
  surfaces signals approaching their review date. Trigger on: "signal capture",
  "log this signal", "strategic signal", "something worth watching", "signal
  review", "what signals are due". Subcommands: capture, review, list. Do NOT
  use for full horizon scanning (use /horizon) or for logging evidence against
  a specific bet (use /bet update).
version: 1.0
output: strategy/signals/YYYY-MM.md + terminal
---

# /signal

Lightweight strategic signal management between horizon scans. Signals are specific observable facts that might matter to the bet portfolio — not predictions, not analyses, not wishes. One observation at a time, classified and time-boxed.

## When to Use

- Any time you observe something in the environment that might be strategically relevant
- Weekly, to review what has accumulated and flag what needs action
- Before running `/horizon` to gather accumulated signals as scan input

**Do NOT use for:**
- Full structured horizon scan → `/horizon`
- Logging evidence against a specific bet thesis → `/bet update`
- Capturing general notes → `/capture`

## Subcommands

- `/signal capture [description]` — log a new signal
- `/signal review [--type threat|opportunity|uncertain] [--bet BET-ID]` — surface signals needing attention
- `/signal list [--since YYYY-MM-DD]` — list all recent signals

---

## Protocol — Capture

**Step 1 — Parse the signal.**

Separate the observable fact from the interpretation. The signal is what happened; the implication is what it might mean. Both are captured, but they must be distinct.

Bad: "AI models are getting better which threatens our bet"
Good: Observation: "OpenAI released a new model with 2x context window at same price point" / Implication: "Reduces the differentiation of our context engineering bet if the base capability converges"

**Step 2 — Classify category and horizon.**

| Category | When |
|----------|------|
| Threat | Could harm a bet thesis or portfolio position |
| Opportunity | Could strengthen a bet or open a new one |
| Noise | Observed but no strategic relevance — log to close the loop, not to act |
| Uncertain | Strategic relevance unclear — needs further evidence before categorizing |

Horizon: H1 (action within 90 days) / H2 (builds over 90d-12mo) / H3 (12+ months out)

**Step 3 — Match to active bets.**

Read `strategy/active-bets.md`. Identify which active bets this signal is relevant to. Record the BET-IDs. If none, record "none."

**Step 4 — Set review_by date.**

Default by category and horizon:
- Threat/H1: 7 days — needs prompt attention
- Threat/H2 or Opportunity/H1: 14 days
- Opportunity/H2 or Uncertain/H1: 30 days
- Any/H3 or Noise: 90 days

**Step 5 — Write the signal entry.**

Read `strategy/signals/[YYYY-MM].md` (current month). If it doesn't exist, create it with a date header.

Append:

```markdown
---
id: SIG-YYYY-NNN
date: YYYY-MM-DD
observation: [the specific observable fact]
implication: [what this might mean strategically]
category: threat | opportunity | noise | uncertain
horizon: H1 | H2 | H3
affects_bets: [BET-IDs or "none"]
review_by: YYYY-MM-DD
status: open
---
```

Increment NNN sequentially within the month.

**Step 6 — Surface immediate flags.**

If category = threat AND horizon = H1:
```
⚠ H1 Threat logged: [observation]
Affects: [bet IDs]
Review by: [date] — 7 days. Consider /bet update [BET-ID] if this is evidence against the thesis.
```

Otherwise: report the signal logged with ID and review_by date.

---

## Protocol — Review

**Step 1 — Read signal files.**

Read `strategy/signals/` for current month and prior month. Parse all entries with `status: open`.

**Step 2 — Filter and prioritize.**

- Overdue: review_by < today
- Urgent: review_by ≤ today + 7 days
- Apply `--type` or `--bet` filters if provided

Sort: overdue first, then urgent, then by horizon (H1 → H2 → H3).

**Step 3 — Surface the review.**

```
Signal Review — [YYYY-MM-DD]
══════════════════════════════

Overdue ([N] signals)
  SIG-YYYY-NNN  [date]  [category/horizon]
    Observation : [text]
    Affects     : [bets]
    Was due     : [date]  ([N] days overdue)
    Action      : /bet update [BET-ID] | /horizon | close as noise

Due within 7 days ([N] signals)
  SIG-YYYY-NNN  [date]  [category/horizon]
    Observation : [text]
    Affects     : [bets]
    Due         : [date]

Coming up — next 30 days ([N] signals)
  [brief list: ID, date, category, affects]

[If all signals are current and not urgent:]
No signals overdue or due within 7 days. [N] signals in the next 30 days.
```

**Step 4 — Offer actions.**

```
Available actions:
  /bet update [BET-ID]         — log signal as evidence against a bet
  /horizon                     — run full scan (recommended if 5+ signals have accumulated)
  Mark signal closed           — say "close SIG-YYYY-NNN" to mark as reviewed
```

---

## Protocol — List

Read signal files matching `--since` filter (default: last 90 days). Output:

```
Signal List — since [date]
═══════════════════════════
SIG-YYYY-NNN  [date]  [category]  [horizon]  [status]  affects: [bets]
  [observation, truncated to 80 chars]
```

## Quality Gate

- [ ] Observation is a specific observable fact — not a prediction or analysis
- [ ] Implication is separate from observation — not mixed into the same field
- [ ] BET-ID matching done against live active-bets.md — not from memory
- [ ] review_by date set per the classification table — not arbitrarily
- [ ] H1 threats surface immediately after logging — not silently
- [ ] Review shows "none overdue" explicitly when that is the case
