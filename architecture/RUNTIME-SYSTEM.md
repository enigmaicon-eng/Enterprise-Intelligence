# Runtime System
## Bounded Autonomous Runtime — Architecture, Rules, and State Schemas

Consolidates: BOUNDED-RUNTIME.md, RUNTIME-STATE-SCHEMA.md

---

## What This Runtime Is

A file-based, human-gated execution layer that persists multi-step workflow state across sessions and machine restarts. The operator starts a workflow, approves each gate, and can pause, resume, or recover at any point. State is always stored in inspectable JSON files. Nothing runs without an explicit human signal.

**What it is not:** An autonomous agent · a background process · a distributed system · a recursive self-directing pipeline · a system that makes decisions without operator visibility.

---

## How the Runtime Works

The runtime is four behaviors, not four components:

1. **Start**: Claude reads `active-workflows.json`. If a workflow is RUNNING or PAUSED, it surfaces it. Otherwise, it proposes a plan, gets approval, and gates on step 1.
2. **Gate**: After each step completes, Claude surfaces the output and waits for explicit approval before step N+1. Nothing proceeds on silence.
3. **Snapshot**: After each step, an immutable snapshot is written to `runtime/snapshots/{wf-id}-stepN.json`.
4. **Recover**: On failure or session end, Claude reads the last valid snapshot and presents recovery options: RETRY / SKIP / REWIND / ABANDON.

That is the entire runtime. The four skills (`/runtime-start`, `/runtime-resume`, `/runtime-status`, `/runtime-recover`) implement these four behaviors.

```
OPERATOR
   │ invokes /runtime-start
   ▼
Claude reads active-workflows.json
   │ surfaces paused workflows or proposes new plan
   ▼
[GATE: operator approval of plan]
   │
   ▼
Step 1 executes → snapshot written → GATE → Step 2 → ... → COMPLETED
                                           │ session ends → PAUSED (resume next session)
                                           │ step fails → GATE (RETRY/SKIP/REWIND/ABANDON)
```

---

## Event Flows

### Flow A — New Workflow

```
Operator request
    │
    ▼ Orchestrator reads active-workflows.json
  Any active workflows? → surface them; don't start new work until resolved
    │
    ▼ Planner decomposes:
  Assigns wf_YYYYMMDD_NNN → writes runtime/plans/{wf-id}.json
    │
    ▼ Plan surfaced: "N-step workflow: [step names]. Start?"
  [GATE: operator approval]
    │
    ▼ WORKFLOW_STARTED event logged
  Domain Executor invokes step 1 skill
    │
    ▼ Step complete → snapshot written: runtime/snapshots/{wf-id}-step1.json
  GATE_PENDING logged
    │
    ▼ Gate presented: "Step 1 complete. Output: [path]. Next: step 2. Continue?"
  [GATE: operator approval]
    │
    ├─ "yes" → RUNNING → next step
    ├─ "pause" → PAUSED → session can end safely
    └─ "stop" → ABANDONED → history updated
    │
    ▼ Final step complete → WORKFLOW_COMPLETED → history.json updated
```

### Flow B — Session Resume

```
Session start → read active-workflows.json
    │
    ├─ No active workflows → normal start
    │
    └─ Active workflows:
         PAUSED → "Workflow [name] paused at step X. Resume?"
         GATE   → "Awaiting approval at step X. Review output?"
         RUNNING → "Was interrupted mid-step. Recover?"
         │
         └─ On resume: read plans/{wf-id}.json + last snapshot
              Re-orient: "Resuming [name]. Completed: [steps]. Next: [step N+1]. Continue?"
              [GATE: one confirmation] → RUNNING → execution resumes
```

### Flow C — Failure Recovery

