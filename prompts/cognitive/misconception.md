# Misconception Detection Prompts
## Version: v1.0

---

## Full Entry Diagnostic

```
Read: [path to knowledge entry]

Run 7 checks:

1. UNIVERSAL CLAIMS — scan for: always, never, in every case, all, every, universally
   Flag: any universal claim without named boundary conditions

2. CAUSAL CLAIMS — scan for: causes, produces, leads to, results in, because
   Flag: any causal claim without a stated mechanism

3. MODEL APPLICATION — identify: any model, framework, heuristic
   Flag: any model applied without stating its validity conditions

4. QUANTITATIVE CLAIMS — scan for: numbers, percentages, ranges, thresholds
   Flag: precision without calibration basis

5. ANALOGIES — scan for: like, similar to, as with, just as, this is the same as
   Flag: analogy used as evidence (not illustration)

6. REVIEWED DATE — check frontmatter reviewed: field
   Flag: >90 days in domains: ai, technical, strategy, product

7. CIRCULAR DEFINITIONS — check ## Definition section
   Flag: definition uses the defined term or synonym

For each finding: [Check #] → [exact flagged text] → [class] → [severity P0|P1|P2]
For P0 findings: draft the corrected version of the specific flagged sentence.
```

---

## Batch Triage (Domain-Level)

```
Read: knowledge/KNOWLEDGE-INDEX.md

Filter entries where:
- confidence: high
AND reviewed date is more than [30 | 60 | 90] days ago

List them in order of oldest reviewed date.

For the top 3 entries:
  Run the universal claims check (Check 1) only.
  Run the reviewed date check (Check 6) only.

Output: prioritized list for full diagnostic. Do not run full diagnostics here — this is triage.
```

---

## Post-Decision Misconception Check

```
A decision was made based on: [entry path]
The outcome was: [what happened]
The outcome contradicts: [what the entry predicted or implied]

Step 1: Identify the specific claim in the entry that led to the incorrect prediction.
Step 2: Classify the failure: 
  Class 1 Overgeneralization | Class 2 Causal Reversal | Class 3 Model Over-application | 
  Class 4 False Precision | Class 5 Confident Analogy | Class 6 Stale Confidence | Class 7 Circular Definition
Step 3: Is this a misconception in the entry, or was the entry correctly applied in the wrong context?
  If misconception in entry → produce corrected claim
  If misapplication → add boundary condition to entry stating when it doesn't apply
Step 4: Are there other decisions or bets that used this entry? List them.
```

---

## Propagation Check

```
A misconception was corrected in: [entry path]
The corrected claim was: [one sentence]

Check whether this misconception has propagated:

1. grep knowledge/ for key terms from the corrected claim — list any other entries that contain similar language
2. grep strategy/ for any reference to the corrected entry
3. grep decision-frameworks/ for any reference to the corrected entry
4. Check strategy/active-bets.md — does any active bet cite this entry or rely on its claim?

For any match found: flag it. State whether the match needs revision or just monitoring.
Output: propagation map with specific file:line references.
```
