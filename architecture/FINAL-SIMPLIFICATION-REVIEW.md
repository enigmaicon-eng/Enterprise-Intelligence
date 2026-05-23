# Final Autonomy Simplification Review
## Enterprise Intelligence Workspace — Complete Runtime Audit

**Date:** 2026-05-23  
**Scope:** P13–P19 autonomous runtime layer, 110 skills, 39 architecture documents  
**Stance:** World-class AI strategist + elite operator + cognitive systems architect + runtime engineer + principal PM  

---

## The Verdict Upfront

The workspace has accumulated a sophisticated-looking but operationally inert infrastructure. The core value — skilled PM and operational work — is sound. The runtime layer surrounding it has drifted into enterprise orchestration theater: dual persistence systems that have never been written to, a 7-component invocation system for routing to skills that are named after what they do, and architecture documentation that outnumbers the workflows it governs by 39:0.

The system must be simplified. Not because it is broken, but because complexity accumulates carrying cost whether or not it is used — in cognitive load, in maintenance surface, in the friction between "I need to do X" and actually doing X.

---

## What Was Examined

| Layer | Artifact Count | Usage Evidence |
|-------|---------------|----------------|
| Runtime (P13+P15) | 8-table SQLite schema, 6 Python scripts, 8 JSON files, 4+4 skills | `active-workflows.json: []`, `events: []` — zero executions |
| Invocation system (P14) | 2 registry JSON files, 5 meta-skills, gap-log.jsonl | Used only to look up skills that already have explicit names |
| Memory system (P16) | 7 typed directories, 6 skills, retrieval index | MEMORY.md + user_profile.md is the real daily load |
| Capability layer (P19) | 4 registry files, 3 scripts, 4 skills | `INVOCATION-LOG.jsonl` empty |
| Architecture docs | 39 documents | Daily context path uses CLAUDE.md + skill files |
| Skills total | 110 commands | 44 are self-routing PM skills; ~20 are meta-infrastructure skills |

---

## Finding 1 — Dual Persistence Is the Largest Structural Error

P13 stores workflow state in human-readable JSON files (`runtime/state/`, `runtime/snapshots/`, etc.).  
P15 then mirrors every piece of that state into a SQLite database (`execution.db`) with 8 tables.

The stated justification: "P13 stores workflow state in JSON files — human-readable but not crash-safe, not queryable, and not event-sourced."

**The problems with this argument:**

First, JSON is crash-safe with atomic writes (write to temp, rename atomically). This is 3 lines of Python, not a new persistence system.

Second, "queryable" is solving for an analytics use case that a single-operator system running at most one workflow at a time does not have. The query surface area of 8 tables adds negligible value over `jq` on two JSON files.

Third, the dual-write requirement (B-11: write SQLite first, then JSON) creates the exact failure mode it claims to prevent. A crash between SQLite write and JSON write produces inconsistent state between the two layers — requiring the very "rebuild from events" recovery flow that was supposed to be the safeguard.

**The real cost:** 6 Python scripts totaling ~1,200 lines, an 8-table schema, 4 diagnostic skills (/exec-journal, /exec-timeline, /exec-snapshot, /exec-diagnose), dual-format state for every piece of runtime data, and B-11 through B-15 governance rules — all for a system that has processed zero workflows.

**The correct architecture:** One file-based persistence layer. JSON files. Atomic writes via temp-file rename. No SQLite. The 4 exec-* diagnostic skills collapse into /runtime-status with a `--history` flag.

---

## Finding 2 — The Executive Orchestrator Is Imaginary Infrastructure

The BOUNDED-RUNTIME.md describes an "Executive Orchestrator" as the session entry point — a component that reads runtime state, routes requests, presents resume options, and manages workflow gates.

There is no Executive Orchestrator. It is Claude reading a JSON file and responding. The elaborate component diagram (8 boxes with arrows) describes what Claude does when it reads the skill file for `/runtime-start`. It is documentation dressed as distributed systems architecture.

