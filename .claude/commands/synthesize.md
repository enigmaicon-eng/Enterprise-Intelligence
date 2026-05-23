---
name: synthesize
description: >-
  Generates a deep, cross-domain synthesis memo on a specific topic. Gathers
  relevant knowledge entries, decisions, meeting patterns, and strategy context.
  Uses maximum reasoning depth. Writes to synthesis/. Trigger on: "synthesize",
  "deep analysis of", "cross-domain insight on", "/synthesize <topic>". Do NOT
  use for single-meeting processing (use /debrief) or weekly review (use /weekly).
  Best results with explicit topic scoping from the user.
---

# Synthesis Memo

Generate a cross-domain synthesis that produces insight not available from any single source.

## Inputs Required

Determined by the topic. Before reading anything, identify:
1. Which knowledge domains are relevant to this topic?
2. Which specific files in `knowledge/` are relevant?
3. Are there recent decisions in `decision-frameworks/decisions-log.md` relevant to this topic?
4. Are there recent meeting processed files relevant to this topic?
5. Is there active strategy in `strategy/` relevant to this topic?

Read `knowledge/KNOWLEDGE-INDEX.md` first to identify which knowledge files to load. Do not load the entire knowledge directory — be surgical.

## Workflow

1. Read `knowledge/KNOWLEDGE-INDEX.md`. Identify relevant entries.
2. Read the specific relevant knowledge files (max 5-7 for a focused synthesis).
3. Read relevant decisions and meeting patterns as needed.
4. Identify: what does each source say? Where do they agree? Where do they diverge or contradict?
5. Generate the synthesis — lead with the highest-leverage insight, not a summary of sources.
6. Extract knowledge candidates (new concepts that emerged from the synthesis).
7. Write to `synthesis/YYYY-MM-DD-<topic-slug>.md`.
8. Report: file written, knowledge candidates identified for /promote.

## Reasoning Discipline

Lead with the highest-leverage insight, not a recitation of sources.

Make connections explicit: "X from [domain A] parallels Y in [domain B] because..."

Separate confirmed patterns from speculative connections — label speculative reasoning clearly.

Always end with: "What would change if this synthesis is wrong?"

## Output Format

```markdown
---
topic: [Topic Name]
date: YYYY-MM-DD
sources:
  - [list of files read]
domains: [list of domains represented]
confidence: high | medium | speculative
knowledge_candidates: []
---

## Core Insight
[The highest-leverage finding — what this synthesis reveals that no single source contains.
1-3 sentences. Lead with this; don't bury it.]

## Cross-Domain Connections
[The structural links found across domains. Explicit: "X parallels Y because..."]
- 

## Confirmed Patterns
[What multiple sources agree on. Convergence = higher confidence.]
- 

## Divergences and Contradictions
[Where sources disagree or point in different directions. These are often the most valuable findings.]
- 

## Implications
[What this means concretely for current work, decisions, or strategy.]
- 

## What Would Change If This Is Wrong
[The assumption most load-bearing for this synthesis. If it fails, which conclusions fall?]

## Open Questions
[What this synthesis surfaced that it couldn't answer. Worth exploring next.]
- 

## Knowledge Candidates
[Concepts that emerged that deserve a permanent knowledge entry. One line each.]
- 
```

## Quality Gate

- [ ] Core Insight leads the document — not buried in section 4
- [ ] Cross-domain connections are explicit (named domains, named concepts, explicit link)
- [ ] Confirmed patterns are separated from speculative ones
- [ ] "What Would Change" section is honest and specific
- [ ] File written to `synthesis/YYYY-MM-DD-<topic>.md`
- [ ] Knowledge candidates listed for user to /promote
- [ ] Confidence level reflects actual certainty of the synthesis
