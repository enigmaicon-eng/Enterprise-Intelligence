# Launch Readiness
## The Go/No-Go System That Prevents Premature Launches

Launch readiness is not a checklist exercise. It is a structured forcing function for surfacing the risks that optimism hides. The purpose is not to prevent launches — it is to prevent launches that fail in ways that could have been anticipated.

---

## Launch Tiers

Not all launches require the same rigor. Right-size the process.

| Tier | Definition | Lead time for readiness check | Who approves go/no-go |
|---|---|---|---|
| Tier 1 | New product, major new capability, pricing change, significant architecture change | 4 weeks | PM Lead + Engineering Lead + executive sponsor |
| Tier 2 | Significant feature, new user segment, external partner dependency | 2 weeks | PM + Engineering Lead |
| Tier 3 | Feature iteration, internal tooling, limited rollout | 1 week | PM |
| Tier 4 | Bug fix, copy change, A/B test variant | None | PM judgment |

**Err toward higher tier when in doubt.** The cost of extra preparation is lower than the cost of a failed launch.

---

## The Launch Readiness Audit

Run this as a working session with engineering, design, QA, and data — not a solo PM checklist.

### Section 1 — Problem and Hypothesis Clarity

- [ ] **Problem statement is locked.** The problem being solved is documented and has not changed significantly since scoping.
- [ ] **Success hypothesis is explicit.** "We believe this launch will [behavior change] because [mechanism]" — the mechanism is stated.
- [ ] **Primary success metric is named.** One metric wins or loses this launch. It is agreed upon by PM, engineering, and leadership.
- [ ] **Guardrail metrics are named.** Metrics that must not degrade. If primary metric improves but guardrails degrade, the launch has failed.
- [ ] **Baseline is captured.** Pre-launch measurement of all primary and guardrail metrics exists.

### Section 2 — Technical Readiness

- [ ] **Feature works end-to-end in staging.** Not "mostly works" — the full user flow is tested.
- [ ] **Load testing completed.** Tested at minimum 2x expected peak traffic. Results documented.
- [ ] **Rollback procedure exists and is tested.** Not documented only — actually tested. Time to rollback is known.
- [ ] **Feature flags in place.** Gradual rollout is possible without a new deployment.
- [ ] **Monitoring and alerting configured.** Alerts set for new feature's error rate, latency, and key events. Someone is on call.
- [ ] **Data migration (if any) validated.** Run in staging. Reversibility assessed.
- [ ] **API contracts locked.** No breaking changes to external or internal APIs without partner sign-off.
- [ ] **Security review complete (if applicable).** Any new data collection, authentication surface, or permissions change reviewed.

### Section 3 — Instrumentation and Data

- [ ] **All events instrumented.** Every event needed to measure the success hypothesis is firing correctly in staging.
- [ ] **Instrumentation verified end-to-end.** Events flow from client → collection → analytics. Not assumed — verified.
- [ ] **Experiment design finalized (if A/B).** Hypothesis, primary metric, guardrails, sample size, duration all documented before launch.
- [ ] **Data team alignment.** Data partner has reviewed instrumentation and experiment design (if applicable).
- [ ] **Analytics access ready.** Dashboard or query exists to measure primary metric from day one.

### Section 4 — User Readiness

- [ ] **User research informed the design.** At least 3 user conversations validated the problem and tested the solution concept.
- [ ] **Usability tested with target users.** Prototype or beta tested. Critical usability issues resolved.
- [ ] **Help and documentation updated.** User-facing docs, tooltips, empty states reflect the new experience.
- [ ] **Edge cases mapped.** What happens when: the user has no data? the feature errors? the user is on a slow connection? Mobile behavior tested if applicable.

### Section 5 — Go-to-Market Readiness

- [ ] **Launch communication plan exists.** Who hears about this, through what channel, in what order? (Internal first, then external.)
- [ ] **Support team trained.** CS/support knows what's launching, what questions to expect, and how to answer them.
- [ ] **Support content ready.** FAQs, escalation paths, known issues documented for support team.
- [ ] **Sales enablement complete (if commercial feature).** Sales knows the value proposition, objection handling, and pricing (if any).
- [ ] **Customer commitments cross-checked.** Any promises made to specific customers about this launch are verified against the actual scope.
- [ ] **Competitive response scenarios documented.** What happens if a competitor reacts to this launch? (Tier 1 and 2 only)

### Section 6 — Organizational Readiness

