# Synthesis Prompts
## Version: v1.0

---

## Cross-Domain Connection Extraction

```
Read: [list the 2-3 source files to synthesize across]

For each pair of concepts across these files:
1. State the candidate connection in one sentence
2. Classify the connection type:
   Mechanism bridge | Prerequisite | Constraint | Generalization | Analog | Compounding
3. Score against three criteria:
   - Specific enough to generate a prediction? [Yes | No]
   - Non-obvious to someone who read both sources? [Yes | No]
   - Changes what you would do in a specific situation? [Yes | No]

Only connections that pass all three criteria proceed.

For each passing connection:
  Mechanism: [the causal or structural link — not just "they're related"]
  Prediction: [what you would expect to observe if this connection is valid]
  Operational implication: [what changes about how you act]

Output: only passing connections. State explicitly if no connections pass.
```

---

## Cluster Synthesis

```
Read: knowledge/clusters/[cluster name].md and all member entries it references.

Current documented connections in KNOWLEDGE-INDEX.md (cross-domain section): [list existing connections]

Identify connections not yet in that list. For each candidate:
- Is it more specific than what's already documented?
- Does it have a mechanism (not just a correlation)?
- Does it generate a falsifiable prediction?

Output:
  New connections: [list, with mechanism and prediction for each]
  Existing connections confirmed by this cluster: [list]
  Gaps in the cluster (concepts that should be here but aren't): [list]
```

---

## Bet-to-Principle Extraction

```
Read: strategy/bets/[bet file] and strategy/postmortems/[postmortem if exists]

The bet outcome contains a learning. Extract it.

Step 1: What was predicted vs. what happened?
Step 2: What assumption drove the bet that turned out to be wrong or right?
Step 3: State the extracted principle:
  "When [conditions], [outcome]. This bet provides evidence because [specific mechanism]."
Step 4: Is this principle already in knowledge/decisions/decision-patterns.md?
  If yes: add this bet as evidence
  If no: draft a new entry
Step 5: Does this principle connect to any existing pattern in knowledge/patterns/index.md?
  If yes: add the link
```

---

## Domain Completion Check

```
Read: knowledge/[domain]/ — all entries.

Assess the domain's coverage:
1. What are the most important concepts in this domain that don't have an entry?
2. Which entries are thin (< 300 words, or missing the ## In Practice section)?
3. Which entries have no connections listed?
4. Which entries have been reviewed least recently?

Output a prioritized gap list:
  Priority 1: Missing entries that are likely load-bearing for decisions in this domain
  Priority 2: Thin entries that need depth
  Priority 3: Entries with no connections (isolated knowledge is fragile knowledge)
  Priority 4: Stale entries by reviewed date
```
