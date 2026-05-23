---
name: bounded-runtime
description: Bounded Autonomous Runtime (BAR) — P13 complete 2026-05-22; persistent file-based workflow execution layer with 4 skills, 2 architecture docs, runtime state infrastructure
metadata:
  type: project
---

Bounded Autonomous Runtime (BAR) implemented as P13 of the workspace build. File-based stateful workflow execution layer that persists multi-step workflow state across sessions and machine restarts.

**Why:** Existing skills handle individual invocations well, but multi-step workflows that span sessions had no state continuity — each session started cold even if work was mid-flight.

**How to apply:** For any request spanning 2+ skills in sequence, or work that must survive session interruption, use `/runtime-start` to create a tracked workflow with human gates. Single-skill requests bypass the runtime entirely.

## What Was Built

- `architecture/BOUNDED-RUNTIME.md` — Master runtime architecture: 8 components, 3 event flows, orchestration rules, bounded autonomy rules, execution lifecycle, failure recovery, state persistence, session continuity protocol
- `architecture/RUNTIME-STATE-SCHEMA.md` — All JSON schemas: workflow plan, active state, history, snapshots, gate checkpoints, event queue, invocation log
- `runtime/state/active-workflows.json` — Live workflow state (starts empty)
- `runtime/state/workflow-history.json` — Completed/failed/abandoned history (append-only)
- `runtime/events/queue.json` — Append-only event log
- `runtime/plans/` — One JSON plan file per workflow
- `runtime/snapshots/` — Immutable step-completion snapshots (recovery foundation)
- `runtime/checkpoints/` — Gate decision records (audit trail)
- `.claude/commands/runtime-start.md` — Start a multi-step workflow
- `.claude/commands/runtime-resume.md` — Resume paused/interrupted/gate-pending workflows
- `.claude/commands/runtime-status.md` — Runtime state dashboard
- `.claude/commands/runtime-recover.md` — Failure recovery: RETRY / SKIP / REWIND / ABANDON
- `templates/workflow-plan.json` — Plan file template
- `templates/workflow-snapshot.json` — Snapshot file template

## Core Invariants

- Human gate required before every step transition
- Maximum 3 retries per step before operator escalation
- Session end pauses (never aborts) active workflows
- All runtime state is human-readable JSON at all times
- Recovery always operator-initiated — runtime surfaces options, operator chooses
- No autonomous memory writes during workflow execution

## Status

Operational. Runtime state is initialized (empty). First workflow requires `/runtime-start`.

[[project_workspace_blueprint]]
