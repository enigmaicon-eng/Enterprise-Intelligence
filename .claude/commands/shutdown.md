# /shutdown — End-of-Day Closure

## Purpose
Close the cognitive loop at the end of a work session. Captures opens, logs decisions, seeds tomorrow. The one non-negotiable ritual in the Daily OS. Running it takes 5-10 minutes. Not running it carries an invisible cognitive cost: unfinished loops stay active overnight and degrade next-session startup.

## Trigger Signals
- User invokes `/shutdown`
- User invokes `/shutdown friday` (weekly variant with fuller summary)
- User says "I'm done for the day" / "wrapping up" / "end of day"

## Modes

**Standard `/shutdown`:** Daily EOD sweep (~5-8 min)
**`/shutdown friday`:** Weekly EOD with cumulative summary (~10-12 min)

---

## STANDARD SHUTDOWN

### Step 1: What happened today?
Read `execution/active-initiatives.md`. Ask:
- Which of today's top 3 commitments were completed?
- What unplanned work happened?
- What was started but not finished?

Do not read the user's full session. Ask directly: "Quick summary: what got done, what's open?"

### Step 2: Decision sweep
Ask: "Any decisions made today that should be logged?"

For each decision surfaced:
- Is it reversible and routine? → Skip
- Is it partially reversible or significant? → Log a one-liner to EOD capture
- Is it irreversible or strategically significant? → Log via `/decide` immediately

### Step 3: Open items sweep
What opened today that isn't captured anywhere?
- Commitments made to others (things you said you'd do)
- Things you learned that belong in the knowledge base
- Action items from meetings not yet debriefed

Route each:
- Action item → mental note or `/capture` in 10 seconds: "Do [X] by [when]"
- Knowledge candidate → flag for `/learn` or `/promote` tomorrow
- Debrief needed → flag: "Debrief [meeting name] tomorrow"

### Step 4: Tomorrow seed
One sentence: "Tomorrow I start with ___."

This is not a full plan. It is the first action of tomorrow, pre-loaded into working memory. It eliminates the startup cost of "what do I do first?"

The seed should be specific and actionable. Not "work on the roadmap" — "Open the Q3 roadmap doc and write the first two paragraphs of the narrative."

### Step 5: Write the EOD capture
Write a brief EOD capture. Format (internal to session, not necessarily filed):

```
EOD — [date]

Done:
- [what actually completed]

Open:
- [what's still running]

Decisions:
- [any that should be logged — route via /decide if needed]

Tomorrow starts with:
[one specific action]
```

### Step 6: File or discard
Ask: "File this or discard?"
- File → write to `notes/raw/eod-[date].md`
- Discard → the seed sentence is enough; the rest was process

---

## FRIDAY SHUTDOWN (`/shutdown friday`)

Everything in standard shutdown, plus:

### Additional Step: Week summary
Three questions:
1. What was the week's actual theme? (Not what you planned — what it became.)
2. What was the most important thing that happened this week?
3. What do you want to carry into next week?

Format:
```
WEEK CLOSE — [Week of YYYY-MM-DD]
Actual theme: [what it became, not what was planned]
Most important: [one thing]
Carry forward: [one thing — a decision, a question, a thread]
```

This feeds the Monday `/plan weekly`. The week's actual theme vs. planned theme is the most honest signal about where your attention actually went.

### Additional Step: Knowledge flag sweep
Anything from this week that should be promoted to knowledge but wasn't?
- List candidates: "The insight about X from Tuesday's meeting."
- Flag each for `/learn` or `/promote` next week.

Do not do the promotion in the shutdown. Just flag.

---

## Constraints
- Maximum 10 minutes wall time. If the sweep is taking longer: the day had too many loose threads. Note that as a system signal.
- Do not log more than 5 items in any section. If there are more than 5 open items, that's a capacity signal, not a capture problem.
- Do not run `/shutdown` in the middle of the day and restart. Shutdown is a commitment to stopping. If you're taking a break mid-day, don't run shutdown — just capture where you are in one sentence.
- The "tomorrow starts with" seed is required. Everything else is optional if time is short.
