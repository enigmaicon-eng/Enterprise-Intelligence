---
name: competitive-radar
description: >-
  Logs competitor and market actor moves and assesses their implications for
  active bets. Distinct from /pm-competitive (product feature analysis) — this
  is bet-level strategic implication. Trigger on: "competitive radar", "log
  competitor move", "competitor did X", "market move", "what are competitors
  doing to my bets", "competitive log [actor] [move]". Subcommands: log, review,
  [bet-id]. Do NOT use for product feature comparison (use /pm-competitive) or
  for general signal capture (use /signal).
version: 1.0
output: strategy/competitive/radar.md + terminal
---

# /competitive-radar

Log competitor and market actor moves and assess their strategic implications — specifically for the active bet portfolio. The question is never "what did they do?" in isolation; it is always "what does this do to our thesis?"

## When to Use

- When a competitor makes an observable, specific move (launch, pricing change, acquisition, partnership, hiring pattern)
- Weekly review — surfaces moves that are disconfirming for active bets
- Before running `/strategy-review` — competitor moves are evidence for bet verdicts

**Do NOT use for:**
- Product-level feature analysis → `/pm-competitive`
- General environmental signal (not competitor-specific) → `/signal`
- Full strategic horizon scan → `/horizon`

## Subcommands

- `/competitive-radar log [move description]` — log a competitor move
- `/competitive-radar review [--bet BET-ID] [--implication disconfirms]` — surface moves needing attention
- `/competitive-radar [BET-ID]` — show all moves relevant to a specific bet

---

## Protocol — Log

**Step 1 — Force specificity.**

Parse the move. Require:
- **Actor**: who made the move (company, market participant, regulator)
- **Action**: what specifically happened — the observable fact, not the interpretation
- **Source**: where this was observed

If the description is vague ("they're expanding"), ask one clarifying question before logging: "What specifically did they do — product launch, pricing change, geographic expansion, acquisition, hire?"

**Step 2 — Read active bets.**

Read `strategy/active-bets.md`. For each active bet, determine if this move is relevant to the bet thesis or kill condition.

Tag affected bet IDs.

**Step 3 — Assess implication per affected bet.**

For each affected bet:
- **Confirms** — the move provides evidence the bet thesis is directionally correct
- **Disconfirms** — the move provides evidence against the bet thesis
- **Neutral** — the move is in the domain but doesn't directly affect the thesis
- **Uncertain** — the move's implications for the thesis are unclear; more evidence needed

One-sentence thesis impact for each affected bet.

**Step 4 — Determine action required.**

- Disconfirms → action: recommend `/bet update [BET-ID]` to log as disconfirming evidence
- Confirms → action: recommend `/bet update [BET-ID]` to log as confirming evidence
- Neutral → action: no immediate action needed; monitor
- Uncertain → action: set review in 30 days; watch for follow-on moves

**Step 5 — Append to radar log.**

Read `strategy/competitive/radar.md`. If the file doesn't exist, create it with a header. Append:

```markdown
---
date: YYYY-MM-DD
actor: [competitor or market actor]
move: [specific observable action]
source: [where observed]
affects_bets: [BET-IDs or "none"]
implication_[BET-ID]: confirms | disconfirms | neutral | uncertain
thesis_impact_[BET-ID]: [one sentence on what this means for this bet's thesis]
action_required: yes | monitor | no
status: open
---
```

**Step 6 — Surface immediate flags.**

If any implication is `disconfirms`:
```
⚠ Disconfirming move logged for [BET-ID]: "[actor] [move]"
Thesis impact: [thesis_impact]
Run /bet update [BET-ID] to log this as disconfirming evidence.
```

Otherwise: confirm logged with actor, move summary, and action required.

---

## Protocol — Review

**Step 1 — Read radar.md.**

Read `strategy/competitive/radar.md`. Parse all entries with `status: open`.

Apply filters if provided: `--bet BET-ID` or `--implication disconfirms`.

**Step 2 — Prioritize.**

Sort by: disconfirming implications first, then confirms, then uncertain/neutral.

Within each group: most recent first.

**Step 3 — Surface the review.**

```
Competitive Radar Review — [YYYY-MM-DD]
════════════════════════════════════════

Disconfirming Moves ([N]) — priority review
  [YYYY-MM-DD]  [actor] — [move summary]
    Affects    : [BET-ID]
    Impact     : [thesis_impact]
    Action     : /bet update [BET-ID]

Confirming Moves ([N])
  [YYYY-MM-DD]  [actor] — [move summary]
    Affects    : [BET-ID]
    Impact     : [thesis_impact]

Uncertain ([N]) — monitor
  [YYYY-MM-DD]  [actor] — [move summary]
    Affects    : [BET-ID]

Neutral / No active bet affected ([N])
  [brief list]

[If radar is empty:]
No competitor moves logged. Run /competitive-radar log to capture observed moves.
```

**Step 4 — Offer escalation.**

For any disconfirming move:
```
Escalate: /bet update [BET-ID] — log "[actor] [move]" as disconfirming evidence
```

---

## Protocol — Bet-Specific View

**Command:** `/competitive-radar [BET-ID]`

Read radar.md. Filter entries where `affects_bets` contains the specified BET-ID. Display chronologically, all implication types.

```
Competitive Radar — [BET-ID]  ([Bet Name])
═══════════════════════════════════════════
[N] moves logged affecting this bet.

[YYYY-MM-DD]  [actor] — [move]  — [implication]
  Impact: [thesis_impact]

[YYYY-MM-DD]  ...
```

---

## Quality Gate

- [ ] Actor and action both specific — not "a competitor expanded" (rejected)
- [ ] Implication assessed against the bet thesis, not the category of move
- [ ] Disconfirming moves surface immediately after logging — not silently
- [ ] `/bet update` offered for all disconfirming and confirming moves
- [ ] Review sorts disconfirming first — they carry the most decision weight
- [ ] `strategy/competitive/radar.md` created if it doesn't exist (first log)
- [ ] Thesis impact is a sentence about the bet thesis specifically — not a generic risk description
