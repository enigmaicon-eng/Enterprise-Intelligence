---
name: personal-learning-analytics
description: P26 Personal Learning Analytics System — 3 skills tracking acquisition velocity, source attribution, and knowledge utilization funnel
metadata:
  type: project
---

# Personal Learning Analytics System (P26)

Built 2026-05-23. Analytics layer on top of the knowledge compounding system (P17). Surfaces the metrics the compounding system captures data for but never reports: learning rate over time, source quality, and knowledge conversion.

**Why:** The existing system handles capture (P17), quality (P18), gaps (P25), and synthesis. None of these answer: Am I learning faster or slower? Which sources are most valuable? What fraction of captured knowledge is actually compounding? Without these analytics, the operator has no feedback loop on the learning system itself.

**How to apply:** Monthly → `/learning-velocity` (acquisition trends) + `/knowledge-utilization` (conversion funnel). Quarterly → `/learning-source` (source ROI). Before /knowledge-cluster session → `/knowledge-utilization --dormant` to surface entries needing connection work first.

## What Was Built

**Architecture doc:** `architecture/PERSONAL-LEARNING-ANALYTICS.md` — Coverage map, capability distinctions, learning velocity model, source attribution model, utilization funnel, anti-patterns

**3 new skills:**
- `/learning-velocity` — Time-series acquisition rate by domain. Momentum classification: Accelerating/Steady/Decelerating/Stalled/New/Dormant. Reads KNOWLEDGE-INDEX.md. Flags domains with no new entries in >90 days.
- `/learning-source` — Source attribution: entry yield, connection rate, synthesis reach per source and source type. Reads KNOWLEDGE-INDEX.md + entry frontmatter + KNOWLEDGE-GRAPH.json + synthesis/cluster files. Requires ≥15 entries across ≥3 sources.
- `/knowledge-utilization` — Conversion funnel: Stage 1 (captured) → Stage 2 (connected ≥1 edge) → Stage 3 (synthesized). Surfaces dormant entries (permanent, unconnected, unsynthesized, ≥60 days). Utilization rate benchmark: <30% = accumulating, 30–60% = healthy, >60% = strong. `--dormant` flag for dormant-only view.

## Existing Skills (Not Duplicated)

| Skill | Covers |
|-------|--------|
| `/knowledge-qa` | Quality scoring per entry |
| `/knowledge-gap` | Gap taxonomy, next actions (what to do) |
| `/retrieval-diag` | Recall readiness tier |
| `/recall-test` | Active recall testing of a specific entry |

## Key Metric Definitions

- **Connection rate** = % of entries with ≥1 edge in KNOWLEDGE-GRAPH.json
- **Synthesis reach** = % of entries appearing in any cluster or synthesis memo
- **Utilization rate** = connected entries ÷ total permanent entries
- **Dormant entry** = permanent, 0 edges, unsynthesized, ≥60 days old

## Anti-Patterns

- Optimizing for entry count (velocity) over connection rate (utilization)
- Running /learning-source on <15 entries
- Treating dormant entries as failures (they're connection opportunities)
- Checking analytics more than monthly
