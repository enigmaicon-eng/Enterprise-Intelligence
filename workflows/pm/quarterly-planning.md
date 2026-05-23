# Quarterly Planning
## The Ritual That Turns Strategy Into Funded Commitments

Quarterly planning is not estimation theater. It is the moment when strategy assumptions become resource bets and organizational alignment becomes visible or not. A quarterly plan that doesn't reflect honest trade-offs is a calendar, not a plan.

---

## The Quarterly Planning Sequence

Six phases. Each has a distinct output that becomes input to the next.

---

### Phase 1 — Strategy Checkpoint (Week -4)

**Before planning what to build, check whether the strategy is still right.**

Run the strategy stress test from `knowledge/pm/product-strategy.md`:

1. **Competitor test:** Can you name three moves a competitor could make that would undermine your H2 bets? If not, you don't understand the competitive landscape well enough to plan.

2. **User test:** In the last 90 days, has anything you learned from users changed what problem you're solving or for whom? If discovery is confirming everything, the questions are wrong.

3. **Engineering test:** What technical decisions made this quarter create future constraints that aren't reflected in the roadmap? Debt, dependencies, platform limitations.

4. **Kill test:** Which H2 bets have hit their kill criteria? Call it before planning a second quarter of investment.

**Output:** Strategy update memo — 1 page max. What changed, what didn't, what that means for this quarter's priorities. This memo goes to leadership before roadmap discussions start.

---

### Phase 2 — Input Collection (Week -3)

**Gather signals before opinions.**

**What to collect:**

| Source | What to extract |
|---|---|
| Discovery conversations (last quarter) | Unresolved user problems, shifting priorities, new evidence |
| Metrics review (last quarter) | Leading indicators vs. lagging, what grew / what stalled |
| Engineering: tech debt and platform state | What slows us down that's getting worse? |
| Sales / CS: win/loss themes | What did we miss? What competitor narrative is working? |
| OKR retrospective | Which key results moved? What explains the gap? |
| Stakeholder input (1:1s this phase) | What are they worried about? What commitment do they need? |

**Format:** Raw notes only — no filtering at this stage. Synthesis happens in Phase 3.

**Anti-pattern:** Collecting input as a compliance exercise and not actually changing priorities based on it. If input collection never changes anything, stakeholders learn to stop giving real input.

---

### Phase 3 — Prioritization Session (Week -2)

**Run the prioritization playbook from `decision-frameworks/pm/prioritization-playbook.md`.**

**Before the session:**
- Apply Strategic Alignment Test to all candidate items — kill anything that fails
- Score surviving items on RICE++ (each person independently, before group)
- Prepare the trade-off record: for each top-10 item, name 2 things that drop off

**During the session:**
- Share individual scores; surface divergences
- Each divergence is a different assumption — name the assumption, don't just average the scores
- Explicitly name what you are NOT doing this quarter
- Decision owner calls the outcome

**Output:** Ranked list with trade-off record. Not just what's in — what's out and why. The "out" list is as important as the "in" list.

**The capacity reality check:** Before finalizing, subtract:
- Known holidays and vacations
- Engineering's estimated maintenance/debt allocation (never zero)
- PM time for discovery, stakeholder management, and cross-functional work
- A 15% buffer for unplanned work (if last quarter needed no buffer, you got lucky)

Whatever's left is your real capacity. Size commitments to fit it.

---

### Phase 4 — Roadmap Drafting (Week -2)

**Structure the quarter's work into a communicable plan.**

**Quarterly roadmap format:**

```
QUARTER: Q[N] YYYY
STRATEGY CONTEXT: [One sentence — what strategic moment is this quarter responding to?]

THEME 1: [Theme name — the organizing intent]
  Initiative 1a: [Name] | Owner: [PM/Team] | Confidence: H/M/L | Timing: Month 1-2
  Initiative 1b: [Name] | Owner: [PM/Team] | Confidence: H/M/L | Timing: Month 2-3
  
THEME 2: [Theme name]
  ...

EXPLICITLY NOT THIS QUARTER:
  - [Item] — [one-sentence rationale]
  - [Item] — [one-sentence rationale]
  - [Item] — [one-sentence rationale]

RISKS:
  - [Top 3 risks with P0/P1/P2 and owner]

KILL CONDITIONS:
  - [H2 initiative]: will be killed if [specific observable condition] by [date]

DEPENDENCIES:
  - [External dependency] — [owner] — [needed by date]
```

