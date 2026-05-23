---
name: pm-gtm
description: Generate a go-to-market brief for a feature or product launch. Covers positioning, audience, launch narrative, channel plan, sales/CS enablement, and success metrics.
version: "1.0"
changed: 2026-05-20
---

# PM GTM

**Input:** Feature/product name, target audience, key differentiation, launch timing, and any known GTM constraints.

**Output:** Written to `notes/structured/gtm-YYYY-MM-DD-<launch-slug>.md`

**Distinct from `/pm-launch`:** This skill produces the go-to-market strategy (who, what, how, when we communicate externally). `/pm-launch` produces the internal readiness checklist (is the product ready to ship?). Both are needed; they are different artifacts.

---

## Steps

1. **Read context.** Load `knowledge/pm/competitive-intelligence.md` (positioning section) and `knowledge/pm/org-dynamics.md` (stakeholder communication section).

2. **Define the target audience.** Segment with precision: who is the primary audience for this launch? Enterprise buyers vs. end users vs. developers vs. the press? Each segment requires a different message and channel.

3. **Write the positioning statement.** For [target audience] who [have this need], [product/feature] is [category] that [primary benefit] because [proof], unlike [alternative] which [limitation].

4. **Develop the launch narrative.** Three messages:
   - **For users:** "You can now [job to be done] without [previous friction]."
   - **For buyers/economic decision-makers:** "This [reduces cost / increases revenue / reduces risk] by [mechanism]."
   - **For the press/market:** "[Product] is doing [what], which matters because [market context]."

5. **Define the channel plan.** For each audience: what channel, what content, who owns, what timeline.

6. **Write sales enablement requirements.** What does sales need to sell this? Battlecard update? New demo script? Pricing clarification? Objection handling for top 3 objections? Name and assign.

7. **Write CS enablement requirements.** What does CS need to support this? FAQ? Known issues? Escalation path? Migration guide if replacing existing behavior?

8. **Write support requirements.** What support volume is expected? What are the top 5 support questions? Is the support team staffed for launch volume?

9. **Define GTM success metrics.** Awareness (impressions, reach), adoption (feature activation within 30 days of launch), commercial impact (attributed pipeline or revenue, if applicable).

10. **Write the output.**

---

## Output Format

```markdown
# GTM Brief — [Feature/Product Name] — [Launch Date]

**PM owner:** [name]  **Status:** Draft | Final  
**Launch tier:** T1 | T2 | T3 (aligned with launch-readiness.md)

---

## Positioning

**Target primary audience:** [Specific segment]

**Positioning statement:**  
For [target audience] who [have this need], [product/feature] is [category] that [benefit] because [proof], unlike [alternative] which [limitation].

---

## Launch Narrative

**User message:** [What users can now do that they couldn't before]

**Buyer message:** [Business value — cost/revenue/risk framing]

**Market message:** [What this signals about product direction — for press/analysts]

---

## Channel Plan

| Audience | Channel | Content | Owner | Date |
|---|---|---|---|---|
| Users | In-app announcement | [Content type] | PM | Launch day |
| Users | Email | [Content type] | Marketing | T+1 day |
| Sales | Slack briefing + battlecard | [Content type] | PM | T-1 week |
| CS | Training + FAQ | [Content type] | PM + CS | T-2 weeks |
| Press (if T1) | Press release / briefings | [Content type] | PR | Embargo date |
| [Other] | | | | |

---

## Sales Enablement

**What sales needs:**
- [ ] Battlecard updated: [what's new]
- [ ] Demo script: [scenario to demo]
- [ ] Pricing/packaging clarification: [detail]
- [ ] Top 3 objections + responses:
  1. Objection: [X] → Response: [Y]
  2. Objection: [X] → Response: [Y]
  3. Objection: [X] → Response: [Y]

**Briefing format:** [Async doc / 30-min call / Office hours]  
**Briefing owner:** [PM]  **Briefing date:** [T-1 week]

---

## CS Enablement

**What CS needs:**
- [ ] FAQ: [Link when ready]
- [ ] Known issues at launch: [List or "none"]
- [ ] Escalation path for: [edge cases CS should escalate to PM]
- [ ] Impact on existing workflows: [What changes for current users]

---

## Support Readiness

**Estimated support volume increase:** [N]% vs. baseline for [N weeks]  
**Top 5 expected questions:** [List]  
**Support staffing:** [Additional headcount or hours needed]

---

## GTM Success Metrics

| Metric | Baseline | Target | Measured at |
|---|---|---|---|
| Feature activation rate | — | [N]% | 30 days post-launch |
| User awareness (announcement open rate) | — | [N]% | 7 days post-launch |
| [Commercial metric if applicable] | [N] | [N] | 90 days post-launch |

---

## Launch Timeline

| Milestone | Date | Owner |
|---|---|---|
| Sales briefing complete | T-1 week | PM |
| CS training complete | T-1 week | PM |
| Content ready | T-3 days | Marketing |
| Internal announcement | T-1 day | PM |
| Launch day | Launch date | PM |
| 30-day GTM review | T+30 days | PM |
```

---

## Quality Gate

- Positioning statement includes a specific alternative (not just "other solutions")
- Each audience in the channel plan has a named owner and date
- Sales enablement lists top 3 objections with responses (not just "update battlecard")
- CS enablement covers known issues (even if "none" — must be stated)
- GTM success metrics are distinct from product success metrics (pm-launch output)
