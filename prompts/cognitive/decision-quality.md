# Decision Quality Prompts
## Version: v1.0

---

## Decision Quality Review (Single Decision)

```
Read: decision-frameworks/decisions-log.md
Target: [decision ID or date]

Apply 4 quality checks:

CHECK 1 — REASONING STRUCTURE
  Were assumptions stated explicitly or implicit?
  Is the causal logic present (A → B because mechanism) or conclusion-first?
  Were alternatives genuinely considered or was one option the obvious default?
  Verdict: Good | Mixed | Weak

CHECK 2 — PREDICTION CALIBRATION
  Was a prediction embedded in this decision? State it.
  Was it falsifiable at the time it was made?
  Outcome vs. prediction: how far off?
  Confidence appropriate given evidence available at decision time? Yes | No
  Verdict: Well-calibrated | Overconfident | Underconfident | No prediction stated

CHECK 3 — INFORMATION USAGE
  What was the relevant knowledge base at decision time?
  Was it consulted? (grep knowledge/ for relevant terms)
  What available information was not weighted?
  Verdict: Complete | Partial | Significant gaps

CHECK 4 — DECISION PACING
  Was this reversible or irreversible?
  Was appropriate time spent given reversibility?
  Reversible + slow = inefficiency. Irreversible + fast = fragility.
  Verdict: Appropriately paced | Too slow | Too fast

JUDGMENT RULE: "When [conditions], [rule]. Evidence: this decision."
Check rule against knowledge/decisions/decision-patterns.md.
```

---

## Batch Decision Pattern Extraction

```
Read: decision-frameworks/decisions-log.md — last 30 days of entries.

For the set as a whole:
1. What is the most common reasoning failure across these decisions?
2. What is the most common information gap?
3. Is there a domain (strategy / execution / technical / people) where decisions are consistently weaker?

Extract the top pattern: "In decisions about [domain], the consistent weakness is [pattern]."
Check against knowledge/decisions/decision-patterns.md.
If new: draft the pattern entry.
```

---

## Bet Kill Condition Audit

```
Read: strategy/active-bets.md

For each active bet:
1. Is a kill condition present? Yes | No
2. Is the kill condition specific (metric + threshold + date)? Yes | Partially | No
3. Has the kill condition date passed? Yes | No
4. Has evidence arrived that would trigger the kill condition? Yes | No | Unclear

For any bet where kill condition is missing or not specific:
  State the minimum viable kill condition: "[metric] falls below/reaches [threshold] by [date]."

For any bet where kill condition date has passed without review:
  Flag as overdue review.

Output: compliance table + specific fixes for non-compliant bets.
```

---

## Outcome-to-Learning Extraction

```
A decision or bet closed with outcome: [describe outcome]

Step 1: What was predicted when the decision was made?
Step 2: What actually happened?
Step 3: What was the gap between prediction and outcome?
Step 4: Was the gap due to:
  A) Wrong assumption in the reasoning (specify which assumption)
  B) Missing information that was knowable at the time
  C) Missing information that was unknowable at the time
  D) Right reasoning, low-probability outcome (luck / variance)

Step 5: For A or B: what decision rule would have prevented the error?
Format: "When [conditions], [rule]. Evidence: this outcome."

Step 6: For C or D: the decision was not a failure — do not extract a rule from variance.
Note: "Outcome was variance, not decision error. No rule extracted."
```
