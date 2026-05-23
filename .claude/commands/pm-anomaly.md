---
name: pm-anomaly
description: Run a structured investigation of an unexpected metric movement. Distinguishes signal from noise, builds a causal hypothesis, and produces an investigation plan with named owner.
version: "1.0"
changed: 2026-05-20
---

# PM Anomaly

**Input:** Metric name, magnitude of change, time period, any context about what changed recently (launches, experiments, seasonality).

**Output:** Written to `notes/structured/anomaly-YYYY-MM-DD-<metric-slug>.md`

**Related to `/pm-rca`:** This skill handles metric anomaly triage (is this real? what explains it?). Use `/pm-rca` when the root cause is already suspected and you need structured causal analysis.

---

## Steps

1. **Read context.** Load `knowledge/pm/metrics-experimentation.md` (metric ambiguity section).

2. **Confirm the anomaly is real.** Before investigating the cause, verify:
   - Is the data pipeline healthy? (Check data freshness, ingestion errors, schema changes)
   - Is the time period long enough to distinguish signal from noise? (One-day spikes are often noise)
   - Is the metric definition stable? (Did anyone change the query, event name, or cohort definition?)
   - Is there a comparison anchor? (Compare to same period last week/month, not just yesterday)

3. **Quantify the anomaly.** Magnitude (% change), duration (how many days), and scope (which segments? which surfaces? which geographies?).

4. **Gather the recent change log.** What changed in the last [N days] that could explain this? (Feature launches, experiment starts/ends, infrastructure changes, marketing campaigns, seasonal events, external events)

5. **Build alternative hypotheses.** At least three explanations for the anomaly — ranked by prior probability. For each: what evidence would confirm or refute it?

6. **Apply the segmentation test.** Anomalies that appear in aggregate often disappear or concentrate when segmented. Segment by: new vs. existing users, platform, geography, user tier, acquisition channel. The segment where the anomaly concentrates reveals the cause.

7. **Assess impact urgency.** Is this affecting revenue-critical or SLA-critical metrics? Priority:
   - P0: Core conversion or retention metric, impact >10%, increasing trend — investigate immediately
   - P1: Secondary metric or smaller impact — investigate within 24 hours
   - P2: Informational metric, stable trend — investigate this week

8. **Produce the investigation plan.** Named owner, specific queries/analyses to run, decision point (when will we know enough to act?).

9. **Write the output.**

---

## Output Format

```markdown
# Anomaly Investigation — [Metric Name] — [Date]

**Metric:** [Full metric name and definition]  
**Change:** [Direction and magnitude — e.g., "DAU down 18% vs. 7-day trailing avg"]  
**Period:** [Date range]  
**Priority:** P0 | P1 | P2  
**Investigation owner:** [Name]

---

## Anomaly Verification

- [ ] Data pipeline healthy (no ingestion errors, freshness confirmed)
- [ ] Metric definition unchanged (no query or event changes)
- [ ] Comparison anchor valid (compared against: [benchmark])
- [ ] Duration sufficient for signal (not a 1-day spike)

**Verdict:** Real anomaly | Likely noise | Data quality issue — investigate pipeline first

---

## Quantified Impact

**Magnitude:** [N]% [increase/decrease] vs. [benchmark]  
**Duration:** [N days]  
**Scope:** [All users / Specific segment / Specific platform / Specific geography]  
**Trend:** [One-time event | Ongoing and stabilizing | Ongoing and worsening]

---

## Recent Change Log

Changes in the last [N] days that could explain this:
- [Date]: [Change — feature launch, experiment, campaign, infra, external]
- [Date]: [Change]

---

## Hypotheses (ranked by prior probability)

1. **[Most likely hypothesis]**  
   Evidence for: [What we already see that supports this]  
   Evidence against: [What would need to be true that seems unlikely]  
   Test: [Specific query or analysis to confirm/refute]

2. **[Alternative hypothesis]**  
   Evidence for: [Support]  
   Test: [How to confirm/refute]

3. **[Alternative hypothesis]**  
   Evidence for: [Support]  
   Test: [How to confirm/refute]

---

## Segmentation Findings

| Segment | Anomaly magnitude | Interpretation |
|---|---|---|
| New users | [N]% | [Concentration signal or not] |
| Existing users | [N]% | |
| [Platform A] | [N]% | |
| [Platform B] | [N]% | |

**Concentration:** Anomaly concentrates in [segment] — [interpretation]

---

## Investigation Plan

| Task | Owner | Due | Output |
|---|---|---|---|
| [Run specific query] | [Name] | [Date/time] | [What we'll learn] |
| [Check experiment allocation] | [Name] | [Date/time] | [What we'll learn] |
| [Segment analysis] | [Name] | [Date/time] | [What we'll learn] |

**Decision point:** By [date], we will know [specific thing] and will [action].

---

## Communication Plan

**If P0:** Immediately notify [names] — status update every [N hours]  
**If P1:** Update [channel] by [time] today  
**If P2:** Include in weekly metrics review
```

---

## Quality Gate

- Anomaly verified as real before hypotheses are generated (data quality ruled out)
- At least 3 hypotheses generated (not one hypothesis and a search for confirmation)
- Segmentation analysis planned (aggregate anomalies hide segment-specific causes)
- Investigation plan has named owner and specific output for each task
- Priority classification drives communication urgency
