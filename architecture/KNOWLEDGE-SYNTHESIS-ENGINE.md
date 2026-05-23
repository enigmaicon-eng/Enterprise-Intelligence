# Knowledge Synthesis Engine

Three skills that extend the existing knowledge compounding system with higher-order synthesis capabilities: cross-domain analogical reasoning, contradiction management, and proactive gap and synthesis-opportunity detection.

## Existing Knowledge System (Do Not Duplicate)

| Skill | What It Covers |
|-------|---------------|
| `/learn` | Captures new knowledge from book, article, course, repo → knowledge/<domain>/ |
| `/promote` | Promotes raw notes to permanent knowledge entries |
| `/recall` | Graph-scored retrieval (5-component score, Python-backed) |
| `/synthesize` | Deep cross-domain synthesis memo → synthesis/ |
| `/knowledge-connect` | Creates/discovers connections; manages KNOWLEDGE-GRAPH.json |
| `/knowledge-cluster` | Synthesizes 5+ connected entries into cluster document |
| `/knowledge-review` | Review entries for quality and freshness |
| `/knowledge-validate` | Validates entries against quality schema |
| `/knowledge-qa` | Quality assurance report |
| `/knowledge-graph` | Graph visualization and statistics |
| `/pattern` | Documents a recurring cross-domain pattern |
| `/insight` | Extracts cross-domain insights |
| `/misconception` | Diagnoses misconceptions in an entry |
| `/recall-test` | Active recall test |

## New Skills (P25)

| Skill | Fills Gap | Core Question |
|-------|----------|--------------|
| `/analogy` | No structural pattern matching across domains | "What does a case from another domain teach me about this problem?" |
| `/contradiction-register` | Contradictions in the graph are created but never managed | "What knowledge do I hold that contradicts other knowledge, and what does that mean?" |
| `/knowledge-gap` | Gap detection is reactive (triggered by failed recalls), never proactive | "Where is my knowledge base thin, stale, or synthesis-ready?" |

## Capability Distinctions

```
Given a problem/situation, find structurally analogous cases
→ /analogy  (structural similarity, cross-domain transfer)

Given a topic keyword, retrieve relevant entries
→ /recall  (keyword + graph scoring, Python-backed)

Two entries have similar concepts but in different domains — connect them
→ /knowledge-connect --discover  (graph edge creation)

Where is my knowledge weak or unintegrated?
→ /knowledge-gap  (proactive systematic analysis)

What knowledge do I have that contradicts itself?
→ /contradiction-register  (contradicts edge management)

What topics have enough entries to cluster-synthesize?
→ /knowledge-gap --synthesis  (synthesis opportunity detection, part of /knowledge-gap)
```

## Analogical Reasoning Model

`/analogy` does structural pattern matching — not keyword retrieval. The process:

```
1. Parse the problem → extract abstract structure (not surface content)
   "My AI system gives overconfident answers despite uncertainty"
   Structure: system lacks calibrated uncertainty representation

2. Search knowledge base for structurally similar patterns
   — across ALL domains, not just the obvious one

3. Map the analogy explicitly:
   Source domain element → Target problem element
   "Probabilistic forecasting (strategy domain) → confidence calibration in AI"

4. Extract the transferable insight:
   What does the source domain know that applies here?

5. Flag where the analogy breaks down:
   Where does the mapping fail? What must be adapted, not transferred?
```

## Contradiction Resolution Framework

Used by `/contradiction-register`:

| Contradiction Type | Resolution Path |
|-------------------|----------------|
| Direct reversal | One entry is wrong or outdated — determine which |
| Domain-specific | Both true in different contexts — add domain qualifier to each |
| Scope difference | One is a special case of the other — integrate as parent/child |
| Conditional | Both true under different conditions — document the conditions |
| Productive tension | Both true simultaneously — the tension is the insight; synthesize |

## Knowledge Gap Taxonomy

Used by `/knowledge-gap`:

| Gap Type | Definition | Action |
|----------|-----------|--------|
| Sparse domain | Domain has <3 entries despite strategic importance | `/learn` or `/promote` |
| Orphaned entry | Entry has 0 connections after >30 days | `/knowledge-connect` |
| Stale entry | `reviewed` field >180 days ago | `/knowledge-review` |
| Connection gap | Entry isolated despite obvious neighbors | `/knowledge-connect --discover` |
| Synthesis gap | 5+ connected entries, no cluster synthesis | `/knowledge-cluster` |
| Never-synthesized domain | Domain with 3+ entries, no synthesis ever run | `/synthesize` |
| Aging cluster | Cluster synthesized >90 days ago with new members added | `/knowledge-cluster` re-run |

## Data Sources

```
knowledge/
  KNOWLEDGE-INDEX.md          ← primary index (read by /knowledge-gap)
  KNOWLEDGE-GRAPH.json        ← graph with edges incl. contradicts (read by /contradiction-register)
  clusters/                   ← cluster syntheses (checked by /knowledge-gap)
  <domain>/                   ← entry files (loaded by /analogy + /contradiction-register)

synthesis/                    ← synthesis memos (checked by /knowledge-gap for coverage)
```

## Anti-Patterns

| Anti-pattern | Why it fails |
|-------------|-------------|
| Using /analogy instead of /recall for known-topic retrieval | Analogy requires structural abstraction; if the topic is directly indexed, /recall is faster and more precise |
| Resolving every contradiction immediately | Some contradictions are productive tensions — "both true" is often the synthesis; force-resolving destroys the insight |
| Running /knowledge-gap before the knowledge base has >10 entries | Gap analysis below critical mass produces noise; build the base first |
| Treating gap detection as a to-do list | Gaps are priorities relative to active work, not an exhaustive task queue |
| Using /knowledge-cluster before /analogy has surfaced structural patterns | Cluster is about connected entries; analogy finds structural kin that may not be connected yet |
