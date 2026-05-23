# /focus — Deep Work Session Framing

## Purpose
Frame a deep work session before starting it. Names the problem, loads only what's needed, states the done condition. Takes 3-5 minutes. Prevents the two most common deep work failures: unclear scope (working on the wrong thing) and context overload (loading too much and losing the thread).

## Trigger Signals
- User invokes `/focus [topic or problem]`
- User says "I need to do deep work on X" / "I'm going to work on X" / "help me set up for X"
- User explicitly wants to start a concentrated work session
- Do NOT trigger for: light tasks, email-style processing, routine reviews, anything that doesn't require sustained concentration

## Input
The topic, problem, or deliverable for this session. If not provided, ask for one sentence: "What are you trying to produce or resolve in this session?"

## Execution Protocol

### Step 1: Name the session
Restate the problem as one specific sentence:
- Not: "Work on the roadmap"
- Yes: "Write the H2 section of the Q3 roadmap narrative — specifically the rationale for de-prioritizing feature X"

If the user's input is too vague, ask one clarifying question: "What specifically will be done at the end of this session that isn't done now?"

### Step 2: Set the done condition
Name the observable output that marks the session as complete:
- A document section written
- A decision made and logged
- A design decision with rationale documented
- A code file modified and tested
- A list of options narrowed to one recommendation

The done condition should be completable in 60-90 minutes. If it isn't: scope it down. What's the minimum version that would still be valuable?

### Step 3: Load context (maximum 3 items)
Based on the session topic, identify the 1-3 files or pieces of context needed:
- The relevant initiative file from `execution/active-initiatives.md`
- The specific knowledge entry from `knowledge/`
- The specific document being worked on

List them. Read them. Do not read anything else.

If more than 3 files seem necessary: the session scope is too large. Split into two sessions with a break between.

### Step 4: Name the one risk to the session
One thing that could derail this session's focus:
- A person likely to interrupt
- An answer you don't have that you'll need to fabricate
- A dependency on something not done yet
- An emotional resistance to the content

Name it. Do not solve it — naming it creates the awareness that prevents it from being acted on unconsciously.

### Step 5: Output the session frame

```
FOCUS SESSION — [date] [time if known]
Problem: [specific sentence]
Done condition: [observable output]

Context loaded:
- [file 1]
- [file 2 if needed]
- [file 3 if needed]

Session risk: [one thing to watch]

Start here: [first specific action — not "begin writing" but "open [file] and write [specific part]"]
```

### Step 6: Optional — post-session close
When the user signals they're done with the session, run a 60-second close:
- Done condition met? Yes | Partial | No
- One sentence on current state (for re-entry)
- Any captures to route (decisions, opens, knowledge candidates)

---

## Deep Work Session Rules (enforce these if violated)

These aren't in the output — they're behavioral rules the skill enforces:

**Single problem.** If the user tries to fold a second problem into the session during framing, name it and park it: "That's a second problem. Capture it for the next session."

**Context ceiling.** If the user lists 4+ files as needed: "You've named 4 context items. Deep work with >3 context sources usually splits attention. Which 2-3 matter most for the done condition?"

**Vague done condition.** If the done condition is a process ("work on the roadmap") rather than an output ("draft the H2 section"): push back once. "That's a process, not a done condition. What will exist at the end of the session that doesn't exist now?"

**Energy check.** If the user signals low energy while trying to start a deep work session: "Deep work when depleted produces poor output. Consider `/shutdown` or a lighter task. What's your energy level?" Do not override — just surface it once.

## Constraints
- The session frame should be produced in 3-5 minutes. This is framing, not planning.
- Do not generate an outline, a writing plan, or a full research summary. Those are outputs of the session, not inputs to it.
- Do not run the work yourself unless the user asks. `/focus` frames the session; the user does the work.
