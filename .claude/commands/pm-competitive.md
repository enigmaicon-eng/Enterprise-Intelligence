---
name: pm-competitive
description: Run a structured competitive analysis on a competitor, market segment, or competitive event. Produces position matrix, win/loss signals, and strategic implications.
version: "1.0"
changed: 2026-05-20
---

# PM Competitive

**Input:** Competitor name, market segment, or competitive event (announcement, pricing change, new product) — provided inline.

**Output:** Written to `notes/structured/competitive-YYYY-MM-DD-<slug>.md`

---

## Steps

1. **Read context.** Load `knowledge/pm/competitive-intelligence.md`. If an existing competitive position matrix exists in `notes/structured/`, read it for context.

2. **Classify the analysis type:**
   - **New competitor:** Full landscape map + position matrix
   - **Competitor update:** Delta from last analysis — what changed, what it means
   - **Competitive event:** Specific move analysis — what happened, signal vs. noise, response options
   - **Win/loss analysis:** Pattern synthesis from sales data — what is being won/lost and why

3. **For landscape / position analysis:**
   - Map the competitor to Ring 1 (direct), Ring 2 (indirect), or Ring 3 (emerging)
   - Complete position matrix: target segment, core strength, pricing model, distribution, defensibility, biggest weakness, recent moves
   - Identify competitive gaps: what do they have that we don't? What do we have that they don't?
   - Identify the competitive narrative they're running (what story do they tell to win?)

4. **For competitive event analysis:**
   - What exactly happened? (Separate fact from interpretation)
   - Who does this affect? (Which of our user segments / which deals?)
   - Is this signal or noise? (Does this change what users can do, or is it marketing?)
   - Does this close a gap that was causing us to lose deals?
   - What is the appropriate response? (Accelerate roadmap item / communicate differentiation / no action)

5. **For win/loss analysis:**
   - Pattern across wins: what did we win on? (Specific capability, price, relationship, timing?)
   - Pattern across losses: what did we lose on? What competitor, what reason?
   - Emerging narrative: is a new competitor narrative appearing in multiple deals?
   - Implication: what does this mean for roadmap, positioning, or sales enablement?

6. **Produce strategic implications.** What should PM do differently based on this analysis? Roadmap priority change? Positioning update? Sales enablement gap?

7. **Write the output.**

---

## Output Format

```markdown
# Competitive Analysis — [Subject] — [Date]

**Analysis type:** Landscape | Event | Win/Loss | Position update  
**Ring:** 1 (direct) | 2 (indirect) | 3 (emerging)

---

## Position Matrix

| Dimension | [Competitor] | Us |
|---|---|---|
| Target segment | | |
| Core strength | | |
| Pricing model | | |
| Distribution | | |
| Primary defensibility | | |
| Biggest weakness | | |
| Recent strategic moves | | |

---

## Competitive Gap Analysis

**They have, we don't:** [Specific capabilities, with impact on deals]
**We have, they don't:** [Specific advantages to emphasize]
**Their narrative:** [The story they tell to win — exact framing if known]
**Our counter-narrative:** [How we should frame against this]

---

## Signal vs. Noise Assessment (for event analyses)

**What happened:** [Fact-only description]
**Who it affects:** [Segments, deal types, geographic markets]
**Signal or noise?** [Genuine capability change vs. marketing / vaporware]
**Deal impact:** [Will this change deal outcomes? Which deals?]

---

## Win/Loss Patterns (for win/loss analyses)

**Win patterns:** [What we won on]
**Loss patterns:** [What we lost on, to whom]
**Emerging competitor narrative:** [New story appearing in deals]
**Gaps creating losses:** [Specific capabilities causing deal losses]

---

## Strategic Implications

**Roadmap:** [Should anything move based on this analysis?]
**Positioning:** [Does the positioning statement need to change?]
**Sales enablement:** [What do sales/CS need to handle this competitor?]
**Monitoring:** [What signals to watch to know if this situation is evolving?]

**Recommended action:** [Specific next step — owner, timeline]
```

---

## Quality Gate

- Competitor moves are described as facts before interpretation (separate sections)
- Gap analysis names specific capabilities, not vague "better UX"
- "Signal or noise" assessment completed for event analyses
- Strategic implications have a specific recommended action with owner
- Win/loss analysis covers both wins AND losses (not just losses)
