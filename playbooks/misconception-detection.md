# Misconception Detection Playbook

## Purpose
A reference guide for diagnosing and correcting misconceptions in the knowledge base. Use when `/misconception` returns findings, when a decision produces unexpected results, or when a belief is challenged and you need a structured investigation.

---

## When to Invoke This Playbook

- `/misconception` returns a P0 or P1 finding
- A bet produces an outcome that contradicts a stated belief in the knowledge base
- A decision based on a knowledge entry produces unexpected results
- An `/arch-critique` surfaces a principle violation that wasn't caught in authoring
- A `/think` stress-test breaks a claim from a knowledge entry

---

## Phase 1: Isolate the Suspect Claim

**Goal:** Identify the single specific claim that is potentially wrong. Not the whole entry — the specific sentence or paragraph.

**Steps:**
1. Read the flagged entry in full.
2. Identify the specific claim under suspicion. Write it as one sentence.
3. Identify the claim type: Empirical / Causal / Normative / Predictive (from `knowledge/systems/reasoning-quality.md`)
4. Identify when the claim was authored and what evidence it was based on.

**Output:** One sentence: the claim under investigation.

---

## Phase 2: Classify the Potential Misconception

Map the suspect claim to a class from `knowledge/systems/misconception-patterns.md`:

| Class | Name | Detection Question |
|---|---|---|
| 1 | Overgeneralization | Does the claim use universal language without boundary conditions? |
| 2 | Causal Reversal | Is the stated causal direction testable? Does it hold under intervention? |
| 3 | Model Over-application | Are the model's validity conditions met in the context where it's applied? |
| 4 | False Precision | Is the quantitative precision reproducible by a different evaluator? |
| 5 | Confident Analogy | Are the structural features that make the analogy valid stated and verified? |
| 6 | Stale Confidence | Has the underlying fact changed since the claim was written? |
| 7 | Circular Definition | Does the definition use the defined term? |

If the suspect claim doesn't map cleanly to a class, it may not be a misconception — it may be an open question. Flag it as "uncertain, not misconception" and proceed.

---

## Phase 3: Gather Counter-Evidence

**Goal:** Determine whether the claim is wrong, underspecified, or valid.

**For empirical claims:**
- What evidence was used to author the claim?
- What evidence would contradict it?
- Is that contradicting evidence available in the knowledge base or from direct observation?

**For causal claims:**
- State the mechanism explicitly.
- Is there an alternative mechanism that would produce the same observation?
- Does the claim hold when the input changes (interventional test)?

**For normative claims:**
- What values or priorities ground the claim?
- Is there a defensible alternative grounding that leads to a different conclusion?

**For predictive claims:**
- What was predicted?
- What actually happened?
- If the prediction was wrong: was it the prediction that was wrong, or the inputs?

**Output:** Evidence assessment — does the counter-evidence exist? Is it strong?

---

## Phase 4: Determine Verdict

Three possible verdicts:

**VALID** — The claim is correct as stated. Counter-evidence is weak or inapplicable. Update `reviewed:` date to today. No change to content.

**UNDERSPECIFIED** — The claim is not wrong, but it's missing boundary conditions. It applies in some contexts but not others. Revise to add the qualifier: "When [conditions], [claim]. When [other conditions], [different behavior]."

**WRONG** — The claim is incorrect. The counter-evidence outweighs the original basis. Replace the claim with the corrected version. Add a brief note about why the original was written (to prevent re-introduction).

---

## Phase 5: Apply Correction

**For UNDERSPECIFIED:**
Replace the universal claim with a bounded version. Use the exact sentence from Phase 1 as `old_string`. Write the bounded replacement with explicit conditions.

**For WRONG:**
Replace the claim with the corrected version. Update the `confidence:` frontmatter field to reflect the revised state. If confidence drops significantly: update the entry's `reviewed:` date and add a note in the `## Open Questions` section naming the specific uncertainty.

**For VALID:**
No content change. Update `reviewed:` date only.

---

## Phase 6: Propagation Check

After correcting a claim, check whether the misconception has propagated:

1. Grep `knowledge/` for the key term in the corrected claim.
2. Grep `strategy/` and `decision-frameworks/` for citations of the corrected entry.
3. For any active bet or decision that was based on the now-corrected claim: flag for re-review via `/bet update` or a note in `decisions-log.md`.

**This step is mandatory for P0 findings.** A corrected knowledge entry that has already been used in an active decision is load-bearing — the decision may need revision.

---

## Correction Anti-Patterns

| Anti-pattern | Risk | Prevention |
|---|---|---|
| Deleting instead of correcting | Loses the reasoning trail; same error can be re-introduced | Always replace content, never delete |
| Correcting without propagation check | Corrected knowledge, but active bets still use old version | Always run Phase 6 for P0 findings |
| Overcorrecting to uncertainty | Converting specific claims to vague hedges | Corrections should be as specific as the original claim |
| Silencing instead of flagging | Marking an entry reviewed without actually reviewing | VALID verdict requires evidence, not just comfort |
