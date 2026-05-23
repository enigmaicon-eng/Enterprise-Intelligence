# /exec-checkpoint — Strategic Checkpoint

Run a structured milestone or strategic checkpoint on an active initiative. Produces a binary gate decision: continue, pivot, or stop. Not a status update — a decision point.

## Trigger
`/exec-checkpoint [initiative-id]` — milestone checkpoint on the most recently completed milestone
`/exec-checkpoint [initiative-id] [milestone]` — checkpoint a specific milestone
`/exec-checkpoint [initiative-id] strategic` — full strategic review (use at monthly cadence or on pivot signals)

## When to Use
- A milestone is marked complete
- Something unexpected happened that changes the validity of the plan
- Monthly initiative review
- You feel uncertain about whether the work is still the right work

Do NOT run checkpoints mid-task or before a milestone is reached. Premature checkpoints produce false signals.

## Protocol

### Step 0: Load context
Read in order:
1. `execution/plans/[initiative-id].md` — original plan, goal, assumptions, success criteria
2. `execution/decompositions/[initiative-id]-[milestone].md` (if exists) — task completion state
3. `execution/risks.md` — filter for this initiative
4. Previous checkpoint record (if any) in `execution/checkpoints/[initiative-id]/`

### Step 1: Build the status picture
Do not rely on memory. Enumerate:
- Milestones completed vs. planned (with dates)
- Tasks completed / overdue / blocked
- Assumptions from the plan — which are confirmed, which are invalidated?
- Risks that have materialized or elevated

### Step 2: Answer the three checkpoint questions
These questions are answered in order. An early "No" changes what follows.

**Q1: Is the goal still right?**
Read the goal statement from the plan. Given what you now know, is this still the right thing to achieve? Signal that the goal has shifted: the work has drifted in a different direction without a decision, or the original problem has changed.

**Q2: Is the approach still right?**
Given execution experience so far, is the current approach the best path? Signal that the approach is wrong: unexpected friction, wrong assumptions proving true, better approach visible now that wasn't visible at planning time.

**Q3: Are load-bearing assumptions still valid?**
Name each assumption from the plan. Check each one against current observations.

### Step 3: Produce the decision
One of three outputs — no middle ground:

**Continue**: Goal is right, approach is right, assumptions hold. State next milestone and its target date.

**Pivot**: Something needs to change. State specifically: what changes, why, and what the updated plan looks like. Write the updated plan version as `execution/plans/[initiative-id]-v[N].md`.

**Stop**: State specifically why — is it the goal (no longer valuable?), the approach (not working?), or resources (not available?)? What happens to the work? What knowledge should be captured?

### Step 4: Write the checkpoint record
Use `templates/strategic-checkpoint.md`.
Write to: `execution/checkpoints/[initiative-id]/[date]-[milestone].md`

### Step 5: Update the initiative register
Read `execution/active-initiatives.md`. Update the initiative row:
- Checkpoint date
- Decision made
- Next milestone if continuing

### Step 6: Report
- Decision made (continue / pivot / stop)
- Primary rationale in one sentence
- If continuing: next checkpoint target
- If pivoting: what specifically changes
- If stopping: knowledge capture recommendation

## Quality Bar
A checkpoint that produces "Continue" with no changes is either:
(a) Genuinely on track — this is valid
(b) Criteria were too vague to surface real drift — this is a planning failure

If checkpoints consistently produce Continue without any insight, revisit the success criteria and assumption list. They may be too vague to generate signal.