```
Step execution fails
    │
    ▼ STEP_FAILED logged → status → FAILED
  Snapshot written: {wf-id}-step{N}-failed.json
    │
    ▼ Operator notified: "Step N failed. Recovery: RETRY | SKIP | REWIND | ABANDON"
    │
    ├─ RETRY:  re-run same step, same inputs. Max 3 attempts.
    ├─ SKIP:   mark step N skipped; advance if N+1 doesn't depend on N's output
    ├─ REWIND: restore from chosen snapshot; re-run from there
    └─ ABANDON: status → ABANDONED; history entry written; artifacts preserved
```

---

## Orchestration Rules

**O-1:** Only one workflow in RUNNING state at a time.

**O-2:** No step N+1 begins until the operator approves the gate after step N. "continue", "yes", "proceed" are gate signals.

**O-3:** A step with `depends_on: [N]` cannot start until step N's output file exists on disk. Missing file = blocked, not skipped.

**O-4:** Every step's output path is declared in the plan before execution begins. No step writes to an undeclared path.

**O-5:** Skills may only write to their declared output paths. No side effects on memory files, strategy docs, or undeclared paths.

**O-6:** After each event, state is updated before the next step begins. If the session ends mid-update, state is recoverable from the last valid snapshot.

**O-7:** If a workflow is at GATE state, no new multi-step workflow requests are accepted until the gate is resolved.

---

## Bounded Autonomy Rules

**B-1:** Human gate before every step transition. No automated advancement. Ever.

**B-2:** One "continue" approves exactly one step — not the whole pipeline.

**B-3:** Three retry maximum. After three failures, escalate to operator. No invented workarounds.

**B-4:** The runtime does not update `memory/`, `CLAUDE.md`, or `strategy/` autonomously. These are operator-controlled surfaces.

**B-5:** The Planner produces a plan once. No re-planning mid-execution, no sub-workflows without operator instruction.

**B-6:** Workflows are never silently discarded. ABANDONED requires explicit operator choice.

**B-7:** `/runtime-status` or reading `active-workflows.json` always reflects true current state.

**B-8:** Session end moves RUNNING workflows to PAUSED. Never FAILED, never ABANDONED.

**B-9:** Step failures are surfaced immediately. The runtime does not proceed past a failed step or substitute a different skill.

**B-10:** Each step gets its own gate. Even if steps 2 and 3 are trivial, each requires confirmation.

---

## Human Gate Protocol

Every gate follows this exact sequence:

1. Step completes. Output artifact written to declared path.
2. Snapshot written: `runtime/snapshots/{wf-id}-step{N}.json`.
3. `GATE_PENDING` logged to `runtime/events/queue.json`.
4. Gate presented:
   ```
   Step [N] complete: [step name]
   Output: [file path]
   Key output: [1-2 sentences]

   Next: Step [N+1] — [name]
   Continue? (yes / pause / stop)
   ```
5. Operator responds: yes/continue → RUNNING | pause → PAUSED | stop/abandon → ABANDONED.
6. Gate event logged: `GATE_APPROVED` or `WORKFLOW_PAUSED` or `WORKFLOW_ABANDONED`.

**Anti-patterns:** Offering "shall I continue with steps 2–5?" · auto-continuing after "OK" · describing next step in so much detail it substitutes for doing it.

---

## Failure Classes

| Class | Description | Recovery |
|-------|-------------|---------|
| F1 — Step failure | Skill did not produce its declared output | RETRY, SKIP, ABANDON |
| F2 — Dependency missing | A step's input file doesn't exist | REWIND to step that should have produced it |
| F3 — Interrupted session | Workflow was RUNNING when session ended | Resume from last snapshot |
| F4 — Corrupted state | active-workflows.json unreadable | Reconstruct from most recent valid snapshot |
| F5 — Max retries exceeded | Step failed 3 times | SKIP or ABANDON required |

---

## Execution Lifecycle

