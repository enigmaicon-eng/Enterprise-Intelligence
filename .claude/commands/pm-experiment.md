---
name: pm-experiment
description: Design an A/B test or controlled experiment. Produces hypothesis, primary metric, guardrail metrics, sample size estimate, duration, and instrumentation checklist.
version: "1.0"
changed: 2026-05-20
---

# PM Experiment

**Input:** Feature or change being tested, hypothesis, target metric, and any known traffic/user volume context.

**Output:** Written to `notes/structured/experiment-YYYY-MM-DD-<slug>.md`

---

## Steps

1. **Read context.** Load `knowledge/pm/metrics-experimentation.md` (experiment design section).

2. **Validate the hypothesis is complete.** Format: "We believe that [change] will cause [behavior change] because [mechanism]." The mechanism is mandatory — it forces a theory, not just a hope. If the mechanism is missing, the experiment design is incomplete.

3. **Define the primary metric.** ONE metric wins or loses the experiment. If more than one metric is proposed as primary, pick the one that most directly measures whether the hypothesis is true. Others become secondary or guardrail.

4. **Define guardrail metrics.** Metrics that must not degrade even if the primary metric improves. At minimum: revenue/conversion (if feature affects funnel), user experience metric (error rate, task completion), and core engagement metric. If primary metric improves but a guardrail degrades, the experiment has failed.

5. **Identify failure modes:**
   - Multiple hypothesis testing: keep to 1 primary metric
   - Novelty effect: plan to measure after novelty period (typically 2-4 weeks)
   - Network effects: do treatment and control users interact? If yes, need cluster randomization
   - Simpson's paradox risk: segment results by key dimensions before concluding

6. **Calculate sample size.** Parameters:
   - Baseline conversion rate (current rate of the primary metric event)
   - Minimum detectable effect (MDE): smallest improvement worth detecting
   - Statistical power: 80% standard
   - Significance level: 95% (α = 0.05) standard
   
   Rough estimate: for binary metrics, n ≈ (16 × p × (1-p)) / δ² per variant, where p = baseline rate and δ = absolute MDE.
   
   State total sample needed, and given traffic, how many days/weeks to reach it.

7. **Set duration before starting.** Duration = time to reach sample size, PLUS novelty buffer if applicable. State: "This experiment runs from [date] to [date]. Results will not be evaluated before [date]." Peeking invalidates the experiment.

8. **Define the rollout plan.** 50/50 split (standard) or graduated (10% treatment for safety check first, then 50/50).

9. **Define the instrumentation checklist.** Every event needed to measure the experiment must be verified before launch.

10. **Define the decision rule.** What outcome triggers: ship / roll back / iterate / run follow-up?

---

## Output Format

```markdown
# Experiment Design — [Feature/Test Name] — [Date]

**Hypothesis:**  
We believe that [change] will cause [behavior change] because [mechanism].

**If wrong, we'd expect:** [Observable signal that would indicate the hypothesis is false]

---

## Metrics

**Primary metric:** [Metric name] — Current baseline: [N%/N]  
**Minimum detectable effect:** [+N% or +N absolute]  
**Direction:** Increase | Decrease (specify which direction = success)

**Guardrail metrics (must not degrade):**
- [Metric] — Current baseline: [N] — Acceptable floor: [N]
- [Metric] — Current baseline: [N] — Acceptable floor: [N]

**Secondary metrics (informational, not decision criteria):**
- [Metric]
- [Metric]

---

## Sample Size and Duration

**Baseline rate:** [N]%  
**MDE:** [N]%  
**Required sample:** [N] users per variant  
**Daily eligible users:** [N]  
**Required duration:** [N] days / [N] weeks  
**Novelty buffer:** [N weeks after initial exposure, if applicable]

**Experiment runs:** [Start date] to [End date]  
**First valid read date:** [Date — no peeking before this]

---

## Rollout Plan

**Phase 1 (safety check):** 5-10% treatment for [N days] — monitor error rates  
**Phase 2 (full experiment):** 50% treatment / 50% control for [N days]

**Randomization unit:** User | Session | [Other — specify for network effect risks]

---

## Failure Mode Checks

- [ ] Single primary metric defined (no multiple hypothesis testing)
- [ ] Novelty period accounted for: [Yes — running N weeks / No — not applicable]
- [ ] Network effects: [Assessed — users in treatment/control do not interact / Cluster randomization needed]
- [ ] Segmentation plan: [Will segment by: segment A, segment B before concluding]

---

## Instrumentation Checklist

- [ ] [Event name] — fires on [trigger] — verified in staging
- [ ] [Event name] — fires on [trigger] — verified in staging
- [ ] Experiment flag assigned and verified
- [ ] Baseline measurement captured and recorded above

---

## Decision Rules

| Outcome | Action |
|---|---|
| Primary metric improves ≥ MDE, all guardrails stable | Ship to 100% |
| Primary metric improves but a guardrail degrades | Do not ship — investigate |
| Primary metric flat or negative | Roll back — run follow-up analysis |
| Insufficient sample reached | Extend duration OR reduce MDE target |

**Decision owner:** [Name]  
**Review meeting date:** [Date — after first valid read date]
```

---

## Quality Gate

- Hypothesis includes a mechanism (not just "we believe X will improve Y")
- ONE primary metric defined
- Guardrail metrics listed and have defined floors
- Sample size calculated from actual baseline data
- Experiment duration set before starting (not adjusted based on interim results)
- "First valid read date" stated (prevents peeking)
- All instrumentation verified in staging before experiment launch
