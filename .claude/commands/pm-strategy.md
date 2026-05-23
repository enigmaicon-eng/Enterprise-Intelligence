---
name: pm-strategy
description: Articulate and stress-test product strategy using the five-question framework. Surfaces gaps, unclear assumptions, and strategy-roadmap disconnects.
version: "1.0"
changed: 2026-05-20
---

# PM Strategy

**Input:** Strategy context inline, or reference to existing strategy doc/OKR set.

**Output:** Written to `reviews/strategy/YYYY-MM-DD-strategy-check.md`

---

## Steps

1. **Read context.** Load `knowledge/pm/product-strategy.md`. If user references an existing strategy doc, read it.

2. **Run the five-question framework:**
   - What game are we playing? (market + winning mechanism)
   - Why can we win? (durable advantage — specific, not generic)
   - What must be true? (3-5 falsifiable assumptions)
   - What are we explicitly NOT doing? (trade-offs named)
   - How will we know if we're winning? (leading indicator with threshold)

3. **Identify vagueness.** For each answer, flag: Is this precise and defensible, or is it hiding uncertainty? Vague answers must be named — not smoothed over.

4. **Run the four stress tests:**
   - Competitor test: name 3 moves a competitor could make that undermine H2 bets
   - User test: does the strategy reflect what discovery has taught us in the last 90 days?
   - Engineering test: are there technical decisions/constraints not reflected in the strategy?
   - Kill test: which bets have hit their kill criteria and haven't been acknowledged?

5. **Identify the three horizon placements.** For each current initiative: H1 (execution confidence), H2 (validation bets with kill conditions), H3 (option value). Flag initiatives without clear horizon assignment.

6. **Write the output.**

---

## Output Format

```markdown
# Strategy Check — [Date]

## Strategy Statement (one paragraph)
[Precise. Falsifiable. A reasonable person could disagree with it.]

## Five-Question Answers

**What game:** [Market + mechanism]
**Why win:** [Specific durable advantage]
**Must be true:**
  1. [Assumption] — Confidence: H/M/L — Evidence: [brief]
  2. [Assumption] — Confidence: H/M/L — Evidence: [brief]
  3. [Assumption] — Confidence: H/M/L — Evidence: [brief]
**Not doing:** [3 explicit exclusions with rationale]
**Winning signal:** [Metric + threshold + timeline]

## Strategy Gaps
[Where answers were vague or missing — specific, not general]

## Stress Test Results
- Competitor test: [Finding]
- User test: [Finding]
- Engineering test: [Finding]
- Kill test: [Finding — any bets past their criteria?]

## Horizon Coverage
- H1 (execution): [initiatives]
- H2 (validation): [initiatives + kill conditions]
- H3 (options): [initiatives]
- Unassigned: [initiatives needing assignment]

## Top 3 Risks to Strategy

| Assumption | Falsification condition | By when |
|---|---|---|
| [#1] | [Observable signal] | [Date] |
| [#2] | [Observable signal] | [Date] |
| [#3] | [Observable signal] | [Date] |

## Kill Condition
If [specific event] by [date], strategy requires revision.

## Next Review: [Date — quarterly default]
```

---

## Quality Gate

- Strategy statement is falsifiable (a reasonable person could disagree)
- Every assumption has a falsification condition
- NOT-doing list has ≥3 explicit items
- All H2 bets have kill conditions
- Gaps are named, not hidden
