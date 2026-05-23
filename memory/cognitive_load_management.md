---
name: cognitive-load-management
description: P29 Cognitive Load Management System — 3 skills for open loop inventory, aggregate load assessment, and strategic attention alignment
metadata:
  type: project
---

# Cognitive Load Management System (P29)

Built 2026-05-23. Manages the aggregate mental overhead of running a complex workspace. Where /briefing and /plan say what to work on, this system diagnoses how much load is present, where threads accumulate, and whether attention is going to the right places.

**Why:** The workspace has grown to 150+ skills and many concurrent concerns (bets, workflows, knowledge, decisions, signals). No skill measured aggregate cognitive burden or compared actual attention against strategic priorities. Operators can feel scattered even when they know their priorities — because the LOAD of unresolved threads across systems is the source of fragmentation, not a missing priority list.

**How to apply:** Session start → `/cognitive-load` (is it safe to do deep work?). When scattered → `/open-loops` (see exactly what's unresolved). Monthly or pre-strategy-review → `/attention-debt` (is attention aligned with strategy?).

## What Was Built

**Architecture doc:** `architecture/COGNITIVE-LOAD-MANAGEMENT.md` — 6 load sources model, load level thresholds (Clear/Moderate/High/Overloaded with scoring), work mode matrix (Deep Focus/Focused Work/Reduction Mode/Maintenance Only), open loop taxonomy (6 categories × staleness thresholds × routing), attention debt model (priority weights by horizon, alignment ratio), load reduction workflow, anti-patterns.

**3 new skills:**

- `/open-loops` — Scans all 6 inbox states: notes/raw/, meeting-intelligence/raw/, strategy/signals/, decisions-log (pending), KNOWLEDGE-GRAPH (unresolved contradictions), active-workflows (GATE/PAUSED). Returns full inventory by category with staleness and routing recommendation. Distinct from /briefing (today's priorities from action-items) and /cognitive-load (aggregate score).

- `/cognitive-load` — Aggregate load scoring. Items = 1pt; stale items = 2pt. Load level from score (Clear 0-8, Moderate 9-20, High 21-40, Overloaded 41+). Maps load level to work mode recommendation. When High/Overloaded: generates 3-step reduction path with time estimates. Distinct from /ops-dashboard (execution health) and /briefing (priorities).

- `/attention-debt` — Strategic attention alignment. Reads active-bets.md (priority signal: H1=weight 3, H2=weight 2, H3=weight 1, At risk +1) and TRACE-INDEX (attention signal). Computes alignment ratio per bet. Flags attention debt (ratio <0.3) and H1 bets with 0 sessions in 14 days as emergencies. Surfaces attention sinks (sessions with no associated bet). Distinct from /exec-allocation (work TYPES) and /exec-throughput (completion rates).

## Load Scoring

6pt/2pt model: items = 1 point, stale items = 2 points.
Clear (<8) → Deep Focus. Moderate (9-20) → Focused Work. High (21-40) → Reduce First. Overloaded (41+) → Maintenance Only.

## Key Distinctions

- `/open-loops` inventory (what's in each box) vs `/cognitive-load` aggregate (total weight of all boxes)
- `/attention-debt` strategic TOPIC alignment vs `/exec-allocation` work TYPE distribution
