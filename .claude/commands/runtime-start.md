---
name: runtime-start
description: >-
  Start a multi-step workflow with persistent state, human approval gates, and
  resumability. Use when a request spans more than one skill invocation, requires
  a sequence of dependent steps, or must survive session interruption. Single-skill
  requests do not need this — invoke the skill directly.
---

# /runtime-start — Start a Bounded Workflow

Decompose a multi-step intent into a tracked, resumable workflow plan. Surface the plan for operator approval. Execute step 1 only after explicit confirmation.

## Trigger

`/runtime-start [intent description]` — describe what needs to happen in plain language.

Use this when:
- The request requires 2+ skills in sequence
- Steps depend on prior step outputs
- The work must survive session interruption
- You need to pause and resume across days

Do NOT use for single-skill requests. Overhead is not worth it. Just invoke the skill directly.

---

## Protocol

### Step 0: Check for active workflows

Read `runtime/state/active-workflows.json`.

If any workflow has status `GATE` or `RUNNING`:
- Surface it: "You have a workflow paused at a gate: [name], step X of Y. Resolve it before starting a new one, or explicitly ask to defer it."
- Do not proceed until the operator resolves or explicitly defers.

If any workflow has status `PAUSED`:
- Mention it: "Note: [name] is paused at step X. Starting new workflow — run /runtime-resume to return to it."
- Proceed.

### Step 1: Decompose the intent

Read relevant context:
- `memory/MEMORY.md` and the most relevant memory file
- Any input files the operator has referenced
- `execution/active-initiatives.md` to check for overlap with existing plans

Decompose the intent into an ordered list of steps. Each step must have:
- A single skill to invoke
- Declared input files
- Declared output path (specific file, not a directory)
- A human gate type: `human_approval` (default) or `human_review`
- Explicit dependencies (which prior steps' output does this step consume)

Constraints:
- Maximum 7 steps per workflow. If more are needed, propose splitting into two linked workflows.
- No step may write to `memory/`, `strategy/active-bets.md`, or `CLAUDE.md` — these are operator-controlled.
- Every output path must be a specific file path, not a directory.

### Step 2: Assign workflow ID

Format: `wf_YYYYMMDD_NNN`

Read `runtime/state/active-workflows.json` and `runtime/state/workflow-history.json` to find the next available NNN for today's date.

### Step 3: Write the plan file

Write to: `runtime/plans/{wf-id}.json`

Use the schema from `architecture/RUNTIME-STATE-SCHEMA.md` → Workflow Plan section.

Set `approved: false` and `approved_at: null`.

### Step 4: Surface the plan for approval

Present the plan in this format — no extra explanation needed:

```
Workflow: [name]
ID: [wf-id]
Steps: [N]

1. [Step name] → [skill] → output: [path]
2. [Step name] → [skill] → output: [path]
   (depends on step 1)
3. [Step name] → [skill] → output: [path]
   (depends on steps 1, 2)

Each step requires your approval before proceeding.

Start step 1?
```

Wait for explicit approval before writing any state beyond the plan file.

### Step 5: On operator approval

1. Update `runtime/plans/{wf-id}.json`: set `approved: true`, `approved_at: [timestamp]`
2. Write entry to `runtime/state/active-workflows.json`:
   ```json
   {
     "id": "{wf-id}",
     "name": "[workflow name]",
     "status": "RUNNING",
     "created": "[timestamp]",
     "last_active": "[timestamp]",
     "plan_file": "runtime/plans/{wf-id}.json",
     "current_step": 1,
     "total_steps": N,
     "gate_pending": false,
     "gate_step": null,
     "gate_message": null,
     "retry_count": 0,
     "last_snapshot": null
   }
   ```
3. Append to `runtime/events/queue.json`: `WORKFLOW_STARTED` event
4. Proceed to execute step 1

### Step 6: Execute step 1

Load the skill definition: `.claude/commands/{skill-name}.md`

Assemble context:
- Read all declared input files for step 1
- Load any memory files the skill protocol requires

Execute the skill per its protocol.

Write the output to the declared output path.

Append to `runtime/events/queue.json`: `STEP_STARTED` then `STEP_COMPLETED` events.

### Step 7: Post-step gate

1. Write snapshot: `runtime/snapshots/{wf-id}-step1.json`
   - Use schema from `architecture/RUNTIME-STATE-SCHEMA.md` → Workflow Snapshot section
   - Include: completed step with output summary, all pending steps, gate state
2. Update `runtime/state/active-workflows.json`:
   - `status: "GATE"`
   - `gate_pending: true`
   - `gate_step: 1`
   - `last_snapshot: "runtime/snapshots/{wf-id}-step1.json"`
3. Append `GATE_PENDING` event
4. Present the gate:

```
Step 1 complete: [step name]
Output: [file path]
[1-2 sentence summary of what was produced]

Next: Step 2 — [step name] (using [skill])
Continue? (yes / pause / stop)
```

### Step 8: Gate resolution

**On "yes" / "continue" / "proceed":**
- Write gate checkpoint: `runtime/checkpoints/{wf-id}-gate1.json`
- Update `active-workflows.json`: `status: "RUNNING"`, `current_step: 2`, `gate_pending: false`
- Append `GATE_APPROVED` event
- Execute step 2 (repeat from Step 6)

**On "pause":**
- Write gate checkpoint with `decision: "paused"`
- Update `active-workflows.json`: `status: "PAUSED"`
- Append `WORKFLOW_PAUSED` event
- Output: "Workflow paused at step 1. Resume anytime with /runtime-resume."

**On "stop" / "abandon":**
- Write gate checkpoint with `decision: "abandoned"`
- Move workflow entry from `active-workflows.json` to `workflow-history.json` with status `ABANDONED`
- Append `WORKFLOW_ABANDONED` event
- Output: "Workflow abandoned. Completed artifacts are preserved at [paths]."

### Step 9: Continue until final step

Repeat the execute → snapshot → gate cycle for each step.

On final step completion:
- Snapshot written as usual
- Gate presented: "Step [N] complete: [summary]. This was the final step. Workflow complete."
- On acknowledgement: move to history with status `COMPLETED`

### Step 10: On step failure

If a step fails to produce its declared output:

1. Write a failed snapshot: `runtime/snapshots/{wf-id}-step{N}-failed.json`
2. Update `active-workflows.json`: `status: "FAILED"`
3. Append `STEP_FAILED` event
4. Present recovery options:

```
Step [N] ([name]) failed to produce output.
Completed work is preserved.

Recovery options:
  RETRY  — re-run this step (attempt [X] of 3)
  SKIP   — skip this step and proceed to step [N+1]
           (only available if step N+1 doesn't depend on this output)
  REWIND — restore from a prior snapshot and re-run from there
  ABANDON — close this workflow; all completed artifacts are kept

Choose a recovery action:
```

Do NOT attempt any recovery action without explicit operator choice.

---

## Quality Gates

- [ ] Plan has no more than 7 steps
- [ ] Every step has a declared output path (specific file, not directory)
- [ ] Every dependency is explicit in the plan
- [ ] No output path writes to memory/, strategy/active-bets.md, or CLAUDE.md
- [ ] Plan approved before any step executes
- [ ] Each gate requires explicit operator signal before advancing
- [ ] Failed steps surface recovery options — never attempt workarounds silently
