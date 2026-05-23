---
name: runtime-status
description: >-
  Display a full dashboard of the bounded runtime's current state: active workflows,
  pending gates, event queue depth, and recent completions. Read-only — nothing is
  written to disk. Use to orient yourself before starting new work, check on paused
  workflows, or verify the runtime is in a consistent state.
---

# /runtime-status — Runtime State Dashboard

Read all runtime state files and produce a consolidated view. Terminal output only — nothing written to disk.

## Trigger

`/runtime-status` — full dashboard view.
`/runtime-status [wf-id]` — detailed view of a specific workflow.

---

## Protocol

### Step 1: Read all state files

Read in parallel (independent):
- `runtime/state/active-workflows.json`
- `runtime/state/workflow-history.json`
- `runtime/events/queue.json`

Also read plan files for each active workflow: `runtime/plans/{wf-id}.json`

### Step 2: Compute summary statistics

From the data:
- Count of active workflows by status (RUNNING, GATE, PAUSED, FAILED, INTERRUPTED)
- Count of events in queue not yet processed (processed = event timestamp < `last_processed`)
- Most recent activity timestamp across all active workflows
- Count of completed workflows in history (last 7 days)
- Count of workflows in history with status ABANDONED or FAILED (last 7 days)

### Step 3: Generate the dashboard

Output format:

```
## Runtime Status — [YYYY-MM-DD HH:MM]

### Active Workflows

[If no active workflows:]
  No active workflows. Runtime is idle.

[For each active workflow:]

  [Workflow name] (ID: [wf-id])
  Status: [STATUS BADGE]
  Progress: Step [X] of [Y]
    ✓ Step 1: [name] → [output path]
    ✓ Step 2: [name] → [output path]
    ⊙ Step 3: [name] ← [current / next]
    ○ Step 4: [name]
  Last active: [relative time, e.g. "2 hours ago"]
  [If GATE:] ⚑ Awaiting approval: [gate message]
  [If FAILED:] ✗ Failed at step [N]: [failure context]
  [If PAUSED:] ⏸ Paused. Resume with /runtime-resume.

---

### Event Queue

  Total events: [N]
  Last processed: [timestamp or "never"]
  Unprocessed events: [N]
  [If unprocessed > 0:] Last unprocessed: [event type] at [timestamp]

---

### Recent History (last 7 days)

  Completed: [N]
  Abandoned: [N]
  Failed: [N]

  [Last 3 completed workflows, most recent first:]
  ✓ [name] — [N] steps — completed [relative time]
  [If abandoned:]
  ✗ [name] — abandoned at step [X] — [relative time]

---

### Runtime Health

[Run these checks and report:]
  [ ] active-workflows.json readable and valid JSON
  [ ] workflow-history.json readable and valid JSON
  [ ] events/queue.json readable and valid JSON
  [ ] All plan files referenced in active-workflows.json exist
  [ ] All last_snapshot files referenced in active-workflows.json exist

[If all pass:] Runtime state is consistent.
[If any fail:] ⚠ Inconsistency detected: [specific issue] — run /runtime-recover.
```

### Step 4: Detailed workflow view (if wf-id provided)

If `/runtime-status [wf-id]` was invoked:

1. Read `runtime/plans/{wf-id}.json`
2. Read `runtime/state/active-workflows.json` entry for this ID
3. List all snapshot files for this workflow: `runtime/snapshots/{wf-id}-step*.json`
4. List all checkpoint files: `runtime/checkpoints/{wf-id}-gate*.json`
5. Read the last snapshot and present its content

Output:

```
## Workflow Detail: [name] ([wf-id])

Plan
  Created: [timestamp]
  Approved: [timestamp or "pending"]
  Total steps: [N]
  Trigger: "[original request text]"

Steps
  [For each step:]
  [✓/⊙/○/✗] [N]. [Step name]
     Skill: [skill name]
     Output: [output path] [exists? ✓/✗]
     [If completed:] Completed: [timestamp]
     [If pending:] Depends on: [step numbers]
     [If failed:] Failed: [failure context, retry count]

Snapshots
  [List of snapshot files with timestamps]

Checkpoints (Gate Decisions)
  [List of gate checkpoint files with decisions and timestamps]

Events (last 10 for this workflow)
  [List of events filtered by wf-id]
```

---

## Quality Gates

- [ ] No files written — this is read-only
- [ ] Output renders in under 50 lines for the standard dashboard
- [ ] Health check explicitly reports on all 5 consistency conditions
- [ ] Detailed view only shown when a specific wf-id is requested
