# Final Cognitive Runtime Review
## Enterprise Intelligence Workspace — Authoritative Architecture Audit

**Date:** 2026-05-23  
**Stance:** World-class AI strategist · elite operator · cognitive systems architect · runtime engineer · FAANG principal PM · operational excellence leader  
**Scope:** Full workspace — all 145 skills, 56 architecture docs, all memory, runtime, trace, observability, knowledge, strategy, execution, PM, cognitive, retrieval, and persistence systems.

---

## The Hard Truth First

The workspace has undergone 30 build phases and one formal simplification review (P20). The P20 review diagnosed the right problems and issued correct remediation orders. Most of those orders were never executed.

The result: the workspace is larger, more complex, and harder to maintain today than when P20 was written — despite P20's explicit goal being the opposite.

**Current measurements against P20 operational constraints:**

| Constraint | P20 Ceiling | Current State | Status |
|-----------|-------------|---------------|--------|
| Skills | ≤ 120 | **145** | ⚠ CRITICAL (+25) |
| Architecture docs | ≤ 25 | **56** | ⚠ CRITICAL (+31) |
| Memory files | ≤ 30 | 23 | ✓ OK |
| MEMORY.md lines | ≤ 200 | 27 | ✓ OK |
| Ritual stack | ≤ 6 | 6 | ✓ OK |

The memory layer is the only dimension within bounds. Every other major dimension is critically over-limit.

This is not a warning. It is structural failure of the constraint system. The constraints were not enforced while building P21 through P30. The workspace has drifted from a cognitive operating environment toward the thing it was explicitly designed not to become: a complex, multi-layered AI infrastructure system.

---

## Part I — System-by-System Findings

### Finding 1 — P20 Consolidation Was Declared, Not Executed

P20 SR-5 ordered 5 document merges: create merged documents, delete source documents. The merged documents were created. The source documents were never deleted.

**13 zombie source documents still present:**

| Zombie Document | Was Merged Into | Status |
|----------------|----------------|--------|
| `AUTONOMOUS-ORCHESTRATION.md` | `OPERATIONAL-ROUTING.md` | Dead — delete |
| `AUTONOMOUS-OPERATIONAL-FLOWS.md` | `OPERATIONAL-ROUTING.md` | Dead — delete |
| `EXECUTION-ORCHESTRATION.md` | `OPERATIONAL-ROUTING.md` | Dead — delete |
| `WORKFLOW-ROUTING.md` | `OPERATIONAL-ROUTING.md` | Dead — delete |
| `DYNAMIC-INVOCATION-SYSTEM.md` | `SKILL-SYSTEM.md` | Dead — delete |
| `SKILL-ROUTING-SYSTEM.md` | `SKILL-SYSTEM.md` | Dead — delete |
| `SKILL-ARCHITECTURE.md` | `SKILL-SYSTEM.md` | Dead — delete |
| `CONTEXT-ENGINEERING-SYSTEM.md` | `CONTEXT-SYSTEM.md` | Dead — delete |
| `CONTEXT-ARCHITECTURE.md` | `CONTEXT-SYSTEM.md` | Dead — delete |
| `CONTEXT-SELECTION-SYSTEM.md` | `CONTEXT-SYSTEM.md` | Dead — delete |
| `BOUNDED-RUNTIME.md` | `RUNTIME-SYSTEM.md` | Dead — delete |
| `RUNTIME-STATE-SCHEMA.md` | `RUNTIME-SYSTEM.md` | Dead — delete |
| `PERSISTENT-EXECUTION-SYSTEM.md` | P15 ELIMINATED in SR-1 | Dead — delete |

These 13 documents describe either (a) systems already documented in the merged documents or (b) a system that was eliminated entirely. Their continued presence inflates the architecture directory by 23% and creates context confusion when any agent or operator reads the directory.

---

### Finding 2 — P14/P15 Skill Remnants Were Never Retired

P20 SR-1 ordered retirement of 4 execution diagnostic skills (P15 remnants). P20 SR-2 ordered retirement of 3 dynamic invocation skills (P14 remnants). None were deleted.

**7 zombie skills still in `.claude/commands/`:**

| Zombie Skill | Retirement Order | What Covers It Now |
|-------------|-----------------|-------------------|
| `exec-journal.md` | SR-1 | `/runtime-status --history` |
| `exec-timeline.md` | SR-1 | `/runtime-status --history` |
| `exec-snapshot.md` | SR-1 | Snapshot files are human-readable JSON |
| `exec-diagnose.md` | SR-1 | `/runtime-recover` |
| `skill-invoke.md` | SR-2 | Direct invocation + CLAUDE.md ambient routing |
| `skill-deps.md` | SR-2 | Skill files declare their own dependencies |
| `skill-gaps.md` | SR-2 | Conversational skill creation via `/skill-new` |

Every one of these skills was identified by name, with a specific replacement, in FINAL-SIMPLIFICATION-REVIEW.md written in the same session. They are still here.

---

### Finding 3 — Architecture Doc Explosion Since P20

After P20, 10 new architecture documents were created for P21–P30 (one per phase). None retired an existing document. The net result: 39 → 56 architecture documents, against a ceiling of 25.

