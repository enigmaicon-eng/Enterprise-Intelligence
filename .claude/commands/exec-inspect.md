---
name: exec-inspect
description: >-
  Deep structured inspection of a single execution trace. Reads a specific
  exec_YYYYMMDD_NNN file and surfaces a scannable breakdown: timeline, decision
  map, artifacts, failures, pattern candidates. Trigger on: "inspect exec_...",
  "show me this trace", "what happened in exec_...", "read trace exec_...",
  "inspect execution [ID]". Do NOT use for searching across traces (use
  /trace-search) or recalling before upcoming work (use /trace-recall).
version: 1.0
output: terminal
---

# /exec-inspect

Read a specific execution trace and present it as a structured, scannable briefing. The goal is clarity over completeness — pull out what matters, not a raw file dump.

## Inputs Required

- Trace ID: `exec_YYYYMMDD_NNN` (required)

If no ID is provided: read `traces/TRACE-INDEX.md` and surface the 5 most recent Execution Episodes for the operator to choose from.

## Workflow

**Step 1 — Validate the trace ID.**

Read `traces/TRACE-INDEX.md`. Confirm the requested exec ID appears in the Execution Episodes table. If it does not exist, say so and list the 5 most recent IDs from the table.

**Step 2 — Load the trace.**

Read `traces/executions/<exec-id>.md`.

**Step 3 — Extract and present the inspection.**

```
Execution Inspect — [exec-id]
══════════════════════════════

Overview
  Goal    : [goal]
  Type    : [session_type]
  Outcome : [outcome]  ([duration])
  Date    : [date]
  Reuse   : [reuse_potential]
  Tags    : [tags]

Timeline
  [For each step in Execution Sequence section, numbered:]
  [N]. [step description]
       [If artifact noted at this step: → artifact path]

Key Decisions
  [For each decision block in Key Decisions section:]
  • [Decision name or label]
    Chose  : [what was decided]
    Over   : [alternative considered — or "not recorded"]
    Because: [rationale]

Artifacts Produced
  [List each artifact with path and description]
  [If none: "No artifacts recorded."]

What Worked
  [Bullet per item from "What Worked" section — or "Not recorded."]

What Failed / Would Do Differently
  [Bullet per item — or "Nothing flagged." if section is empty]

Pattern Candidates
  [List each checkbox item from Pattern Candidates section with its status]
  [ ] [candidate description]  ← open
  [x] [candidate description]  ← actioned
  [If none: "No pattern candidates flagged."]

Links
  [Related traces, knowledge entries, patterns — or "None recorded."]
```

**Step 4 — Offer next actions.**

```
Next actions:
  /pattern-mine               — codify a flagged candidate above
  /trace-recall [goal]        — find traces with a similar goal
  /failure-review             — analyze failures across all traces
```

## Quality Gate

- [ ] Trace ID validated against TRACE-INDEX.md before the trace file is loaded
- [ ] Output is structured — not a raw YAML/markdown file dump
- [ ] "What Failed" section shown explicitly even when empty — surfaces the gap
- [ ] Pattern candidates shown with their checkbox state (open vs. actioned)
- [ ] If trace ID not found: says so clearly and lists recent IDs from the index
- [ ] If no ID provided: lists 5 most recent from index before asking to choose
