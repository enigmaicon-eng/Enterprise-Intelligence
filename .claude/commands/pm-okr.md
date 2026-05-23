---
name: pm-okr
description: Craft OKRs from strategic context. Applies the three-horizon model, ensures key results are measurable with baselines, and validates alignment between Objective intent and KR measurement.
version: "1.0"
changed: 2026-05-20
---

# PM OKR

**Input:** Strategic context, time horizon (quarterly/annual), key initiatives or bets for the period, team/product scope.

**Output:** Written to `strategy/monthly/YYYY-Q[N]-okrs.md` or displayed inline if drafting only.

---

## Steps

1. **Read context.** Load `knowledge/pm/product-strategy.md` (three-horizon section). If a strategy check exists, read it first — OKRs should be downstream of strategy, not an alternative to it.

2. **Validate the Objective is an objective.** An OKR objective is a qualitative statement of direction — inspirational, directional, time-bound. It answers "what are we trying to achieve?" NOT what metric we'll improve. If the user gives a metric as the objective, reframe it.
   - Wrong: "Increase retention from 40% to 60%"
   - Right: "Build a product users return to habitually"

3. **Draft the Objective.** One sentence. Aspirational but grounded. Should be achievable in the time horizon. Should clearly communicate direction to someone who doesn't know the team's plans.

4. **Generate Key Results.** 3-5 KRs per objective. Each KR:
   - Is measurable (specific metric or milestone)
   - Has a baseline (where we are now) and a target (where we want to be)
   - Has a confidence level (60-70% attainable is the right stretch — not 100%, not 10%)
   - Is an outcome, not an output ("40% of new users complete onboarding" not "ship onboarding v2")
   - If achieved, would confirm the objective was reached

5. **Run the alignment check.** For each KR: "If this KR is achieved but all others fail, does the objective feel achieved?" If yes, it's a strong KR. If no, it's measuring activity, not outcome.

6. **Identify leading vs. lagging KRs.** At least one KR should be a leading indicator (measurable in the first half of the quarter). A set of purely lagging KRs means the team has no early warning signal.

7. **Map to initiatives.** For each KR, name the 1-2 initiatives that will drive it. If a KR has no named initiative, it's aspirational without a path — flag it.

8. **Write the output.**

---

## Output Format

```markdown
# OKRs — [Team/Product] — Q[N] YYYY

**Time horizon:** Quarterly  
**Owner:** [PM name]  
**Strategy context:** [One sentence — what strategic moment this quarter serves]

---

## Objective 1: [Qualitative direction statement]

**Intent:** [One sentence — what "winning" looks like if this Objective is achieved]

| Key Result | Baseline | Target | Confidence | Type | Owner |
|---|---|---|---|---|---|
| KR1: [Measurable outcome] | [Current] | [Target] | 65% | Lagging | [name] |
| KR2: [Measurable outcome] | [Current] | [Target] | 70% | Leading | [name] |
| KR3: [Measurable outcome] | [Current] | [Target] | 60% | Lagging | [name] |

**Initiatives driving this Objective:**
- [Initiative name] → KR1, KR2
- [Initiative name] → KR3

---

## Objective 2: [Qualitative direction statement]

[Same structure]

---

## OKR Health Check

**Alignment to strategy:** [Which strategy assumption does each Objective test or advance?]

**Leading indicator coverage:** [Is at least one KR per Objective measurable in the first 6 weeks?]

**Initiative coverage:** [Does every KR have a named initiative? Flag any KRs without one.]

**Anti-stretch check:** [Any KR at 100% confidence should be questioned — it's a forecast, not an objective]

**Anti-impossible check:** [Any KR at <40% confidence should be questioned — is this aspirational or just ungrounded?]
```

---

## Quality Gate

- Objective is qualitative and directional — contains no numbers
- Each KR has a baseline and a target (not just "improve X")
- At least one KR per objective is a leading indicator
- All KRs pass the alignment check (achieving it confirms the objective)
- Every KR has a named initiative (or is flagged as aspirational-without-path)
- Confidence levels are 50-80% (not 100%, not <30%)
- Output entries = output metrics only if intentional (milestones are acceptable KRs for non-quantifiable outcomes)
