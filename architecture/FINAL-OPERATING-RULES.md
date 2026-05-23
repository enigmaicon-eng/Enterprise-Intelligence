# Final Operating Rules
## Enterprise Intelligence Workspace — Permanent Governance

These rules govern the workspace going forward. They are not suggestions. Violating them creates the complexity accumulation that required the P11 review.

---

## Rule 1: CLAUDE.md is a behavior file, not a catalog

**CLAUDE.md must stay under 1,500 tokens.**

The routing table lists only skills whose trigger signals are non-obvious to someone who knows the workspace. Skills that self-document by name (e.g., `/pm-wireframe`, `/pm-market-sizing`) are not listed individually — they're covered by the single PM routing line.

**Test before adding to CLAUDE.md routing table:** Would a user who knows this workspace and knows they need a PM artifact fail to type `/pm-[what they need]`? If no: don't add it.

**Never add to CLAUDE.md System References.** New architecture documents belong in `architecture/WORKSPACE-GUIDE.md`.

---

## Rule 2: Skills are the canonical specification

When a skill file and a prompt file or playbook describe the same workflow, the skill file wins. Prompt files and playbooks are supplementary reference only.

**Implication:** When updating a workflow, update the skill file. If the prompt file or playbook diverges from the skill, the playbook is wrong.

**No new prompt files that duplicate skill content.** Prompts belong inside skill files or as standalone files only when they contain content not in any skill.

---

## Rule 3: Three-tier ritual model

**Tier 1 — Required (never skip):**
- `/briefing` — daily session start
- `/shutdown` — daily session end
- `/weekly` + `/exec-review weekly` — Monday

**Tier 2 — High-value (use when relevant):**
- `/plan` — when direction is unclear
- `/focus` — before deep work
- `/prep` — before high-stakes meetings
- Monthly cognitive review
- Monthly strategy review

**Tier 3 — Situational (triggered by events, not cadence):**
- Everything else

**Adding a new ritual requires removing or downgrading an existing one.** The ritual stack has a carrying cost. It does not grow without bound.

---

## Rule 4: Architecture documents are reference, not operations

Architecture documents are written once, updated occasionally, and consulted rarely. They are not part of the daily context path.

**When completing a new system build:**
1. Write the architecture document in `architecture/`
2. Add its description to `architecture/WORKSPACE-GUIDE.md`
3. Do NOT add it to CLAUDE.md System References

**The daily context path is:** CLAUDE.md → memory/MEMORY.md → skill (when invoked) → knowledge (on demand).

---

## Rule 5: Top 3 rule applies to commitments AND systems

Just as daily commitments are capped at 3, active workspace systems should be manageable. The test: can you describe all active components of the workspace in 3 minutes?

If the answer is no, the workspace has grown past its operator's cognitive bandwidth. Simplify before adding.

---

## Rule 6: Knowledge entries get staggered reviewed dates

When creating knowledge entries in a batch (e.g., during a build phase): set `reviewed:` dates 14-30 days before the creation date to distribute future review load.

**Never set `reviewed:` to the creation date for all entries in a batch.** This creates a simultaneous review wave in 90 days.

---

## Rule 7: No new PM skills in the routing table

The 44 PM skills are discoverable via the `/pm-*` prefix and autonomous routing. Future PM skills that are added to the catalog (in `skills/README.md`) are not added to the CLAUDE.md routing table.

**Exception:** A PM skill that cannot be discovered by intent-typing (one whose trigger signal is genuinely non-obvious) may be added to the routing table with a specific, non-obvious trigger description.

---

## Rule 8: Playbooks have a "versus skill" test

Before writing a new playbook, ask: does this contain content that is not in any skill file? If the playbook is a prose expansion of what a skill already does, don't write it — update the skill.

**A playbook justifies its existence when:** it contains multi-skill orchestration, decision trees that don't belong in a single skill, or reference material (tables, taxonomies) that informs multiple skills.

---

## Rule 9: One sentence before every context switch

Before switching from one problem to another: write one sentence. Current state + next action. This is not optional when switching mid-deep-work-session.

---

## Rule 10: Workspace health check quarterly

Run `/observe` quarterly. Review `architecture/FINAL-REVIEW.md` findings for any that haven't been addressed. Add new findings as P0/P1/P2.

The workspace should feel simpler over time, not more complex. If quarterly review reveals net complexity increase, something is wrong with the operating rules.

---

## Simplification Heuristics

**When to remove a skill:**
- It hasn't been invoked in 6 months and has an obvious alternative
- Its function has been absorbed into a more general skill
- Its trigger signal overlaps with another skill and the distinction is unclear to the user

**When to remove a knowledge entry:**
- Its content is fully covered by a newer, broader entry
- Its `confidence:` has been revised to `low` and there's no path to improvement
- The domain it covers is no longer relevant to active work

**When to merge architecture documents:**
- Two documents describe the same system from slightly different angles
- One document is referenced in the other but rarely consulted independently
- A document has no entries in `architecture/WORKSPACE-GUIDE.md`

**When to prune the ritual stack:**
- A ritual runs but doesn't produce a concrete output
- A ritual's output is never used in downstream workflows
- A ritual was added "to be comprehensive" rather than because the workspace actually needed it

---

## Maintenance Schedule

| Frequency | Activity |
|---|---|
| Daily | `/shutdown` — keep open loops from accumulating |
| Weekly | `/weekly` + exec review — keep initiatives and knowledge current |
| Monthly | Cognitive review + strategy review + retro |
| Quarterly | `/observe` + review `FINAL-REVIEW.md` + simplification pass |
| On new build | Add to `WORKSPACE-GUIDE.md`; do NOT add to CLAUDE.md System References |
| On new PM skill | Add to `skills/README.md`; do NOT add to CLAUDE.md routing table |
