---
title: Task Decomposition — [Initiative Name or Milestone]
initiative_id: INIT-YYYY-NNN
milestone: M[N] — [milestone name]
decomposed: YYYY-MM-DD
decomposed_by: [name]
---

## Decomposition Goal
What outcome does completing all tasks in this decomposition achieve?

## Dependency Graph
Visual representation of task order. Use arrows to show "must complete before."

```
[T01] → [T02] → [T04]
              ↘
[T03] ──────→ [T05] → [T06 — milestone done]
```

## Task Register

Each task must have:
- **Action verb** at the start (Build, Write, Review, Decide, Define, Test, Deploy...)
- **Single owner** — one name, not a team
- **Done condition** — observable, not "make progress on"
- **Effort estimate** — in hours or half-days, not story points
- **Dependencies** — which tasks must complete first

---

### T01 — [Task Name]
- **Action**: [Verb + object: what specifically to do]
- **Owner**: [name]
- **Done when**: [Observable condition — someone can verify this without asking you]
- **Effort**: [X hours / half-day / full day]
- **Depends on**: [T00 / none]
- **Notes**: [Optional: constraint, approach note, or risk]

### T02 — [Task Name]
- **Action**: ...
- **Owner**: ...
- **Done when**: ...
- **Effort**: ...
- **Depends on**: T01
- **Notes**: ...

<!-- Repeat for each task -->

---

## Blocked Tasks
Tasks that can't start yet. List them with their explicit unblock condition.

| Task | Blocked By | Unblocked When |
|------|-----------|---------------|
| T0N | [external dependency or task] | [specific condition] |

## Risk Flags
Tasks with elevated uncertainty. These get extra attention in reviews.

| Task | Risk | Mitigation |
|------|------|-----------|
| T0N | [What could go wrong] | [Pre-planned response] |

## Decomposition Health Check
Before finalizing, verify:
- [ ] Every task starts with an action verb
- [ ] Every task has a single named owner
- [ ] Every task has an observable done condition (not "make progress")
- [ ] All dependencies between tasks are explicit
- [ ] No task is estimated at more than 4 hours (if so, decompose further)
- [ ] The critical path is identified (longest sequence of dependent tasks)
