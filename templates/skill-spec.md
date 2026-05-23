---
name: skill-name-in-kebab-case
description: >-
  One dense paragraph. What this skill does, when to trigger it, what it
  explicitly does NOT cover (name the adjacent skill). Third person only.
  If the description contains "and", split into two skills.
version: "1.0"
changed: "YYYY-MM-DD — Initial version"
---

# /skill-name — Human-Readable Name

One sentence: the single job this skill does.

---

## When to Use

**Invoke when:**
- [Specific situation 1 — observable, not vague]
- [Specific situation 2]
- [Specific situation 3]

**Trigger signals:** "[phrase 1]", "[phrase 2]", "[phrase 3]", "[phrase 4]"

**Do NOT use when:**
- [Situation 1] → use `/[adjacent-skill]` instead
- [Situation 2] → use `/[adjacent-skill]` instead

---

## Inputs Required

Read before executing:

1. `[path/to/required-file.md]` — [what it provides]
2. `[path/to/required-file-2.md]` — [what it provides]
3. [User-provided: description of what the operator must supply at invocation]

If any required input is missing: name it and stop. Do not improvise.

---

## Workflow

### Step 1: [Action verb + specific object]
[Concrete action. Not philosophy. What to read, compute, or produce.]

### Step 2: [Action verb + specific object]
[Concrete action.]

### Step 3: [Action verb + specific object]
[Concrete action. If this step has a gate condition, state it here.]

[3-7 steps. Each step is a concrete action. "Think about X" is not a step.]

---

## Output Format

[Exact structure of the output. Use headers, sections, or table format as appropriate. Leave nothing vague.]

```
## [Section 1 Title]

[What goes here — description of content]

## [Section 2 Title]

[What goes here]

## [Section 3 Title]

[What goes here]
```

**Output location:** `[directory/path/]`
**Filename pattern:** `YYYY-MM-DD-[descriptive-slug].md`

---

## Quality Gate

The output passes if:
- [ ] [Specific, observable criterion — can be verified without subjective judgment]
- [ ] [Specific, observable criterion]
- [ ] [Specific, observable criterion]
- [ ] [3-5 criteria total. Each must be checkable by reading the output.]