**New docs added post-P20:**
TRACE-CAPTURE-SYSTEM.md · OBSERVABILITY-SYSTEM.md · DECISION-INTELLIGENCE-SYSTEM.md · STRATEGIC-INTELLIGENCE-SYSTEM.md · KNOWLEDGE-SYNTHESIS-ENGINE.md · PERSONAL-LEARNING-ANALYTICS.md · EXECUTION-INTELLIGENCE-SYSTEM.md · RUNTIME-HARDENING-SYSTEM.md · COGNITIVE-LOAD-MANAGEMENT.md · WORKSPACE-AUDIT-FRAMEWORK.md

These are not wrong to have written. The failure is not writing them — it is never archiving an older document to compensate. The hard constraint (≤25) was ignored as a build tax. It is not optional.

---

### Finding 4 — Skill Sprawl: 145 Commands, 33+ Invisible

The 145 skills break down as follows:

| Category | Count | Routing Table Visibility |
|----------|-------|------------------------|
| PM skills (pm-*) | 44 | Visible (self-routing) |
| Daily operations | 6 | Visible |
| Capture/synthesis | 6 | Visible |
| Knowledge (core) | 9 | Visible |
| Knowledge (analytics: P17/P18/P25/P26) | 15 | Partial (9 invisible) |
| Strategy | 7 | 6 visible, 1 invisible |
| Execution operations | 9 | 6 visible, 3 invisible |
| Trace & recall | 5 | Visible |
| Cognitive tools | 6 | Visible |
| Decision intelligence | 5 | Visible |
| Runtime | 4 | Visible (no routing entry) |
| Runtime hardening | 3 | Visible |
| Cognitive load | 3 | Visible |
| Workspace audit | 3 | Visible |
| Observability | 6 | Visible |
| **P14 remnants** | **3** | **Invisible — retired but present** |
| **P15 remnants** | **4** | **Invisible — retired but present** |
| Memory system (P16) | 6 | **Invisible — not in routing table** |
| Skill management | 2+3=5 | 2 invisible (kept), 3 ghost (retired) |
| MCP system | 4 | **Invisible — not in routing table** |
| Context engineering (P8) | 2 | **Invisible — not in routing table** |
| AI evaluation | 2 | **Invisible — not in routing table** |
| Misc | ~6 | Partial |

**The invisibility problem:** 33+ skills exist in `.claude/commands/` but have no entry in the CLAUDE.md routing table. A skill that is not discoverable is effectively dead weight — the operator cannot trigger it and Claude cannot suggest it. The `/mem-*` system (6 skills) and `/mcp-*` system (4 skills) are invisible despite being real capabilities.

---

### Finding 5 — P16 Memory System Creates Ghost Layer

The P16 memory system (mem-capture, mem-recall, mem-adr, mem-failure, mem-reconstruct, mem-hygiene) was declared sound in P20 ("P16 Is Right"). But:

1. None of these 6 skills appear in the CLAUDE.md routing table
2. The workspace now has Claude's native auto-memory system handling session-to-session memory persistence
3. The `memory/` directory + MEMORY.md index + Claude auto-memory together already serve the P16 use cases
4. `/mem-capture` duplicates what `/capture` + CLAUDE.md memory protocol already does
5. `/mem-recall` duplicates reading `memory/*.md` files directly
6. `/mem-reconstruct` + `/mem-hygiene` are maintenance tasks absorbed by natural memory hygiene

The P16 system was "right" architecturally, but has been superseded by simpler, already-present mechanisms. Six skills that cannot be discovered and duplicate simpler behavior are a complexity liability.

---

### Finding 6 — The Runtime Architecture Doc Still Contains Theater

`RUNTIME-SYSTEM.md` (the P20-consolidated runtime document) opens with the "Executive Orchestrator" + "Domain Executors" component diagram that FINAL-SIMPLIFICATION-REVIEW.md explicitly identified as "autonomy theater" (Findings 2, 3). The simplification review was incorporated into a NEW document, but the NEW document preserved the old framing. The consolidation merged words without applying the finding.

The system description should read: "Claude reads `active-workflows.json`, surfaces paused workflows, proposes a plan, and gates on every step." This is the entire runtime.

---

### Finding 7 — Knowledge Layer Fragmentation (15+ Skills)

The knowledge system has grown across 4 P-series phases (P17/P18/P25/P26) into 15 knowledge-specific skills plus `/learn`, `/recall`, `/synthesize`, `/promote`, `/pattern` from earlier phases. The operator faces:

- `/learn` vs `/repo-learn` (both capture knowledge)
- `/recall` vs `/knowledge-graph` vs `/knowledge-cluster` (all retrieve/surface knowledge)
- `/knowledge-validate` vs `/knowledge-qa` vs `/knowledge-review` (all assess quality)
- `/analogy` + `/contradiction-register` + `/knowledge-gap` (synthesis layer)
- `/learning-velocity` + `/learning-source` + `/knowledge-utilization` (analytics layer)

This is not necessarily wrong — each skill genuinely has a different job. But 20+ knowledge skills in a solo operator workspace represents a discovery problem: the operator cannot hold the full knowledge menu in working memory.

---

### Finding 8 — Multiple Redundant Analytics Layers

Three separate phases built execution analytics:
- P22 Observability: ops-dashboard, exec-inspect, failure-review, retrieval-diag
- P27 Execution Intelligence: exec-throughput, exec-allocation, exec-friction
- P30 Workspace Audit: workspace-audit, skill-overlap, simplify

Plus trace infrastructure from P21: trace-capture, workflow-journal, trace-recall, trace-search, pattern-mine.

Plus runtime validation from P28: runtime-validate, snapshot-verify, reliability-check.

