---
name: pm-discovery
description: Synthesize discovery conversations into structured insight using the observation-interpretation-implication-action chain. Surfaces assumption status, surprises, and recommended actions.
version: "1.0"
changed: 2026-05-20
---

# PM Discovery

**Input:** Raw discovery notes, processed debrief files, or direct quotes. Minimum 3 conversations for synthesis; works on individual conversation analysis too.

**Output:** Written to `meeting-intelligence/processed/discovery-synthesis-YYYY-MM-DD.md`

**Also updates:** `notes/raw/` promote candidates if any findings qualify as knowledge

---

## Steps

1. **Read context.** Load `knowledge/pm/discovery-intelligence.md`. Read any referenced source files.

2. **First pass — extraction:**
   - Separate what users did (behavior) from what they said (stated preference). Behavioral evidence outweighs stated preference when they conflict.
   - Rank problems by: frequency across conversations × emotional intensity × workaround sophistication.
   - Flag contradictions — what did users say that contradicted each other, or contradicted prior assumptions?

3. **Second pass — interpretation (JTBD frame):**
   - For each problem, ask: what are they trying to accomplish at a higher level of abstraction?
   - Identify root causes vs. symptoms. A symptom is a problem that disappears if you solve a different problem. A root cause doesn't.
   - Note segment differences. Aggregate findings hide segment-specific patterns.

4. **Third pass — assumption status:**
   - For each assumption the discovery was testing: what happened? Confirmed / challenged / insufficient signal.
   - Flag assumptions that were tested zero times — not because they were confirmed, but because the questions didn't surface them.

5. **Fourth pass — action.**
   - What changes now (this sprint or quarter)?
   - What needs more investigation?
   - What should be flagged to leadership or stakeholders?

6. **Write the output.**

---

## Output Format

```markdown
# Discovery Synthesis — [Topic] — [Date]

**Conversations:** [N] | **Segment:** [description] | **Focus:** [hypothesis tested]

---

## Top Findings

### Finding 1: [One-line label]
**Evidence (behavioral):** [What they did — specific, sourced]
**Evidence (stated):** [What they said — quote if available]
**Interpretation:** [Underlying need, JTBD frame]
**Implication:** [What this means for the product, roadmap, strategy]

### Finding 2: [One-line label]
[Same structure]

### Finding 3: [One-line label]
[Same structure]

---

## Assumption Status

| Assumption | Status | Evidence |
|---|---|---|
| [Assumption] | Confirmed / Challenged / Insufficient signal | [Brief] |

---

## Surprises
[What contradicted prior beliefs. These are the highest-value findings — don't bury them.]

---

## Open Questions
- [Question] — [Proposed method to answer]

---

## Recommended Actions
1. [Action] — [Rationale] — Owner: [name] — By: [date]
2. [Action] — [Rationale] — Owner: [name] — By: [date]
3. [Action] — [Rationale] — Owner: [name] — By: [date]

---

## Knowledge Candidates
[Findings that should be promoted to knowledge/pm/ — set promote_candidate: true in next /capture]
```

---

## Quality Gate

- Every finding has a complete chain: observation → interpretation → implication
- Behavioral evidence is separated from stated preference
- At least one finding challenges a prior assumption (all-confirming synthesis = wrong questions)
- Recommended actions are specific enough to act on without follow-up conversation
- Segment differences noted where present