This is autonomy theater: making simple, desirable behavior look like sophisticated infrastructure. The behavior is good. The framing makes it appear more complex and more "agentic" than it is, which:
- Creates cognitive overhead for the operator trying to understand the system
- Makes the architecture documents harder to maintain than the actual behavior
- Suggests a more automated system than actually exists (which is dangerous for trust calibration)

**Correct framing:** `/runtime-start` reads `active-workflows.json`, surfaces paused workflows if present, and proposes a plan. That sentence describes the entire "Executive Orchestrator."

---

## Finding 3 — Domain Executors Are Naming Without Substance

Five "Domain Executors" (Knowledge, Meeting, Strategy, PM, Cognitive) are described as "thin adapters — each knows how to invoke a skill cluster."

They are not thin adapters. They are not components. They are categories of skills that Claude already knows from the skill files and the CLAUDE.md routing table. No code implements them. No file instantiates them. They appear as boxes in an architecture diagram and nowhere else.

Removing this abstraction does not change the system's behavior by one character. It removes 30 lines of architecture documentation that describe nothing real and adds conceptual weight to simple intent-routing.

**Verdict:** Delete this layer from the architecture narrative.

---

## Finding 4 — The Dynamic Invocation System Adds Friction to Direct Execution

P14 builds a 7-component invocation system (registry, capability index, router, context-aware selector, dependency resolver, gap detector, skill synthesizer) to answer the question: "which skill should I run?"

The answer to that question in 90% of cases is: the one the operator typed (explicit command) or the one obvious from the routing table in CLAUDE.md.

The `/skill-invoke [intent]` path adds 7 steps (signal extraction → capability matching → candidate ranking → context fit → dependency check → surface invocation plan → gate) to something that took 1 step: typing `/pm-discovery`.

The dependency resolver (`/skill-deps`) checks whether input files exist before running a skill. This is done better by trying to run the skill and seeing what's missing — which produces a more useful error message than a pre-flight check that may not match what the skill actually needs.

The gap log (`skills/gap-log.jsonl`) + multi-gate synthesis flow (`/skill-new`) is right-sized for a team of PMs building a shared tool library. For a solo operator creating skills ad hoc when needed, it adds bureaucracy to a 15-minute task.

**What to keep:** `/skill-lookup` (useful for discovery of the 110-skill catalog), `/skill-new` (scaffolding template is genuinely useful). The registry.json is useful as a machine-readable index.

**What to eliminate as active workflows:** `/skill-invoke`, `/skill-deps`, `/skill-gaps`. The routing behavior these implement should live in ambient CLAUDE.md behavior, not in explicit meta-skills that must be manually invoked.

---

## Finding 5 — The Gap Log Creates Bureaucracy for Rare Events

The skill synthesis system requires:
1. Gap detected (confidence < 0.4)
2. Logged to skills/gap-log.jsonl
3. Must occur 2+ times before synthesizing
4. Gate 1: gap validation
5. Gate 2: spec review
6. Gate 3: registration confirmation

For a solo operator who creates perhaps 2-3 new skills per quarter, this is enormous overhead. The real flow: user recognizes a recurring need → describes what they want → Claude drafts the skill → operator approves the file. Three seconds of thought, one confirmation.

The multi-gate synthesis flow optimizes for the wrong risk: it guards against synthesizing skills too hastily, when the real risk is having too many meta-skills governing skill creation.

---

## Finding 6 — Skill Count Has Reached the Cognitive Bandwidth Boundary

110 skills. The FINAL-OPERATING-RULES.md asks: "Can you describe all active components of the workspace in 3 minutes?" At 110 skills, the answer is no.