That is 19 skills in the "observe/measure/analyze the workspace itself" category. For a solo operator, this level of introspective tooling creates its own cognitive overhead. The workspace is spending more cognitive budget observing itself than doing the work that justifies the observation.

---

### Finding 9 — MCP System Is Invisible

The MCP capability layer (P19) has 4 skills: mcp-register, mcp-status, capability-search, capability-audit. Zero of these appear in the CLAUDE.md routing table. An operator managing MCP servers cannot discover these capabilities without already knowing they exist. This is a routing design failure.

---

### Finding 10 — Duplicated Memory Files for Eliminated Systems

`memory/persistent_execution.md` documents P15, which was ELIMINATED in SR-1. The file accurately records the elimination but should have been removed once the elimination was confirmed. Keeping documentation of an eliminated system in the active memory layer adds noise to memory scanning.

`memory/dynamic_invocation.md` documents P14, which was partially simplified (3 of 5 skills retired per SR-2, except the retirements were never executed). This file's continued presence implies P14 is active when it has been operationally simplified.

---

## Part II — FINAL Workspace Architecture

### The System Is Three Things

This workspace is, and should remain, exactly three things:

**1. A skill library** — Named, invokable behaviors covering PM work, operational intelligence, cognitive tools, strategic analysis, and knowledge management. Skills are files. Claude loads them on demand.

**2. A file-based operational memory** — A directory of structured markdown files encoding what matters across sessions: knowledge, decisions, traces, strategies, memory. No database. No sync layer. Human-readable at all times.

**3. A governed external tool interface** — The MCP capability layer gives controlled access to external services (Figma, Google, Slack, etc.) under a 4-class permission model. All external writes require gates.

Everything else is either commentary on these three things or complexity that has grown around them without adding to their function.

### Canonical Directory Map

```
Enterprise-Intelligence-Workspace/
├── CLAUDE.md                    ← behavior rules + routing table (≤1,500 tokens)
├── .claude/commands/*.md        ← skill library (TARGET: ≤90 skills)
├── memory/
│   ├── MEMORY.md               ← index only (≤200 lines)
│   └── *.md                    ← oriented facts, per P-series system (≤30 files)
├── knowledge/<domain>/         ← permanent knowledge entries
├── strategy/
│   ├── active-bets.md
│   ├── monthly/
│   └── signals/
├── traces/
│   ├── TRACE-INDEX.md
│   ├── executions/
│   ├── journal/
│   ├── patterns/
│   └── primitives/
├── runtime/
│   ├── state/
│   │   ├── active-workflows.json
│   │   └── workflow-history.json
│   ├── events/queue.json
│   ├── plans/
│   └── snapshots/
├── notes/raw/                  ← inbox
├── meeting-intelligence/       ← raw + processed
├── decision-frameworks/
│   └── decisions-log.md
├── architecture/               ← reference only (TARGET: ≤22 docs)
└── skills/README.md            ← skill registry (sync with .claude/commands/)
```

### The Runtime Is Four Lines of Behavior

The "bounded autonomous runtime" is this: Claude reads `active-workflows.json`. If a workflow is RUNNING or PAUSED, Claude surfaces it. The operator chooses to resume or abandon. When starting new work, Claude writes a plan, gets approval, then gates on each step. On failure, Claude surfaces recovery options from the last snapshot.

That is it. No Executive Orchestrator. No Domain Executors. No retry protocol taxonomy. Four skills implement this: `/runtime-start`, `/runtime-resume`, `/runtime-status`, `/runtime-recover`.

---

## Part III — Concrete Simplification Plan

### Step 1 — Delete 13 Architecture Zombies (Immediate)

These files describe either an eliminated system or a system whose content now lives in a consolidated document. Deleting them loses nothing and reduces the architecture directory by 23%.

```
DELETE immediately:
architecture/AUTONOMOUS-ORCHESTRATION.md
architecture/AUTONOMOUS-OPERATIONAL-FLOWS.md
architecture/EXECUTION-ORCHESTRATION.md
architecture/WORKFLOW-ROUTING.md
architecture/DYNAMIC-INVOCATION-SYSTEM.md
architecture/SKILL-ROUTING-SYSTEM.md
architecture/SKILL-ARCHITECTURE.md
architecture/CONTEXT-ENGINEERING-SYSTEM.md
architecture/CONTEXT-ARCHITECTURE.md
architecture/CONTEXT-SELECTION-SYSTEM.md
architecture/BOUNDED-RUNTIME.md
architecture/RUNTIME-STATE-SCHEMA.md
architecture/PERSISTENT-EXECUTION-SYSTEM.md
```

Remaining after Step 1: 56 - 13 = **43 architecture docs**

### Step 2 — Archive Historical P-Series Docs

These docs describe the state of the workspace as of a specific build phase. That history is in MEMORY.md and git history. The architecture directory should describe the current system.

```
ARCHIVE (move to architecture/archive/):
PRODUCTION-AI-LEARNING-SYSTEM.md       ← P9 historical
COGNITIVE-ACCELERATION-SYSTEM.md       ← P10 historical  
DAILY-OPERATING-SYSTEM.md              ← P11 historical
FINAL-REVIEW.md                        ← P12, superseded by FINAL-SIMPLIFICATION-REVIEW.md
MEMORY-CONTINUITY-SYSTEM.md            ← P16 historical, covered by MEMORY-MAP.md
KNOWLEDGE-QA-SYSTEM.md                 ← P18 historical, covered by KNOWLEDGE-ARCHITECTURE.md
KNOWLEDGE-COMPOUNDING-SYSTEM.md        ← P17 historical, covered by KNOWLEDGE-ARCHITECTURE.md
```

