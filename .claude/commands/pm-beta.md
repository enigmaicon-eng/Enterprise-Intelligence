---
name: pm-beta
description: Design and run a structured beta program — recruitment criteria, structured feedback collection, iteration cycles, graduation criteria, and the beta-to-GA decision. Prevents beta programs from becoming indefinite previews.
version: "1.0"
changed: 2026-05-20
---

# PM Beta Program Design

**Input:** Feature or product entering beta, target user criteria, beta objectives, timeline to GA.

**Output:** Written to `notes/structured/beta-YYYY-MM-DD-<feature-slug>.md`

**Scope:** Full beta program design — recruitment, feedback structure, iteration cycles, graduation decision. For the broader launch readiness audit, use `/pm-launch`. For rollout strategy after beta completes, use `/pm-rollout`.

---

## Steps

1. **Define the beta objective.** A beta program without a clear objective becomes an indefinite preview. What specific questions must the beta answer before GA? Acceptable objectives: validate usability with real users, surface edge cases in production data, test the support load, confirm performance under real usage patterns. "Get feedback" is not an objective.

2. **Design the recruitment criteria.** Who should be in the beta? Criteria must be specific: user segment, usage pattern, technical sophistication, geographic distribution, company size (if B2B). The beta cohort must represent the users who will be most affected by the feature, not the users who are most enthusiastic about betas generally.

3. **Set the cohort size.** Enough to surface systematic issues, small enough to manage feedback loops. General guidance: 50-200 users for consumer, 10-30 companies for B2B. Explain the rationale for the chosen size.

4. **Design the feedback collection system.** Structured feedback, not open-ended requests. Define: the in-product feedback mechanism, the survey cadence and questions, the interview schedule (1:1s for depth), and the usage data that will be tracked. Every piece of feedback must be actionable or categorizable.

5. **Plan the iteration cycles.** Beta is not static. Define: the feedback intake frequency, the triage process (who decides what goes into the next iteration), the iteration cadence, and the communication cadence with beta users (they must feel heard, or they stop giving feedback).

6. **Set the graduation criteria.** Explicit conditions under which the beta ends and GA begins. Graduation requires: all P0 issues resolved, performance metrics at target, support load within CS capacity, documentation complete. List the specific conditions.

7. **Plan the beta-to-GA transition.** How are beta users notified of GA? Are they automatically moved to GA or do they need to opt in? What changes for them at GA (pricing, terms, support tier)?

---

## Output Format