```
DRAFT → APPROVED → RUNNING → GATE → RUNNING (next step) ... → COMPLETED
                                  └─ PAUSED → RESUMING → RUNNING
                   RUNNING → FAILED → RETRY → RUNNING
                                    → SKIP/REWIND → RUNNING
                                    → ABANDON → ABANDONED
```

| State | Session-safe? | Meaning |
|-------|:------------:|---------|
| DRAFT | Yes | Plan written, pending review |
| APPROVED | Yes | Plan confirmed, step 1 queued |
| RUNNING | No → moves to PAUSED | Step actively executing |
| GATE | Yes | Awaiting operator confirmation |
| PAUSED | Yes | Operator paused or session ended cleanly |
| RESUMING | Transient | Loading context, one confirmation before RUNNING |
| FAILED | Yes | Recovery needed |
| COMPLETED | Final | All steps done |
| ABANDONED | Final | Operator chose to stop |

---

## State File Schemas

### active-workflows.json

`runtime/state/active-workflows.json` — all non-terminal workflows.

```json
{
  "schema_version": "1.0",
  "last_updated": "2026-05-22T10:30:00Z",
  "workflows": [{
    "id": "wf_20260522_001",
    "name": "Q2 Strategy Synthesis",
    "status": "GATE",
    "created": "2026-05-22T09:00:00Z",
    "last_active": "2026-05-22T10:28:00Z",
    "plan_file": "runtime/plans/wf_20260522_001.json",
    "current_step": 2,
    "total_steps": 4,
    "gate_pending": true,
    "gate_step": 2,
    "gate_message": "Step 2 complete. Review before step 3?",
    "retry_count": 0,
    "last_snapshot": "runtime/snapshots/wf_20260522_001-step2.json"
  }]
}
```

### workflow-history.json

`runtime/state/workflow-history.json` — append-only, terminal workflows.

```json
{
  "schema_version": "1.0",
  "entries": [{
    "id": "wf_20260521_001",
    "name": "Weekly Review Preparation",
    "status": "COMPLETED",
    "created": "2026-05-21T08:00:00Z",
    "completed_at": "2026-05-21T09:45:00Z",
    "total_steps": 3,
    "steps_completed": 3,
    "output_files": ["reviews/weekly/2026-21.md"],
    "abandon_reason": "",
    "notes": ""
  }]
}
```

### Workflow Plan

`runtime/plans/{wf-id}.json` — written once at plan time, immutable after APPROVED.

```json
{
  "schema_version": "1.0",
  "id": "wf_20260522_002",
  "name": "Discovery to PRD Pipeline",
  "trigger": "User: synthesize Q2 discovery findings into a PRD",
  "approved": false,
  "steps": [{
    "index": 1,
    "name": "Synthesize discovery findings",
    "skill": "/pm-discovery",
    "inputs": { "files": ["meeting-intelligence/processed/"] },
    "output_path": "synthesis/2026-05-22-q2-discovery.md",
    "gate": { "type": "human_approval", "required": true },
    "depends_on": [],
    "status": "pending",
    "retry_limit": 3
  }]
}
```

**Gate types:** `human_approval` (explicit yes/no) | `human_review` (operator reviews and provides feedback) | `auto` (diagnostic steps with no downstream effect only).

### Workflow Snapshot

`runtime/snapshots/{wf-id}-step{N}.json` — immutable after write.

```json
{
  "schema_version": "1.0",
  "snapshot_id": "snap_wf_20260522_002_step1",
  "workflow_id": "wf_20260522_002",
  "captured_at": "2026-05-22T11:42:00Z",
  "step_just_completed": 1,
  "total_steps": 3,
  "completed_steps": [{
    "index": 1, "skill": "/pm-discovery",
    "status": "COMPLETED", "output_path": "synthesis/...",
    "output_summary": "7 themes identified.", "retry_count": 0
  }],
  "pending_steps": [{ "index": 2, "skill": "/pm-prd", "status": "pending" }],
  "gate_state": { "step": 1, "type": "human_approval", "approved": false },
  "recovery_valid": true
}
```