Remaining after Step 2: 43 - 7 = **36 architecture docs**

### Step 3 — Merge Duplicate-Topic Docs

```
MERGE:
MEMORY-MAP.md + MEMORY-SCHEMAS.md + COGNITIVE-MEMORY-SYSTEM.md
  → MEMORY-SYSTEM.md (delete all three after merge)

RETRIEVAL-SYSTEM.md + RETRIEVAL-INTELLIGENCE.md
  → RETRIEVAL-SYSTEM.md (absorb and delete RETRIEVAL-INTELLIGENCE.md)

MCP-ROUTING-SYSTEM.md + MCP-CAPABILITY-LAYER.md
  → MCP-SYSTEM.md (delete both after merge)
```

Net: -4 docs (3 merged into 1 + 1 absorbed + 2 merged into 1 = save 4)

Remaining after Step 3: 36 - 4 = **32 architecture docs**

### Step 4 — Evaluate and Archive Low-Signal Docs

```
ARCHIVE (low signal, content absorbed elsewhere):
EXECUTION-RIGOR-SYSTEM.md              ← superseded by RUNTIME-HARDENING-SYSTEM.md
REASONING-STRUCTURE.md                 ← cognitive framing doc, superseded by skills
BEHAVIORAL-TUNING.md                   ← superseded by FINAL-OPERATING-RULES.md
PROMPT-ARCHITECTURE.md                 ← prompt management, superseded by skill files
MAINTENANCE-CONVENTIONS.md             ← absorbed by FINAL-OPERATING-RULES.md
```

Remaining after Step 4: 32 - 5 = **27 architecture docs** — approaching target of ≤25.

Final 2 to archive: the operator can choose from remaining docs based on currency.

**Target architecture directory (22 docs):**
```
WORKSPACE-GUIDE.md
FINAL-SIMPLIFICATION-REVIEW.md
FINAL-OPERATING-RULES.md
RUNTIME-SYSTEM.md (updated — remove theater framing)
RUNTIME-HARDENING-SYSTEM.md
RECOVERY-PLAYBOOKS.md
SKILL-SYSTEM.md
OPERATIONAL-ROUTING.md
CONTEXT-SYSTEM.md
CONTEXT-DIAGNOSTICS.md
KNOWLEDGE-ARCHITECTURE.md
MEMORY-SYSTEM.md (merged)
RETRIEVAL-SYSTEM.md (merged)
MCP-SYSTEM.md (merged)
SYSTEM-ARCHITECTURE.md
DATA-FLOWS.md
ANTI-PATTERNS.md
TRACE-CAPTURE-SYSTEM.md
OBSERVABILITY-SYSTEM.md
DECISION-INTELLIGENCE-SYSTEM.md
WORKSPACE-AUDIT-FRAMEWORK.md
FINAL-COGNITIVE-RUNTIME-REVIEW.md (this document)
```

---

### Step 5 — Retire 7 Zombie Skills (Immediate)

These were ordered retired in P20. Delete the files:

```
DELETE:
.claude/commands/exec-journal.md
.claude/commands/exec-timeline.md
.claude/commands/exec-snapshot.md
.claude/commands/exec-diagnose.md
.claude/commands/skill-invoke.md
.claude/commands/skill-deps.md
.claude/commands/skill-gaps.md
```

Remove corresponding rows from `skills/README.md`.
Skills after Step 5: 145 - 7 = **138 skills**

### Step 6 — Retire P16 Memory Skills

The `/mem-*` system (6 skills) is not discoverable, duplicates simpler mechanisms, and has been superseded by the auto-memory system + direct MEMORY.md reads.

```
RETIRE:
.claude/commands/mem-capture.md      ← /capture + CLAUDE.md memory protocol covers this
.claude/commands/mem-recall.md       ← reading memory/*.md directly
.claude/commands/mem-adr.md          ← /decide + decisions-log.md covers ADR function
.claude/commands/mem-failure.md      ← /failure-review covers this
.claude/commands/mem-reconstruct.md  ← /runtime-recover covers workflow reconstruction
.claude/commands/mem-hygiene.md      ← /workspace-audit covers memory hygiene
```

Skills after Step 6: 138 - 6 = **132 skills**

### Step 7 — Retire Invisible/Superseded Skills

```
RETIRE:
.claude/commands/context-audit.md    ← P8 CE system; not in routing; superseded
.claude/commands/context-compile.md  ← P8 CE system; not in routing; superseded
.claude/commands/eval.md             ← AI evaluation; absorbed by /ops-dashboard + /debug-ai
.claude/commands/prod-review.md      ← production review; absorbed by /exec-review + /observe
.claude/commands/decision-review.md  ← absorbed by /decision-due + /decision-recall
.claude/commands/arch-critique.md    ← architectural review; ad-hoc conversational task
```

Skills after Step 7: 132 - 6 = **126 skills**

### Step 8 — Route-Table MCP and Skill Management Skills

These 6 skills have genuine value but are invisible. Either add them to the routing table or consolidate them:

Add to CLAUDE.md routing table under a new `**Tool access**` section:
- `/mcp-register` — Register and configure a new MCP server
- `/mcp-status` — Health check on registered MCP servers
- `/capability-search` — Find available MCP tool capabilities
- `/capability-audit` — Audit MCP tool usage and anomalies