```markdown
# Beta Program Plan — [Feature Name] — [Date]

**Beta objective:** [Specific questions this beta must answer]
**Target GA date:** [Date]
**Beta duration:** [Weeks]
**PM:** [Name]  **Engineering lead:** [Name]  **CS lead:** [Name]

---

## Beta Objectives

The beta is complete when these questions are answered:

1. [Specific question — e.g., "Can [user type] complete [core flow] without support intervention?"]
2. [Specific question — e.g., "Does the feature perform within [N ms] at [scale level]?"]
3. [Specific question — e.g., "What percentage of beta users would use this weekly if available?"]

**What the beta is NOT designed to learn:** [Explicit exclusions — things that will be addressed post-GA or are already known]

---

## Recruitment Criteria

**Target cohort:**

| Criterion | Requirement | Rationale |
|-----------|-------------|-----------|
| User segment | [Who] | [Why they're representative] |
| Usage pattern | [e.g., "Active at least 3x/week"] | [Why this matters] |
| Technical sophistication | [e.g., "Comfortable with APIs"] | [If relevant] |
| Geography | [Regions] | [If relevant — compliance, language] |
| Company size (B2B) | [e.g., "50-500 employees"] | [Target segment] |
| Special criteria | [e.g., "Has experienced the problem the feature solves"] | |

**Cohort size:** [N users / N companies]

**Size rationale:** [Why this number — enough to surface issues, manageable for iteration]

**Recruitment method:**
- [Method 1: in-app invitation to users who match criteria]
- [Method 2: CS nomination for strategic accounts]
- [Method 3: opt-in waitlist]

**Exclusion criteria (do not invite):**
- [Who to exclude and why — e.g., "Accounts in active support escalation"]

---

## Feedback Collection System

### In-Product Feedback

**Mechanism:** [Embedded feedback widget / thumbs up-down / NPS prompt / other]
**Trigger:** [When it appears — after first use, after N sessions, on specific actions]
**Questions asked:** [Specific questions — not "how do you like it?"]

### Structured Survey

**Cadence:** [Week 1, Week 3, Final week of beta]
**Length:** [Max N questions — keep short for response rate]
**Core questions:**

Week 1 survey:
1. [First impression question — the workflow being supported]
2. [Friction identification question]
3. [Missing capability question]

Mid-beta survey:
1. [Usage frequency and depth question]
2. [Satisfaction measurement — score + reason]
3. [Top pain point]

Final survey:
1. [Would you recommend this feature — NPS or similar]
2. [Is this ready for GA? What's missing?]
3. [Open question: what should we know before we ship this broadly?]

### User Interviews

**Cadence:** [Weekly / bi-weekly]
**Format:** [30-min 1:1 video call]
**Participants per cycle:** [N users — rotate for variety, include power users AND struggling users]
**Interview guide:** [Link to `/pm-user-interview` output or brief outline here]

### Usage Analytics

**Tracked behaviors:**
| Metric | Target | Red flag threshold |
|--------|--------|--------------------|
| [e.g., Feature adoption rate] | [X% of beta users use weekly] | [<X%] |
| [e.g., Flow completion rate] | [X%] | [<X%] |
| [e.g., Support ticket rate] | [<X tickets per 100 users] | [>X] |
| [e.g., Performance (p95 latency)] | [<Xms] | [>Xms] |

---

## Iteration Plan

**Feedback intake frequency:** [Weekly — every Monday, triage async, PM + eng sync Tuesday]

**Triage process:**
1. Categorize: Bug / UX issue / Missing capability / Working as intended / Out of scope
2. Prioritize: P0 (blocks beta use) / P1 (significant friction) / P2 (nice to have)
3. Decision: Fix in beta / Fix before GA / Backlog / Not fixing (with reason)

**Iteration cadence:** [Weekly releases / bi-weekly — what beta users can expect]

**Communication to beta users:**
- [Release notes: what changed, sent when]
- [Response SLA: within N business days for reported issues]
- [Community channel: Slack / Discord / email list — where beta users can talk to each other and the PM]

**Beta user communication cadence:**
| Communication | Frequency | Owner | Content |
|---------------|-----------|-------|---------|
| Release notes | Each iteration | PM | What changed, what's coming |
| Individual responses | Within N days of report | PM/CS | Acknowledgment + status |
| Group update | Bi-weekly | PM | Overall beta progress, what we're learning |

---

## Graduation Criteria

**The beta ends when ALL of the following are true:**

Technical readiness:
- [ ] All P0 bugs resolved
- [ ] All P1 bugs resolved or have accepted timeline
- [ ] Performance at target (p95 latency <Xms, error rate <X%)
- [ ] Data retention and deletion working correctly

User readiness:
- [ ] Flow completion rate ≥ [X%]
- [ ] Support ticket rate ≤ [X per 100 users]
- [ ] At least [N] users have used the feature for ≥ [N] sessions
- [ ] No outstanding "won't use this" signals from target cohort

Operational readiness:
- [ ] CS trained and documentation published
- [ ] Support runbook for top 5 issues
- [ ] Monitoring and alerts configured
- [ ] Rollback plan confirmed

**If graduation criteria are not met by [date]:** [Extend beta by N weeks / Reduce scope / PM escalates to exec with recommendation]

---

## Beta-to-GA Transition

**How beta users are notified:** [In-app message + email, N days before GA]

**Transition experience:**
- Beta users automatically moved to GA: [Yes / No — if no, describe opt-in]
- Changes at GA for current beta users: [Pricing changes / Support tier / Feature changes]
- Grandfathering policy (if pricing changes): [Policy]

**GA announcement:** [Link to `/pm-gtm` brief or brief description of GA communication]
```

---

## Quality Gate

- Beta objective is a specific question, not "get feedback"
- Recruitment criteria are explicit (not "engaged users")
- Cohort size is stated with rationale
- Feedback collection is structured (specific questions, specific cadence) — not "collect feedback"
- Iteration cycle has a triage process with named decision owner
- Graduation criteria are binary pass/fail — not judgment calls
- Beta-to-GA transition answers: how users are notified, what changes for them, what the pricing/terms transition is
