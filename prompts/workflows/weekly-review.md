<!-- v1.0 | 2026-05-20 | Initial -->
You are generating a structured weekly review for an operational intelligence workspace.

You have been given:
- Action items from this week (completed and incomplete)
- Processed meeting summaries from this week
- New knowledge entries added
- Decisions logged
- Telemetry summary (workflows run, token costs)

Produce a structured weekly review following this schema exactly.

## Output Schema

### Week Summary
2-3 sentences. The essential character of this week — what it was about, what the dominant theme was.

### Progress vs. Commitments
For each commitment from last week:
- **[Complete / Partial / Slipped]** — Task description — brief explanation if partial or slipped

### Patterns & Insights
What repeated? What surprised? What contradicted expectations? Minimum 3 patterns, maximum 6.

### Knowledge Added This Week
List new knowledge entries created. Note any particularly important additions.

### Decision Quality Retrospective
For decisions made this week: with the benefit of a week's hindsight, were they well-reasoned? Any that should be revisited?

### Next Week Priorities
Exactly 5 priorities, ranked. For each:
- **Priority [N]:** [Description] — [Why this, not something else: strategy alignment in one sentence]

### Open Questions
Threads that need resolution. Not action items — genuinely open questions where the answer isn't clear yet.

### System Health Note
One sentence on the workspace itself: what's working, what needs attention (per telemetry).

---

### Synthesis Flag
**synthesis_needed:** [true / false]
If true, explain in one sentence what cross-domain synthesis would be most valuable this week.
