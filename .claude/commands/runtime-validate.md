---
name: runtime-validate
description: >-
  Proactive runtime state integrity validation — reads all files in runtime/
  and checks for JSON parseability, schema completeness, active/history
  disjoint, plan file presence, snapshot presence, retry limit compliance, and
  event queue consistency. Returns VALID / WARNINGS / INVALID with specific
  issues and remediation. Distinct from /runtime-status (which shows workflow
  state) and /ops-dashboard (which shows execution health metrics). Run after
  machine restart, unexpected shutdown, or any time state may be inconsistent.
version: "1.0"
changed: "2026-05-23 — initial"
output: inline (validation report)
---

# /runtime-validate — Runtime State Integrity Validation

## When to Use

- After machine restart or unexpected Claude Code shutdown
- Before resuming a workflow that was RUNNING when interrupted
- After manually editing any file in `runtime/` (even well-intentioned edits can corrupt state)
- As part of the operational continuity protocol (weekly or post-disruption)

**Do NOT use for:**
- Checking current workflow progress → `/runtime-status`
- Viewing execution history metrics → `/ops-dashboard`
- Verifying snapshot recoverability → `/snapshot-verify`
- Cross-layer consistency (traces, memory, knowledge) → `/reliability-check`

---

## Input

```
/runtime-validate              ← Full validation (all runtime/ files)
/runtime-validate --quick      ← JSON parseability + active workflow checks only
/runtime-validate <wf-id>      ← Validate one specific workflow
```

---

## Process

### Step 1 — Read all runtime state files

Read:
- `runtime/state/active-workflows.json`
- `runtime/state/workflow-history.json`
- `runtime/events/queue.json`

If any file is unreadable (missing, invalid JSON, truncated): immediately classify as **INVALID** and report the specific file and error. Do not proceed with checks that depend on the unreadable file.

### Step 2 — Check 1: JSON parseability

Confirm each file can be parsed. If a file is missing entirely:
- `active-workflows.json` missing: INVALID (cannot determine active workflow state)
- `workflow-history.json` missing: WARNING (history lost, active state may still be valid)
- `events/queue.json` missing: WARNING (audit trail lost, state may still be recoverable)

### Step 3 — Check 2: Schema completeness

For each file that parsed successfully:
- Confirm `schema_version` field is present
- Confirm `last_updated` field is present in `active-workflows.json`

Missing schema fields: WARNING.

### Step 4 — Check 3: Active/history disjoint

Extract all workflow IDs from `active-workflows.json` workflows array. Extract all IDs from `workflow-history.json` entries array. Any ID appearing in both: INVALID — the same workflow cannot be both active and completed.

### Step 5 — Check 4: Plan file presence

For each workflow in `active-workflows.json`, check that the file at `plan_file` path exists on disk. Missing plan file: INVALID for that workflow (cannot resume or validate steps without the plan).

### Step 6 — Check 5: Snapshot presence

For each workflow in `active-workflows.json` that has a `last_snapshot` field, check that the file exists on disk.

Missing snapshot when workflow is GATE or PAUSED: INVALID (cannot safely resume).
Missing snapshot when workflow is RUNNING or FAILED: WARNING (may still recover from event log).
`last_snapshot` field absent entirely on a GATE/PAUSED workflow: WARNING.

### Step 7 — Check 6: Retry limit compliance (Hardening Rule H-7)

For each workflow in `active-workflows.json`:
- If `retry_count ≥ 3` AND status = RUNNING or GATE: INVALID — this violates B-3 and H-7; operator must decide SKIP or ABANDON before proceeding.
- If `retry_count = 2` AND status = FAILED: WARNING — one retry remains; surface before the next attempt.

### Step 8 — Check 7: Gate state coherence

For each workflow where `gate_pending = true`: status should be GATE, not RUNNING.
If `gate_pending = true` and status ≠ GATE: INVALID (inconsistent gate/status state).

### Step 9 — Check 8: Event queue tail consistency

Read the last event in `queue.json` for each active workflow (match by workflow ID in event payload if present).
- If last event is `STEP_STARTED` and workflow status is RUNNING: consistent — step was in progress when interrupted.
- If last event is `STEP_COMPLETED` and workflow status is RUNNING (not GATE): WARNING — step completed but gate wasn't set.
- If last event is `WORKFLOW_COMPLETED` and workflow is still in active-workflows: INVALID.

---

## Output Format

```
RUNTIME VALIDATION — [YYYY-MM-DD HH:MM]
Overall result: [VALID ✓ / WARNINGS ⚠ / INVALID ✗]

FILES READ
  active-workflows.json  : [OK / UNREADABLE / MISSING]
  workflow-history.json  : [OK / UNREADABLE / MISSING]
  events/queue.json      : [OK / UNREADABLE / MISSING]

ACTIVE WORKFLOWS ([N] found)
  [wf-id]  [name]  Status: [STATUS]
    Plan file     : [exists / MISSING ✗]
    Last snapshot : [exists / MISSING ✗ / not set]
    Retry count   : [N]   [OK / AT LIMIT ✗]
    Gate coherent : [yes / MISMATCH ✗]
    Event tail    : [consistent / WARNING]

VALIDATION RESULTS

[INVALID issues — blocks safe operation:]
  ✗ [specific issue with file/field/workflow ID]
  ✗ [...]

[WARNINGS — degrade reliability:]
  ⚠ [specific issue]
  ⚠ [...]

[If all clear:]
  ✓ All checks passed. Runtime state is valid.

RECOMMENDED ACTIONS
[For each INVALID: specific remediation step]
[For each WARNING: specific optional action]
[If VALID: "Safe to resume. Run /runtime-resume for any PAUSED/GATE workflows."]
```

---

## Quality Gate

Before outputting:
- [ ] All three state files attempted to read (report missing ones explicitly)
- [ ] All 8 checks run for each active workflow
- [ ] INVALID severity only for issues that block safe operation
- [ ] WARNING severity for issues that degrade but don't block
- [ ] Each finding cites the specific file, field, and workflow ID
- [ ] Remediation step named for every INVALID issue
- [ ] Overall result = INVALID if any single INVALID check fired; WARNINGS if only warnings; VALID otherwise
