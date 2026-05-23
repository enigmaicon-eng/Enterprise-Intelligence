---
name: weekly
description: >-
  Runs the weekly review: assembles the week's output, assesses progress against
  commitments, surfaces patterns, and produces next week's priorities. Reads
  all processed meetings, action items, decisions, and memory for the past 7
  days. Writes to reviews/weekly/. Trigger on: "weekly review", "end of week",
  "/weekly". Do NOT use for daily briefing (/briefing), monthly strategy
  (/synthesize with monthly scope), or system health (/observe).
---

# Weekly Review

Close the loop on the week. Surface patterns. Calibrate next week.

## Inputs Required

Read these files before generating output:

1. `execution/action-items.md` — all items (completed, open, slipped this week)
2. `meeting-intelligence/processed/` — all files dated within the past 7 days
3. `decision-frameworks/decisions-log.md` — entries from this week
4. `knowledge/KNOWLEDGE-INDEX.md` — entries added this week (check `created:` dates)
5. `memory/MEMORY.md` → read relevant memory files (active projects, priorities)
6. `telemetry/workflow-log.jsonl` — past 7 days (for system health note)

Do not read more than the past 7 days of files. This is a weekly scope only.

## Workflow

1. Read all inputs listed above. Do not skip any — completeness matters here.
2. Separate action items: completed / partial / slipped. For slipped: note why (if stated).
3. Identify patterns across meetings and work: what repeated? what surprised?
4. Assess decisions made this week: with one week's hindsight, were they well-reasoned?
5. Identify next week's top 5 priorities. Rank by: urgency × strategy alignment. Each must have a one-clause rationale.
6. Set `synthesis_needed` flag: true if a cross-domain synthesis would be valuable this week. Name the topic.
7. Write the review to `reviews/weekly/YYYY-WW.md`.
8. Update `execution/action-items.md`: carry over open items, close completed ones, re-prioritize.
9. Update relevant memory files if new patterns or project phases emerged.
10. Report: file written, memory updates made, whether synthesis was flagged.

## Output Format

```markdown
---
week: YYYY-WW
date_range: YYYY-MM-DD to YYYY-MM-DD
synthesis_needed: true | false
synthesis_topic: [if true: the topic worth synthesizing]
---

## Week Summary
[2-3 sentences. The essential character of this week — what it was about, what the dominant theme was.]

## Progress vs. Commitments
[For each commitment from last week's priorities:]
- [Complete | Partial | Slipped] — Task — [brief explanation if partial or slipped]

## Patterns & Insights
[What repeated, what surprised, what contradicted expectations. 3-6 bullets. Specific, not generic.]
- 

## Knowledge Added
[New knowledge entries created this week. One line each.]
- 

## Decision Quality
[For each decision made this week: in hindsight, was it well-reasoned? What would you change?]
- 

## Next Week Priorities
1. [Task] — Why: [one clause on strategy alignment]
2. [Task] — Why:
3. [Task] — Why:
4. [Task] — Why:
5. [Task] — Why:

## Open Questions
[Genuinely unresolved — not action items, but things where the answer isn't clear yet.]
- 

## System Health Note
[One sentence on the workspace: what's working, what needs attention based on workflow log.]
```

## Quality Gate

- [ ] All 6 input sources read before generating output
- [ ] Progress section covers EVERY commitment from last week (not just some)
- [ ] Patterns section has 3-6 items, each specific (no "continued making progress")
- [ ] Next week has exactly 5 priorities, each with a rationale clause
- [ ] File written to `reviews/weekly/YYYY-WW.md`
- [ ] `execution/action-items.md` updated (carries, closures, re-prioritization)
- [ ] Memory updated if new project phases or patterns emerged
- [ ] `synthesis_needed` flag set with a topic if true
