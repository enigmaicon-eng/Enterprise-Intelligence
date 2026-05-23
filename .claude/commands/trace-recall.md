---
name: trace-recall
description: >-
  Retrieval-enhanced execution: surfaces relevant past traces before starting
  work similar to something done before. Reads TRACE-INDEX.md, identifies the
  1-3 most relevant execution episodes, loads them, and surfaces key decisions
  and lessons from each. Trigger on: "what did I do last time I worked on X",
  "recall how I approached Y", "find relevant traces for Z", "before I start
  this, what have I done like it", or explicitly as /trace-recall [description].
  Do NOT use for general knowledge retrieval (use /recall) or when there is
  no clear prior work to reference.
version: 1.0
output: terminal (context loaded for upcoming session)
---

# /trace-recall

Retrieval-enhanced execution. Before starting work, surface what has been done before — the decisions made, what worked, what failed — so the upcoming session starts with accumulated experience rather than a blank slate.

## When to Use

- Before starting a workflow that resembles past work
- Before a debugging session on a system you've debugged before
- Before a PM session on a topic with prior history in the traces
- When the operator explicitly asks "how did I do this before?"

**Do NOT use for:**
- General knowledge retrieval → `/recall`
- Searching by keyword without execution context → `/trace-search`
- Retrieving knowledge concepts → `/recall` + KNOWLEDGE-INDEX.md

## Inputs Required

- Description of the upcoming work (natural language)

## Workflow

**Step 1 — Read the index.**

Read `traces/TRACE-INDEX.md`. Do not skip this step.

**Step 2 — Score for relevance.**

For each entry in the Execution Episodes table, score relevance to the operator's description based on:
- Goal similarity (keywords overlap with upcoming work description)
- Type match (upcoming debug session → past debug traces score higher)
- Tags overlap
- Recency (prefer warm traces over old ones, all else equal)

Select the top 1–3 traces. If no traces score as clearly relevant, say so.

**Step 3 — Load and read the top traces.**

Read each selected trace file from `traces/executions/`. Also check `traces/patterns/` and `traces/primitives/` for any entries whose tags match — these are even more directly applicable.

**Step 4 — Surface the findings.**

For each relevant trace, extract and present:
- What the goal was
- The key decision(s) made and the rationale
- What worked
- What failed / would be done differently

For each relevant pattern or primitive, surface it directly: "You have a codified primitive for this: `prim_<slug>` — [name]. Procedure: [steps]."

Format as a concise briefing, not a full file dump:

```
Trace Recall — [upcoming work description]
══════════════════════════════════════════

Relevant traces found: [N]

1. exec_YYYYMMDD_NNN — [goal]  ([date], [outcome])
   Key decision: [decision + rationale]
   What worked: [bullet]
   Watch out for: [failure/lesson]

2. exec_YYYYMMDD_NNN — [goal]  ([date], [outcome])
   ...

Relevant primitives: [if any]
  prim_<slug> — [name]: [procedure summary]

Patterns applicable: [if any]
  pat_<slug> — [name]: [pattern statement]
```

**Step 5 — Offer to load more detail.**

```
Load full trace for exec_YYYYMMDD_NNN? (yes to read the complete file)
```

Only load the full file on request — the summary is sufficient for most cases.

## Output Format

See Step 4 above. Terminal output only — not written to disk.

## Quality Gate

- [ ] TRACE-INDEX.md was read before loading any trace files
- [ ] Relevance scoring is based on goal/tag/type match, not just recency
- [ ] Output is a concise briefing — not a raw file dump
- [ ] Patterns and primitives are surfaced if tags match
- [ ] If no relevant traces: says so clearly, does not invent relevance
