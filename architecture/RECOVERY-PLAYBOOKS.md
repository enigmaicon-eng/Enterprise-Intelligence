# Recovery Playbooks
## Operator Guides for the File-Based Bounded Runtime

---

## When to Use This Document

When a workflow is in an unexpected state after a session restart, machine reboot, or crash. Use `/runtime-recover` for most recovery actions — these playbooks document the decision logic and edge cases.

---

## Playbook 1 — Session Restart (Normal)

**Situation:** You closed Claude Code and are starting a new session. A workflow was PAUSED or at GATE.

**Expected behavior:** `/runtime-resume` detects the paused workflow automatically.

**Steps:**
1. Open session.
2. Run `/briefing` — it surfaces any PAUSED or GATE workflows.
3. Or run `/runtime-resume` directly.
4. Confirm the re-orientation block (workflow name, step, last action, next step).
5. Provide gate signal if at GATE, or proceed if PAUSED.

No recovery needed. The workflow's status in `runtime/state/active-workflows.json` is PAUSED or GATE, and the snapshot at `runtime/snapshots/{wf-id}-step{N}.json` holds the full state.

---

## Playbook 2 — Machine Restart or Unexpected Shutdown

**Situation:** Claude Code closed without `/shutdown` being called. A workflow was RUNNING when it closed.

**Detection signals:**
- Workflow status is RUNNING in `active-workflows.json`
- Most recent event in `runtime/events/queue.json` is `STEP_STARTED` with no following `STEP_COMPLETED`

**Steps:**
1. Run `/runtime-recover <workflow_id>`.
2. Review the diagnosis — interrupted workflows are classified as F3 (session interrupted mid-step).
3. Identify the last valid snapshot from `runtime/snapshots/`.
4. Verify output files from completed steps are present on disk.
5. Choose recovery option:
   - If the interrupted step produced no output: REWIND to last snapshot, then resume.
   - If the interrupted step produced partial output: REWIND, manually delete the partial output, then resume.
   - If you are confident the step completed: RETRY (the skill will re-check whether output already exists).
6. Confirm your chosen option — `/runtime-recover` always requires explicit approval before executing.

**Prevention:** Always run `/shutdown` before closing Claude Code. `/shutdown` moves any RUNNING workflow to PAUSED.

---

## Playbook 3 — Corrupted JSON State Files

**Situation:** `runtime/state/active-workflows.json` cannot be parsed, or a snapshot file is truncated.

**Detection signals:**
- JSON parse error when reading active-workflows.json
- `/runtime-status` shows no workflows despite knowing one was active
- A snapshot file in `runtime/snapshots/` is clearly truncated

**Steps:**
1. Identify the affected workflow ID from the filename of the most recent snapshot.
2. Read the most recent valid snapshot: `runtime/snapshots/{wf-id}-step{N}.json`.
3. Reconstruct `active-workflows.json` manually from the snapshot's state fields.
4. Take a new snapshot immediately by running `/runtime-recover` → any action that triggers a state write.
5. Verify with `/runtime-status`.
6. Proceed with `/runtime-resume`.

**Why this works:** Snapshots are written atomically and are immutable after creation. Even if the active state file is corrupted, the most recent completed snapshot is always a valid starting point.

---

## Playbook 4 — Missing Artifacts

**Situation:** A workflow step expected an input file that no longer exists.

**Detection signals:**
- `/runtime-resume` reports "input file not found" before a step
- A step's declared output path is empty or missing

**Steps:**
1. Read the workflow's current snapshot to identify which step's output is missing.
2. Assess: can the missing file be regenerated?
   - **If yes:** REWIND to the snapshot before that step, then re-run it.
   - **If no (permanently gone):** REWIND to a checkpoint before the step that required it, then re-run from there.
3. Run `/runtime-recover <workflow_id>` → REWIND to the appropriate snapshot.
4. Resume from the rewound state.

**Prevention:** Never manually delete files in workflow output directories while a workflow is active. PAUSE the workflow first, clean up, then resume.

---

## Playbook 5 — Step Failure (Skill Error)

**Situation:** A skill returned an error during execution. Workflow status is FAILED.

**Failure class:** F1

**Steps:**
1. Read `runtime/events/queue.json` for the STEP_FAILED event and its error payload.
2. Identify the root cause from the event data.
3. Run `/runtime-recover <workflow_id>` and choose:
   - **RETRY:** If the input was fixable or the error was transient. Fix the input first, then retry. Maximum 3 attempts.
   - **SKIP:** Only if no downstream steps depend on this step's output.
   - **REWIND:** If you want to re-approach the step differently.
   - **ABANDON:** If the workflow is no longer viable.

---

## Playbook 6 — No Valid Snapshot Exists

**Situation:** A workflow needs recovery but no valid snapshots exist in `runtime/snapshots/`.

**Why this happens:**
- Workflow crashed before the first step completed (before the first snapshot was written)
- Snapshot files were manually deleted

**Steps:**
1. Read `runtime/events/queue.json` for this workflow's events.
2. Check which step output files exist on disk in the declared output directories.
3. If steps 0..N are confirmed complete (output files present):
   - Manually set the workflow's `current_step` in `active-workflows.json` to step N+1.
   - Resume — the next step will write a new snapshot on completion.
4. If no steps completed: restart the workflow from the beginning with `/runtime-start` using the same plan.

---

## Recovery Decision Tree

```
Workflow in unexpected state
         │
         ▼
  Run /runtime-recover
         │
    ┌────┴───────────────────────────────┐
    │                                    │
    ▼                                    ▼
Status = PAUSED/GATE               Status = RUNNING/FAILED
(normal pause)                     (interrupted/failed)
    │                                    │
    ▼                                    ▼
/runtime-resume                   Read queue.json events
                                  Read snapshots/
                                         │
                              ┌──────────┼─────────────┐
                              │          │             │
                              ▼          ▼             ▼
                           F1 FAIL    F3 INTERRUPT  F4 CORRUPT
                           (skill)    (no shutdown) (bad JSON)
                              │          │             │
                              ▼          ▼             ▼
                           RETRY/SKIP  REWIND+RESUME  manual
                           (≤3 times)  (snapshot)     reconstruct
```

---

## Quick Reference

| Symptom | Playbook | Action |
|---------|----------|--------|
| Workflow paused, starting new session | 1 | `/runtime-resume` |
| Machine restarted, workflow was RUNNING | 2 | `/runtime-recover` → REWIND or RETRY |
| JSON state file corrupted | 3 | Read snapshot, reconstruct manually |
| Output file from prior step is missing | 4 | `/runtime-recover` → REWIND |
| Step failed with error | 5 | Read queue.json → `/runtime-recover` |
| No snapshots exist | 6 | Check disk, restart or manual reconstruct |

---

## Related

- `/runtime-recover` — primary recovery skill
- `/runtime-resume` — resume a paused or gate-pending workflow
- `/runtime-status` — current workflow state
- `architecture/RUNTIME-SYSTEM.md` — full runtime architecture and state schema
