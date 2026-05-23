---
name: trace-capture
description: >-
  Captures a structured execution trace for a completed workflow, debugging
  session, architecture decision, PM session, or synthesis run. Records the
  goal, execution sequence, key decisions with rationale, artifacts produced,
  what worked, and what failed. Writes to traces/executions/ and updates
  TRACE-INDEX.md. Trigger on: "capture this trace", "log what I just did",
  "record this workflow", "trace capture", after completing a significant
  session. Do NOT use for quick daily logs (use /workflow-journal) or for
  capturing knowledge concepts (use /learn or /promote).
version: 1.0
output: traces/executions/exec_YYYYMMDD_NNN.md + TRACE-INDEX.md
---

# /trace-capture

Capture a structured execution trace for a completed session. The purpose is to preserve the execution path — decisions, sequence, what worked, what failed — so it can be retrieved and reused when doing similar work later.

## When to Use

- After completing a multi-step workflow (especially if it took >30 min)
- After a debugging session where you found the root cause
- After an architecture or build session that produced reusable patterns
- After a PM session with significant decisions logged
- When reuse potential feels medium or high

**Do NOT use for:**
- Quick daily logs → `/workflow-journal`
- Capturing a knowledge concept → `/learn` or `/promote`
- Logging a single decision → `/decide`

## Inputs Required

- Description of the session (provided by operator in the invocation message)
- Optional: reference to any workflow plan file or session artifacts

## Workflow

**Step 1 — Determine the trace ID.**

Read `traces/TRACE-INDEX.md`. Find the highest exec number for today's date and increment. If no traces today, use `exec_YYYYMMDD_001` where YYYYMMDD is today's date.

**Step 2 — Gather session details.**

If the operator has not already provided full details, ask for:
- Session type: workflow | debug | architecture | pm-session | synthesis | build
- Goal: what were you trying to accomplish?
- Outcome: completed | partial | abandoned | failed
- Approximate duration

Then ask the operator to walk through: execution sequence, key decisions, artifacts produced, what worked, and what failed. One clarifying question at a time if needed — do not overwhelm with a form.

**Step 3 — Assess reuse potential.**

Based on what was described, assess reuse_potential as:
- `high` — a specific repeatable workflow with clear steps and transferable decisions
- `medium` — some transferable elements but heavily context-specific
- `low` — highly one-off; capture for completeness but unlikely to recall

**Step 4 — Write the trace file.**

Use `templates/execution-trace.md`. Write to `traces/executions/exec_YYYYMMDD_NNN.md`.

Fill in all sections. For "Pattern Candidates," identify any elements that appeared to be recurring — flag them as unchecked checkboxes. Don't draft the pattern yet; just flag the candidate.

**Step 5 — Update the index.**

Append one row to the Execution Episodes table in `traces/TRACE-INDEX.md`:

```
| exec_YYYYMMDD_NNN | YYYY-MM-DD | [type] | [goal, <8 words] | [outcome] | [reuse] | [tags] |
```

**Step 6 — Surface pattern candidates.**

If any pattern candidates were flagged in the trace:

```
Pattern candidate flagged: "[description]"
This is the [Nth] time a similar element has appeared.
Run /pattern-mine to codify it → or defer until 2+ instances accumulate.
```

## Output Format

```
Trace captured: exec_YYYYMMDD_NNN
  Type     : [type]
  Goal     : [goal]
  Outcome  : [outcome]
  Reuse    : [high/medium/low]
  Artifacts: [count] files
  Patterns : [N] candidates flagged
  File     : traces/executions/exec_YYYYMMDD_NNN.md
  Index    : TRACE-INDEX.md updated
```

## Quality Gate

- [ ] Trace ID is unique and follows `exec_YYYYMMDD_NNN` format
- [ ] All template sections filled (no empty required fields)
- [ ] Key decisions include rationale, not just the choice made
- [ ] "What failed" section is honest — not left blank if anything went wrong
- [ ] Pattern candidates are flagged if any recurring elements were observed
- [ ] TRACE-INDEX.md row appended with correct columns
