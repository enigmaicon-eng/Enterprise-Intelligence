# Personal Learning Analytics System

Analytics layer on top of the knowledge compounding system. Answers the questions the compounding system captures data for but never surfaces: How fast am I learning? Where is my learning coming from? Is the knowledge I capture actually compounding?

## Existing Coverage (Do Not Duplicate)

| Skill | What It Covers |
|-------|---------------|
| `/knowledge-qa` | Quality scoring per entry (0–90), calibration flags, dead link detection |
| `/knowledge-review` | Freshness and accuracy check for a specific entry |
| `/knowledge-gap` | Gap taxonomy (7 types), synthesis opportunities, next actions |
| `/retrieval-diag` | Recall readiness tiers (entry count vs search coverage) |
| `/recall-test` | Active recall testing of a specific entry |
| `/skill-stats` | Skill invocation analytics from trace history |

## New Skills (P26)

| Skill | Fills Gap | Core Question |
|-------|----------|--------------|
| `/learning-velocity` | Acquisition rate is never tracked over time | "Am I learning faster or slower? Which domains are growing?" |
| `/learning-source` | Source attribution is never analyzed | "Which books/articles/courses yield the most compoundable knowledge?" |
| `/knowledge-utilization` | Conversion funnel is never measured | "How much of what I capture actually compounds?" |

## Capability Distinctions

```
How many entries do I have and are they high quality?
→ /knowledge-qa  (quality scoring, calibration)

What is missing from my knowledge base?
→ /knowledge-gap  (gap taxonomy, next actions)

Am I learning faster or slower over time, and in which domains?
→ /learning-velocity  (time-series acquisition, domain growth curves)

Which learning sources are most valuable?
→ /learning-source  (source attribution, connection rate per source)

What fraction of my captured knowledge is actually compounding?
→ /knowledge-utilization  (conversion funnel: captured → connected → synthesized)
```

## Learning Velocity Model

`/learning-velocity` reads KNOWLEDGE-INDEX.md and parses creation dates to construct a time series.

```
Time window → entry count → domain breakdown
→ 30-day rolling rate (entries per week)
→ Domain growth rate: (entries last 90 days) / (total entries)
→ Momentum classification: Accelerating / Steady / Decelerating / Stalled

Stalled domain: no new entries in >90 days AND <5 total entries
Decelerating: rate in last 30 days < rate in prior 30 days by >50%
Accelerating: rate in last 30 days > rate in prior 30 days by >50%
```

## Source Attribution Model

`/learning-source` reads entry files for `source` metadata (written by `/learn`). Source types:

| Source Type | Connection Rate Baseline |
|-------------|------------------------|
| Book | High (dense, structured concepts) |
| Article | Medium (often single-concept) |
| Course | Medium-high (curated progression) |
| Repository | Variable (depends on domain) |
| Observation | Low (raw; needs promotion + connection work) |

Attribution metrics per source:
- **Entry yield**: total entries extracted
- **Connection rate**: % of entries with ≥1 graph edge
- **Synthesis reach**: entries from this source that appear in any synthesis or cluster doc

## Utilization Funnel

`/knowledge-utilization` measures conversion at each stage:

```
Stage 1: Captured (any entry in knowledge/)
Stage 2: Promoted (permanent entry, not raw note)
Stage 3: Connected (≥1 edge in KNOWLEDGE-GRAPH.json)
Stage 4: Synthesized (appears in any cluster or synthesis memo)

Utilization rate = Stage 3 / Stage 1
Synthesis coverage = Stage 4 / Stage 1
Dormant knowledge = permanent entries at Stage 2 (connected: 0, synthesized: no) for >60 days
```

## Data Sources

```
knowledge/
  KNOWLEDGE-INDEX.md     ← primary index (all 3 skills)
  KNOWLEDGE-GRAPH.json   ← edge counts (learning-source, knowledge-utilization)
  clusters/              ← synthesis coverage check (knowledge-utilization)
  <domain>/<entry>.md    ← source metadata, creation dates (learning-source)

synthesis/               ← synthesis memo coverage (knowledge-utilization)
```

## Recommended Cadence

- **Monthly**: `/learning-velocity` — check acquisition rate and domain momentum
- **Quarterly**: `/learning-source` — evaluate source quality and rebalance
- **Monthly**: `/knowledge-utilization` — check conversion funnel; chase dormant entries
- **Trigger**: run `/knowledge-utilization` before any `/knowledge-cluster` session

## Anti-Patterns

| Anti-pattern | Why it fails |
|-------------|-------------|
| Optimizing for entry count (velocity) over connection rate (utilization) | Raw acquisition without synthesis is just hoarding; utilization rate matters more |
| Running /learning-source on <15 entries | Attribution requires sufficient sample; below threshold, the signal is noise |
| Treating dormant entries as failures | Dormancy flags a connection opportunity, not a bad entry — act with /knowledge-connect, not deletion |
| Using /learning-velocity to judge domain importance | Slow growth in a mature domain is correct, not a problem; weight by domain size |
| Checking analytics more than monthly | These are trend signals, not dashboards — daily checking produces anxiety, not insight |
