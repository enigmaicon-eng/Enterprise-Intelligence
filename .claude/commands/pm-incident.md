---
name: pm-incident
description: Run the PM's role in an incident post-mortem. Focuses on user impact assessment, communication obligations, product-level root cause, and preventing recurrence through product decisions.
version: "1.0"
changed: 2026-05-20
---

# PM Incident

**Input:** Incident description, duration, affected users/features, any timeline of events.

**Output:** Written to `decision-frameworks/decisions-log.md` (incident entry) and `notes/structured/incident-YYYY-MM-DD-<slug>.md`

**Scope:** PM's role in the post-mortem — user impact, communication, product-level causes, and prevention. Engineering owns the technical post-mortem (root cause, fix, technical prevention). This skill produces the PM's contribution to that process, not a replacement for it.

---

## Steps

1. **Read context.** Load `decision-frameworks/pm/risk-radar.md`. If this was a P0 risk on the risk register, note whether the early warning signal was visible.

2. **Assess user impact.** Not system impact — user impact. How many users were affected? What were they unable to do? Did they lose data? Were there downstream consequences (missed deadlines, financial impact, lost trust)?

3. **Classify the incident for communication obligations:**
   - **Tier 1 (major):** >5% of users impacted, >1 hour duration, or data integrity affected → executive notification + external communication required
   - **Tier 2 (significant):** 1-5% of users impacted, <1 hour duration → internal notification + proactive customer success outreach
   - **Tier 3 (minor):** <1% of users, <15 min, no data impact → internal logging only

4. **Run the communication checklist.** Was communication timely? Accurate? Did it set the right expectations? Did it reach all affected users? (This is PM's responsibility, not engineering's.)

5. **Identify the product-level root causes.** Technical post-mortems find the proximate technical cause. The PM's post-mortem question is: what product decision, priority decision, or process decision created the conditions for this incident?
   - Was a launch readiness step skipped?
   - Was a risk on the risk register that wasn't mitigated?
   - Was this a known risk that was accepted without adequate mitigation?
   - Was a rollback trigger too slow to activate?
   - Was the monitoring insufficient for PM to detect the incident without engineering escalating?

6. **Write the prevention plan from a product perspective.** What process or decision changes prevent the next incident? (Not "add more monitoring" — that's engineering's domain — but "add launch readiness audit to all Tier 1 launches" or "update kill criteria for all A/B tests to include error rate threshold.")

7. **Write the output.**

---

## Output Format

```markdown
# Incident Post-Mortem (PM View) — [Incident Name] — [Date]

**Incident date:** [Date/time]  **Duration:** [N hours]  
**Severity:** Tier 1 / Tier 2 / Tier 3  
**Engineering incident doc:** [Link to technical post-mortem]

---

## User Impact

**Users affected:** [N or %]  
**What they couldn't do:** [Specific user-facing behavior that failed]  
**Data impact:** [None / Data delayed / Data incorrect / Data lost]  
**Downstream consequences:** [Specific — missed deadlines, financial impact, support escalations]

**Highest-impact affected accounts:** [List strategic accounts, if any]

---

## Communication Timeline

| Time | Action | Audience | Content | Sent by |
|---|---|---|---|---|
| [T+N min] | Initial notification | [Internal / External] | [Content summary] | [Name] |
| [T+N min] | Status update | [Audience] | [Content] | [Name] |
| [T+N min] | Resolution notice | [Audience] | [Content] | [Name] |
| [T+N min] | Post-incident summary | [Audience] | [Content] | [Name] |

**Communication quality assessment:**
- Time to first external communication: [N minutes] — Target: <30 min for Tier 1
- Accuracy of first communication: [Was initial assessment correct?]
- Expectation accuracy: [Did we correctly predict the timeline to resolution?]

---

## Product-Level Root Causes

[Not the technical cause — the product decision or process failure that created the conditions]

1. **[Root cause]**
   - What decision or process gap contributed to this?
   - When was this risk visible and not acted on?
   - Was this on the risk register?

2. **[Root cause, if multiple]**

---

## Prevention Plan (PM Responsibilities)

| Action | Owner | Due | How it prevents recurrence |
|---|---|---|---|
| [Process change] | PM | [Date] | [Mechanism] |
| [Launch readiness update] | PM | [Date] | [Mechanism] |
| [Risk register update] | PM | [Date] | [Mechanism] |

---

## Customer Success Actions

- Accounts to proactively reach out to: [List — strategic accounts affected]
- Compensation / goodwill gestures: [None required / [Specific gesture] approved by [name]]
- Follow-up communication schedule: [Timeline]

---

## Risk Register Update

New risk to add / existing risk to update based on this incident:
```yaml
risk_id: R-[YYYYMM]-[NN]
category: execution | technical | market | organizational
description: [Risk this incident revealed]
probability: high | medium | low
impact: high | medium | low
priority: P0 | P1 | P2
mitigation: [Specific action from prevention plan]
```
```

---

## Quality Gate

- User impact is stated in user terms (not system terms)
- Communication timeline is complete with actual times
- At least one product-level root cause identified (not just technical cause)
- Prevention plan includes PM-owned actions (not just "engineering will fix")
- Strategic accounts affected have a named CS action
- Risk register updated based on incident learnings
