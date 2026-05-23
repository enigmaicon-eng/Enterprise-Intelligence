# Reasoning Structure
## Reasoning Blocks, Output Architecture, and Chain-of-Thought Discipline

Reasoning structure governs how the model organizes its internal inference before producing output. Well-structured reasoning produces consistent, defensible outputs. Poor structure produces drift, unwarranted confidence, and format inconsistency.

This document defines five reasoning block templates, six output architecture patterns, and the chain-of-thought discipline that governs when each applies.

---

## Reasoning Blocks

Reasoning blocks are internal inference templates. Match the block type to the task before reasoning.

### Block 1 — Diagnosis
Use when: identifying the cause of a problem, failure, or gap.

```
1. OBSERVE: What is the symptom? (Specific, observable, not inferred)
2. GENERATE: What are the 2-4 most plausible causes?
3. TEST: What evidence supports or rules out each cause?
4. CONCLUDE: Which cause is best supported? State confidence level.
5. ACTION: What's the minimum intervention to address the root cause?
```

**Discipline:** Don't jump from symptom to cause. Step 2 requires generating multiple candidates before selecting one. If only one cause comes to mind, it's premature closure.

### Block 2 — Decision
Use when: recommending between options, choosing a path, advising on trade-offs.

```
1. FRAME: What is actually being decided? (Often narrower than stated)
2. OPTIONS: What are the realistic alternatives? (2-4; not strawmen)
3. CRITERIA: What makes one option better than another for this context?
4. APPLY: How does each option perform against the criteria?
5. RECOMMEND: Which option wins? State why. Name the key trade-off accepted.
6. CAVEAT: What single uncertainty most threatens the recommendation?
```

**Discipline:** Step 6 gets one caveat — the most important one. Not a list of hedges. If there's genuine uncertainty, name it specifically ("this assumes X, which hasn't been verified").

### Block 3 — Analysis
Use when: making sense of data, patterns, behavior, or market signals.

```
1. OBSERVE: What's actually there? (Data, facts, behaviors — no interpretation yet)
2. PATTERN: What recurring structure or trend is present?
3. IMPLICATION: If this pattern holds, what follows?
4. ANOMALY: What doesn't fit the pattern? (This often holds the insight)
5. SO WHAT: What should change because of this analysis?
```

**Discipline:** Step 4 is mandatory. Analysis that ignores anomalies confirms prior beliefs rather than discovering new ones. Anomalies are often where the real signal lives.

### Block 4 — Planning
Use when: building a sequence of actions to achieve a goal.

```
1. GOAL: What does success look like at the end? (Observable, not vague)
2. CONSTRAINTS: What can't change? (Time, resources, non-negotiables)
3. DEPENDENCIES: What must happen before what?
4. SEQUENCE: What's the minimum viable sequence of steps?
5. RISKS: What's most likely to break this plan? How do we detect it early?
6. CHECKPOINT: When do we evaluate if the plan is still valid?
```

**Discipline:** Step 4 is minimum viable — don't plan every possible contingency. Plans that cover every scenario are too brittle to execute. Build in a checkpoint (Step 6) instead.

### Block 5 — Synthesis
Use when: generating insight from multiple inputs (meetings, documents, research).

```
1. INPUTS: What are the source materials? What type is each?
2. THEMES: What appears across multiple sources? (Cross-source, not single-source)
3. TENSION: Where do sources disagree or contradict?
4. INSIGHT: What's non-obvious that the synthesis reveals?
5. CONNECTION: How does this connect to existing knowledge? ([[link]])
6. GAP: What question does this synthesis raise that can't yet be answered?
```

**Discipline:** Step 4 must be non-obvious. If the insight would be immediately apparent to anyone who read the sources, it's a summary, not a synthesis. A synthesis surface something the raw sources don't individually contain.

---

## Output Architecture

Output architecture defines the surface form — what the output looks like. Match the pattern to the task type.

### Pattern 1 — Direct Answer
Use for: simple questions, factual lookups, status checks.

```
[Answer in 1-3 sentences]
[One supporting detail if needed]
```

Never add headers, preamble, or summary. The answer is the output.

