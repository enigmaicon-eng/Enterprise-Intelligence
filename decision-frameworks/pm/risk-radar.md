# Risk Radar
## Risk Identification, Classification, and Triage for PMs

Risk management is not about avoiding risk — product work is inherently uncertain. It is about knowing which risks you're taking, whether they're the right risks to take, and what you'll do when they materialize.

---

## The PM Risk Taxonomy

Organize risks into four categories. Each requires different detection and response.

**Category 1 — Strategic risks**
The bet is wrong: wrong market, wrong timing, wrong advantage theory.
Detection: Strategy assumptions not being validated by discovery. Leading indicators not moving as expected. Competitive landscape shifting against you.
Response: Structured strategy review (quarterly minimum). Discovery investment against the riskiest assumptions. Kill criteria for H2 bets.

**Category 2 — Execution risks**
Right direction, wrong execution: misaligned teams, unclear requirements, dependency failures, scope creep.
Detection: Velocity declining without explanation. Recurring rework. Dependencies not surfacing until they block. "Done" definition shifting.
Response: Weekly execution audit. Pre-sprint contract. Explicit dependency mapping on every initiative.

**Category 3 — Market risks**
External conditions changing: regulatory, competitive, economic, technological.
Detection: Competitor moves. Regulatory signals. Customer feedback patterns shifting. Partner behavior changes.
Response: Periodic environmental scan. Scenario planning for top market risks.

**Category 4 — Organizational risks**
People and process: key person dependency, team misalignment, burnout, attrition, leadership changes.
Detection: Escalating conflicts. Key people becoming bottlenecks. Decision velocity declining. Team satisfaction signals.
Response: 1:1 engagement. Cross-training for single points of failure. Explicit succession for PM-owned knowledge.

---

## The Risk Radar Matrix

Weekly practice: maintain a living risk log. Each risk entry includes:

```yaml
risk_id: R-YYYYMM-NN
category: strategic | execution | market | organizational
description: [What could go wrong, precisely]
probability: high | medium | low
impact: high | medium | low
priority: P0 | P1 | P2  # high/high = P0, rest based on judgment
owner: [Named person]
early_warning_signal: [Observable leading indicator that risk is materializing]
mitigation: [Specific action being taken]
contingency: [What we do if the risk materializes]
last_reviewed: YYYY-MM-DD
status: active | mitigated | realized | closed
```

**Priority math:**
- P0: High probability + High impact. Act now.
- P1: High probability + Medium impact, OR Medium probability + High impact. Plan mitigation this sprint.
- P2: Everything else. Monitor.

**The risk register is a living document.** Risks that are closed should be documented: what happened, was the early warning signal correct, what would you do differently? This builds organizational risk intuition.

---

## Pre-Mortem Discipline

Before any major launch or milestone, run a pre-mortem:

**The prompt:** "It is [date X]. The initiative has failed. What went wrong?"

Run this in a group. Have each person write their failure scenario silently before the group discussion (prevents anchoring on the first scenario proposed).

**What pre-mortem surfaces:**
- Risks the team knew but weren't discussing (the "obviously")
- Risks the team had different models of (the "I thought you were handling that")
- Risks no one was thinking about (the "I hadn't considered that")

**Output:** A prioritized list of failure scenarios with named mitigations. The best pre-mortems produce 3-5 specific actions before the launch.

**Avoid:** The pre-mortem that produces a list of risks but no actions. The list without actions is a false sense of security.

---

## Risk Communication

**To the team:** Transparent risk log. No hidden risks. When a risk materializes, announce it immediately with: what happened, what we're doing about it, what we need from the team.

**To stakeholders:** Regular risk summary in executive updates — not a full risk register, but the top 3 risks and their status. Frame: "Here's what we're watching and what we're doing about it."

**To leadership:** Escalate P0 risks immediately. Don't wait for the next scheduled review. If you know about a P0 risk on a Tuesday and your next exec review is Friday, send a heads-up on Tuesday.

**Risk communication anti-pattern:** Withholding risks to "protect the team" or "avoid panicking stakeholders." This almost always makes things worse. Leaders can manage risks they know about. They cannot manage risks they discover at crisis stage.

---

## Launch Risk Checklist

For any significant launch, assess these specifically:

**Technical:**
- [ ] Load testing at 2x expected peak traffic
- [ ] Rollback procedure documented and tested
- [ ] Feature flags enabling gradual rollout
- [ ] Monitoring and alerting configured for new feature
- [ ] Data migration (if any) validated in staging

**Market:**
- [ ] Competitive response scenarios modeled
- [ ] Launch timing risk assessed (avoid holidays, competitive announcements)
- [ ] Regulatory review complete if applicable

**Organizational:**
- [ ] Support team trained and staffed for launch volume
- [ ] Sales enablement complete
- [ ] Internal communication plan executed

**Data:**
- [ ] Instrumentation verified in staging
- [ ] Baseline metrics captured pre-launch
- [ ] Experiment design finalized (if A/B testing)

---

## Risk Management Anti-Patterns

**The risk list without owners:** Every risk has a name on it. Ownerless risks become everyone's problem and no one's responsibility.

**The static risk register:** Risks that haven't been reviewed in 30 days are not being managed — they're being filed. Review the register weekly.

**The optimism bias:** Probability assessments that systematically underestimate downside scenarios. Fix: at review, ask "what would a pessimist say?" for each risk.

**The solved-problem risk:** A risk is marked "mitigated" after a plan is made but before the mitigation is verified. Mitigation status requires evidence, not intentions.
