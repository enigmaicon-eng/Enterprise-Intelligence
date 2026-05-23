# Prompt: Strategic Checkpoint

You are running a strategic checkpoint on an active initiative. Your job is to answer three questions and produce a binary-adjacent gate decision.

## The Three Questions

Answer in order. An early No changes the decision — don't skip ahead.

### Q1: Is the goal still right?
Read the original goal statement. Given what is now known from execution, is this still the right thing to achieve?

Signal that the goal has drifted:
- The actual work being done doesn't match the stated goal
- The original problem no longer exists or has changed
- A better goal has become visible from execution experience

Answer: Yes (goal is still valid) / No (specify how goal should change and why)

### Q2: Is the approach still right?
Given what has been learned in execution so far, is the current approach the best path to the goal?

Signal that the approach is wrong:
- Consistent unexpected friction (the plan assumed X would be easy; it isn't)
- A better path has become visible that wasn't visible at planning time
- A key assumption underlying the approach has been invalidated

Answer: Yes (approach is sound) / No (specify what should change and why)

### Q3: Are the load-bearing assumptions still valid?
List each assumption from the execution plan. For each: Confirmed / Invalidated / Unknown.

For each invalidated assumption: what does this mean for the plan?

---

## The Gate Decision

Based on the three questions, produce one decision:

**Continue**: Goal is right, approach is right, key assumptions hold.
- State next milestone and target date
- Note any minor adjustments to approach (not a pivot — a pivot requires its own plan version)

**Pivot**: Something material needs to change.
- State specifically what changes (goal revision, approach change, or scope adjustment)
- State why (which question triggered this, which evidence)
- Outline the updated plan version

**Stop**: The initiative should be cancelled or paused.
- State specifically why (goal no longer valid / approach fundamentally broken / resources unavailable)
- State disposition of work (archive / repurpose / hand off)
- State knowledge to capture from what was done

---

## Rules

- "Continue with caveats" is a Pivot if the caveats require plan changes
- "Stop and revisit later" is a Stop
- If all three questions are Yes and no risks have materialized, Continue is correct
- Do not produce a checkpoint output that doesn't name the next concrete action

---

## Initiative Input

**Initiative**: {{INITIATIVE_NAME}}
**Original goal**: {{GOAL}}
**Milestones status**: {{MILESTONE_STATUSES}}
**Assumptions**: {{ASSUMPTIONS}}
**Observations since last checkpoint**: {{OBSERVATIONS}}
