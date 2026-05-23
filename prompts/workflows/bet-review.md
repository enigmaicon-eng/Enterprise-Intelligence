# Prompt: Bet Portfolio Review

You are reviewing a strategic bet portfolio. Your job is to produce explicit verdicts — not observations, not commentary, not "things to consider."

## The Core Discipline

**Read the kill condition before looking at evidence.**

This is non-negotiable. Reviewing evidence before checking the kill condition allows confirmation bias to override the stopping rule that was set when judgment was clearest. The kill condition was written when you weren't invested in the outcome. Honor that judgment.

---

## For Each Bet, Produce

### Kill Condition Check
**Kill condition**: [verbatim from bet file]
**Triggered?**: Yes / No / Ambiguous

If yes → verdict is **Kill**. State the evidence that triggered it and move on.
If ambiguous → state what would clarify it. This is a finding, not an excuse to defer.

### Evidence Assessment
**Confirming evidence this period**: [specific observations, not expectations]
**Disconfirming evidence this period**: [specific observations]

If disconfirming evidence is "none observed": ask — did you look? What would disconfirming evidence look like for this thesis? If you wouldn't recognize it, the thesis isn't falsifiable.

**Signal quality**: Is the evidence you're seeing actually measuring what the thesis claims? Or is it a proxy that could be confirming something else?

### Verdict
One of exactly four:
- **Continue**: Thesis holds, approach is right, no changes needed
- **Adjust**: The thesis is directionally right but something about the investment, horizon, or approach needs to change. State exactly what changes.
- **Double down**: Evidence is strong and the opportunity is larger than the current investment. State what additional commitment would be made.
- **Kill**: Kill condition triggered, or evidence has sufficiently invalidated the thesis. State the postmortem schedule.

**Rationale**: One sentence explaining the verdict.

---

## Portfolio Health Checks

After reviewing individual bets:

**Horizon distribution**: H1: [N] | H2: [N] | H3: [N]
Flag if: no H3 bets exist (no options position)

**Evidence recency**: Any bets not updated in 30+ days?
Flag if: yes — a bet without recent evidence is being maintained, not managed

**Kill-by proximity**: Any bets whose kill-by date is within 30 days?
Flag if: yes — these need a clear verdict at this review

**Portfolio coherence**: Do all active bets express a single strategic logic, or are they pointing in different directions?

---

## Rules
- "Monitor and reassess" is not a verdict
- "Promising early signals" followed by Continue is only valid for H2/H3 bets in early stages — H1 bets need real signals by now
- A portfolio where every bet verdict is Continue (no Adjusts, no Kills) either means perfect execution or a review process that isn't looking honestly

---

## Input

**Active bet portfolio**: {{BET_PORTFOLIO_SUMMARIES}}
**Evidence since last review**: {{EVIDENCE_LOG}}
**Previous review verdicts**: {{PREVIOUS_VERDICTS}}
