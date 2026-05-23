---
name: pm-analytics
description: Run a structured product analytics deep dive — cohort analysis, funnel investigation, retention decomposition, and segmentation. Produces an evidence-based diagnosis, not a data dump.
version: "1.0"
changed: 2026-05-20
---

# PM Product Analytics Deep Dive

**Input:** Metric or question to investigate, product area, available data sources, time range.

**Output:** Written to `notes/structured/analytics-YYYY-MM-DD-<question-slug>.md`

**Scope:** PM-led analytics investigation — structured diagnosis from data. For designing the measurement system before a feature builds, use `/pm-metric-design`. For investigating a specific metric anomaly, use `/pm-anomaly`. For growth-specific funnel and loop analysis, use `/pm-growth`.

---

## Steps

1. **Define the investigation question precisely.** "Why is retention dropping?" is a starting hypothesis, not a question. "What user behavior at Day 1-7 predicts whether a user is still active at Day 30?" is an investigation question. Specificity determines whether the analysis is useful or just interesting.

2. **Identify the primary metric and its decomposition.** Break the primary metric into its component parts. Retention = acquisition rate × activation rate × re-engagement rate − churn rate. Identify which component has changed. Do not investigate all components simultaneously — diagnose which lever is moving first.

3. **Segment the data before drawing conclusions.** Aggregated metrics hide the story. Before concluding that "retention is dropping," confirm whether it's dropping for all users or a specific segment (acquisition channel, geography, user type, cohort, device, plan tier). The segment that is and isn't experiencing the drop defines the diagnosis.

4. **Run the cohort analysis.** Cohort analysis separates the behavior of users who joined at different times, preventing the mix-up of new-user trends with existing-user trends. If overall retention looks flat but new cohorts are worse than old cohorts, the product has a growing problem that aggregates are hiding.

5. **Investigate the funnel.** For the flow in question: where is the drop-off? What percentage of users who enter the funnel complete each step? Where is the drop-off largest relative to expectation? What do users who drop off have in common that users who complete do not?

6. **Test 3 hypotheses.** Based on the segmentation and funnel data, form 3 hypotheses for what is causing the pattern. For each hypothesis: what additional data would confirm or refute it? Collect that data. Do not declare a finding until at least one hypothesis has been tested against data.

7. **Produce an evidence-based diagnosis.** State: what is happening (the metric pattern), who it's happening to (the segment), when it started (the cohort or date), and the most supported explanation for why. Separate "confirmed" from "likely" from "hypothesis."

---

## Output Format

```markdown
# Product Analytics Investigation — [Question] — [Date]

**Investigation question:** [The precise question this analysis answers]
**Metric investigated:** [Primary metric]
**Time range:** [Start date] → [End date]
**Data sources:** [Analytics platform, data warehouse, etc.]
**PM:** [Name]

---

## Investigation Summary

*(Written last — the one-paragraph diagnosis for readers who don't read the full analysis)*

[What is happening, who it's happening to, when it started, most supported explanation. Findings marked as "confirmed," "likely," or "hypothesis."]

---

## Primary Metric Decomposition

**Primary metric:** [e.g., Day 30 retention rate]

**Decomposition:**

[e.g., Day 30 retention = (users active at Day 30) ÷ (users who completed activation)]

| Component | Current value | Previous period | Change | Direction |
|-----------|-------------|----------------|--------|-----------|
| [Component 1] | [X%] | [X%] | [+/-X pp] | ↑ ↓ → |
| [Component 2] | [X%] | [X%] | | |

**Primary lever moving:** [Which component accounts for most of the change in the primary metric]

---

## Segmentation Analysis

**Dimensions analyzed:**

| Segment dimension | Affected? | Notes |
|------------------|---------|-------|
| Acquisition channel | [Yes — [channels] / No] | |
| Geography | [Yes — [regions] / No] | |
| User type / persona | [Yes — [types] / No] | |
| Plan tier | [Yes — [tiers] / No] | |
| Device / platform | [Yes — [devices] / No] | |
| Signup cohort | [Yes — [cohorts] / No] | |
| Feature usage | [Yes — users who [do X] vs. don't] | |

**Key segmentation finding:**

The metric is [declining / improving / flat] for [specific segment] and [stable / different] for [other segment]. This means the investigation should focus on [what this isolates].

**Segments that are NOT affected:** [Important — rules out certain hypotheses]

---

## Cohort Analysis

**Cohort definition:** [Users grouped by [week/month] of [signup / first activation / first purchase]]

| Cohort | Day 1 | Day 7 | Day 14 | Day 30 | Day 60 | Trend vs. prior cohort |
|--------|-------|-------|--------|--------|--------|------------------------|
| [Month 1] | | | | | | Baseline |
| [Month 2] | | | | | | [+/-X pp] |
| [Month 3] | | | | | | [+/-X pp] |

**Cohort analysis finding:**

[Are newer cohorts performing better or worse than older cohorts? When did the inflection happen? This isolates whether the problem is with new users (acquisition/activation change) or existing users (product change, competition, seasonality).]

---

## Funnel Analysis

**Funnel:** [Entry point] → [Step 1] → [Step 2] → [Step N] → [Goal]

| Step | Users entering | Users completing | Completion rate | Benchmark / target | Delta |
|------|--------------|----------------|----------------|-------------------|-------|
| [Step 1] | [N] | [N] | [X%] | [X%] | [+/-X pp] |
| [Step 2] | | | | | |
| [Goal] | | | | | |

**Largest absolute drop-off:** Step [N] — [N users lost here]

**Largest relative drop-off vs. benchmark:** Step [N] — [X pp worse than target]

**Who drops off at the largest drop-off point:**

| Characteristic | Drop-off users | Completers | Difference |
|---------------|---------------|------------|------------|
| [e.g., Channel] | [X%] | [X%] | [Delta] |
| [e.g., Device] | | | |

---

## Hypothesis Testing

**Hypothesis 1: [Name]**

Hypothesis: [What PM believes is causing the pattern]

Evidence for: [Data point supporting this hypothesis]
Evidence against: [Data point that weakens this hypothesis]
Test: [What additional data would confirm or refute it]
Result: [Confirmed / Refuted / Inconclusive — with data]

**Hypothesis 2: [Name]**

Hypothesis:
Evidence for:
Evidence against:
Test:
Result:

**Hypothesis 3: [Name]**

Hypothesis:
Evidence for:
Evidence against:
Test:
Result:

---

## Findings

**Confirmed (data clearly supports):**
1. [Finding with data citation]

**Likely (directionally supported, not conclusive):**
1. [Finding with data citation and caveat]

**Hypothesis (plausible but not yet tested):**
1. [Hypothesis with what would be needed to test it]

---

## Recommended Actions

| Action | Evidence basis | Owner | Priority | Timeline |
|--------|--------------|-------|---------|---------|
| [Action] | [Finding it addresses] | [Name] | P0/P1/P2 | [Date] |

**What this analysis cannot determine:** [What data would be needed to answer remaining questions — be explicit about the limits of the analysis]

**Follow-up analysis recommended:** [Yes / No — if yes, what question]
```

---

## Quality Gate

- Investigation question is precise and answerable (not "understand retention")
- Primary metric decomposed into components before investigating
- Data segmented before conclusions drawn (aggregates can hide the story)
- Cohort analysis completed — distinguishes new-user vs. existing-user trends
- Funnel analysis identifies the step with the largest absolute and relative drop-off
- At least 3 hypotheses tested against data (not declared as findings without testing)
- Findings separated into: confirmed / likely / hypothesis
- Analysis limitations stated explicitly (what it can't determine)
