---
name: trace-search
description: >-
  Keyword or topic search across the execution trace history. Reads
  TRACE-INDEX.md and returns matching traces, patterns, and primitives.
  More direct than /trace-recall — no pre-execution framing, just find
  what's there. Trigger on: "search traces for X", "find when I worked on Y",
  "what traces exist about Z", "show me all debugging traces", "find traces
  tagged with X". Do NOT use when preparing for upcoming work (use
  /trace-recall) or when searching knowledge entries (use /recall).
version: 1.0
output: terminal
---

# /trace-search

Keyword or filter search across execution history. Answers: "what do I have on this topic?"

## When to Use

- Looking for a specific past session by topic, type, or tag
- Auditing what traces exist in a domain before pattern-mining
- Finding whether a workflow was ever captured before
- Exploring trace coverage across a time range

**Do NOT use for:**
- Pre-execution context loading → `/trace-recall` (that has relevance scoring and framing)
- Knowledge concept search → `/recall`

## Inputs Required

One of:
- Keyword or topic (natural language)
- Tag filter: `--tag [tag]`
- Type filter: `--type [workflow|debug|architecture|pm-session|synthesis|build]`
- Date filter: `--since YYYY-MM-DD`
- Outcome filter: `--outcome [completed|partial|abandoned|failed]`
- Reuse filter: `--reuse [high|medium|low]`
- Patterns only: `--patterns`
- Primitives only: `--primitives`

Filters can be combined.

## Workflow

**Step 1 — Read TRACE-INDEX.md.**

**Step 2 — Apply filters.**

Match against all four index tables (Execution Episodes, Journal Entries, Patterns, Primitives) based on the operator's search criteria. Keyword search checks Goal, Tags, and (for patterns/primitives) Name columns.

**Step 3 — Return results.**

If results found:

```
Trace Search — "[keyword]"
══════════════════════════

Execution Episodes ([N] found):
  exec_YYYYMMDD_NNN  [date]  [type]  [goal]  [outcome]  tags: [tags]
  exec_YYYYMMDD_NNN  ...

Patterns ([N] found):
  pat_<slug>  [name]  [type]  confidence: [level]  instances: [N]

Primitives ([N] found):
  prim_<slug>  [name]  [type]  duration: [est]

Journal entries: [N] matching days
```

If no results:

```
No traces found matching "[keyword]".

Trace coverage:
  Total episodes : [N]
  Patterns       : [N]
  Primitives     : [N]
  Date range     : [earliest] – [latest]

Consider running /trace-capture after your next session on this topic.
```

**Step 4 — Offer to load detail.**

```
Load full trace for any of these? (specify trace ID)
```

## Output Format

See Step 3 above. Terminal only — not written to disk.

## Quality Gate

- [ ] TRACE-INDEX.md read before any file loading
- [ ] All four index tables searched (not just episodes)
- [ ] Empty results surface trace coverage stats, not just "nothing found"
- [ ] Results are sorted by date descending (most recent first) within each category
