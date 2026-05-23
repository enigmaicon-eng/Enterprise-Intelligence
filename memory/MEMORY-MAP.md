# Memory Map
## Navigation and Retrieval Guide for the P16 Memory System

---

## Quick Navigation

| What you want | Where to look | Skill |
|---------------|--------------|-------|
| What happened on date X | `memory/episodic/` | `/mem-recall --type episodic --date X` |
| Current understanding of concept X | `memory/semantic/` | `/mem-recall --topic X --type semantic` |
| Why decision D was made | `memory/decisions/` | `/mem-adr view dec_*` |
| How to execute task type T | `memory/execution/` | `/mem-recall --topic T --type execution` |
| What went wrong with F | `memory/failures/` | `/mem-recall --topic F --type failure` |
| Recurring pattern P | `memory/insights/` | `/mem-recall --topic P --type insight` |
| State of topic T when I last worked on it | `memory/context/` | `/mem-reconstruct T` |
| Everything relevant to topic T | All types | `/mem-recall T` (no type filter) |
| Memory health | All types | `/mem-hygiene` |

---

## Memory Type Map

```
memory/
│
├── episodic/            Layer 1 — Fast decay (14-day review)
│   └── ep_*.md          What happened + why I did it that way
│
├── semantic/            Layer 3 — Medium decay (30-day review)
│   └── sem_*.md         Current working concepts (mutable)
│
├── decisions/           Layer 4 — Slow decay (90-day review)
│   └── dec_*.md         Architecture Decision Records
│
├── execution/           Layer 2 — Medium decay (30-day review)
│   └── exec_*.md        Task-type execution lessons (1 file per type)
│
├── failures/            Layer 2 — Medium decay (30-day review)
│   └── fail_*.md        Failure records + causal chains
│
├── insights/            Layer 4 — Slow decay (90-day review)
│   └── ins_*.md         Distilled recurring patterns (≥3 observations)
│
├── context/             Layer 3 — Medium decay (30-day review)
│   └── ctx_*.md         Per-topic context reconstructions
│
├── archive/             Archived entries (not active retrieval)
│   ├── YYYY-MM/
│   └── ARCHIVE-LOG.md
│
├── MEMORY.md            Orientation index (original, unchanged)
├── MEMORY-MAP.md        This file
├── MEMORY-LIFECYCLE.md  Decay rules, review cadence, pruning
└── RETRIEVAL-INDEX.json Machine-readable manifest (generated)
```

---

## How Retrieval Works

`/mem-recall` reads `RETRIEVAL-INDEX.json` (the manifest) rather than scanning the filesystem. This means:

1. **The index must be current.** Run `python scripts/memory_index.py` after adding or modifying memory files.
2. **Retrieval scores on:** recency × relevance × link density. A highly-linked entry scores higher than an isolated one.
3. **Type filters narrow results.** Without a type filter, `/mem-recall` searches all 7 types.
4. **Time range works on:** episodic (`timestamp`), decision (`date`), failure (`last_seen`), context (`as_of`).

---

## ID Cross-Reference

All memory files use typed IDs. When a memory file links to another, it uses the ID directly:

```yaml
linked_to: [dec_20260522_001, ep_20260601_003, wf_20260522_001]
```

IDs can cross-reference:
- Other memory types: `ep_*`, `sem_*`, `dec_*`, `exec_*`, `fail_*`, `ins_*`, `ctx_*`
- Workflow IDs from P13/P15: `wf_*`
- Knowledge file paths: `knowledge/pm/product-strategy.md`
- Checkpoint IDs from P15: `ckpt_*`

---

## When to Use Memory vs. Knowledge

| Signal | Use Memory | Use Knowledge |
|--------|-----------|---------------|
| Idea is new, not yet validated | ✓ (semantic) | |
| Understanding will likely change | ✓ (semantic) | |
| Operational pattern (how to work) | ✓ (insight/execution) | |
| Domain knowledge (what to know) | | ✓ |
| Needs to survive 2+ years | | ✓ |
| Something that happened | ✓ (episodic) | |
| A decision and its reasoning | ✓ (decision ADR) | |
| Stable concept, well understood | | ✓ (promote from semantic) |

---

## Maintenance Checklist

Run `/mem-hygiene` weekly. It surfaces:
- [ ] Entries past `review_date`
- [ ] Episodic entries with 0 links older than 30 days
- [ ] Semantic entries with `confidence: low` older than 60 days
- [ ] Context reconstructions older than 30 days on active topics
- [ ] Insights with `counter_evidence_count > evidence_count`
- [ ] Archive log inconsistencies (entries in archive not in log)
- [ ] RETRIEVAL-INDEX.json staleness (files present but not indexed)
