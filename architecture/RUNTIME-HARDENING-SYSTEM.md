# Runtime Hardening + Reliability System

Extends `architecture/RUNTIME-SYSTEM.md` with proactive validation, snapshot integrity verification, infrastructure reliability patterns, and operational continuity protocols. The existing system handles recovery after problems occur — this system prevents and detects problems before they cascade.

## Existing Coverage (Do Not Duplicate)

| Concern | Covered By |
|---------|-----------|
| Workflow state machine | RUNTIME-SYSTEM.md (O-1 – O-7, B-1 – B-10) |
| Recovery procedures | RECOVERY-PLAYBOOKS.md (Playbooks 1–6) |
| Workflow start/resume/recover | `/runtime-start`, `/runtime-resume`, `/runtime-recover` |
| Current workflow status | `/runtime-status` |
| Execution tracing | `/trace-capture`, `/exec-inspect` |

## New Capabilities (P28)

| Concern | Gap | Skill |
|---------|-----|-------|
| State file integrity | No proactive check of runtime/ consistency | `/runtime-validate` |
| Snapshot recoverability | No check that snapshots would actually support recovery | `/snapshot-verify` |
| Cross-layer coherence | No check of consistency across runtime/, traces/, memory/, knowledge/ | `/reliability-check` |

---

## Hardening Rules

Extensions to the existing O-* and B-* rules. Reference these when building or modifying workflows.

**H-1 — Validate before resume.**
Run `/runtime-validate` before resuming any workflow interrupted by machine restart or unexpected shutdown. Never resume from potentially corrupted state without validation.

**H-2 — Verify snapshot before rewind.**
Run `/snapshot-verify` before selecting a snapshot for REWIND recovery. A snapshot that passes schema validation may still reference missing output files.

**H-3 — One writer per state file.**
`active-workflows.json`, `workflow-history.json`, and `events/queue.json` must never be written by two processes concurrently. In a multi-session environment, serialise writes through file locking or a dedicated writer process.

**H-4 — Write atomically.**
State file updates must be written atomically: write to a temp file, verify the write, then rename to the target path. A partial write to `active-workflows.json` renders it unreadable.

**H-5 — Snapshot before every gate, not just after.**
The pre-gate snapshot is written AFTER a step completes. If the step produced partial output, the snapshot captures the partial state. Supplement with a pre-step checkpoint if the step is destructive.

**H-6 — events/queue.json is append-only and never compacted.**
The event queue is the ground truth for audit and forensic recovery. Compacting or rotating it removes recovery capability. Archive rather than delete if size becomes a concern.

**H-7 — Retry count is a contract, not a suggestion.**
B-3 sets 3 as the maximum retry count. `/runtime-validate` checks that no active workflow has `retry_count ≥ 3` in RUNNING state — that is a hardening violation requiring immediate operator decision.

**H-8 — Cross-layer references must be verifiable.**
Any file path written into a state file (plan output_path, snapshot output_path) must point to a path that can be confirmed to exist at read time. Broken references are detected by `/reliability-check`.

---

## Validation Protocols

### Runtime Layer Validation (`/runtime-validate`)

Check in this order:

1. **JSON parseability**: can each file in `runtime/state/` be parsed without error?
2. **Schema completeness**: does each file have `schema_version` and `last_updated`?
3. **Active/history disjoint**: no workflow ID appears in both `active-workflows.json` and `workflow-history.json`
4. **Plan file presence**: every `plan_file` path in active workflows exists on disk
5. **Snapshot presence**: every `last_snapshot` path in active workflows exists on disk
6. **Retry limit compliance**: no active workflow has `retry_count ≥ 3` in RUNNING state
7. **Gate state coherence**: if `gate_pending = true`, the workflow status should be GATE, not RUNNING
8. **Event tail consistency**: the last event in `queue.json` for each active workflow should match its current status

Severity levels:
- **INVALID**: blocks safe operation (unreadable JSON, missing plan file, retry limit exceeded)
- **WARNING**: degrades reliability but doesn't block (snapshot missing, schema field absent)
- **VALID**: all checks pass

### Snapshot Layer Validation (`/snapshot-verify`)