The breakdown:
- 44 PM skills (self-routing via /pm-*, fine)
- 4 daily ops skills (/briefing, /plan, /focus, /shutdown, /prep, /weekly — actually 6)
- 4 runtime skills (/runtime-start, /runtime-resume, /runtime-status, /runtime-recover)
- 4 exec diagnostic skills (/exec-journal, /exec-timeline, /exec-snapshot, /exec-diagnose)
- 5 invocation meta-skills (/skill-lookup, /skill-invoke, /skill-deps, /skill-gaps, /skill-new)
- 6 memory skills (/mem-capture, /mem-recall, /mem-adr, /mem-failure, /mem-reconstruct, /mem-hygiene)
- 4 knowledge skills (/knowledge-connect, /knowledge-cluster, /knowledge-review, /knowledge-graph)
- 2 knowledge QA skills (/knowledge-validate, /knowledge-qa)
- 6 strategy/cognitive skills (/bet, /horizon, /think, /misconception, /insight, /recall-test, /recall, /pattern)
- 4 MCP skills (/mcp-register, /mcp-status, /capability-search, /capability-audit)
- ~5 PM admin skills (/promote, /capture, /learn, /debrief, /decide)

The meta-infrastructure layer (runtime, exec, skill, mem, knowledge, MCP skills) is 25+ skills. This is 23% of the catalog dedicated to governing the other 77%. A healthy ratio is closer to 10%.

---

## Finding 7 — Architecture Document Proliferation Violates Final Operating Rule 4

Final Operating Rule 4: "Architecture documents are written once, updated occasionally, and consulted rarely. They are not part of the daily context path."

There are 39 architecture documents. Several describe the same system from different angles:

**Overlapping pairs/groups:**
- AUTONOMOUS-ORCHESTRATION.md + AUTONOMOUS-OPERATIONAL-FLOWS.md + EXECUTION-ORCHESTRATION.md + WORKFLOW-ROUTING.md: all describe intent-routing and sequencing
- BOUNDED-RUNTIME.md + RUNTIME-STATE-SCHEMA.md: runtime is the schema
- DYNAMIC-INVOCATION-SYSTEM.md + SKILL-ROUTING-SYSTEM.md: same topic, different level
- SKILL-ARCHITECTURE.md + DYNAMIC-CAPABILITY-GENERATION.md: capability management from two angles
- CONTEXT-ENGINEERING-SYSTEM.md + CONTEXT-ARCHITECTURE.md + CONTEXT-DIAGNOSTICS.md + CONTEXT-SELECTION-SYSTEM.md: context described 4 times

At 39 documents, the architecture layer has become a documentation system for a documentation system.

---

## Finding 8 — The Retry Backoff Is Behavior Theater

The retry backoff specification (from BOUNDED-RUNTIME.md):
- 1st retry: "Immediate re-run"
- 2nd retry: "Re-run with context refresh (re-read input files)"
- 3rd retry: "Re-run with operator-provided clarification before running"

"Context refresh (re-read input files)" is: read the file again. This takes one line, not an architectural specification.

"Operator-provided clarification before running" is: ask the user what they want. This is a normal conversational move, not a retry strategy.

The elaborate specification names trivial behavior as if it were a technical protocol. This is the pattern of autonomy theater at the behavior level: making Claude asking a follow-up question sound like "3rd-attempt retry with operator-provided clarification protocol."

---

## The Correct Final Architecture

### Principle 1 — One Runtime, One Persistence Layer

The runtime is a single human-gated execution layer with file-based state. No SQLite. No dual-write. No cache vs. source-of-truth tension.

```
runtime/
├── state/
│   ├── active-workflows.json    ← write atomically (temp→rename)
│   └── workflow-history.json   ← append-only
├── events/
│   └── queue.json              ← append-only
├── plans/
│   └── {wf-id}.json           ← immutable after APPROVED
└── snapshots/
    └── {wf-id}-step{N}.json   ← immutable after write
```

That's it. Checkpoints, persistence tables, and context_summaries are eliminated. The snapshot files ARE the checkpoints. The events queue IS the audit log. The active-workflows.json IS the source of truth.

**Recovery from crash:** Read active-workflows.json. If a workflow is RUNNING, the last valid snapshot is the recovery anchor. The operator decides what to do. There is no "rebuild JSON from SQLite" because there is no SQLite.

### Principle 2 — Four Skills Run the Runtime (Not Eight)

The runtime interface is exactly four skills:

| Skill | Role |
|-------|------|
| `/runtime-start` | Propose a workflow plan; gate before step 1 |
| `/runtime-resume` | Resume a paused workflow from last snapshot |
| `/runtime-status` | Show current workflow state; optionally show history (`--history`) |
| `/runtime-recover` | Surface recovery options for a failed/interrupted workflow |

The `/exec-*` diagnostic skills (journal, timeline, snapshot, diagnose) are eliminated. Their function: `/runtime-status --history [wf-id]` covers the timeline; snapshots are human-readable JSON; diagnosis is `/runtime-recover`.

### Principle 3 — Routing Is CLAUDE.md + Skill Names (Not a 7-Component System)

The invocation system reduces to:
- **Explicit invocation:** Operator types `/skill-name` → runs immediately, no routing needed
- **Ambient routing:** CLAUDE.md signal table + natural language matching → suggests a skill → one confirmation
- **Discovery:** `/skill-lookup [keyword]` → searches registry → returns matches

The active `/skill-invoke` path (7-step routing pipeline with gates) is eliminated. When routing is needed, it is conversational: "This looks like a /pm-discovery — want me to run it?"

### Principle 4 — Skill Synthesis Is a Conversation, Not a Pipeline

New skills are created when needed:
1. Operator describes what they need
2. Claude drafts a skill using the canonical template
3. Operator approves → file is written
4. Done

The gap-log, occurrence counting, and three-gate synthesis flow are retired. The production bar is still the same (one job, specific triggers, tested before marking active). The process is just a conversation.

### Principle 5 — The Memory System Stays as Designed (P16 Is Right)

MEMORY.md index + selective file loading is the right model. This system is not over-built — it is appropriately scaled. No changes.

### Principle 6 — The MCP Capability Layer Stays, With One Simplification

P19's permission model (R/RW/NET/DESTR), registry, and audit trail are appropriate governance for external tools. One change: remove GATE_BYPASS anomaly detection.

The GATE_BYPASS anomaly fires when a NET/DESTR tool is invoked with `gated: false`. For a solo operator, every tool invocation IS operator-initiated. The only way to have `gated: false` on a NET/DESTR tool is if the logging code didn't set the flag — which is a code quality issue, not a governance issue. The anomaly detection reads real for a multi-user system; it is paperwork theater for one.

Keep: HIGH_ERROR_RATE anomaly (genuinely signals tool reliability problems). Simplify VOLUME_SPIKE threshold to 100 (50 is too easily triggered). Remove GATE_BYPASS detection.

### Principle 7 — Consolidate Architecture Documentation

From 39 documents, the target is 20 through merges:

| Merged Document | Sources |
|----------------|---------|
| `OPERATIONAL-ROUTING.md` | AUTONOMOUS-ORCHESTRATION.md + AUTONOMOUS-OPERATIONAL-FLOWS.md + EXECUTION-ORCHESTRATION.md + WORKFLOW-ROUTING.md |
| `RUNTIME-SYSTEM.md` | BOUNDED-RUNTIME.md + RUNTIME-STATE-SCHEMA.md |
| `SKILL-SYSTEM.md` | DYNAMIC-INVOCATION-SYSTEM.md + SKILL-ROUTING-SYSTEM.md + SKILL-ARCHITECTURE.md (routing sections) |
| `CAPABILITY-GENERATION.md` | DYNAMIC-CAPABILITY-GENERATION.md (standalone — well-written) |
| `CONTEXT-SYSTEM.md` | CONTEXT-ENGINEERING-SYSTEM.md + CONTEXT-ARCHITECTURE.md + CONTEXT-SELECTION-SYSTEM.md (CONTEXT-DIAGNOSTICS.md stays separate) |

---

## FINAL Autonomy Guardrails

These are the only autonomy rules that matter. Governance rules that describe trivial behavior as protocol are eliminated.

**A-1 (Human gate before every step transition)**  
No step N+1 begins until the operator approves at the gate after step N. "Continue", "yes", "proceed", "next step" — exactly one of these gates exactly one step. This rule is non-negotiable.

