---
name: knowledge-compounding
description: P17 Knowledge Compounding + Retrieval Intelligence System — what was built, design decisions, integration points
metadata:
  type: project
---

# P17 — Knowledge Compounding + Retrieval Intelligence System

Complete 2026-05-22.

## What Was Built

**Architecture:**
- `architecture/KNOWLEDGE-COMPOUNDING-SYSTEM.md` — compounding model, node/edge/cluster schema, 5 compounding mechanisms, integration map
- `architecture/RETRIEVAL-INTELLIGENCE.md` — 7-step retrieval pipeline, 5-component scoring algorithm, spaced repetition schedule, gap signal types

**Knowledge infrastructure:**
- `knowledge/KNOWLEDGE-GRAPH.json` — machine-readable graph (initialized empty; rebuilt by knowledge_index.py)
- `knowledge/COMPOUNDING-LOG.md` — append-only audit trail of all compound events (CONNECTION, SYNTHESIS, ENRICHMENT, REVIEW, PROMOTION, GAP_DETECTED)
- `knowledge/<domain>/` — 8 domain directories: pm, strategy, systems, technical, operations, patterns, decisions, clusters

**Python scripts:**
- `scripts/knowledge_index.py` — scans all domain dirs, extracts frontmatter edges, merges manual edges, rebuilds KNOWLEDGE-GRAPH.json; CLI: --check, --stats, --orphans, --candidates
- `scripts/knowledge_search.py` — 5-component scored retrieval, access tracking (last_accessed, access_count), 1-hop neighbor traversal; CLI: --domain, --type, --stats, --gaps, --no-track
- `scripts/knowledge_review.py` — spaced repetition schedule by (confidence, connection_count); priority scoring; --mark-reviewed; CLI: --domain, --all

**Skills:**
- `/recall` — upgraded to graph-aware; runs knowledge_search.py, traverses neighbors, detects 4 gap types, tracks access
- `/knowledge-connect` — create/discover/view connections; writes edges to graph; logs to COMPOUNDING-LOG.md; detects cluster threshold
- `/knowledge-cluster` — synthesize ≥5 connected entries into knowledge/clusters/; gated; adds synthesizes edges; logs SYNTHESIS event
- `/knowledge-review` — spaced repetition review surface; active recall prompts; confidence update; logs REVIEW event
- `/knowledge-graph` — read-only graph diagnostic: stats, orphans, candidates, gaps, top-connected entries

**Template:**
- `templates/cluster-synthesis.md` — cluster synthesis output template with core claim, shared themes, cross-entry patterns, tensions, synthesized insight, member contributions

## Core Design Decisions

**Retrieval scoring (5 components, fixed weights):**
`keyword_match × 0.45 + confidence × 0.20 + recency × 0.15 + connection_density × 0.10 + tag_match × 0.10`
Keyword dominates so that explicit search intent is always honored. Confidence and recency ensure that well-validated, recently-reviewed entries naturally outrank older uncertain ones. Connection density rewards network effects without overriding relevance.

**Cluster threshold at ≥5 nodes:** Small enough to be reachable, large enough to produce genuine synthesis value. Below 5, individual entries suffice. At 5+, emergent patterns become visible.

**COMPOUNDING-LOG.md is append-only:** Provides an audit trail and momentum signal. Never edit or delete entries.

**knowledge_index.py merges manually-added edges:** Frontmatter-extracted edges are rebuilt on every run. Manual edges (written by /knowledge-connect to the JSON) are preserved during rebuild — they are not overwritten.

**Access tracking on every retrieval:** Every `/recall` query increments access_count and sets last_accessed. This creates a feedback loop: popular entries surface more via recency, making them even more accessible.

## Why

**Why:** Knowledge that isn't networked and reviewed decays in value. Without compounding — connections between entries, clusters that synthesize themes, spaced review — a knowledge base is just a file pile. The compounding mechanisms (connection → cluster → synthesis → insight) are what make individual learning compound into strategic capability.

**How to apply:** Run `/recall` before any synthesis or planning task. Add connections via `/knowledge-connect` whenever two entries are obviously related. When any node reaches 5 connections, synthesize with `/knowledge-cluster`. Review overdue entries weekly with `/knowledge-review` — especially low-confidence ones.

## Links

[[production_ai_learning]] — P9 produced the initial 8 knowledge entries this graph operates on
[[cognitive_acceleration_system]] — P10 error-signal practices feed into knowledge confidence levels
