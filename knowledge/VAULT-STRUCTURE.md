# Vault Structure
## Directory Map and Domain Contracts

---

```
Enterprise Intelligence Workspace
│
├── knowledge/                          ← Permanent knowledge base
│   ├── KNOWLEDGE-INDEX.md              ← Master index: all entries, all domains
│   ├── VAULT-STRUCTURE.md              ← This file
│   ├── KNOWLEDGE-GRAPH.md              ← Connection map (generated, not maintained manually)
│   │
│   ├── pm/                             ← Product management knowledge
│   │   └── [18+ concept files]
│   │
│   ├── strategy/                       ← Strategic thinking and frameworks
│   │   ├── mental-models.md            ← Core strategic mental models
│   │   ├── bets-history.md             ← Historical bet patterns and outcomes
│   │   └── annual-themes.md            ← Themes by year (updated annually)
│   │
│   ├── systems/                        ← Systems thinking and design
│   │   ├── emergence-patterns.md       ← How complex behavior emerges
│   │   └── feedback-loop-library.md    ← Annotated feedback loop types
│   │
│   ├── technical/                      ← AI, software, and technical knowledge
│   │   ├── ai-systems.md               ← AI/Claude model knowledge
│   │   ├── context-engineering.md      ← Context management science
│   │   ├── claude-patterns.md          ← Claude-specific effective patterns
│   │   ├── mcp-patterns.md             ← MCP integration patterns
│   │   └── repo-insights/              ← Per-repository extracted intelligence
│   │       └── [repo-name].md
│   │
│   ├── operations/                     ← Operational intelligence
│   │   ├── work-patterns.md            ← What works operationally
│   │   ├── tool-mastery.md             ← Claude Code / AI tool learnings
│   │   └── friction-points.md         ← Where the system creates friction
│   │
│   ├── patterns/                       ← Cross-domain patterns
│   │   ├── index.md                    ← Pattern library index
│   │   └── [pattern-slug].md
│   │
│   ├── decisions/                      ← Decision intelligence
│   │   ├── decision-patterns.md        ← Recurring decision types and heuristics
│   │   └── decision-retrospective.md   ← Quality review of past decisions
│   │
│   └── clusters/                       ← Thematic synthesis (generated at 5+ note threshold)
│       ├── ai-systems.md               ← Everything about AI in this workspace
│       └── operational-intelligence.md ← How the workspace operates
│
├── learning/                           ← Staging area for external learning
│   ├── pm/
│   ├── technical/
│   ├── strategy/
│   └── [entries promoted → knowledge/ or archived]
│
├── templates/                          ← Note templates (copy, don't edit)
│   ├── atomic-concept.md
│   ├── cluster-note.md
│   ├── pattern-entry.md
│   ├── learning-entry.md
│   ├── decision-journal.md
│   ├── repo-insight.md
│   ├── operational-retro.md
│   ├── knowledge-entry.md             ← Legacy template, superseded by atomic-concept
│   └── [other existing templates]
│
├── synthesis/                          ← Cross-domain synthesis outputs
│   ├── weekly-insights/
│   └── monthly-insights/
│
└── decision-frameworks/                ← Operational decisions and frameworks
    ├── decisions-log.md                ← Individual decision log
    └── pm/                             ← PM-specific frameworks
```

---

## Domain Contracts

### `knowledge/pm/` — Product Management
**What belongs:** PM concepts, frameworks, techniques, mental models specific to product management.
**What doesn't belong:** Generic business strategy (→ `strategy/`), organizational dynamics that aren't PM-specific (→ `systems/`).

### `knowledge/strategy/` — Strategic Thinking
**What belongs:** How to think strategically — mental models, bet frameworks, strategic patterns.
**What doesn't belong:** Specific product decisions (→ `decision-frameworks/`), tactical PM work (→ `pm/`).

### `knowledge/systems/` — Systems Thinking
**What belongs:** Systems dynamics, feedback loops, emergence patterns, complex adaptive systems.
**What doesn't belong:** Software system architecture (→ `technical/`), PM systems thinking (→ `pm/systems-thinking-pm`).

### `knowledge/technical/` — Technical Knowledge
**What belongs:** AI systems, software architecture, context engineering, APIs, Claude patterns, MCP.
**What doesn't belong:** PM technical fluency (→ `pm/technical-fluency`), operational scripts (→ `scripts/`).

### `knowledge/operations/` — Operational Intelligence
**What belongs:** What works in this workspace operationally, tool mastery, friction points, workflow patterns.
**What doesn't belong:** Specific workflow steps (→ `workflows/`), architectural decisions (→ `architecture/`).

### `knowledge/patterns/` — Cross-Domain Patterns
**What belongs:** Patterns that appear across multiple domains. Structured as: context → forces → solution → consequences.
**What doesn't belong:** Domain-specific techniques (those belong in their domain).

### `knowledge/clusters/` — Synthesis Clusters
**What belongs:** Thematic synthesis of 5+ related notes. Generated output, not manual filing.
**What doesn't belong:** Individual concept notes (those belong in their domain). Clusters are synthesis artifacts.

---

## Obsidian Vault Configuration (optional)

If using Obsidian as a visual interface for this knowledge base:

1. Set vault root to `C:\Users\DELL\Enterprise-Intelligence-Workspace\`
2. Enable: `Files and links → Use [[Wikilinks]]`
3. Enable: `Files and links → Automatically update internal links`
4. Graph view settings: Show attachments OFF, Show orphans OFF, Node size by connections
5. Core plugins to enable: Graph view, Backlinks, Outgoing links, Tags
6. Exclude from graph: `repos/`, `.git/`, `node_modules/`

The `[[link]]` syntax used throughout this knowledge base is Obsidian-compatible without any conversion.
