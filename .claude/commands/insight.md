# /insight — Strategic Insight Accumulation

## Purpose
Extract cross-domain connections not yet explicitly documented. Reads across knowledge clusters to surface structural patterns, causal bridges, and insight compounds. Output is either a new pattern entry or a cross-domain connection added to KNOWLEDGE-INDEX.md. Not a summary — a synthesis that produces a net-new claim.

## Trigger Signals
- User invokes `/insight`
- User invokes `/insight [domain or cluster]`
- After completing 3+ knowledge entries in the same domain
- After a bet closes with learnable outcome
- Monthly cognitive review (synthesis section)

## Input
- No argument: read `knowledge/clusters/` and the most recently-updated domain, find the highest-density connection opportunity
- Domain name: focus synthesis on `knowledge/<domain>/` entries
- Cluster name: synthesize across a specific cluster
- Topic: grep `knowledge/` for the topic; synthesize across all matching entries

## Execution Protocol

**Step 1: Load the source material**
Read the target entries. For a domain: read all files in `knowledge/<domain>/`. For a cluster: read `knowledge/clusters/<cluster>.md` and follow its member links. For a topic: grep `knowledge/` and read the top 5 matching entries.

Also read `knowledge/patterns/index.md` to identify what's already documented — only generate connections that aren't there yet.

**Step 2: Generate candidate connections**
For each pair of concepts across the loaded entries: what is the structural relationship? Candidate types:

- **Mechanism bridge:** Concept A explains the mechanism behind Concept B
- **Prerequisite:** Concept A is required for Concept B to function
- **Constraint:** Concept A limits or bounds Concept B
- **Generalization:** Concept A is the domain-general version of Concept B
- **Analog:** Concept A in domain X is structurally equivalent to Concept B in domain Y
- **Compounding:** Combining A and B produces a capability neither has alone

**Step 3: Score candidate connections**
For each candidate:
- **Specificity:** Is the connection specific enough to generate a prediction or action? "Context quality and decision quality are related" fails. "Context degradation in the knowledge layer produces overconfident strategy recommendations because outdated evidence is indistinguishable from current evidence at read-time" passes.
- **Non-obviousness:** Would this connection be obvious to someone who read both source entries? If yes, it's documentation, not insight.
- **Actionability:** Does the connection change what you would do in a specific situation? If not, it's interesting but not operationally useful.

Only connections that pass all three criteria proceed.

**Step 4: Draft the insight**
For each qualifying connection:

```
INSIGHT: [one-sentence claim that is the net-new synthesis]
Source A: [entry] → [specific claim]
Source B: [entry] → [specific claim]
Connection type: [Mechanism bridge | Prerequisite | Constraint | Generalization | Analog | Compounding]
Mechanism: [why does A relate to B? what is the causal or structural link?]
Prediction: [what would you expect to observe if this connection is valid?]
Operational implication: [what does this change about how you act?]
Confidence: [high | medium | low]
```

**Step 5: Route the output**

For a qualifying insight that meets all 3 score criteria:
- If it fits an existing pattern in `knowledge/patterns/index.md`: add it as evidence under that pattern
- If it's a new pattern: write a full pattern entry via `/pattern` workflow
- If it's a cross-domain connection but not quite a full pattern: add to `KNOWLEDGE-INDEX.md` under "Cross-Domain Connections" table

For a connection that's interesting but not specific enough: note it in the insight output as "promising but underspecified — needs more evidence before pattern entry."

**Step 6: Output**

Format:
```
INSIGHT SESSION — [date]
Source material: [files read]

QUALIFYING INSIGHTS:

[1] INSIGHT: [claim]
    Source A: [citation]
    Source B: [citation]
    Connection type: [type]
    Mechanism: [causal/structural link]
    Prediction: [what to observe]
    Operational implication: [what changes]
    Confidence: [level]
    Routed to: [patterns/index.md | KNOWLEDGE-INDEX.md cross-domain table | new pattern entry]

[repeat]

PROMISING BUT UNDERSPECIFIED:
    [connections worth watching but not yet ready to document]

KNOWLEDGE GAPS SURFACED:
    [domains where synthesis is blocked because an entry doesn't exist yet]
```

## Constraints
- Generate a minimum of 1 qualifying insight, maximum of 3, per invocation. If no qualifying insights emerge, report that explicitly — it is better to have nothing than to pad with weak connections.
- Do not synthesize across more than 2 source entries per insight. Three-way connections dilute specificity.
- Do not add to `knowledge/patterns/index.md` without a full mechanism statement. Pattern lists without mechanism are noise.
- Insights must be falsifiable — they must generate a prediction that could be proven wrong.
