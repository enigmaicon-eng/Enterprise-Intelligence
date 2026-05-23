# Sprint Workflow
## The Bi-Weekly Cycle That Turns Roadmap Into Shipped Product

A sprint is not a time-box for completing tasks. It is a commitment cycle — a period during which the team commits to a specific outcome and executes against it. The PM's role in the sprint cycle is not project management — it is clarity supply chain: ensuring the team always has enough context to make good decisions without needing to escalate.

---

## Sprint Roles (PM Perspective)

**PM owns:** Acceptance criteria, priority calls within the sprint, user-facing decisions, stakeholder communication.

**Engineering owns:** Technical approach, estimation, task breakdown, implementation decisions, velocity.

**Design owns:** UX decisions within agreed parameters, design assets, usability validation.

**PM does NOT own:** How engineering solves the problem, sprint task assignments, daily standup outcomes.

The most common sprint failure is PM over-involvement in the "how" and under-investment in the "what" and "why."

---

## Sprint Planning (Day 1, 2-3 hours)

**Pre-planning PM checklist (must complete before the meeting):**
- [ ] Sprint goal drafted (one sentence: what outcome does this sprint achieve for users?)
- [ ] Top 5-7 stories fully specified with acceptance criteria
- [ ] P0 items have zero open questions (all [DECISION NEEDED] annotations resolved)
- [ ] Dependencies surfaced and named: external dependencies either confirmed or risk-accepted
- [ ] Design assets ready for stories that need them (not "in progress")
- [ ] Capacity accounted for: vacations, interviews, on-call rotation noted

**The pre-sprint contract (30 min before planning):**
PM + engineering lead, not the full team. Align on:
- What is the sprint goal? (One sentence outcome)
- What is the team's capacity this sprint? (Accounting for all non-sprint time)
- What are the must-have items and what is flexible?
- Are there any technical unknowns that need a spike?

**During planning:**
1. PM presents the sprint goal (one sentence — not a list of tickets)
2. Team reviews stories, asks questions; PM answers or flags for follow-up (not mid-meeting research)
3. Team estimates; PM does not advocate for specific estimates
4. If capacity overflows: PM prioritizes cuts, not engineering
5. Sprint commitment is the team's commitment, not PM's wish list

**Sprint goal standard:** "At the end of this sprint, users will be able to [observable outcome] because [engineering deliverable]." Not: "Complete tickets X, Y, Z."

---

## During the Sprint (Days 2-10)

**PM's daily practice:**
- 15-minute async check on blockers: scan standup notes or Slack for anything that needs PM input
- Respond to engineering questions within 2 hours (PM as the fast path to decisions)
- Surface and resolve any open design questions before they block engineering

**The PM blocker taxonomy:**
- **Requires PM decision:** Make the call immediately, document it, don't let it wait for a meeting
- **Requires stakeholder input:** Pull the right person in within 24 hours
- **Requires design:** Flag to designer with context; give them a deadline
- **Requires discovery:** Is this a validation question? Can it be answered from existing data? If it will take >1 sprint to answer, make the best decision with current information and instrument to learn

**Scope change protocol during sprint:**
If new work arrives mid-sprint:
1. Is it more important than anything in the current sprint? If no, add to backlog.
2. If yes: name what it replaces. Nothing gets added without something removed or the sprint goal changing.
3. Communicate scope change to anyone who expected the replaced work.

**Not the PM's job during sprint:**
- Running daily standups (Scrum Master / Engineering Lead)
- Tracking individual task completion
- Reporting sprint progress to executives mid-sprint (let the sprint complete)

---

## Sprint Review / Demo (Last Day, 1 hour)

**Purpose:** Show stakeholders what was built. Create shared reality between builders and stakeholders.

**PM responsibilities before review:**
- [ ] Acceptance criteria verified (PM tests before the meeting, not during)
- [ ] Demo environment is stable and representative
- [ ] Stakeholder invite list is right (people affected by the output should be there)
- [ ] Anything not completed has an explanation and a disposition (carry forward / de-scope / delay)

**During review:**
- Engineering demonstrates (not PM presents). PM provides context.
- Feedback is collected, not immediately acted on. "That's great feedback — let me capture it for prioritization" is the right response to scope requests during demo.
- PM calls out explicitly: what was committed, what shipped, what didn't ship and why.

**The review anti-pattern:** Demo sessions that become scope requests. The review is for showing what was built. New work goes through the backlog.

---

## Sprint Retrospective (Last Day, 45-60 min)

**Purpose:** Improve the team's way of working. Not a blame session, not a status report.

**PM responsibilities:**
- Create psychological safety: retros where PM dominates produce less honest feedback
- Prepare 2-3 specific observations from the sprint (what worked, what didn't, a specific pattern noticed)
- Participate as a team member, not a manager

**Retro format (PM-facilitated when needed):**
1. Reflect (10 min): each person writes 3 cards — What went well / What was hard / What would I change
2. Share (15 min): read cards, cluster similar themes
3. Prioritize (5 min): vote on top 2 themes to discuss
4. Discuss (20 min): for each theme — what's the root cause? what would we do differently?
5. Commit (10 min): 1-2 specific, owned action items for next sprint

**The retro output:** 1-2 specific, actionable changes to be made in the next sprint. Not aspirational principles — concrete mechanics. "We'll put acceptance criteria in all stories before planning" not "We'll communicate better."

---

## Backlog Grooming (Mid-Sprint, 60-90 min, bi-weekly)

**Purpose:** Ensure the next sprint's stories are ready before sprint planning. Prevents "planning theater" where requirements are figured out in the planning meeting.

**PM responsibilities before grooming:**
- [ ] New stories written and in the backlog
- [ ] Stories for next sprint have draft acceptance criteria
- [ ] Dependencies mapped
- [ ] Rough priority order set

**During grooming:**
- Engineering raises technical questions; PM answers or commits to an answer date
- Stories are estimated (roughly — not binding commitment)
- Stories that aren't ready are flagged and returned to PM for completion
- "Not ready" is a legitimate outcome — it's better than planning from an incomplete story

**Grooming output:** A "ready" backlog of 2-3 sprints of work, with the next sprint fully specified.

---

## Sprint Metrics (PM Tracking)

| Metric | What it tells you | Healthy range |
|---|---|---|
| Sprint commitment rate | % of committed scope shipped | >80% consistently |
| Sprint goal completion | Did we achieve the sprint outcome? | >85% |
| Carry-forward rate | % of tickets carrying across 2+ sprints | <15% |
| Acceptance criteria change rate | % of stories with AC changed mid-sprint | <10% |
| Blocker days | Total days blocked on PM decisions | <1 day/sprint |

**The carry-forward signal:** Items carrying across 2+ sprints are either: too large (split them), blocked (surface the block), or mis-prioritized (de-scope them). Never let a carry-forward continue without a diagnosis.

---

## Sprint Anti-Patterns

**The sprint dump:** Loading a sprint with 20 tickets because "we might get to them." Commitment should be to the goal, not to maximum throughput. Loaded sprints produce incomplete stories, not more shipping.

**Acceptance criteria written post-development:** If engineering is writing AC after the code is written, the story was never specified. AC written post-development is not criteria — it's documentation of what was built.

**The PM as project manager:** Using sprint ceremonies to track individual developer progress. Standups are for surfacing blockers, not status reporting. If PM is asking "how's ticket X going?" in standup, they're using the wrong tool.

**The surprise demo:** Engineering showing the demo to PM for the first time in the review meeting. PM should have seen the work at least once mid-sprint. If the demo is a surprise, the sprint had insufficient PM engagement.
