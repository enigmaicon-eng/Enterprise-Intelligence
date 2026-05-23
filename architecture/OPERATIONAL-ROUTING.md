# Operational Routing
## Intent Detection, Workflow Sequencing, and Core Flow Maps

Consolidates: AUTONOMOUS-ORCHESTRATION.md, AUTONOMOUS-OPERATIONAL-FLOWS.md, EXECUTION-ORCHESTRATION.md, WORKFLOW-ROUTING.md

---

## Routing Philosophy

Routing is pattern recognition, not keyword matching. The user invokes a skill explicitly or describes intent — the goal is to read what they actually need and name the right skill. A strong suggestion beats a missed inference.

**Three routing modes:**

| Mode | Trigger | Behavior |
|------|---------|----------|
| Explicit | User types `/skill` | Run directly, no inference |
| Inferred | Clear single-skill signal | Suggest, then run on confirmation |
| Ambiguous | Multiple plausible skills | Name candidates, ask one question |

**Rule:** Suggest before executing. One sentence: "This looks like a `/pm-rca` — want me to run it with this incident as input?"

---

## Intent Classification

Every user input maps to one of four types:

| Type | Signals | Routing |
|------|---------|---------|
| **Operational** | "capture", "log", "process", "debrief" | Core operational skill |
| **Analytical** | "why", "root cause", "investigate" | PM analytical skill or `/synthesize` |
| **Generative** | "write", "draft", "design", "create" | PM generative skill or MCP |
| **Strategic** | "roadmap", "vision", "bet", "direction" | PM strategy cluster |

Mixed signals → decompose: "write a PRD based on discovery" = `/pm-discovery` + `/pm-prd`.

---

## Domain Detection

| Domain Signals | Skill Cluster |
|----------------|--------------|
| "meeting", "sync", "call", "transcript" | `/debrief`, `/capture` |
| "product", "feature", "launch", "users", "roadmap" | `/pm-*` skills |
| "decision", "chose", "going with", "we decided" | `/decide` |
| "strategy", "bets", "horizon", "OKR" | `/pm-strategy`, `/synthesize` |
| "note", "save", "remember", "reference" | `/capture` |
| "week", "review", "what happened" | `/weekly` |
| "workspace health", "telemetry" | `/observe` |
| "design", "mockup", "UI", Figma URL | MCP: Figma |
| "presentation", "deck", "slides" | MCP: Gamma |
| "email", "send", "inbox" | MCP: Gmail |

---

## Cognitive Mode Detection

| Mode | Signals | Output Implication |
|------|---------|-------------------|
| **Divergent** | "brainstorm", "options", "ideas" | Wide exploration |
| **Convergent** | "decide", "choose", "rank" | Structured criteria + recommendation |
| **Analytical** | "why", "root cause", "what's driving" | Depth, evidence, mechanism |
| **Executive** | "brief", "update", "status" | Summary, signal-to-noise |

---

## Routing Decision Tree

```
User input arrives
       │
       ├─── Contains /command → invoke directly
       │
       ├─── Current state question
       │    ├─── "what's open?" → /briefing
       │    ├─── "what did we decide?" → decisions-log.md
       │    └─── "what do I know about X?" → KNOWLEDGE-INDEX.md
       │
       ├─── New artifact
       │    ├─── Meeting transcript → /debrief
       │    ├─── Quick note, URL → /capture
       │    └─── Decision to log → /decide
       │
       ├─── Synthesis/analysis
       │    ├─── Single topic → /synthesize
       │    ├─── Week in review → /weekly
       │    └─── PM analysis → /pm-[domain]
       │
       └─── System maintenance
            └─── "how is the workspace?" → /observe
```

---

## Execution Modes

### Mode 1 — Direct Execution
User invokes a single skill explicitly. Run it.

### Mode 2 — Inferred Single Execution
Clear intent, one skill match. Suggest then confirm.
```
User: "Log the decision we made about pricing."
→ Suggest: "This looks like a /decide — want me to log it?"
→ On confirmation: execute
```

### Mode 3 — Composed Pipeline
Multiple skills in sequence. Surface the plan first.
```
User: "We finished discovery and need to write requirements."
→ "Two-step workflow: /pm-discovery synthesis → /pm-prd.  Start with discovery?"
→ Confirm → step 1 → surface output → confirm → step 2
```
**Never run step 2 automatically after step 1.** Each gate requires confirmation.

### Mode 4 — Decomposed Execution
Complex request with no clean skill match. Decompose explicitly before running.
```
User: "Prepare a QBR covering what we shipped, what worked, and what we're betting on."
→ Decompose: pull shipped work → /pm-retro → /pm-strategy → /pm-exec-brief
→ Surface: "5-step QBR prep. Run this sequence?"
```

---

## Sequencing Rules

**S-1 — Dependencies before execution.** Never start a step that depends on prior output until that output exists.

**S-2 — Gates are human checkpoints.** "Continue" or "looks good" is the gate signal. Not automatic.

**S-3 — Independent steps can be proposed together.** If two steps don't depend on each other, offer to run both.

**S-4 — Don't re-run what's already done.** Check existing outputs before re-executing. If `reviews/weekly/2026-21.md` exists, don't re-run `/weekly` unless asked.

**S-5 — Surface complexity before executing.** For complex and novel requests, always surface the plan and get alignment before starting.

---

## Core Workflow Maps

### Map 1 — Daily Operations

```
Session start
    ├─ Read MEMORY.md → load relevant project/priority files
    └─ /briefing → ephemeral terminal output

During session:
    ├─ New note/reference → /capture
    ├─ Meeting → /debrief (same day)
    └─ Decision made → /decide

Session end:
    └─ Update memory if new patterns emerged (2 min)
```

