# Discovery Sprint
## A Dedicated 1-2 Week Cycle for High-Intensity Problem Exploration

A discovery sprint is used when the team faces a significant unknown that must be resolved before committing to a build sprint. It is not a research phase that happens before a project — it is a time-boxed, outcome-oriented cycle that produces a specific deliverable: a decision about whether and how to proceed.

Discovery sprints are triggered by genuine uncertainty. If the team already knows what to build, a discovery sprint is waste. If the team is using discovery as a way to delay a decision they're afraid to make, that's also waste.

---

## When to Run a Discovery Sprint

**Run a discovery sprint when:**
- A significant initiative has a core assumption that hasn't been validated and is high-risk
- The team has conflicting mental models about the user problem and needs external evidence to resolve them
- Multiple solution approaches are being considered and qualitative/quantitative data would differentiate them
- A strategic bet is being made for the next quarter and the problem space needs fresh exploration
- An existing feature is underperforming and the root cause is unclear

**Do NOT run a discovery sprint when:**
- The problem is already well understood and the team just needs to prioritize solutions
- The discovery is a stalling tactic (if the business case is wrong, discovery won't fix it — have the conversation)
- Time-to-market pressure means learning won't change the decision anyway
- The question can be answered with existing data in <1 day

---

## Discovery Sprint Structure

### Day 1-2: Frame and Focus

**Kickoff (2 hours, PM + designer + 1 engineer):**

1. **State the uncertainty:** "We don't know [X]. This matters because [impact on the roadmap/strategy]."
2. **Define the specific question:** One primary question the sprint will answer. Not "understand the user better" — "validate whether [specific assumption] is true for [specific segment]."
3. **Define success for the sprint:** "At the end of 5 days, we will know [specific thing] well enough to make a decision about [specific action]."
4. **List current assumptions:** Write every assumption the team is making. Don't filter — write them all. Then prioritize by: uncertainty × consequence. The highest-priority assumptions are what the sprint targets.
5. **Agree on methods:** Given the question, which research methods will produce the most useful signal? (See `knowledge/pm/user-research-methods.md` for method selection.)

**Recruiting and scheduling (parallel to kickoff):**
- If interviews are needed: begin recruiting immediately. 5+ participants takes 2-3 days to schedule.
- If analytics are needed: confirm data access and query setup on Day 1.
- If competitive analysis: assign and timebox.

---

### Day 2-3: Research Execution

**Interview track:**
- 3-5 user interviews (60-90 min each)
- PM + designer together whenever possible (two perspectives, richer debrief)
- Debrief within 2 hours of each interview while fresh
- Document: observations verbatim, then interpretations separately

**Analytics track:**
- 1-2 specific analytical questions (not exploratory — specific hypotheses to test)
- Data partner involved from Day 1
- Output: specific quantitative findings, not a general dashboard

**Competitive track:**
- Specific competitive hypotheses to investigate
- Not "understand the competitive landscape" — "verify whether Competitor X has solved [specific problem] and how"

---

### Day 4: Synthesis

**Individual synthesis first (1 hour):**
Each team member reviews their notes independently and writes:
- Top 3 observations (what they saw/heard/measured)
- Top 3 interpretations (what they think it means)
- The one finding that most surprised them

**Group synthesis (2 hours):**
1. Share individual syntheses — no cross-talk until everyone has shared
2. Cluster similar themes across team members
3. Identify the pattern that most changes the team's prior beliefs
4. Resolve conflicts: where do interpretations diverge? What assumption explains the divergence?

**Assumption update:**
Return to the assumption list from Day 1. For each assumption:
- Confirmed: what evidence confirms it?
- Challenged: what evidence contradicts it?
- Insufficient signal: what would we need to confirm or refute this?

---

### Day 5: Decision and Documentation

**The decision (2 hours with broader team):**

Answer the primary sprint question explicitly. No hedging. One of three outcomes:

1. **Proceed as planned:** The hypothesis is validated. The team understands the problem. Move to the build sprint with defined success criteria.

2. **Proceed differently:** The hypothesis was partially wrong. Adjust the solution approach based on what was learned. Proceed to build a modified version.

3. **Stop / pivot:** The hypothesis is invalid. The opportunity doesn't exist as assumed, or the problem is different than expected. Redirect resources.

**The decision document:**
```markdown
# Discovery Sprint Decision — [Topic] — [Date]

**Primary question answered:** [Restate the question]

**Answer:** [One sentence — what is now known]

**Key evidence:**
- [Finding 1 — observation + interpretation]
- [Finding 2 — observation + interpretation]
- [Finding 3 — observation + interpretation]

**Assumption status:**
| Assumption | Status | Evidence |
|---|---|---|
| [Assumption] | Confirmed / Challenged / Insufficient | [Brief] |

**Decision:** Proceed as planned | Proceed differently | Stop/pivot

**If proceed differently:** [What changes]

**If stop/pivot:** [What instead]

**Success criteria for build sprint (if proceeding):**
- Primary metric: [metric + baseline + target]
- Guardrail metrics: [list]

**Open questions still remaining:** [What we still don't know and whether that's acceptable]

**Decision owner:** [Name]
**Attendees:** [Names]
```

---

## Two-Week Discovery Sprint

For complex problems requiring deeper investigation, extend to 2 weeks:

- Week 1: Frame + Research (8-10 interviews, analytics, competitive)
- Week 2: Synthesis + Concept testing + Decision

**Concept testing in Week 2:**
After initial synthesis, create a rough prototype or concept (paper, Figma mockup, verbal description) and test it with 3-5 users. Goal: validate the solution direction before committing engineering resources.

---

## Discovery Sprint Output Files

| Artifact | Location | Owner |
|---|---|---|
| Sprint kickoff frame (assumptions, question, methods) | `meeting-intelligence/processed/` | PM |
| Interview notes (raw) | `meeting-intelligence/raw/` | PM or designer |
| Synthesis document | `meeting-intelligence/processed/discovery-synthesis-YYYY-MM-DD.md` | PM (via `/pm-discovery`) |
| Decision document | `decision-frameworks/decisions-log.md` | PM (via `/decide`) |
| Knowledge candidates | `notes/raw/` flagged for promotion | PM |

---

## Discovery Sprint Anti-Patterns

**The 4-week discovery sprint:** When discovery has no time-box, it expands to fill all available time. A discovery sprint that produces a decision in week 5 is a project that used discovery to avoid the build.

**Confirmatory discovery:** Designing research to confirm a decision already made. If the team started writing PRD before the discovery sprint ended, the sprint was theater.

**The unactionable finding:** "Users find the product confusing" is not an actionable finding. "Users cannot complete [workflow] without abandoning because [specific friction point] requires [information they don't have at that stage]" is actionable.

**Discovery without a decision:** A synthesis document that says "we learned X, Y, Z" but doesn't produce a proceed/stop/pivot decision. The whole point of the discovery sprint is to make a decision.