**A-2 (One workflow in RUNNING state)**  
Only one workflow can be RUNNING at a time. A second can be PAUSED or PLANNED. Two running simultaneously is not a supported state.

**A-3 (Plans declared before execution)**  
All steps, output paths, and dependencies are written to the plan file before step 1 begins. Steps cannot be added during execution. The operator approves the full plan.

**A-4 (Failure is visible, not silent)**  
A failed step immediately surfaces to the operator with options (RETRY / SKIP / REWIND / ABANDON). The runtime does not proceed, substitute, or invent an alternative without operator instruction.

**A-5 (Output paths are declared)**  
Every step declares its output path in the plan. No step writes to an undeclared location.

**A-6 (Session end pauses, never aborts)**  
If a session ends mid-workflow, the workflow becomes PAUSED. All snapshots are preserved. The next session opens with a resume offer.

**A-7 (No autonomous memory writes)**  
The runtime does not write to `memory/`, `CLAUDE.md`, or `strategy/` files during workflow execution. These are operator-controlled surfaces updated manually at session end.

**A-8 (External capabilities require gate)**  
NET-class tools require per-invocation or per-session pre-authorization. DESTR-class tools require per-invocation confirmation. No blanket session approval for DESTR.

---

## FINAL Orchestration Rules

**O-1 (Propose before executing)**  
For any multi-step or ambiguous request: surface the plan in one sentence before running anything. "This is a 3-step workflow: A → B → C. Start with A?"

**O-2 (One clarifying question maximum)**  
When intent is ambiguous: ask exactly one discriminating question. Never more. If still ambiguous after one question, default to the more general skill and say so.

**O-3 (Check before re-running)**  
Before executing a skill: check if its output file already exists. If it does, state it and ask whether to refresh or use the existing output.

**O-4 (Dependencies block, not bypass)**  
If a skill's declared input is missing: name what's missing and propose how to produce it. Do not improvise an alternative or run with incomplete input.

**O-5 (Skill then MCP)**  
When a workflow involves both a skill and an MCP: run the skill first (produces content), then invoke the MCP (renders/transmits). Never invoke a write-capable MCP without skill-produced input.

**O-6 (Maximum 7 steps per workflow)**  
Workflows longer than 7 steps are too large for meaningful operator review at each gate. Break them into sub-initiatives and link them rather than chaining them in one workflow.

**O-7 (Recover from last valid snapshot)**  
On workflow failure or interruption: the recovery anchor is the last valid snapshot. Never reconstruct state from memory or inference — always from the snapshot file.

---

## FINAL Simplification Recommendations

Ordered by impact-to-effort ratio.

### SR-1 — Eliminate SQLite Persistence Layer (P15) [HIGH IMPACT]

**Remove:**
- `runtime/persistence/execution.db`
- `scripts/db_init.py`
- `scripts/event_store.py`
- `scripts/checkpoint_manager.py`
- `scripts/recovery_engine.py`
- `scripts/artifact_tracker.py`
- `scripts/timeline_viewer.py`
- `.claude/commands/exec-journal.md`
- `.claude/commands/exec-timeline.md`
- `.claude/commands/exec-snapshot.md`
- `.claude/commands/exec-diagnose.md`
- `architecture/PERSISTENT-EXECUTION-SYSTEM.md`
- Governance rules B-11 through B-15

**Replace with:**
- Atomic writes in the runtime skills (temp→rename pattern, ~5 lines)
- `/runtime-status --history` for the exec-timeline use case

**Result:** -7 Python scripts, -4 skills, -1 architecture doc, -5 B-rules. Zero reduction in functionality for a single-operator workspace.

### SR-2 — Retire /skill-invoke, /skill-deps, /skill-gaps [MEDIUM IMPACT]

These three meta-skills add routing overhead to skills that are already named descriptively and routeable through CLAUDE.md.

**Remove:**
- `.claude/commands/skill-invoke.md`
- `.claude/commands/skill-deps.md`
- `.claude/commands/skill-gaps.md`

