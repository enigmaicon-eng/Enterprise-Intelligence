# /misconception — Knowledge Base Misconception Diagnosis

## Purpose
Run a structured internal consistency check on knowledge entries to surface overconfident claims, logical gaps, stale content, and structural flaws. Operates against the live knowledge base. Not a tutoring exercise — a diagnostic.

## Trigger Signals
- User invokes `/misconception`
- User invokes `/misconception [file path or domain]`
- As part of monthly cognitive review (playbooks/cognitive-review.md)

## Input
- No argument: check the 5 most recently written or most confidently tagged entries in `knowledge/`
- File path: check a specific knowledge entry
- Domain name: check all entries in `knowledge/<domain>/`

## Execution Protocol

**Step 1: Load target entries**
Read the specified file(s). If no argument, read `knowledge/KNOWLEDGE-INDEX.md` to identify entries with `confidence: high` and `reviewed` dates >30 days ago — these are the highest-risk entries.

**Step 2: Run the 7-check diagnostic on each entry**

For each knowledge entry:

**Check 1: Universal Claims**
Scan for: "always," "never," "in every case," "all," "every," "universally."
Flag: any universal claim that lacks named boundary conditions.

**Check 2: Causal Claims**
Scan for: "causes," "produces," "leads to," "results in," "because."
Flag: any causal claim without a stated mechanism. Correlation stated as causation.

**Check 3: Model Application Context**
Identify: any model, framework, or heuristic described.
Flag: any model applied without stating its validity conditions.

**Check 4: Quantitative Claims**
Scan for: numbers, percentages, ranges, thresholds.
Flag: any number without a calibration basis — particularly numbers that are too precise (3 decimal places on a judgment call) or too round (exactly 80% on an empirical claim).

**Check 5: Analogies**
Scan for: "like," "similar to," "as with," "just as," "this is the same as."
Flag: any analogy used as evidence rather than illustration.

**Check 6: Reviewed Date**
Check: `reviewed:` frontmatter field against today's date (2026-05-22).
Flag: any entry with reviewed date >90 days in domains tagged: ai, technical, strategy, product.

**Check 7: Circular Definitions**
Check: the `## Definition` section of each entry.
Flag: any definition that uses the defined term (or its synonym) in its own definition.

**Step 3: Score severity**
- **P0:** Claim is currently load-bearing in active work (bets, execution plans, decisions-log entries) and contains a structural flaw. Requires immediate correction before next use.
- **P1:** Claim exists in knowledge base, not currently load-bearing, contains structural flaw. Fix before next recall.
- **P2:** Stale confidence only. Verify and update reviewed date; no structural flaw.
- **PASS:** No findings.

**Step 4: Output diagnostic report**

Format:
```
MISCONCEPTION DIAGNOSTIC — [date]
Files checked: [list]

[ENTRY: filename]
  Status: P0 | P1 | P2 | PASS
  Findings:
    - [Check #]: [specific finding] → [exact text flagged]
  Recommended action: [correct claim | add boundary condition | verify and re-date | no action]

[repeat per entry]

SUMMARY:
  P0 findings: [count]
  P1 findings: [count]
  P2 findings: [count]
  Total entries checked: [count]
```

**Step 5: For P0 findings — draft correction**
If a P0 finding is identified, draft the corrected version of the flagged claim. Do not rewrite the whole entry — replace only the specific flawed sentence or paragraph. Present the original and the correction side-by-side for user review.

## Constraints
- Do not speculate about intent. Report only what is present in the text.
- Do not flag things as misconceptions because they're uncertain — flag them only when a specific structural flaw is identifiable.
- Do not rewrite entries without user instruction. Surface findings; let the user decide whether to revise.
- One file at a time for deep checks. Use broad scan only for date-based triage.
