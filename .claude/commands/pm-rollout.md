---
name: pm-rollout
description: Design a feature rollout strategy — flag architecture, staged percentage rollout, kill switch design, rollout monitoring plan, and the full/pause/rollback decision criteria. Ships safely without big-bang risk.
version: "1.0"
changed: 2026-05-20
---

# PM Feature Rollout Strategy

**Input:** Feature to roll out, target audience, risk level, any infrastructure constraints.

**Output:** Written to `notes/structured/rollout-YYYY-MM-DD-<feature-slug>.md`

**Scope:** Rollout strategy and feature flag design. For beta program design before rollout, use `/pm-beta`. For the full launch readiness audit, use `/pm-launch`. For GTM communication strategy, use `/pm-gtm`.

---

## Steps

1. **Assess the rollout risk.** What is the blast radius if this feature has a production bug? How many users are affected, how severely, and how reversibly? A dark launch (internal users only) carries different risk than a 100% rollout to all paying customers. Risk assessment drives the rollout pace.

2. **Select the rollout pattern.** Options: dark launch (feature exists but invisible), internal-only, closed beta, open beta, percentage rollout (1% → 5% → 25% → 100%), segment-first (specific user segment before general), geographic-first, or simultaneous global release. Choose based on risk and the type of signal needed.

3. **Design the flag architecture.** Identify every flag needed for this rollout. For each flag: who can toggle it (PM, on-call engineer, automated), what the default state is (off until enabled, or on for N%), and what happens if the flag service becomes unavailable.

4. **Define the rollout gates.** What signal must be observed at each stage before advancing to the next? Gates should be metric-based (error rate, performance, support ticket rate) not time-based. Advancing because "we've been at 25% for a week" without checking the signal is not a gate — it's a wait.

5. **Design the kill switch.** What can be turned off instantly if something goes wrong? Who can activate the kill switch? What is the user experience when a feature is killed mid-session (graceful degradation vs. hard stop)? The kill switch must be tested before rollout begins.

6. **Write the rollout monitoring plan.** What metrics are watched at each stage? Who is the on-call PM? What is the alert threshold that triggers a pause? What is the alert threshold that triggers a rollback?

7. **Set the rollout communication plan.** Who needs to know what at each stage — CS, support, sales, marketing? What is communicated to users at each stage, if anything?

---

## Output Format

