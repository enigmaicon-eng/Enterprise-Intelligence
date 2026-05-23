---
title: AI Evaluation Workflows
domain: technical
created: 2026-05-22
reviewed: 2026-05-22
tags: [evaluation, evals, LLM-as-judge, rubrics, quality, AI-ops, regression-detection]
connections: [observability, ai-debugging, telemetry, prompt-architecture, ai-systems]
confidence: high
source: original synthesis
---

## Definition
Evaluation (evals) is the systematic practice of measuring whether AI outputs meet defined quality criteria. An eval is a test for AI behavior — not whether code compiles or a function returns the right value, but whether the model's output is useful, correct, and appropriately structured.

Evals are the bridge between "seems to work" and "demonstrably works." They convert subjective quality judgment into measurable, trackable signal.

## Why It Matters
AI quality degrades silently. A prompt that worked well 60 days ago may produce worse outputs today because: the model was updated, the context has grown, the user's needs have evolved, or the skill has drifted from its spec. Without evals, you don't know degradation is happening until a user complains — or worse, until you make a bad decision based on bad output.

Evals also enable confident improvement. Without a baseline, you can't know if a prompt change helped or hurt. With evals, you can run before/after comparisons and make decisions from evidence.

## The Four Evaluation Dimensions

Every AI output in this workspace is assessable on four dimensions. These are binary (pass/fail), not graded — binary ratings produce more actionable signal than 1-5 scales.

**1. Factual Accuracy**
Does the output contain claims that can be verified? Are those claims correct? For knowledge-based outputs (meeting debriefs, synthesis memos), this is the most important dimension.
- Pass: All factual claims are accurate; nothing was hallucinated.
- Fail: At least one claim is factually incorrect or not supported by the source material.

**2. Completeness**
Does the output cover the required scope? For structured outputs (PRDs, execution plans, decision logs), every required section must be present.
- Pass: All required sections/fields are present and substantive.
- Fail: A required section is missing, empty, or contains placeholder text.

**3. Format Compliance**
Does the output match the expected format? For machine-readable outputs (JSON, YAML) this is binary. For human-readable outputs (prose reports), this means the output structure matches the output pattern specified in `architecture/REASONING-STRUCTURE.md`.
- Pass: Output format exactly matches the schema or pattern.
- Fail: Format deviates in a way that would break downstream use or requires manual correction.

**4. Actionability**
Does the output enable the next step? A debrief that lists actions with no owner or date is complete but not actionable. A strategy synthesis that raises implications but draws no conclusions is articulate but not actionable.
- Pass: A reader could act on this output immediately without asking clarifying questions.
- Fail: Output requires clarification, re-work, or interpretation before it can be acted on.

## LLM-as-Judge

LLM-as-judge uses a model to evaluate another model's output. This enables scalable, consistent eval without human review on every call.

**When to use:** High-volume workflows where manual review of every output isn't feasible. Regression detection. Automated quality gating.

**When not to use:** Novel task types where the rubric isn't calibrated yet. High-stakes decisions where human judgment is non-negotiable. Cases where the eval rubric is still evolving.

**Prompt structure for LLM-as-judge:**

```
System: You are a quality evaluator for an operational intelligence workspace.
Evaluate the following output on exactly 4 dimensions.
Return only a JSON object with dimension names as keys and "pass" or "fail" as values,
plus a "reasoning" field with one sentence per dimension explaining your verdict.

Input context: [source material the model was given]
Expected output schema: [the output pattern the model was supposed to follow]
Actual output: [the model's output to evaluate]

Dimensions:
1. factual_accuracy: Are all factual claims supported by the input context?
2. completeness: Are all required sections present and substantive?
3. format_compliance: Does the output match the expected schema?
4. actionability: Could a reader act on this without asking clarifying questions?
```

**Calibration rule:** Before deploying LLM-as-judge, manually rate 10 outputs and compare to the judge's ratings. If agreement is < 80%, the rubric needs more specificity.

## Eval Workflow Protocol

```
Step 1 — Select sample
  For periodic evals: last 5 outputs from the target skill
  For regression testing: 3 "before" outputs + 3 "after" outputs (post-prompt-change)
  For incident investigation: the specific output that triggered the incident

Step 2 — Apply rubric
  Run each output against all 4 dimensions
  Use LLM-as-judge for volume; human review for high-stakes or calibration

Step 3 — Score
  Pass rate = (passes across all dimensions and samples) / (total dimension-sample pairs)
  Threshold: < 80% pass rate = prompt needs revision

Step 4 — Identify failure pattern
  When failures cluster on one dimension: the rubric points to the root cause
  factual_accuracy fails → context was wrong or missing
  completeness fails → prompt doesn't specify all required sections
  format_compliance fails → output schema not enforced
  actionability fails → prompt doesn't require concrete next steps

Step 5 — Act
  Log the result to observability/quality.jsonl
  If pass rate < 80%: revise the prompt; re-eval; confirm improvement
  If pass rate > 80% but trending down: monitor; schedule next eval sooner
```

## Regression Detection

A regression is a quality decline from a prior baseline. Detecting regressions requires:

1. A baseline score (eval from before the change)
2. A comparison score (eval after the change)
3. A significance threshold (a 5% decline is noise; a 20% decline is a regression)

**Regression triggers in this workspace:**
- Prompt file updated (version bump in PROMPT-REGISTRY.md)
- Model ID changed (model retired or upgraded)
- Context changed (CLAUDE.md updated, memory file added)
- Skill command file changed

When any of these happen: run an eval before and after. Don't ship a prompt change without an eval comparison.

## Quality Score Logging

Log every eval result to `observability/quality.jsonl`:

```json
{
  "ts": "2026-05-22T10:00:00Z",
  "prompt": "workflows/meeting-debrief",
  "prompt_version": "v1.2",
  "session_id": "debrief-20260522-abc123",
  "evaluator": "human",
  "factual_accuracy": "pass",
  "completeness": "pass",
  "format_compliance": "fail",
  "actionability": "pass",
  "pass_rate": 0.75,
  "note": "Output format missing action item owner field"
}
```

Rolling 7-day average < 80%: prompt is in regression. Scheduled revision required.

## Key Principles

- **Binary ratings produce more signal than scales.** A 1-5 score for "quality" is ambiguous. "completeness: fail because the action items section is missing" is actionable.
- **Evals require a baseline.** You can't detect regression without knowing where you started. Establish a baseline before changing any prompt.
- **The rubric is the spec.** If the rubric says "actionability: pass requires an owner and date for every action item," the prompt must specify that. The eval reveals whether the prompt does its job.
- **LLM-as-judge is only as good as the rubric.** A vague rubric produces vague judge verdicts. Specificity is what makes evals useful.
- **Eval the eval.** Periodically (quarterly), manually review 10 LLM-as-judge verdicts and check for calibration drift. The judge can degrade too.

## Connections
- [[observability]] — quality scores are the quality signal layer of the observability system
- [[ai-debugging]] — eval failures point directly to failure class (prompt, context, model, infra)
- [[telemetry]] — trace IDs link eval results to the specific API calls that produced them
- [[prompt-architecture]] — prompt compilation decisions are the primary lever for improving eval results

## Open Questions
- What's the minimum sample size for an eval to be statistically meaningful at this workflow volume?
- Should LLM-as-judge results be cross-checked against human ratings monthly, or can the judge be trusted once calibrated?
