---
name: knowledge-gap
description: >-
  Proactive knowledge gap analysis and synthesis opportunity detection. Reads
  KNOWLEDGE-INDEX.md and KNOWLEDGE-GRAPH.json to surface where the knowledge
  base is thin, stale, orphaned, or synthesis-ready. Gap detection is
  systematic, not reactive. Use before a learning sprint, during a weekly
  review, or when the knowledge base feels large but underconnected. Do NOT
  run before the knowledge base has >10 entries — below critical mass,
  results are noise.
version: "1.0"
changed: "2026-05-23 — initial"
output: inline (gap register with prioritized next actions)
---

# /knowledge-gap — Proactive Gap Analysis

## When to Use

- Starting a new learning sprint and want to know where to focus
- Knowledge base has grown but synthesis hasn't kept up
- Long time since last gap check (>60 days or >20 new entries)
- About to run `/knowledge-cluster` or `/synthesize` and want to know where to start
- Weekly review cadence: scan for stale + orphaned entries

**Do NOT use for:**
- Finding a specific piece of knowledge → `/recall`
- Reviewing a specific entry's quality → `/knowledge-review`
- Running QA on the whole base → `/knowledge-qa`
- Knowledge base has <10 entries → build the base first, then gap-check

**Flags:**
```
/knowledge-gap              ← Full gap analysis (all 7 gap types)
/knowledge-gap --synthesis  ← Synthesis opportunities only (types 5–7)
/knowledge-gap --stale      ← Stale + orphaned entries only (types 2–3)
```

---

## Process

### Step 1 — Load index and graph

Read `knowledge/KNOWLEDGE-INDEX.md` — get full entry list with domains, dates, connection counts.
Read `knowledge/KNOWLEDGE-GRAPH.json` — get edge counts per entry, all edge types.

Check for existing cluster syntheses in `knowledge/clusters/` and synthesis memos in `synthesis/`.

### Step 2 — Evaluate all 7 gap types

**Type 1 — Sparse domain**
Condition: domain has <3 entries despite entries in adjacent domains suggesting strategic importance.
Signal: domain appears in connections/edges but not as a source of entries.
Action: `/learn` or `/promote` raw notes in this domain.

**Type 2 — Orphaned entry**
Condition: entry has 0 connections in KNOWLEDGE-GRAPH.json AND was created >30 days ago.
Signal: no edges in or out for this node.
Action: `/knowledge-connect --discover` or `/knowledge-connect` manually.

**Type 3 — Stale entry**
Condition: entry `reviewed` date >180 days ago (or never reviewed and created >180 days ago).
Signal: `reviewed` field is old or absent.
Action: `/knowledge-review` on that entry.

**Type 4 — Connection gap**
Condition: entry is isolated but has obvious neighbors — entries in the same or adjacent domains that don't link to it.
Signal: domain overlap in titles/tags without graph edges.
Action: `/knowledge-connect --discover` across that domain.

**Type 5 — Synthesis gap**
Condition: 5+ entries are connected (form a cluster) but no cluster synthesis document exists in `knowledge/clusters/`.
Signal: connected component ≥5 nodes, no cluster file matching that domain.
Action: `/knowledge-cluster` on that cluster.

**Type 6 — Never-synthesized domain**
Condition: domain has 3+ entries, no synthesis memo in `synthesis/` covers it, and no cluster synthesis exists.
Signal: domain appears in KNOWLEDGE-INDEX but not in any synthesis/ file names or cluster files.
Action: `/synthesize` on that domain.

**Type 7 — Aging cluster**
Condition: cluster synthesis was created >90 days ago AND new entries have been added to its domain since then.
Signal: cluster file date older than 90 days + new entries in same domain exist.
Action: `/knowledge-cluster` re-run to incorporate new entries.

### Step 3 — Prioritize gaps

Priority order:
1. Synthesis gaps (Type 5) + Never-synthesized (Type 6) — highest leverage; existing knowledge underutilized
2. Aging clusters (Type 7) — synthesis is stale; misleading if relied on
3. Orphaned entries (Type 2) — knowledge isolated from the graph doesn't compound
4. Connection gaps (Type 4) — missed connections = missed insights
5. Stale entries (Type 3) — accuracy risk if used in synthesis
6. Sparse domains (Type 1) — acquisition gaps; lower urgency than integration gaps

Do not report gaps as a flat list. Group by type, prioritize by leverage.

### Step 4 (--synthesis flag)

Show only Types 5, 6, 7. For each, show the cluster/domain, entry count, and last synthesis date (or "never"). Sorted by entry count descending — highest-leverage synthesis first.

---

## Output Format

```
KNOWLEDGE GAP ANALYSIS
Entries: [N] across [D] domains
Last gap analysis: [date or "first run"]

── HIGH PRIORITY: Synthesis Gaps ──

Synthesis Gap: [domain/cluster name]
  Entries in cluster: [N] — [list entry titles]
  No cluster synthesis exists.
  → /knowledge-cluster [domain]

Never-synthesized domain: [domain]
  Entries: [N] — [list titles]
  No synthesis memo or cluster doc found.
  → /synthesize [domain]

── MEDIUM PRIORITY: Integration Gaps ──

Orphaned entry: "[entry title]" ([domain])
  0 connections. Created [date] ([N] days ago).
  → /knowledge-connect --discover "[entry title]"

Connection gap: "[entry title]" ([domain])
  [N] entries in same domain without edges to this entry.
  → /knowledge-connect --discover [domain]

── LOWER PRIORITY ──

Stale entry: "[entry title]" ([domain])
  Last reviewed: [date] ([N] days ago).
  → /knowledge-review "[entry title]"

Sparse domain: [domain]
  [N] entries. Referenced in [M] connections from other domains.
  → /learn [suggested source type] or /promote pending notes

── SYNTHESIS OPPORTUNITIES ──
[Aging clusters listed here with last synthesis date]

SUMMARY
[X] gaps found: [N] high / [N] medium / [N] lower priority
Top recommended action: [single most-leveraged next step]
```

If 0 gaps of a given type: omit that section header entirely.

---

## Quality Gate

Before outputting:
- [ ] Both KNOWLEDGE-INDEX.md and KNOWLEDGE-GRAPH.json were read (not inferred)
- [ ] Orphaned entry check uses actual edge count from graph, not estimated
- [ ] Stale check uses actual `reviewed` field dates, not entry creation dates
- [ ] Synthesis gaps confirmed by checking clusters/ directory, not just inferred
- [ ] Priority ordering respected (synthesis > aging > orphaned > connection > stale > sparse)
- [ ] If <10 entries total: report this and recommend building the base before gap analysis
- [ ] --synthesis flag shows only Types 5-7; does not show acquisition gaps
