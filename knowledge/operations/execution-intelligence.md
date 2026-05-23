---
title: Execution Intelligence — What Works in Execution
domain: operations
created: 2026-05-21
reviewed: 2026-05-21
tags: [execution, delivery, decomposition, planning, reviews, prioritization]
connections: [work-patterns, friction-points, mental-models, decision-patterns]
confidence: medium
source: original synthesis
---

## Definition
Execution intelligence is accumulated knowledge about how to take ambiguous intent and deliver verifiable outcomes reliably — through decomposition, explicit criteria, structured reviews, and checkpoints that produce decisions rather than narratives. It is the operational complement to strategic intelligence.

## Why It Matters
Most execution failures aren't resource failures or motivation failures — they're clarity failures. Work starts with ambiguous goals, unclear done conditions, and undeclared assumptions. When reality diverges from plan, there's no mechanism to detect the divergence until it's expensive to correct. Execution intelligence builds the detection and correction mechanisms in before they're needed.

## Key Principles

- **Decompose until ownership is unambiguous.** A task is too large if two people could both claim to own it, or if "done" requires discussion to assess.
- **Define done before starting.** A done condition written before work starts is far more useful than one written after, because after-the-fact criteria tend to match what was actually delivered.
- **Reviews answer "what changes?" not "how are we doing?"** A review that ends without a change decision was either premature or the criteria were wrong.
- **Checkpoints are gates, not ceremonies.** The checkpoint output is Continue, Pivot, or Stop — not "good progress, keep it up."
- **Risk is tracked to force decisions, not to document awareness.** A risk with no owner and no trigger condition is risk theater.

## Confirmed Execution Patterns

### The Decomposition Test
A task passes the decomposition test if and only if:
1. It starts with an action verb
2. One person can own it entirely
3. "Done" can be assessed by someone who wasn't working on it
4. It's completable in under 4 hours

Tasks that fail this test are projects masquerading as tasks.

### The Criteria-First Protocol
Before reviewing any deliverable: write the pass criteria. If you can't write them, you don't have enough clarity to review. The act of writing criteria before reviewing is as valuable as the review itself — it surfaces criteria ambiguity that would have caused the deliverable to be built to the wrong spec.

### The Assumption Register
Every execution plan contains load-bearing assumptions — things that must be true for the plan to work. Name them explicitly. Each is a checkpoint trigger: when an assumption is invalidated, run a checkpoint immediately.

### The Leverage Test for Prioritization
When two items compete for priority and commitment level is equal: does completing item A enable other work to proceed? If yes, A ranks higher — not because A is more important, but because completing A has compound value that completing B doesn't.

## Failure Modes
- **Zombie initiatives**: work in `active-initiatives.md` for 60+ days with no movement. Not cancelled, not progressed. Force a checkpoint decision — the cost of ambiguity accumulates.
- **Infinite refinement loop**: 4+ review cycles on a deliverable where criteria were never explicitly stated. The fix is always the same: write the criteria, then review once.
- **Delivery without learning**: completing milestones without a checkpoint means delivery happened but improvement didn't. The checkpoint is the mechanism for learning from execution, not just finishing it.
- **Risk inventory vs. risk management**: a risk register with 20 items where none have owners or trigger conditions. Risk entries without these are documentation, not management.

## Connections
- [[work-patterns]] — operational habits that support execution discipline
- [[friction-points]] — where execution discipline breaks down in practice
- [[mental-models]] — the reversibility filter and second-order thinking apply directly to execution planning
- [[decision-patterns]] — execution checkpoints are a class of decision

## Open Questions
- Is there a reliable heuristic for when to checkpoint vs. when to just continue (avoiding premature checkpoints that produce noise)?
- What is the minimum viable decomposition — the point at which further decomposition creates more overhead than clarity?

## Referenced By
<!-- Populated as other notes link to this one -->
