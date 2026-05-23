---
name: promote
description: >-
  Promotes a raw note, meeting extract, or knowledge candidate to a permanent
  knowledge entry in knowledge/<domain>/. Checks for existing entries on the
  same concept before creating a new one. Updates KNOWLEDGE-INDEX.md and adds
  [[connections]] to related entries. Trigger on: "promote this", "add to
  knowledge", "/promote <file or text>". Do NOT use for meeting files (use
  /debrief first), or for synthesis across topics (use /synthesize).
---

# Promote to Knowledge

Elevate a capture to permanent, linked knowledge.

## Inputs Required

1. The source: either a file path in `notes/` or text passed inline.
2. `knowledge/KNOWLEDGE-INDEX.md` — to check for existing entries on this concept.
3. If an existing related entry is found: read that file too.

## Workflow

1. Read the source content.
2. Read `knowledge/KNOWLEDGE-INDEX.md`. Ask: does a related concept already exist?
   - **Yes:** Decide — extend the existing entry, or create a sub-entry that links to it?
   - **No:** Create a new entry.
3. Determine the domain: strategy | technical | systems | operations.
4. Generate a concept slug (3-4 words, kebab-case, noun-focused).
5. Write the knowledge entry to `knowledge/<domain>/<slug>.md` using the template.
6. Update `knowledge/KNOWLEDGE-INDEX.md` — add the new entry under the correct domain.
7. Scan for `[[connections]]` — if the entry links to existing knowledge files, add a back-reference in those files.
8. If source was a note in `notes/raw/`: update its frontmatter to `promote_candidate: promoted`.
9. Report: file path created, domain assigned, connections made.

## Output Format — Knowledge Entry

```markdown
---
title: Concept Name (human-readable, title case)
domain: strategy | technical | systems | operations
created: YYYY-MM-DD
reviewed: YYYY-MM-DD
connections: []
confidence: high | medium | low
source: inline | note-slug | meeting-YYYY-MM-DD
tags: []
---

## Definition
[One clear paragraph. What is this concept, precisely? No jargon without definition.]

## Why It Matters
[How this connects to current work. Practical stakes and concrete implications.]

## Key Principles
[3-5 actionable principles. Concrete, not abstract platitudes.]
- 

## Connections
[Links to related knowledge: [[slug-of-related-concept]]]

## Open Questions
[What you don't yet know about this topic. Honest gaps.]
```

## Quality Gate

- [ ] Entry written to correct domain subdirectory
- [ ] KNOWLEDGE-INDEX.md updated with new entry
- [ ] All required sections present (Definition, Why It Matters, Key Principles, Connections, Open Questions)
- [ ] Confidence level reflects actual certainty — not inflated
- [ ] Source file updated if applicable (`promote_candidate: promoted`)
- [ ] Back-references added to connected entries
