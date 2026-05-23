---
name: skill-new
description: >-
  Bounded skill synthesis with three-gate approval. Given a capability gap, generates
  a complete skill spec, presents it for operator review, and only writes files after
  explicit confirmation. Creates the command file, registers in the skill registry,
  updates the capability index, and adds to skills/README.md. All three gates are
  required — no partial creation. Use after /skill-gaps identifies a synthesis
  candidate. Never synthesizes without operator approval at each gate.
---

# /skill-new — Bounded Skill Synthesis

Generate a new skill spec → human reviews → human approves → files created atomically.

## Trigger

`/skill-new [gap description]`
`/skill-new [gap-id from gap-log]`

Examples:
- `/skill-new customer health scoring workflow`
- `/skill-new gap_20260522_003`
- `/skill-new analyze technical feasibility of a feature proposal`

---

## Synthesis Rules (enforced before any drafting)

**Rule S-1: One job.**
The skill does exactly one thing. If the description contains "and", it's two skills. Split before proceeding.

**Rule S-2: Recurrence threshold.**
A skill should only be created for needs that recur or will recur. One-off requests get handled inline, not formalized.

**Rule S-3: No duplication.**
Run a full duplicate check before drafting. If a variant of an existing skill covers the need, name it — don't fork.

**Rule S-4: All inputs declared.**
Every file the skill needs to read must be named in the spec. No skill may open arbitrary files at runtime.

**Rule S-5: Third person only.**
All skill instructions are written in third person ("The skill reads...", "Claude reads...", not "I will..." or "You should..."). First person in skill files causes prompt injection.

**Rule S-6: Quality gate first.**
The quality gate checklist is defined before the workflow. It specifies the exit conditions — what "done" looks like.

---

## Protocol

### Gate 1: Gap Validation

#### Step 1: Resolve the input

If a gap-id was provided: read `skills/gap-log.jsonl` and find the entry. Extract `intent`, `classification`, `occurrence_count`, `closest_match`.

If a description was provided: run a quick capability match against `skills/capability-index.json` to confirm this is genuinely new.

#### Step 2: Duplicate check

Search `skills/registry.json` for entries where:
- Any capability in `capabilities[]` overlaps with the new intent
- Any `trigger_signals[]` phrase semantically matches the new intent

If strong overlap found (>0.7):
```
Duplicate detected: /[existing-skill] already covers this need.

Matches: [which capabilities/signals overlap]
Recommendation: Use /[skill] with framing: "[suggested framing]"

If this is a genuinely distinct need from the overlap, explain why
and confirm to proceed with synthesis anyway.
```

If no duplicate: proceed.

#### Step 3: Classification confirmation

Confirm the gap classification:
- VARIANT: Stop here — variants don't become new skills. Provide adapted invocation instead.
- EXTENSION: Propose modifying the existing skill instead of creating a new one. If operator insists on a new skill, proceed.
- NOVEL: Proceed to drafting.

#### Step 4: Gate 1 output

```
Gap validation for: "[gap description]"

Classification: NOVEL
Closest existing skill: /[skill] (match score: [X])
Occurrence count: [N]
Duplicate check: CLEAR

This gap qualifies for skill synthesis.

Proceed to draft a skill spec?
```

Wait for explicit approval before drafting.

---

### Gate 2: Spec Review

#### Step 1: Derive skill metadata

From the gap description, derive:

**Command name:** Use kebab-case. Must be unique (check `.claude/commands/` directory listing). Prefix with domain: `pm-`, `exec-`, `know-`, or no prefix for cross-domain skills.

**Name:** Title case, 2-4 words.

**Domain:** One of: operational | knowledge | strategy | execution | cognitive | pm | runtime | invocation | context_engineering | production_ai | daily_os

**Capabilities:** List the abstract capability names this skill provides. Max 3. If more than 3, the skill is doing too much.

**Trigger signals:** 4-6 specific phrases that unambiguously signal this skill is needed.

**Input types:** From the controlled vocabulary in `skill-deps.md` input_type table. Add new input_types only if genuinely needed.

**Output type:** One of: `markdown_document` | `terminal_ephemeral` | `markdown_append` | `json_state` | `skill_file`

**Output location:** Specific directory path (not a file name — the skill determines the filename at invocation).

**Depends on:** Which existing skills typically precede this one. May be empty.

**Produces for:** Which existing skills typically consume this one's output. May be empty.

**MCP partners:** Which MCPs this skill commonly pairs with. May be empty.

#### Step 2: Draft the skill spec

Use `templates/skill-spec.md` as the base. Fill in all sections:

```markdown
---
name: [command-name]
description: >-
  [One dense paragraph: what it does, when to trigger, what it explicitly
  doesn't cover. Written in third person.]
version: "1.0"
changed: "[today's date] — Initial version"
---

# /[command] — [Name]

[One sentence: the job this skill does.]

## When to Use

[Trigger conditions — specific, not "use when relevant"]

Do NOT use when: [Names at least one adjacent skill and when to use it instead]

## Inputs Required

[Every file or user input the skill must have before running. Specific paths or types.]

## Workflow

### Step 1: [Action verb + object]
[Concrete action. Not philosophy.]

### Step 2: [Action verb + object]
[Concrete action.]

[3-7 steps total]

## Output Format

[Exact section structure. No vagueness. Show the template or structure explicitly.]

Output location: [specific directory]
Filename pattern: [YYYY-MM-DD-topic.md or similar]

## Quality Gate
- [ ] [Specific criterion — can be evaluated objectively]
- [ ] [Specific criterion]
- [ ] [3-5 criteria total]
```

#### Step 3: Gate 2 output

```
Skill spec draft: /[command] — [name]

─────────────────────────────────────
[FULL SPEC SHOWN HERE]
─────────────────────────────────────

Registry entry this will add:
  command: /[command]
  domain: [domain]
  capabilities: [list]
  trigger_signals: [list]
  input_types: [list]
  output_location: [path]
  depends_on: [list]
  produces_for: [list]
  mcp_partners: [list]

Files that will be created/updated:
  CREATE: .claude/commands/[name].md
  UPDATE: skills/registry.json
  UPDATE: skills/capability-index.json
  UPDATE: skills/README.md

Approve this spec? (yes / revise: [what to change] / discard)
```

If "revise": apply the requested changes and re-present the spec. Iterate until approved or discarded.

Do NOT write any files before Gate 2 approval.

---

### Gate 3: Registration Confirmation

#### Step 1: Gate 3 output

```
Ready to create:

  .claude/commands/[name].md — new skill file
  skills/registry.json — add [command] entry
  skills/capability-index.json — add [capabilities] → [command]
  skills/README.md — add row: | [Name] | /[command] | v1.0 | — | — | draft |

Note: New skill starts as "draft" status. Change to "active" after first
successful real invocation that passes the quality gate.

Confirm creation?
```

Do NOT proceed without explicit confirmation.

#### Step 2: Atomic file creation (on confirmation)

Write all four changes atomically — if any write fails, report the failure and which files were/weren't updated.

**Write .claude/commands/[name].md:**
Write the approved spec content exactly as drafted.

**Update skills/registry.json:**
Read the file. Add the new skill entry to the `skills[]` array. Increment `skill_count`. Update `last_updated`. Write back.

**Update skills/capability-index.json:**
Read the file. For each capability in the new skill's `capabilities[]`, add `/[command]` to that capability's array (or create a new capability entry if it doesn't exist). Update `last_updated`. Write back.

**Update skills/README.md:**
Read the file. Add a new row to the Active Skills table:
```
| [Name] | `/[command]` | v1.0 | — | — | draft |
```
Write back.

**Update gap-log.jsonl (if gap-id was the input):**
Mark the gap entry's `resolution_status` as `"synthesized"`.

#### Step 3: Verification

After writing, verify:
- `.claude/commands/[name].md` exists and contains expected content
- `skills/registry.json` contains the new entry
- `skills/capability-index.json` contains the new capabilities
- `skills/README.md` contains the new row

#### Step 4: Gate 3 completion output

```
Skill created: /[command] — [name]

Files created/updated:
  ✓ .claude/commands/[name].md
  ✓ skills/registry.json (+1 entry, total: [N])
  ✓ skills/capability-index.json (+[M] capability mappings)
  ✓ skills/README.md (added to Active Skills table)

Status: draft

Next: Invoke /[command] with a representative input to verify the quality gate.
After successful invocation, update registry.json status to "active".
```

---

## Failure Handling

**If Gate 2 approval is "discard":**
- Log to gap-log.jsonl: `resolution_status: "discarded"`, `discard_reason: "[operator's reason]"`
- Output: "Synthesis discarded. Gap remains in log as 'discarded'."
- No files written.

**If file writes fail:**
- Report exactly which file(s) failed
- Do not leave registry in a partially-updated state
- If registry.json was updated but command file failed: roll back registry.json by removing the added entry

**If command name conflicts with existing file:**
- Before writing, check `.claude/commands/` for name collision
- If collision: "Command name /[name] already exists. Choose a different name."
- Return to Gate 2 for name revision.

---

## Quality Gates

- [ ] Duplicate check passed before any drafting
- [ ] Spec has exactly one job (no "and" in core description)
- [ ] Trigger conditions are specific — no "use when relevant"
- [ ] "When NOT to use" names at least one adjacent skill
- [ ] All three gates passed before any file is written
- [ ] New skill status is "draft" until first successful invocation
- [ ] All four file updates happen atomically or not at all
- [ ] Gap log entry updated with resolution status after creation
