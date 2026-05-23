---
name: pm-vision
description: Write or stress-test a product vision document. Produces a 3-year directional narrative that is inspiring, specific enough to make decisions from, and grounded in user and market reality.
version: "1.0"
changed: 2026-05-20
---

# PM Vision

**Input:** Product context, current strategy, any draft vision statement or direction, team/product scope.

**Output:** Written to `strategy/monthly/YYYY-product-vision.md`

---

## Steps

1. **Read context.** Load `knowledge/pm/product-strategy.md`. If an existing strategy doc exists, read it first.

2. **Establish the time horizon.** Product vision is typically 3 years. Not "where we'll be in 1 year" (that's a roadmap) and not "in 10 years" (that's a mission). 3 years is concrete enough to make decisions from, far enough to set direction beyond the current planning cycle.

3. **Start with the user future state.** A product vision begins with the user's world, not the product's features. "In 2028, [target user] will [state of being / capability / outcome] that is impossible today." What is better for users because this product exists at scale?

4. **Connect to market and competitive context.** What change in the market enables this vision? (Technology shift, behavioral shift, regulatory change, cost curve.) A vision that ignores market dynamics is a wish, not a direction.

5. **State the product's role.** How does the product create this future state? What is the mechanism — what does the product do, for whom, that makes the user future state possible?

6. **Define what this vision rules out.** A vision that's consistent with any product direction isn't a vision. For every vision statement, name 2-3 strategic directions it explicitly excludes.

7. **Test the vision against five criteria:**
   - **Inspirational:** Does it motivate? Would a great engineer or designer want to work on this?
   - **Specific enough:** Can you make a roadmap decision by asking "does this move us toward the vision?"
   - **User-grounded:** Does it describe a user outcome, not a product feature?
   - **Time-bound:** Is there a horizon? "Someday" is not a vision.
   - **Differentiated:** Is this distinct from what competitors are building toward?

8. **Identify the three capabilities that make the vision achievable.** What must be true about the product in 3 years for this vision to be realized? These become the anchors for the three-horizon strategy.

9. **Write the output.**

---

## Output Format

```markdown
# Product Vision — [Product/Team] — [Date]

**Time horizon:** [Year — typically 3 years from now]  
**Author:** [PM]  **Status:** Draft | Reviewed | Adopted

---

## The North Star Narrative

[2-3 paragraphs. Written in present tense as if it's [Year].
Describes the world users live in, what they can accomplish, what they no longer struggle with.
NOT a list of features. NOT product-centric. User-world-centric.]

---

## What This Vision Requires of the Market

[What must be true about the world for this vision to be achievable?
Technology readiness, user behavior shifts, regulatory environment, cost curves.]

---

## What This Vision Requires of the Product

[What must this product be capable of in 3 years?
3 anchor capabilities — the foundational things that make the vision possible.]

1. **[Capability]:** [What it enables for users, why it's essential to the vision]
2. **[Capability]:** [What it enables, why essential]
3. **[Capability]:** [What it enables, why essential]

---

## What This Vision Rules Out

This vision is NOT:
- [Strategic direction explicitly excluded] — [why]
- [Strategic direction explicitly excluded] — [why]
- [Strategic direction explicitly excluded] — [why]

---

## Vision Quality Check

| Criterion | Evaluation |
|---|---|
| Inspirational | [Does it motivate? Why/why not?] |
| Specific enough | [Can roadmap decisions be made against it?] |
| User-grounded | [Describes user outcome, not product feature?] |
| Time-bound | [Has a specific horizon?] |
| Differentiated | [Distinct from competitors' direction?] |

**Weakest element:** [Which criterion is least satisfied, and what would strengthen it]

---

## Tension with Current Strategy

[Where does the vision create tension with the current roadmap or strategy?
These tensions are healthy — they surface where current plans need to evolve.]

---

## Connection to Three Horizons

- **H1 (Now):** [Which current initiatives build toward this vision?]
- **H2 (Next):** [Which H2 bets are essential steps toward the vision?]
- **H3 (Later):** [Which H3 options become critical capabilities in this vision?]
```

---

## Quality Gate

- Vision is written from the user's future state (not the product's capabilities)
- Time horizon is explicit (a specific year, not "the future")
- "What this rules out" section has ≥3 explicit exclusions
- Quality check completed — weakest criterion identified and improvement noted
- Tension with current strategy acknowledged (tension = healthy signal)
- Three anchor capabilities named (these drive the three-horizon strategy)
