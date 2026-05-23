# /recall — Graph-Aware Knowledge Retrieval

Search and retrieve relevant knowledge from the workspace knowledge base using scored retrieval with graph traversal.

## Trigger
`/recall [query]` — query can be a concept name, keywords, a question, or a topic area.
`/recall --domain pm [query]` — restrict to a specific domain.
`/recall --no-track [query]` — read-only, do not update access statistics.

## Protocol

### Step 1: Graph-scored retrieval (primary path)

Run: `python scripts/knowledge_search.py "[query]"`

This executes the 5-component retrieval algorithm:

```
score = keyword_match × 0.45
      + confidence_weight × 0.20
      + recency_weight × 0.15
      + connection_density × 0.10
      + tag_match × 0.10
```

The script returns ranked results with 1-hop neighbors already resolved. It also updates `last_accessed` and `access_count` on each retrieved node (unless `--no-track` is passed).

**If results are returned:** Read the top-ranked file(s), then proceed to Step 3.

**If no results:** Proceed to Step 2 (fallback scan).

### Step 2: Fallback — domain inference + grep

When the graph returns no results (empty knowledge base or query too specific):

Infer domain from query:
- PM terms → `knowledge/pm/`
- Strategy, bets, mental models → `knowledge/strategy/`
- Systems, feedback, emergence → `knowledge/systems/`
- AI, APIs, context, Claude → `knowledge/technical/`
- Workflow, tools, friction → `knowledge/operations/`
- Recurring patterns → `knowledge/patterns/`
- Decisions → `knowledge/decisions/`

Grep the relevant domain directory. Read top 2–3 matching files.

### Step 3: Neighbor traversal

From the top result, check its neighbors (returned in search output). If 1–2 neighbors are directly relevant to the query, read them as well.

Check `knowledge/clusters/` for any synthesis that covers the same topic — a cluster synthesis is always higher signal than individual entries.

### Step 4: Gap signal detection

If retrieval returned 0 results OR all results scored below 0.25:

- **Hard gap:** No entries on this topic at all → suggest `/learn` to create one.
- **Soft gap:** Low-confidence entries exist → surface them with the ⚠ flag and recommend enrichment.
- **Connection gap:** Entry exists but is isolated (0 neighbors) → suggest `/knowledge-connect` to add connections.
- **Stale gap:** Entry exists but `reviewed` is > 180 days ago → flag as potentially outdated.

Log gaps with: `# Gap: [query] — [gap type] — [date]` as a note in context (do not write to file automatically).

### Step 5: Report findings

Structure the response as:

1. **Found:** The key insight from the best-matching entry. Lead with the answer — do not make the user read through file paths first.
2. **Source:** `knowledge/[domain]/[slug].md` — confidence level, last reviewed date.
3. **Also see:** Up to 3 neighbor entries from graph traversal with edge type annotation (related_to / builds_on / contradicts).
4. **Gap (if any):** Named gap type and suggested action.

## Output Format

- Answer first. Source second.
- Cite the file path so the user can navigate directly.
- If confidence is `low`, flag with ⚠ before the finding.
- If two entries contradict each other, surface the tension explicitly — do not silently pick one.
- If a cluster synthesis exists on the topic, lead with it instead of individual entries.

## Access Tracking

Each `/recall` call updates `access_count` and `last_accessed` on retrieved nodes via `knowledge_search.py`. This feeds into:
- `/knowledge-review` priority scoring (frequently accessed = higher review priority)
- `/knowledge-graph --stats` gap detection (never-accessed entries)

Use `--no-track` only when auditing or previewing — access tracking is the feedback loop that makes the graph self-reinforcing.

## What This Is NOT

- `/recall` is retrieval, not synthesis. For synthesis across multiple entries, use `/synthesize` or `/knowledge-cluster`.
- `/recall` reads existing knowledge. To create new knowledge entries, use `/learn` or `/promote`.
- `/recall` is for the knowledge base. For active-project memory (episodic, semantic, decisions), use `/mem-recall`.
