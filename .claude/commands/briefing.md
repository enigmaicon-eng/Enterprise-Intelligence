---
name: briefing
description: >-
  Generates the daily operational briefing: what's critical, what to focus on,
  what to be aware of. Reads action items and active memory. Outputs to terminal
  only — not written to a file. Trigger on: "briefing", "what should I focus on",
  "what's open", "start my day", "what's on my plate". Do NOT use for weekly
  review (use /weekly), monthly strategy (use /synthesize), or workspace health
  (/observe).
---

# Daily Briefing

Produce a focused, scannable briefing for the current session. Speed matters — this should complete in one Claude call.

## Inputs Required

Read these files before generating output:

1. `execution/action-items.md` — open items, due dates, priorities
2. `memory/MEMORY.md` — identify which memory files are relevant
3. The 1-2 memory files most relevant to current priorities (project + user profile)

Do not read meeting files, knowledge files, or strategy files for a briefing. Scope is today.

## Workflow

1. Read `execution/action-items.md`. Separate into: overdue / due today / this week.
2. Read memory files. Extract: active projects + their current phase, stated top priorities.
3. Identify top 3 focus items: highest-priority open items aligned with active project phases.
4. Check for any meetings or follow-ups flagged in action items for today.
5. Generate the briefing in the output format below.
6. Do not write to any file. Output to conversation only.

## Output Format

```
## Briefing — [YYYY-MM-DD]

### Critical
[Overdue items or items due today. If none: "Nothing overdue."]
- [ ] ITEM — due DATE — source

### Focus
[Top 3 items ranked by priority × strategy alignment. No more than 3.]
1. ITEM — why this, not something else (one clause)
2. ITEM — why this
3. ITEM — why this

### Heads-Up
[Meetings today with brief context, or pending async follow-ups. If none: omit section.]
- ITEM
```

## Quality Gate

- [ ] Critical section shows only truly overdue or due-today items — not "soon"
- [ ] Focus has exactly 3 items, each with a one-clause rationale
- [ ] No items appear in both Critical and Focus
- [ ] Total output fits in one screen (under 30 lines)
- [ ] Nothing written to disk — this is ephemeral output only
