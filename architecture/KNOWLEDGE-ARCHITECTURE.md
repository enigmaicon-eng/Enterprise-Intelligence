# Knowledge Architecture
## Linked Thinking, Synthesis Workflows, and Knowledge Compounding

---

## Design Philosophy

Knowledge compounds when connections are explicit, retrieval is fast, and synthesis happens at the right moment — not on demand from scratch.

Three principles from kepano / Obsidian applied to a flat-file workspace:

1. **Atomic notes beat long documents.** One concept per file, fully self-contained. You can link to it, read it in isolation, and update it without touching anything else.
2. **Links are more valuable than hierarchy.** `[[context-engineering]]` pointing to another note is permanent intelligence. Folder nesting is just filing.
3. **Evergreen over ephemeral.** A note that evolves over time beats a note that captures a moment. Update `[[mental-models]]` rather than writing a new one.

---

## Note Taxonomy

Five note types. Every file in `knowledge/` is one of these:

| Type | Location | Purpose | Template |
|------|----------|---------|---------|
| **Atomic concept** | `knowledge/<domain>/` | One fully-understood idea | `templates/atomic-concept.md` |
| **Cluster** | `knowledge/clusters/` | Thematic synthesis of 5+ related notes | `templates/cluster-note.md` |
| **Pattern** | `knowledge/patterns/` | Recurring structure with context/forces/solution | `templates/pattern-entry.md` |
| **Learning** | `learning/<domain>/` | Structured capture from external source | `templates/learning-entry.md` |
| **Repo insight** | `knowledge/technical/repo-insights/` | Extracted intelligence from a repository | `templates/repo-insight.md` |

Decision journal entries live in `knowledge/decisions/` and use `templates/decision-journal.md`.
Operational retrospectives live in `knowledge/operations/` and use `templates/operational-retro.md`.

---

## Domain Structure

```
knowledge/
├── KNOWLEDGE-INDEX.md          ← Master index (domain-grouped, tag-searchable)
├── VAULT-STRUCTURE.md          ← Directory map and purpose of each domain
├── KNOWLEDGE-GRAPH.md          ← Textual connection map (updated when clusters generated)
│
├── pm/                         ← Product management (18+ entries)
├── strategy/                   ← Strategic thinking, mental models, bets
├── systems/                    ← Systems design, emergence, feedback loops
├── technical/                  ← AI, software, context engineering, APIs
│   └── repo-insights/          ← Per-repository extracted intelligence
├── operations/                 ← Work patterns, tool mastery, friction points
├── patterns/                   ← Cross-domain recurring patterns
├── decisions/                  ← Decision patterns and meta-decisions
└── clusters/                   ← Synthesis clusters for major themes
```

---

## Link Convention

Every knowledge file participates in the link graph:

**Frontmatter connections (structured):**
```yaml
connections: [context-engineering, memory-continuity-system, progressive-loading]
```

**Body links (inline, bidirectional-intent):**
```markdown
See also: [[context-engineering]] for how this applies to session management.
```

**Back-references (added by /promote workflow):**
When a note B links to note A, note A should eventually gain an entry:
```markdown
## Referenced By
- [[note-B]] — relevant because [reason]
```

**Rule:** Never add a connection frontmatter entry without having a corresponding `[[link]]` in the body that explains *why* these concepts connect.

---

## Retrieval Protocol

Four retrieval modes, in order of precision:

1. **Direct lookup** — You know the note slug. Read `knowledge/<domain>/<slug>.md` directly.
2. **Index scan** — You know the domain or tag. Grep `knowledge/KNOWLEDGE-INDEX.md`.
3. **Full-text search** — You know keywords. Grep the `knowledge/` tree.
4. **Cluster synthesis** — You need a cross-domain view. Read `knowledge/clusters/<theme>.md`.

Use `/recall <query>` for modes 2–3. Use cluster notes for mode 4.

