---
name: debrief
description: >-
  Processes a raw meeting file into structured operational intelligence: extracts
  action items, decisions, knowledge candidates, and follow-ups. Input is a file
  in meeting-intelligence/raw/. Output is a processed file plus updates to
  action-items.md and decisions-log.md. Trigger on: "debrief", "process this
  meeting", "/debrief <filename>". Do NOT use for non-meeting documents (use
  /synthesize or /promote) or for generating a synthesis across multiple meetings
  (use /weekly).
---

# Meeting Debrief

Transform a raw meeting record into structured, forward-feeding intelligence.

## Inputs Required

1. The raw meeting file: `meeting-intelligence/raw/<filename>` — read in full.
2. `execution/action-items.md` — to append extracted action items.
3. `decision-frameworks/decisions-log.md` — to append extracted decisions.

Do not read other files. Scope is this meeting only.

## Workflow

1. Read the raw meeting file in full. Note: do NOT summarize or interpret at this stage — read first.
2. Extract the following (see Output Format for each section's schema):
   - Action items (with owner, due, priority)
   - Decisions made (with rationale, reversibility)
   - Knowledge candidates (topics worth permanent knowledge entry)
   - Follow-ups needed (unresolved threads)
   - Patterns (connections to other meetings or ongoing themes)
3. Write the processed file to `meeting-intelligence/processed/<same-filename>`.
4. Append extracted action items to `execution/action-items.md`.
5. Append extracted decisions to `decision-frameworks/decisions-log.md`.
6. Update the raw file's frontmatter: set `processed: true` and `action_items_extracted: true`.
7. Report: what was extracted (counts), file path written, and list of knowledge candidates for the user to /promote when ready.

## Precision Rule

Do not paraphrase decisions or action items. Capture them as stated. If something is unclear from the raw notes, mark it `[UNCLEAR]` and continue — do not guess.

## Output Format — Processed File

```markdown
---
date: YYYY-MM-DD
participants: [as stated in raw file]
duration_minutes: [as stated or estimated]
type: [as stated]
topics: [extracted from content]
processed: true
action_items_extracted: true
---

## Summary
[3 sentences maximum. What this meeting was about and what the net outcome was.]

## Key Points
[Bulleted, specific. Not interpretations — what was actually said/agreed.]
- 

## Decisions Made
[For each decision:]
- **Decision:** [exact decision]
  **Rationale:** [if stated]
  **Owner:** [who is accountable]
  **Reversibility:** high | medium | low | irreversible

## Action Items
[For each action item:]
- **Task:** [specific deliverable]
  **Owner:** [name]
  **Due:** [date or relative]
  **Priority:** 🔴 | 🟡 | 🟢

## Knowledge Candidates
[Topics that should become permanent knowledge entries. Short phrases only.]
- 

## Follow-Up Needed
[Async threads, unresolved questions, dependencies to resolve before next meeting.]
- 

## Patterns
[Connections to prior meetings, recurring themes, signals for the weekly review.]
- 
```

## Quality Gate

- [ ] Processed file written to `meeting-intelligence/processed/`
- [ ] Raw file frontmatter updated (`processed: true`)
- [ ] Action items appended to `execution/action-items.md` with priority and due date
- [ ] Decisions appended to `decision-frameworks/decisions-log.md`
- [ ] Knowledge candidates listed (even if empty — "None identified")
- [ ] No paraphrasing of decisions or action items — verbatim or [UNCLEAR]
- [ ] Summary is 3 sentences maximum
