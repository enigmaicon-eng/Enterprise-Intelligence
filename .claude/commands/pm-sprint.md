---
name: pm-sprint
description: Run sprint planning preparation. Produces a sprint goal, prioritized story list with acceptance criteria verification, dependency check, and capacity confirmation.
version: "1.0"
changed: 2026-05-20
---

# PM Sprint

**Input:** Sprint number, available capacity (person-weeks or story points), team members, and the backlog to draw from. Can be run before sprint planning meeting.

**Output:** Written to `notes/structured/sprint-YYYY-WW-plan.md`

---

## Steps

1. **Read context.** Load `workflows/pm/sprint-workflow.md`. Read `execution/action-items.md` for any carry-forward items.

2. **Write the sprint goal.** One sentence. Format: "At the end of this sprint, [specific users] will be able to [do something they couldn't before] because [what engineering will deliver]." Not a list of tickets — a user outcome.

3. **Confirm capacity.** Subtract from available engineering days:
   - Planned PTO and holidays
   - Recurring meetings (standups, retros, grooming) — typically 10-15% overhead
   - On-call rotation if applicable
   - Engineering discretionary time (tech debt, learning) — typically 10-20%
   - A 15% buffer for unplanned work
   The remainder is committable capacity.

4. **Select stories for the sprint.** Apply in order:
   - All P0 stories from the backlog that fit the sprint goal
   - P1 stories that contribute to the sprint goal or are independently valuable
   - Carry-forward items from last sprint (evaluate: should they carry or be de-scoped?)
   - Stop when capacity is reached — do not over-commit

5. **Verify each selected story is sprint-ready:**
   - [ ] Acceptance criteria written (before development starts)
   - [ ] No open [DECISION NEEDED] annotations
   - [ ] Design assets ready (if needed)
   - [ ] Dependencies confirmed (or risk-accepted)
   - [ ] Engineering has seen the story and hasn't flagged unknowns

6. **Run the dependency check.** For each story: are there dependencies on other stories, other teams, or external factors? Flag any unresolved.

7. **Identify the top risk in this sprint.** The one thing most likely to prevent the sprint goal from being achieved.

8. **Write the pre-sprint contract summary.** The 3 things the sprint needs from PM to succeed (decisions to make, information to provide, stakeholders to manage).

9. **Write the output.**

---

## Output Format

```markdown
# Sprint [N] Plan — [Date range]

**Sprint goal:**  
"At the end of this sprint, [users] will be able to [outcome] because [engineering delivers]."

**Capacity:** [N available days] — [N committed days after overhead/buffer]

---

## Stories Committed

| # | Story | P | Estimate | AC verified? | Dependencies |
|---|---|---|---|---|---|
| 1 | [Story title] | P0 | [N days] | ✓ | None |
| 2 | [Story title] | P0 | [N days] | ✓ | D-02 confirmed |
| 3 | [Story title] | P1 | [N days] | ✓ | None |
| ... | | | | | |
| **Total** | | | **[N days]** | | |

**Capacity check:** [N committed] / [N available] = [N]% — [OK / Over capacity]

---

## Stories Backlogged (Ready for next sprint)
- [Story] — Ready, deferred for capacity
- [Story] — Ready, deferred for capacity

---

## Carry-Forwards from Sprint [N-1]
| Story | Disposition | Reason |
|---|---|---|
| [Story] | Carry / De-scope / Split | [Brief reason] |

---

## Dependency Status

| Story | Dependency | Owner | Confirmed? | Risk if late |
|---|---|---|---|---|
| [Story] | [Dep description] | [Name] | Yes / At risk | [Impact] |

---

## Sprint Risk

**Top risk:** [The one thing most likely to prevent the sprint goal]  
**Mitigation:** [What PM or engineering is doing about it]  
**Contingency:** [What we'll do if the risk materializes — which stories get cut?]

---

## Pre-Sprint Contract (PM commits to providing)

1. [Decision or information needed by engineering, by which date]
2. [Design review of [story], by [date]]
3. [Stakeholder alignment on [item] before [date]]

---

## Sprint Definition of Done Checklist

- [ ] Sprint goal stated and agreed on
- [ ] All P0 stories have verified AC
- [ ] Capacity confirmed (committed ≤ available - overhead - buffer)
- [ ] Dependencies surfaced and owners notified
- [ ] Carry-forwards have named dispositions
- [ ] Top risk identified and mitigation named
```

---

## Quality Gate

- Sprint goal is a user outcome (one sentence — not a list of tickets)
- Capacity math shown (available days - overhead - buffer = committable)
- Every story in the committed list has AC verified before planning
- Carry-forwards have explicit dispositions (carry / de-scope / split)
- Top risk is identified (not "we don't foresee any risks")
- Pre-sprint contract names what PM will deliver to engineering, by when
