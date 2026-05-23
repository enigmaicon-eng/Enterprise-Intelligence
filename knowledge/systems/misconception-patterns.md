---
title: Misconception Patterns
domain: systems
created: 2026-05-22
reviewed: 2026-05-22
tags: [misconceptions, epistemics, knowledge-quality, belief-revision, calibration]
connections: [systems/reasoning-quality.md, systems/learning-science.md, decisions/decision-patterns.md]
confidence: high
source: epistemics literature + operational observation from knowledge base maintenance
---

# Misconception Patterns

## Definition

A misconception is a belief that feels stable and well-grounded but contains a structural flaw: a hidden false premise, an overgeneralization, a model applied outside its validity range, or a causal story that runs backward. Misconceptions are persistent because they generate less error signal than correct beliefs — they're coherent within their local frame.

## Why It Matters

Misconceptions are more dangerous than ignorance. Ignorance creates a visible gap; misconceptions create invisible errors. A knowledge base full of misconceptions actively degrades decision quality by providing confident-sounding but flawed foundations. Regular misconception detection is a quality gate, not an academic exercise.

## Key Misconception Classes

**Class 1: Overgeneralization**
A principle true in domain A applied as if universal. The cross-domain transfer happens without checking whether the relevant structural features hold.

*Example:* "Faster iteration always produces better products" — true in early-stage consumer product, false in safety-critical medical devices.

*Detection signal:* Universal claim ("always," "never," "in every case") without named boundary conditions.

**Class 2: Causal Reversal**
Two things correlate; the causal direction is stated wrong. Often looks like "correlation as proof" but with a stated direction.

*Example:* "High-performing teams communicate more" → stated as "more communication makes high-performing teams." The direction may run the other way.

*Detection signal:* Causal claim derived from observational pattern without intervention evidence.

**Class 3: Model Over-Application**
A model built for one set of conditions applied beyond those conditions. The model isn't wrong — it's being used outside its validity range.

*Example:* RICE scoring applied to early-stage bets where inputs are unknowable. The model is built for relative prioritization of known work, not discovery-phase bet sizing.

*Detection signal:* Model applied in a context where its required inputs can only be fabricated.

**Class 4: False Precision**
Quantitative framing applied to fundamentally qualitative judgment, generating the appearance of rigor without the substance.

*Example:* Scoring stakeholder influence 1-10 and summing to rank engagement priority, when the scores are uncalibrated gut-feel.

*Detection signal:* Numbers without calibration basis; precision that can't be reproduced by a different evaluator.

**Class 5: Confident Analogy Failure**
An analogy from another domain is used as evidence rather than as illustration. The structural features that would make the analogy valid are assumed rather than tested.

*Example:* "This is like how Netflix killed Blockbuster, so incumbents always lose to new entrants." The analogy doesn't transfer without checking whether the specific structural conditions (streaming economics, content rights, consumer switching costs) apply.

*Detection signal:* "It's just like..." or "as X showed..." used to ground a claim, not illustrate it.

**Class 6: Stale-Confidence**
A belief that was accurate when formed but hasn't been reviewed as conditions changed. The confidence remains high; the underlying fact has shifted.

*Example:* A knowledge entry written when Claude Sonnet 3 was the best model, stating Sonnet tier as the default for complex reasoning — now outdated.

*Detection signal:* `reviewed` date >90 days in a rapidly-changing domain.

**Class 7: Circular Definition**
A term defined using itself or its synonyms, creating apparent clarity without actual meaning.

*Example:* "Good decisions are decisions made by good decision-makers."

*Detection signal:* The definition could be cut without loss; the term appears in its own definition.

## Detection Protocol

For any knowledge entry:

1. **Scan for universal claims** — flag anything stated without boundary conditions.
2. **Check causal claims** — state the causal mechanism explicitly. Does the mechanism hold?
3. **Check model application context** — what conditions must hold for this model to be valid? Are those conditions present?
4. **Check quantitative claims** — what's the calibration basis? Can the number be reproduced?
5. **Check analogies** — what structural features must transfer? Do they?
6. **Check reviewed date** — for fast-changing domains, >90 days is suspect.
7. **Check definitions** — does the definition of key terms require the term itself?

## In Practice

Run the detection protocol against any knowledge entry before citing it in a decision, before using it in a synthesis, or as part of the monthly cognitive review.

Flag findings with severity:
- **P0:** Actively used in strategy or execution and contains a Class 1-5 misconception
- **P1:** Exists in knowledge base but not currently load-bearing; needs revision
- **P2:** Stale-confidence only; update reviewed date after verification

Do not delete flagged entries. Annotate with the specific finding. Revise the claim if a correction can be stated confidently; add an explicit uncertainty marker if it cannot.

## Connections

- `systems/reasoning-quality.md`: misconceptions often persist because they pass local coherence checks
- `systems/learning-science.md`: misconceptions generate low error signal, which is why they persist
- `decisions/decision-patterns.md`: Class 3 (model over-application) is the most common source of decision pattern failure

## Open Questions

- Is there a reliable signal that distinguishes a misconception from a legitimate domain-specific claim? The boundary is context-dependent.
- How often should misconception detection be run on high-confidence entries? The highest-confidence entries are the most dangerous if they're wrong.
