# Discovery Synthesis Prompt
## Converting Raw Conversation Data into Structured Insight

**Use when:** After 3+ discovery conversations, or when synthesizing a batch of user research before a planning cycle or roadmap decision.

**Principle from `knowledge/pm/discovery-intelligence.md`:** The insight chain must be complete — observation → interpretation → implication → action. A synthesis that stops at observation is not an insight.

---

## The Prompt

```
Synthesize the following discovery conversations into structured insight.

CONTEXT:
- Number of conversations: [N]
- User segment: [Who was interviewed — role, company size, use case]
- Discovery focus: [What assumption or problem space were we investigating?]
- What would change our thinking: [What signal would confirm or refute the hypothesis?]

RAW INPUTS:
[Paste or reference: conversation notes, quotes, behavioral observations]
[Format: can be raw notes, processed debrief files, or direct quotes]

SYNTHESIS INSTRUCTIONS:
1. First pass — extraction:
   - What did users actually do (behavior), not just say (stated preference)?
   - What problems did they describe? Rank by: frequency across conversations, emotional intensity, and workaround sophistication.
   - What surprised you? What contradicted prior assumptions?

2. Second pass — interpretation:
   - What is the underlying need behind the stated problem? (JTBD frame: what are they trying to accomplish?)
   - Which problems are symptoms and which are root causes?
   - Are there patterns that cut across segments, or are findings segment-specific?

3. Third pass — implication:
   - What does this mean for the roadmap / strategy / current initiative?
   - What assumption does this confirm? What assumption does this challenge?
   - What would we do differently if we fully believed these findings?

4. Fourth pass — action:
   - What should change now (this sprint or quarter)?
   - What needs more investigation before we can act?
   - What should be flagged to leadership or stakeholders?

OUTPUT FORMAT:
Section 1: Top 3 findings (observation + interpretation + implication, one chain per finding)
Section 2: Assumption status (which assumptions were tested and what happened)
Section 3: Surprises (things that contradicted prior beliefs)
Section 4: Open questions (what we still don't know and how to find out)
Section 5: Recommended actions (3 max, ranked, with rationale)
```

---

## Output Template

```markdown
# Discovery Synthesis — [Topic] — [Date]

**Conversations:** [N] | **Segment:** [description] | **Focus:** [hypothesis tested]

---

## Top Findings

### Finding 1: [One-line label]
**Observation:** [What was said or done, with evidence — quote or behavior]
**Interpretation:** [What this means — the underlying need or pattern]
**Implication:** [What this means for the product, roadmap, or strategy]

### Finding 2: [One-line label]
[same structure]

### Finding 3: [One-line label]
[same structure]

---

## Assumption Status

| Assumption | Status | Evidence |
|---|---|---|
| [Assumption from discovery plan] | Confirmed / Challenged / Insufficient signal | [Brief evidence] |

---

## Surprises

- [Something that contradicted a prior belief]
- [Something the team didn't know to look for]

---

## Open Questions

- [Question] — [Proposed method to answer it]
- [Question] — [Proposed method to answer it]

---

## Recommended Actions

1. [Action] — [Rationale] — [Owner] — [By when]
2. [Action] — [Rationale] — [Owner] — [By when]
3. [Action] — [Rationale] — [Owner] — [By when]
```

---

## Quality Gates

Before finalizing:
- [ ] Every finding has an implication (not just observation + interpretation)
- [ ] Behavioral evidence is separated from stated preference (what they did vs. what they said)
- [ ] Segment differences are noted — aggregate findings can mask segment-specific truths
- [ ] At least one finding challenges a prior assumption (if all findings confirm priors, the questions were wrong)
- [ ] Recommended actions are specific enough that someone could act on them without a follow-up conversation

---

## Common Failures

**Surface-level synthesis:** "Users want X feature" is not an insight. "Users want X because their current workflow requires [workaround Y], which takes [N hours] per week and introduces [Z error rate]" is the beginning of an insight.

**Confirmation bias in synthesis:** Finding evidence for what you already believed and not logging the contradicting signals. Surprises belong in the synthesis even if they're inconvenient.

**Missing the JTBD layer:** Synthesizing what users asked for without asking what they were trying to accomplish. The solution space is larger than the stated request.

**Action-less synthesis:** A synthesis that ends with "interesting findings" but no next step. Discovery without action is a library, not a learning loop.
