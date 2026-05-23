# Socratic Stress-Test Prompts
## Version: v1.0

---

## Constraint-Based Challenge (Empirical Claim)

```
CLAIM TO TEST: [paste the claim]

Constraint: Defend this claim using only evidence from [specific file or source].
No analogies. No appeals to general principle. No external examples.

What specifically remains when all borrowed support is removed?
What had to be removed?
Everything removed was borrowed confidence, not evidence.
```

---

## Mechanism Demand (Causal Claim)

```
CLAIM TO TEST: [paste the causal claim]

State the mechanism. Not "[A] causes [B]" — the specific process by which A produces B.
Name each step in the causal chain.

Then: what would interrupt that mechanism without changing A?
If you can name an interruption, the causal claim is weaker than stated.
If you cannot name an interruption, the mechanism is underspecified.
```

---

## Value Assumption Exposure (Normative Claim)

```
CLAIM TO TEST: [paste the normative recommendation or "should" statement]

Name the assumption about value or priority that grounds this claim.
Be explicit: "This claim assumes that [X] matters more than [Y]."

Now: defend the claim to someone who prioritizes [Y] over [X].
Does the recommendation survive? If not, the claim is conditional, not universal — state the condition.
```

---

## Falsifiability Test (Predictive Claim)

```
CLAIM TO TEST: [paste the prediction]

State two observations:
1. What specific evidence, visible in the next [30 / 90 / 180 days], would confirm this prediction?
2. What specific evidence, visible in the same period, would refute it?

If you cannot name (2), the prediction is unfalsifiable. Unfalsifiable predictions are decorative.
They cannot be updated; they cannot be wrong; they cannot be learned from.
```

---

## Inversion (Any Claim)

```
CLAIM TO TEST: [paste the claim]

Apply inversion: what would have to be true for the opposite of this claim to be correct?

Name the conditions, evidence, or assumptions that would make the opposite true.

If you cannot name any: the claim is unfalsifiable (see falsifiability prompt).
If you can name conditions: how confident are you that those conditions don't hold?
That confidence gap is the real uncertainty in your original claim.
```

---

## Analogy Validity Check

```
ANALOGY TO TEST: [paste the analogy or cross-domain claim]

State the structural features that must transfer from the source domain to the target domain for this analogy to be valid.

For each feature: does it actually hold in the target domain?
Mark each: [Holds | Doesn't hold | Unknown]

If any required feature doesn't hold: the analogy illustrates but does not prove.
If marked Unknown: the analogy is borrowed confidence pending investigation.
```