```markdown
# Feature Rollout Plan — [Feature Name] — [Date]

**Target GA date:** [Date]
**PM owner:** [Name]
**Engineering owner:** [Name]
**On-call PM during rollout:** [Name]

---

## Rollout Risk Assessment

**User impact if production bug:** [N users affected / All paying customers / Internal only]

**Reversibility:** [Fully reversible (flag off) / Partially reversible (data changes) / Not reversible (sent communications, billing)]

**Data changes:** [None / New data written / Existing data modified — [describe]]

**Dependent systems:** [What other systems are affected by this rollout]

**Risk level:** [Low / Medium / High] — [Rationale]

---

## Rollout Pattern

**Selected pattern:** [Dark launch / Internal / Closed beta / Percentage / Segment-first / Geographic / Global simultaneous]

**Rationale:** [Why this pattern matches the risk level and signal needed]

**Rollout stages:**

| Stage | Audience | % of users | Duration | Gate before advancing |
|-------|---------|-----------|---------|----------------------|
| 0 — Dark launch | [Internal team] | 0% visible | [N days] | [Signal required] |
| 1 — Internal | [Employees / Internal accounts] | [N%] | [N days] | Error rate <X%, no P0 bugs |
| 2 — Closed beta | [Beta cohort] | [N%] | [N weeks] | [Gate metrics] |
| 3 — X% rollout | [Random N% of target segment] | [N%] | [N days] | [Gate metrics] |
| 4 — Full rollout | [All target users] | 100% | — | All gates passed |

---

## Flag Architecture

| Flag name | Purpose | Default state | Who can toggle | Fallback if service down |
|-----------|---------|--------------|----------------|-------------------------|
| [flag_name] | [What enabling this flag does] | [off] | [PM / Eng on-call / Auto at X%] | [Default off / Default on] |
| [flag_name] | | | | |

**Flag dependencies:** [Any flag that must be enabled before another can work]

**Flag cleanup plan:** [When these flags will be removed from the codebase — flags are temporary, not permanent]

---

## Rollout Gates

**Gate logic:** Advance to the next stage only when all gate metrics are satisfied — not based on time alone.

| Gate | From stage | To stage | Metric | Threshold | Measurement window |
|------|-----------|---------|--------|-----------|-------------------|
| G1 | Dark → Internal | Error rate | <[X%] | [N hours] | |
| G1 | Dark → Internal | P0 bugs | 0 | [N hours] | |
| G2 | Internal → Beta | [Metric] | [Threshold] | [Window] | |
| G3 | Beta → X% | [Metric] | [Threshold] | [Window] | |
| G4 | X% → Full | [Metric] | [Threshold] | [Window] | |

**Gate owner:** [Who evaluates and approves each gate — PM? Engineering? Both?]

---

## Kill Switch Design

**Kill switch mechanism:** [Feature flag off / Code path disabled / Database flag]

**Who can activate:**
- PM: [How]
- On-call engineer: [How]
- Automated trigger: [If any — at what threshold]

**Kill switch test plan:** [Kill switch must be tested in staging before Stage 1 begins — describe test]

**User experience when killed:**
- Mid-session: [Graceful degradation to [fallback state] / Hard error with message "[text]"]
- On next session: [What the user sees]

**Data behavior when killed:**
- Data written before kill: [Preserved / Rolled back / Partially preserved]
- In-flight requests at moment of kill: [Completed / Failed cleanly / May be inconsistent]

---

## Monitoring Plan

**Monitoring owner during rollout:** [PM name — responsible for watching metrics at each stage]

**Metrics watched at each stage:**

| Metric | Alert threshold | Pause trigger | Rollback trigger | Owner |
|--------|----------------|--------------|-----------------|-------|
| Client error rate | >[X%] | >[X%] for [N min] | >[X%] for [N min] | Eng |
| Server error rate | >[X%] | >[X%] | >[X%] | Eng |
| p95 latency | >[Xms] | >[Xms] sustained | >[Xms] for [N min] | Eng |
| Support ticket rate | >[X per N users] | >[X] | >[X] | CS/PM |
| Feature adoption | <[X%] by Day N | — | — | PM |
| [Feature-specific metric] | | | | |

**Alert routing:** [Who is paged for pause-trigger alerts during and outside business hours]

**Monitoring dashboard:** [Link to dashboard — must exist before Stage 1 begins]

---

## Pause and Rollback Decision Criteria

**Pause (stop advancing, investigate):**
- [Metric] exceeds [threshold] for [duration]
- Unexpected user behavior reported at [volume]
- [Other trigger]

**Rollback (disable feature for affected users):**
- [Metric] exceeds [rollback threshold]
- P0 bug identified with no immediate fix
- [Other trigger]

**Rollback procedure:**
1. Toggle kill switch off
2. Notify [CS lead, Eng lead, PM manager] within [N minutes]
3. Assess user impact — how many affected, data state
4. Draft user communication (if users were aware of the feature)
5. Post-mortem within [N days]

---

## Communication Plan

| Stage | Internal communications | User communications |
|-------|------------------------|---------------------|
| Stage 1 | Notify [CS, Support] | None |
| Stage 2 (Beta) | [CS enablement doc sent] | [Beta users notified — how] |
| Stage 3 (X%) | [Sales briefed] | [In-product tooltip / None] |
| Stage 4 (Full) | [Company announcement] | [In-product announcement / Email / None] |

**CS enablement checklist before Stage 2:**
- [ ] FAQ document published
- [ ] Support runbook for top 3 issues
- [ ] CS training session completed
```

---

## Quality Gate

- Blast radius assessed (how many users, how severely, how reversibly)
- Rollout stages have explicit metric-based gates (not time-based advancement)
- Flag architecture names who can toggle and what happens if flag service is unavailable
- Kill switch design specifies user experience during a mid-session kill
- Kill switch is tested before Stage 1 begins
- Monitoring dashboard exists before rollout starts (not "will be set up")
- Pause and rollback thresholds are distinct and named
- CS communication is planned at each stage where CS interaction is expected
