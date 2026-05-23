---
name: pm-metric-design
description: Design the measurement system for a feature before it's built. Produces instrumentation brief, metric hierarchy, success criteria, and the baseline measurement plan.
version: "1.0"
changed: 2026-05-20
---

# PM Metric Design

**Input:** Feature name, success hypothesis, target user behavior to change.

**Output:** Written to `notes/structured/metrics-YYYY-MM-DD-<feature-slug>.md`

**When to run:** Before engineering starts the feature — not after. Instrumentation added post-hoc creates measurement debt.

---

## Steps

1. **Read context.** Load `knowledge/pm/metrics-experimentation.md` (instrumentation section and metrics stack).

2. **State the behavior change clearly.** "This feature should change [current behavior] to [target behavior]." If you can't state the behavior change, the feature's success criterion is unclear — stop and clarify before designing metrics.

3. **Map to the metrics stack.** For this feature, identify:
   - **North star connection:** How does this feature contribute to the north star metric?
   - **Product health layer (L2):** Which AAERM metric does this feature primarily move? (Acquisition / Activation / Engagement / Retention / Monetization)
   - **Feature layer (L3):** What feature-specific metrics will measure this feature's specific job?
   - **Operational layer (L4):** What error rates, latency thresholds, or data quality metrics are needed?

4. **Write the instrumentation brief:**
   - What user behaviors are we trying to change?
   - What events will tell us those behaviors changed?
   - What's the baseline we're measuring against?
   - What's the minimum detectable effect we care about?
   - How many weeks of data are needed to be confident?

5. **Identify the instrumentation events.** For each event:
   - Event name (consistent with naming convention)
   - When it fires (trigger)
   - Properties to capture (user ID, session, variant, context)
   - Which metric it measures

6. **Capture baselines.** For every metric that will measure this feature's success: record the current baseline BEFORE the feature launches. This is required for any post-launch analysis.

7. **Define the measurement plan.** When will we first look? What does "working" look like at 7 days / 30 days / 90 days?

8. **Write the output.**

---

## Output Format

```markdown
# Metric Design — [Feature Name] — [Date]

**Feature:** [Name]  
**Success hypothesis:** [The behavior change this feature enables]

---

## Metric Hierarchy

**North star connection:**  
[How this feature contributes to the north star metric — even if indirect]

**Primary product health metric (L2):**  
[Which AAERM dimension this primarily impacts and how]

**Feature success metrics (L3):**
| Metric | Definition | Measurement Method | Baseline | Target |
|---|---|---|---|---|
| [Primary] | [What it measures] | [How] | [Current] | [Goal] |
| [Secondary] | [What it measures] | [How] | [Current] | — |

**Guardrail metrics:**
| Metric | Baseline | Floor (must not fall below) |
|---|---|---|
| [Metric] | [N] | [N] |

**Operational metrics (L4):**
| Metric | Threshold |
|---|---|
| Error rate | < [N]% |
| P95 latency | < [N]ms |

---

## Instrumentation Brief

**Behaviors we're trying to change:**
1. [Current behavior] → [Target behavior]
2. [Current behavior] → [Target behavior]

**Events needed:**

| Event name | Fires when | Properties to capture | Metric it measures |
|---|---|---|---|
| [event_name] | [trigger] | [user_id, session, ...] | [metric] |
| [event_name] | [trigger] | [properties] | [metric] |

**Baseline capture:**
- [ ] All L3 metrics baselined before launch: [date]
- [ ] Baseline values recorded above

**Minimum detectable effect:** [N]% change in [primary metric] worth measuring  
**Weeks of data to confidence:** [N] weeks at expected traffic

---

## Measurement Plan

| Checkpoint | Date | What we're looking for |
|---|---|---|
| T+7 days | [Date] | Early signal on activation/adoption |
| T+30 days | [Date] | Retention cohort first read |
| T+90 days | [Date] | Full lifecycle signal |

**Decision rule at T+30:** If [primary metric] is [above / below] [threshold], we [continue / investigate / iterate].

---

## Instrumentation Debt Assessment

**Gaps in current tracking:** [What's not currently tracked that needs to be]  
**Engineering work required:** [New events / new dashboards / new queries]  
**Risk if not instrumented:** [What decision we won't be able to make without this data]
```

---

## Quality Gate

- Behavior change stated (not "improve engagement" — specific behavior)
- Baseline values are actual current numbers, not estimates
- Every metric has a measurement method (not assumed to exist)
- Guardrail metrics defined alongside success metrics
- Instrumentation events listed with trigger and properties
- Engineering work for instrumentation is part of the feature scope
