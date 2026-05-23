---
title: Decision Patterns — Recurring Decision Structures and Heuristics
domain: decisions
created: 2026-05-21
reviewed: 2026-05-21
tags: [decisions, heuristics, patterns, judgment, strategy]
connections: [mental-models, bets-history, execution-intelligence]
confidence: medium
source: original synthesis
---

## Definition
Decision patterns are generalizable heuristics extracted from specific past decisions — the distilled judgment of previous choices, made available to future decisions so they don't start from zero. Unlike mental models (which are general reasoning frameworks), decision patterns are specific to recurring decision types observed in this workspace.

## Why It Matters
Without explicit decision patterns, the same reasoning has to be redone each time a similar situation arises. With them, decision quality compounds — each new instance of a pattern is informed by previous instances, their outcomes, and the specific ways the pattern has been applied well or poorly.

## How Patterns Are Added

Decision patterns are extracted from two sources:
1. **Bet postmortems** (`/bet postmortem`) — patterns extracted from strategic bet closures
2. **Decision retrospectives** (`knowledge/decisions/decision-retrospective.md`) — patterns extracted from periodic decision quality reviews

Each pattern follows the format from `templates/pattern-entry.md`.

---

## Active Decision Patterns

*(Patterns are added here as bets close and decisions are reviewed.)*

---

## Candidate Patterns

*(Weak signals — seen once or twice but not yet confirmed. Upgrade to Active when confirmed.)*

### Candidate: Kill Condition Specificity
**Observation**: Bets with specific, observable kill conditions ("if metric X doesn't reach Y by Z") close cleanly. Bets with vague kill conditions ("if results disappoint") stay open indefinitely.
**Status**: Candidate — seen in planning, not yet confirmed from closed bets.
**Potential pattern**: Kill conditions require a metric, a threshold, and a date — all three — to be effective.

### Candidate: Assumption Front-Loading
**Observation**: Plans that name load-bearing assumptions at creation time have more useful checkpoints than plans that don't. The act of naming the assumption makes it observable.
**Status**: Candidate — plausible from planning experience, not yet confirmed from multiple instances.

### Candidate: Disconfirmation Blindness
**Observation**: Reviews that don't explicitly ask "what evidence against the thesis arrived this period?" tend to produce only confirming evidence — not because disconfirming evidence doesn't exist, but because it isn't looked for.
**Status**: Candidate — consistent with cognitive bias literature; workspace confirmation pending.

---

## Pattern Extraction Protocol

When a bet closes or a decision is reviewed, the pattern extractor asks:
1. What recurring decision structure did this instance reveal?
2. Would a different decision in the same situation look the same?
3. What is the actionable heuristic — the specific different behavior next time?

If all three questions can be answered, a new pattern entry is warranted.

## Connections
- [[mental-models]] — mental models are general frameworks; decision patterns are specific to recurring decision types
- [[bets-history]] — bet postmortems are the primary source of extracted patterns
- [[execution-intelligence]] — execution decisions generate patterns through checkpoint and review retrospectives

## Open Questions
- At what point does a "candidate" pattern have enough instances to become "active"? Is 2 instances enough, or does it require 3+?
- Should decision patterns be organized by domain (strategic / operational / product) or by type (reversibility / ambiguity / commitment)?

## Referenced By
<!-- Populated as other notes link to this one -->