Add to CLAUDE.md routing under `**Knowledge**`:
- `/skill-lookup` — Search the skill catalog by keyword

Add to CLAUDE.md routing under `**Daily operations**`:
- `/skill-new` — Create a new skill from template

Skills count stays at 126. But now 6 previously invisible skills become discoverable.

### Step 9 — Consolidate Knowledge Analytics

15+ knowledge skills is too many distinct invocations. The analytics layer (P26) overlaps with the compounding layer (P17) semantically:

```
RETIRE (absorbed by other skills):
.claude/commands/knowledge-validate.md  ← /knowledge-qa is the higher-quality check
.claude/commands/knowledge-review.md    ← /knowledge-qa + /recall-test covers this
```

Skills after Step 9: 126 - 2 = **124 skills**

### Step 10 — Target State After Simplification

```
Projected state after all 10 steps:
- Skills: 124 (still 4 over ceiling — retire 4 more at next /workspace-audit)
- Architecture docs: ≈ 22 (✓ within ceiling)
- Memory files: 23 (✓ within ceiling, after removing 2 dead memory files)
- MEMORY.md: 27 lines (✓ well within ceiling)
```

**Two memory files to remove:**
```
DELETE:
memory/persistent_execution.md    ← P15 was eliminated; no need to document it in active memory
memory/dynamic_invocation.md      ← P14 was simplified; historical, not operational
```

The final 4 skills to reach the 120 ceiling should be identified by running `/skill-overlap` on the knowledge and observability sections, where the highest density of overlap exists.

---

## Part IV — The Ten Rule Sets

---

### 1. NON-NEGOTIABLE ARCHITECTURAL RULES

**NAR-1 — Three things only.** This workspace is a skill library, a file-based operational memory, and a governed external tool interface. Every new component must fit one of these three categories or it does not belong.

**NAR-2 — One persistence format per concern.** Runtime state lives in JSON files, atomically written. No parallel database. No summary tables. No second format. If JSON is not sufficient, the design is wrong.

**NAR-3 — The operator is the only actor.** There is no autonomous background process. There is no self-initiating agent. All execution is Claude + file-reads + operator approval. A component that executes without explicit operator instruction is a design violation.

**NAR-4 — Skills are the runtime.** There is no middleware. There is no orchestration layer above the skill files. The skill file IS the behavior specification AND the execution contract.

**NAR-5 — Human-readable state at all times.** Every file in `runtime/`, `memory/`, `traces/`, `knowledge/`, and `strategy/` must be directly readable and editable by the operator without tooling. The moment a state artifact requires a tool to interpret, the design has violated operator sovereignty.

**NAR-6 — No component that only names behavior.** If a "component" has no file, no code, and is not invokable, it is not a component. It is commentary. It belongs in a comment in a skill file, not in a component diagram.

**NAR-7 — All active skills must be discoverable.** Every skill in `.claude/commands/` must appear in either the CLAUDE.md routing table or the `skills/README.md` with a clear trigger description. An undiscoverable skill is dead weight.

---

### 2. ANTI-DRIFT RULES

**ADR-1 — Ceiling violations trigger immediate retirement, not just noting.** When `/workspace-audit` reports a ceiling violation: the session does not end until at least one retirement or archive action is executed. Noting a violation without acting on it is drift.

**ADR-2 — New architecture doc requires an old one archived.** Creating a P-series architecture doc is permissible. Doing so without archiving or merging an existing doc is not. One-in one-out. This is not a suggestion.

**ADR-3 — New skill requires justification against the ceiling.** Before creating a skill, state: current skill count, ceiling, available budget. If budget is zero or negative, name the skill to retire before creating the new one.

**ADR-4 — Simplification orders have a 48-hour execution window.** When this document or `/simplify` issues a specific retirement or deletion order, the action executes in the next session. Orders that are "acknowledged but deferred" are drift. The P20 SR-1/SR-2 retirements that were never executed are the canonical example of what this rule prevents.

**ADR-5 — Autonomy theater is a drift signal.** When a design document describes trivial behavior using enterprise architecture language (retry protocols, recovery engines, orchestration meshes), it is masking a bias toward over-building. Name this immediately and simplify.

**ADR-6 — P-series phases are build events, not permanent landmarks.** A P-series memory file is written once, then may be deleted when the system it describes is either (a) stable and described by active skills, or (b) eliminated. Memory files are operational context, not a build log.

---

### 3. MAXIMUM COMPLEXITY LIMITS

| Resource | Hard Limit | Current | Action if Exceeded |
|---------|-----------|---------|-------------------|
| Skills | 120 | 145 | Retire before adding — no exceptions |
| Architecture docs | 25 | 56 | Archive before creating — no exceptions |
| Memory files | 30 | 23 | Clean stale files quarterly |
| MEMORY.md lines | 200 | 27 | Index only — never write content |
| Ritual stack | 6 | 6 | Retire to add |
| Workflow steps | 7 | N/A | Decompose if longer |
| Active workflows | 1 RUNNING | N/A | Resolve before starting new |
| Paused workflows | 3 max | N/A | Abandon oldest if at limit |
| Arch docs describing same system | 1 | Multiple | Merge immediately |
| Knowledge analytics skills | 8 | 13 | Target 8; retire low-signal |
| Execution analytics skills | 8 | 12 | Target 8; retire redundant |

Violations above the "Critical" threshold (>150 skills, >35 arch docs) indicate the constraint system has failed and emergency simplification is required before any build work.

---

### 4. OPERATIONAL SIMPLICITY RULES

