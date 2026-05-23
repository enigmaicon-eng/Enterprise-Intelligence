---
title: Decision Retrospective — Quality Review of Past Decisions
domain: decisions
created: 2026-05-21
reviewed: 2026-05-21
tags: [decisions, retrospective, quality, judgment, calibration]
connections: [decision-patterns, mental-models, bets-history]
confidence: low
source: original synthesis
---

## Definition
A decision retrospective is a periodic audit of decision quality — not whether outcomes were good (luck affects outcomes), but whether the decision process was sound given what was known at the time. Good process + bad outcome is recoverable. Bad process + good outcome is dangerous, because it teaches the wrong lesson.

## Why It Matters
Without retrospectives, decision quality doesn't improve — it just accumulates anecdotally. Systematic retrospectives surface calibration patterns (are we systematically over- or under-confident?), process failures (which steps in the decision protocol are being skipped?), and domain-specific blind spots (where does judgment most often fail?).

## Retrospective Protocol

Run quarterly, concurrent with the quarterly strategy review.

For each significant decision logged in `decision-frameworks/decisions-log.md` in the past quarter:

### Process Audit
1. Was the decision made explicitly or by default? (Default decisions — where inaction is the decision — are the most common quality failure)
2. Were options considered, or was the first option taken?
3. Were assumptions named at decision time?
4. Was a review date set? Was it honored?

### Outcome Check (for decisions 90+ days old)
1. What was the expected outcome?
2. What actually happened?
3. Was the outcome driven by the decision quality or by luck/circumstances?
4. If the outcome was bad: was the decision bad, or was it a good decision in an uncertain environment that happened to go wrong?

### Calibration Check
Are we systematically:
- **Overconfident**: Decisions that were marked "high confidence" that turned out wrong more than 30% of the time?
- **Under-scoped**: Decisions made without naming the alternatives?
- **Assumption-blind**: Decisions where assumptions weren't named and later proved to be the actual decision driver?
- **Review-avoidant**: Decisions where review dates were set but not honored?

---

## Retrospective Log

*(Quarterly entries added here)*

### Q[N] YYYY Retrospective

**Period**: YYYY-MM-DD to YYYY-MM-DD
**Decisions reviewed**: N
**Decisions with outcomes available**: N

**Process quality summary**:
- Explicit decisions (vs. default): [%]
- Decisions with named alternatives: [%]
- Decisions with named assumptions: [%]
- Decisions with honored review dates: [%]

**Calibration summary**:
- High-confidence decisions that held: [N/N]
- Systematic bias observed: [overconfident / under-confident / no clear pattern]

**Patterns extracted this quarter**: [list → add to decision-patterns.md]

**One thing to change in the decision protocol**: [specific]

---

## Connections
- [[decision-patterns]] — patterns extracted from retrospectives live here
- [[mental-models]] — the reversibility filter and other models are evaluated here
- [[bets-history]] — bet postmortems feed into decision retrospectives

## Open Questions
- Is quarterly the right cadence, or should retrospectives be triggered by decision density (N decisions in a period) rather than calendar time?
- How do you distinguish between "bad decision" and "bad outcome from a good decision" reliably?

## Referenced By
<!-- Populated as other notes link to this one -->
