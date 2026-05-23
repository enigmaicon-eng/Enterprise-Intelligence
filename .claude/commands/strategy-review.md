# /strategy-review — Periodic Strategic Review

Run a structured periodic strategy review: evaluate the bet portfolio, check OKR signal quality, scan horizons, and surface what you were wrong about. Produces verdicts — not observations.

## Trigger
`/strategy-review` — monthly review (default)
`/strategy-review quarterly` — quarterly review with deeper horizon analysis
`/strategy-review [YYYY-MM]` — review for a specific past period

## Distinct from Other Reviews
- `/synthesize` generates a cross-domain knowledge synthesis — not a strategy review
- `/exec-review weekly` assesses execution health — not strategic posture
- `/strategy-review` answers "are our bets still right?" — strategy layer only

## Protocol

### Step 0: Silent context load
Read in order:
1. `memory/MEMORY.md`
2. `strategy/active-bets.md` — the live portfolio
3. `strategy/OKRs.md` — current objectives and key results
4. Previous strategy review (most recent in `strategy/reviews/`) — what did we say last time?

### Step 1: Bet portfolio review
For each active bet in `strategy/active-bets.md`:

**Rule: Read the kill condition before looking at any other evidence.**

1. Is the kill condition triggered? If yes, verdict is Kill regardless of other evidence.
2. What confirming evidence arrived this period? Name specific observations.
3. What disconfirming evidence arrived? If none observed, ask: did we look?
4. Signal quality: is the evidence measuring what the thesis claims?
5. Produce one of four verdicts: **Continue | Adjust | Double down | Kill**

No other verdicts are valid. "Monitor" is not a verdict.

### Step 2: OKR progress check
For each active objective:
- Progress: [current vs. target]
- Signal quality check: does this KR actually measure the outcome the objective is pursuing?
- Noisy/lagging KRs get flagged — note what better signal would look like
- Recommendation: On track / Needs adjustment / Retire the objective

### Step 3: Horizon scan (abbreviated)
H1: Any execution window closing or bet ready to close?
H2: What changed in the environment affecting build-zone bets?
H3: Any H3 option whose value has changed materially?

For a quarterly review, run full `/horizon` instead of this abbreviated scan.

### Step 4: What I Was Wrong About
This section is mandatory. Review what was said in the previous strategy review.

What was predicted? What actually happened? What does this change?

If nothing was wrong, the review is incomplete — look harder.

### Step 5: Write the strategy review
Use `templates/strategic-review.md`.
Write to: `strategy/reviews/[YYYY-MM].md` (monthly) or `strategy/reviews/[YYYY]-Q[N].md` (quarterly)

### Step 6: Log decisions
For each Kill, Adjust, or major Pivot verdict: run `/decide` to log the decision with rationale in `decision-frameworks/decisions-log.md`. Strategic verdicts must be traceable.

### Step 7: Schedule postmortems
For each killed bet: schedule a postmortem within 7 days.
Note the bet ID and target date in `execution/action-items.md`.

### Step 8: Report
- Bet verdicts: [N continue, N adjust, N double-down, N kill]
- OKR health summary
- Top strategic question for next period
- Decisions logged

## Quality Bar
The review fails if:
- Any bet exits without an explicit verdict
- "What I Was Wrong About" is empty or generic ("we could always improve")
- Kill verdicts aren't logged as decisions
- Postmortems aren't scheduled for killed bets