### Map 2 — Meeting Intelligence Pipeline

```
Meeting happens → notes to meeting-intelligence/raw/YYYY-MM-DD-topic.md
    │
    ▼
/debrief
    ├─ Writes: meeting-intelligence/processed/YYYY-MM-DD-topic.md
    ├─ Appends: execution/action-items.md
    ├─ Appends: decision-frameworks/decisions-log.md
    └─ Flags: knowledge candidates

    │ (for each candidate)
    ▼
/promote → knowledge/<domain>/concept-slug.md
```

### Map 3 — Weekly Review Cycle

```
Trigger: Monday or /weekly
    │
    ▼
/weekly reads:
    ├─ meeting-intelligence/processed/ (Mon-Sun files)
    ├─ execution/action-items.md
    ├─ decision-frameworks/decisions-log.md
    └─ memory/ (active projects + priorities)
    │
    ▼
Produces: reviews/weekly/YYYY-WW.md
    ├─ If synthesis needed → /synthesize → synthesis/weekly-insights/YYYY-WW.md
    └─ Always → update action-items.md + memory/
```

### Map 4 — Knowledge Compounding Loop

```
notes/raw/ → /promote
    ├─ Checks KNOWLEDGE-INDEX.md: concept exists? → extend | create
    ├─ Writes: knowledge/<domain>/<slug>.md
    ├─ Updates: knowledge/KNOWLEDGE-INDEX.md
    └─ Scans existing entries for [[connections]]
```

### Map 5 — Observability Loop

```
Every API call → telemetry/api-log.jsonl
Every workflow → telemetry/workflow-log.jsonl
Human ratings → observability/quality.jsonl (weekly)
    │
    ▼ /observe (weekly)
observability/dashboard.md
    └─ Flags: cost anomalies, quality drops, dead workflows, stale knowledge
```

---

## MCP Routing

### Pattern 1: Skill → MCP (produce then render)
Run the skill first to produce structured content. Then invoke MCP to render or transmit.

| Skill | MCP | Role |
|-------|-----|------|
| `/pm-wireframe` | Figma | Spec → rendered wireframe |
| `/pm-gtm` | Gamma | Brief → launch deck |
| `/pm-status` | Gmail | Update → email draft |
| `/pm-launch` | Vercel | Go/no-go → deploy to preview |
| `/pm-competitive` | Playwright | URL → screenshot → analysis |

### Pattern 2: MCP → Skill (gather then analyze)
MCP gathers raw material; skill processes it into intelligence.

| MCP | Skill | Example |
|-----|-------|---------|
| Playwright (screenshot competitor) | `/pm-teardown` | Analyze competitor product |
| Google Drive (read customer doc) | `/pm-discovery` | Synthesize customer feedback |

### Pattern 3: Pure MCP (no skill required)
Read-only: screenshot, calendar check, status queries. Always confirm before write/send/deploy.

---

## Flow Diagrams

### Session Start

```
New session begins → read MEMORY.md index
     │
     ├─ "start my day" / "what's on my plate" → /briefing immediately
     ├─ References specific project → read memory/project_<name>.md first
     ├─ References past decision → check decisions-log.md
     └─ New task, no prior context → read user_profile.md, proceed
```

### Ambiguous Intent

```
Signal analysis yields 2-3 candidates
     │
     ▼
Ask exactly ONE clarifying question:
"Is this [skill A description] or [skill B description]?"
     │
     ├─ Clear answer → route to correct skill
     └─ Still unclear → default to more general skill; state the choice
```

### Capability Gap

```
No skill matches intent
     │
     ├─ Variant (80%+ covered by existing skill)
     │    └─ Adapt invocation; state what you're doing
     │
     ├─ Extension (one step missing)
     │    └─ Execute with the extra step inline; offer to formalize
     │
     └─ Novel (genuinely new)
          └─ Execute the task inline (gap doesn't block work)
               After: "Want me to create a /[name] skill for this?"
```

### Decision Continuity

```
User asks about a topic or approach
     │
     ├─ Prior decision likely? → grep decisions-log.md
     │    ├─ Found → surface: "We decided [X] on [date]. Re-evaluate, or proceed?"
     │    └─ Not found → proceed with recommendation; offer to log
     └─ No decision expected → proceed
```

---

## Naming Conventions

| Type | Convention | Example |
|------|-----------|---------|
| Meeting files | `YYYY-MM-DD-topic-slug.md` | `2026-05-20-product-roadmap.md` |
| Weekly reviews | `YYYY-WW.md` | `2026-21.md` |
| Knowledge entries | `concept-slug.md` | `context-degradation.md` |
| Synthesis memos | `YYYY-MM-DD-topic.md` | `2026-05-20-ai-strategy.md` |
| Memory files | `type_slug.md` | `project_workspace-build.md` |

---

## Anti-Patterns

| Anti-Pattern | Problem | Fix |
|---|---|---|
| Auto-advancing past gate on ambiguous input | Removes human control | Require explicit gate signal |
| Running a pipeline without surfacing the plan | User surprised by what ran | Surface plan; confirm before step 1 |
| Re-executing skills when output exists | Wasted effort | Check output files before re-running |
| Routing by feel ("seems like a /weekly") | Wrong skill runs | Describe intent → name skill → invoke |
| Asking more than one clarifying question | Friction | One question maximum; default to general skill |
| Running MCP before skill produces its input | Low-quality artifacts | Skill first; MCP second |
| Dead action items | Items stale for >14 days | Weekly review forces disposition on every item |
