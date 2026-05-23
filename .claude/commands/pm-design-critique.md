---
name: pm-design-critique
description: Run a structured PM design review — evaluate designs against user outcomes, not aesthetic preferences. Separates PM's legitimate concerns from design's domain. Produces actionable feedback without prescribing solutions.
version: "1.0"
changed: 2026-05-20
---

# PM Design Critique

**Input:** Design to review (Figma link, screenshot, or description), the user problem it solves, success criteria from the PRD or design brief, any specific concerns to examine.

**Output:** Written to `notes/structured/design-critique-YYYY-MM-DD-<feature-slug>.md`

**Scope:** PM's structured evaluation of a design against product requirements and user outcomes. PM reviews against problem-outcome criteria — not visual design choices, which are the designer's domain. For creating the design brief PM hands off to design, use `/pm-design-brief`.

---

## Steps

1. **Read context.** If a PRD, design brief, or wireframe spec exists for this feature, read it before looking at the design. The critique is against requirements, not preferences.

2. **Clarify the PM's role in design review.** PM evaluates: does this design solve the user problem? Does it match the success criteria? Does it handle the required states and edge cases? Does it make the primary action clear? PM does not evaluate: visual hierarchy choices, color decisions, spacing and layout (unless they create a usability problem), typographic choices.

3. **Evaluate problem-outcome fit.** Would a user in the target scenario accomplish their goal with this design? Walk through the user's task from their starting state to their goal state. Note where the design aids the task and where it creates friction.

4. **Evaluate against success criteria.** For each success criterion in the PRD or design brief: does the design support it? Name the specific element that serves the criterion, or name the gap.

5. **Evaluate state coverage.** Does the design address all required states: default, loading, empty, error, success? Are the edge cases handled? Check against the wireframe spec or PRD.

6. **Frame all feedback as outcomes, not solutions.** "The user won't know this button submits the form" is legitimate PM feedback. "Make the button bigger and change the color to blue" is not — that's the designer's job. Every piece of feedback must name the user outcome at risk, not the visual change to make.

7. **Separate blocking from non-blocking feedback.** Blocking: the design will prevent users from completing the primary task, or violates a stated requirement. Non-blocking: PM's preference or observation that the designer should be aware of but can resolve at their discretion.

---

## Output Format

```markdown
# Design Critique — [Feature Name] — [Date]

**Design reviewed:** [Link or description]
**Design version:** [Version number or date]
**Designer:** [Name]
**PM:** [Name]
**Criteria reviewed against:** [PRD / Design brief / Wireframe spec — link]

---

## PM Role Reminder

This review evaluates the design against product requirements and user outcomes. The following are outside PM's review scope and are not commented on:
- Visual hierarchy, layout, and spacing (unless they create a measured usability problem)
- Color choices (except accessibility — see below)
- Typography choices
- Illustration and icon style

The designer has final authority on visual design. PM has final authority on whether user outcomes are achieved.

---

## Problem-Outcome Evaluation

**User scenario walked through:**

[Starting state] → [Steps taken] → [Goal achieved? Yes / Partially / No]

**Where the design aids the task:**
- [Step / element]: [How it helps the user]
- [Step / element]: [How it helps the user]

**Where the design creates friction:**
- [Step / element]: [What friction, why it matters to the user]
- [Step / element]: [What friction]

**Primary action clarity:** [Clear / Unclear] — [Observation about what the user's eye goes to first]

---

## Success Criteria Evaluation

| Success criterion (from PRD/brief) | Design supports it? | Evidence or gap |
|-----------------------------------|--------------------|--------------------|
| [Criterion 1] | Yes / Partially / No | [Which element serves it, or what's missing] |
| [Criterion 2] | Yes / Partially / No | |
| [Criterion 3] | Yes / Partially / No | |

---

## State Coverage Evaluation

| State | Designed? | Notes |
|-------|----------|-------|
| Default | Yes / No / Partial | |
| Loading | Yes / No / Partial | |
| Empty (no data) | Yes / No / Partial | |
| Error | Yes / No / Partial | |
| Success / confirmation | Yes / No / Partial | |
| [Feature-specific state] | Yes / No / Partial | |

**Missing states that must be designed before handoff:**
- [State]: [What happens now if this state is triggered without a design]

---

## Blocking Feedback

*(These must be resolved before this design moves to engineering)*

**B1 — [Short description of the issue]**
- User outcome at risk: [What users cannot accomplish or will get wrong]
- Evidence: [What in the design creates this risk — specific element or state]
- Not a solution prescription: [State what problem must be solved, not how to solve it]
- Open question for designer: [Question if PM is uncertain about how to solve it]

**B2 — [Short description]**
- User outcome at risk:
- Evidence:

---

## Non-Blocking Feedback

*(Observations for the designer to weigh at their discretion — not PM requirements)*

**N1 — [Short description]**
- Observation: [What PM noticed]
- Why it might matter: [The user scenario where this could affect the outcome]
- Designer's call: [Acknowledged — not a requirement]

**N2 — [Short description]**

---

## Accessibility Check (PM-Level)

*(PM should flag observable accessibility concerns — full audit requires a specialist)*

- Color contrast: [Pass / Potential issue — [where]]
- Interactive elements keyboard-navigable: [Observable / Can't assess from design alone]
- Error states: [Communicated by more than color alone — Yes / No]
- Touch target sizes (mobile): [Appear adequate / Potential concern]

---

## Questions for the Designer

*(Questions PM genuinely doesn't have a preference on — for design's judgment)*

1. [Question about a design decision PM would like to understand the rationale for]
2. [Question about a trade-off that is visible in the design]

---

## Verdict

**Status:** Approved / Approved with revisions / Revisions required before approval

**Blocking items:** [N items — must be resolved before moving to engineering]

**Target resolution date:** [Date]

**Next review:** [When / If blocking items resolved, async approval / Second in-person review]
```

---

## Quality Gate

- PM reviewed against PRD or design brief criteria (not in isolation)
- PM role boundary stated (what PM reviews vs. what is designer's domain)
- Problem-outcome walk-through completed step by step
- All required states checked (default, loading, empty, error, success)
- All blocking feedback stated as user outcomes at risk (not as visual solutions)
- Non-blocking feedback clearly separated from blocking feedback
- Verdict is explicit: approved / approved with revisions / revisions required
