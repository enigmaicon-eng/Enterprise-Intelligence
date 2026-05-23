---
name: trace-capture-system
description: P21 Trace Capture + Skill Codification System — personal operational memory compounding
metadata:
  type: project
---

# Trace Capture + Skill Codification System (P21)

Built 2026-05-23. Personal operational memory compounding for one operator.

**Why:** Without execution memory, every session starts blank. Repeated failure modes get re-discovered; working sequences get re-invented. This system closes that loop by making execution history retrievable.

**How to apply:** Before starting complex work, run /trace-recall. After meaningful sessions, run /trace-capture or /workflow-journal. Run /pattern-mine monthly or after /trace-capture flags 2+ pattern candidates.

## What Was Built

**Architecture doc:** `architecture/TRACE-CAPTURE-SYSTEM.md`

**5 skills:**
- `/trace-capture` — structured execution trace after a session (>30 min, multi-step)
- `/workflow-journal` — lightweight 5-minute daily log
- `/trace-recall` — relevance-scored retrieval before starting similar work
- `/trace-search` — keyword/filter search across execution history
- `/pattern-mine` — detect + codify recurring patterns (two-gate: detect → approve → write)

**Templates:**
- `templates/execution-trace.md` — YAML + 10 sections
- `templates/execution-pattern.md` — pattern_id, pattern statement, trigger conditions, anti-triggers
- `templates/execution-primitive.md` — procedure checklist format

**Infrastructure:**
- `traces/TRACE-INDEX.md` — master retrieval index (all skills read this first)
- `traces/executions/` — episodic memory (exec_YYYYMMDD_NNN.md)
- `traces/journal/` — working memory (YYYY-MM-DD.md)
- `traces/patterns/` — semantic memory (pat_<slug>.md)
- `traces/primitives/` — procedural memory (prim_<slug>.md)
- `traces/archive/` — cold storage (90+ day episodes)

## Memory Tiers

| Tier | Contents | Always-loaded? |
|------|----------|---------------|
| Hot | Today's journal | Yes |
| Warm | Episodes 0–90 days + all patterns + primitives | On demand |
| Cold | archive/ (90+ days) | Retrieval only |

## Scope Constraints

This is NOT: collective intelligence, org-level shared cognition, autonomous capability evolution.
This IS: one operator's execution history, made searchable and retrievable.

No Python scripts. No automated pattern detection. No SQLite. Operator approves all codification steps.

## Promotion Pathway

execution trace → pattern candidate flagged → /pattern-mine → pattern/primitive entry → (if warranted) /skill-new
