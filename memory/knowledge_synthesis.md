---
name: knowledge-synthesis
description: P25 Knowledge Synthesis Engine — 3 skills adding analogical reasoning, contradiction management, and proactive gap analysis to the knowledge system
metadata:
  type: project
---

# Knowledge Synthesis Engine (P25)

Built 2026-05-23. Extends the existing knowledge compounding system (P17–P18) with higher-order synthesis capabilities.

**Why:** The existing system handles capture, retrieval, and graph connections. It does not: find structural analogies across domains, manage contradictions explicitly, or proactively surface where the knowledge base is thin or synthesis-ready. These three gaps limit the compounding potential of a large, well-connected knowledge base.

**How to apply:** When stuck on a problem → `/analogy`. When the graph feels inconsistent or contradictions accumulate → `/contradiction-register`. Before a learning sprint or monthly review → `/knowledge-gap`.

## What Was Built

**Architecture doc:** `architecture/KNOWLEDGE-SYNTHESIS-ENGINE.md` — Capability distinctions, analogical reasoning model (5-step structural process), contradiction resolution framework (5 types), knowledge gap taxonomy (7 types), anti-patterns

**3 new skills:**
- `/analogy` — Structural pattern matching (not keyword retrieval). Parses problem → extracts abstract structure → searches all domains for structural kin → maps analogies explicitly (source element ↔ problem element) → flags analogy breakdown points. Reads KNOWLEDGE-INDEX.md + up to 7 entry files.
- `/contradiction-register` — Reads KNOWLEDGE-GRAPH.json for `contradicts` edges. Loads both entry files per contradiction. Classifies by 5 types (direct reversal / domain-specific / scope difference / conditional / productive tension). Tracks resolution status. Productive tensions NOT resolved — flagged as synthesis candidates.
- `/knowledge-gap` — Reads KNOWLEDGE-INDEX.md + KNOWLEDGE-GRAPH.json. Surfaces 7 gap types: sparse domain, orphaned entry, stale entry, connection gap, synthesis gap, never-synthesized domain, aging cluster. Prioritized register with specific next-action skill. `--synthesis` flag for synthesis opportunities only. Requires >10 entries.

## Existing Skills (Not Duplicated)

| Skill | Covers |
|-------|--------|
| `/recall` | Keyword + graph-scored retrieval |
| `/synthesize` | Deep cross-domain synthesis memo |
| `/knowledge-connect` | Edge creation; `--discover` mode |
| `/knowledge-cluster` | Cluster synthesis (5+ connected entries) |
| `/knowledge-review` | Single-entry quality + freshness review |

## Gap Taxonomy (7 Types)

Sparse domain / Orphaned entry / Stale entry / Connection gap / Synthesis gap / Never-synthesized domain / Aging cluster

## Anti-Patterns

- Using /analogy for known-topic retrieval (use /recall)
- Force-resolving productive tensions (the tension IS the insight)
- Running /knowledge-gap before >10 entries (produces noise)
- Treating gap register as a to-do queue (gaps are priorities, not tasks)
