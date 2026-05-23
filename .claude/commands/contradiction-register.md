---
name: contradiction-register
description: >-
  Manages contradictions in the knowledge graph. Reads KNOWLEDGE-GRAPH.json
  for all `contradicts` edges, loads the conflicting entries, classifies each
  contradiction by type, and assigns resolution status. Productive tensions
  are flagged as synthesis candidates. Use when you want to surface and work
  through knowledge that conflicts with itself. Does NOT create new
  contradicts edges (use /knowledge-connect for that). Does NOT resolve
  contradictions by deleting entries.
version: "1.0"
changed: "2026-05-23 — initial"
output: inline (contradiction register) + optional entry updates
---

# /contradiction-register — Contradiction Management

## When to Use

- Want to surface all unresolved contradictions in the knowledge base
- Preparing for synthesis work and need to clear contradictions first
- Knowledge base has grown and contradictions may have accumulated
- A new entry was added that might contradict existing knowledge

**Do NOT use for:**
- Creating new contradicts relationships → `/knowledge-connect`
- Synthesizing entries that are related but not contradictory → `/knowledge-cluster`
- Reviewing entry quality → `/knowledge-review` or `/knowledge-qa`

---

## Input

```
/contradiction-register              ← Full register: all unresolved contradictions
/contradiction-register --resolve    ← Work through one contradiction at a time
/contradiction-register --all        ← All contradictions including resolved ones
```

---

## Process

### Step 1 — Load contradiction edges

Read `knowledge/KNOWLEDGE-GRAPH.json`. Extract all edges where `type` = `"contradicts"`. Each edge has: source entry, target entry, and optionally a `resolution_status` field.

If no contradicts edges exist: report "No contradictions registered in knowledge graph. Use /knowledge-connect to register contradicts relationships when found."

### Step 2 — Load contradicting entries

For each contradicts edge, load both entry files. Extract:
- The specific claim(s) that conflict
- The domain and context of each claim
- Any conditions or qualifiers attached to the claims

### Step 3 — Classify each contradiction

Apply the contradiction resolution framework:

| Type | Signal | Resolution path |
|------|--------|----------------|
| **Direct reversal** | Same scope, opposite claims | One entry is wrong or outdated — determine which based on evidence quality, recency, source authority |
| **Domain-specific** | Both true but in different contexts | Add domain qualifier to each entry; the contradiction is resolved by scoping |
| **Scope difference** | One is a special case of the other | Integrate as parent/child; the narrower claim is a boundary condition of the broader one |
| **Conditional** | Both true under different conditions | Document the conditions explicitly; the contradiction is resolved by specifying when each applies |
| **Productive tension** | Both true simultaneously; the tension is generative | Do NOT resolve — flag as synthesis candidate for `/knowledge-cluster` or `/synthesize` |

### Step 4 — Assign resolution status

For each contradiction:
- **Unresolved** — not yet classified; action required
- **Domain-specific** — scoped to different domains; entries updated with qualifiers
- **Conditional** — conditions documented in entries
- **Integrated** — scope difference resolved; entries updated to reflect parent/child
- **Productive tension** — both true; flagged as synthesis candidate; do NOT force resolution

### Step 5 (--resolve mode only)

Present one Unresolved contradiction at a time. For each:
1. Show both claims
2. Show the likely contradiction type with reasoning
3. Propose the resolution path
4. Ask: "Accept this resolution? (yes/adjust/skip)"

On acceptance: update KNOWLEDGE-GRAPH.json edge to add `resolution_status` field. If domain-specific or conditional: note which entry files need qualifier updates (do not auto-edit entries without operator review).

---

## Output Format

```
CONTRADICTION REGISTER
[N] contradictions total — [X] unresolved, [Y] productive tensions, [Z] resolved

── Contradiction 1 ──
Entry A: [title] ([domain])
  Claim: "[relevant excerpt]"
Entry B: [title] ([domain])
  Claim: "[relevant excerpt]"
Type: [Direct reversal / Domain-specific / Scope difference / Conditional / Productive tension]
Status: [Unresolved / Domain-specific / Conditional / Integrated / Productive tension]
Resolution path: [specific action]

── Contradiction 2 ──
[same structure]

...

SYNTHESIS CANDIDATES (Productive tensions)
[List productive tensions flagged for /knowledge-cluster or /synthesize]
[These should NOT be resolved — the tension is the insight]

NEXT ACTIONS
[For each Unresolved: specific recommended action]
[Run /contradiction-register --resolve to work through these one at a time]
```

---

## Quality Gate

Before outputting:
- [ ] Every contradicts edge in KNOWLEDGE-GRAPH.json has been evaluated
- [ ] Classification uses specific signals (not guessed from entry titles)
- [ ] Productive tensions are NOT flagged for deletion or forced resolution
- [ ] Resolution paths are specific actions, not vague instructions
- [ ] If 0 contradicts edges: clear message explaining how to register them
- [ ] --resolve mode presents one contradiction at a time, not a batch
