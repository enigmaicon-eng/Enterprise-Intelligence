---
name: assumption-register
description: >-
  Derives and tracks the implicit assumptions underlying each active bet's thesis.
  Scans the evidence log for observations that challenge those assumptions. Surfaces
  assumption status (Untested / Tested-held / At risk / Violated) before monthly
  strategy review. Trigger on: "assumption register", "check bet assumptions",
  "which assumptions are at risk", "what does this bet assume", "assumption check".
  Do NOT use for reviewing bet evidence (use /bet update or /strategy-review) or
  for full horizon scanning (use /horizon).
version: 1.0
output: terminal
---

# /assumption-register

Surface and track the implicit assumptions underlying each active bet. The bet thesis rests on assumptions — if the assumptions fail, the thesis fails before the kill condition triggers. This is the earliest warning layer in the strategy stack.

## When to Use

- Monthly, before running `/strategy-review` — surfaces at-risk assumptions so verdicts are informed
- When a bet's evidence log has been updated and you want to check assumption status
- When a signal or competitive move makes you wonder if a bet's foundation is sound

**Do NOT use for:**
- Reviewing evidence and issuing verdicts → `/strategy-review`
- Logging new evidence → `/bet update`
- Full horizon scan → `/horizon`

## Inputs

- No argument: full register for all active bets
- `[BET-ID]`: register for one specific bet
- `--risk`: show only assumptions with status At risk or Violated

## Assumption Status Taxonomy

| Status | Definition |
|--------|-----------|
| Untested | No evidence in the log that bears on this assumption |
| Tested-held | Evidence log contains observations on this assumption; it still holds |
| At risk | Disconfirming evidence in the log challenges this assumption |
| Violated | The assumption has been observably falsified — thesis needs reassessment |

---

## Workflow

**Step 1 — Read active bets.**

Read `strategy/active-bets.md`. If no active bets: report "No active bets to analyze" and exit.

If a specific BET-ID was given: confirm it exists, then load only that bet.

**Step 2 — Load bet files.**

For each target bet: read `strategy/bets/[BET-ID].md`. Extract:
- The thesis (the belief about how the world works)
- The kill condition
- The full evidence log (all dated entries with confirming and disconfirming observations)

**Step 3 — Derive implicit assumptions.**

From the thesis and kill condition, derive 3-5 key assumptions — the things that would need to be true for the thesis to hold.

Each assumption should be:
- Falsifiable: you could observe evidence that challenges it
- Specific: "users will pay more for X" not "there is demand"
- Causal: it explains WHY the thesis works, not just restates it

Label each: **A1**, **A2**, **A3**, etc.

**Step 4 — Scan the evidence log for assumption challenges.**

For each assumption, scan the evidence log entries. Look for:
- Disconfirming observations that specifically challenge this assumption
- Confirming observations that specifically support it
- Absence of any evidence bearing on this assumption (→ Untested)

Assign status:
- **Untested** — no evidence log entry mentions or implies this assumption
- **Tested-held** — evidence exists and the assumption still stands
- **At risk** — disconfirming evidence challenges the assumption (note which entry)
- **Violated** — evidence directly and strongly falsifies the assumption

**Step 5 — Surface the register.**

```
Assumption Register — [YYYY-MM-DD]
════════════════════════════════════

BET-YYYY-NNN — [Bet Name]  |  [H1/H2/H3]  |  Last updated: [date]
  Thesis: [one sentence]
  Kill condition: [kill condition text]

  Assumptions
  A1. [assumption]
      Status: Untested
      Evidence: —

  A2. [assumption]
      Status: Tested-held
      Evidence: "[specific confirming observation from log, date]"

  A3. [assumption]                                     ← ⚠ AT RISK
      Status: At risk
      Evidence: "[specific disconfirming observation from log, date]"
      Consider: /bet update BET-YYYY-NNN to log a verdict on this assumption.

  A4. [assumption]
      Status: Untested
      Evidence: —

[Repeat per bet]

══════════════════════════════════════

Summary
  Bets analyzed       : [N]
  Total assumptions   : [N]
  At risk             : [N]  ← requires attention before /strategy-review
  Violated            : [N]  ← thesis may need reassessment
  Untested            : [N]  ← actively monitor; absence of evidence is not safety
  Tested-held         : [N]
```

**Step 6 — Flag critical conditions.**

If any assumption is Violated:
```
⚠ VIOLATED assumption in [BET-ID]: [assumption text]
This means the bet thesis may no longer hold.
Run /bet update [BET-ID] and consider a Kill verdict in the next /strategy-review.
```

If `--risk` flag used: show only At risk and Violated assumptions with their bets. Skip Untested and Tested-held.

## Quality Gate

- [ ] Bet files actually read — not derived from memory
- [ ] Assumptions derived from the thesis and kill condition — not generic risks
- [ ] Evidence log scanned per-assumption — not as a bulk read
- [ ] Status assigned from evidence — "Untested" is not the same as "safe"
- [ ] At-risk and Violated assumptions surface specific evidence entries with dates
- [ ] `/bet update` offered for at-risk assumptions — assumption register is diagnostic, not prescriptive
- [ ] If no active bets: exits cleanly rather than producing empty output