**OSR-1 — The routing table is the system's operating interface.** What is not in the routing table effectively does not exist for the operator. The routing table is not a catalog of everything — it is the trigger map for non-obvious skills. Test: would an expert user not type the right command without seeing the routing entry? If they would figure it out naturally, don't add the routing entry.

**OSR-2 — One skill per job.** Skills should not have more than 2-3 `--flag` variants before becoming candidates for a parent skill that routes to them. The test: can you describe what this skill does in one sentence? If not, it is two skills.

**OSR-3 — The daily path is ≤5 hops.** From session start to productive output: CLAUDE.md load → MEMORY.md scan → briefing skill → work skill → capture. No workflow should require more than 5 skill invocations for standard work. If it does, the workflow is wrong.

**OSR-4 — Self-documenting names eliminate routing entries.** `/pm-sprint`, `/pm-prd`, `/pm-incident` do not need routing table entries because any PM who knows the concept types the right command. Routing entries are for skills whose names don't reveal their trigger.

**OSR-5 — No skill should require reading its predecessor skill to understand it.** Each skill is standalone. It declares its own context, reads its own files, and produces its own output. Skills that require "run /skill-A before /skill-B" are tightly coupled and candidates for merger.

**OSR-6 — Simplicity is a feature, not a failure.** A workspace that does 90% of the work with 70 skills is better than one that does 95% of the work with 145 skills. The 5% gap is not worth 107% more complexity.

---

### 5. BOUNDED AUTONOMY RULES

These are the only autonomy rules that govern this system. All prior autonomy rule sets (B-rules, G-rules variants) are superseded by this list.

**BAR-1 — Human gate before every step transition.** No step N+1 begins without explicit operator approval of step N's output and gate. "Continue" / "proceed" / "yes" approves exactly one step.

**BAR-2 — One workflow in RUNNING state.** This is a hard system invariant, not a guideline. Two simultaneous RUNNING workflows indicate a state corruption, not a feature.

**BAR-3 — Plans before execution.** All steps, output paths, and input dependencies are declared in the plan file before step 1. No mid-execution plan modifications.

**BAR-4 — Failures are visible, options are operator-chosen.** A failed step presents: RETRY / SKIP / REWIND / ABANDON. Claude does not select a recovery path without explicit operator instruction. Inventing alternatives is a guardrail violation.

**BAR-5 — Output paths are declared.** No step writes to an undeclared location. This is checkable before execution begins.

**BAR-6 — Session end pauses, never aborts.** Incomplete workflows become PAUSED with all snapshots preserved. The next session opens with a resume offer.

**BAR-7 — No autonomous memory writes during workflows.** The runtime does not modify `memory/`, `CLAUDE.md`, or `strategy/` during workflow execution. These surfaces are operator-controlled.

**BAR-8 — External tool gates are per-invocation for DESTR class.** NET-class tools: per-session pre-authorization acceptable. DESTR-class: per-invocation confirmation required. No blanket approvals for DESTR.

**BAR-9 — The system does not observe itself without operator instruction.** Auto-running `/workspace-audit` or `/ops-dashboard` as part of another workflow is prohibited. Introspective tools are operator-triggered only.

**BAR-10 — Autonomy ceiling: Claude proposes, operator decides.** This is the fundamental contract. Claude is a cognitive instrument. It produces analysis, options, drafts, and synthesis. The operator decides what is true, what to do, and what matters. Any design that shifts that boundary — skills that decide for the operator, workflows that execute without gates, recommendations that take effect without approval — violates the core contract.

---

### 6. MEMORY HYGIENE RULES

**MHR-1 — Memory describes current operational state, not build history.** A memory file that says "P15 was eliminated" is not operational memory. It is historical record. Delete it once the elimination is confirmed stable.

**MHR-2 — One memory file per system or topic, not per phase.** When P25 is built and P17 covered a related topic, update the P17 memory file or create a combined file — do not accumulate one file per build phase.

**MHR-3 — MEMORY.md is an index, not a log.** Every line in MEMORY.md should read as "this file exists and here is its relevance." Lines that say "P-series complete" without naming operational relevance are log entries masquerading as index entries.

**MHR-4 — Dead system memory files are deleted at next session.** When a system is eliminated (like P15), its memory file is deleted in the same session or the next. Never longer.

**MHR-5 — Memory files have a decay model.** A memory file that has not been read or referenced in 6 months is a candidate for deletion. The test: if this file vanished, would any current workflow fail? If no, delete it.

**MHR-6 — The auto-memory system (`.claude/projects/...`) and the workspace memory (`memory/`) serve different purposes.** Auto-memory is session-to-session context for Claude. Workspace memory is durable operational state for the operator. Do not mirror content between them. Auto-memory should reference workspace memory, not duplicate it.

**MHR-7 — Memory ceiling is 30 files.** This counts every `.md` file in `memory/` except MEMORY.md. When approaching 25 files, delete 3 before creating new ones. Memory files are not perpetual — they expire when their topic is stable, retired, or fully absorbed into skills.

---

### 7. RETRIEVAL QUALITY RULES

**RQR-1 — Retrieval is a skill, not a system.** `/recall` + direct file reads + KNOWLEDGE-INDEX.md is the retrieval system. It does not require a retrieval layer, a vector database, an embedding pipeline, or a semantic search API for a solo operator.

