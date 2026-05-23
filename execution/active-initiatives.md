# Active Initiatives Register

Lean register of in-flight initiatives. One row per initiative. Full detail in `execution/plans/[id].md`.

---

## Status Definitions

| Status | Meaning |
|--------|---------|
| `planning` | Execution plan being written, not yet executing |
| `active` | Executing — tasks in flight, milestones being pursued |
| `paused` | Deliberately paused — reason and resume trigger noted in plan |
| `at-risk` | On track to miss a milestone or key assumption invalidated |
| `checkpoint` | Milestone reached, awaiting continue/pivot/stop decision |
| `complete` | All milestones done, success criteria verified |
| `stopped` | Cancelled — see plan file for rationale |

---

## Active

| ID | Initiative | Owner | Target | Next Milestone | Status | Last Checkpoint |
|----|-----------|-------|--------|---------------|--------|----------------|
| *(no active initiatives yet — create with `/exec-plan`)* | | | | | | |

---

## Paused / At Risk

| ID | Initiative | Status | Reason | Resume Trigger |
|----|-----------|--------|--------|---------------|
| | | | | |

---

## Completed (Last 90 Days)

| ID | Initiative | Completed | Outcome | Knowledge Captured |
|----|-----------|-----------|---------|-------------------|
| | | | | |

---

## Archive
Initiatives older than 90 days (complete or stopped) are moved to `execution/archive/initiatives-YYYY.md`.

---

*Updated by: `/exec-plan` (creates), `/exec-checkpoint` (updates), `/exec-review weekly` (status scan)*
