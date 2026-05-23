---
name: runtime-recover
description: >-
  Diagnose and recover from a failed, interrupted, or inconsistent workflow.
  Reads the last valid snapshot, presents recovery options (RETRY, SKIP, REWIND,
  ABANDON), and executes the chosen action. Also handles corrupted state files.
  Always operator-initiated — never takes autonomous recovery action.
---

# /runtime-recover — Workflow Recovery

Diagnose what went wrong. Surface the last valid state. Let the operator choose the recovery path. Execute the chosen action.

## Trigger

`/runtime-recover` — scan all active workflows for recoverable failures.
`/runtime-recover [wf-id]` — recover a specific workflow.

---

## Protocol

### Step 1: Identify workflows needing recovery

Read `runtime/state/active-workflows.json`.

Recoverable statuses: `FAILED`, `INTERRUPTED`.

Also flag: any workflow with `status: "RUNNING"` but `last_active` older than the current session start time (this indicates an interrupted workflow from a prior session that wasn't cleaned up).

If no recoverable workflows:
- Output: "No workflows in a failed or interrupted state. Use /runtime-status to check active workflows."
- Stop.

### Step 2: Diagnose the failure

For each recoverable workflow:

Read (in order):
1. `runtime/plans/{wf-id}.json` — the original plan
2. `runtime/state/active-workflows.json` entry — current state
3. The most recent snapshot: check `last_snapshot` field, then read that file
4. All events for this workflow in `runtime/events/queue.json` (filter by `workflow_id`)

Determine:
- **Last successful step:** The highest-index step with status COMPLETED in the snapshot
- **Failed step:** The step that failed (look for `STEP_FAILED` event or snapshot with `recovery_valid: false`)
- **Failure class:**
  - F1 — Output file declared but does not exist on disk
  - F2 — A dependency file that should exist from a prior step is missing
  - F3 — Session interrupted (workflow was RUNNING, now in new session)
  - F4 — State file unreadable or inconsistent
  - F5 — Max retries (3) exceeded for a step

### Step 3: Surface the diagnosis

Format:

```
Recovery needed: [workflow name] (ID: [wf-id])

Diagnosis
  Status: [FAILED / INTERRUPTED]
  Failure class: [F1-F5] — [plain language description]
  Last successful step: [N] — [step name] (output: [path]) [exists? ✓/✗]
  Failed step: [N+1] — [step name]
  Retry count: [X] of 3

What succeeded (preserved):
  [List of completed step output files with existence check]

What failed:
  [Specific description of what the step was supposed to do and what went wrong]
```

### Step 4: Present recovery options

Present only options that are available given the failure class:

```
Recovery options:

  RETRY   — Re-run step [N+1] from its declared inputs
             [Available if retry count < 3]
             [Not available: max retries exceeded]

  SKIP    — Mark step [N+1] as skipped, proceed to step [N+2]
             [Available if step N+2 does not depend on N+1's output]
             [Not available: step [N+2] depends on this step's output]

  REWIND  — Restore from a prior snapshot and re-run from that point
             Available snapshots:
               Snapshot at step [N] — [timestamp]
               Snapshot at step [N-1] — [timestamp]

  ABANDON — Close this workflow. All completed artifacts are preserved.
             [Always available]

Choose a recovery action:
```

Do NOT auto-select. Wait for explicit operator input.

### Step 5: Execute the chosen recovery action

**RETRY:**
1. Log `RETRY_ATTEMPTED` event with attempt number
2. Update `active-workflows.json`: `status: "RUNNING"`, increment `retry_count`
3. Re-read all declared input files for the failed step (fresh read, in case files changed)
4. Re-execute the skill
5. If succeeds: write snapshot, present gate (continue as normal)
6. If fails again and count < 3: offer RETRY again
7. If fails on 3rd attempt: return to recovery options, RETRY no longer available

**SKIP:**
1. Verify the next step (N+2) does not list N+1 in its `depends_on`
   - If it does: "Cannot skip — step [N+2] depends on [N+1]'s output. Choose REWIND or ABANDON."
2. Write a skip snapshot: `runtime/snapshots/{wf-id}-step{N+1}-skipped.json`
3. Log `STEP_SKIPPED` event
4. Update `active-workflows.json`: `current_step: N+2`, `status: "GATE"` (present gate before continuing)
5. Present gate: "Step [N+1] skipped. Next: step [N+2] — [name]. Continue?"

**REWIND:**
1. List available snapshots with timestamps
2. Let operator choose which snapshot to restore from
3. On operator selection:
   - Read the chosen snapshot file
   - Update `active-workflows.json`:
     - `current_step`: the step after the snapshot's `step_just_completed`
     - `status: "PAUSED"` (not RUNNING — one more confirmation needed before execution)
     - `last_snapshot`: path to the chosen snapshot
   - Log `RECOVERY_INITIATED` event with `rewind_to: [snapshot_id]`
4. Present: "Restored to step [N]. Ready to re-run step [N+1] — [name]. Continue?"
5. On confirmation: execute step N+1 fresh

**ABANDON:**
1. Ask for confirmation: "Abandon [workflow name]? This cannot be undone. All completed artifacts are kept."
2. On confirmation:
   - Read the `workflow-history.json` file
   - Add entry with:
     - `status: "ABANDONED"`
     - `abandoned_at: [timestamp]`
     - `steps_completed: [count from last snapshot]`
     - `output_files: [list of all output files from completed steps]`
     - `abandon_reason: [short operator-provided reason]` — ask for a brief reason
   - Remove the workflow from `active-workflows.json`
   - Log `WORKFLOW_ABANDONED` event
3. Output: "Workflow [name] abandoned. Completed artifacts preserved at: [file list]"

### Step 6: Handle corrupted state (Failure Class F4)

If `active-workflows.json` is unreadable or invalid JSON:

1. Do not attempt to write to it — it may be partially written
2. List all snapshot files in `runtime/snapshots/` — they are the ground truth
3. Present: "State file is corrupted. Found [N] snapshots. Reconstruct state from snapshots?"
4. On confirmation:
   - Read all snapshot files and reconstruct the workflow list
   - Rewrite `active-workflows.json` from snapshot data
   - All reconstructed workflows get status `PAUSED` (require operator confirmation before running)
5. Run `/runtime-status` to verify the reconstructed state

---

## Recovery Invariants

- The operator always chooses the recovery action — the engine never selects autonomously
- No recovery action modifies completed step output files — they are always preserved
- ABANDON always available, no matter what else is broken
- After any recovery action, the workflow is in a valid, consistent state before execution resumes
- Recovery actions are logged — the audit trail is never modified

---

## Quality Gates

- [ ] No recovery action taken without explicit operator choice
- [ ] Retry count tracked and respected (max 3)
- [ ] SKIP only available if next step has no dependency on skipped step
- [ ] REWIND presents all available snapshots for operator to choose from
- [ ] ABANDON requires confirmation and reason before executing
- [ ] Corrupted state recovered from snapshots, not discarded
- [ ] All recovery actions logged to events/queue.json