For each snapshot file:

1. **Schema fields**: `schema_version`, `snapshot_id`, `workflow_id`, `captured_at`, `step_just_completed`, `recovery_valid` are all present
2. **recovery_valid flag**: explicitly `true` — a snapshot written during a failed step may have `recovery_valid: false`
3. **Completed step outputs**: for each entry in `completed_steps`, the declared `output_path` exists on disk
4. **Snapshot chain completeness**: for a given workflow, snapshots exist for steps 1..N without gaps
5. **Timestamp ordering**: snapshot timestamps are monotonically increasing across the step chain

Recoverability levels:
- **RECOVERABLE**: all checks pass; rewind to this snapshot is safe
- **DEGRADED**: snapshot is valid but one or more output files are missing; rewind possible but step re-run may be needed
- **UNRECOVERABLE**: recovery_valid=false, or schema incomplete; do not use for rewind

### Cross-Layer Validation (`/reliability-check`)

Four layers checked:

1. **Runtime → Traces**: completed workflows in `workflow-history.json` should appear in `traces/TRACE-INDEX.md` (captures execution memory). Orphaned completed workflows have no trace.

2. **Memory layer**: every file path in `memory/MEMORY.md` index entries should exist as an actual file in `memory/`. Dangling index entries corrupt future recall.

3. **Knowledge layer**: every entry in `knowledge/KNOWLEDGE-INDEX.md` should correspond to an existing file in `knowledge/<domain>/`. Dead index entries are surfaced by `/knowledge-qa` but not by runtime checks.

4. **Trace layer**: every `exec_*` row in `traces/TRACE-INDEX.md` should point to a file in `traces/executions/` that exists. Missing trace files break `/trace-recall` and `/exec-inspect`.

---

## Retry Policy Framework

Extends B-3 (3-retry max) with explicit retry taxonomy.

| Error Class | Retry Appropriate? | Max Retries | Retry Strategy |
|-------------|-------------------|-------------|---------------|
| Transient tool error | Yes | 3 | Immediate retry; same inputs |
| Missing input file | No | 0 | REWIND to step that should have produced it |
| Output path conflict | Yes | 1 | Clear the conflicting path, then retry |
| Skill timeout | Yes | 2 | Retry with reduced scope if possible |
| Operator input required | No | 0 | Pause; await operator correction |
| Environmental failure | Yes | 3 | Retry after environment check |

**Retry escalation:** After 2 retries on the same step, surface a diagnosis before the 3rd attempt. After 3 failures, SKIP or ABANDON — do not offer a 4th retry.

---

## Failure Containment Rules

**FC-1 — A step failure cannot contaminate adjacent workflows.**
Step failures are scoped to their workflow ID. The event queue, snapshots, and state file updates for one workflow never affect another workflow's state.

**FC-2 — Partial output is quarantined, not silently retained.**
If a step produces partial output before failing, the partial file must be noted in the failure snapshot and NOT treated as a completed artifact by downstream steps.

**FC-3 — FAILED status is sticky until operator action.**
A workflow in FAILED state must stay in FAILED until the operator explicitly chooses RETRY, SKIP, REWIND, or ABANDON. The runtime does not auto-recover.

**FC-4 — Recovery actions are logged before execution.**
Before executing a REWIND or RETRY, log a `RECOVERY_INITIATED` event with the chosen action, rationale, and target snapshot. This is the audit record.

**FC-5 — Cascading failure detection.**
If the same step fails on 2+ different workflows in the same session, flag a potential systemic issue (not just transient). Recommend investigating the shared skill or environment before further retries.

---

## Infrastructure Reliability Model

The workspace is file-based. The following guidance applies if infrastructure layers are added.

### SQLite

**When to add:** Workflow count grows past ~50/month; query performance on history becomes slow; multi-session concurrent access is needed.

**Hardening requirements:**
- Enable WAL mode: `PRAGMA journal_mode=WAL` — prevents write locks from blocking reads
- Enable foreign key constraints: `PRAGMA foreign_keys=ON`
- Use transactions for all state updates: never write multiple tables in separate statements
- Keep `events/queue.json` as the append-only audit trail even after migrating state to SQLite — the file log survives DB corruption
- Daily backup: `sqlite3 runtime.db .dump > runtime_YYYYMMDD.sql`

