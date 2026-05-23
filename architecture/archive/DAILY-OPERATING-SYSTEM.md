# Daily Operating System
## P11 Master Architecture

---

## Purpose

A minimal, sustainable operational structure for daily execution. The Daily OS wraps the existing skill ecosystem with four lightweight rituals, an energy model, and a context-switching protocol. It adds exactly what was missing: daily coherence, EOD closure, meeting preparation, and deep work framing.

**What it is NOT:**
- A productivity system
- A time-blocking framework
- A rigid schedule
- A checklist factory

**What it IS:**
- A cognitive coherence layer
- A context-loading protocol
- A capture discipline
- A closure mechanism

---

## The Four Daily Rituals

All four are optional on any given day. All four take ≤10 minutes. The one that should almost never be skipped is `/shutdown`.

| Ritual | Skill | Trigger | Time | Output |
|--------|-------|---------|------|--------|
| Morning planning | `/plan` | First session, when you need to think before acting | 5-10 min | Today's theme + top 3 commitments |
| Deep work framing | `/focus` | Before any session requiring sustained concentration | 3-5 min | Session scope + done condition + context loaded |
| Meeting preparation | `/prep` | 15-30 min before a meeting that matters | 5-10 min | Pre-read + your role + the decision to make |
| End-of-day shutdown | `/shutdown` | Last action before closing the workspace | 5-10 min | Opens captured + decisions logged + tomorrow seeded |

The existing `/briefing` remains the primary daily orientation (≤2 min). `/plan` extends it when more is needed.

---

## Energy Model

Three energy states. Route work accordingly. The model is descriptive, not prescriptive — you know your energy state; the system responds to it.

**High energy (typically: morning first 2-3 hours)**
Best for: original thinking, architecture, strategy, writing, difficult conversations, deep work sessions
Skills: `/focus`, `/think`, `/arch-critique`, `/pm-strategy`, `/bet`, `/horizon`

**Medium energy (typically: late morning, early afternoon)**
Best for: meetings, reviews, prioritization, stakeholder work, planning
Skills: `/plan`, `/prep`, `/exec-review`, `/exec-prioritize`, `/decision-review`, `/pm-prd`

**Low energy (typically: mid-afternoon)**
Best for: captures, processing, filing, administrative, knowledge work that is reading-only
Skills: `/capture`, `/recall`, `/debrief`, `/learn`, `/misconception` (read-only mode)

**Recovery (depleted)**
Best for: nothing requiring decisions. Run `/shutdown` and close.
Do NOT: make strategy decisions, write key documents, or have difficult conversations.

---

## Daily Cadence (Minimum Viable)

```
[Morning — High energy zone]
1. /briefing          → 2 min   → orient to what's live
2. /plan (optional)   → 5-10 min → set theme + commitments when needed
3. /focus             → 3-5 min  → frame the first deep work block

[Midday — Medium energy zone]
4. /prep (if meeting) → 5-10 min → before any meeting worth preparing for
5. /debrief           → 10-15 min → after any meeting with decisions or actions

[End of day — Any energy level]
6. /shutdown          → 5-10 min → close the loop, seed tomorrow
```

Total ritual overhead: 20-35 minutes on a full day. 7-10 minutes on a minimal day (briefing + shutdown only).

---

## Weekly Cadence Integration

The Daily OS integrates with existing weekly rituals in `execution/RITUALS.md`:

| Day | Existing | Daily OS Addition |
|-----|----------|------------------|
| Monday | `/exec-review weekly` + `/weekly` | `/plan weekly` — set week theme + top 3 week commitments |
| Tuesday-Thursday | `/briefing` + work | `/focus` before key deep work blocks |
| Friday | End of week | `/shutdown friday` — fuller EOD with week summary |

---

## Context Switching Protocol

Context switching is the primary source of cognitive cost in knowledge work. The protocol:

**Before switching contexts:**
1. Write one sentence: where were you, what's the current state, what's the next action.
2. Save it. (This can be a `/capture` or a note in a running session file.)
3. Then switch.

The sentence is not for anyone else. It's the re-entry point. Without it, context restoration costs 5-15 minutes per switch.

**Minimum context load per task type:**