**Keep:**
- `/skill-lookup` — discovery of the catalog
- `/skill-new` — scaffolded skill creation
- `skills/registry.json` — useful machine-readable index

**Routing behavior:** Absorbed into ambient Claude behavior via CLAUDE.md signal matching. For dependency resolution: the skill file says what it needs; missing inputs surface naturally during execution.

**Result:** -3 skills, -3 architecture subsections. No friction reduction for standard workflows.

### SR-3 — Retire the Gap Log System [LOW-MEDIUM IMPACT]

**Remove:**
- `skills/gap-log.jsonl` (active tracking)
- 3-gate synthesis flow from DYNAMIC-INVOCATION-SYSTEM.md
- Occurrence counting requirements

**Keep:**
- Skill creation template (templates/skill-spec.md)
- `/skill-new` skill, simplified: describe gap → Claude drafts → operator approves

**Result:** -1 data file, simplified skill creation narrative.

### SR-4 — Remove Domain Executor Abstraction [LOW IMPACT, HIGH SIGNAL]

Remove the 5-executor layer (Knowledge / Meeting / Strategy / PM / Cognitive) from the runtime architecture narrative.

**Replace with:** "Claude routes each workflow step to the appropriate skill based on the step specification."

**Result:** -30 lines of misleading architecture documentation, +clarity about how routing actually works.

### SR-5 — Consolidate Architecture Documents [MEDIUM IMPACT]

Execute the 5 document merges listed in Principle 7. Target: 39 → ~22 documents.

The merge is documentation work, not system change. But 39 documents creates maintenance debt: when the system changes, 39 documents may need updating instead of 22.

### SR-6 — Simplify P19 Anomaly Detection [LOW IMPACT]

In `scripts/capability_audit.py`:
- Remove GATE_BYPASS anomaly class
- Raise VOLUME_SPIKE threshold from 50 to 100

2-line code change. Removes theater-governance from a solo-operator tool.

---

## FINAL Maintenance Guidance

**Weekly (5 minutes):**
- `/briefing` → work → `/shutdown`
- No runtime maintenance required unless a workflow is active

**Monthly (30 minutes):**
- Run `/capability-audit --stats` to confirm tool health
- Run `/knowledge-qa` to surface decayed entries
- Run `/runtime-status --history` to review completed workflows

**Quarterly (90 minutes):**
- Run `/observe` — full workspace health
- Execute the simplification heuristics from FINAL-OPERATING-RULES.md
- Check skill usage: any skill unused in 6 months with a clear alternative → retire it
- Check architecture docs: any doc that describes a removed system → archive or delete
- The workspace should feel simpler at the end of quarterly review than at the start

**On new skill creation:**
- Describe the need conversationally
- Claude drafts from canonical template
- Operator reviews and approves
- Test once before marking active
- Add to skills/README.md (not to CLAUDE.md unless genuinely non-obvious trigger)

**On new MCP server:**
- Follow `playbooks/mcp-onboarding.md`
- No exceptions to permission class assessment
- Rebuild capability index after registration

**Never:**
- Add to CLAUDE.md System References (use WORKSPACE-GUIDE.md)
- Add PM skills to CLAUDE.md routing table (they self-route)
- Create a new architecture document for a system already described in an existing one
- Create a skill for a one-off need

---

## FINAL Operational Constraints

These are hard limits the workspace operates within. Not guidelines — constraints.

**Skill catalog:** Maximum 120 total skills. The current 110 leaves 10 slots. New skills require explicit justification (recurring need, ≥2 natural occurrences). Creating a new skill does not retire the constraint — retiring an old one does.

**Architecture documents:** Maximum 25. Currently at 39 — the merge roadmap (SR-5) brings this to ~22. New architecture documents require an existing document to be archived or merged.

**Workflow complexity:** Maximum 7 steps per workflow. Longer workflows must be decomposed into multiple linked initiatives.

**Ritual stack:** Maximum 6 active rituals (current: briefing, plan, focus, prep, shutdown, weekly — exactly 6). A new ritual requires retiring or demoting an existing one.