**RQR-2 — Retrieval quality degrades with catalog size.** Every additional knowledge entry, skill file, and architecture document adds retrieval surface area. Quality of recall and relevance of context loading degrade as the catalog grows. The skill ceiling and archive discipline are retrieval quality measures.

**RQR-3 — MEMORY.md is a 200-line retrieval surface.** It is loaded in every session. At 27 lines, it is excellent. At 200 lines, it becomes noise. Keep it under 100 lines where possible by writing better, more specific one-line hooks rather than more entries.

**RQR-4 — Knowledge entries are recalled by domain structure, not metadata soup.** Entries in `knowledge/<domain>/` are retrieved by scanning a domain directory. Avoid deep nesting, complex tag hierarchies, or faceted classification systems. Flat + domain-named is maximally retrievable.

**RQR-5 — Trace retrieval degrades without consistent tagging.** TRACE-INDEX.md is the retrieval surface for execution history. Traces without consistent session_type tags and goal statements are unretrievable. Quality gate: every trace entry must have a goal sentence and at least one tag.

**RQR-6 — Retrieval tools are optional, not required.** `/recall`, `/trace-recall`, `/knowledge-gap` are accelerators. Direct file reads are always the baseline retrieval method. A skill that cannot be used without running a prerequisite retrieval skill first is poorly designed.

---

### 8. SKILL CREATION CONSTRAINTS

**SCC-1 — Recurring need threshold: 3 natural occurrences.** A skill is justified when the same workflow has occurred organically 3+ times. One-time needs are conversational. Two-time needs are prompts. Three-time needs are skills.

**SCC-2 — One job per skill.** A skill does one thing, well, reliably. It has one primary verb. It produces one class of output. It reads from declared sources. If a skill description contains "and also", it is two skills.

**SCC-3 — Skills are not documentation.** A skill that only explains what to do is a playbook, not a skill. A skill executes a specific behavior with specific inputs and specific outputs. If there is no execution, there is no skill.

**SCC-4 — Every skill declares "Do NOT use for."** The skill's boundary is as important as its trigger. The "Do NOT use for" section, pointing to named adjacent skills, is required before a skill is marked Active.

**SCC-5 — New skill requires identifying a retirement candidate.** When the catalog is at or above 120 skills, creating a new skill requires naming a skill to retire before or simultaneously. This is enforced by the operator, not the system.

**SCC-6 — Skills are not built for completeness.** Building 44 PM skills is justified by PM workflow coverage. Building a PM skill "because we should have one for every PM activity" is completeness theater. Each skill must be justified by observed recurring need, not by taxonomy gaps.

**SCC-7 — Skill naming follows the command convention.** `verb` or `domain-verb`. `/capture`, `/debrief`, `/pm-strategy`. Not `/run-capture-workflow`, not `/execute-daily-debrief`, not `/intelligent-capture-system`. Shorter is better. The name is the trigger.

---

### 9. ORCHESTRATION CONSTRAINTS

**OCR-1 — Propose before executing.** Any multi-step or ambiguous request: one sentence plan before any execution. "This is a 3-step workflow: A → B → C. Start?" This is non-optional.

**OCR-2 — One clarifying question maximum.** Ambiguous intent: one discriminating question. Not three. Not a menu. If still unclear after one question, default to the more general skill and say so.

**OCR-3 — Seven steps maximum per workflow.** Longer than 7 steps cannot be meaningfully reviewed at each gate. Decompose into sub-initiatives linked by reference.

**OCR-4 — Skill invocation is not orchestration.** Running `/pm-strategy` is not an orchestrated workflow — it is one skill with one output. "Orchestration" applies only to multi-step, multi-skill, gated workflows with file-based state. Do not describe single skill invocations as workflows.

**OCR-5 — No skill invokes another skill.** Skills do not chain each other. If a workflow requires `/signal` then `/assumption-register` then `/strategy-review`, the operator invokes each. Claude may suggest the sequence. No skill auto-triggers another.

**OCR-6 — Output before process.** Skills deliver their output before explaining what they did. The output is the value. The methodology is secondary context.

**OCR-7 — Recovery from last valid snapshot, never from inference.** On workflow failure: read the last snapshot file. Never reconstruct state from conversation context, memory, or inference. If the snapshot is missing or corrupted, surface the problem and stop.

**OCR-8 — MCP tools are always last in a workflow step.** When a workflow step involves both skill work and an external tool call: skill produces content, then MCP renders/transmits. Never invoke a write-capable MCP without skill-generated input.

---

### 10. LONG-TERM MAINTENANCE RULES

**LMR-1 — The workspace simplifies at every quarterly review.** A quarterly review that ends with the same or more complexity than it started is a failed review. The target: at least 3 concrete retirements or archives per quarter.

**LMR-2 — P-series phases are complete when their skills work, not when their architecture docs are written.** The architecture document is a side effect of building. The skill files are the product. Do not confuse documentation completeness for system completeness.

**LMR-3 — The skills/README.md catalog must stay synchronized.** Count of `.claude/commands/*.md` files must match row count of the Active Skills table in `skills/README.md`. Drift between these two is hygiene debt that compounds into routing failures.

**LMR-4 — Every file in architecture/ must survive the currency test.** Quarterly: for each architecture doc, ask "does this describe the current system?" If it describes a retired system, archive it. If it duplicates another doc, merge it. If it hasn't been referenced or consulted in 12 months and isn't in the canonical 22, archive it.

**LMR-5 — Skills with zero usage in 12 months and no unique surface are retired.** Not "flagged for review." Retired. The retirement is the review outcome. The only exception: a skill with a unique capability that has not yet had its use case arise (a "waiting for the right situation" skill). Name this explicitly if keeping.

