# Daily Operations Playbook

## Purpose
The complete guide to running a day with the Enterprise Intelligence Workspace. Everything here maps to specific skills or existing workflows. This is operational, not aspirational.

---

## The Minimum Viable Day

If time, energy, or context is limited, this is enough:

1. `/briefing` — 2 minutes to orient
2. Do your most important commitment
3. `/shutdown` — 5-10 minutes to close

Everything else is additive. The ritual stack doesn't require full execution every day.

---

## How to Run a Full Day

### Morning block (high energy — first 60-90 minutes)

**1. Orient** (2 min)
```
/briefing
```
Critical items, opens from yesterday, today's surface-level priorities.

**2. Plan (when needed)** (5-10 min)
```
/plan
```
Run this when: you have competing priorities, you don't know what to do first, or the week has changed. Skip it when `/briefing` gives you clear direction.

Output: today's theme + top 3 commitments.

**3. Frame the first deep work session** (3-5 min)
```
/focus [what you're working on]
```
Run this before any session requiring sustained concentration. Sets the done condition, loads the right context, names the one risk.

Skip it for: meetings, light reviews, administrative work.

### Execution blocks (work)

**Meetings:**
```
Before: /prep [meeting name]        ← if the meeting warrants preparation
After:  /debrief [meeting file]     ← if the meeting produced decisions or actions
```

**Captures during the day:**
```
/capture [note, thought, action item, reference]
```
Use this for anything that would otherwise stay as a loose thread. Fast path — no synthesis, no routing decisions.

**Decisions:**
```
/decide [decision context]          ← for irreversible or strategically significant decisions only
```
Routine reversible decisions: capture at EOD in `/shutdown`.

**When work is blocked:**
Option 1: Identify the blocker and capture it. Proceed to the next commitment.
Option 2: `/exec-risk [initiative]` — surface and log the risk formally.

**Between contexts — the one-sentence rule:**
Before switching from one problem to another: write one sentence. Where are you, what's the current state, what's the next action. This is the re-entry point. Without it, context restoration costs 5-15 minutes per switch.

### End of day (any energy level — last 10 minutes)

```
/shutdown           ← standard EOD
/shutdown friday    ← Friday EOD with week summary
```

This is the non-negotiable ritual. If you only do one thing, do this.

---

## Workflow Routing by Situation

**"I don't know what to work on"**
→ `/briefing` then `/plan`

**"I have too many things"**
→ `/exec-prioritize` — apply commitment → leverage → reversibility. Max 7 items. No ties.

**"I'm about to go into an important meeting"**
→ `/prep [meeting name]`

**"I just came out of a meeting with decisions and actions"**
→ `/debrief [meeting file]`

**"I need to do a hard thinking task"**
→ `/focus [problem]` then work

**"I have an idea or need to capture something"**
→ `/capture`

**"I made an important decision"**
→ `/decide [decision]`

**"I need to stress-test something I believe"**
→ `/think [claim]`

**"I'm done for the day"**
→ `/shutdown`

**"Something is blocked and I don't know what to do"**
1. Capture the blocker: `/capture blocked on [X] because [Y]`
2. Identify if it's a risk: `/exec-risk [initiative]`
3. Identify if it's a decision: `/decide [what you need to decide to unblock]`

**"I want to learn from what happened today"**
→ Include in `/shutdown` decision sweep, or run `/recall-test` on relevant knowledge entry

---

## Energy-Based Routing

Match cognitive demand to energy state. The system supports all three states.

**High energy → produce**
Use: `/focus`, `/think`, `/pm-strategy`, `/pm-prd`, `/arch-critique`, `/bet`, `/horizon`
Do: original writing, architecture decisions, strategy work, difficult conversations, deep analysis

**Medium energy → process**
Use: `/plan`, `/prep`, `/exec-review`, `/decision-review`, `/pm-prioritize`
Do: meetings, reviews, planning, stakeholder work, refining existing work

**Low energy → file and clear**
Use: `/capture`, `/recall`, `/debrief`, `/learn`, `/shutdown`
Do: processing outputs from earlier, routing captured items, filing and organizing

**Depleted → stop**
Do not make decisions. Do not write strategy documents. Run `/shutdown` and close. The cost of low-quality work in a depleted state is higher than the cost of not doing it.

---

## Meeting System

