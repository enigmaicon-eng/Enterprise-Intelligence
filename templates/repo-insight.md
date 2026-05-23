---
title: "[Repo Name] — Repository Insight"
repo: [owner/repo-name]
repo_url: [URL]
analyzed: YYYY-MM-DD
commit_sha: [short SHA at time of analysis]
domain: technical
tags: [tag1, tag2, tag3]
confidence: high | medium | low
connections: [related-slug-1, related-slug-2]
---

## What This Repo Is
One paragraph. What problem does this solve, who built it, what is its design philosophy?

## Architecture Overview
How is the codebase structured? Key directories, entry points, and the flow from input to output.

```
[repo-name]/
├── [key-dir]/     ← [what it contains]
├── [key-dir]/     ← [what it contains]
└── [key-file]     ← [role of this file]
```

## Core Design Decisions
What architectural choices did the author make? What did they optimize for?

1. **[Decision]** — Why it was made and what it enables/costs.
2. **[Decision]** — ...

## Patterns Worth Extracting
Specific implementation patterns from this repo that are reusable elsewhere.

### Pattern: [Name]
- **Where:** `path/to/file.ext:line_number`
- **What it does:** ...
- **When to use:** ...

## Key Abstractions
What concepts or interfaces does this repo introduce that you should understand?

- **[Concept]:** Definition and role in the system.
- **[Concept]:** ...

## How to Apply Learnings Here
Concrete ways the insights from this repo change how you would approach work in this workspace.

1. ...
2. ...

## Limitations and Gaps
What does this repo NOT do well, where does the approach break down, or what's missing?

## Connection to Workspace Work
- [[knowledge-slug]] — how this repo's patterns relate to existing knowledge
- [[knowledge-slug]] — ...

## Staleness Signal
This entry flags for review when the repo accumulates 50+ new commits since `commit_sha` above.
