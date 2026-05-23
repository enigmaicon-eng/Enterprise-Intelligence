# /plan — Morning Planning

## Purpose
Set today's operational theme and name the top 3 commitments. Extends `/briefing` with intentional framing. Not a schedule — a compass. Run this when you need to think before you act; skip it when `/briefing` is sufficient.

## Trigger Signals
- User invokes `/plan`
- User invokes `/plan weekly` (Monday weekly planning variant)
- User says "I need to plan today" / "what should I focus on" / "help me plan my week"
- Do NOT trigger if user just ran `/briefing` and already has clear direction

## Modes

**Daily (default):** Today's theme + top 3 commitments + one risk flag
**Weekly (`/plan weekly`):** Week theme + top 3 week commitments + one strategic dependency

---

## DAILY PLANNING

### Step 1: Load context
Read in order, stop when you have enough:
1. `memory/MEMORY.md` — orient to what's active (already loaded at session start if /briefing ran)
2. `execution/active-initiatives.md` — current initiative statuses and last-known blockers
3. Any action items surfaced by `/briefing` (if already run, use that output)

### Step 2: Apply the prioritization hierarchy
Using commitment → leverage → reversibility:
- **Commitment:** What did you tell someone you'd deliver today or this week? These come first.
- **Leverage:** What, if done today, unblocks the most downstream work?
- **Reversibility:** What, if not done today, forecloses options?

### Step 3: Set the theme
One word or phrase that names the day's cognitive orientation. Not a task — a frame.

Examples of good themes:
- "Architecture clarity" (a day of design decisions)
- "Stakeholder alignment" (a day of relationship work)
- "Execution push" (a day of output, not thinking)
- "Discovery" (a day of learning and sensing)
- "Recovery and process" (a day of admin and catch-up)

Bad themes: "Meetings" (descriptive, not orienting), "Work" (not useful), "Everything" (the problem, not the theme).

### Step 4: Name the top 3
Three commitments. Not a list — three. If something is important but not in the top 3, it belongs in tomorrow's plan or needs to be delegated/declined.

Format: action verb + specific output + (optional: recipient or deadline)
- Good: "Draft the Q3 roadmap narrative for the review on Thursday"
- Bad: "Work on roadmap"

### Step 5: Flag one risk
One thing that could make the top 3 impossible today. Not a worry list — one specific threat. What's the most plausible blocker?

### Step 6: Set context load decision
Based on the top 3: what files or context will you need? Name them (max 3). Pre-loading the right context before work saves 10-15 min per session.

### Output format
Write to terminal (not file, unless user requests):

```
PLAN — [date]
Theme: [one phrase]

Commitments:
1. [specific output] → [why: commitment | leverage | reversibility]
2. [specific output] → [why]
3. [specific output] → [why]

Risk: [one specific blocker to watch]

Context to load: [1-3 files or topics]
```

---

## WEEKLY PLANNING (`/plan weekly`)

### Step 1: Load context
1. Read `execution/active-initiatives.md`
2. Read `strategy/active-bets.md` — check if any bet has a review due this week
3. Read last week's exec review if available (`reviews/weekly/`)

### Step 2: Set the week theme
Same format as daily theme. One phrase that orients the week.

### Step 3: Name top 3 week commitments
Week-level commitments: things that, if done this week, represent real progress. Not the full list of things you might do — three.

### Step 4: Identify the strategic dependency
One external dependency that could affect the week. Someone else's deliverable, a decision you're waiting on, a bet that has a review trigger this week.

### Step 5: Set one decision threshold
What is the one decision this week that, if delayed, costs more than deciding it sub-optimally? Name it. This is the decision that needs to happen regardless of perfect information.

### Output format:
```
WEEK PLAN — [Week of YYYY-MM-DD]
Theme: [one phrase]

Week commitments:
1. [output] → [initiative ID if applicable]
2. [output]
3. [output]

Strategic dependency: [what / from whom / when]
Decision threshold: [the decision that can't wait]
```

---

## Constraints
- Produce the plan output before offering any analysis or commentary.
- Do not expand the top 3 beyond 3. If the user lists 5 things, apply the prioritization hierarchy and trim to 3.
- Do not write the plan to a file unless the user asks. It is a working document for the session, not a record.
- If context cannot be loaded (files missing, system not initialized): generate the plan from user input only. Note what couldn't be read.