- [ ] **Launch timing risk assessed.** No conflicts with: holidays, competitor announcements, company all-hands, compliance deadlines, adjacent launches.
- [ ] **Regulatory review complete (if applicable).** Legal/compliance has reviewed if the feature touches: payments, healthcare data, privacy-regulated data, financial data, international markets.
- [ ] **Executive visibility confirmed (Tier 1).** Executive sponsor is aware of the launch date and has reviewed risk summary.
- [ ] **Post-launch monitoring schedule set.** Who is checking metrics, how often, for how long after launch?
- [ ] **Escalation path clear.** If something goes wrong post-launch, who is the first call? Who approves a rollback?

---

## The Go/No-Go Decision

Run the go/no-go meeting with all owners present. It is not a status update — it is a decision.

**Structure:**
1. Review open items from readiness audit (items marked incomplete)
2. For each open item: accept the risk, mitigate before launch, or delay
3. State the go/no-go decision explicitly
4. If go: name the post-launch monitoring owner and first check-in time
5. If no-go: name the specific criteria that would change the decision and estimated date

**Decision recording:**
```yaml
launch: [feature name]
date: YYYY-MM-DD
tier: 1 | 2 | 3
decision: go | no-go | conditional-go
open_items:
  - item: [description]
    disposition: accepted | mitigated | blocking
conditions_if_conditional_go:
  - [condition that must be met before launch proceeds]
post_launch_owner: [name]
first_check_in: [time after launch]
rollback_criteria: [observable condition that triggers rollback]
approvers: [names]
```

### Conditional Go

A conditional go is sometimes appropriate: "We will launch on [date] if [specific condition] is met by [date]." The condition must be specific and observable — not "when we feel confident" but "when load test at 2x traffic passes with p99 < 500ms."

If the condition is not met by the deadline, the default is no-go. Don't renegotiate the condition under deadline pressure.

---

## Post-Launch Monitoring Protocol

Launch is not the end — it is the beginning of the measurement phase.

**Week 1 monitoring rhythm:**
- Day 1 (launch day): error rate check every 2 hours. PM on standby.
- Days 2-3: daily metric review. Support ticket volume tracked.
- Days 4-7: every-other-day review. Experiment is running — no peeking at results yet (p-hacking risk).

**Week 2-4:**
- Weekly metric review against success hypothesis
- Support escalation patterns reviewed with CS
- If A/B: do not call the experiment early. Respect the predetermined duration.

**30-day retrospective:**
- Primary metric result vs. hypothesis
- Guardrail metric status
- Instrumentation gaps discovered post-launch
- What would have changed the go/no-go decision if known at launch time?
- Launch readiness checklist: which items turned out to matter most? Which were theater?

---

## Rollback Decision Framework

Rollback criteria should be written before launch. At launch, emotions run high and judgment degrades. Written criteria remove the judgment call.

**Automatic rollback triggers (no discussion needed):**
- Error rate exceeds [N]% for [M] consecutive minutes
- Core user flow completion rate drops below [X]% (vs. baseline)
- Data loss or corruption detected

**Discussion-required rollback triggers:**
- Guardrail metric degrades by >[Y]% with no signs of recovery after [Z] hours
- Support ticket volume exceeds [N]x normal within first 48 hours
- Significant customer escalation from a strategic account

**When rollback is not available:** If the feature cannot be rolled back (data migration, external partner announcement, customer commitments made), the launch tier should be elevated and the readiness standard should be correspondingly higher.

---

## Launch Readiness Anti-Patterns

**The feature-complete fallacy:** "Engineering says it's done" ≠ ready to launch. Done means the code is merged. Ready means the entire system (monitoring, docs, support, instrumentation, rollback) is prepared.

**The optimistic checklist:** Marking items green because "we'll handle it post-launch." Checklist items are commitments, not suggestions. An incomplete item that's accepted must be explicitly marked as a risk with a named owner, not silently checked off.

**Scope creep into the readiness period:** Adding features during the readiness window to "make the launch better." Every addition resets the readiness checklist for that component.

**The launch date as immovable object:** When the go/no-go decision is made before the readiness audit because the launch date can't slip. Dates should be inputs to planning, not overrides of readiness. A failed launch costs more than a delayed launch.

**No rollback plan:** "We'll figure it out if something goes wrong." Rollback procedures that are invented under production pressure are slower, riskier, and more error-prone than ones written in advance.
