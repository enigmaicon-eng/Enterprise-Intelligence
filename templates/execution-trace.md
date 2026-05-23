---
trace_id: exec_YYYYMMDD_NNN
date: YYYY-MM-DD
session_type: workflow | debug | architecture | pm-session | synthesis | build
goal: brief goal statement (one line)
outcome: completed | partial | abandoned | failed
duration: short (<1h) | medium (1-3h) | long (3h+)
tags: [tag1, tag2, tag3]
reuse_potential: high | medium | low
artifacts: []
---

## Goal
What were you trying to accomplish? What would "done" look like?

## Context
What triggered this work? What was the situation before it started? What constraints were in play?

## Execution Sequence

1. [Step — what you did and what it produced]
2. [Step]
3. [Step]
<!-- Add as many steps as needed. Be specific enough to reconstruct the path. -->

## Key Decisions

- **Decision:** [what you chose]
  **Rationale:** [why this over alternatives]
  **Alternative considered:** [what you ruled out and why]

<!-- Add one block per significant decision point -->

## Artifacts Produced

- `[file/path]` — [brief description of what it contains]

## What Worked

- [Bullet — specific technique, framing, or sequence that was effective]

## What Failed / What I'd Do Differently

- [Bullet — specific failure point, wrong turn, or improvement for next time]

## Pattern Candidates

Recurring elements that might be worth codifying as a pattern or primitive.

- [ ] [Describe the recurring element]

## Links

- Related traces: [[exec_YYYYMMDD_NNN]]
- Related knowledge: [[concept-slug]]
- Related pattern: [[pat_slug]]