| Task type | Load before starting |
|-----------|---------------------|
| Deep work on active initiative | Read: `execution/active-initiatives.md` entry + most recent exec review |
| Strategy work | Read: `strategy/active-bets.md` + relevant bet file |
| Meeting prep | Read: relevant initiative or topic file |
| Knowledge work | Read: relevant `knowledge/` entry + KNOWLEDGE-INDEX cross-domain connections |
| Routine PM work | Read: `/briefing` output — usually sufficient |

**Maximum context load:** 3 files before starting. If you need more than 3 files to begin, the task scope is too large or the context architecture needs restructuring.

---

## Deep Work Session Architecture

A deep work session is a block of sustained concentration on a single problem. It has four components:

**1. Frame (before):** What is the problem? What is the done condition? What context do I need?
**2. Load (before):** Load the 1-3 files required. No more. Use `/focus`.
**3. Work (during):** Single problem. No captures. No context switches. No routing decisions.
**4. Close (after):** Write one sentence: current state + next action. Save it.

Sessions should be 60-90 minutes. Longer produces diminishing returns for most knowledge work. Shorter isn't deep work — it's reactive work with better framing.

---

## Meeting System

Three meeting states, three different skill invocations:

| Meeting state | Skill | Output |
|---|---|---|
| Before a high-stakes meeting | `/prep` | Pre-read + your role + decision to make |
| After any meeting with outputs | `/debrief` | Actions + decisions + knowledge candidates |
| Creating an agenda for a meeting you're running | `/pm-agenda` | Timed agenda + pre-read brief + decision framing |

**Meeting preparation rule:** Only prepare for meetings where your preparation changes the outcome. Routine standups don't need `/prep`. A strategy review, customer interview, or escalation does.

---

## Prioritization Protocol

Daily prioritization uses the same hierarchy as `/exec-prioritize`:
1. **Commitment** — what did you tell someone you'd deliver?
2. **Leverage** — what, if done, unblocks the most downstream work?
3. **Reversibility** — what, if not done today, forecloses options?

**Top 3 rule:** Name 3 commitments per day maximum. Not the full list — 3. If all 3 are done, the day succeeded. Everything else is bonus.

This is integrated into `/plan`. It is the core output of the morning planning ritual.

---

## Decision Capture Protocol

Decisions made during the day should be captured at EOD, not in the moment. The in-moment cost of stopping to log a decision is too high relative to the benefit. The EOD protocol (`/shutdown`) includes a decision sweep.

Exception: high-stakes, irreversible decisions should be logged via `/decide` immediately. The standard is: if you'll want to know 6 months from now why you made this call, log it now.

**Decision capture threshold:**
- Reversible, routine: log at EOD sweep or skip
- Partially reversible, significant: log at EOD sweep
- Irreversible or strategically significant: log immediately via `/decide`

---

## Compounding Mechanisms

The Daily OS is designed to compound through consistent, minimal inputs:

| Practice | Compounds into |
|---|---|
| `/shutdown` daily → decisions logged | `/decision-review` pattern library grows |
| `/debrief` after meetings → processed intelligence | `/weekly` knowledge review has content |
| `/plan` daily → themes documented | Monthly retro has patterns to surface |
| `/focus` framing → done conditions stated | Execution reviews have observable outputs |
| Context switch sentences → re-entry points | Cognitive overhead drops across weeks |

---

## Failure Modes

| Failure | Signal | Correction |
|---|---|---|
| Ritual theater | Running `/plan` but ignoring the output | If you don't use the plan, stop making it |
| Productivity maximalism | Adding more rituals | Remove, don't add. One habit at a time. |
| Skipping shutdown | Day ends without closure | `/shutdown` is the one required ritual. Make it non-negotiable. |
| Context overload | Loading 5+ files before every task | Use the 3-file maximum. Trust the context architecture. |
| Energy mismatch | Doing deep work when depleted | Stop. Run `/shutdown`. Deep work when depleted is waste. |

---

## File Map

```
architecture/
  DAILY-OPERATING-SYSTEM.md              ← this file

.claude/commands/
  plan.md                                 ← morning planning
  shutdown.md                             ← EOD closure
  prep.md                                 ← meeting preparation
  focus.md                                ← deep work session framing

playbooks/
  daily-operations.md                     ← full daily operations guide

templates/
  daily-plan.md                           ← morning plan output format
  eod-capture.md                          ← EOD capture format

prompts/workflows/
  daily-planning.md                       ← planning prompts
  focus-session.md                        ← deep work prompts

knowledge/operations/
  daily-os-patterns.md                    ← operational patterns from daily usage
```
