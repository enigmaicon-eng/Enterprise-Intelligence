---
name: knowledge-utilization
description: >-
  Knowledge utilization and conversion funnel analytics — measures how much of
  captured knowledge is actually compounding (connected, synthesized, applied).
  Surfaces dormant entries: permanent entries that have never been connected or
  synthesized after ≥60 days. Answers "Is my knowledge accumulating or
  compounding?" Distinct from /knowledge-gap (which tells you what's missing
  and what to do) — this tells you the conversion rate on what you have.
version: "1.0"
changed: "2026-05-23 — initial"
output: inline (utilization report + dormant entry list)
---

# /knowledge-utilization — Knowledge Conversion Analytics

## When to Use

- Monthly check: is captured knowledge compounding or just accumulating?
- Before a `/knowledge-cluster` or `/synthesize` session: surface dormant entries first
- After a burst of `/learn` entries: check how many have been connected
- Sense that the knowledge base is large but not generating insight: diagnose the funnel

**Do NOT use for:**
- What gaps exist and what to do about them → `/knowledge-gap`
- Entry quality scores → `/knowledge-qa`
- Learning rate over time → `/learning-velocity`
- Which sources yield the most value → `/learning-source`

---

## Input

```
/knowledge-utilization             ← Full funnel report
/knowledge-utilization --dormant   ← Dormant entries list only
/knowledge-utilization --domain <name>   ← Funnel for one domain
```

---

## Process

### Step 1 — Load index and graph

Read `knowledge/KNOWLEDGE-INDEX.md` — get all permanent entries with creation dates.
Read `knowledge/KNOWLEDGE-GRAPH.json` — get edge count per entry.

Distinguish entry types:
- **Raw note**: in `notes/raw/` or flagged as unreviewed (not in KNOWLEDGE-INDEX = not permanent)
- **Permanent entry**: indexed in KNOWLEDGE-INDEX (Stage 1 baseline)

Only permanent entries flow through the funnel. Raw notes are not counted.

### Step 2 — Check synthesis coverage

Scan `knowledge/clusters/` for cluster synthesis documents. Scan `synthesis/` for synthesis memos.

For each permanent entry, check if its ID or title appears in any cluster or synthesis document. This is "synthesized."

### Step 3 — Compute funnel stages

```
Stage 1 — Captured (permanent entries in KNOWLEDGE-INDEX):  [N]
Stage 2 — Connected (Stage 1 entries with ≥1 edge in graph): [N]  →  [X]% of Stage 1
Stage 3 — Synthesized (Stage 1 entries appearing in any cluster or synthesis memo): [N]  →  [X]% of Stage 1
```

Note: an entry can be Synthesized without being Connected (though this is unusual). Report both independently.

### Step 4 — Identify dormant entries

An entry is dormant if:
- It is a permanent entry (in KNOWLEDGE-INDEX)
- It has 0 edges in KNOWLEDGE-GRAPH.json
- It does NOT appear in any synthesis or cluster document
- Its creation date is ≥60 days ago

Sort dormant entries by age (oldest first — highest priority for connection).

### Step 5 — Domain breakdown

For each domain, compute:
- Total entries
- Connected count + rate
- Synthesized count + rate
- Dormant count

Domains sorted by dormant count descending — highest dormancy first = most connection work needed.

### Step 6 — Compute utilization rate

**Utilization rate** = Connected entries ÷ Total permanent entries × 100%
**Synthesis coverage** = Synthesized entries ÷ Total permanent entries × 100%

Benchmarks (rough):
- Utilization rate <30%: knowledge is accumulating, not compounding — prioritize /knowledge-connect
- Utilization rate 30–60%: healthy active compounding
- Utilization rate >60%: strong compounding; check if synthesis coverage is keeping up

---

## Output Format

```
KNOWLEDGE UTILIZATION
[N] permanent entries across [D] domains

CONVERSION FUNNEL

Stage 1 — Captured:    [N]  (100%)
Stage 2 — Connected:   [N]  ([X]%)  ← entries with ≥1 graph edge
Stage 3 — Synthesized: [N]  ([X]%)  ← entries appearing in a cluster or synthesis

Utilization rate:    [X]%   [Accumulating / Healthy / Strong]
Synthesis coverage:  [X]%

DOMAIN BREAKDOWN

Domain         | Entries | Connected | Synthesized | Dormant
---------------|---------|-----------|-------------|--------
[domain]       |   [N]   |  [N] [X]% |  [N] [X]%  |  [N]
[domain]       |   [N]   |  [N] [X]% |  [N] [X]%  |  [N]
[...]

DORMANT ENTRIES ([N] total — permanent, unconnected, unsynthesized, ≥60 days)

[entry title] ([domain]) — [N] days since creation
  → /knowledge-connect --discover "[entry title]"
[...]

[If 0 dormant entries: "No dormant entries. All permanent entries are connected or recent."]

INTERPRETATION
[1-2 sentences: what the funnel shape means and the single most leveraged next action]
```

---

## Quality Gate

Before outputting:
- [ ] Only permanent entries counted (entries in KNOWLEDGE-INDEX, not raw notes)
- [ ] Connection rate from actual KNOWLEDGE-GRAPH.json edge counts
- [ ] Synthesis coverage checked against actual file contents (not just cluster existence)
- [ ] Dormant entries: all 3 conditions confirmed (0 edges, unsynthesized, ≥60 days)
- [ ] Utilization classification matches the actual rate against benchmarks
- [ ] Dormant list sorted oldest-first
- [ ] Interpretation names one specific next action (not a list of all possible actions)
- [ ] --dormant flag shows only the dormant list, not the full funnel report
