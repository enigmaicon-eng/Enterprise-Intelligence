---
title: Refinement Cycle — [Deliverable Name]
deliverable: [what is being refined]
cycle: 1 | 2 | 3
reviewer: [name]
date: YYYY-MM-DD
exit_condition: [state the done condition before reviewing]
---

## Criteria (Set Before Review)
What quality bar must this deliverable meet? Name it before looking at the work.

1. **[Criterion]** — Pass condition: [what "good" looks like for this criterion]
2. **[Criterion]** — Pass condition: ...
3. **[Criterion]** — Pass condition: ...

*If you can't define the criteria before reviewing, stop. Go define them.*

---

## Review Findings

### What Passes
Against which criteria does this deliverable already meet the bar?
- [Criterion X]: Pass — [brief note]
- ...

### What Fails
Specific gaps against stated criteria. "Could be better" is not a finding — name the gap precisely.

| Gap | Which Criterion | Severity (blocks ship / degrades quality / minor) | Specific Change Required |
|-----|----------------|--------------------------------------------------|------------------------|
| [Gap description] | [Criterion N] | [severity] | [Concrete change — not direction] |
| ... | | | |

---

## Change Plan
From the failing criteria, what changes are required before the next review?

- [ ] [Concrete change] — Owner: [name] — Effort: [estimate]
- [ ] [Concrete change] — Owner: [name] — Effort: [estimate]

**Estimated time to next review**: [X hours / days]

---

## Cycle Decision
After reviewing all criteria:

- [ ] **Pass** — All criteria met. Deliverable is done. No further refinement.
- [ ] **Cycle again** — [N] gaps remain. Proceeding to Cycle [N+1].
- [ ] **Criteria revision** — Criteria were wrong or ambiguous. Redefine before Cycle [N+1].
- [ ] **Kill** — Effort to reach criteria not worth the value. Stopping work.

---

## Refinement History
*(Append each cycle — do not overwrite)*

| Cycle | Date | Criteria Met | Gaps Found | Decision |
|-------|------|-------------|-----------|---------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

**Rule**: After Cycle 3, the deliverable either ships or is killed. A fourth cycle requires explicit justification written here.
