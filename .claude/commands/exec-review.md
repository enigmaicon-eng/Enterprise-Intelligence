# /exec-review — Execution Review

Run a structured review of a deliverable, task, or milestone against stated criteria. Produces a concrete verdict and change list — not a narrative assessment.

## Trigger
`/exec-review [deliverable or file]` — what to review
`/exec-review weekly` — review the current week's execution across all active initiatives

## Two Modes

### Mode A: Deliverable Review
Review a specific artifact against quality criteria.

### Mode B: Weekly Execution Review
Review all active initiatives for the past week. Surfaces drift, blockers, and priorities for next week.

---

## Protocol — Mode A: Deliverable Review

### Step 0: Establish criteria
Before reading the deliverable, establish what "good" looks like. Check for:
1. Explicit criteria in the initiative plan (`execution/plans/[id].md`) under Success Criteria
2. Milestone done condition
3. Criteria stated by the user in the `/exec-review` invocation

If no criteria exist, ask for them before reviewing. A review without stated criteria is an opinion, not a review.

### Step 1: Read the deliverable
Read the deliverable file. Do not form judgments before reading.

### Step 2: Score against criteria
For each criterion: Pass / Fail / Partial with a one-line explanation of why.

### Step 3: Surface gaps
For each failing or partial criterion:
- Name the specific gap (not "could be improved")
- State the change that would close it
- Estimate effort: <30min / 1-2hr / half-day+

### Step 4: Produce verdict
- **Ship**: All criteria pass. No further changes needed.
- **Refine**: [N] criteria fail. Use `templates/refinement-cycle.md` to manage changes.
- **Rewrite**: The deliverable doesn't meet criteria at a structural level. Start over with revised criteria.
- **Kill**: The deliverable's purpose is no longer valid. Stop the work.

### Step 5: Write review record
Append review summary to the deliverable's frontmatter:
```yaml
last_review: YYYY-MM-DD
review_verdict: ship | refine | rewrite | kill
review_cycles: N
```
Or write a standalone review note if the deliverable shouldn't be edited.

---

## Protocol — Mode B: Weekly Execution Review

### Step 0: Load execution state
Read in order:
1. `execution/active-initiatives.md` — initiative status
2. `execution/action-items.md` — filter for this week (completed, overdue, in-progress)
3. `execution/risks.md` — risks opened or triggered this week

### Step 1: Initiative health scan
For each active initiative:
- What was the plan for this week (from milestones)?
- What actually happened?
- Delta: on track / slipping / blocked / at risk

### Step 2: Action item audit
- Completed on time: [count]
- Completed late: [count] — what caused the delay?
- Overdue (not completed): [count] — what's blocking?
- New items added mid-week: [count] — were they planned or reactive?

### Step 3: Risk scan
- Any risks triggered or escalated this week?
- Any risks approaching their trigger condition?

### Step 4: Priority recalibration
Apply the three-criterion stack (commitment → leverage → reversibility) to identify the highest-priority work for next week. Produce a ranked list of ≤5 items.

### Step 5: Write the weekly execution review
Write to: `reviews/weekly/[YYYY-WW]-exec.md`

Sections:
- **Week in One Line**: the shape of the week
- **Initiative Status**: table with health signal per initiative
- **Action Item Audit**: counts with brief commentary
- **Top Risk This Week**: the one risk most likely to materialize
- **Next Week Top 5**: ranked, with one-line rationale per item
- **One Change to Make**: the single process/workflow change that would most improve next week

## Ownership
- `/exec-review [deliverable]` = deliverable review (Mode A)
- `/exec-review weekly` = weekly execution review (Mode B)
- `/weekly` handles the strategic/knowledge weekly review — these are separate
