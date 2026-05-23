---
name: pm-design-brief
description: Generate a design brief for the design team. Provides problem framing, user context, constraints, success criteria, and design principles — not design solutions.
version: "1.0"
changed: 2026-05-20
---

# PM Design Brief

**Input:** Feature or problem context, target user, any known constraints (technical, business, time), and discovery insights if available.

**Output:** Written to `notes/structured/design-brief-YYYY-MM-DD-<feature-slug>.md`

**Core principle:** A design brief gives design the problem, not the solution. The moment PM specifies "a dropdown with 3 options" in the brief, the design process has been short-circuited. Define the job to be done; let design solve for how.

---

## Steps

1. **Read context.** Load `knowledge/pm/discovery-intelligence.md` if discovery notes exist for this feature. Load `knowledge/pm/writing-standards.md` for the writing frame.

2. **Write the problem statement from the user's perspective.** Not "we need a dashboard" — "users who manage 5+ projects currently lack a way to see where all their deadlines fall without opening each project individually, causing them to miss cross-project conflicts."

3. **Define the user.** Specific persona in specific context. What do they know, what are they trying to accomplish, what's their environment (mobile vs. desktop, interrupted vs. focused, expert vs. novice)?

4. **Summarize discovery insights.** What did users say or do that's most relevant to this design challenge? Quotes, behaviors, workarounds. Give the designer the raw material to empathize with, not a sanitized summary.

5. **Articulate the job to be done.** What is the user trying to accomplish? What does success look like from their perspective — not from the product perspective?

6. **Define the constraints.** Technical (what engineering has already decided about the implementation), business (what cannot change for legal, compliance, or commercial reasons), time (when design needs to be complete for engineering to start), platform (web / mobile / both).

7. **State what success looks like.** How will we know design solved the problem? What user behavior changes? What metric moves? This should be observable and specific.

8. **List open questions for design.** Things PM doesn't know the answer to and is genuinely leaving to design's expertise.

9. **Explicitly state what NOT to design.** Out-of-scope components, future states that shouldn't be explored in this round, adjacent problems that are out of scope.

10. **Write the output.**

---

## Output Format

```markdown
# Design Brief — [Feature Name] — [Date]

**PM:** [name]  **Design owner:** [name]  
**Sprint target:** [Which sprint design should be complete for]  
**Engineering handoff by:** [Date]

---

## The Problem

[One paragraph from the user's perspective. Current state, gap, why it matters to them.
No product framing — frame it from the user's experience.]

---

## The User

**Persona:** [Specific — role, context, what they're trying to accomplish]

**Mental model:** [How they think about this — what vocabulary they use, what they compare it to]

**Environment:** [Where / when they do this task — desktop vs. mobile, focused vs. interrupted]

**Experience level:** [Expert user / intermediate / novice / mixed]

---

## Discovery Insights

[What we learned from research that is most relevant to this design challenge.
Include direct quotes. Include behavioral observations. Include workarounds users have invented.]

Key quotes:
- "[User quote]" — [User context]
- "[User quote]" — [User context]

Observed behaviors:
- [What users currently do — specific]

---

## Job to Be Done

[The underlying goal the user is trying to accomplish.
At the right level of abstraction — not too concrete (a button to do X), not too abstract (manage their work).]

When this design is successful, a user will be able to [accomplish specific job] without [current friction], and they will [observable behavior change].

---

## Constraints

**Technical (non-negotiable):**
- [What engineering has decided about the implementation]
- [Data that's available vs. not available]
- [Performance constraints]

**Business (non-negotiable):**
- [Legal / compliance / commercial constraints]

**Time:**
- Design complete by: [Date] (for engineering to start [Sprint N])
- Usability testing: [Included / Not included in this round]

**Platform:** [Web / iOS / Android / All]

---

## Success Criteria

Design is successful when:
- [Observable user behavior change]
- [Metric that should move — qualitative or quantitative]
- [Usability threshold: e.g., ≥80% of test users can complete the task without assistance]

---

## Open Questions for Design

(Things I don't know the answer to — genuinely leaving to design's expertise)
- [Question — e.g., "Is there a pattern that works better for list vs. grid display for this content type?"]
- [Question]

---

## Out of Scope for This Brief

- [What NOT to design in this round]
- [Adjacent problems that are intentionally excluded]
- [Future states / V2 ideas — valid but not now]
```

---

## Quality Gate

- Problem statement is written from the user's perspective (no product framing)
- JTBD section describes the underlying goal, not the feature
- Technical constraints are distinguished from design preferences
- Open questions are genuinely open (PM doesn't have a preferred answer hidden)
- Out-of-scope section explicitly lists items that were considered and excluded
- No solution is prescribed in the brief (dropdowns, buttons, layouts are design's domain)
