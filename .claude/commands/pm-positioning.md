---
name: pm-positioning
description: Develop or stress-test a competitive positioning statement. Produces a positioning formula, differentiation map, category framing, and messaging hierarchy for sales and marketing.
version: "1.0"
changed: 2026-05-20
---

# PM Positioning

**Input:** Product/feature description, target segment, competitive alternatives, and any existing positioning statement.

**Output:** Written to `notes/structured/positioning-YYYY-MM-DD.md`

---

## Steps

1. **Read context.** Load `knowledge/pm/competitive-intelligence.md` (positioning section). If a competitive analysis exists, read it for context.

2. **Confirm the target segment is specific.** Positioning is only meaningful relative to a specific segment. "Everyone" cannot be positioned to. If the segment is too broad, position to the primary buyer persona first, then adapt for secondary.

3. **Write the positioning statement using the full formula:**
   - For [target user segment] who [have this specific need],
   - [Product name] is the [category] that [primary differentiator]
   - because [proof point],
   - unlike [primary alternative] which [alternative's limitation].

4. **Stress-test the statement:**
   - Is the segment specific enough that they would recognize themselves?
   - Is the category correct? (Claiming to be in the wrong category creates cognitive dissonance)
   - Is the differentiator truly different, or do competitors claim the same thing?
   - Is the proof point verifiable and compelling?
   - Is the alternative the one the target user actually considers?

5. **Map the differentiation.** On the dimensions that matter most to the target segment, where does the product stand vs. alternatives? A differentiation map reveals where the positioning is genuinely defensible vs. aspirational.

6. **Develop the messaging hierarchy.** Three tiers:
   - **Headline:** One sentence — the primary claim (what makes us different, for whom)
   - **Value props (3 max):** The three reasons the claim is true — each supported by proof
   - **Proof points:** Specific evidence for each value prop (data, customer stories, capabilities)

7. **Write the output.**

---

## Output Format

```markdown
# Positioning — [Product/Feature] — [Date]

**Target segment:** [Specific — role + context + need]  
**Primary alternative:** [What users actually use instead]

---

## Positioning Statement

For [target segment] who [specific need],  
[Product] is the [category] that [differentiator]  
because [proof point],  
unlike [primary alternative] which [limitation].

---

## Positioning Stress Test

| Criterion | Assessment | Improvement needed |
|---|---|---|
| Segment recognition | [Would they identify with "for [segment]"?] | |
| Category accuracy | [Is this the right category?] | |
| Differentiator uniqueness | [Do competitors claim the same?] | |
| Proof verifiability | [Is there evidence?] | |
| Alternative accuracy | [Is this what they actually consider?] | |

**Weakest element:** [Which criterion fails most — and what would fix it]

---

## Differentiation Map

Dimensions that matter most to [target segment]:

| Dimension | Us | Primary alternative | Secondary alternative |
|---|---|---|---|
| [Dimension 1] | [Strong/Medium/Weak] | | |
| [Dimension 2] | | | |
| [Dimension 3] | | | |

**Defensible differentiation:** [Where we're genuinely stronger — hard to replicate]  
**Parity dimensions:** [Where we match alternatives — table stakes]  
**Gap dimensions:** [Where we're weaker — acknowledged or in progress]

---

## Messaging Hierarchy

**Headline (one sentence):**  
[The primary claim — what we are for whom, in one sentence]

**Value Proposition 1:** [Claim]  
→ Proof: [Specific evidence — data point, customer example, capability]

**Value Proposition 2:** [Claim]  
→ Proof: [Specific evidence]

**Value Proposition 3:** [Claim]  
→ Proof: [Specific evidence]

---

## Positioning Anti-Patterns Caught

- [ ] Feature positioning (claiming "we have X, Y, Z features" instead of outcomes)
- [ ] Category confusion (claiming to be in a category where we're not strongest)
- [ ] Aspirational positioning (claiming to be something we're not yet)
- [ ] Me-too positioning (same claim as primary alternative)

---

## Usage Notes

**Sales:** Use positioning statement as the frame for first qualification conversations.  
**Marketing:** Headline + 3 value props are the structure for landing pages and ads.  
**PM:** Use differentiation map to inform roadmap — invest in defensible dimensions, reach parity on gaps.
```

---

## Quality Gate

- Positioning formula complete (all 5 elements: segment / need / product / category / differentiator / proof / alternative / alternative limitation)
- Primary alternative is the one users actually consider (verified from win/loss or discovery)
- At least one proof point per value proposition (not just a claim)
- Differentiation map completed (not just narrative)
- Stress test run — weakest element identified and improvement noted