### Redis

**When to add:** Session resumption latency is unacceptable; need sub-second active workflow lookup; concurrent operator sessions.

**Hardening requirements:**
- Persistence: `appendonly yes` in redis.conf — AOF prevents data loss on restart
- Set TTL on transient gate-state keys (e.g., `gate:wf_id:step_N` expires after 24h if not consumed)
- Never use Redis as the system of record for workflow state — use it as a cache; file/SQLite is authoritative
- Connection retry: client-side retry with exponential backoff (max 3 attempts, 1s/2s/4s)

### APScheduler

**When to add:** Recurring workflows need to be triggered on a schedule without operator initiation.

**Hardening requirements:**
- Use `SQLAlchemyJobStore` backed by the runtime SQLite DB — in-memory job stores don't survive restarts
- Set `misfire_grace_time` to account for session gaps (e.g., 3600s for daily jobs)
- Always check for already-running instances before firing a scheduled job (O-1: one RUNNING workflow at a time)
- Log all scheduled firings to `runtime/events/queue.json` as `WORKFLOW_SCHEDULED_TRIGGER` events

### ChromaDB

**When to add:** Knowledge base exceeds ~500 entries; semantic recall accuracy matters more than keyword recall; `/recall` query time is slow.

**Hardening requirements:**
- Persist to disk: `chromadb.PersistentClient(path="chroma/")` — not in-memory
- Keep `knowledge/KNOWLEDGE-INDEX.md` in sync: ChromaDB and the markdown index must agree on entry IDs
- Rebuild on corruption: `chroma/` directory can be deleted and rebuilt from `knowledge/` — it's a derived index, not the source of truth
- Version stamp: store `schema_version` as collection metadata to detect incompatible index rebuilds

### Local Filesystem Persistence

**Hardening requirements (currently active layer):**
- Atomic writes: write to `.tmp` → verify → rename. Never write directly to the target path.
- Immutable snapshots: snapshots are written once and never modified. New state = new file.
- Backup strategy: use git or file-copy to snapshot `runtime/` before disruptive operations.
- Size limits: `events/queue.json` can grow unboundedly. Archive entries older than 90 days to `runtime/archive/events-YYYY-MM.json`.
- Read-before-write: always read the current file state before appending or updating, to detect concurrent modification.

---

## Operational Continuity Protocol

Run this sequence after any of: machine restart, unexpected shutdown, environment change, >7 days away from the workspace.

**Step 1 — Runtime layer check.**
Run `/runtime-validate`. If INVALID: do not resume any workflow until issues are resolved. If WARNING: review warnings, proceed with known limitations.

**Step 2 — Snapshot recoverability check.**
Run `/snapshot-verify` for all active workflows. If any are UNRECOVERABLE: decide ABANDON or manual reconstruct before proceeding.

**Step 3 — Cross-layer check.**
Run `/reliability-check`. Resolve any INVALID-level issues (broken file references in critical indices) before running knowledge or trace operations.

**Step 4 — Operational briefing.**
Run `/briefing` to surface current priorities. Run `/ops-dashboard` to confirm execution health.

**Step 5 — Resume or defer.**
With clean validation across all layers, proceed. With unresolved issues: scope work to unaffected layers only.

---

## Anti-Patterns

| Anti-pattern | Why it fails |
|-------------|-------------|
| Running /runtime-resume without /runtime-validate after a crash | Resuming from corrupted state corrupts further |
| Treating events/queue.json as compactable | Losing event history destroys audit trail and forensic recovery |
| Selecting a snapshot for REWIND without verifying its output files still exist | Rewinding to a snapshot that references missing files leaves the workflow unresumable |
| Adding Redis/SQLite before understanding file-based failure modes | Infrastructure adds failure modes faster than it removes them at small scale |
| Ignoring WARNING-level validation results | Warnings accumulate into INVALID state; they signal debt, not tolerance |
| Running /reliability-check on every session start | Cross-layer check is expensive; run it after disruption or weekly, not every session |
