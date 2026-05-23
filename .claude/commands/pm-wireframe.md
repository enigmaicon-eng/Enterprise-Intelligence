---
name: pm-wireframe
description: Generate annotated low-fidelity wireframe descriptions and flow specifications. Produces screen-by-screen structural descriptions with annotations, states, and edge cases — ready for a designer or prototyping tool.
version: "1.0"
changed: 2026-05-20
---

# PM Wireframe

**Input:** Feature name, user flow to wireframe, any known constraints or reference screens.

**Output:** Written to `notes/structured/wireframe-YYYY-MM-DD-<feature-slug>.md`

**Scope:** This skill produces textual wireframe specifications and annotated descriptions — the PM's structural intent before visual design. For interactive prototype specifications, use `/pm-prototype`.

---

## Steps

1. **Read context.** Load `knowledge/pm/wireframing-prototyping.md`. If a PRD or design brief exists for this feature, read it first.

2. **Map the flow before any single screen.** What screens are needed? In what sequence? What are the entry points and exit points? Write the flow map first — not the screens.

3. **For each screen, define:**
   - Screen name and purpose (one sentence)
   - Primary action (the most important thing a user does here)
   - Information hierarchy (what must be visible above the fold / at the top)
   - Components (what UI elements are present — list, not design)
   - States (default, loading, empty, error, success)
   - Navigation elements (back, close, next, skip)

4. **Write annotations for every non-obvious element.** Every button, input, or interactive component needs a behavior annotation. Non-obvious = anything a developer would need to ask about.

5. **Map the edge cases explicitly.** What happens when: there's no data, the action fails, the user abandons mid-flow, the session expires, the user tries the action twice.

6. **Write the out-of-scope list.** Things PM considered but explicitly excluded from this wireframe version.

7. **Produce a component list.** All UI components needed — this serves as the first cut of the engineering component inventory.

---

## Output Format

```markdown
# Wireframe Specification — [Feature Name] — [Date]

**PM:** [name]  **Design owner:** [name]  **Status:** For design handoff / For review

---

## Flow Map

Entry point: [How users arrive here]

[Screen A] → [action] → [Screen B] → [action] → [Screen C — success state]
                                   ↘ [error] → [Screen E — error state]

Exit points: [Where users can leave and where they go]

---

## Screen 1: [Screen Name]

**Purpose:** [One sentence — what this screen helps the user accomplish]  
**Entry from:** [Previous screen or entry point]  
**Primary action:** [The main thing the user does here]

**Structure (top to bottom):**
- [Element]: [What it shows / does] — Annotation: [behavior detail]
- [Element]: [What it shows / does] — Annotation: [behavior detail]
- [Element]: [Primary CTA label] — Annotation: [what happens on click; destination]
- [Element]: [Secondary action] — Annotation: [behavior]

**States:**
- Default: [What the screen looks like with typical data]
- Empty: [What shows when the user has no data]
- Loading: [What shows while data is fetching]
- Error: [What shows if the action fails — error message + recovery action]

**Annotations:**
1. [Annotation 1 — behavior detail]
2. [Annotation 2 — data source or constraint]
3. [Annotation 3 — open question if any]

---

## Screen 2: [Screen Name]

[Same structure]

---

## Screen N: [Success / Error / Edge Case State]

[Same structure]

---

## Edge Cases Accounted For

- No data state: [Handled in Screen X, [specific treatment]]
- Error state: [Handled in Screen Y, [specific treatment]]
- User abandons mid-flow: [Where they return to, what state is preserved]
- Session expiration: [Behavior]

---

## Out of Scope (this wireframe version)

- [Element / state / flow] — [rationale]
- [Element / state / flow] — [rationale]

---

## Component Inventory

UI components required by this flow:
- [Component name] — [Usage]
- [Component name] — [Usage]

Existing components (reuse): [list]  
New components needed: [list]

---

## Open Questions for Design

1. [Question PM genuinely doesn't have a preference on]
2. [Question]
```

---

## Quality Gate

- Flow map drawn before individual screens
- Every screen has a purpose statement (one sentence)
- Every interactive element has a behavior annotation
- All states defined (default, empty, loading, error)
- Edge cases explicitly addressed (not just happy path)
- Out-of-scope list present (prevents scope creep in design)
- Component inventory separates new vs. reuse
