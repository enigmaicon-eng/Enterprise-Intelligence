---
name: learning-source
description: >-
  Learning source attribution analytics — which books, articles, courses, and
  repos produce the most compoundable knowledge. Groups entries by source,
  measures connection rate and synthesis reach per source. Answers "Where
  should I invest my learning time?" Do NOT use for acquisition rate tracking
  (use /learning-velocity) or gap detection (use /knowledge-gap). Requires
  ≥15 entries across ≥3 sources for meaningful signal.
version: "1.0"
changed: "2026-05-23 — initial"
output: inline (source attribution report)
---

# /learning-source — Learning Source Attribution

## When to Use

- Quarterly review: evaluate which learning sources are producing compoundable knowledge
- Deciding between two learning resources and want data on source type ROI
- Notice that a domain has many entries but few connections — trace it back to the source
- Planning a learning sprint and want to allocate time to highest-yield source types

**Do NOT use for:**
- Acquisition rate over time → `/learning-velocity`
- What domains are missing → `/knowledge-gap`
- Knowledge conversion funnel → `/knowledge-utilization`
- Quality scoring individual entries → `/knowledge-qa`

**Minimum viable signal: ≥15 entries across ≥3 distinct sources. Below this, patterns are noise.**

---

## Input

```
/learning-source                  ← Full attribution report (all sources)
/learning-source --type book      ← Filter to one source type
/learning-source --top 5          ← Top 5 sources by entry yield only
```

---

## Process

### Step 1 — Read entry source metadata

Read `knowledge/KNOWLEDGE-INDEX.md` for the full entry list. For each entry, read the frontmatter `source` field (written by `/learn` as title + type) and `domain` field.

Entries without a `source` field were likely promoted manually — group them under "Observation / Direct."

### Step 2 — Read graph for connection data

Read `knowledge/KNOWLEDGE-GRAPH.json`. For each entry, count its edges. An entry is "connected" if it has ≥1 edge of any type.

### Step 3 — Check synthesis reach

Scan `knowledge/clusters/` and `synthesis/` file names. For each entry, check if its title appears in any cluster or synthesis document. An entry has "synthesis reach" if it appears in any synthesis memo or cluster synthesis.

### Step 4 — Compute per-source metrics

For each source:
- **Entry yield**: total entries attributed to this source
- **Domain spread**: number of distinct domains the source contributed to
- **Connection rate**: (connected entries from source) ÷ (total entries from source) × 100%
- **Synthesis reach**: (entries from source that appear in any synthesis) ÷ (total from source) × 100%

### Step 5 — Compute per-type aggregates

Group sources by type (book / article / course / repo / observation). Average the metrics across sources of each type. This gives source TYPE ROI independent of individual source quality.

### Step 6 — Rank and flag

Rank sources by: connection rate first (high = dense, compoundable), then entry yield (high = productive source), then synthesis reach.

Flag:
- **High yield, low connection**: many entries but few edges — these entries need `/knowledge-connect` work
- **Low yield, high connection**: few entries but all connected — source is precise, not verbose; valuable
- **High synthesis reach**: entries from this source appear in multiple syntheses — the source is cross-domain

---

## Output Format

```
LEARNING SOURCE ATTRIBUTION
[N] entries from [S] sources

SOURCE RANKINGS

Rank | Source | Type | Entries | Connection Rate | Synthesis Reach
-----|--------|------|---------|----------------|----------------
1    | [title]| book |   [N]   |     [X]%       |     [X]%
2    | [title]| ...  |   [N]   |     [X]%       |     [X]%
[...]

SOURCE TYPE AGGREGATES

Type         | Avg Entries | Avg Connection Rate | Avg Synthesis Reach
-------------|-------------|--------------------|-----------------
Book         |    [N]      |       [X]%         |       [X]%
Article      |    [N]      |       [X]%         |       [X]%
Course       |    [N]      |       [X]%         |       [X]%
Repository   |    [N]      |       [X]%         |       [X]%
Observation  |    [N]      |       [X]%         |       [X]%

FLAGS

High yield / low connection: [sources needing /knowledge-connect work]
High synthesis reach: [sources contributing cross-domain compounding]

INSIGHT
[1-2 sentences: which source type is producing the most compoundable knowledge for this operator, and what to do about it]
```

---

## Quality Gate

Before outputting:
- [ ] Source metadata read from actual entry frontmatter, not inferred from file names
- [ ] Connection rate computed from actual graph edges, not estimated
- [ ] Synthesis reach checked against actual cluster/synthesis file contents (entry title present)
- [ ] If <15 entries or <3 sources: report this explicitly and do not surface rankings
- [ ] Insight is a concrete recommendation, not a restatement of the table
- [ ] Source type aggregates computed across ≥3 sources per type to be meaningful; otherwise labeled "[insufficient sample]"
