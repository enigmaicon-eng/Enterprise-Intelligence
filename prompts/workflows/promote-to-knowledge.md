<!-- v1.0 | 2026-05-21 | Initial -->
You are converting a raw note, meeting extract, or capture into a permanent knowledge entry for a structured knowledge base. The output must stand alone — a future reader with no context should be able to read this entry and fully understand the concept.

## Output Format

```markdown
---
title: [Concept Name — be specific, not generic]
domain: strategy | technical | systems | operations | pm | learning
created: YYYY-MM-DD
reviewed: YYYY-MM-DD
tags: [tag1, tag2, tag3]
connections: [related-concept-slug, another-concept]
confidence: high | medium | low
source: [original synthesis | meeting-YYYY-MM-DD | note-slug | url]
---

## Definition
One precise paragraph. What is this concept, practice, or insight? Define it clearly enough that someone encountering it for the first time understands it completely.

## Why It Matters
Practical stakes. How does this connect to real work? What breaks if you ignore this?

## Key Principles
3-5 bullet points. Each principle should be actionable or directly applicable, not just descriptive.

## Connections
Links to related knowledge entries: [[related-concept]], [[another-concept]].
Explain the relationship in one sentence each — not just the link.

## Open Questions
What remains unknown or unresolved about this concept? What would need to be true to increase confidence?
```

## Rules
- The title should be specific enough to distinguish this entry from adjacent concepts.
- Definition must be self-contained — no references to "this note" or "as discussed."
- Confidence reflects how well-validated this knowledge is: high = tested, medium = inferred, low = hypothesis.
- If source is a URL, include it. If synthesized, say so.
- Connections must name actual concepts that could exist in the knowledge base.
- Do not pad. A tight 200-word entry beats a padded 600-word one.
