# Context Compilation Workflow
## Version: v1.0

Assemble the optimal context configuration for a specified task. Produces a context manifest: which layers are needed, which files to load, in what order, and estimated token budget.

---

## When to Use

Use before starting a complex multi-file workflow to verify the context configuration before committing tokens. Especially useful for:
- Strategic analysis tasks that might over-load context
- First use of a new skill pipeline
- Sessions where context overhead has been growing

---

## Compilation Steps

### 1. Task type identification
Map the described task to the Context Routing table in `architecture/CONTEXT-ENGINEERING-SYSTEM.md`.
State the task type explicitly: "This is a [type] task."

### 2. Layer assembly (sequential)

```
Layer A — CLAUDE.md
  Estimate tokens: file size in bytes ÷ 4
  Flag if > 1,000 tokens

Layer B — Memory (selective)
  Always include: memory/MEMORY.md index
  Include user_profile.md if: the task requires judgment about the user's context
  Include project file if: a named project is the session's focus
  List each included memory file and its estimated token cost

Layer C — Skill
  Identify the active skill for this task
  Include its .claude/commands/<skill>.md
  Estimate tokens: file size ÷ 4

Layer D — Task Data
  List only the files the active skill's workflow requires
  For each: state which workflow step requires it and its estimated token cost
  Apply: index-first heuristic, date filtering, size-check for large files
```

### 3. Budget calculation
Sum estimated tokens for all layers A+B+C+D.
Compare against the 4,000-token overhead target.

```
If under 3,500: green — proceed
If 3,500–4,000: yellow — monitor; don't load additional files speculatively
If over 4,000: red — identify what to defer or compress before proceeding
```

### 4. Output the manifest

```
## Context Manifest — [Task Type] — [Date]

Layers:
  A: CLAUDE.md — ~[N] tokens
  B: memory/MEMORY.md — ~[N] tokens
  B: [per-file memory] — ~[N] tokens [reason]
  C: .claude/commands/[skill].md — ~[N] tokens
  D: [file] — ~[N] tokens [workflow step]

Load order: [sequence]
Total overhead: ~[N] tokens — [green/yellow/red]

Flags: [any issues: missing files, over-budget layers, broken pointers]
```

---

## Quality Criteria

A complete, correct context manifest:
- Names every layer explicitly (even layers not needed, with "not loaded" noted)
- Provides token estimates for every included file
- States the budget status (green/yellow/red)
- Lists any flags before the workflow begins
- Does not include files not required by the active workflow step
