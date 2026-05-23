---
name: capture
description: >-
  Captures raw input — a note, thought, URL, reference, or idea — and writes it
  to notes/raw/ with minimal structure and auto-tagging. Fast path: no synthesis,
  no analysis, no promotion. Trigger on: "capture this", "note:", "save this",
  "log this", "/capture <text>". Do NOT use when the user wants the note
  immediately promoted to knowledge (use /promote), or when the input is a
  meeting (use /debrief).
---

# Capture

Fast, frictionless capture. Write first, structure minimally, synthesize later.

## Inputs Required

The text or content to capture. May be:
- Inline text in the command: `/capture <text>`
- A file path to structure: `/capture <path-to-file>`
- A URL + title to bookmark

No other files need to be read.

## Workflow

1. Receive the content to capture.
2. Generate a short slug from the content (3-4 words, kebab-case).
3. Add minimal frontmatter (see Output Format).
4. Write to `notes/raw/YYYY-MM-DD-HHmm-<slug>.md`.
5. If urgency=high: also append to `execution/action-items.md` as a low-priority item.
6. Report: file path created + whether it was flagged as an action item.

## Tagging Rules

- **domain:** strategy | technical | operations | learning | reference | other
- **type:** insight | question | action | idea | reference | resource
- **urgency:** high (needs to happen this week) | medium | low
- **promote_candidate:** true if this deserves permanent knowledge; false otherwise

When uncertain about tagging, bias toward: domain=other, type=idea, urgency=low, promote_candidate=false.

## Output Format

```markdown
---
captured: YYYY-MM-DDTHH:MM
domain: [domain]
type: [type]
urgency: [urgency]
promote_candidate: [true|false]
tags: []
source: inline | url | file
---

[Content exactly as provided, without modification]
```

## Quality Gate

- [ ] File written to `notes/raw/` with correct naming convention
- [ ] Frontmatter complete with all required fields
- [ ] Content not modified or summarized — captured verbatim
- [ ] If urgency=high: action item appended to `execution/action-items.md`
- [ ] Response to user: file path + tag summary in 2 lines max
