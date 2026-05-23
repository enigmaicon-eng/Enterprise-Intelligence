# Weekly PM Rhythm
## The Operational Cadence That Prevents Chaos

A PM without a weekly rhythm becomes reactive. Every week becomes a new emergency because nothing was tracked or anticipated. The weekly rhythm is the system that turns reactive firefighting into proactive execution.

---

## The Weekly Stack

Five recurring practices. Each has a purpose, a time budget, and an output.

---

### Practice 1 — Monday: Weekly Orientation (30 min)

**Purpose:** Set direction for the week before the week sets direction for you.

**Inputs:**
- Last week's review (if done — see Practice 5)
- Action items from `execution/action-items.md`
- Calendar: what meetings are happening, what's due

**Output (document or mental model):**
- Top 3 outcomes I'm driving this week (not tasks — outcomes)
- The one risk I'm watching most closely
- The one relationship I need to invest in this week
- What I'll defer or say no to if something breaks

**Run as:** `/briefing` command — adds today's critical and focus items

---

### Practice 2 — Tuesday/Wednesday: Discovery Conversations (60-90 min)

**Purpose:** Maintain continuous discovery. Never let the team lose contact with real users.

**Target:** 2-3 user/customer conversations per week. PM + designer when possible.

**Before each conversation:**
- What assumption are we testing today?
- What would tell us the assumption is wrong?

**After each conversation:**
- Document in `meeting-intelligence/raw/` with: what was said, what it means, what (if anything) changes
- Debrief with the designer immediately — while it's fresh
- Flag insights that should update the strategy or roadmap

**Quality check:** If three consecutive weeks of discovery conversations change nothing in your thinking, your questions are wrong.

---

### Practice 3 — Wednesday: Metrics Review (45 min)

**Purpose:** Let data speak before the week's narrative solidifies.

**Inputs:**
- Dashboard of product health metrics (Layer 2 from metrics stack)
- Experiment results from running tests
- Support ticket volume/category trends

**Output:**
- One insight from the data (not just "metrics are up/down" — what does this mean?)
- One anomaly to investigate (something that doesn't fit the mental model)
- One metric trend that should inform next week's priorities

**Format:** Not a report — a working session. PM + data partner if available. Talk through the numbers; don't just read them.

**Anti-pattern:** Reviewing metrics to confirm your current plan. Review metrics to challenge your current plan.

---

### Practice 4 — Thursday: Stakeholder Pulse (30 min)

**Purpose:** Maintain alignment before misalignment becomes visible.

**Practice:**
- One 1:1 with a key stakeholder this week (rotate through: engineering lead, design lead, sales, customer success, a senior exec)
- Purpose: not status update — understanding what they're worried about, what they need, what they're hearing from their side

**Questions that surface useful signal:**
- "What's the biggest concern you have about how we're executing right now?"
- "What are you hearing from [customers / leadership / your team] that you think I should know?"
- "Is there anything I could change about how we're working together that would help you?"

**Output:** One insight documented in `notes/raw/` with context. If the conversation reveals misalignment, document the next action immediately.

---

### Practice 5 — Friday: Weekly Close (45 min)

**Purpose:** Synthesize the week, extract learnings, set next week up to start well.

**Run as:** `/weekly` command

**Inputs:** All practices from the week, action items, metrics, stakeholder conversations

**Output:** `reviews/weekly/YYYY-WW.md` with:
- What moved vs. what slipped
- Patterns from discovery and metrics
- Strategy-level implications (anything that should update the roadmap or strategy)
- Next week's top 5 priorities with rationale

**Critical discipline:** Don't skip Friday close because the week was rough. The rough weeks produce the most important learnings. The close forces articulation of what happened and why — which prevents the same week from repeating.

---

## Standing Meeting Architecture

These are the recurring meetings that support the weekly rhythm. Each has a purpose and a hygiene standard.

**Sprint planning / Sprint review (bi-weekly)**
- Purpose: align on what's being built, review what was built
- Hygiene: PM arrives with clear priority list and acceptance criteria; no agenda-less planning
- Anti-pattern: planning meeting where requirements are unclear and the team is expected to "figure it out"

**Design review (weekly)**
- Purpose: ensure design decisions align with product intent and user understanding
- Hygiene: PM reviews with specific questions, not general approval; designer presents the problem before the solution
- Anti-pattern: PM seeing design for the first time in the review; no critique culture

**Engineering sync (weekly or bi-weekly)**
- Purpose: surface technical risks, clarify requirements, maintain PM-engineering trust
- Hygiene: PM brings specific questions and open requirements; engineering brings blockers and technical decisions that need PM input
- Anti-pattern: PM using the sync to project-manage rather than to collaborate

**Stakeholder updates (bi-weekly or monthly)**
- Purpose: maintain alignment across functions
- Hygiene: structured format — what we did, what we learned, what's next, what we need
- Anti-pattern: slide-deck status report with no engagement or decision-making

**Strategy review (quarterly)**
- Purpose: check that the strategy is still right given what we've learned
- Hygiene: PM prepares a strategy update that honestly assesses assumptions — not just progress
- Anti-pattern: strategy review that confirms the strategy without examining the assumptions

---

## Calendar Hygiene Rules

**Deep work blocks:** PM needs uninterrupted thinking time. Minimum 2 hours of protected deep work daily. Meetings that don't require the PM should not have the PM.

**The meeting audit:** Quarterly, audit every recurring meeting. For each: what decision or alignment is this producing? If you can't answer clearly, kill it or reduce frequency.

**The pre-read contract:** Any meeting that requires judgment should have a pre-read sent 24h in advance. Meetings without pre-reads produce discussion, not decisions.

**Meeting roles:** For every meeting with a decision involved: who is driving (proposes)? Who is approving (decides)? Who is consulted? A meeting where this is unclear will produce follow-up meetings.

---

## Weekly Rhythm Anti-Patterns

**Discovery skipping:** "We don't have time for user conversations this week." Discovery is maintenance, not optional. Skipping it is like skipping car maintenance — the cost appears later, larger.

**Metrics reporting vs. metrics thinking:** Reviewing metrics to produce a status slide is not the same as thinking with metrics. The output of metrics review should be an insight, not a number.

**The perpetual carry-forward:** Action items that have been in the system for 3+ weeks and keep getting carried. These are either: actually low priority (remove them), blocked (escalate the block), or too vague (rewrite as a specific action with a specific owner).

**No Friday close:** Skipping the weekly review because you're tired or behind. This is exactly when you need the reflection — the worst weeks are the ones with the most to learn.