**Index-first rule:** Before reading any knowledge file speculatively, scan the index. This is a 200-token check that prevents 2,000-token reads of irrelevant files.

---

## Knowledge Compounding Loop

```
Raw capture (notes/raw/)
    │
    ▼
/promote → Atomic concept or learning entry
    │
    ├─ Check KNOWLEDGE-INDEX.md: does this concept exist?
    │    ├─ Yes → extend the existing entry
    │    └─ No → create new file, add to index
    │
    ├─ Scan for connections: does this link to existing concepts?
    │    └─ Add [[links]] to the new note
    │    └─ Add back-references to linked notes
    │
    └─ Check: does this complete a cluster threshold (5+ notes in a theme)?
         └─ Yes → trigger /synthesize for that cluster
```

**Cluster threshold:** When 5+ atomic notes share a domain or theme, generate a cluster note. Clusters are synthesis outputs, not filing folders.

---

## Meeting Intelligence → Knowledge Pipeline

```
Meeting debrief output
    │
    ├─ Action items → execution/action-items.md (immediate)
    ├─ Decisions → decision-frameworks/decisions-log.md (immediate)
    │
    └─ Knowledge candidates
         │
         ▼
    /promote (within 48 hours)
         │
         ├─ Atomic concept if it's a new idea worth keeping
         ├─ Pattern entry if it's a recurring structure you recognized
         └─ Decision journal if it represents a meta-decision pattern
```

---

## Learning → Knowledge Pipeline

```
External source (book, article, course, repo, conversation)
    │
    ▼
/learn → learning/<domain>/YYYY-MM-DD-<slug>.md
    │
    ├─ Immediate capture: what + why it matters + mental model update
    │
    └─ Within 7 days: /promote → knowledge/<domain>/<slug>.md
         (if the learning reveals a durable concept worth keeping forever)
```

The `learning/` directory is a staging area. It's not permanent knowledge. Entries either get promoted or archived.

---

## Synthesis Triggers

When to run `/synthesize` on the knowledge base:

| Trigger | Condition |
|---------|-----------|
| Cluster threshold met | 5+ notes share a domain/theme — generate cluster note |
| Monthly strategy | Cross-domain patterns from the past month |
| Decision density | 5+ decisions in the same topic area — synthesize into decision pattern |
| Repository learning complete | After `/repo-learn` on a significant repo |
| Strategic question arises | "How do we think about X?" — synthesize before answering |

---

## Decay and Freshness

Knowledge that isn't reviewed doesn't compound — it rots.

| Note type | Review frequency | Staleness signal |
|-----------|-----------------|-----------------|
| Atomic concepts | Every 90 days | `reviewed:` date in frontmatter |
| Clusters | After major updates to member notes | Re-generate when 3+ linked notes updated |
| Patterns | After encountering the pattern again | New instance updates confidence |
| Repo insights | After repo changes significantly | Flag when repo has 50+ new commits |
| Decision patterns | After major decisions in that domain | Add to pattern when decision is logged |

`/observe` flags entries with `reviewed:` older than 90 days.

---

## Anti-Patterns

| Anti-Pattern | Symptom | Fix |
|---|---|---|
| Knowledge hoarding | Files exist, never linked, never read | Every note must be linked to at least one other. If it isn't, it shouldn't be knowledge — archive it. |
| Over-tagging | 10+ tags per note | Max 5 tags. Tags are for retrieval. If you need 10 tags to describe a note, it's two notes. |
| Wiki chaos | Nested folders with no clear schema | All atomic concepts at domain level. No sub-folders in domain directories. |
| Hierarchy trap | Topic → subtopic → sub-subtopic folders | Hierarchy is for filing, links are for thinking. Keep domain dirs flat. |
| Evergreen rot | Concept file last updated on creation date | Scheduled review + decay policy. Notes that don't get updated eventually get archived. |
| Cluster too early | Generating clusters with 2-3 notes | Wait for 5+ notes on a theme. Premature clusters are just summaries. |
