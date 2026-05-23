# Knowledge Validation + Quality Assurance System
## Maintaining Signal Integrity in the Knowledge Graph

---

## What This System Is

P18 adds a quality assurance layer over the knowledge compounding system (P17). Where P17 builds the graph, P18 keeps it honest. A knowledge base that grows without quality controls develops three failure modes:

1. **Confidence drift** — entries stay "high confidence" long after the evidence base that justified that rating has gone stale
2. **Structural decay** — entries missing frontmatter fields (tags, reviewed dates, confidence) participate poorly in retrieval, silently degrading search quality
3. **Coverage blind spots** — domains go thin or go unexamined; topics appear in tags but have no dedicated entry

P18 does not replace `/misconception` (logic integrity), `/knowledge-review` (spaced repetition), or `/knowledge-graph` (graph stats). It operates at the structural and calibration level — questions that can be answered by examining metadata and graph topology without requiring LLM reasoning on content.

---

## Quality Dimensions

Every knowledge entry is evaluated on five dimensions:

### 1. Structural Completeness (0–40 pts)
Required frontmatter fields. Missing fields silently degrade retrieval.

| Field | Points | Why it matters |
|-------|--------|---------------|
| `title` | 10 | Entry identity; used in keyword matching |
| `confidence` | 10 | Determines retrieval weighting (×0.20) |
| `reviewed` date | 10 | Determines recency score (×0.15) |
| ≥2 `tags` | 10 | Tag matching contributes ×0.10 to retrieval |

### 2. Retrieval Readiness (0–30 pts)
How well the entry participates in graph-scored retrieval.

| Condition | Points |
|-----------|--------|
| ≥1 connection in graph | 15 |
| Reviewed within 180 days | 15 |

### 3. Content Richness (0–20 pts)
Thin entries provide no retrieval value even if well-tagged.

| Condition | Points |
|-----------|--------|
| Body content > 300 chars | 10 |
| Body content > 800 chars | 10 (additional) |

### 4. Confidence Calibration (flags, not points)
Calibration issues are flagged separately — they affect trust, not just retrieval:

| Flag | Condition | Risk |
|------|-----------|------|
| `HIGH_NO_CORROBORATION` | confidence=high, 0 connections, never re-reviewed | Unverifiable confidence |
| `HIGH_STALE` | confidence=high, reviewed > 180 days | Confident in stale information |
| `LOW_MATURE` | confidence=low, reviewed 3+ times, 0 promotions | Should be medium or removed |
| `CONFIDENCE_MISSING` | No confidence field | Defaults to medium in retrieval; may be wrong |

### 5. Graph Integrity (flags, not points)
Edge-level problems that cause silent retrieval failures:

| Flag | Condition |
|------|-----------|
| `DEAD_LINK` | Edge points to a node_id with no corresponding file on disk |
| `ASYMMETRIC_CONTRADICTION` | A contradicts B, but B has no edge back to A |
| `SELF_REFERENCE` | Edge where from == to |

---

## Quality Score Bands

| Score | Band | Interpretation |
|-------|------|---------------|
| 80–100 | Strong | Participates fully in retrieval; well-calibrated |
| 60–79 | Adequate | Minor gaps; fix before next review |
| 40–59 | Weak | Significant structural or retrieval issues |
| 0–39 | Critical | Entry is likely invisible in retrieval |

---

## Validation Pipeline

```
Entry file (*.md)
    ↓
parse_frontmatter()         → structural completeness score
    ↓
load_graph_node()           → retrieval readiness (connections, reviewed date)
    ↓
measure_content_richness()  → content score
    ↓
check_calibration()         → confidence flags
    ↓
check_graph_integrity()     → dead links, asymmetric edges
    ↓
QualityReport {
    score: int (0-90),
    band: "Strong | Adequate | Weak | Critical",
    calibration_flags: list[str],
    integrity_flags: list[str],
    recommendations: list[str]
}
```

---

## QA Report Structure

The aggregate report (from `knowledge_qa_report.py`) provides:

### Coverage Analysis
- Nodes per domain (absolute and %)
- Domains with < 3 entries ("thin domains")
- Tag frequency distribution — topics that appear in 3+ tags but have no dedicated entry

### Quality Distribution
- Count of entries per band (Strong / Adequate / Weak / Critical)
- Domain-level breakdown of weak/critical entries

### Confidence Calibration Summary
- Total HIGH_NO_CORROBORATION flags
- Total HIGH_STALE flags
- Total LOW_MATURE flags
- Promotion candidates (low → medium, medium → high)

### Graph Integrity
- Dead links count and list
- Asymmetric contradictions
- Entries with 0 connections (orphans — also available in `/knowledge-graph --orphans`)

### Missed Connection Candidates
Pairs of entries in the same domain with ≥3 shared tags but no edge between them. These are not confirmed connections — they are surface candidates for human review.

---

## Integration Map

| P17 Component | P18 Extends It By |
|--------------|-------------------|
| `KNOWLEDGE-GRAPH.json` | Validating edge integrity (dead links, asymmetric edges) |
| `knowledge_index.py` | `knowledge_validate.py` uses same node scan |
| `/knowledge-review` | QA surfaces calibration drift that review schedule alone misses |
| `/misconception` | QA flags structural issues; misconception checks logical content |
| `/knowledge-graph` | QA adds quality scoring; graph adds stats |

---

## Anti-Patterns

| Pattern | Why Forbidden |
|---------|--------------|
| Marking everything "high confidence" to boost retrieval scores | Inflates confidence weight in scoring; degrades signal |
| Adding tags without reviewing content | Improves retrieval hit rate but returns low-quality results |
| Ignoring DEAD_LINK flags | Silent retrieval failures — neighbor traversal breaks |
| Conflating QA score with knowledge value | A well-structured thin entry scores higher than a deep poorly-tagged one |
| Using QA score to delete entries | Low score = needs improvement, not deletion; use human judgment |
