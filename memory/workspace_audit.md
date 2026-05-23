---
name: workspace-audit-system
description: P30 Workspace Audit + Simplification Review — 3 skills for constraint compliance, overlap detection, and simplification planning
metadata:
  type: project
---

# Workspace Audit + Simplification Review (P30)

Built 2026-05-23. Repeatable audit methodology for detecting complexity accumulation, constraint violations, skill boundary erosion, and architecture drift. Complements P20 FINAL-SIMPLIFICATION-REVIEW.md — does not duplicate its AC rules.

**Why:** As the workspace grows through P-series phases, skills accumulate past the AC-7 ceiling of 120. No system existed to periodically measure compliance, detect unmanaged overlap, or generate concrete retirement targets.

**How to apply:** Quarterly → `/workspace-audit` + `/skill-overlap` + `/simplify`. After any new P-series (3+ skills) → `/workspace-audit --quick`. Pre-strategy-review → `/skill-overlap --section strategy`.

## Skills (3)

| Skill | Purpose |
|-------|---------|
| `/workspace-audit` | 5-dimension audit against P20 constraints; scale compliance counts with Critical/Warning/OK severity |
| `/skill-overlap` | Pairwise 0-4 overlap scoring by CLAUDE.md section; surfaces retirement and merge candidates |
| `/simplify` | Synthesizes audit + overlap findings into prioritized action plan; outputs delta "X → Y skills" |

## P20 Operational Constraints (enforced by /workspace-audit)

| Constraint | Ceiling |
|-----------|---------|
| Skills (.claude/commands/) | 120 |
| Architecture docs | 25 |
| Workspace memory files | 30 |
| MEMORY.md line count | 200 |
| Ritual stack | 6 |

## Overlap Score Model

Score 0-4 per pair: same primary verb (+1), same output type (+1), trigger overlap (+1), missing mutual "Do NOT use for" (+1).
- 0-1: well-differentiated
- 2: boundary gap — add documentation
- 3-4: retirement or merge candidate

## Architecture

`architecture/WORKSPACE-AUDIT-FRAMEWORK.md`

## Not Duplicating

- `/observe` = workspace telemetry/health snapshot (not constraint compliance)
- `/ops-dashboard` = execution runtime health (not skill ceiling compliance)
- `architecture/FINAL-SIMPLIFICATION-REVIEW.md` = P20 one-time review (AC rules source, not repeatable process)

## Related

[[final_simplification_review]] [[observability_system]] [[trace_capture_system]]
