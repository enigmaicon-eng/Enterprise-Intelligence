---
name: decision-intelligence
description: P23 Decision Intelligence System — 4 skills covering the pre-decision lifecycle
metadata:
  type: project
---

# Decision Intelligence System (P23)

Built 2026-05-23. Extends the existing `/decide` + `/decision-review` pair with pre-decision analysis, pattern recall, review queue management, and consequence mapping.

**Why:** Decisions were being logged but not analyzed before they were made. The reasoning quality at decision time determines what judgment rules can be extracted later. Better in → better out.

**How to apply:** For significant irreversible decisions: run `/decision-recall` → `/pre-decide` → `/consequence-map` → `/decide`. Weekly: run `/decision-due` to surface overdue reviews. Monthly: run `/decision-review` to extract judgment rules.

## What Was Built

**Architecture doc:** `architecture/DECISION-INTELLIGENCE-SYSTEM.md`

**4 new skills:**
- `/pre-decide` — generates option set, applies bias check (7 types × 2-3 biases), checks past decisions, runs pre-mortem
- `/decision-recall` — relevance-scored retrieval of past decisions + judgment rules before deciding
- `/decision-due` — surfaces decisions by urgency tier (overdue/due soon/upcoming), sorted by reversibility
- `/consequence-map` — maps first/second-order consequences with reversibility classification, identifies highest-risk chain

## Existing Skills (Not Duplicated)

| Skill | Covers |
|-------|--------|
| `/decide` | Logging with options/rationale/assumptions/reversibility/review_date |
| `/decision-review` | 5-check quality retrospective, judgment rule extraction |
| `/think` | Single-claim stress-test (adversarial, not generative) |

## Data Sources

- `decision-frameworks/decisions-log.md` — read by all 4 new skills
- `knowledge/decisions/decision-patterns.md` — read by /pre-decide + /decision-recall

## Pre-Decision Workflow

Significant irreversible decisions:
1. `/decision-recall` → 2. `/pre-decide` → 3. `/consequence-map` → 4. `/decide`

Reversible low-stakes decisions: skip to `/decide` directly.

## Scope

Single-operator, conversational. No automated decision tracking. No approval workflows. No ML recommendations.
