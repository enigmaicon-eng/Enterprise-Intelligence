---
name: runtime-hardening
description: P28 Runtime Hardening + Reliability System — 3 skills adding proactive validation, snapshot integrity, and cross-layer consistency checks
metadata:
  type: project
---

# Runtime Hardening + Reliability System (P28)

Built 2026-05-23. Proactive validation and integrity layer on top of the existing bounded runtime (P13) and recovery playbooks.

**Why:** RUNTIME-SYSTEM.md defines a comprehensive state machine, orchestration rules, and failure classes. RECOVERY-PLAYBOOKS.md covers 6 recovery scenarios. Both are reactive — they handle problems after they occur. Nothing validates the runtime state proactively, confirms snapshots are actually recoverable before a REWIND, or checks cross-layer consistency (runtime vs traces vs memory vs knowledge).

**How to apply:** After machine restart/unexpected shutdown → `/runtime-validate` then `/snapshot-verify`. Before REWIND recovery → `/snapshot-verify` to confirm target. Weekly or post-disruption → `/reliability-check`. These are the Operational Continuity Protocol steps documented in the architecture.

## What Was Built

**Architecture doc:** `architecture/RUNTIME-HARDENING-SYSTEM.md` — 8 hardening rules (H-1 through H-8), 3-tier validation protocol (runtime/snapshot/cross-layer), retry policy framework with error class taxonomy, 5 failure containment rules (FC-1 through FC-5), full infrastructure reliability guidance (SQLite/Redis/APScheduler/ChromaDB/filesystem), operational continuity protocol (5 steps), anti-patterns.

**3 new skills:**

- `/runtime-validate` — Runtime state integrity check. Reads active-workflows.json, workflow-history.json, events/queue.json. 8 checks: JSON parseability, schema completeness, active/history disjoint, plan file presence, snapshot presence, retry limit compliance (H-7), gate state coherence, event tail consistency. Returns VALID/WARNINGS/INVALID with specific file/field/workflow citations and remediation steps.

- `/snapshot-verify` — Snapshot recoverability validation. Reads snapshot files for active workflows. 5 checks: required schema fields, recovery_valid flag, completed step output files exist on disk, snapshot chain completeness (no step gaps), timestamp ordering. Returns RECOVERABLE/DEGRADED/UNRECOVERABLE per snapshot. Identifies best REWIND target. References Playbook 6 when no recoverable snapshot exists.

- `/reliability-check` — Cross-layer consistency check. Reads 4 layers: runtime (history → trace alignment), traces (TRACE-INDEX → file existence for exec/pattern/primitive/journal), memory (MEMORY.md index → file existence + frontmatter health), knowledge (KNOWLEDGE-INDEX → files, graph nodes → index, cluster references). Severity: INVALID (blocks a skill), WARNING (degrades), INFO (capture gap). Per-layer flags, priority remediation action.

## Existing Coverage (Not Duplicated)

- RUNTIME-SYSTEM.md — state machine, O-rules, B-rules, failure classes
- RECOVERY-PLAYBOOKS.md — 6 recovery scenarios, decision tree
- `/runtime-recover` — recovery execution
- `/runtime-status` — current workflow state

## Hardening Rules Summary

H-1: Validate before resume after crash. H-2: Verify snapshot before rewind. H-3: One writer per state file. H-4: Write atomically. H-5: Snapshot before every gate. H-6: events/queue.json append-only, never compacted. H-7: retry_count ≥ 3 in RUNNING = hardening violation. H-8: Cross-layer file references must be verifiable.
