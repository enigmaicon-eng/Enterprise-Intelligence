# Trace Index
## Searchable Execution History — One Operator

All execution traces, journal entries, patterns, and primitives are indexed here. Read this before loading any individual trace file. Never scan `traces/executions/` directly.

---

## How to Search

- **By topic/goal:** Scan the Goal column for keywords matching your upcoming work.
- **By tag:** Use Grep on this file: `traces/patterns/TRACE-INDEX.md` with your keyword.
- **By date:** Filter the Date column for a time range.
- **By type:** Filter the Type column for the session type you want.
- **By reuse:** Filter for `reuse=high` to find the most transferable traces.

For retrieval before starting work: `/trace-recall [description of upcoming work]`
For keyword search: `/trace-search [keyword]`

---

## Execution Episodes

| ID | Date | Type | Goal | Outcome | Reuse | Tags |
|----|------|------|------|---------|-------|------|
| *(no traces yet — first trace will appear here)* | | | | | | |

---

## Journal Entries

| Date | Session Focus | Key Insight | Tags |
|------|--------------|-------------|------|
| *(no journal entries yet)* | | | |

---

## Patterns

| ID | Name | Type | Confidence | Instances | Tags |
|----|------|------|------------|-----------|------|
| *(no patterns yet)* | | | | | |

---

## Primitives

| ID | Name | Type | Duration | Tags |
|----|------|------|----------|------|
| *(no primitives yet)* | | | | |

---

## Lifecycle Notes

- Warm traces (0–90 days): in `traces/executions/`
- Cold traces (90+ days): moved to `traces/archive/` during `/observe`
- Patterns and primitives: always warm — never archived
- Index is updated every time `/trace-capture` or `/workflow-journal` runs
