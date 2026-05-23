---
name: memory-continuity-system
description: P16 complete — Memory + Decision Continuity System; 4-layer memstack, 7 typed memory dirs, retrieval index, lifecycle rules, 6 skills, 6 templates, 2 scripts
metadata:
  type: project
---

Memory + Decision Continuity System (P16). Extends the flat memory/ orientation system with a typed, retrievable, lifecycle-managed cognitive continuity layer.

**Why:** The existing memory/ system stores orientation facts well but has no mechanism for: reasoning context preservation, systematic decision recording with full rationale, failure pattern tracking, working concept management, or context reconstruction after long breaks. P16 adds all of these without replacing the existing system.

**How to apply:** Use `/mem-recall` to search memory before decisions and task starts. Use `/mem-adr` for decisions with real alternatives. Use `/mem-failure` after any workflow failure. Use `/mem-reconstruct` when returning to a topic after >7 days. Use `/mem-hygiene` weekly. Use `/mem-capture` to record reasoning context after significant episodes.

## What Was Built (2026-05-22)

Architecture:
- `architecture/COGNITIVE-MEMORY-SYSTEM.md` — Full system: 4-layer memstack, 7 memory types, retrieval system, decision continuity, lifecycle summary, integration map, anti-patterns
- `architecture/MEMORY-SCHEMAS.md` — Canonical schemas for all 7 memory types with YAML frontmatter + body structure + rules

Memory Infrastructure:
- `memory/MEMORY-MAP.md` — Navigation guide, type map, retrieval guide, when-to-use table
- `memory/MEMORY-LIFECYCLE.md` — Decay rates, review intervals, archive/prune/promotion protocols, memory budget limits
- `memory/RETRIEVAL-INDEX.json` — Machine-readable manifest (initialized empty; built by memory_index.py)
- `memory/archive/ARCHIVE-LOG.md` — Append-only archive log

7 Memory Directories (each with README.md):
- `memory/episodic/` — Layer 1: timestamped experience + reasoning records (ep_*.md, 14-day review)
- `memory/semantic/` — Layer 3: working concept records (sem_*.md, 30-day review, promote when stable)
- `memory/decisions/` — Layer 4: Architecture Decision Records (dec_*.md, 90-day review, permanent)
- `memory/execution/` — Layer 2: task-type execution lessons (exec_*.md, 30-day review, update in place)
- `memory/failures/` — Layer 2: failure records with causal chains (fail_*.md, 30-day review)
- `memory/insights/` — Layer 4: distilled strategic patterns (ins_*.md, 90-day review, ≥3 observations required)
- `memory/context/` — Layer 3: per-topic context reconstructions (ctx_*.md, 30-day review, regenerate not update)
- `memory/archive/` — Archived entries (not active retrieval)

2 Python Scripts:
- `scripts/memory_index.py` — Scans all typed memory dirs, parses frontmatter, builds RETRIEVAL-INDEX.json; --check and --stats flags
- `scripts/memory_prune.py` — Generates prune manifests: overdue reviews, archive candidates, regen-needed, promotion candidates; --preview flag; no auto-delete

6 New Skills:
- `/mem-capture` — Create episodic, semantic, or execution memory; drafts before writing; --type flag
- `/mem-recall` — Search all 7 types via RETRIEVAL-INDEX.json; relevance × recency × link_density scoring; type/date/tag filters
- `/mem-adr` — Create/view/review/supersede Architecture Decision Records; gated creation (2+ real options required)
- `/mem-failure` — Log failure memory; duplicate check before creation; recurrence increment on existing records
- `/mem-reconstruct` — Full context reconstruction across all memory layers for a topic; optional --write to persist ctx_*.md
- `/mem-hygiene` — Weekly memory health audit; surfaces past-due, orphaned, stale, promotion candidates; operator-confirmed actions

6 Templates:
- `templates/episodic-memory.md`
- `templates/semantic-memory.md`
- `templates/adr.md` (Architecture Decision Record)
- `templates/failure-memory.md`
- `templates/insight-memory.md`
- `templates/context-reconstruction.md`

## Core Design Decisions

- 7 typed subdirs alongside existing flat memory/ files — no migration, no disruption to existing orientation memory
- RETRIEVAL-INDEX.json as machine-readable manifest — skills scan index, not filesystem
- Lifecycle rules are enforced by /mem-hygiene + memory_prune.py — no auto-deletion
- ADRs never deleted — status=superseded with superseded_by link is the terminal state
- Failure records: duplicate check before create, recurrence increment on existing
- Promotion path: semantic → knowledge/ when stable (not a one-way door — must be explicitly promoted)
- Memory budget limits: soft limits per type, hard limits trigger automatic archival of oldest entries

[[bounded_runtime]]
[[persistent_execution_system]]
[[dynamic_invocation]]