### Event Queue

`runtime/events/queue.json` — append-only. Never deleted. The audit trail.

Key event types: `WORKFLOW_PLANNED` · `WORKFLOW_STARTED` · `STEP_STARTED` · `STEP_COMPLETED` · `STEP_FAILED` · `STEP_SKIPPED` · `GATE_PENDING` · `GATE_APPROVED` · `WORKFLOW_PAUSED` · `WORKFLOW_RESUMED` · `WORKFLOW_COMPLETED` · `WORKFLOW_FAILED` · `WORKFLOW_ABANDONED` · `RECOVERY_INITIATED` · `RETRY_ATTEMPTED`

---

## Naming Conventions

| Entity | Pattern | Example |
|--------|---------|---------|
| Workflow ID | `wf_YYYYMMDD_NNN` | `wf_20260522_001` |
| Event ID | `evt_YYYYMMDD_NNN` | `evt_20260522_005` |
| Snapshot ID | `snap_{wf-id}_step{N}` | `snap_wf_20260522_001_step2` |
| Plan file | `runtime/plans/{wf-id}.json` | |
| Snapshot file | `runtime/snapshots/{wf-id}-step{N}.json` | |

---

## State Transition Table

| From | Trigger | To | Files Written |
|------|---------|----|----|
| (none) | Plan created | DRAFT | `plans/{id}.json` |
| DRAFT | Operator approves plan | APPROVED | `active-workflows.json` updated |
| APPROVED | Step 1 begins | RUNNING | `events/queue.json` (WORKFLOW_STARTED) |
| RUNNING | Step N completes | GATE | `snapshots/{id}-step{N}.json`, events |
| GATE | Operator approves | RUNNING | events (GATE_APPROVED) |
| GATE | Operator pauses | PAUSED | `active-workflows.json`, events |
| GATE | Operator abandons | ABANDONED | `workflow-history.json`, `active-workflows.json` cleared |
| PAUSED | Operator resumes | RESUMING | events (WORKFLOW_RESUMED) |
| RUNNING | Session ends unexpectedly | INTERRUPTED | detected at next session start |
| RUNNING | Step fails | FAILED | `snapshots/{id}-step{N}-failed.json`, events |
| FAILED | RETRY | RUNNING | events (RETRY_ATTEMPTED) |
| FAILED | ABANDON | ABANDONED | `workflow-history.json` entry |
| RUNNING | Final step complete | COMPLETED | `workflow-history.json`, `active-workflows.json` cleared |

---

## File Locations Quick Reference

| What | Path |
|------|------|
| Active workflow state | `runtime/state/active-workflows.json` |
| Workflow history | `runtime/state/workflow-history.json` |
| Event log | `runtime/events/queue.json` |
| Workflow plans | `runtime/plans/{wf-id}.json` |
| Step snapshots | `runtime/snapshots/{wf-id}-step{N}.json` |
| Start a workflow | `/runtime-start` |
| Resume a workflow | `/runtime-resume` |
| Check runtime state | `/runtime-status` |
| Recover from failure | `/runtime-recover` |

---

## Anti-Patterns

| Anti-Pattern | Problem | Fix |
|---|---|---|
| Auto-advancing past a gate on "OK" | Removes human control | Explicit gate signal required |
| >7 steps in a single workflow | Plan unmanageable | Break into sub-initiatives |
| Same skill twice with no gate between | Compounding errors without review | Gate after every skill invocation |
| Silently skipping a failed step | Operator doesn't know work was skipped | Surface every skip, get confirmation |
| Writing state files outside `runtime/` | Untrackable state | All runtime state writes to `runtime/` only |
| Continuing when gate is pending in another workflow | Parallel gate states | One gate at a time |
| Treating "yes" on an unrelated question as gate approval | Context dependency failure | Gate approval must name the workflow and step |