| Scenario | Skill | Time | When |
|---|---|---|---|
| Creating a meeting | `/pm-agenda` | 10-15 min | When you're running it |
| Preparing for a meeting | `/prep` | 5-10 min | When preparation changes outcome |
| Processing a meeting | `/debrief` | 10-15 min | After any meeting with outputs |
| Preparing your exec update | `/pm-exec-brief` | 10-15 min | When audience is senior |

Meeting preparation rule: only prepare when preparation changes the outcome. Not every meeting gets `/prep`. High-stakes decisions, strategy reviews, customer conversations, escalations: always prepare. Weekly standups you run regularly: skip prep.

---

## Context Switching Protocol

Context switches are expensive. The protocol keeps the cost low:

**Before switching:**
Write one sentence: where you are + current state + next action.
Example: "Mid-way through Q3 roadmap narrative intro; next: write the second paragraph arguing for the H1/H2 balance rationale."

**Context load ceiling:**
Maximum 3 files per task. If you need more: the task scope is too large, or you're doing the wrong task.

**Batch context switches:**
Don't switch contexts 8 times in a day. Group similar work into blocks. Context switching has a 5-15 minute restoration cost per switch — 8 switches = up to 2 hours lost.

---

## Prioritization Quick Reference

Prioritization hierarchy (from `architecture/DAILY-OPERATING-SYSTEM.md`):
1. **Commitment** — what did you tell someone you'd do?
2. **Leverage** — what unblocks the most downstream work?
3. **Reversibility** — what, if not done now, forecloses options?

Top 3 rule: name 3 commitments maximum per day. The list doesn't help you. Three named commitments do.

If competing for position: commitment beats leverage beats reversibility. If tied on hierarchy level: choose the one that takes less time first (get it off the plate).

---

## Learning Workflows

**After a book, article, or course:**
```
/learn [source]
```
→ Produces structured knowledge entry + connections + open questions

**After a meeting with insight:**
→ `/debrief` surfaces knowledge candidates
→ Follow up with `/promote` if candidate is worth elevating

**Recall maintenance:**
```
/recall-test [entry]    ← within 48h of writing a new entry
/recall-test            ← weekly for entries reviewed >30 days ago
```

**Cross-domain synthesis:**
```
/insight                ← after 3+ entries in same domain, or after a bet closes
```

---

## Weekly Cadence Integration

| Day | Ritual | Skill | Time |
|---|---|---|---|
| Monday | Week orientation | `/briefing` + `/plan weekly` | 10-15 min |
| Monday | Execution review | `/exec-review weekly` | 10-15 min |
| Monday | Knowledge review | `/weekly` | 10-15 min |
| Daily | Session orientation | `/briefing` | 2 min |
| Daily | EOD closure | `/shutdown` | 5-10 min |
| Friday | Week close | `/shutdown friday` | 10-12 min |

Do not add more recurring rituals. If the above feels like too much: drop `/plan weekly` and consolidate Monday into briefing + exec review only.

---

## When the Day Goes Off-Plan

Off-plan days are normal. The system handles them.

**Reactive day (meetings/fires all day):**
- `/briefing` in the morning — minimum viable
- `/capture` for anything that surfaces
- `/shutdown` at end — capture the decisions and opens
- Do not try to salvage focus time if it's gone. Accept the day for what it was.

**Low output day:**
- `/shutdown` regardless — the EOD seed for tomorrow is the most valuable thing you can do
- Do not compensate by working late into low-energy time. Sleep wins.

**Overcommitted day:**
- Run `/exec-prioritize` — apply the hierarchy, trim to 3
- Communicate clearly about what slips
- Log the scope decision: "Chose to drop X in favor of Y because commitment beat leverage today"

---

## Anti-Patterns

| Anti-pattern | Signal | Correction |
|---|---|---|
| Ritual theater | Running `/plan` but doing something different | If you don't use the output, stop producing it |
| Checklist maximalism | Running 6 rituals before starting work | Morning ritual stack: max 15 min total |
| Productivity tracking | Counting tasks completed | Count commitments delivered, not tasks done |
| Skipping shutdown | "I'll catch up tomorrow" | Tomorrow's you pays the startup cost. Shutdown now. |
| Energy mismatch | Deep work when depleted | Stop. Route to low-energy task or shutdown. |
| Context overload | Loading 5+ files before every task | 3-file ceiling. Trust the architecture. |
| Capture hoarding | Captures accumulating without routing | Weekly review routes captures. Don't batch more than 7 days. |
