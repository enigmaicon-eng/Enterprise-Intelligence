---
name: pm-prototype
description: Select prototype fidelity, define scope, and produce a prototype brief matched to the research goal. Prevents the prototype scope trap and ensures fidelity matches what is being tested.
version: "1.0"
changed: 2026-05-20
---

# PM Prototype

**Input:** Research goal, feature or flow to prototype, available time, current design state.

**Output:** Written to `notes/structured/prototype-YYYY-MM-DD-<feature-slug>.md`

**Scope:** This skill produces a prototype brief and scope specification — what to build, at what fidelity, and what to test. For wireframe structure specifications, use `/pm-wireframe`. For the actual research session design, use `/pm-user-interview`.

---

## Steps

1. **Read context.** Load `knowledge/pm/wireframing-prototyping.md`. If a wireframe spec or PRD exists for this feature, read it.

2. **Identify the research goal.** What question must this prototype answer? Force a single primary question. "Does the interaction pattern make sense?" and "Do users trust this product?" require different fidelity — conflating them wastes build time and produces ambiguous results.

3. **Select fidelity.** Apply the fidelity-to-goal matrix:
   - Concept comprehension → lo-fi or paper
   - Flow completion (can users finish the task?) → mid-fi
   - Trust and visual polish → hi-fi
   - Animation or real-data feel → coded prototype
   State the fidelity decision and the reason. If push-back is expected, note alternative fidelity and why it was rejected.

4. **Scope the prototype.** Name every screen to build. Name every screen NOT to build. Apply the prototype scope rule: scope to exactly what needs testing. A 5-screen focused prototype outperforms a 30-screen comprehensive one. Identify placeholder screens (where users will navigate but behavior isn't being tested).

5. **Define the test flow.** What is the starting state? What task will users be asked to complete? What is the success state? Write this as a single scenario sentence: "Starting from [screen], the user wants to [goal] and should end up at [outcome]."

6. **Define what must be interactive vs. static.** Every interactive element requires build time. Make only the elements being tested interactive. Everything else is a screenshot or a click-through.

7. **Write the prototype handoff note.** If this prototype goes to design to build, include: fidelity directive ("structural only — designer solves visual"), what's being tested, what's out of scope, when the prototype is needed, and the research session date.

---

## Output Format

```markdown
# Prototype Brief — [Feature Name] — [Date]

**Research goal:** [Single primary question this prototype must answer]
**Fidelity:** [Lo-fi / Mid-fi / Hi-fi / Coded] — [one-sentence rationale]
**Estimated build time:** [hours or days]
**Research session date:** [date or "TBD"]

---

## Fidelity Decision

**Selected fidelity:** [fidelity level]

**Reason:** [Why this fidelity matches the research goal]

**Rejected alternative:** [What was considered and why rejected]

---

## Prototype Scope

**Screens to build:**

| Screen | Purpose | Interactive elements | Static elements |
|--------|---------|----------------------|-----------------|
| [Name] | [Why it's needed] | [What user must click/input] | [Everything else] |

**Screens NOT in scope:**

| Screen | Why excluded | Placeholder approach |
|--------|-------------|----------------------|
| [Name] | [Reason] | [How to handle if user navigates here] |

---

## Test Flow

**Starting state:** [Screen and state the user begins in]

**User task:** "[Exact task instruction that will be given to participant]"

**Success state:** [What the user must reach for the task to be complete]

**Expected failure point:** [Where users are most likely to struggle — this is what we're learning from]

---

## Interaction Specification

Elements that must be interactive (in priority order):
1. [Element] — [What it does when triggered]
2. [Element] — [What it does when triggered]

Elements that are static (no interaction needed):
- [Element] — display only
- [Element] — display only

States to build:
- [State name]: [When triggered, what it shows]
- [State name]: [When triggered, what it shows]

---

## Prototype Handoff Note

**For designer / builder:**

This prototype is [structural only — designer solves visual / hi-fi — follow visual system].

**Being tested:** [The interaction pattern / trust / flow completion / other]

**Not being tested (do not invest in):** [Visual details / copy / edge cases / secondary flows]

**Must be ready by:** [Date]

**Research session:** [Date, who is running it]

---

## Open Questions

1. [Question about the prototype itself — not the product]
2. [Question]
```

---

## Quality Gate

- Single primary research question stated
- Fidelity matched to research goal with stated rationale
- Rejected fidelity alternative named and dismissed
- Every screen scoped: build vs. not-build, with placeholder approach for excluded screens
- Interactive vs. static elements specified
- Test flow written as a single scenario sentence with start/success/expected-failure
- Prototype handoff note separates what's being tested from what's out of scope
