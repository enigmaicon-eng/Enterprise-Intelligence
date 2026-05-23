---
title: Bet Postmortem — [Bet Name]
bet_id: BET-YYYY-NNN
outcome: won | cut
close_date: YYYY-MM-DD
horizon: H1 | H2 | H3
duration: [N months from open to close]
postmortem_date: YYYY-MM-DD
conducted_by: [name]
---

## Bet Summary
One paragraph recapping what the bet was, what was invested, and how it closed. Write for someone who hasn't read the bet file.

---

## What Was Predicted vs. What Happened

| Dimension | Predicted (at bet creation) | Actual |
|-----------|---------------------------|--------|
| Outcome | [thesis prediction] | [what actually occurred] |
| Timeline | [horizon classification] | [how long it actually took] |
| Investment | [what was committed] | [what was actually spent] |
| Kill condition | [stated condition] | [was it triggered? was it the right condition?] |

---

## The Thesis Audit
Read the original thesis. Do not rewrite it.

**Original thesis**: [verbatim from bet file]

**Was the thesis correct?** Yes / Partially / No

**What part of the thesis was wrong?**
Name the specific belief that turned out to be false. Be precise — "the market" or "timing" are not specific enough.

**Why was it wrong?**
- Was it wrong from the beginning (bad reasoning at the time)?
- Was it right at the time but conditions changed?
- Was it right but execution failed to realize it?

---

## Evidence Quality Audit

**Confirming evidence actually observed**: [what happened that supported the thesis]
**Disconfirming evidence actually observed**: [what happened that challenged it]

**Were we looking for disconfirming evidence?** Yes / No / We looked but didn't find it / We found it but discounted it

**Signal quality**: Did we have the right metrics and observations to evaluate the thesis? What would better signal have looked like?

---

## Kill Condition Audit

**Kill condition stated**: [verbatim from bet file]

**Was the kill condition triggered?** Yes / No / Ambiguous

**If the bet was cut and the kill condition wasn't triggered**: What actually caused the cut? This is a signal that the kill condition was wrong — extract the better kill condition.

**If the bet was won and the kill condition was never close**: Was the kill condition too strict? Not strict enough? Did it measure the right thing?

**Kill condition improvement**: What would a better kill condition have looked like for this bet?

---

## Assumption Audit

For each assumption listed in the bet file:

| Assumption | Confirmed / Invalidated / Never tested | When it became clear |
|-----------|---------------------------------------|---------------------|
| [Assumption 1] | | |
| [Assumption 2] | | |
| [Assumption 3] | | |

**Which assumption most determined the outcome?** The single assumption that mattered most.

---

## Decision Quality Audit
Were the monthly review verdicts (Continue / Adjust / Double down / Kill) correct in hindsight?

| Review date | Verdict given | Verdict in hindsight | Delta |
|------------|--------------|---------------------|-------|
| | | | |

**Pattern**: Were we systematically too optimistic / too conservative / too slow to act?

---

## What Would We Do Differently?
Not "work harder" or "move faster." Specific decision points where a different choice would have changed the outcome.

1. **Decision point**: [specific moment] — **Different choice**: [what to do instead] — **Why**: [reasoning]
2. ...

---

## Pattern Extraction
What generalizable pattern(s) does this postmortem reveal? These feed `knowledge/decisions/decision-patterns.md`.

### Pattern: [Name]
- **Context**: When does this pattern apply?
- **Lesson**: What the pattern teaches
- **How to apply next time**: Specific different behavior

→ Add to `knowledge/decisions/decision-patterns.md`: [pattern name]
→ Add to `strategy/[year]/bets-history.md`: one-row summary
