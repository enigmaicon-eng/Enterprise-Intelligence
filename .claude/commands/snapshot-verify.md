---
name: snapshot-verify
description: >-
  Snapshot recoverability verification — reads workflow snapshots and confirms
  they can actually support a REWIND recovery: schema completeness, recovery_valid
  flag, output files exist on disk, snapshot chain has no gaps. Returns
  RECOVERABLE / DEGRADED / UNRECOVERABLE per snapshot with specific issues.
  Use before selecting a snapshot for REWIND in /runtime-recover. Distinct from
  /runtime-validate (which checks state file consistency) and /exec-snapshot
  (which writes new snapshots).
version: "1.0"
changed: "2026-05-23 — initial"
output: inline (snapshot recoverability report)
---

# /snapshot-verify — Snapshot Recoverability Verification

## When to Use

- Before REWIND recovery: confirm the target snapshot can actually support recovery
- After unexpected shutdown: verify the most recent snapshot is usable before resuming
- Periodic audit: confirm no snapshots have become stale due to file moves or deletions
- After manually managing output files: check that snapshots still reference valid paths

**Do NOT use for:**
- Writing a new snapshot → `/exec-snapshot`
- Validating runtime state files (JSON consistency, active/history) → `/runtime-validate`
- Full cross-layer coherence → `/reliability-check`

---

## Input

```
/snapshot-verify                    ← All active workflow snapshots
/snapshot-verify <wf-id>            ← All snapshots for one workflow
/snapshot-verify <snapshot-id>      ← One specific snapshot
/snapshot-verify --all              ← All snapshots including completed workflows
```

---

## Process

### Step 1 — Identify scope

Read `runtime/state/active-workflows.json`. Extract `last_snapshot` paths for each active workflow.

For `--all` flag: also read `runtime/state/workflow-history.json` and find snapshot paths referenced in history entries if any.

For a specific `<wf-id>`: list all files in `runtime/snapshots/` matching `{wf-id}-step*.json`, sorted by step number.

### Step 2 — Read each snapshot file

For each snapshot path:
- Check the file exists. If not: classify immediately as UNRECOVERABLE and note path.
- Read the file content.
- Check JSON parseability. If invalid JSON: UNRECOVERABLE.

### Step 3 — Check 1: Required schema fields

Verify presence of all required fields:

| Field | Required | If missing |
|-------|----------|-----------|
| `schema_version` | Yes | WARNING |
| `snapshot_id` | Yes | WARNING |
| `workflow_id` | Yes | INVALID — cannot associate to a workflow |
| `captured_at` | Yes | WARNING |
| `step_just_completed` | Yes | INVALID — cannot determine recovery point |
| `recovery_valid` | Yes | Treat as false if absent |
| `completed_steps` | Yes | INVALID |
| `pending_steps` | Yes | WARNING (may be empty on final step) |

INVALID-field snapshots: UNRECOVERABLE.
WARNING-field snapshots: DEGRADED.

### Step 4 — Check 2: recovery_valid flag

If `recovery_valid = false` (or absent): this snapshot was written during a failure event and MUST NOT be used for REWIND without operator review. Mark UNRECOVERABLE for REWIND purposes. Note: this snapshot may still be useful for forensic analysis.

### Step 5 — Check 3: Completed step output files

For each entry in `completed_steps`:
- If `output_path` is declared: check the file exists on disk.
- Missing output file for a completed step: DEGRADED.
- More than one missing output file: UNRECOVERABLE (rewind would leave the workflow without multiple required artifacts).

Note: a single missing output file may be acceptable if the REWIND goes back further than this snapshot. Flag and let the operator decide.

### Step 6 — Check 4: Snapshot chain completeness

For a given workflow, snapshots should exist for steps 1 through N without gaps. If step 3's snapshot exists but step 2's is missing, rewind to step 3 is not problematic, but rewind to step 2 is impossible.

Report the chain: which steps have snapshots, which are missing.

### Step 7 — Check 5: Timestamp ordering

Snapshot `captured_at` timestamps should increase monotonically by step number. Out-of-order timestamps suggest state file manipulation and should be flagged as WARNING.

---

## Output Format

```
SNAPSHOT VERIFICATION — [YYYY-MM-DD HH:MM]

[For each workflow:]

── Workflow: [wf-id]  "[name]" ──
  Status: [workflow status]
  Snapshot chain: step [N] → step [N] → step [N]   [or: GAPS at steps [N, N]]

  snap_[wf-id]_step[N]  ([captured_at])
    recovery_valid : [true / false / absent]
    Schema fields  : [complete / WARNINGS: list missing fields]
    Output files   : [N/N present]  [or: MISSING: [path]]
    Timestamp order: [OK / OUT OF ORDER]
    Result: [RECOVERABLE ✓ / DEGRADED ⚠ / UNRECOVERABLE ✗]
    [If DEGRADED: "Missing: [path]. Rewind possible but step [N] re-run likely needed."]
    [If UNRECOVERABLE: specific reason]

  [repeat for each snapshot in chain]

  BEST REWIND TARGET: snap_[wf-id]_step[N]  ([reasoning])
  [If no valid target: "No recoverable snapshot. Use ABANDON or manual reconstruct — see Playbook 6."]

SUMMARY
Snapshots verified: [N]
RECOVERABLE: [N]  |  DEGRADED: [N]  |  UNRECOVERABLE: [N]

[If DEGRADED/UNRECOVERABLE present:]
Before running /runtime-recover, note:
  [specific per-workflow issues and recommended target snapshot]
```

---

## Quality Gate

Before outputting:
- [ ] Each snapshot file read from disk (not inferred from active-workflows.json data)
- [ ] recovery_valid=false triggers UNRECOVERABLE classification regardless of other checks
- [ ] Output file existence checked for each completed_step, not just the last step
- [ ] Snapshot chain gaps reported by specific missing step numbers
- [ ] Best REWIND TARGET identified: the most recent RECOVERABLE snapshot
- [ ] If no RECOVERABLE snapshots exist: Playbook 6 reference given
- [ ] DEGRADED means "usable with caveats" — operator must decide; do not block automatically