**LMR-6 — Adding infrastructure requires removing infrastructure.** A new system (observability, reliability, etc.) that adds 5+ skills must retire or merge 5+ existing skills. The workspace operates under a conservation law: capability density, not capability count, is the measure of quality.

**LMR-7 — The 3-minute test is the maintainability test.** Can you describe all active components of the workspace in 3 minutes? If no, simplify until yes. This is FINAL-OPERATING-RULES.md Rule 5, elevated to a maintenance rule: run the test at every quarterly review.

**LMR-8 — Skill quality degrades at high counts.** At 120 skills, the operator can hold the catalog in working memory with effort. At 145, key skills become invisible (as P16 and MCP skills demonstrate). At 200, the workspace becomes a legacy system that requires its own documentation system. Stop before 150.

**LMR-9 — Never build what Claude already does.** The auto-memory system, natural language routing, context loading from CLAUDE.md, and conversational task execution are capabilities that already exist in Claude Code. Building skills that replicate these behaviors (P14 dynamic invocation, P16 mem-capture) creates ghost layers. Ask: "would Claude do this naturally?" before building.

**LMR-10 — Long-term sustainability is measured by operator fatigue, not feature count.** The workspace is sustainable when starting a session feels clear, not heavy. When the routing table feels familiar, not overwhelming. When a new skill can be created in 10 minutes, not 45. When the operator trusts the system to remember what matters, without needing to manage the memory system. These are the sustainability metrics. Optimize for them.

---

## Part V — FINAL Operational Doctrine

### The System Identity Statement

This workspace is a **persistent cognitive operating environment for one operator** — a second brain, an execution cockpit, a PM intelligence layer, and a knowledge compounding engine. It is built for **one person doing elite knowledge work** across product strategy, execution, learning, and operational intelligence.

It is not, and must never become, an AI infrastructure platform, an organizational memory system, a multi-agent coordination fabric, or a governance-heavy enterprise runtime. The moment it begins to feel like something a team of engineers maintains, rather than something one person uses fluently, it has drifted past its design boundary.

### The Operator Experience Contract

Every session should feel like:
1. A clear, fast start (briefing → work, ≤3 minutes)
2. Frictionless skill invocation (command + output, no meta-workflows)
3. Effortless capture (raw → structured, one command)
4. Trustworthy memory (the workspace remembers; the operator doesn't have to)
5. A clean end (shutdown → seed for tomorrow, ≤5 minutes)

Anything that makes sessions feel heavier, longer, or more complicated is a complexity tax. Charge it immediately.

### The Build-vs-Maintain Balance

New capabilities should be added at one-third the current rate. The ratio of "building new skills" to "maintaining existing skills" has been approximately 10:1 through P1-P30. The healthy ratio is 2:1. The transition to maintenance mode begins now.

For every new skill added: two existing skills get reviewed for relevance. For every new architecture doc: one existing doc is archived. This is the new default posture.

### What Success Looks Like at P31+

- Skill count trending toward 90-100 (not growing)
- Architecture docs stable at 18-22
- MEMORY.md stays under 40 lines
- Every skill in the routing table gets invoked at least once per quarter
- The 3-minute workspace description test passes
- Quarterly reviews produce net negative complexity
- Session starts feel faster, not slower

The workspace is complete when it is fluent. Not when it is comprehensive.

---

## Summary: The Immediate Action List

Execute in order. Do not proceed to the next phase without completing the current one.

**Phase A — P20 Reckoning (this session or next)**
1. Delete 13 zombie architecture source docs (Step 1 above)
2. Delete 7 zombie P14/P15 skill files (Step 5 above)
3. Delete 2 dead memory files (persistent_execution.md, dynamic_invocation.md)

Net: -13 arch docs, -7 skills, -2 memory files

**Phase B — P16 Retirement**
4. Retire 6 `/mem-*` skills (Step 6 above)
5. Remove corresponding rows from skills/README.md

Net: -6 skills

**Phase C — Invisible Skill Retirement**
6. Retire 6 invisible/superseded skills (Step 7 above)
7. Make 6 MCP/skill-management skills visible in routing table (Step 8 above)

Net: -6 skills, +6 discoverable

**Phase D — Knowledge Consolidation**
8. Retire knowledge-validate.md and knowledge-review.md (Step 9 above)
9. Archive 7 historical P-series arch docs (Step 2 above)

Net: -2 skills, -7 arch docs

**Phase E — Architecture Merges**
10. Merge memory docs → MEMORY-SYSTEM.md (Step 3 above)
11. Merge retrieval docs (Step 3 above)
12. Merge MCP docs → MCP-SYSTEM.md (Step 3 above)
13. Archive low-signal docs (Step 4 above)

Net: -4 arch docs, -5 arch docs

**After Phase A-E:**
| Metric | Start | End | Target |
|--------|-------|-----|--------|
| Skills | 145 | ~124 | 120 |
| Architecture docs | 56 | ~22 | ≤25 |
| Memory files | 23 | 21 | ≤30 |

The remaining 4-skill gap closes at the next quarterly `/workspace-audit` → `/skill-overlap` → `/simplify` cycle.

---

## One-Sentence System Definition

This workspace is a **skill library with file-based memory, operator-gated multi-step workflows, governed external tool access, and PM intelligence coverage** — for one operator, permanently — and everything that does not serve that definition should not exist in it.
