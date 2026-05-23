---
name: knowledge-qa
description: P18 Knowledge Validation + Quality Assurance System — what was built, design decisions, integration with P17
metadata:
  type: project
---

# P18 — Knowledge Validation + Quality Assurance System

Complete 2026-05-22.

## What Was Built

**Architecture:**
- `architecture/KNOWLEDGE-QA-SYSTEM.md` — 5 quality dimensions, 0–90 scoring model, calibration flag taxonomy (HIGH_NO_CORROBORATION, HIGH_STALE, LOW_MATURE, CONFIDENCE_MISSING), graph integrity flags (DEAD_LINK, ASYMMETRIC_CONTRADICTION), score bands, validation pipeline, anti-patterns

**Python scripts:**
- `scripts/knowledge_validate.py` — per-entry validation; structural completeness (0–40), retrieval readiness (0–30), content richness (0–20), calibration flags, graph integrity; CLI: node_id, --domain, --all, --stale, --uncalibrated, --dead-links
- `scripts/knowledge_qa_report.py` — aggregate QA: domain coverage, band distribution, calibration summary, dead link detection, missed connection candidates (≥3 shared tags, no edge), confidence promotion candidates; CLI: --domain, --coverage, --missed, --promotions, --json

**Skills:**
- `/knowledge-validate` — validate one entry or domain; presents score + flags; operator-gated frontmatter fixes; logs ENRICHMENT events; rebuilds index after changes
- `/knowledge-qa` — aggregate QA report; priority routing table (dead links → critical entries → stale confidence → thin domains → missed connections); routes to specialist skills for remediation

## Core Design Decisions

**Score is 0–90, not 0–100:** The theoretical max (perfect frontmatter + connected + recently reviewed + rich content) isn't 100 — it reflects genuine uncertainty about whether any entry can be fully "complete." Keeps the band thresholds realistic (Strong = 80+, not 90+).

**Calibration flags separate from score:** Confidence calibration is an epistemic issue, not a structural one. A well-tagged, well-connected entry with HIGH_STALE calibration should still score well structurally — but the flag ensures the epistemic problem surfaces separately.

**Missed connection detection by tag overlap (≥3 tags), not content similarity:** Content-based similarity requires LLM reasoning. Tag overlap is deterministic, fast, and accurate enough to surface genuine candidates for human review. False positives are common — the operator decides.

**Dead links are highest priority:** They cause silent retrieval failures in neighbor traversal. No other quality issue has the same immediate impact on system behavior.

**Promotion candidates by usage, not assertion:** Confidence upgrades are earned through evidence: access count + connections + compound events. Entries that have been used and connected are more trustworthy than entries that were marked high confidence at creation.

## Why

**Why:** Compounding knowledge without quality controls creates a graph where high-confidence connections between poorly-sourced entries amplify misinformation instead of insight. The QA system ensures that as the graph grows, signal quality scales with size rather than degrading.

**How to apply:**
- Run `/knowledge-qa` monthly alongside `/knowledge-review`
- Run `/knowledge-validate --dead-links` after any manual graph edits
- Run `/knowledge-qa --coverage` before any `/learn` session to direct capture toward thin domains
- Treat calibration flags as epistemic debt; clear them before relying on flagged entries in high-stakes decisions

## Links

[[knowledge_compounding]] — P17 builds the graph this system validates
[[production_ai_learning]] — P9 produced the 18 initial knowledge entries that P18 now scores
