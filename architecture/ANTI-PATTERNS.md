# Anti-Pattern Catalog
## Prevention Rules for the Enterprise Intelligence Workspace

Adapted from rootnode-anti-pattern-detection's seven structural patterns + workspace-specific additions.

---

## How to Use This Document

When the workspace isn't behaving as expected — outputs are inconsistent, context seems lost, or workflows feel brittle — check this catalog first. Each pattern has exact detection criteria and a concrete fix.

Never assert an anti-pattern without citing specific evidence. "This seems like X" is not a diagnosis.

---

## Pattern 1 — The Monolith

**What it is:** CLAUDE.md contains reference material mixed with behavioral rules. OR a knowledge file serves multiple unrelated purposes.

**Workspace-specific symptoms:**
- CLAUDE.md exceeds 1,000 tokens
- CLAUDE.md contains tables of workflow steps, data schemas, or directory listings beyond the routing table
- A knowledge file covers both how-to and reference data
- A skill file describes its domain domain's full theory rather than the workflow steps needed

**Detection:**
- Read CLAUDE.md. Can you delete any section and still have a functional workspace?
- If yes: that section is reference material that belongs in a lower layer.

**Fix:**
- Move all reference tables to `architecture/` docs
- Move workflow steps to `workflows/`
- Move knowledge content to `knowledge/<domain>/`
- Keep CLAUDE.md: identity + layer contract + routing + output standards + behavioral guardrails only

**Target state:** CLAUDE.md under 1,000 tokens, every line is behavioral or routing.

---

## Pattern 2 — The Orphan File

**What it is:** A file exists in the workspace but nothing routes to it or references it.

**Workspace-specific symptoms:**
- A knowledge file exists with no entry in `knowledge/KNOWLEDGE-INDEX.md`
- A template exists in `templates/` but no skill or workflow references it
- A prompt exists in `prompts/` with no entry in `prompts/PROMPT-REGISTRY.md`
- A memory file exists but isn't listed in `memory/MEMORY.md`

**Detection:**
```
Every knowledge file → must have a routing entry in KNOWLEDGE-INDEX.md
Every skill → must be listed in skills/README.md AND .claude/commands/
Every prompt → must be listed in PROMPT-REGISTRY.md
Every memory file → must be listed in memory/MEMORY.md
```

**Fix:**
- For each orphaned file: either add the routing entry OR archive the file
- If the file has no clear home: it probably belongs archived (it exists but no workflow needs it)
- Never let files accumulate without routing

---

## Pattern 3 — The Echo Chamber

**What it is:** The same content exists in multiple layers simultaneously.

**Workspace-specific symptoms:**
- A behavioral rule exists in both CLAUDE.md and a memory feedback file
- A project status exists in both a memory file and a knowledge file
- An action item exists in both `execution/action-items.md` and a meeting processed file
- A decision rationale exists in both a memory file and `decisions-log.md`

**Detection:** If you can find the same fact in two different files, one of them is the echo.

**Fix:**
- Identify the correct layer for the fact (per `architecture/MEMORY-MAP.md` decision table)
- Remove it from all other locations
- Add a pointer if needed: "See decisions-log.md for decisions" (pointer, not duplication)

**One home rule:** Every piece of information lives in exactly one layer.

---

## Pattern 4 — The Phantom Session

**What it is:** Memory or knowledge files contain session-specific context that should be ephemeral.

**Workspace-specific symptoms:**
- A memory file contains "Today I worked on..." or "In our last session..."
- A knowledge file captures what Claude said in a specific conversation
- A memory file grows after every session with notes about what happened
- Action items reference specific Claude responses rather than concrete tasks

**Detection:** If a memory file reads like a journal or a chat log, it has captured ephemeral context.

**Fix:**
- Strip the conversational wrapper; keep only the durable fact
- "In our session today, we decided to use Python for the pipeline" → "Decision: Python for pipeline. See decisions-log.md entry 2026-05-20."
- Ephemeral context belongs in conversation, not in memory

---

## Pattern 5 — Kitchen Sink Skill

**What it is:** A skill tries to do multiple distinct things, or accumulates scope over time.