### Pattern 2 — Structured Report
Use for: weekly reviews, debriefs, audits, status updates.

```
## [Report Title]
[2-3 sentence framing: what period, what scope]

### [Section 1 — mandatory content]
[prose or short bullets as the section requires]

### [Section 2 — mandatory content]
...

### Actions / Next Steps
[Bulleted list with owner and date for each item]
```

Sections are defined by the skill spec. Don't invent new sections. Don't omit mandatory sections.

### Pattern 3 — Recommendation + Rationale
Use for: decisions, trade-off analysis, option evaluation.

```
**Recommendation:** [One sentence. The choice, stated directly.]

**Why:** [2-4 sentences. Criteria applied + how winner performed against them.]

**Trade-off accepted:** [One sentence. What you're giving up by choosing this.]

**Key assumption:** [One sentence. The thing most likely to invalidate this if wrong.]
```

This pattern is the Decision Block (Block 2) expressed as output. Four elements, no more.

### Pattern 4 — Action Manifest
Use for: execution plans, task decompositions, project kickoffs.

```
## [Initiative Name] — Action Manifest

**Goal:** [One sentence. Observable success condition.]

### Milestone 1: [Name] — [Date]
- [ ] Task: [verb phrase] | Owner: [name] | Done when: [specific condition]
- [ ] Task: ...

### Milestone 2: [Name] — [Date]
...

### Risks
| Risk | Trigger signal | Owner |
|------|--------------|-------|
| [risk] | [what to watch] | [who watches] |
```

Every task has an owner and a done condition. Vague tasks block execution.

### Pattern 5 — Diagnostic Report
Use for: context audits, anti-pattern detection, health checks.

```
## Diagnostic Report — [Date]

### P0 — Immediate Fix Required
[List each P0 issue: what it is, where it is, exact fix]

### P1 — Fix Before Next Session
[List each P1 issue: what it is, where it is, recommended fix]

### P2 — Fix This Month
[List each P2 issue]

### Healthy Checks (passing)
[Brief list of what's working]

### Score
[Dimension]: [score]
Overall health: [pass/warn/fail]
```

P0s are always shown first. An empty P0 section is a good sign, not a flaw.

### Pattern 6 — Knowledge Entry
Use for: /learn, /pattern, /promote output.

```yaml
---
title: [Concept Name]
domain: [technical | strategy | pm | operations | systems | patterns | decisions]
created: [YYYY-MM-DD]
reviewed: [YYYY-MM-DD]
tags: [comma-separated]
connections: [list of [[linked-concepts]]]
confidence: [high | medium | low]
source: [original synthesis | external: URL | meeting: filename]
---

## Definition
[What this is, in 2-4 sentences. Precise enough to distinguish from adjacent concepts.]

## Why It Matters
[Why this is worth knowing. The consequence of not knowing it.]

## Key Principles
[3-7 bullet points. Each is a standalone rule or insight.]

## In Practice
[How this applies in this workspace. Specific, not generic.]

## Connections
[[[linked-concept]] — how it relates]

## Open Questions
[What isn't yet resolved about this topic]
```

---

## Chain-of-Thought Discipline

Rules governing when and how to use explicit reasoning before generating output.

**Use reasoning blocks when:**
- The task has genuine ambiguity or multiple plausible approaches
- The stakes of a wrong answer are high (decisions, plans, analysis)
- The output requires a specific format and you need to verify fit

**Skip reasoning blocks when:**
- The answer is directly in context and requires no inference
- The task is retrieval-only (find and return a file's content)
- The output is clearly defined by a skill spec with no judgment required

**Reasoning is internal.** Don't narrate the block steps to the user. Apply the template, produce the output. Only surface the reasoning if the user asks "why."

**Confidence signaling:**
- State conclusions directly when evidence clearly supports them.
- Use "likely" or "probably" when evidence is partial.
- Use "uncertain" + name the specific uncertainty when evidence is absent.
- Never use "might," "could," "possibly" as filler hedges. Reserve them for genuine uncertainty.

**Premature closure prevention:** Before concluding a reasoning block, check: did you consider at least two alternatives? If no, you closed too early. Generate a second option and compare.
