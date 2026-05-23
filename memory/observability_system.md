---
name: observability-system
description: P22 Operational Observability System — 5 skills for runtime visibility and execution introspection
metadata:
  type: project
---

# Operational Observability System (P22)

Built 2026-05-23. Fills the diagnostic gap between what `/observe` covers (API costs/cache/quality) and what the operator needs to understand operational execution health.

**Why:** Without observability, failure patterns go undetected, trace history goes unanalyzed, and the retrieval system silently degrades. These 5 skills make the operational layer inspectable.

**How to apply:** Run `/ops-dashboard` at the start of a work block. Use `/retrieval-diag` monthly. Use `/failure-review` when failure density is elevated. Use `/exec-inspect` to understand any specific trace. Use `/skill-stats` before a pattern-mining session.

## What Was Built

**Architecture doc:** `architecture/OBSERVABILITY-SYSTEM.md`

**5 skills:**
- `/ops-dashboard` — integrated operational dashboard (execution history + runtime state + pattern coverage + recommended actions)
- `/exec-inspect` — deep structured inspection of a single execution trace (timeline, decisions, artifacts, failures, candidates)
- `/skill-stats` — skill invocation analytics (type distribution, tag frequency, outcome rates, pattern mining opportunities)
- `/failure-review` — failure pattern analysis (taxonomy of failed/partial/abandoned, recurring failure modes, /pattern-mine feed)
- `/retrieval-diag` — retrieval system health (index completeness, coverage gaps, recall readiness score, open candidates)

## What Already Existed (Not Duplicated)

| Skill | Covers |
|-------|--------|
| `/observe` | API cost, cache rates, quality scores |
| `/runtime-status` | Active workflow state, event queue |
| `/context-audit` | 8-dimension context health |
| `/debug-ai` | AI system failure diagnosis |

## Scope

Single-operator, conversational observability. No Python scripts. No automated monitoring. No continuous collection. All skills read existing file-based state on demand.

## Related

[[trace_capture_system]] [[final_simplification_review]]