**Workspace-specific symptoms:**
- A skill has multiple "also" clauses: "/debrief also does X and also updates Y"
- A skill's trigger description contains "or" multiple times for unrelated cases
- A skill writes to more than 2 distinct output locations
- A skill reads more than 5 files (suggesting it's doing the work of multiple skills)

**Detection:** Count the distinct jobs. More than one → kitchen sink.

**Fix:** Split the skill. Each resulting skill should have one trigger condition and one primary output.

If the two jobs are truly coupled and always happen together, make one of them a step in the workflow doc — not a separate skill invocation.

---

## Pattern 6 — Misaligned Hierarchy

**What it is:** Content is placed in the wrong layer, degrading retrieval and response quality.

**Most common misalignments in this workspace:**

| Content placed wrongly | Correct location |
|----------------------|-----------------|
| Behavioral rules in a memory file | CLAUDE.md |
| Knowledge entries in memory | `knowledge/<domain>/` |
| Current priorities in a knowledge file | `memory/` |
| Workflow steps in CLAUDE.md | `skills/<name>/SKILL.md` |
| Permanent knowledge in `notes/` | `knowledge/` (after /promote) |
| Decision rationale in a meeting processed file only | `decision-frameworks/decisions-log.md` |
| Reference data in CLAUDE.md | `architecture/` or `knowledge/` |

**Detection:** Apply the decision table in `architecture/MEMORY-MAP.md` to each piece of content.

**Fix:** Move the content to the correct layer. Update routing/index entries. Delete the misplaced copy.

---

## Pattern 7 — Blurred Layers

**What it is:** The boundary between layers becomes unclear because the directory contract isn't enforced.

**Workspace-specific symptoms:**
- Notes that were never promoted living indefinitely in `notes/raw/`
- Meeting processed files containing knowledge entries inline rather than routing to `/promote`
- `synthesis/` files that are really just long meeting debriefs
- `knowledge/` entries that are really just raw notes with frontmatter added

**Detection:** Read 3-4 files from each directory. Do they match their directory's contract?

**Fix:**
- Promote or archive all `notes/raw/` files older than 7 days
- Extract knowledge candidates from meeting processed files; route via `/promote`
- Delete synthesis files that are single-meeting summaries (those belong in `meeting-intelligence/`)
- Rewrite knowledge entries that lack the required sections (Definition, Why It Matters, Key Principles)

---

## Workspace-Specific Anti-Patterns (Beyond the Seven)

### Prompt Drift

**What it is:** Prompts in `prompts/` diverge from what skills actually invoke, or skill command files diverge from `skills/` canonical specs.

**Symptom:** The skill spec says one output format but the prompt produces another.

**Fix:** When updating a prompt, update the skill spec. When updating a skill spec, update the prompt. They must stay in sync. Version numbers make drift visible.

---

### Telemetry Gap

**What it is:** API calls are being made but not logged to `telemetry/api-log.jsonl`.

**Symptom:** The observability dashboard shows fewer calls than you know were made.

**Fix:** Every API call through `production-ai/claude_client.py` logs automatically. If calls are being made outside this client, they must be logged manually. There are no exceptions — un-logged calls are invisible to the improvement loop.

---

### Context Budget Blindness

**What it is:** Memory files, CLAUDE.md, and skills are growing without anyone checking total token overhead.

**Symptom:** Sessions feel slower; Claude seems to miss context; CLAUDE.md is over 1,500 tokens.

**Fix:** Run `/observe` and include a token audit section. Check:
- CLAUDE.md size: `wc -c CLAUDE.md` → divide by 4 for token estimate
- Total memory file size: same approach
- If CLAUDE.md > 1,000 tokens: prune
- If total memory > 3,000 tokens: archive stale files

---

### Dead Workflow

**What it is:** A workflow or skill exists but hasn't been invoked in >30 days.

**Symptom:** Dashboard shows W0x with 0 runs this month.

**Fix:** Deliberate choice: either remove it (if no longer relevant) or invoke it intentionally and note why it was skipped. Don't maintain dead infrastructure.

---

## Anti-Pattern Detection Checklist

Run this monthly (or add to `/observe` output):

```
CLAUDE.md health:
  [ ] Under 1,000 tokens?
  [ ] Zero reference material?
  [ ] All sections behavioral or routing?

Memory health:
  [ ] MEMORY.md index under 100 lines?
  [ ] All files listed in MEMORY.md exist?
  [ ] No file over 500 tokens?
  [ ] No file updated >30 days ago (projects) or >90 days (others)?

Knowledge health:
  [ ] Every knowledge file in KNOWLEDGE-INDEX.md?
  [ ] No knowledge file with reviewed: >90 days?
  [ ] No orphaned files in notes/raw/ >7 days old?

Skill health:
  [ ] Every skill in skills/README.md?
  [ ] Every skill has a .claude/commands/ file?
  [ ] Every skill invoked at least once in past 30 days?

Prompt health:
  [ ] Every prompt in PROMPT-REGISTRY.md?
  [ ] No prompt version that hasn't been quality-rated?

Layer separation:
  [ ] No behavioral rules outside CLAUDE.md?
  [ ] No knowledge content in memory/?
  [ ] No ephemeral session context in memory/?
```
