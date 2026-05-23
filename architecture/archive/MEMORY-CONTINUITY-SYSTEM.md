# Memory Continuity System
## Selective Loading, Session Threading, and Persistent Context

---

## The Core Problem

Memory without selection is noise. Loading all memory files at every session start:
- Wastes tokens on irrelevant context
- Dilutes attention across stale projects
- Creates the illusion of awareness without the substance

The goal is selective continuity: at any point in a session, exactly the right context is active — no more, no less.

---

## Memory Relevance Model

Every memory file has a topic domain. Match the user's current intent to the relevant domain:

| User Intent Domain | Memory Files to Load |
|-------------------|---------------------|
| Any session start | `memory/MEMORY.md` (index always loaded) |
| User preferences and working style | `memory/user_profile.md` |
| Any active project mentioned | `memory/project_<name>.md` |
| Behavioral patterns or feedback | `memory/feedback_*.md` |
| External tool or system reference | `memory/reference_*.md` |

**Default load at session start:** `MEMORY.md` index + `user_profile.md` + any project file matching the session's likely focus. That's 2-3 files, ~800-1,200 tokens, leaving the rest of the context for actual work.

---

## Session Continuity

How to treat each session as continuation, not cold start:

### At Session Start
1. Read `memory/MEMORY.md` — scan for active projects and recent threads
2. Read `user_profile.md` — orient to user's domain and working style
3. Identify the session's likely domain from the opening message
4. Read the relevant project file if one matches
5. Don't read more until a workflow requires it

### During Session
- When a new project or initiative is named: check if a project file exists; read it if so
- When a decision question arises: check `decision-frameworks/decisions-log.md` for prior decisions on that topic
- When synthesis is needed: check `synthesis/` index for prior relevant work before generating fresh

### At Session End
If any of these happened, update memory:
- New project emerged → create `memory/project_<name>.md`
- Behavioral feedback was given → update or create `memory/feedback_*.md`
- A project phase changed → update the project file
- New reference system or tool was introduced → update `memory/reference_*.md`

**Rule:** Only persist what would be valuable in a different session, weeks from now. Ephemeral session context stays in conversation, not memory.

---

## Continuity Types

### Project Continuity
Active projects maintain state across sessions. Each project file tracks:
- Current phase and milestone
- Key constraints and non-negotiables
- Active blockers
- Next action (one concrete next step)

When a user picks up a project thread, the project file ensures they don't need to re-explain context they've already established.

**Staleness trigger:** A project file's phase hasn't changed in >3 weeks. Either the project is stuck, deprioritized, or the file needs updating.

### Decision Continuity
Settled decisions should not be re-litigated. Before recommending an option, check:
- Is there an entry in `decision-frameworks/decisions-log.md` on this topic?
- If yes: surface the prior decision, state when it was made, note its review date
- Don't override past decisions without surfacing that you're doing so

**How to check:** When the user asks about a topic where a decision was likely made, grep `decisions-log.md` for relevant terms before answering.

### Strategic Continuity
Long-horizon goals remain visible even when day-to-day work is tactical. This is maintained via:
- `memory/user_profile.md` — captures the user's current strategic focus areas
- Weekly review (`reviews/weekly/`) — connects tactical work to strategic direction
- Monthly synthesis — surfaces drift between execution and strategy

When answering tactical questions, briefly anchor to strategic context when it's relevant and non-obvious. Don't force it — but don't lose the thread either.

### Knowledge Continuity
Before generating new knowledge (research, analysis, synthesis), check if it already exists:
1. Check `knowledge/KNOWLEDGE-INDEX.md` for the concept or domain
2. If an entry exists, build on it rather than generating from scratch
3. After generating new knowledge, check for connection opportunities (`[[linked-concept]]` references)

This prevents the workspace from developing contradictory or duplicated knowledge over time.

---

## Memory Loading Protocol

```
Opening message arrives
     │
     ▼
Read MEMORY.md index (always)
     │
     ├─ Identify: does this session have a known project focus?
     │    ├─ Yes → read that project file
     │    └─ No → proceed without project file until one becomes relevant
     │
     ├─ Identify: does the user's working style matter for this task?
     │    ├─ Yes (most sessions) → read user_profile.md
     │    └─ No (pure research session) → skip
     │
     └─ Is there feedback that directly applies to this task type?
          ├─ Yes → read relevant feedback file
          └─ No → proceed
     │
     ▼
Task begins with exactly the context needed
```

---

## Memory Update Triggers

Conditions that should produce a memory update before the session ends:

| Trigger | Memory File to Update |
|---------|----------------------|
| New project introduced | Create `memory/project_<name>.md` |
| Project phase changed | Update `memory/project_<name>.md` |
| User explicitly corrected behavior | Create/update `memory/feedback_<topic>.md` |
| User confirmed an approach worked | Update `memory/feedback_<topic>.md` |
| New external tool/system referenced | Create/update `memory/reference_<tool>.md` |
| User's role or focus area changed | Update `memory/user_profile.md` |
| User explicitly asked you to remember something | Save to appropriate file immediately |

When updating memory, keep the file under 500 tokens. If an update would push it over, compress or split the existing content first.

---

## Memory Continuity Anti-Patterns

| Anti-Pattern | What Happens | Fix |
|---|---|---|
| Reading all memory files at session start | Token bloat, diluted attention | Read MEMORY.md index; load files selectively |
| Never updating memory | Sessions feel like cold starts | Update when triggers fire (see table above) |
| Storing session summaries in memory | Memory fills with conversation history | Memory holds durable facts, not session logs |
| Ignoring past decisions | Re-litigating settled things | Check `decisions-log.md` before recommending |
| Loading stale project files | Context from 6 weeks ago | Check `updated:` date; if >3 weeks, verify with user before relying on it |
| Over-reading context | Consuming tokens for memory you didn't need | Read only what the current task requires |
