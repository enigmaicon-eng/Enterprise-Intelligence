---
title: PM Writing Standards
domain: pm
created: 2026-05-20
reviewed: 2026-05-20
connections: [discovery-intelligence, technical-fluency, org-dynamics]
confidence: high
source: original synthesis
tags: [pm, writing, prd, spec, stories, acceptance-criteria, communication]
---

## Definition

PM writing is not documentation — it is decision infrastructure. A PRD, spec, or user story that gets filed but doesn't change what engineering builds has failed, regardless of how well-written it is. Write for clarity and alignment, not comprehensiveness.

The standard for any PM artifact: a new engineer who joins the team tomorrow should be able to read it and understand what's being built, why, what done looks like, and what's out of scope.

## The PRD (Product Requirements Document)

### When to write a PRD

Write a PRD when: the work involves >2 weeks of engineering effort, multiple functions (design, data, CS, sales) need alignment, or the feature involves architectural decisions that constrain future work.

Do NOT write a PRD when: it's a bug fix, a minor copy change, a well-scoped iteration where the sprint ticket suffices.

**The PRD anti-pattern:** Writing comprehensive PRDs for small features to look thorough. Long PRDs for small features signal unclear thinking, not rigor.

### PRD Structure (canonical)

```markdown
# [Feature Name]
**Author:** [PM name]  **Status:** Draft | In Review | Approved | Deprecated  
**Last updated:** YYYY-MM-DD  **Engineering owner:** [name]  **Design owner:** [name]

## Problem Statement
[One paragraph. What problem exists for which users? Why does it matter now?
Must contain: user segment, current state, gap, why solving it matters to the business.]

## Success Criteria
[How will we know this worked? Primary metric with baseline and target.
Guardrail metrics that must not degrade. Timeline for measurement.]

## Non-Goals (Explicit)
[What this feature deliberately does NOT do. This section is as important as what it does.]

## User Stories
[Who + What + Why format. See user story standards below.]

## Requirements
[Functional requirements: what the system must do.
Non-functional requirements: performance, reliability, security, accessibility.
Numbered for reference. Mark each P0 (must-have) / P1 (should-have) / P2 (nice-to-have).]

## Design
[Link to Figma / design doc. PM notes on intent — not prescriptive, but directional.]

## Technical Considerations
[What PM knows about technical constraints, dependencies, or risks.
Leave technical decisions to engineering — flag the constraints that affect scope.]

## Open Questions
[Numbered list. Owner assigned. Blocking vs. non-blocking marked.]

## Dependencies
[External teams, systems, or timelines this depends on.]

## Out of Scope (Confirmed)
[Items that were explicitly considered and excluded — with brief rationale.]
```

### PRD Writing Rules

**Lead with the problem, not the solution.** The first paragraph should not describe the feature — it should describe the user's current reality and why it's inadequate.

**Success criteria before requirements.** If you can't state how you'll measure success, you don't understand the problem well enough to write requirements.

**Non-goals are mandatory.** Every PRD without explicit non-goals generates scope creep, because nothing has been ruled out.

**P0/P1/P2 on every requirement.** Requirements without priority produce "all or nothing" conversations with engineering. Priority allows negotiation.

**Minimize prescription, maximize intent.** "Users should be able to see all their open tasks sorted by due date" describes intent. "Display tasks in a list with due date in column 3, using red text for overdue items" is prescription. Write intent; design solves for prescription.

## User Stories

### Format
```
As a [specific user persona, not "user"],
I want to [accomplish a goal],
So that [the underlying value — the "why"].
```

**Bad story:** "As a user, I want a search bar so I can search."
- Who is the user? What are they searching for? Why does finding it matter?

**Good story:** "As a project lead managing 3+ concurrent projects, I want to filter tasks by project across my unified inbox, so that I can triage my day without switching between project views."

### Story sizing

Stories should be completable in a single sprint. If a story requires multiple sprints, it is an epic — split it into stories where each delivers independent value.

**The INVEST test for user stories:**
- **I**ndependent: can be built and deployed without other stories (or dependency is explicit)
- **N**egotiable: not a contract — PM and engineering negotiate scope within the intent
- **V**aluable: delivers value to the user on its own, even if small
- **E**stimable: engineering can estimate the effort
- **S**mall: completable in a sprint
- **T**estable: there are clear acceptance criteria

### Acceptance Criteria

For every user story, write acceptance criteria before development begins. Format: **Given** [context] **When** [action] **Then** [observable outcome].

```
Given a project lead is viewing their unified inbox
When they apply a filter for "Project Alpha"
Then only tasks tagged to Project Alpha appear
And the task count updates to reflect the filter
And a "Clear filter" option appears in the header
```

**Acceptance criteria must be:**
- Testable by QA without interpretation
- Complete for the happy path AND the 3 most likely edge cases
- Written before engineering starts, not after

**Criteria anti-patterns:**
- "Works correctly" — not testable
- "Is fast" — not measurable (state the threshold: <500ms p95)
- "Looks good" — not testable (design is the reference)

## One-Pagers and Strategic Briefs

For internal alignment documents shorter than a PRD:

```markdown
# [Topic]
**Purpose:** [One sentence — what decision or alignment this achieves]

## Situation
[2-3 sentences. Current state. What's true today.]

## Proposal
[What we're doing and why. The bet. The trade-off we're accepting.]

## Success looks like
[Observable in 90 days: what has changed?]

## What we need
[Specific asks from specific functions with dates.]
```

**Principle:** One-pagers should create alignment, not demonstrate thoroughness. If the reader could act on the document without a follow-up meeting, it's well-written.

## Annotation Standards

When writing any PM artifact:
- **[DECISION NEEDED]** — marks open questions that block progress
- **[ASSUMPTION]** — marks claims that haven't been validated
- **[TBD — Owner: name, By: date]** — marks incomplete sections with explicit accountability
- **[OUT OF SCOPE — Reason: X]** — marks explicit exclusions with rationale

These annotations prevent the "looks complete but isn't" failure mode.

## Connections

Links to [[discovery-intelligence]] — PRD problem statements are output of discovery. Links to [[technical-fluency]] — requirements must reflect technical constraints. Links to [[org-dynamics]] — PRDs are alignment artifacts as much as specification artifacts.
