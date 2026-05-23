# Strategy Articulation Prompt
## Forcing Clarity on What the Strategy Actually Is

**Use when:** You need to articulate (or test) the product strategy — before a planning cycle, before a leadership review, or when there's misalignment about direction. Also use when you suspect the strategy exists as a vague shared understanding rather than a precise, testable claim.

**Principle from `knowledge/pm/product-strategy.md`:** Strategy is a coherent theory about how to win. Not a set of features. Not a list of OKRs. Not a roadmap. A theory that answers: what game are we playing, why can we win it, what must be true for the theory to hold.

---

## The Prompt — Strategy Clarity Test

```
Help me articulate and stress-test the product strategy using the five-question framework.

CONTEXT:
- Product/team: [Name and brief description]
- Current strategy statement (if any): [Paste existing strategy doc, OKRs, or roadmap themes]
- Current moment: [What strategic inflection is happening? E.g., new competitor, market shift, scale milestone]
- Time horizon being addressed: [H1 (0-6mo) / H2 (6-18mo) / H3 (18mo+)]

FIVE-QUESTION STRESS TEST:
Answer each question as precisely as possible. Where you can't answer precisely, note what's unclear.

1. What game are we playing?
   [Define the market and the competition. Who wins in this market and by what mechanism?]

2. Why can we win?
   [Name the durable advantage — not "we move fast" or "we care about users." What do we have or know that competitors don't?]

3. What must be true for this strategy to work?
   [Name the 3-5 assumptions the strategy rests on. These are falsifiable claims, not wishes.]

4. What are we explicitly NOT doing?
   [Name 3 things that would be good ideas but that this strategy deliberately excludes.]

5. How will we know if we're winning?
   [Name the leading indicator that would confirm or refute the strategy within 90 days.]

SYNTHESIS INSTRUCTIONS:
After answering, identify:
- Which answers are precise and defensible?
- Which answers are vague (and therefore hiding uncertainty)?
- Which assumptions are highest-risk and least validated?
- Where does the strategy have gaps or internal contradictions?

Then produce:
- A one-paragraph strategy statement that a new team member could act on
- The top 3 riskiest assumptions with falsification conditions
- The one thing that, if proven false, would require the strategy to change
```

---

## Output Template

```markdown
# Strategy Articulation — [Product/Team] — [Date]

## The Strategy (one paragraph)
[Precise statement. No more than 100 words. Should be falsifiable — a reasonable person should be able to disagree with it.]

## Five-Question Answers

**What game are we playing?**
[Answer]

**Why can we win?**
[Durable advantage — specific, not generic]

**What must be true?**
1. [Assumption] — Confidence: H/M/L — Current evidence: [brief]
2. [Assumption] — Confidence: H/M/L — Current evidence: [brief]
3. [Assumption] — Confidence: H/M/L — Current evidence: [brief]

**What are we NOT doing?**
- [Explicit exclusion + one-sentence rationale]
- [Explicit exclusion + one-sentence rationale]
- [Explicit exclusion + one-sentence rationale]

**How will we know if we're winning?**
Leading indicator: [Metric or observable signal]
Timeline: [When we'd expect to see movement]
Threshold: [What "winning" looks like on this signal]

## Strategy Gaps
[Where the answers were vague, contradictory, or missing]

## Top Risks to the Strategy

| Assumption | What would prove it false | By when we'd know |
|---|---|---|
| [#1] | [Falsification condition] | [Date] |
| [#2] | [Falsification condition] | [Date] |
| [#3] | [Falsification condition] | [Date] |

## Kill Condition
If [specific observable event] occurs by [date], the strategy requires revision.
```

---

## Quality Gates

- [ ] The strategy statement takes a position a reasonable person could disagree with (if not, it's not a strategy)
- [ ] The durable advantage is specific to this team/product, not generic ("better execution" is not an advantage)
- [ ] Assumptions are falsifiable — each has a condition under which it would be proven wrong
- [ ] The NOT-doing list includes at least one thing that stakeholders have explicitly asked for
- [ ] The leading indicator is a leading indicator, not a lagging one (revenue is lagging; activation rate is leading)

---

## Common Failures

**The strategy that describes activity:** "We will invest in [capability], [capability], and [capability]." This is a roadmap, not a strategy. A strategy explains why those investments will produce a competitive outcome.

**The unfalsifiable advantage:** "We have the best team." No observable condition would disprove this. A real advantage: "We have 18 months of proprietary training data that competitors cannot replicate."

**The strategy without NOT:** A strategy that doesn't say what it's not doing is not making a trade-off — it's trying to do everything. Trade-offs are the essence of strategy.

**The abstract leading indicator:** "We'll know it's working when users love the product." How will you measure love? When? What threshold? Name the metric.
