# Dynamic Capability Generation
## Gap Detection, Skill Creation, and Safe Integration

---

## When to Generate a New Capability

New capabilities are generated when a recurring, well-defined need has no existing coverage. The bar is intentionally high:

**Generate a new skill when:**
- The request has been made 2+ times with no existing skill covering it
- The need is specific enough to have clear trigger conditions and output format
- The need is distinct enough that it doesn't overlap with an existing skill

**Do NOT generate a new skill when:**
- An existing skill with minor adaptation would cover the need (adapt, don't create)
- The request is a one-off that won't recur (handle inline, don't formalize)
- The gap is in configuration or data, not capability (fix the input, not the skill)
- The existing skill is misconfigured or misunderstood (fix it, don't fork it)

---

## Gap Classification

Before creating anything, classify the gap:

### Variant Gap (80% covered by existing skill)
The existing skill handles most of this, but the trigger or output differs slightly.

**Example:** `/pm-competitive` exists, but user needs a competitive teardown specifically for enterprise sales positioning.

**Fix:** Adapt the invocation of `/pm-competitive` with specific framing, OR add a "Sales Positioning Mode" to the existing skill's workflow. Don't create `/pm-competitive-sales`.

### Extension Gap (20% beyond existing skill)
The skill is right, but one workflow step is missing or the output format needs expansion.

**Example:** `/pm-launch` does a go/no-go checklist, but user wants it to also generate a post-launch monitoring plan.

**Fix:** Extend `/pm-launch` to add a monitoring plan section as an optional workflow step. Bump the version number.

### Novel Gap (genuinely new domain)
No existing skill covers this domain or workflow type.

**Example:** User needs a structured "customer health scoring" workflow that doesn't map to any current PM skill.

**Fix:** Create a new skill. Follow the generation pipeline below.

---

## Generation Pipeline

When a novel gap is confirmed, follow this sequence:

### Step 1 — Define the Capability
Answer these questions before writing anything:
1. What is this skill's one job? (If the answer contains "and", it's two skills.)
2. What triggers this skill? (Specific phrases, artifact types, user situations.)
3. What does it explicitly NOT cover? (Where do adjacent skills take over?)
4. What inputs does it need? (Named files or user-provided content.)
5. What does it produce? (Specific output location and format.)

### Step 2 — Draft the SKILL.md
Follow the canonical SKILL.md format exactly:

```markdown
---
name: skill-name
description: >-
  One paragraph. What it does, when to trigger, what it explicitly doesn't cover.
  Written in third person.
version: "1.0"
changed: "YYYY-MM-DD — Initial version"
---

# Skill Name

## When to Use
Explicit trigger conditions.
When NOT to use this skill (name the alternative).

## Inputs Required
List every file this skill must read before executing.

## Workflow
1. Step one (concrete action, not philosophy)
2. Step two
3. ...

## Output Format
Exact section structure or template. No vagueness.
Output location: [directory/filename pattern]

## Quality Gate
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3
```

### Step 3 — Create the Command File
Write `.claude/commands/<name>.md`. This file can be identical to SKILL.md or can be a stripped-down version focused on the executable workflow. The SKILL.md is the design spec; the command file is what Claude Code loads at invocation.

### Step 4 — Register the Skill
1. Add a row to `skills/README.md` Active Skills table
2. Add the command file to the file listing in `skills/README.md`
3. Add to `CLAUDE.md` routing table if the skill is frequent enough to belong there
4. Log to `prompts/PROMPT-REGISTRY.md` if the skill uses a standalone prompt

### Step 5 — Test Before Marking Active
Invoke the new skill at least once with a real or representative input. Review the output against the quality gate. If it fails the gate, revise the skill spec before marking it Active.

---

## MCP Gap Detection

When a workflow needs an external integration that doesn't have an MCP:

1. **Name the primitive operation.** What exact action is needed? (Read calendar, send email, create Figma file, deploy code.)
2. **Check existing MCPs.** Can this be approximated with what exists? (Playwright can read web pages even without a dedicated MCP.)
3. **Document the gap.** Create a note in `notes/raw/` with:
   - What's needed (specific operation)
   - How often it would be used
   - What the manual workaround is
   - What the ideal MCP would provide
4. **Build a workaround.** If the gap is blocking work, define the best available workaround and document it in `architecture/MCP-ROUTING-SYSTEM.md` under "MCP Capability Gaps."

MCP gaps are surface in `/observe` for tracking. They don't block work — they become improvement candidates.

---

## Prompt Gap Detection

When the quality of a skill's output is consistently below expectations, the gap may be in the prompt, not the skill spec:

**Signals of a prompt gap:**
- Skill output misses key sections despite the spec defining them
- Output format drifts from the template
- Quality scores for the skill are consistently below 3/5

**How to address:**
1. Compare the skill's command file against the actual output
2. Identify where the gap is: missing instruction, ambiguous format spec, unclear trigger
3. Revise the prompt: add specificity, tighten the output schema, add a negative example
4. Bump the version number in the skill's frontmatter
5. Re-test and log the quality score improvement

---

## Capability Generation Quality Gate

Before a new capability is considered production-ready:

```
Definition quality:
  [ ] One job — no "and" in the description
  [ ] Trigger conditions are specific (not "use when relevant")
  [ ] "When NOT to use" names at least one adjacent skill
  [ ] All inputs are explicitly named

Skill file quality:
  [ ] SKILL.md follows the canonical format exactly
  [ ] .claude/commands/<name>.md exists and is functional
  [ ] Registered in skills/README.md
  [ ] Routing entry in CLAUDE.md (if frequent enough)

Integration quality:
  [ ] No overlap with existing skills (checked against SKILL-ROUTING-SYSTEM.md signal map)
  [ ] Tested at least once with real input
  [ ] Quality gate checklist passes on first real invocation
```

---

## Anti-Patterns in Capability Generation

| Anti-Pattern | Problem | Fix |
|---|---|---|
| Creating a skill for every one-off request | Catalog bloat, dead workflows within weeks | Apply the "2+ times" rule before creating |
| Forking an existing skill for minor variation | Duplication, maintenance burden | Adapt with parameters, not forks |
| Creating a skill without testing | Untested skills produce untested output | Gate: test before marking Active |
| Missing the "When NOT to use" section | Skills accumulate scope creep | Write the exclusion boundary explicitly |
| Generating a capability inline without formalizing it | The capability exists once, then is lost | If worth doing twice, formalize it |
| Writing skills in first person | Prompt injection when loaded as system context | Always third person in SKILL.md |
