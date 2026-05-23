# Memory System
## Hierarchy, Schemas, and Maintenance
## Consolidates: MEMORY-MAP.md · MEMORY-SCHEMAS.md · COGNITIVE-MEMORY-SYSTEM.md

---

## Memory Hierarchy

```
Tier 1 — Always Present (embedded in CLAUDE.md)
├── Who the user is (2-3 sentences)
├── How to interact (working style, communication preferences)
└── Target: 150 tokens, changes <monthly

Tier 2 — Orientation (memory/ flat files)
├── MEMORY.md         ← Index only. One line per file. Never write content here.
├── user_profile.md   ← Role, expertise, goals, preferences
├── project_*.md      ← Active projects (one file per active project)
└── feedback_*.md     ← Behavioral guidance from past sessions
    Target per file: <500 tokens. Total: <3,000 tokens.

Tier 3 — Domain Context (skills, loaded on demand)
├── Skill context loaded when the skill is invoked
└── Never pre-loaded into memory

Tier 4 — Episodic (distributed across workspace, read on demand)
├── meeting-intelligence/processed/  ← Processed meeting records
├── reviews/                         ← Weekly and monthly reviews
├── synthesis/                       ← Cross-domain insight memos
└── knowledge/                       ← Permanent knowledge entries
    No token budget — read only when a workflow explicitly needs them.
```

---

## Layer Placement Rules

| Content type | Layer |
|-------------|-------|
| Behavioral rules, routing, output standards | CLAUDE.md |
| User's professional role, expertise, working style | `memory/user_profile.md` |
| Active project: phase, constraints, blockers, milestone | `memory/project_*.md` |
| Behavioral guidance from past sessions | `memory/feedback_*.md` |
| External system locations and pointers | `memory/reference_*.md` |
| Permanent, synthesized knowledge concept | `knowledge/<domain>/` |
| Event-specific record (meeting, decision) | `meeting-intelligence/` or `decision-frameworks/` |
| Cross-domain insight memo | `synthesis/` |
| Ephemeral session context | Do not persist |

---

## Memory File Format

Every memory file uses this frontmatter:

```yaml
---
name: short-kebab-slug
description: One-line summary — specific enough to determine relevance without reading the file
metadata:
  type: user | feedback | project | reference
  updated: YYYY-MM-DD
---
```

**Body structure by type:**

**user:** Facts about the user organized by category (role, expertise, preferences).

**feedback:** Lead with the rule. Then `**Why:**` (reason given). Then `**How to apply:**` (scope and edge cases). Link related memories with `[[slug]]`.

**project:** Lead with the key fact. Then `**Why:**` (motivation or constraint). Then `**How to apply:**` (how this should shape suggestions). Project memories decay fast — `updated:` date matters.

**reference:** Location → Purpose → How to access (if non-obvious).

---

## MEMORY.md Index Format

MEMORY.md is a flat index. Each entry is one line:

```
- [Title](filename.md) — one-line hook, under 100 characters
```

**Hard limits:** 200 lines maximum · No line over 150 characters · Index only — never write content here.

If MEMORY.md starts to look like a document, it has absorbed content that belongs in per-file memories.

---

## Memory Loading Protocol

1. **Session start:** Read `memory/MEMORY.md`. Identify which files are relevant to the current task.
2. **Selective read:** Read only the relevant 2-3 memory files — not all of them. Reading 5+ is a sign the memory system needs restructuring.
3. **During workflow:** If new context should be persistent, note it for memory update at session end.
4. **Memory update:** Write to the specific file. Update `updated:` frontmatter. Update MEMORY.md if a new file was created.

**Never:**
- Read all memory files as a batch at session start
- Write session notes into memory (ephemeral context doesn't belong in memory)
- Let a single memory file grow beyond 500 tokens without splitting it

---

## Typed Memory Subdirectories (P16)

The `memory/` directory may contain typed subdirectories for deeper operational memory:

| Subdirectory | Type | Decay | Purpose |
|-------------|------|-------|---------|
| `memory/episodic/` | Timestamped reasoning records | 14 days | What happened and why, non-obvious reasoning context |
| `memory/semantic/` | Working concept records | 30 days | Current understanding of a concept (promote to knowledge/ when stable) |
| `memory/decisions/` | Architecture Decision Records | 90 days / permanent | Full reasoning chains for significant decisions |
| `memory/execution/` | Task execution lessons | 30 days | What works/fails for a specific task type |
| `memory/failures/` | Failure records with causal chains | 30 days | Root causes and recovery patterns |
| `memory/insights/` | Distilled strategic patterns | 90 days | High-confidence operational patterns |
| `memory/context/` | Per-topic context reconstructions | 30 days | State of a topic before returning to it |

**ID conventions:** `ep_YYYYMMDD_NNN` (episodic) · `sem_SLUG` (semantic) · `dec_YYYYMMDD_NNN` (decision) · `exec_TASKSLUG` (execution) · `fail_YYYYMMDD_NNN` (failure) · `ins_SLUG` (insight) · `ctx_SLUG` (context)

**Key rules:**
- Semantic memory promotes to `knowledge/` when `confidence: high` and understanding is stable
- Decision ADRs are never deleted — archived if superseded (`superseded_by:` set)
- Context reconstructions are regenerated, not updated in place — stale reconstructions are misleading
- Failure records increment `recurrence_count` on the existing record rather than creating duplicates

---

## Memory Freshness Rules

| Memory Type | Review Trigger | Staleness Signal |
|-------------|---------------|-----------------|
| `user_profile.md` | Quarterly or when user changes role | Expertise fields feel outdated |
| `project_*.md` | Weekly review | Phase or milestone hasn't changed in >3 weeks |
| `feedback_*.md` | When feedback is contradicted or confirmed | No sessions have referenced in >90 days |
| `reference_*.md` | When external systems change | Location no longer matches description |

**Stale protocol:** `/workspace-audit` surfaces memory files not updated per their type's freshness schedule. Either update the file or archive it to `memory/archive/`.

---

## Memory Anti-Patterns

| Anti-pattern | Fix |
|-------------|-----|
| MEMORY.md index near 200 lines | Archive completed project memories; compress feedback |
| Memory file contains detailed how-to instructions | Move to `knowledge/`; memory should point to it |
| `project_*.md` describes a phase from 6 weeks ago | Update to current phase or archive if complete |
| Behavioral preference in a feedback memory | Universal preferences belong in CLAUDE.md output standards |
| Memory files contain session summaries or tool outputs | Memory holds durable facts, not conversation history |
| Memory file for an eliminated system | Delete — historical record belongs in git history |

---

## Memory Constraints

- Maximum 30 files in `memory/` (excluding subdirectories)
- MEMORY.md index: ≤200 lines, index only
- Per-file target: <500 tokens
- Dead system memory files: deleted at next session after elimination confirmed
