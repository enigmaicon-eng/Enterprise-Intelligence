---
name: pm-prd
description: Generate a complete Product Requirements Document from problem context. Produces structured PRD with problem statement, success criteria, user stories, requirements, non-goals, and open questions.
version: "1.0"
changed: 2026-05-20
---

# PM PRD

**Input:** Feature name, problem context, target user, success metrics, and any known constraints — provided inline.

**Output:** Written to `notes/structured/prd-YYYY-MM-DD-<feature-slug>.md`

---

## Steps

1. **Read context.** Load `knowledge/pm/writing-standards.md`. If discovery notes exist for this feature, read them first.

2. **Verify the problem is clear before writing requirements.** If the problem statement is vague ("improve user experience"), stop and ask: who specifically, what specifically, why now? Requirements written for a vague problem will be wrong.

3. **Draft the problem statement.** One paragraph: user segment + current state + gap + why it matters to the business. Lead with the user pain, not the product feature.

4. **Define success criteria before requirements.** Primary metric (with baseline and target), guardrail metrics, and measurement timeline. If these can't be stated, the problem isn't understood well enough to write requirements.

5. **Write the non-goals explicitly.** At minimum 3 items. These are as important as the requirements — they prevent scope creep and align expectations.

6. **Write user stories.** Format: "As a [specific persona], I want to [accomplish goal], so that [underlying value]." Each story must have the "so that" — it forces the JTBD abstraction.

7. **Write requirements.** Functional requirements (what the system must do), non-functional (performance, security, accessibility). Mark each P0 (must-have) / P1 (should-have) / P2 (nice-to-have). Do not prescribe the implementation — state the behavior.

8. **List open questions.** Numbered, with owner and blocking/non-blocking flag.

9. **List dependencies.** External teams, systems, or timelines.

10. **Write the output.**

---

## Output Format

```markdown
# PRD: [Feature Name]

**Author:** [PM]  **Status:** Draft  
**Updated:** YYYY-MM-DD  **Engineering owner:** TBD  **Design owner:** TBD

---

## Problem Statement
[One paragraph: user segment, current state, gap, business impact.]

## Success Criteria
**Primary metric:** [Metric] — Baseline: [N] — Target: [N] — Timeline: [weeks post-launch]  
**Guardrail metrics:** [List — must not degrade]  
**Measurement plan:** [How we'll track — instrumentation already exists / needs new events]

## Non-Goals
- [Explicit exclusion with one-line rationale]
- [Explicit exclusion with one-line rationale]
- [Explicit exclusion with one-line rationale]

## User Stories

### Story 1
As a [specific persona],  
I want to [accomplish goal],  
So that [underlying value].

**Acceptance criteria:**
- Given [context] When [action] Then [observable outcome]
- Given [context] When [action] Then [observable outcome]
- Given [edge case] When [action] Then [behavior]

### Story 2
[Same format]

## Requirements

### Functional (P0 — must-have)
1. [Behavior the system must exhibit]
2. [Behavior the system must exhibit]

### Functional (P1 — should-have)
3. [Behavior — can be cut if needed]

### Non-Functional
- Performance: [threshold — e.g., page load <2s at p95]
- Reliability: [uptime / error rate threshold]
- Security: [relevant requirements]
- Accessibility: [WCAG level or specific requirements]

## Technical Considerations
[Known constraints, dependencies, architectural notes from engineering conversations.
Do not prescribe solutions — flag constraints.]

## Open Questions
1. [BLOCKING] [Question] — Owner: [name] — Needed by: [date]
2. [NON-BLOCKING] [Question] — Owner: [name]

## Dependencies
- [External team / system] — needed by [date] — owner [name]

## Out of Scope (Confirmed)
- [Item] — [brief rationale]
```

---

## Quality Gate

- Problem statement mentions a specific user segment (not "users")
- Success criteria includes a primary metric with baseline + target (not just "improve engagement")
- Non-goals has ≥3 explicit items
- Every user story has a "so that" clause (JTBD layer)
- Every P0 acceptance criterion is testable without interpretation
- Open questions are numbered with owners
- Nothing in requirements prescribes a technical implementation
