# /exec-decompose — Task Decomposition

Decompose an initiative milestone into a concrete, owned task register with explicit dependencies. Eliminates ambiguity before work starts.

## Trigger
`/exec-decompose [initiative-id] [milestone]` — e.g., `/exec-decompose INIT-2026-001 M1`
`/exec-decompose [initiative-id]` — decomposes the next pending milestone

## When to Use
Run decomposition when:
- About to start a new milestone
- A task turns out to be larger than one session
- Handoff is needed and another person needs clarity on what to do

Do NOT run decomposition for single tasks that are already clear.

## Protocol

### Step 0: Load context
Read the execution plan at `execution/plans/[initiative-id].md`. Focus on:
- The milestone being decomposed (its done condition)
- Assumptions (what can be taken for granted in task design)
- Dependencies from the plan (external constraints on task sequencing)

### Step 1: Generate task candidates
From the milestone done condition, work backwards: what must be completed for the milestone to be done? Generate the full set of tasks before assigning IDs or owners.

**Decomposition rule**: Keep decomposing until every task:
- Starts with an action verb
- Can be completed in ≤4 hours by one person
- Has an observable done condition
- Is independent of other tasks, OR has an explicit dependency named

### Step 2: Build the dependency graph
After generating all tasks, identify the critical path (the longest sequence of dependent tasks). Draw the dependency graph in ASCII.

### Step 3: Assign task IDs
Format: `T[NN]` within this decomposition. Numbering is sequential within the milestone, not globally unique.

### Step 4: Flag risk tasks
Tasks with any of the following get a risk flag:
- Effort estimate > 3 hours (high uncertainty)
- External dependency (blocked by someone/something outside the initiative)
- New approach being tried for the first time
- Done condition is harder to verify than usual

### Step 5: Write the decomposition
Use `templates/task-decomposition.md`.
Write to: `execution/decompositions/[initiative-id]-[milestone].md`

### Step 6: Generate action items
For every T01...TNN task that has no upstream dependencies (can start immediately), generate an action item in `execution/action-items.md`:

```
- [ ] [Task name] | INIT-2026-001 M1 | Owner: [name] | Due: [date] | Effort: [Xh]
```

### Step 7: Report
- File path of decomposition
- Task count by status (ready-to-start / blocked / flagged)
- Critical path length (number of tasks × estimated hours)
- Any tasks that failed the decomposition health check (list them)

## Quality Gate
Do not finalize the decomposition if:
- Any task lacks a done condition
- Any task has effort > 4 hours without a note explaining why it wasn't decomposed further
- Dependencies exist that reference external systems without a named owner on the dependency
