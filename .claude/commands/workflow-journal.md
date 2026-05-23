---
name: workflow-journal
description: >-
  Quick daily or session-end journal entry. Logs what was worked on, key
  insights, open questions, and tomorrow's seeds. Lightweight — 5 minutes,
  not a full trace. Writes to traces/journal/YYYY-MM-DD.md and updates the
  journal section of TRACE-INDEX.md. Trigger on: "journal entry", "log today",
  "what did I do today", "session log", "end of day journal", or at
  /shutdown. Do NOT use when you want a full structured trace (use
  /trace-capture) or a formal decision log (use /decide).
version: 1.0
output: traces/journal/YYYY-MM-DD.md + TRACE-INDEX.md
---

# /workflow-journal

Quick daily session log. The goal is operational continuity — the next session (or next week) opens with a clear picture of where things stand, without re-reading everything.

## When to Use

- At the end of any meaningful work session
- When /shutdown is running and there's something worth preserving
- When a key insight lands mid-session and you want to lock it in
- When you want to note an open question to pick up next time

**Do NOT use for:**
- A full workflow trace (that has decisions, sequences, artifacts) → `/trace-capture`
- Logging a formal decision with rationale → `/decide`
- Capturing a meeting → `/debrief`

## Inputs Required

- Operator's brief description of the session (what was worked on)
- Any notable insights or blockers to log

## Workflow

**Step 1 — Determine the journal file.**

Check if `traces/journal/YYYY-MM-DD.md` exists for today. If yes, append to it. If not, create it.

**Step 2 — Gather journal content.**

Collect from the operator (or infer from the session if context is clear):
- **Worked on:** what was the main focus?
- **Key insight:** one sentence — what's the most important thing that landed today?
- **Open question:** what's unresolved and worth picking up next time?
- **Tomorrow seed:** one specific thing to start with next session

If the operator provides these upfront, don't ask again. Write directly.

**Step 3 — Write the journal entry.**

Format:

```markdown
## [HH:MM] Session — [brief label]

**Worked on:** [what was done]

**Key insight:** [one sentence]

**Open question:** [what's unresolved]

**Tomorrow seed:** [specific next action]
```

If this is the first entry of the day, add a date header:
```markdown
# YYYY-MM-DD

## [HH:MM] Session — [brief label]
...
```

If appending to an existing file, add a `---` separator before the new session block.

**Step 4 — Update the index.**

Append or update one row in the Journal Entries table of `traces/TRACE-INDEX.md`:

```
| YYYY-MM-DD | [session focus, <6 words] | [key insight, <10 words] | [tags] |
```

If a row for today already exists, update it in place (append the new session focus if multiple sessions occurred).

**Step 5 — Suggest trace capture if warranted.**

If the session description suggests high reuse potential:

```
This session sounds like it may be worth a full trace.
Run /trace-capture to record the full execution sequence and decisions.
```

Do not force this — only suggest if reuse potential is clearly high.

## Output Format

```
Journal entry written: traces/journal/YYYY-MM-DD.md
  Session : [label]
  Insight : [key insight]
  Seed    : [tomorrow's seed]
```

## Quality Gate

- [ ] Entry written to correct date file
- [ ] Key insight is one sentence — specific, not generic
- [ ] Tomorrow seed is actionable (a verb phrase, not a topic)
- [ ] TRACE-INDEX.md journal row updated
- [ ] Separator (`---`) added if appending to an existing day file
