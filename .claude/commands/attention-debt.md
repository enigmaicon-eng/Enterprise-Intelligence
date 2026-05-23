---
name: attention-debt
description: >-
  Strategic attention alignment analysis — compares where attention has
  actually been going (trace history, recent work) against where the strategy
  says it should go (active bets by horizon, investment levels). Surfaces
  attention debt (high-priority areas getting no attention) and attention sinks
  (areas absorbing attention without strategic weight). Distinct from
  /exec-allocation (work type distribution) and /cognitive-load (aggregate
  load). Run monthly or before a strategy review. Requires active-bets.md and
  ≥10 recent traces for meaningful signal.
version: "1.0"
changed: "2026-05-23 — initial"
output: inline (attention alignment report)
---

# /attention-debt — Strategic Attention Alignment

## When to Use

- Monthly check: is actual work aligned with strategic priorities?
- Before `/strategy-review`: understand where attention has been before issuing verdicts
- When a bet feels neglected but you're not sure if it actually is
- After a high-interrupt month to assess strategic drift
- Setting next month's learning or execution priorities

**Do NOT use for:**
- Work type distribution (strategic/reactive/overhead) → `/exec-allocation`
- Aggregate cognitive load → `/cognitive-load`
- Learning domain growth rates → `/learning-velocity`
- Execution throughput trends → `/exec-throughput`

**Requires ≥10 traces in TRACE-INDEX.md for meaningful attention signal. Requires `strategy/active-bets.md` to be current.**

---

## Input

```
/attention-debt              ← Full attention alignment report (last 30 days)
/attention-debt --60         ← Last 60 days
/attention-debt --bet <id>   ← Deep dive on one specific bet
```

---

## Process

### Step 1 — Build the priority signal

Read `strategy/active-bets.md`. For each active bet, extract:
- Bet ID and name
- Horizon: H1 (urgent, now) / H2 (building, next 6 months) / H3 (exploring, future)
- Investment level: High / Medium / Low (or derive from horizon if not explicit)
- Status: Active / Monitoring / At risk

Assign a **priority weight** per bet:
- H1 Active: weight 3 (highest — deserves regular attention)
- H2 Active: weight 2 (should appear regularly)
- H3 Active / Monitoring: weight 1 (periodic check-in sufficient)
- At risk (any horizon): weight +1 bonus (elevated attention warranted)

Also note declared strategic domains from bet names (domains the bets operate in).

### Step 2 — Build the attention signal

Read `traces/TRACE-INDEX.md`. Extract execution episodes in the target period.

For each episode, scan the goal and tags to classify which bet(s) or domain(s) it relates to. Classification:
- Explicit bet ID in goal or tags → map directly
- Domain keyword matching → map to highest-weight bet in that domain
- No match → classify as "Unattributed"

Build a per-bet attention count: how many sessions touched this bet in the period?

Also scan `strategy/signals/[YYYY-MM].md` for signal entries — signals reviewed for a bet's domain count as attention signal.

### Step 3 — Compute attention alignment

For each active bet:
- **Attention score**: session count touching this bet in the period
- **Expected attention**: proportional to priority weight (high-weight bets should have more sessions)
- **Alignment ratio**: attention score ÷ expected attention (1.0 = exactly aligned; <0.5 = under-attended; >2.0 = over-attended)

**Attention debt**: bets where alignment ratio < 0.3 — getting less than 30% of expected attention.
- H1 Active with 0 sessions in last 14 days: attention debt **emergency** (flag immediately).

**Attention sink**: domains/topics where sessions exist but no active bet is associated — attention is going somewhere without strategic purpose.

### Step 4 — Identify drift patterns

If the same bet has shown attention debt for >2 consecutive monthly checks (if prior /attention-debt runs are in traces): this is structural drift, not temporary neglect. Recommend a bet review or explicit deprioritization.

---

## Output Format

```
ATTENTION ALIGNMENT — [date range]
[N] traces analyzed  |  [N] active bets

PRIORITY SIGNAL (from strategy/active-bets.md)
Bet                      | Horizon | Weight | Status
-------------------------|---------|--------|-------
[bet name]               |   H1    |   3    | Active
[bet name]               |   H2    |   2    | Active
[bet name]               |   H2    |   3    | At risk
[bet name]               |   H3    |   1    | Monitoring

ATTENTION DISTRIBUTION
Bet                      | Sessions | Alignment | Assessment
-------------------------|----------|-----------|----------
[bet name]               |    [N]   |   [X]x    | [Aligned / Under / DEBT / Sink]
[bet name]               |    [N]   |   [X]x    | ...
Unattributed             |    [N]   |    —      | [% of total]

ATTENTION DEBT (alignment ratio < 0.3)
⚠  [bet name] — [N] sessions in [N] days  [H1 + 0 sessions → EMERGENCY if applicable]
   Expected: [N] sessions at H[N] weight
   Last touched: [date or "no sessions found in period"]
   Recommended: [/bet update / /signal review / schedule a session]

[If none:] ✓  No attention debt detected.

ATTENTION SINKS ([N] sessions without strategic attribution)
[domain/topic] — [N] sessions — no associated active bet
  → Consider: is this pre-bet exploration (capture with /signal) or drift (reduce)?

[If none:] ✓  All attention maps to active bets.

INTERPRETATION
[2-3 sentences: what the attention distribution reveals about strategic alignment,
 and the single most important redirection to make]
[If strategy/active-bets.md is current and all bets are aligned: say so clearly]
```

---

## Quality Gate

Before outputting:
- [ ] `strategy/active-bets.md` read and all active bets extracted with horizon labels
- [ ] Priority weights applied from the model (H1=3, H2=2, H3=1, At risk +1)
- [ ] Attention classification from actual trace goals/tags, not assumed
- [ ] H1 bets with 0 sessions in 14 days flagged as EMERGENCY regardless of overall alignment
- [ ] Unattributed sessions reported as % of total (reveals how much work is off-strategy)
- [ ] If <10 traces: note "Insufficient trace history for attention signal. Build trace history first."
- [ ] If active-bets.md is absent or empty: note this and skip — attention debt without a priority signal is undefined
- [ ] Interpretation is 2-3 sentences maximum with one specific redirection
