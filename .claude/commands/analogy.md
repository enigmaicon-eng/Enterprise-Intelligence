---
name: analogy
description: >-
  Structural analogical reasoning — given a problem or situation, finds
  structurally similar cases across all knowledge domains and maps the
  transferable insight explicitly. Does NOT do keyword retrieval (use /recall
  for that). Does NOT synthesize entries together (use /synthesize or
  /knowledge-cluster). Use when stuck on a problem and want to learn from a
  structurally parallel case in a different domain.
version: "1.0"
changed: "2026-05-23 — initial"
output: inline (no file written)
---

# /analogy — Analogical Reasoning

## When to Use

- Stuck on a problem and want insight from a structurally similar case in another domain
- Designing a system and wondering if a known pattern from elsewhere applies
- Sense that a problem has been "solved" somewhere — just not in this field
- Want to stress-test a proposed solution by finding where analogous solutions failed

**Do NOT use for:**
- Retrieving entries on a known topic → `/recall`
- Connecting two entries you already know about → `/knowledge-connect`
- Synthesizing a cluster of entries → `/knowledge-cluster`
- Identifying what patterns exist across entries → `/pattern-mine`

---

## Input

```
/analogy <problem or situation description>
```

Problem description should be specific enough to extract structure. Vague inputs produce vague analogies.

Good: "My AI system gives overconfident answers despite uncertainty"
Weak: "AI problems"

---

## Process

### Step 1 — Parse the problem

Read the problem description. Extract:
- **Domain**: what field/context is this in?
- **Actor**: who or what is the agent experiencing the problem?
- **Constraint or failure mode**: what specifically isn't working or is needed?
- **Desired property**: what behavior or state would solve it?

### Step 2 — Extract abstract structure

Strip the domain-specific surface content. Restate the problem as a domain-neutral structure:

Format: `[Actor type] lacks [property] → causes [failure mode] → desired: [outcome]`

Example:
- Surface: "AI gives overconfident answers despite uncertainty"
- Structure: "output-generating system lacks calibrated uncertainty representation → causes miscalibrated user trust → desired: outputs signal their own reliability"

This abstract structure is what you search for, not the surface keywords.

### Step 3 — Search the knowledge base

Read `knowledge/KNOWLEDGE-INDEX.md`. Scan all domains. Look for entries whose **core mechanisms** match the abstract structure — not entries with matching keywords.

Load up to 7 candidate entries (the most structurally promising ones across different domains). Do not load all entries.

For each candidate, ask: does the mechanism this entry describes map onto the abstract structure?

### Step 4 — Map analogies explicitly

For each analogy found (target: 2–3 strong ones):

**Source:** [entry title, domain]
**Structural match:**
- [source element] ↔ [problem element]
- [source element] ↔ [problem element]
- [source mechanism] ↔ [problem mechanism]

**Transferable insight:** What does the source domain know that applies to the problem? State it as a concrete recommendation or principle.

**Where the analogy breaks down:** Name 1–2 specific points where the mapping fails and what must be adapted rather than transferred directly.

### Step 5 — Flag synthesis opportunities

If 2+ analogies point to the same underlying principle, note it. This may be a cross-domain pattern worth capturing with `/pattern`.

---

## Output Format

```
PROBLEM
[Problem as stated]

ABSTRACT STRUCTURE
[Domain-neutral restatement]

ANALOGIES

── Analogy 1: [Entry title] ([domain]) ──
Structural match:
  [source element] ↔ [problem element]
  [source element] ↔ [problem element]
Transferable insight: [1-2 sentences]
Analogy limits: [where mapping fails]

── Analogy 2: [Entry title] ([domain]) ──
[same structure]

── Analogy 3: [Entry title] ([domain]) ── [if applicable]
[same structure]

SYNTHESIS SIGNAL
[If 2+ analogies share a principle: name it. Flag for /pattern capture.]
[If only 1 analogy found: note the knowledge base may be too thin in adjacent domains.]
[If 0 analogies: say so explicitly — do not force weak matches.]
```

---

## Quality Gate

Before outputting:
- [ ] Abstract structure is domain-neutral (no surface keywords from the problem)
- [ ] Each analogy maps at least 2 structural elements explicitly
- [ ] Transferable insight is a concrete principle, not a restatement of the source entry
- [ ] Analogy limits named for each analogy
- [ ] No weak matches forced — better to report 1 strong analogy than 3 weak ones
- [ ] If 0 strong matches: say so and suggest domains to learn from
