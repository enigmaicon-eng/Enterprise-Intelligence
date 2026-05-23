---
name: pm-ml
description: Structure AI/ML PM work — eval set design, responsible AI review, model card drafting, LLM system prompt specification, and human-in-the-loop design. Converts ambiguous AI features into defined PM artifacts.
version: "1.0"
changed: 2026-05-20
---

# PM AI/ML Feature Specification

**Input:** AI/ML feature name, problem the model is solving, target user behavior change, any known model constraints.

**Output:** Written to `notes/structured/pm-ml-YYYY-MM-DD-<feature-slug>.md`

**Scope:** PM-level AI/ML artifacts — evals, model card, system prompt spec, responsible AI checklist, HITL design. Does not include ML engineering decisions (architecture, training pipeline, hyperparameters).

---

## Steps

1. **Read context.** Load `knowledge/pm/ai-ml-pm.md`. If a PRD or discovery document exists for this feature, read it.

2. **Define the problem statement in ML terms.** What is the input? What is the output? What does correct look like? What does incorrect look like — and which error type (false positive vs. false negative) is more costly to the user?

3. **Design the eval set.** What 20-30 cases will be used to measure model quality before and after each change? Include: representative happy-path cases, edge cases the model is likely to get wrong, adversarial cases (attempts to break the model), and cases that represent the "almost correct" failure mode. Write the ground truth for each.

4. **Write the responsible AI checklist.** Bias/fairness (which groups, which harm), transparency (does the user know AI is involved), privacy (what data is processed, retained, shared), safety/harm (what is the worst case failure and what is the safeguard).

5. **Design the human-in-the-loop pattern.** Which HITL mode is appropriate: human-on-the-loop (AI acts, human reviews after), human-in-the-loop (human approves before action), human-as-the-loop (AI informs, human decides and acts)? State the decision criteria.

6. **If LLM feature: Write the system prompt specification.** System prompt is a PM deliverable, not an engineering afterthought. Define: persona/role, constraints (what the model must not do), output format, context the model needs, and escalation behavior (what to do when it can't answer).

7. **Draft the model card.** PM-level model card for stakeholder communication: what the model does, what it doesn't do, known limitations, known failure modes, fairness considerations, monitoring plan.

---

## Output Format

```markdown
# AI/ML Feature Specification — [Feature Name] — [Date]

**Problem statement:** [What the model must do]
**Input:** [What data goes in]
**Output:** [What the model produces]
**User behavior change:** [What users should do differently as a result]

---

## Error Cost Analysis

| Error type | What it looks like | Cost to user | Cost to product |
|-----------|-------------------|-------------|----------------|
| False positive | [Model says X when X is wrong] | [Impact] | [Impact] |
| False negative | [Model misses X when X is right] | [Impact] | [Impact] |

**Primary error to minimize:** [FP or FN] — [reason this matters more in this context]

---

## Eval Set Design

**Purpose:** These cases define "good" before engineering writes a line of code. Any model change must be evaluated against this set.

**Eval cases:**

| ID | Input | Expected output | Case type | Notes |
|----|-------|----------------|-----------|-------|
| E001 | [Input] | [Expected] | Happy path | |
| E002 | [Input] | [Expected] | Edge case | [What makes this edge] |
| E003 | [Input] | [Expected] | Adversarial | [What the model is being tricked into] |
| E004 | [Input] | [Expected] | Almost-correct failure | [The likely failure mode] |

**Minimum eval set size:** [N cases]

**Evaluation metrics:**
- Primary: [accuracy / F1 / precision / recall / NDCG / other — with rationale]
- Secondary: [metric]
- Guardrail (must not regress): [metric + threshold]

**Baseline:** [Current performance before this feature, or human-level benchmark]

**Target:** [What "good enough to ship" looks like, as a number]

---

## Responsible AI Checklist

### Bias and Fairness

- Which user groups are represented in the training/eval data?
- Which groups may receive worse outputs? [Named — not "all groups equally"]
- How will we test for disparate performance across groups?
- Mitigation plan if disparate impact is found:

### Transparency

- Does the user know AI is producing this output? [Yes/No — if No, justify]
- How is the AI nature disclosed? [Label, tooltip, documentation, terms]
- Can users understand why the AI produced a specific output? [Explainability requirement]

### Privacy

- What user data does this model process?
- Is any user data used for training? [Explicit opt-in required if yes]
- Data retention: how long is inference data stored? Who has access?
- Third-party model APIs: what data leaves our systems?

### Safety and Harm

- Worst-case failure: [If the model is maximally wrong, what happens to the user?]
- Safeguard for worst-case failure: [Technical or UX control that prevents or mitigates]
- Content or output types this model must never produce: [Explicit list]
- Abuse vector: [How a bad actor might exploit this feature — and the defense]

---

## Human-in-the-Loop Design

**Selected HITL pattern:** [Human-on-the-loop / Human-in-the-loop / Human-as-the-loop]

**Rationale:** [Why this pattern — what the error cost and stakes require]

**HITL specification:**

| Scenario | AI action | Human action | Timing |
|---------|-----------|-------------|--------|
| High-confidence output | [AI does X] | [Human reviews at [cadence]] | Post-action |
| Low-confidence output | [AI flags] | [Human approves before action] | Pre-action |
| Out-of-distribution input | [AI declines / escalates] | [Human handles] | At inference |

**Confidence threshold:** [The score below which AI defers to human — must be measurable]

---

## LLM System Prompt Specification

*(Complete this section only if the feature uses an LLM)*

**Persona/role:** [What role the model is playing — constrain the frame]

**Task definition:** [Exactly what the model is asked to do — be precise]

**Constraints (must not):**
- [What the model must never do]
- [Topics, output types, or behaviors that are out of bounds]
- [How to handle requests that violate constraints]

**Output format:** [Exact format — structured JSON, markdown, plain prose, etc. Provide a template if structured]

**Context the model receives:**
- [What user data is included in context]
- [What system state is included]
- [What is NOT passed to the model — by design]

**Escalation behavior:** [What the model should say/do when it can't answer, is uncertain, or detects a violation]

**Latency budget:** [Maximum acceptable response time — this is a product constraint, not an engineering suggestion]

**Context window management:** [What gets summarized, truncated, or dropped as context grows]

---

## Model Card

**What this model does:** [One clear sentence]

**What this model does not do:** [Two or three explicit limitations]

**Known failure modes:**
- [Failure mode 1]: [When it occurs, what the user sees]
- [Failure mode 2]: [When it occurs, what the user sees]

**Known limitations:**
- Training data cutoff: [Date if applicable]
- Languages supported: [List]
- Input types supported: [List]
- Input types that degrade performance: [List]

**Fairness considerations:** [One paragraph — honest assessment, not marketing]

**Monitoring plan:**
- Metrics monitored in production: [List with owners]
- Alert thresholds: [What triggers a review]
- Retraining trigger: [What performance degradation signals that the model needs retraining]

**PM sign-off required before deployment:** [Yes — this model card must be reviewed]

---

## Open Questions for ML Engineering

1. [Question PM genuinely doesn't know the answer to — not a specification gap]
2. [Question]
```

---

## Quality Gate

- Error cost analysis names which error type is costlier and why
- Eval set includes all four case types (happy path, edge, adversarial, almost-correct failure)
- Eval set has stated metric with numeric target and baseline
- Responsible AI checklist addresses all four areas (bias, transparency, privacy, safety)
- HITL pattern selected with stated rationale
- LLM system prompt spec includes constraints, output format, escalation, and latency budget
- Model card written as a communication artifact (not technical doc)
- Model card is honest about failure modes and limitations
