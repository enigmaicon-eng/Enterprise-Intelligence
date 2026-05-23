---
name: runtime-resume
description: >-
  Resume a paused, interrupted, or gate-pending workflow. Also invoked automatically
  at session start when active workflows are detected. Shows all resumable workflows,
  lets operator choose which to continue, and re-establishes execution context before
  resuming. Use after any session interruption, machine restart, or deliberate pause.
---

# /runtime-resume — Resume a Workflow

Surface all paused and interrupted workflows. Let the operator choose one to resume. Re-establish execution context from the last valid snapshot. Resume from the next step.

## Trigger

`/runtime-resume` — invoked explicitly, or by the Executive Orchestrator at session start when active workflows are detected.

`/runtime-resume [wf-id]` — resume a specific workflow directly.

---

## Protocol

### Step 1: Read all resumable workflows

Read `runtime/state/active-workflows.json`.

Resumable statuses: `PAUSED`, `GATE`, `INTERRUPTED`, `FAILED`.

If the file is empty or has no resumable workflows:
- Output: "No active workflows. Start a new one with /runtime-start."
- Stop.

### Step 2: Classify each resumable workflow

| Status | Meaning | Display |
|--------|---------|---------|
| PAUSED | Deliberately paused by operator | "Paused at step X — ready to continue" |
| GATE | Awaiting gate approval | "Awaiting your approval at step X — review output?" |
| INTERRUPTED | Session ended mid-execution | "Interrupted at step X — resume from last checkpoint" |
| FAILED | Step failed, recovery needed | "Step X failed — recovery required before resuming" |

### Step 3: Surface resumable workflows

If one workflow: present it directly.
If multiple: list them in order of `last_active` (most recent first).

Format:

```
Active workflows:

1. [Workflow name] (ID: wf_YYYYMMDD_NNN)
   Status: [PAUSED / GATE / INTERRUPTED / FAILED]
   Progress: Step [X] of [Y] — [current step name]
   Last active: [timestamp]
   [Status-specific note, e.g. "Awaiting approval: review synthesis before writing PRD"]

2. [Second workflow, if any]
   ...

Which to resume? (enter number or ID, or "defer" to skip for this session)
```

### Step 4: On operator selection

**If PAUSED:**
1. Read `runtime/plans/{wf-id}.json` — reload the full plan
2. Read the last snapshot: `runtime/state/active-workflows.json` → `last_snapshot` field
3. Present re-orientation:
   ```
   Resuming: [workflow name]
   Completed: Steps [list of completed step names]
   Next: Step [N+1] — [step name] using [skill]
   Inputs needed: [declared input files]

   Continue with step [N+1]?
   ```
4. Wait for explicit confirmation before executing

**If GATE:**
1. Read the last snapshot
2. Present the gate output summary:
   ```
   Resuming: [workflow name]
   Step [N] completed: [step name]
   Output: [file path]
   [Output summary from snapshot]

   Next: Step [N+1] — [step name]
   Continue? (yes / pause / stop)
   ```
3. This IS the gate — explicit approval here starts step N+1

**If INTERRUPTED:**
1. Note that the workflow was mid-execution when the session ended
2. Read the last valid snapshot (look for the most recent snapshot file for this wf-id)
3. Present:
   ```
   [Workflow name] was interrupted during step [N].
   Last completed step: [N-1] — [step name]
   Step [N] ([name]) may be incomplete — its output should be verified.

   Recovery options:
     RETRY  — re-run step [N] from its declared inputs
     SKIP   — skip step [N] and continue from step [N+1]
     VERIFY — check if step [N]'s output file exists and is complete, then decide
     ABANDON — close this workflow

   Choose:
   ```
4. Execute chosen recovery action

**If FAILED:**
- Hand off directly to `/runtime-recover` protocol for this workflow

### Step 5: On operator selecting "defer"

- Do not modify any workflow state
- Output: "Deferred. Workflows remain active. Resume with /runtime-resume when ready."
- Continue with normal session operations

### Step 6: Execute the resumed step

After confirmation:
1. Update `runtime/state/active-workflows.json`: `status: "RUNNING"`, `last_active: [timestamp]`
2. Append `WORKFLOW_RESUMED` event to `runtime/events/queue.json`
3. Load the skill for the next step
4. Assemble context:
   - Re-read all declared input files for this step
   - The step's `depends_on` outputs must exist — verify before executing
5. Execute the skill
6. Continue through the standard execute → snapshot → gate cycle (same as `/runtime-start` Step 6 onward)

### Step 7: Dependency verification on resume

Before executing any resumed step, verify all dependency outputs exist:

For each file in the step's `depends_on` output paths:
- Check the file exists on disk
- If missing: "Step [N] depends on [file] which does not exist. This may have been deleted. Recovery options: REWIND to the step that produced it, or ABANDON."
- Do NOT proceed if dependencies are missing

---

## Quality Gates

- [ ] Resumable workflows are classified by status before presenting options
- [ ] Operator selects which workflow to resume — never auto-select
- [ ] One additional confirmation required before executing any resumed step
- [ ] Dependency files verified to exist before execution begins
- [ ] INTERRUPTED workflows surface recovery options, not automatic continuation
- [ ] Workflow state updated to RUNNING only after operator confirms
