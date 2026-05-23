---
name: pattern-mine
description: >-
  Scans recent execution traces to detect recurring elements, then drafts
  a pattern entry or execution primitive for operator review and approval.
  Two-gate process: detect candidates, then codify the chosen one. Trigger on:
  "mine patterns from traces", "what patterns do I have", "codify this
  pattern", "detect patterns in my traces", "turn this into a primitive",
  or after /trace-capture flags 2+ pattern candidates. Do NOT use for
  knowledge pattern detection (use /pattern) or for creating a full new
  skill (use /skill-new — this is a prerequisite step).
version: 1.0
output: traces/patterns/pat_<slug>.md OR traces/primitives/prim_<slug>.md + TRACE-INDEX.md
---

# /pattern-mine

Detect recurring operational patterns in execution history and codify them as reusable entries. Two-gate process — detection first, codification only after operator review.

## When to Use

- After accumulating 3+ traces and wanting to extract what's reusable
- When /trace-capture flags a pattern candidate for the 2nd time
- When the operator wants to turn a known working sequence into a named primitive
- Monthly as part of the `/observe` workspace health ritual

**Do NOT use for:**
- Cross-domain knowledge patterns → `/pattern` (that's for insight patterns, not execution patterns)
- Creating a full workspace skill → `/skill-new` (use pattern-mine first to codify, then skill-new to formalize)
- Mining patterns from a single trace (require 2+ instances for pattern, 3+ for primitive)

## Inputs Required

One of:
- Date range: scan traces from YYYY-MM-DD to YYYY-MM-DD
- Tag filter: scan traces tagged with `[tag]`
- Specific traces: list of exec IDs to analyze
- Flagged candidates: run after `/trace-capture` flagged candidates

## Workflow

**Step 1 — Read the index.**

Read `traces/TRACE-INDEX.md`. Identify the scope of traces to scan.

**Step 2 — Load and read the scoped traces.**

Read each trace file in scope from `traces/executions/`. Note: do not read more than 10 traces in one pass — if the scope is large, filter further.

**Step 3 — Detect candidates.**

Scan for recurring elements across the loaded traces:
- Repeated execution sequences (same steps in the same order across multiple sessions)
- Repeated decision patterns (same choice made for the same reason in similar situations)
- Repeated trigger conditions (same situation leading to the same type of work)
- Flagged pattern candidates in the trace files (the `[ ]` checkboxes in the Pattern Candidates section)

**Step 4 — Present detection results.**

Surface findings before writing anything:

```
Pattern Detection — [scope description]
════════════════════════════════════════

[N] candidate(s) detected:

1. "[Recurring element description]"
   Seen in: exec_YYYYMMDD_NNN, exec_YYYYMMDD_NNN ([N] instances)
   Recommendation: [Pattern entry | Execution primitive]
   Reason: [why this classification]

2. "[Recurring element description]"
   ...

Which would you like to codify? (number, or "skip all")
```

**Step 5 — Determine output type.**

For the selected candidate, ask:

```
Codify as:
  A. Operational pattern — situation-sequence-outcome (when X, do Y, get Z)
  B. Execution primitive — atomic reusable procedure with checklist

Which fits best?
```

Guide the decision:
- Pattern if the value is in the *recognition* — knowing when to apply the approach
- Primitive if the value is in the *procedure* — a step-by-step you'd follow every time

**Step 6 — Draft the entry.**

**If Pattern:** Use `templates/execution-pattern.md`. Draft:
- Pattern statement (one sentence: "When [context], [do X], to [achieve Y]")
- Trigger conditions
- Execution sequence
- Decision points
- Anti-triggers
- Known instances (the traces that sourced it)

Surface to operator:

```
Pattern draft: "[name]"
══════════════════════════════════
[full draft shown]

Approve, revise, or discard?
```

**If Primitive:** Use `templates/execution-primitive.md`. Draft:
- What it does (one sentence)
- Inputs required
- Procedure (numbered steps)
- Quality check criteria
- Known applications

Surface to operator in the same way.

**Step 7 — On approval, write the file.**

Determine the slug: lowercase, hyphenated, descriptive (`debug-first-then-diagnose`, `pm-session-close`, etc.).

Write to:
- `traces/patterns/pat_<slug>.md` (for patterns)
- `traces/primitives/prim_<slug>.md` (for primitives)

**Step 8 — Update the index.**

Append to the appropriate section of `traces/TRACE-INDEX.md`:

For patterns:
```
| pat_<slug> | [name] | [type] | emerging | [N] | [tags] |
```

For primitives:
```
| prim_<slug> | [name] | [type] | [duration] | [tags] |
```

**Step 9 — Offer skill promotion.**

If the primitive is high-value and would benefit from being a named workspace skill:

```
This primitive is well-defined enough to become a workspace skill.
Run /skill-new to formalize it as /[proposed-name].
```

Only offer this if the primitive is genuinely reusable beyond its current framing.

## Output Format

```
Pattern codified: pat_<slug>         [OR]  Primitive codified: prim_<slug>
  Name     : [name]
  Type     : [type]
  Sources  : exec_YYYYMMDD_NNN, exec_YYYYMMDD_NNN
  File     : traces/patterns/pat_<slug>.md
  Index    : TRACE-INDEX.md updated
```

## Quality Gate

- [ ] Detection presented to operator before any file is written
- [ ] Operator explicitly chose pattern vs. primitive
- [ ] Operator approved the draft before writing
- [ ] Slug is descriptive (not `pattern-001` or `prim-temp`)
- [ ] Known instances list references the source trace IDs
- [ ] TRACE-INDEX.md updated in the correct table
- [ ] 2+ instances required for pattern; 3+ recommended for primitive
