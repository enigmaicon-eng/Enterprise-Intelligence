---
name: pm-opportunity
description: Run a structured opportunity assessment before committing to a new initiative or bet. Evaluates market size, user need, strategic fit, competitive window, and resource feasibility.
version: "1.0"
changed: 2026-05-20
---

# PM Opportunity

**Input:** Problem or opportunity description, target user, any known context on market size or competitive dynamics.

**Output:** Written to `notes/structured/opportunity-YYYY-MM-DD-<slug>.md`

**When to run:** Before a problem goes on the roadmap as a committed initiative. Prevents "we built it and nobody came" failures.

---

## Steps

1. **Read context.** Load `knowledge/pm/product-strategy.md` (three-horizon model and portfolio thinking section). Load `decision-frameworks/pm/prioritization-playbook.md` (strategic alignment gate).

2. **Run the strategic alignment gate first.** Before any further analysis:
   - Which strategy assumption does this opportunity test or advance?
   - Which horizon does it belong to?
   - If the strategy is wrong, does this still create value?
   - If it can't answer these: it goes to the parking lot.

3. **Define the problem precisely.** Opportunity assessment begins with a specific problem for a specific user, not a market category. "Small business invoicing" is a market. "Small business owners who manually reconcile invoices from >5 clients lose 4+ hours/week on a task that creates no competitive advantage" is a problem.

4. **Assess the opportunity size.**
   - How many users have this problem? (TAM at problem level, not market level)
   - What's the frequency and intensity? (Daily pain vs. once-a-quarter inconvenience?)
   - What's the workaround sophistication? (Elaborate workarounds = validated pain)
   - What would users pay or do differently if this problem were solved?

5. **Assess the competitive window.**
   - Does a good solution already exist? Why haven't users adopted it?
   - What timing advantage do we have (if any)?
   - What would it take for a competitor to close this gap?

6. **Assess our right to win.**
   - Do we have a defensible advantage for solving this? (Data, distribution, domain expertise, existing user trust)
   - Can we solve this better than alternatives? Why?
   - What would we need to build that others can't easily replicate?

7. **Assess the feasibility.**
   - What's the rough effort to validate the opportunity? (Discovery sprint vs. full initiative)
   - What's the rough effort to execute if validated?
   - What dependencies exist (technical, data, partnerships)?

8. **Produce a recommendation.** One of: Invest (full initiative) / Explore (discovery sprint first) / Monitor (watch but don't invest) / Pass (not for us).

9. **Write the output.**

---

## Output Format

```markdown
# Opportunity Assessment — [Problem/Opportunity Name] — [Date]

**PM:** [name]  **Status:** Draft | Decision pending | Decided

---

## Strategic Alignment Gate

- **Strategy assumption advanced:** [Which assumption this tests or confirms]
- **Horizon:** H1 | H2 | H3
- **Value if strategy changes:** [Yes — standalone value / No — strategic value only]

**Gate result:** ✓ Pass | ✗ Parking lot

---

## Problem Definition

**Specific problem:** [One paragraph — who, what, frequency, intensity]

**Workaround evidence:** [What users currently do to solve this — elaborate workarounds = strong signal]

**User quote (if available):** "[Verbatim quote from discovery that illustrates the pain]"

---

## Opportunity Size

| Dimension | Assessment | Evidence |
|---|---|---|
| Users affected | [N estimate] | [Source] |
| Frequency of pain | Daily / Weekly / Monthly / Occasional | [Source] |
| Intensity | High (workflow blocker) / Medium / Low | [Source] |
| Willingness to pay / act | [What users would do to solve this] | [Source] |

**Opportunity score:** [Ulwick formula: Importance + max(Importance - Satisfaction, 0) — range 10-20]
- Importance: [1-10] — Satisfaction with current solutions: [1-10] → Score: [N]

---

## Competitive Window

- **Existing solutions:** [What exists — why users haven't fully adopted]
- **Timing advantage:** [Why now vs. 12 months ago / 12 months from now]
- **Competitive durability:** [How long before others close the gap if we move first]

---

## Our Right to Win

- **Defensible advantage:** [Specific — data, distribution, trust, expertise]
- **Why us vs. alternatives:** [Specific capability or position advantage]
- **Moat potential:** [What compounds over time if we win here]

---

## Feasibility

| Dimension | Assessment |
|---|---|
| Discovery effort (to validate) | [N weeks] — [method: interviews / analytics / experiment] |
| Build effort (if validated) | [N person-weeks estimate — very rough] |
| Key dependencies | [Technical / data / partner / organizational] |
| Risk of not solving | [What happens to users / business if we don't solve this] |

---

## Recommendation

**Decision:** Invest (full initiative) | Explore (discovery sprint) | Monitor | Pass

**Rationale:** [2-3 sentences — why this recommendation]

**If Explore:** What specific question does the discovery sprint answer?

**If Invest:** What's the first milestone and success criterion?

**If Monitor:** What would change this to Explore or Invest?

**If Pass:** What conditions would change this recommendation?

**Decision needed from:** [PM lead / leadership / none]  
**Decision by:** [Date]
```

---

## Quality Gate

- Problem statement names a specific user and a specific pain (not a market category)
- Opportunity size includes frequency AND intensity (not just headcount)
- Workaround evidence cited (users' workarounds are the best signal of problem validity)
- "Right to win" is specific — not "we have a great team"
- Recommendation is one of four options with explicit rationale
- If Explore: the specific discovery question is stated
