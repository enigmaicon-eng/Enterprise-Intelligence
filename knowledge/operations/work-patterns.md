---
title: Work Patterns — What Works Operationally
domain: operations
created: 2026-05-21
reviewed: 2026-05-21
tags: [workflow, productivity, habits, operational-intelligence, session-management]
connections: [friction-points, tool-mastery, context-engineering]
confidence: medium
source: original synthesis
---

## Definition
Work patterns are the operational habits and workflow structures that have been observed to produce better outcomes in this workspace — either higher quality output, lower friction, or better context continuity across sessions. This is a living document: patterns are added when they're confirmed (2+ instances), not when hypothesized.

## Why It Matters
Undocumented work patterns mean rediscovering the same optimizations each session. Explicit patterns make the system self-improving: each retro feeds this file, and this file feeds the next session's starting posture.

## Confirmed Patterns

### Session Start Protocol
**Pattern**: Read `memory/MEMORY.md` before any workflow. Never assume prior context.
**Why it works**: Claude Code starts each session with a blank slate. Memory files are the only cross-session continuity mechanism. Skipping the read causes duplicated work and contradicted decisions.
**Signal to apply**: Any session that references prior work or ongoing projects.

### Briefing Before Execution
**Pattern**: Run `/briefing` at the start of each working day before touching any project work.
**Why it works**: Forces prioritization before the day's entropy sets the agenda. Prevents spending the first 30 minutes on the first thing that appears rather than the highest-leverage thing.
**Signal to apply**: Start of any working day.

### Debrief Within 24 Hours
**Pattern**: Process meeting notes with `/debrief` within 24 hours of the meeting.
**Why it works**: After 24 hours, context needed to interpret shorthand notes decays. Action items captured late are less specific and less actionable than those captured same-day.
**Signal to apply**: Any meeting-intelligence/raw/ file older than the same day.

### Knowledge Promotion on Insight Recognition
**Pattern**: When you notice yourself thinking "I'll need to remember this" — that's the signal to run `/promote`, not "when I have time later."
**Why it works**: The gap between insight and promotion is where knowledge is lost. The insight recognition moment has the highest fidelity; waiting reduces both recall accuracy and motivation to capture.
**Signal to apply**: Any moment of "I should remember this."

### Atomic Task Completion Before Context Switch
**Pattern**: Complete the current task to a defined stopping point before switching contexts.
**Why it works**: Partial tasks create invisible overhead — the mental model for the half-done task stays loaded and creates interference. A clean stopping point is defined by: a written next step, a committed state, or a clear handoff.
**Signal to apply**: Any urge to "quickly check" something unrelated to the current task.

## Patterns Under Observation
*(Seen once — watching for confirmation)*

- Running `/observe` weekly (not just when something feels wrong) correlates with fewer cache misses.
- Writing the pre-mortem at decision time (not review time) produces more specific failure predictions.

## Failure Modes
- **Pattern accumulation without review**: adding patterns but never retiring obsolete ones. Every entry here should be re-validated at the monthly retro.
- **Pattern theater**: following the form of a pattern without its substance (e.g., writing a debrief that just copies meeting notes without extracting knowledge candidates).

## Connections
- [[friction-points]] — where these patterns break down or create unexpected resistance
- [[tool-mastery]] — tool-specific knowledge that supports these patterns
- [[context-engineering]] — the technical substrate that makes session-start protocol worth following

## Open Questions
- What is the minimum viable weekly review that still produces compound knowledge value vs. a full `/weekly` run?
- Is there a pattern for deciding when to break atomic task completion (legitimate interrupts vs. distraction)?

## Referenced By
<!-- Populated as other notes link to this one -->