**Memory files:** Maximum 30 files in memory/ (current: ~18). MEMORY.md index must stay under 200 lines.

**Active workflows:** Maximum 1 in RUNNING state. Maximum 3 in PAUSED state. Old paused workflows must be resolved (resume or abandon) before new ones are created.

---

## FINAL Anti-Complexity Rules

These are rules against patterns specifically observed in this workspace's growth.

**AC-1 (No dual persistence)**  
One data format per concern. If runtime state lives in JSON, it lives only in JSON. Mirroring to SQLite, a second JSON format, or a summary table is forbidden.

**AC-2 (No components that are just naming)**  
If a "component" has no code, no file, and is not invokable — it is not a component. It is either documented behavior (belongs in a skill) or unnecessary abstraction (belongs deleted).

**AC-3 (No meta-skills that govern skill invocation)**  
Skills that route to other skills are routing documentation that should live in CLAUDE.md, not additional commands. /skill-invoke governing /pm-discovery is a layer on a layer on a layer.

**AC-4 (No governance for self-governing behavior)**  
When the operator is the only actor, gate-bypass detection is monitoring the operator's own behavior. Gate compliance is enforced by the operator, not audited by the system. Anomaly detection is justified only for errors the operator cannot observe directly (tool reliability).

**AC-5 (No retry protocol for asking questions)**  
When a step fails for unclear reasons, the recovery is: ask the operator what happened and what to do. Specifying this as "3rd-attempt retry with operator-provided clarification" is behavior theater. Name trivial behavior trivially.

**AC-6 (No architecture documents for removed systems)**  
When a system is simplified or removed, its architecture document is archived or deleted, not preserved as documentation of what was. The architecture directory describes the current system.

**AC-7 (Skill count growth requires skill retirement)**  
The catalog grows by displacement, not by accumulation. Every new skill added beyond 110 requires identifying a skill to retire. The catalog is a finite resource with a cognitive budget.

**AC-8 (Document one thing once)**  
If two architecture documents describe the same system (intent routing, MCP selection, context loading), they must be merged. The fact that they were written at different phases of development does not justify duplicate documents at steady state.

**AC-9 (No elaborate specification of simple behavior)**  
"Re-read input files" does not require a named retry strategy. "Ask the user a question" does not require a recovery protocol. Naming trivial behavior with elaborate terms creates a false sense of infrastructure. Write what actually happens.

**AC-10 (The operator's cognitive load is the system's primary resource)**  
Every skill, rule, document, and abstraction has a cost: operator attention. The question is not "does this add capability?" but "does this add capability faster than it adds cognitive overhead?" If not, don't build it.

---

## Summary Scorecard

| Dimension | Current State | Target State |
|-----------|--------------|-------------|
| Persistence layers | 2 (JSON + SQLite) | 1 (JSON, atomic writes) |
| Runtime skills | 8 (/runtime-* + /exec-*) | 4 (/runtime-* only) |
| Python scripts (runtime) | 6 | 0 (replaced by atomic writes in skills) |
| Meta-skills | ~10 (/skill-invoke, /skill-deps, /skill-gaps, /exec-*) | 5 (/skill-lookup, /skill-new, /mcp-status, /capability-search, /capability-audit) |
| Architecture documents | 39 | ~22 |
| Governance rules (B+G+O+A) | 28+ | 16 (A1-A8 + O1-O7, plus G-rules for MCP) |
| Effective skill count | 110 | 110 (no change to PM/content skills) |
| Working skills retired | 0 | 3 (/skill-invoke, /skill-deps, /skill-gaps) |
| Data files (runtime) | 8+ | 5 |

The functional capability of the workspace does not decrease. The complexity of maintaining and understanding it decreases substantially. This is the correct trade.

---

## One-Line System Definition

This workspace is a **skill library with file-based memory, operator-gated multi-step workflows, and governed external tool access** — nothing more, nothing less. If a design element does not serve one of those three functions for one operator, it should not exist.
