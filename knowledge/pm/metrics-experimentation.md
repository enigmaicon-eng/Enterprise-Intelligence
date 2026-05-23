---
title: Metrics and Experimentation
domain: technical
created: 2026-05-20
reviewed: 2026-05-20
connections: [PM-OS, discovery-intelligence, product-strategy]
confidence: high
source: original synthesis
tags: [pm, metrics, experimentation, north-star, instrumentation, ab-testing]
---

## Definition

Metrics are not measurements — they are hypotheses about what drives value. Experimentation is not A/B testing — it is the discipline of learning from controlled change. Both are only as valuable as the theory they're testing.

The PM who treats metrics as reporting is doing retrospective analysis. The PM who treats metrics as forward-looking hypotheses is building a learning organization.

## The North Star Problem

Most PM teams pick a north star metric and then discover its failure modes too late.

**North star failure modes:**

*Gaming:* Any metric that becomes a target becomes easier to game than to improve authentically. Engagement metrics incentivize dark patterns. MAU incentivizes notification spam. Revenue incentivizes upsells over value.

*Proxy drift:* The metric was a proxy for the thing that mattered, but over time the proxy and the thing drifted apart. Clicks were a proxy for engagement but stopped predicting retention. Find the metric that still correlates.

*Horizon mismatch:* The north star metric shows results in 90 days, but the most important strategic bets pay off in 24 months. A north star that only captures short-term effects biases the roadmap toward short-term work.

**The north star standard:** A well-chosen north star metric has three properties:
1. It reflects genuine customer value, not just business value
2. It leads the business metrics (retention, revenue) rather than lagging them
3. It degrades under gaming — it gets harder to improve, not easier, when you try to inflate it without real value

## Instrumentation as a PM Responsibility

The PM who waits for the data team to instrument a new feature for them is giving up months of learning time.

**What to instrument (and when):**
- Before launch: all events needed to measure the feature's success hypothesis
- At launch: cohort markers, experiment flags, funnel entry/exit points
- After launch: secondary effects, downstream impacts, unintended behaviors

**The instrumentation brief:** Before any feature ships, document:
- What user behaviors are we trying to change?
- What events will tell us those behaviors changed?
- What's the baseline we're measuring against?
- What's the minimum detectable effect size we care about?
- How many weeks of data do we need to be confident?

**The instrumentation debt trap:** Shipping features without instrumentation creates measurement debt. You can analyze the feature, but you can't diagnose it — you know it's working or not, but not why. Instrumentation debt compounds: later you want to build on this feature but don't understand its mechanics.

## Experiment Design for PMs

**Before running an experiment:**

1. **State the hypothesis explicitly:** "We believe that [change] will cause [behavior change] because [mechanism]." The mechanism is crucial — it forces you to have a theory, not just a hope.

2. **Define the primary metric:** One metric wins or loses the experiment. If you define 10 success metrics, every experiment will succeed on at least one.

3. **Define guardrail metrics:** Metrics that must not degrade. These are your "do no harm" conditions. If the primary metric improves but a guardrail degrades, the experiment has failed.

4. **Calculate the required sample size:** Don't start an experiment you don't have the power to conclude. An experiment with insufficient sample size produces noise you'll misinterpret as signal.

5. **Set the duration before you start:** Running an experiment until it produces a result you like is p-hacking. Set the duration based on the sample size calculation, not the result.

**Common experiment failure modes:**

*Multiple hypothesis testing:* You ran 20 metrics and celebrated that 3 were significant. At 5% significance level, 1 would be significant by chance. Adjust for multiple comparisons.

*Novelty effect:* Users behave differently with new features because they're new. Measure behavior after the novelty period has passed (typically 2-4 weeks).

*Network effects in the treatment group:* If users interact with each other, assigning them randomly to control/treatment mixes the treatment effect. Cluster randomization or holdout groups are needed.

*Simpson's paradox:* An aggregate metric improves while every subgroup metric degrades (or vice versa), because the composition of the test group changed. Always segment your results.

## The Metrics Stack

Organize metrics in layers. Each layer answers a different question.

**Layer 1 — North star:** Are we delivering value to users at scale? (Monthly, quarterly view)

**Layer 2 — Product health:** Is the product working well on the dimensions that drive the north star? (Weekly view)
- Acquisition: where do users come from and at what quality?
- Activation: do new users reach the first moment of value?
- Engagement: are active users getting recurring value?
- Retention: are users coming back?
- Monetization: is value converting to revenue?

**Layer 3 — Feature-level:** Is this specific investment doing what we expected? (Sprint-level view)
- Feature adoption
- Workflow completion rates
- Feature-specific error rates
- Time-to-value on the feature's specific job

**Layer 4 — Operational:** Are we running a healthy system? (Daily view)
- Error rates, latency, uptime
- Support ticket volume by category
- Data pipeline health

**Common anti-pattern:** Reporting Layer 4 metrics to executives (system health) as if they answer Layer 1 questions (value delivery). Executives don't need to know the p99 latency — they need to know if the product is delivering strategic outcomes.

## Decision Frameworks for Metric Ambiguity

**When the metrics disagree:** If engagement is up but retention is down, dig into the mechanism. More engagement that doesn't convert to retention usually means engagement with low-value features. Find the engagement that predicts retention — that's your real engagement metric.

**When metrics are flat:** Flat metrics are not good news. They mean either the initiative had no effect (expected by the 70% failure rate of product features), or the effect is too small to detect given your sample size, or the instrumentation is broken. Investigate all three before concluding "it worked."

**When you don't have enough data:** Don't make the number up. The right answer is: "We don't have enough signal to conclude anything. Here's what we'll measure and by when." Then actually measure it. Pressure-tested uncertainty is more credible than false precision.

## Connections

Metrics connect to [[discovery-intelligence]] — discovery hypotheses become experiment designs. Connects to [[product-strategy]] — the north star should reflect the strategic theory of value. Connects to [[PM-OS]] — the weekly PM rhythm includes metric review as a standing practice.
