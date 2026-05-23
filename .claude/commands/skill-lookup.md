---
name: skill-lookup
description: >-
  Semantic skill search. Given a natural language intent or capability description,
  finds the best matching skill(s) from the registry without routing or executing anything.
  Pure lookup — no invocation, no confirmation required. Use when the operator wants to
  know which skill to use without triggering routing logic. For smart routing that also
  checks context and dependencies, use /skill-invoke instead.
---

# /skill-lookup — Semantic Skill Search

Find the right skill by capability, not by exact command name. Returns matches ranked by signal strength.

## Trigger

`/skill-lookup [intent or capability description]`

Examples:
- `/skill-lookup I want to write a product spec`
- `/skill-lookup find a skill for market analysis`
- `/skill-lookup what covers retrospectives`
- `/skill-lookup is there a skill for AI feature specifications`

---

## Protocol

### Step 1: Parse the query

Extract from the query:
- **Domain signals** — which domain vocabulary cluster does this hit? (PM, knowledge, strategy, execution, cognitive, runtime, operational)
- **Capability signals** — which abstract capabilities map to this intent?
- **Action verbs** — write, analyze, review, plan, synthesize, capture, design, spec, map, audit...
- **Output hints** — document, decision, metric, story, strategy, plan...
- **Cognitive mode** — divergent (brainstorm, explore) / convergent (decide, spec) / analytical (investigate, review) / executive (status, brief)

### Step 2: Match against capability-index.json

Read `skills/capability-index.json`.

For each capability in the index:
- Does the query intent map to this capability? Score 0-1 (1 = exact match, 0 = no match)
- Use semantic similarity, not exact keyword match

Collect all capabilities with score > 0.3. Retrieve the skill commands for each.

### Step 3: Match against registry trigger_signals

Read `skills/registry.json`.

For each skill that appeared in Step 2, check the `trigger_signals[]` field.
Score additional signal matches:
- Exact phrase match: +0.3
- Partial phrase match: +0.1
- Domain alignment (query domain matches skill domain): +0.1
- Cognitive mode alignment: +0.05

Rank all candidate skills by total score.

### Step 4: Output results

Format:

```
Skill lookup: "[query]"

Best match:
  /[command] — [name]
  Capabilities: [list]
  Why: [which signals matched]
  Input needed: [input_types]
  Output: [output_type] → [output_location]

[If 2-3 additional strong matches:]
Also relevant:
  /[command] — [name] (why this is close but not primary)
  /[command] — [name]

[If query could go multiple ways:]
Clarifying question: "[one question that distinguishes the top matches]"
```

### Step 5: Ambiguity handling

If top two scores are within 0.1 of each other:
- Don't pick one — name both
- Ask one question to distinguish: "Is this [interpretation A] or [interpretation B]?"

If query covers multiple capabilities (composite request):
- Name all matched skills
- Propose the sequence: "This looks like [A] → [B] → [C] in order."
- Don't invoke the pipeline — just name it

### Step 6: No match handling

If no skill scores above 0.3:
- State clearly: "No strong match found for this intent."
- Name the closest partial matches (score 0.1-0.3) with explanation of the gap
- Suggest: "Run /skill-gaps to log this as a capability gap."

---

## Quality Gates

- [ ] Results ranked by signal strength, not alphabetical
- [ ] "Why" explanation shows specific signals that matched
- [ ] Ambiguous results ask one question — not two
- [ ] No-match cases name closest partials and suggest /skill-gaps
- [ ] No invocation happens — lookup only