**Confidence levels matter.** High = this is happening and scoped. Medium = directionally right, details TBD. Low = important but uncertain — we're committing to the problem, not the solution. Don't hide low-confidence items under medium to look more certain.

---

### Phase 5 — Alignment Cascade (Week -1)

**Pre-align before the official planning meeting, not during it.**

**Order of operations:**
1. Engineering lead — does this scope fit the team's capacity? Are there technical blockers we haven't surfaced?
2. Design lead — is there enough design capacity for these initiatives? What needs to start now to be ready for engineering?
3. Sales and CS — what commitment are they making to customers this quarter based on this roadmap? What do they need from us that isn't in the plan?
4. Your manager — does this plan reflect the right strategic priorities from leadership's perspective?

**Each conversation produces:** one adjustment or one explicit acknowledgment of a tension the organization is choosing to carry.

**After alignment:** Write and distribute the one-pager (see template below) 48 hours before the planning meeting.

---

### Phase 6 — Quarterly Kickoff (Week 0)

**The planning meeting is a decision meeting, not a presentation.**

**Agenda:**
1. Strategy update (10 min) — what changed, what we're betting on this quarter
2. Trade-offs (15 min) — walk through what's in AND what's out, with rationale
3. Risks and dependencies (10 min) — P0/P1 risks, who owns mitigation
4. Alignment checks (15 min) — where is there remaining tension? What needs a decision now?
5. Commitments (10 min) — explicit commitments made by each function

**Output:** Signed-off plan document. "Signed off" means: each stakeholder has explicitly acknowledged the plan, including the trade-offs. Silence is not agreement.

---

## The Quarterly One-Pager

Every quarter's plan should fit on one page when communicated externally.

```
Q[N] PLAN: [Product/Team Name]
[Date]

WHAT WE'RE DOING:
[3-4 bullet points — the themes and their intent]

WHAT WE'RE NOT DOING (and why):
[2-3 bullet points — the explicit deferrals]

WHAT WE NEED FROM YOU:
[Function-specific asks — engineering capacity, sales alignment, exec support]

HOW WE'LL KNOW IT'S WORKING:
[3 metrics — the leading indicators we'll track weekly]

BIGGEST RISK:
[One sentence — the thing most likely to derail the plan and what we're doing about it]
```

**Principle:** If a stakeholder reads only the one-pager, they should understand the trade-offs well enough to know when to escalate.

---

## Mid-Quarter Check (Week 6)

**Scheduled checkpoint — do not skip.**

Questions to answer:
- Are the leading indicators moving? If not, is the initiative on track or is the hypothesis wrong?
- Have any kill conditions been triggered?
- Have dependencies been met on schedule? If not, what slips?
- Is capacity tracking as estimated? What adjustments are needed?
- Have any new risks emerged that weren't in the original risk register?

**Output:** A brief written update to stakeholders. "We're on track" is not an update — name what moved, what slipped, what you're watching, and what (if anything) changes.

**When to re-plan mid-quarter:** If >30% of the committed scope has slipped or been redirected, the plan is no longer the plan. Acknowledge it and re-publish rather than carrying the fiction forward.

---

## Quarterly Planning Anti-Patterns

**The commitment theater quarter:** Planning to satisfy the planning process, not to make real bets. Every initiative is medium confidence and medium priority. Nothing gets killed. Nothing hard gets decided. This produces a list, not a plan.

**Capacity inflation:** Planning at 100% engineering capacity without accounting for maintenance, interrupts, vacations, and ramp-up. Reality will hit by week 4 and the quarter becomes a negotiation over what slips.

**Strategy-plan disconnect:** The strategy says "win enterprise" but the roadmap is full of consumer-grade features. If you can't explain how each initiative advances the strategy, the plan doesn't reflect the strategy.

**No kill conditions written:** Initiatives continue past the point of evidence because no one wrote down what "this isn't working" looks like. H2 bets without kill conditions become zombie projects.

**Alignment theater:** Running alignment conversations but not actually adjusting the plan based on feedback. Stakeholders learn that their input doesn't matter and stop giving real input.
