---
title: Final Autonomy Simplification
type: project
updated: 2026-05-23
current_as_of: 2026-05-23
---

# Final Autonomy Simplification — P20 + SR-1 + SR-5

Complete as of 2026-05-23. The autonomous runtime layer (P13–P19) underwent a full simplification review and two major structural simplifications.

## What Was Eliminated

**SR-1 — SQLite Persistence Layer (P15):**
- 4 exec-* skills retired: exec-journal, exec-timeline, exec-snapshot, exec-diagnose
- 6 Python scripts deleted: db_init.py, event_store.py, checkpoint_manager.py, recovery_engine.py, artifact_tracker.py, timeline_viewer.py
- runtime/persistence/ cleared
- RECOVERY-PLAYBOOKS.md rewritten to file-based approach only
- Reason: zero workflows ever executed in P15; dual-write complexity without benefit

**SR-2 (earlier) — Invocation Overhead:**
- skill-invoke, skill-deps, skill-gaps retired
- Reason: 7-step routing pipeline for 110 named skills is theater

## What Was Consolidated

**SR-5 — Architecture Document Merges:**
- OPERATIONAL-ROUTING.md ← 4 routing/orchestration docs
- SKILL-SYSTEM.md ← 3 skill architecture/routing docs
- CONTEXT-SYSTEM.md ← 3 context architecture/engineering docs
- RUNTIME-SYSTEM.md ← 2 runtime/schema docs

## Governing Constraints Going Forward

**10 Anti-Complexity Rules (AC-1 through AC-10):** Max 120 skills; max 25 arch docs; no new persistence without 100 workflow executions; one gate mechanism; skills not skills-about-skills; no enterprise patterns for solo-operator problems.

**Full specification:** `architecture/FINAL-SIMPLIFICATION-REVIEW.md`

## What the Workspace Is Now

A skill library with file-based memory, operator-gated multi-step workflows, and governed external tool access. Nothing more.
