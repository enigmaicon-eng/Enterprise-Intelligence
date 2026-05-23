# /knowledge-qa — Knowledge Quality Assurance Report

Full aggregate QA report across the knowledge graph: domain coverage, quality distribution, confidence calibration, graph integrity, missed connection candidates, and promotion recommendations.

## Trigger
`/knowledge-qa` — full report across all domains.
`/knowledge-qa --domain [domain]` — domain-specific report.
`/knowledge-qa --coverage` — domain coverage only (fast).
`/knowledge-qa --missed` — missed connection candidates only.
`/knowledge-qa --promotions` — confidence promotion candidates only.

## Relationship to Other Skills

| Skill | What it checks |
|-------|---------------|
| `/knowledge-qa` | Aggregate quality across the whole corpus |
| `/knowledge-validate` | Per-entry structural quality + fix flow |
| `/misconception` | Logical/claim integrity within entries |
| `/knowledge-review` | Spaced repetition: which entries are overdue |
| `/knowledge-graph` | Graph stats: nodes, edges, orphans, cluster candidates |

Run `/knowledge-qa` first to get the big picture. Then use the specialist skills to fix what it surfaces.

## Protocol

### Full report: `/knowledge-qa`

**Step 1:** Run `python scripts/knowledge_qa_report.py`.

**Step 2:** Parse and present the full report. Highlight the most urgent findings:

```
Knowledge QA Report
══════════════════════════════════════════════════════════
  Entries: [N]  |  Avg score: [X]/90
  Strong: [N]  |  Adequate: [N]  |  Weak: [N]  |  Critical: [N]

  Coverage:
    [domain]     [N] entries
    ...
    [domain] ← THIN (<3 entries)

  Calibration issues: [N] entries
    HIGH_STALE: [N]  — confident in stale information
    HIGH_NO_CORROBORATION: [N]  — unverifiable high confidence
    LOW_MATURE: [N]  — should be promoted or removed

  Graph integrity: [OK | N dead links found]

  Missed connection candidates: [N] pairs
    [node_a] ↔ [node_b]  (shared tags: ...)
    ...

  Promotion candidates: [N]
    [node_id]  low → medium  (accessed 4×, 2 connections)
    ...

══════════════════════════════════════════════════════════
  Priority actions:
    1. [Most urgent action based on findings]
    2. [Second priority]
    3. [Third priority]
```

**Step 3:** Prioritize what to act on.

Priority order:
1. **Dead links** (if any) — fix immediately; they cause silent retrieval failures
2. **Critical entries** — score 0–39; essentially invisible in retrieval
3. **HIGH_STALE calibration** — high confidence in stale information is the highest epistemic risk
4. **Thin domains** — coverage gaps mean retrieval fails entire topic areas
5. **Missed connection candidates** — unconnected high-overlap pairs are lost compounding value

**Step 4:** Route to the right skill for each finding:

| Finding | Action skill |
|---------|-------------|
| Dead links | `/knowledge-validate --dead-links` |
| Critical/Weak entries | `/knowledge-validate [node_id]` |
| Stale high confidence | `/knowledge-review [node_id]` |
| Logical drift in high-confidence entries | `/misconception [node_id]` |
| Thin domain | `/learn` (capture new entry) |
| Missed connections | `/knowledge-connect [a] [b] related_to` |
| Promotion candidate | `/knowledge-validate [node_id]`, update frontmatter |

---

### Coverage report: `/knowledge-qa --coverage`

Run `python scripts/knowledge_qa_report.py --coverage`.

Shows entry count per domain. Thin domains (< 3 entries) are flagged. Useful before a `/learn` session to identify where to focus new knowledge capture.

---

### Missed connections: `/knowledge-qa --missed`

Run `python scripts/knowledge_qa_report.py --missed`.

Pairs of entries in the same domain with ≥3 shared tags but no edge between them. These are heuristic candidates — shared tags suggest conceptual overlap, but not every candidate is a real connection. The operator decides.

For each candidate:
```
pm/product-strategy ↔ pm/metrics-experimentation
  shared tags: strategy, metrics, prioritization

Connect? (yes [type] / no / skip)
```

If confirmed, runs the `/knowledge-connect` flow for that pair.

---

### Promotion candidates: `/knowledge-qa --promotions`

Run `python scripts/knowledge_qa_report.py --promotions`.

Entries whose usage patterns suggest confidence should be upgraded:
- `low → medium`: accessed 3+ times, has ≥1 connection (no longer untested)
- `medium → high`: accessed 5+ times, ≥3 connections, 2+ compound events (evidence has accumulated)

For each candidate:
```
pm/product-strategy  medium → high
  Reason: accessed 7×, 4 connections, 3 compound events
  
Update confidence? (yes / no)
```

If confirmed, update the `confidence` field in the entry's frontmatter. Rebuild index. Log:
```
| [YYYY-MM-DD] | REVIEW | [node_id] — confidence: medium→high (QA promotion) |
```

## When to Run

**Weekly (light):** `/knowledge-qa --coverage` — check if any domain is thinning out.

**Monthly (full):** `/knowledge-qa` — full report, prioritize findings, schedule fix session.

**After any batch `/learn` session:** Run to see how new entries affected coverage and identify immediate connection candidates.

**After graph edit (connection add, cluster synthesis):** Check for new missed connections at the graph's new topology.
