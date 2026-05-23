# /exec-plan — Execution Planning

Build a structured execution plan for an initiative from a goal or intent statement. Produces a plan that can be handed off, checkpoint-reviewed, and decomposed into tasks.

## Trigger
`/exec-plan [initiative description]` — describe the goal or initiative in plain language.

## When to Use
An execution plan is warranted when:
- Work spans more than one session
- More than one person is involved (or could be)
- The work has milestones that matter (not just a single task)
- The work involves real trade-offs in scope, time, or approach

Do NOT plan work that can be done immediately. If it fits in one session, just do it.

## Protocol

### Step 0: Silent context load
Read `memory/MEMORY.md`. Read `execution/active-initiatives.md` to check if a related initiative already exists — if so, surface it before creating a new one.

### Step 1: Scope clarification (if needed)
If the user's description lacks one of these, ask (one round only):
- What does "done" look like? (observable outcome, not activity)
- Is there a hard deadline or a target date?
- What's explicitly out of scope?

Do not ask if these are answerable from context.

### Step 2: Build the execution plan
Use `templates/execution-plan.md`. Required:
- **Goal**: One sentence with an observable done condition. Rewrite vague goals before proceeding.
- **Milestones**: 2-5 milestones. Each must have an observable done condition, not just a name.
- **Scope**: Both in-scope AND out-of-scope. Explicit out-of-scope prevents scope creep.
- **Assumptions**: Name the load-bearing ones — these are what checkpoints will verify.
- **Top 3 Risks**: Use the P×I heuristic. Only surface risks with owners and mitigations.
- **Success Criteria**: What observable outcome proves the goal was achieved?

### Step 3: Assign initiative ID
Format: `INIT-YYYY-NNN` where NNN is sequential within the year.
Read `execution/active-initiatives.md` to find the next available number.

### Step 4: Write the plan
Write to: `execution/plans/[initiative-id].md`

### Step 5: Register in active initiatives
Read `execution/active-initiatives.md`. Add one row:
```
| [INIT-ID] | [Title] | [Owner] | [Target date] | [M1 due] | planning |
```

### Step 6: Offer decomposition
Ask: "Ready to decompose into tasks? Run `/exec-decompose [initiative-id]` when you want to break down M1."
Do NOT auto-run decomposition — let the user initiate it.

### Step 7: Report
- File path of plan
- Initiative ID assigned
- Milestone dates
- Top risk identified
- Whether any existing initiative overlaps with this one

## Quality Bar
- The goal section fails if it contains words like "improve," "work on," or "continue" without a measurable endpoint.
- The done-condition fails if it can only be assessed by the person who did the work.
- The scope section fails if Out of Scope is empty — everything that's ambiguous should be explicitly excluded.
