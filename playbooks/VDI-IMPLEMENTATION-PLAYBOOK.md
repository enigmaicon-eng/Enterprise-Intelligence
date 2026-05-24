# Enterprise Intelligence Workspace
# VDI Implementation Playbook

**Target environment:** Corporate VDI — VS Code + GitHub Copilot  
**Purpose:** A bounded cognitive execution environment for one operator  
**Not:** AI-Enterprise-OS · enterprise AI infrastructure · AGI runtime · multi-agent system

---

## What You Are Building

A structured, file-based workspace that runs inside VS Code + GitHub Copilot. Every session starts with context, every output feeds forward, every skill is a named, invokable prompt. The system compounds — knowledge connects to knowledge, decisions reference past decisions, execution traces reveal patterns.

**Three things:**
1. A prompt library — named skills covering PM work, strategy, execution, knowledge, and cognitive tools
2. A file-based operational memory — structured markdown encoding decisions, knowledge, traces, and state
3. A governed context system — behavioral rules that make Copilot behave consistently across sessions

**One operator. One session. Everything human-gated.**

---

## What This Is Not

- Not an autonomous agent pipeline
- Not enterprise AI infrastructure
- Not a multi-agent orchestration system
- Not a database-backed persistence layer
- Not a background process or scheduler
- Not a recursive self-directing system

---

## Prerequisites

| Requirement | Notes |
|-------------|-------|
| VS Code (1.99+) | Prompt files require 1.99+ |
| GitHub Copilot extension | Chat + Agent mode required |
| Git | For version control and sync |
| Corporate Git remote | GitHub Enterprise or approved remote |
| Read/write access to VDI filesystem | Standard user permissions sufficient |

**No npm, pip, Docker, or admin rights required.**

---

## Implementation Overview

| Phase | Name | Time | Output |
|-------|------|------|--------|
| 1 | Repository Foundation | 15 min | Folder structure + Git init |
| 2 | Copilot Configuration | 20 min | `copilot-instructions.md` (the brain) |
| 3 | Daily Ritual Skills | 30 min | 6 core prompt files |
| 4 | Core Skills | 45 min | 20 essential prompt files |
| 5 | PM Skills | 30 min | 15 PM prompt files |
| 6 | Memory System | 20 min | `memory/` structure + index |
| 7 | Knowledge System | 15 min | `knowledge/` structure + index |
| 8 | Runtime System | 15 min | `runtime/` state files |
| 9 | Execution & Trace Systems | 10 min | `execution/` + `traces/` |
| 10 | VS Code Wiring | 10 min | Workspace settings + keybindings |
| 11 | First Session Validation | 15 min | Verified operational |

**Total: ~3.5 hours from empty folder to operational workspace**

---

## Phase 1: Repository Foundation

### 1.1 Create the Repository

```bash
# In VS Code terminal (Ctrl+`)
mkdir Enterprise-Intelligence
cd Enterprise-Intelligence
git init
git remote add origin <your-corporate-git-remote-url>
```

### 1.2 Full Directory Structure

Create every folder now. Empty folders need a `.gitkeep` placeholder.

```bash
# Run this entire block in the terminal
mkdir -p .github/prompts
mkdir -p architecture/archive
mkdir -p memory
mkdir -p knowledge/strategy
mkdir -p knowledge/product
mkdir -p knowledge/technical
mkdir -p knowledge/leadership
mkdir -p knowledge/domain
mkdir -p strategy/monthly
mkdir -p execution
mkdir -p traces/executions
mkdir -p traces/journal
mkdir -p traces/patterns
mkdir -p traces/primitives
mkdir -p runtime/state
mkdir -p runtime/plans
mkdir -p runtime/snapshots
mkdir -p runtime/events
mkdir -p notes/raw
mkdir -p notes/structured
mkdir -p meeting-intelligence/raw
mkdir -p meeting-intelligence/processed
mkdir -p decision-frameworks
mkdir -p synthesis
mkdir -p reviews/weekly
mkdir -p playbooks
mkdir -p templates
mkdir -p prompts

# Placeholders for empty dirs
for d in traces/executions traces/journal traces/patterns traces/primitives \
          runtime/plans runtime/snapshots runtime/events \
          notes/raw notes/structured \
          meeting-intelligence/raw meeting-intelligence/processed \
          reviews/weekly synthesis; do
  touch "$d/.gitkeep"
done
```

**Final structure:**

```
Enterprise-Intelligence/
├── .github/
│   ├── copilot-instructions.md      ← Behavioral rules (loaded every session)
│   └── prompts/                     ← Skill library (invoked on demand)
│       ├── briefing.prompt.md
│       ├── plan.prompt.md
│       └── ... (all skills)
├── architecture/                    ← System reference docs
│   └── archive/
├── memory/                          ← Orientation facts across sessions
│   └── MEMORY.md                    ← Index (never write content here)
├── knowledge/                       ← Permanent knowledge by domain
│   ├── KNOWLEDGE-INDEX.md
│   ├── strategy/
│   ├── product/
│   ├── technical/
│   ├── leadership/
│   └── domain/
├── strategy/                        ← Active bets, OKRs, signals
│   └── monthly/
├── execution/                       ← Action items, initiatives, risks
├── traces/                          ← Execution history
│   ├── TRACE-INDEX.md
│   ├── executions/
│   ├── journal/
│   ├── patterns/
│   └── primitives/
├── runtime/                         ← Workflow state (JSON, atomic)
│   ├── state/
│   ├── plans/
│   ├── snapshots/
│   └── events/
├── notes/                           ← Raw + structured captures
│   ├── raw/
│   └── structured/
├── meeting-intelligence/
│   ├── raw/
│   └── processed/
├── decision-frameworks/
│   └── decisions-log.md
├── synthesis/
├── reviews/
│   └── weekly/
├── playbooks/
├── templates/
└── prompts/
```

### 1.3 .gitignore

Create `.gitignore`:

```
# Runtime state — ephemeral, machine-specific
runtime/state/
runtime/events/
runtime/snapshots/

# OS artifacts
.DS_Store
Thumbs.db
desktop.ini

# Editor artifacts
.vscode/settings.json
*.swp
*~

# Secrets
.env
*.env
*.key
*.pem
credentials.json
token.json
```

### 1.4 Initial Commit

```bash
git add .
git commit -m "init: workspace foundation structure"
git push -u origin main
```

---

## Phase 2: Copilot Configuration

### 2.1 copilot-instructions.md

This file is automatically loaded into every Copilot Chat conversation. It is the behavioral brain of the system.

Create `.github/copilot-instructions.md`:

```markdown
# Enterprise Intelligence Workspace

AI-native operational intelligence system for one operator.
Every artifact produced feeds forward. Context compounds.

## Identity

You are an operational intelligence analyst in a structured, file-based
knowledge workspace. Read files before responding to anything that concerns
workspace state. Write outputs to the correct directory per the routing table.

## Layer Contract

- This file: behavioral rules, routing, output standards only
- `memory/`: orientation facts — read MEMORY.md at session start
- `.github/prompts/`: skills — loaded only when invoked
- `knowledge/`, `strategy/`, `synthesis/`: reference depth, read on demand

## Skill Routing

| Intent | Prompt File |
|--------|------------|
| Today's briefing / priorities | `#briefing` |
| Set today's theme + top 3 commitments | `#plan` |
| Frame a deep work session | `#focus` |
| Prepare for a specific meeting | `#prep` |
| End-of-day closure + tomorrow seed | `#shutdown` |
| Run weekly review | `#weekly` |
| Inventory all open threads | `#open-loops` |
| Cognitive load check | `#cognitive-load` |
| Capture a note, thought, or reference | `#capture` |
| Process a meeting file | `#debrief` |
| Promote a note to permanent knowledge | `#promote` |
| Log a decision | `#decide` |
| Capture from book/article/course | `#learn` |
| Retrieve knowledge by keyword | `#recall` |
| Document a recurring pattern | `#pattern` |
| Open, update, close a strategic bet | `#bet` |
| Scan H1/H2/H3 horizons | `#horizon` |
| Build an execution plan | `#exec-plan` |
| Prioritize work | `#exec-prioritize` |
| Strategic checkpoint | `#exec-checkpoint` |
| Capture execution trace | `#trace-capture` |
| Retrieve past traces | `#trace-recall` |
| Stress-test a claim | `#think` |
| Cross-domain insight | `#insight` |
| Pre-decision analysis | `#pre-decide` |
| Map consequences of a choice | `#consequence-map` |
| Start a multi-step workflow | `#runtime-start` |
| Resume a paused workflow | `#runtime-resume` |
| Check workflow status | `#runtime-status` |
| PRD generation | `#pm-prd` |
| Discovery synthesis | `#pm-discovery` |
| Prioritization framework | `#pm-prioritize` |
| Root cause analysis | `#pm-rca` |
| Executive brief | `#pm-exec-brief` |
| OKR crafting | `#pm-okr` |
| Competitive analysis | `#pm-competitive` |
| Sprint planning | `#pm-sprint` |
| Retrospective | `#pm-retro` |
| Roadmap narrative | `#pm-roadmap` |
| Status update | `#pm-status` |
| Experiment design | `#pm-experiment` |
| User story | `#pm-story` |
| GTM brief | `#pm-gtm` |
| Launch readiness | `#pm-launch` |

## File Routing

- Raw captures → `notes/raw/`
- Structured notes → `notes/structured/`
- Meeting inputs → `meeting-intelligence/raw/`
- Processed meetings → `meeting-intelligence/processed/`
- Knowledge entries → `knowledge/<domain>/`
- Decisions → `decision-frameworks/decisions-log.md`
- Weekly reviews → `reviews/weekly/`
- Syntheses → `synthesis/`
- Execution traces → `traces/executions/`
- Trace journal → `traces/journal/`

## Output Standards

- Default to prose. Lists only for genuinely parallel items.
- Match length to complexity. A sentence suffices for simple questions.
- Begin with the answer. Do not restate the question.
- When evidence supports a recommendation, issue it.
- State conclusions directly.

## Memory Protocol

1. Read `memory/MEMORY.md` before any workflow touching workspace state.
2. Update memory files when new patterns, projects, or preferences emerge.
3. Never write content into `memory/MEMORY.md` — it is an index only.
4. Per-file target: <500 tokens.

## Behavioral Guardrails

- Read referenced files before responding about their content.
- If the premise of a request contains a flaw, name it before proceeding.
- Scope all work to what was requested.
- One workflow active at a time. Human gate before every step.
```

### 2.2 How Copilot Loads This

When you open Copilot Chat (`Ctrl+Alt+I`) in this workspace, the `copilot-instructions.md` is automatically included as system context. You do not need to reference it — it is always active.

---

## Phase 3: Daily Ritual Skills

Each file goes in `.github/prompts/`. The frontmatter `mode: 'agent'` allows Copilot to read and write files.

**Invocation:** In Copilot Chat, type `#briefing` (or the filename without `.prompt.md`) and press Enter.

---

### briefing.prompt.md

```markdown
---
mode: 'agent'
description: 'Morning operational briefing — priorities, risks, open loops'
---

You are running the daily briefing for the operator. This is the first
cognitive act of the day. Be direct and useful, not ceremonial.

Step 1: Read `memory/MEMORY.md` to orient on current projects and priorities.
Step 2: Read `execution/active-initiatives.md` if it exists.
Step 3: Read `decision-frameworks/decisions-log.md` — last 3 entries only.
Step 4: Check `runtime/state/active-workflows.json` for any paused workflows.

Produce a briefing with exactly these sections:

**TODAY** (1-2 sentences: what matters most today)

**ACTIVE WORK** (bullet list: initiatives in flight, each with status)

**OPEN DECISIONS** (any decisions flagged for review today)

**PAUSED WORKFLOWS** (any runtime workflows in PAUSED or GATE state)

**RISKS** (2-3 items that could derail the day, if any)

**SEED** (one question or thread worth keeping in mind today)

If a file doesn't exist, skip that section silently. Do not fabricate state.
```

---

### plan.prompt.md

```markdown
---
mode: 'agent'
description: 'Set today theme and top 3 commitments'
---

Help the operator set today's execution plan. This takes 5 minutes and
produces a binding commitment for the day.

Step 1: Read `memory/MEMORY.md` for active projects and priorities.
Step 2: Ask (if not already provided): "What is today's primary focus?"

Then produce:

**THEME** — one sentence: what today is for

**TOP 3 COMMITMENTS**
1. [Most important — outcome, not activity]
2. [Second priority]
3. [Third priority]

**NOT TODAY** — one sentence on what you are explicitly deferring

**ENERGY ALLOCATION** — rough split (e.g., "60% deep work, 40% comms")

Write the plan to `notes/structured/plan-YYYY-MM-DD.md` using today's date.
Confirm the path when done.
```

---

### focus.prompt.md

```markdown
---
mode: 'agent'
description: 'Frame a deep work session with constraints and intention'
---

The operator is entering a deep work session. Frame it clearly.

Ask (if not provided): "What is the deep work target for this session?"

Then produce:

**SESSION INTENT** — one sentence: what done looks like at the end

**SCOPE** — what is in scope, what is explicitly out of scope

**DECISION RIGHTS** — what the operator can decide alone vs. what needs input

**CONSTRAINTS** — time box, dependencies, known blockers

**FOCUS SIGNAL** — one concrete question to answer or artifact to produce

Do not write a file. Output inline only. Keep it under 200 words.
```

---

### prep.prompt.md

```markdown
---
mode: 'agent'
description: 'Prepare for a specific meeting or conversation'
---

The operator needs to prepare for a meeting. Gather context and produce a
preparation brief.

Ask (if not provided): "What meeting? With whom? What is the desired outcome?"

Step 1: Check `meeting-intelligence/processed/` for any prior meetings with
        the same attendees or topic.
Step 2: Check `decision-frameworks/decisions-log.md` for relevant past decisions.
Step 3: Check `strategy/` for relevant strategic context.

Produce:

**MEETING BRIEF**
- Purpose: [one sentence]
- Desired outcome: [what done looks like]
- Our position: [where we stand on the key topic]

**CONTEXT** (2-3 bullets: what they need to know going in)

**KEY QUESTIONS** (2-3 questions to ask or get answered)

**RISKS** (1-2 things that could derail this meeting)

**OPENING** (suggested 1-sentence opener)

Output inline. Do not write a file.
```

---

### shutdown.prompt.md

```markdown
---
mode: 'agent'
description: 'End-of-day closure — capture, close loops, seed tomorrow'
---

The operator is closing the day. Run the shutdown ritual.

Step 1: Read `notes/structured/plan-YYYY-MM-DD.md` for today's commitments
        (use today's actual date).
Step 2: Read `runtime/state/active-workflows.json` for any RUNNING workflows
        — move them to PAUSED status.

Produce:

**DONE** (what actually got completed from the plan)

**CARRIED** (what moves to tomorrow, and why)

**CAPTURED** (any new knowledge, decisions, or threads from today worth keeping)

**TOMORROW SEED** (one thing to start tomorrow with — a question, draft, or decision)

**COGNITIVE CLOSE** (one sentence: what you can let go of tonight)

Then ask: "Anything else to capture before closing?"

Write a brief journal entry to `traces/journal/YYYY-MM-DD.md`.
```

---

### weekly.prompt.md

```markdown
---
mode: 'agent'
description: 'Weekly review — what moved, what matters, what next'
---

Run the weekly review. This is a 30-minute structured reflection.

Step 1: Read `memory/MEMORY.md` for current projects and priorities.
Step 2: Read the last 5 daily journal entries in `traces/journal/`.
Step 3: Read `execution/active-initiatives.md`.
Step 4: Read `strategy/STRATEGY-OS.md` if it exists.

Produce a weekly review with these sections:

**WEEK SUMMARY** (2-3 sentences: what the week was actually about)

**COMMITMENTS: MET / MISSED / MOVED**
- Met: [list]
- Missed: [list + brief cause]
- Moved: [list + to when]

**MOMENTUM** (what is accelerating, what is stalling)

**SIGNALS** (any new strategic signals worth tracking)

**LEARNING** (one thing learned this week worth keeping)

**NEXT WEEK THEME** (one sentence)

**TOP 3 NEXT WEEK** (binding commitments)

Write output to `reviews/weekly/YYYY-WNN.md` using ISO week notation.
Confirm path when done.
```

---

## Phase 4: Core Skills

### capture.prompt.md

```markdown
---
mode: 'agent'
description: 'Capture a note, thought, reference, or observation'
---

Capture whatever the operator provides. Route it correctly.

The input may be: a raw thought, a URL, a quote, an observation, a decision
seed, a task, or a reference.

Step 1: Classify the input:
  - THOUGHT → `notes/raw/YYYY-MM-DD-<slug>.md`
  - REFERENCE → `notes/raw/YYYY-MM-DD-ref-<slug>.md`
  - DECISION SEED → `notes/raw/YYYY-MM-DD-decide-<slug>.md`
  - KNOWLEDGE → `notes/raw/YYYY-MM-DD-learn-<slug>.md`
  - TASK → append to `execution/active-initiatives.md`

Step 2: Write the capture with frontmatter:
```yaml
---
date: YYYY-MM-DD
type: [thought|reference|decision-seed|knowledge|task]
tags: []
status: raw
---
```

Step 3: Confirm path. If it looks like it should be promoted to permanent
knowledge, say so — but do not promote automatically.
```

---

### debrief.prompt.md

```markdown
---
mode: 'agent'
description: 'Process a raw meeting file into structured intelligence'
---

Process a meeting file into structured, retrievable intelligence.

The operator will provide the meeting file path or paste raw notes.

Produce:

**MEETING DEBRIEF**
- Date: [date]
- Attendees: [names/roles]
- Purpose: [one sentence]

**KEY DECISIONS** (bullet: decision + who owns it)

**ACTION ITEMS** (bullet: action + owner + due date)

**COMMITMENTS MADE** (what we committed to)

**SIGNALS** (any strategic signals worth tracking)

**FOLLOW-UP REQUIRED** (what needs to happen before next meeting)

**OPEN QUESTIONS** (unresolved threads)

Write output to `meeting-intelligence/processed/YYYY-MM-DD-<topic>.md`.
Append action items to `execution/active-initiatives.md`.
Confirm both paths when done.
```

---

### learn.prompt.md

```markdown
---
mode: 'agent'
description: 'Capture structured knowledge from a book, article, course, or repo'
---

Help the operator capture structured knowledge from a source.

Ask (if not provided): "What is the source? What is the core insight?"

Produce a knowledge entry with this format:

```yaml
---
title: [Concept or insight name]
source: [Book/article/course title + author]
domain: [strategy|product|technical|leadership|domain]
tags: []
confidence: [high|medium|low]
reviewed: YYYY-MM-DD
connections: []
---
```

**CORE INSIGHT** (2-3 sentences: the durable idea)

**WHY IT MATTERS** (one sentence: operational relevance)

**APPLICATION** (how to use this — concrete, not abstract)

**TENSIONS** (what this idea conflicts with or limits)

**CONNECTIONS** (what other knowledge entries this connects to)

Write to `knowledge/<domain>/YYYY-MM-DD-<slug>.md`.
Add an entry to `knowledge/KNOWLEDGE-INDEX.md`.
Confirm both paths.
```

---

### recall.prompt.md

```markdown
---
mode: 'agent'
description: 'Retrieve knowledge by keyword, topic, or concept'
---

Retrieve relevant knowledge for the operator's query.

Step 1: Read `knowledge/KNOWLEDGE-INDEX.md`.
Step 2: Identify entries matching the query by title, tags, or domain.
Step 3: Read the top 2-3 matching files.

Produce:

**RETRIEVED: [Query]**

For each relevant entry:
- **[Title]** (`knowledge/<domain>/filename.md`)
  - Core insight: [1-2 sentences]
  - Application: [how to use it]
  - Confidence: [high|medium|low] | Reviewed: [date]

**CONNECTIONS** (related entries worth reading)

**GAP** (if nothing found: "No entries for [query]. Use #learn to capture.")

Do not fabricate knowledge. Only surface what is in the knowledge files.
```

---

### decide.prompt.md

```markdown
---
mode: 'agent'
description: 'Log a decision with rationale, alternatives, and review date'
---

Log a decision into the decision record.

Ask (if not provided): "What is the decision? What were the alternatives?"

Produce a decision entry:

```markdown
## [Decision Title]
**Date:** YYYY-MM-DD
**Status:** DECIDED

**Decision:** [One sentence — what was decided]

**Context:** [Why this decision was needed]

**Alternatives considered:**
1. [Option A] — [why rejected]
2. [Option B] — [why rejected]

**Rationale:** [Why this choice]

**Assumptions:** [What must be true for this to be right]

**Review date:** [When to revisit — default 90 days]

**Owner:** [Who is accountable]
```

Append to `decision-frameworks/decisions-log.md`.
Confirm when done.
```

---

### think.prompt.md

```markdown
---
mode: 'agent'
description: 'Stress-test a claim, plan, or decision with constraint-based challenge'
---

The operator wants to stress-test a claim or plan. Apply rigorous challenge.

The operator will provide the claim or plan to test.

Apply these lenses in order:
1. **Falsification** — What single piece of evidence would prove this wrong?
2. **Steelmanning** — What is the strongest version of the opposing view?
3. **Assumption audit** — List every assumption this depends on. Mark each: CONFIRMED / UNCERTAIN / UNVERIFIED
4. **Scope creep check** — Is this solving the stated problem or a different one?
5. **Pre-mortem** — It's 6 months later and this failed. What happened?
6. **Decision quality** — Is this a reversible or irreversible decision? Does that change the approach?

Produce:
**VERDICT** — one sentence: how strong is this claim/plan?
**CRITICAL ASSUMPTION** — the one assumption that carries the most risk
**RECOMMENDED ACTION** — what to do before proceeding

Output inline. Do not write a file.
```

---

### pre-decide.prompt.md

```markdown
---
mode: 'agent'
description: 'Structured pre-decision analysis — options, biases, pre-mortem'
---

Run a structured pre-decision analysis before the operator commits.

The operator will provide the decision to be made.

Step 1: Read `decision-frameworks/decisions-log.md` for analogous past decisions.

Produce:

**DECISION FRAMING**
- Decision: [one sentence]
- Deadline: [when must this be decided]
- Reversibility: [reversible | partially reversible | irreversible]

**OPTIONS**
For each option: name, expected outcome, key risk, key assumption

**COGNITIVE BIAS CHECK**
Flag any present:
- Sunk cost: [yes/no + evidence]
- Anchoring: [yes/no + evidence]
- Confirmation bias: [yes/no + evidence]
- Status quo bias: [yes/no + evidence]

**PRE-MORTEM**
Assume the chosen option failed. In 3 bullets: why it failed.

**RECOMMENDATION**
One sentence. If insufficient information: name exactly what is missing.

**ANALOGOUS PAST DECISION** (if found in decisions-log)

Output inline. Do not write a file.
```

---

### insight.prompt.md

```markdown
---
mode: 'agent'
description: 'Extract cross-domain insights from current knowledge'
---

Surface non-obvious connections across knowledge domains.

Step 1: Read `knowledge/KNOWLEDGE-INDEX.md`.
Step 2: Read 3-5 entries from different domains.
Step 3: Look for structural analogies, contradictions, and compounding patterns.

Produce:

**CROSS-DOMAIN INSIGHT**

**Pattern:** [The structural similarity across domains]

**Domain A application:** [How it manifests in domain A]
**Domain B application:** [How it manifests in domain B]

**Compounding effect:** [What becomes possible when you hold both]

**Tension:** [Where they conflict or limit each other]

**Operational implication:** [What the operator should do differently because of this]

Output inline. Suggest `/learn` to capture if the insight is durable.
```

---

### trace-capture.prompt.md

```markdown
---
mode: 'agent'
description: 'Capture an execution trace after completing a workflow'
---

Capture an execution trace for future reference and pattern mining.

The operator will describe what was just completed.

Produce a trace entry:

```yaml
---
date: YYYY-MM-DD
workflow: [name]
duration: [estimated]
outcome: [success|partial|failed]
tags: []
---
```

**WHAT HAPPENED** (2-3 sentences: what was done and what was produced)

**WHAT WORKED** (specific techniques or approaches that helped)

**WHAT DIDN'T** (blockers, wrong turns, wasted effort)

**DECISION POINTS** (key choices made during execution)

**PATTERN** (if this reveals a recurring pattern, name it)

**NEXT TIME** (one sentence: what to do differently)

Write to `traces/executions/YYYY-MM-DD-<workflow-slug>.md`.
Append a one-line entry to `traces/TRACE-INDEX.md`.
Confirm both paths.
```

---

### exec-plan.prompt.md

```markdown
---
mode: 'agent'
description: 'Build a structured execution plan for a project or initiative'
---

Build an execution plan. This is an operational plan, not a project charter.

The operator will provide the initiative or goal.

Step 1: Read `execution/active-initiatives.md` to check for existing plans.
Step 2: Read `memory/MEMORY.md` for context on priorities and constraints.

Produce:

**EXECUTION PLAN: [Initiative Name]**
**Owner:** [operator]
**Start:** YYYY-MM-DD
**Target completion:** YYYY-MM-DD

**OBJECTIVE** (one sentence: what done looks like)

**STEPS** (numbered, sequenced, each with: action + output + dependency)

**CRITICAL PATH** (the 2-3 steps where delay kills everything)

**RISKS** (top 3: risk + mitigation)

**RESOURCE REQUIREMENTS** (time, people, tools, decisions needed)

**FIRST ACTION** (what to do in the next 24 hours)

Write to `execution/<initiative-slug>-plan.md`.
Append a summary line to `execution/active-initiatives.md`.
Confirm paths.
```

---

### exec-prioritize.prompt.md

```markdown
---
mode: 'agent'
description: 'Prioritize work using commitment, leverage, and reversibility'
---

Help the operator prioritize work across competing demands.

The operator will provide the list of items to prioritize, or you will read it
from `execution/active-initiatives.md`.

Score each item on three dimensions (1-3 each):
- **Commitment** — Is this committed to someone? (3=hard commitment, 1=self-initiated)
- **Leverage** — Does this unlock or accelerate other work? (3=high, 1=isolated)
- **Reversibility** — How hard is it to undo not doing this? (3=irreversible, 1=easy to recover)

Sort by total score descending.

Produce:

**PRIORITY STACK**
| Rank | Item | Commit | Leverage | Reversibility | Total | Action |
|------|------|--------|----------|---------------|-------|--------|

**DEFER LIST** (items scoring <5: explicit deferral with reason)

**NOT THIS WEEK** (items explicitly parked)

Output inline. Do not write a file.
```

---

## Phase 5: PM Skills

### pm-prd.prompt.md

```markdown
---
mode: 'agent'
description: 'Generate a Product Requirements Document from context'
---

Generate a PRD. This is a working document, not a ceremony.

The operator will provide: feature/product name, problem statement, and target users.

Step 1: Read `memory/MEMORY.md` for product context.
Step 2: Read `knowledge/product/` index for relevant product knowledge.

Produce a PRD with these sections:

**[Feature Name] — PRD**
**Author:** [operator]
**Date:** YYYY-MM-DD
**Status:** DRAFT

---

**PROBLEM**
What problem does this solve? For whom? How do we know it's real?

**SOLUTION**
What are we building? What are we explicitly NOT building?

**USER STORIES**
Format: As a [user], I want to [action] so that [outcome].
Include: happy path + 2-3 edge cases.

**REQUIREMENTS**
Functional: [numbered list]
Non-functional: [performance, reliability, privacy constraints]
Out of scope: [explicit exclusions]

**SUCCESS METRICS**
- Primary: [the metric that proves this worked]
- Secondary: [supporting signals]
- Counter-metric: [what we must not worsen]

**DEPENDENCIES**
- Technical: [APIs, systems, infrastructure]
- Cross-team: [who needs to be involved]
- External: [third-party requirements]

**OPEN QUESTIONS**
[Numbered list — must resolve before build]

**RISKS**
[Top 3 with mitigation]

---

Write to `notes/structured/prd-<feature-slug>-YYYY-MM-DD.md`.
Confirm path.
```

---

### pm-discovery.prompt.md

```markdown
---
mode: 'agent'
description: 'Synthesize discovery findings into themes and opportunities'
---

Synthesize discovery findings into structured product intelligence.

The operator will provide: raw discovery notes, interview transcripts, or a
meeting-intelligence file path.

Produce:

**DISCOVERY SYNTHESIS: [Topic]**
**Date:** YYYY-MM-DD
**Sources:** [list]

**TOP THEMES** (ranked by frequency and severity)
For each theme:
- Theme name
- Evidence: [2-3 quotes or observations]
- Frequency: [how many users/sources]
- Severity: [critical|important|nice-to-have]

**UNMET NEEDS** (gaps in current solutions)

**OPPORTUNITY AREAS** (where investment would have highest impact)

**ANTI-PATTERNS** (what users are doing as workarounds — high signal)

**CONFLICTING SIGNALS** (where evidence contradicts itself)

**RECOMMENDED NEXT STEP** (one action: build, test, research more)

Write to `synthesis/discovery-<topic>-YYYY-MM-DD.md`.
Confirm path.
```

---

### pm-prioritize.prompt.md

```markdown
---
mode: 'agent'
description: 'Prioritize product opportunities using impact, confidence, and effort'
---

Prioritize product opportunities. Use ICE scoring: Impact × Confidence / Effort.

The operator will provide the opportunity list, or you will read from context.

For each opportunity, score 1-10:
- **Impact:** What is the potential upside if this works?
- **Confidence:** How sure are we this will work as expected?
- **Effort:** How much work is this? (10 = minimal effort, 1 = massive effort)

ICE Score = (Impact × Confidence) / Effort

Produce:

**PRIORITIZED OPPORTUNITY STACK**
| Rank | Opportunity | Impact | Confidence | Effort | ICE | Recommendation |
|------|-------------|--------|------------|--------|-----|----------------|

**TOP PICK** (one sentence: why this is #1)

**SKIP LIST** (bottom items with reason — be explicit)

**ASSUMPTIONS** (what must be true for this ranking to hold)

Output inline.
```

---

### pm-rca.prompt.md

```markdown
---
mode: 'agent'
description: 'Root cause analysis for a product incident or metric drop'
---

Run a structured root cause analysis.

The operator will describe the incident or anomaly.

Apply 5-Why methodology + timeline reconstruction:

**INCIDENT SUMMARY**
- What happened: [observable symptom]
- When: [timestamp / detection time]
- Impact: [users affected, severity, business impact]
- Current status: [resolved | active | mitigated]

**TIMELINE**
[Chronological reconstruction of events]

**5-WHY ANALYSIS**
Why 1: [immediate cause]
Why 2: [cause of cause 1]
Why 3: [cause of cause 2]
Why 4: [cause of cause 3]
Why 5: [root cause]

**ROOT CAUSE** (one sentence)

**CONTRIBUTING FACTORS** (what made this worse or harder to detect)

**CORRECTIVE ACTIONS**
| Action | Owner | Due | Type [fix/detect/prevent] |

**PREVENTIVE MEASURES** (systemic changes to prevent recurrence)

**OPEN QUESTIONS** (what we still don't know)

Write to `notes/structured/rca-<incident-slug>-YYYY-MM-DD.md`.
```

---

### pm-okr.prompt.md

```markdown
---
mode: 'agent'
description: 'Craft well-formed OKRs for a team or initiative'
---

Craft OKRs. Objective + 2-3 Key Results per objective.

Rules for a good Objective: inspiring, qualitative, time-bound, unambiguous.
Rules for a good Key Result: measurable, specific, outcome-not-output,
lagging indicator preferred.

The operator will provide the strategic context or goal area.

Step 1: Read `strategy/STRATEGY-OS.md` if it exists for alignment.

Produce:

**OKR SET: [Quarter/Period]**

**Objective 1:** [Inspiring statement]
- KR 1.1: [Metric] from [baseline] to [target] by [date]
- KR 1.2: [Metric] from [baseline] to [target] by [date]
- KR 1.3: [Metric] from [baseline] to [target] by [date]

**Health check for each KR:**
- [ ] Measurable (not "improve X" but "X goes from A to B")
- [ ] Outcome, not output (not "launch feature" but "X% of users do Y")
- [ ] Ambitious but achievable (50-70% confidence of hitting)
- [ ] Does not incentivize gaming

**ANTI-OBJECTIVES** (what success explicitly does not mean)

Output inline.
```

---

### pm-status.prompt.md

```markdown
---
mode: 'agent'
description: 'Generate a stakeholder status update for a product or initiative'
---

Generate a status update. Stakeholders need signal, not noise.

The operator will provide the initiative and audience.

Step 1: Read `execution/active-initiatives.md` for current status.
Step 2: Read recent traces in `traces/executions/` for the initiative.

Produce:

**STATUS UPDATE: [Initiative Name]**
**Date:** YYYY-MM-DD
**Audience:** [Stakeholder group]
**Status:** 🟢 On Track | 🟡 At Risk | 🔴 Off Track

**SUMMARY** (2-3 sentences: what's happening, what's changed)

**PROGRESS**
- Done since last update: [bullet list]
- In progress now: [bullet list]
- Next: [bullet list]

**RISKS / BLOCKERS**
[Only items that require stakeholder awareness or action]

**DECISIONS NEEDED** (explicit ask, if any)

**ETA** (unchanged / updated to [date] / TBD because [reason])

Output inline. Keep it under 250 words.
```

---

### pm-retro.prompt.md

```markdown
---
mode: 'agent'
description: 'Run a structured product or sprint retrospective'
---

Run a retrospective. The goal is learning, not catharsis.

The operator will provide the sprint/cycle scope.

Step 1: Read relevant traces from `traces/executions/` for the period.

Produce:

**RETROSPECTIVE: [Sprint/Cycle Name]**
**Date:** YYYY-MM-DD
**Period covered:** [dates]

**WENT WELL** (specific, concrete — not "good communication")

**DIDN'T GO WELL** (specific, honest — not vague complaints)

**ROOT CAUSE** (for each item in "didn't go well": why, not just what)

**EXPERIMENTS FOR NEXT CYCLE**
For each: hypothesis + how we'll know if it worked

**COMMITMENTS** (1-3 binding changes — not aspirations)

**CARRIED FORWARD** (unresolved items from last retro, if any)

Write to `notes/structured/retro-<sprint-slug>-YYYY-MM-DD.md`.
```

---

### pm-competitive.prompt.md

```markdown
---
mode: 'agent'
description: 'Competitive analysis — positioning, gaps, and strategic implications'
---

Run a competitive analysis for a product area or competitor.

The operator will name the competitor(s) or market space.

Step 1: Read `knowledge/strategy/` for any existing competitive intelligence.
Step 2: Read `strategy/STRATEGY-OS.md` for bet-level context.

Produce:

**COMPETITIVE ANALYSIS: [Space/Competitor]**
**Date:** YYYY-MM-DD

**COMPETITOR PROFILES**
For each competitor:
- Positioning: [how they describe themselves]
- Core strengths: [3 bullets]
- Known weaknesses: [3 bullets]
- Recent moves: [notable changes, launches, pivots]
- Target customer: [who they optimize for]

**COMPETITIVE GAPS** (what none of them do well — opportunity space)

**OUR DIFFERENTIATION** (where we are distinctly better or different)

**THREAT ASSESSMENT** (which competitor is most dangerous and why)

**STRATEGIC IMPLICATION** (one action or bet adjustment this analysis suggests)

Write to `knowledge/strategy/competitive-<space>-YYYY-MM-DD.md`.
Add entry to `knowledge/KNOWLEDGE-INDEX.md`.
```

---

### pm-exec-brief.prompt.md

```markdown
---
mode: 'agent'
description: 'Executive brief for leadership alignment or decision'
---

Write an executive brief. Leadership needs the decision, not the journey.

The operator will provide the topic and the ask.

Produce a brief in this structure (target: one page / 400 words max):

**[Topic] — Executive Brief**
**Date:** YYYY-MM-DD
**Author:** [operator]
**Ask:** [One sentence — what you need from leadership]

---

**SITUATION** (2-3 sentences: what's true right now)

**COMPLICATION** (1-2 sentences: why the status quo is insufficient)

**RECOMMENDATION** (one sentence — the specific ask, clearly stated)

**OPTIONS CONSIDERED**
| Option | Upside | Downside | Recommended? |
|--------|--------|----------|--------------|

**RISKS OF INACTION** (what happens if we do nothing)

**WHAT WE NEED**
- Decision: [yes/no/approve/fund]
- By: [date]
- Resources: [headcount/budget/time]

**APPENDIX** (supporting data, if any — reference only, not inline)

Write to `notes/structured/exec-brief-<topic>-YYYY-MM-DD.md`.
```

---

### pm-sprint.prompt.md

```markdown
---
mode: 'agent'
description: 'Sprint planning — goal, scope, and capacity allocation'
---

Run sprint planning. The output is a committed, realistic sprint scope.

The operator will provide the sprint goal or context.

Step 1: Read `execution/active-initiatives.md` for backlog context.
Step 2: Ask (if not provided): "What is the sprint capacity (story points or days)?"

Produce:

**SPRINT PLAN: Sprint [N]**
**Duration:** [dates]
**Capacity:** [total]
**Goal:** [one sentence — what done looks like]

**COMMITTED SCOPE**
| Item | Type | Estimate | Owner | Dependency |
|------|------|----------|-------|------------|

**TOTAL:** [X of Y capacity consumed]

**EXPLICITLY OUT OF SCOPE** (what we are not doing this sprint)

**RISKS** (what could prevent hitting the goal)

**DEFINITION OF DONE** (how we'll know the sprint goal is met)

**FIRST ACTION** (what starts in the next 24 hours)

Output inline.
```

---

## Phase 6: Runtime Skills

The runtime system manages multi-step workflows across sessions.

### runtime-start.prompt.md

```markdown
---
mode: 'agent'
description: 'Start a multi-step workflow with a human gate before each step'
---

Start a bounded multi-step workflow. One operator. One workflow active at a time.
Human gate before every step — no auto-advancement.

Step 1: Read `runtime/state/active-workflows.json`.
  - If any workflow is in RUNNING or GATE state: surface it. Do not start a new one.
  - If any workflow is in PAUSED state: ask "Resume [name]?" before starting new work.

Step 2: The operator will describe the workflow goal.

Step 3: Decompose into steps (max 7). For each step:
  - Name
  - Skill to invoke
  - Declared output path
  - Dependencies on prior steps

Step 4: Surface the plan:
```
Proposed workflow: [name]
Steps:
  1. [step name] → output: [path]
  2. [step name] → output: [path]
  ...
Start? (yes / modify / cancel)
```

Step 5: On approval, write `runtime/state/active-workflows.json`:
```json
{
  "schema_version": "1.0",
  "last_updated": "YYYY-MM-DDTHH:MM:SSZ",
  "workflows": [{
    "id": "wf_YYYYMMDD_001",
    "name": "[workflow name]",
    "status": "RUNNING",
    "current_step": 1,
    "total_steps": N,
    "gate_pending": false,
    "last_snapshot": null
  }]
}
```

Step 6: Execute step 1. Then stop and surface:
```
Step 1 complete: [name]
Output: [path]
Key result: [1-2 sentences]

Next: Step 2 — [name]
Continue? (yes / pause / stop)
```

Wait for explicit approval before step 2. Never auto-advance.
```

---

### runtime-resume.prompt.md

```markdown
---
mode: 'agent'
description: 'Resume a paused workflow from the last completed step'
---

Resume a paused workflow. Read state, re-orient the operator, gate before
the next step.

Step 1: Read `runtime/state/active-workflows.json`.

If no active workflows: "No active workflows. Use #runtime-start to begin one."

If PAUSED workflow found:
```
Workflow: [name]
Status: PAUSED at step [N] of [total]
Completed: [list of completed steps]
Next: Step [N+1] — [name]

Resume? (yes / abandon)
```

On "yes": Update status to RUNNING. Execute next step. Gate afterward.

On "abandon": Update status to ABANDONED. Write history entry.

Do not re-run completed steps. Do not skip gate after the resumed step.
```

---

### runtime-status.prompt.md

```markdown
---
mode: 'agent'
description: 'Check current workflow state'
---

Report current workflow state.

Read `runtime/state/active-workflows.json`.

If empty: "No active workflows."

For each workflow, report:
- Name
- Status: [RUNNING|PAUSED|GATE|FAILED]
- Progress: Step [N] of [total]
- Last action: [timestamp if available]
- Gate pending: [yes/no — what is it waiting for]

If status is FAILED: surface recovery options (RETRY / SKIP / ABANDON).

Output inline. No file writes.
```

---

### runtime-recover.prompt.md

```markdown
---
mode: 'agent'
description: 'Recover a failed or interrupted workflow'
---

Recover a failed or interrupted workflow.

Step 1: Read `runtime/state/active-workflows.json` for FAILED or interrupted workflows.
Step 2: Read the last snapshot in `runtime/snapshots/` for the workflow.

Surface recovery options:
```
Workflow: [name]
Failed at: Step [N] — [name]
Failure reason: [if known]

Recovery options:
  RETRY  — Re-run step [N] with the same inputs (attempt [X] of 3)
  SKIP   — Mark step [N] skipped; proceed to step [N+1] if no dependency
  REWIND — Restore from step [N-1] and re-run from there
  ABANDON — Mark workflow ABANDONED; preserve all artifacts

Choose: (retry / skip / rewind / abandon)
```

On selection: Update `active-workflows.json` and write a recovery snapshot.
After 3 RETRY failures: SKIP or ABANDON required. No more retries.
```

---

## Phase 7: Observability Skills

### ops-dashboard.prompt.md

```markdown
---
mode: 'agent'
description: 'Integrated operational dashboard — workspace health at a glance'
---

Generate the operational dashboard. This is the workspace health check.

Read these files in order:
1. `memory/MEMORY.md` — current projects and priorities
2. `execution/active-initiatives.md` — work in flight
3. `runtime/state/active-workflows.json` — runtime state
4. `traces/TRACE-INDEX.md` — recent execution history (last 5 entries)
5. `decision-frameworks/decisions-log.md` — decisions needing review

Produce:

**OPERATIONAL DASHBOARD** — YYYY-MM-DD

**WORKSPACE STATE**
- Active initiatives: [N]
- Runtime workflows: [status summary]
- Decisions pending review: [N]
- Knowledge entries: [rough count from KNOWLEDGE-INDEX.md]

**ACTIVE WORK**
[bullet: each initiative + status + next action]

**EXECUTION VELOCITY** (from last 5 traces: improving / steady / declining)

**OPEN LOOPS** (unresolved threads across all systems)

**DECISIONS DUE** (any with review date ≤ today + 7 days)

**SYSTEM HEALTH**
- Memory files: [count vs 30 ceiling]
- Knowledge entries: [count]
- Traces: [last trace date]

Output inline. Flag anything Critical.
```

---

## Phase 8: Memory System

### 8.1 Initialize memory/MEMORY.md

Create `memory/MEMORY.md`:

```markdown
# Memory Index

<!-- Index only. Never write content here. Each entry → its own file. -->
<!-- Format: - [Title](filename.md) — one-line hook -->
<!-- Ceiling: 200 lines. If exceeded, consolidate files. -->
```

### 8.2 Initial Memory Files

Create `memory/user-profile.md`:

```markdown
---
name: user-profile
description: Operator role, context, domain expertise, working style
metadata:
  type: user
---

**Role:** [Your role and team]
**Domain:** [Primary domain expertise]
**Working style:** [How you prefer to work]
**Current focus:** [Primary initiative or priority right now]
**VDI context:** Corporate VDI — VS Code + GitHub Copilot. No MCP tools available.
```

Create `memory/active-projects.md`:

```markdown
---
name: active-projects
description: Current projects, initiatives, and priorities in flight
metadata:
  type: project
---

**As of:** YYYY-MM-DD

[List active projects here. Update when priorities shift.]
```

Create `memory/workspace-setup.md`:

```markdown
---
name: workspace-setup
description: Workspace configuration, constraints, and operational conventions
metadata:
  type: project
---

**Workspace:** Enterprise Intelligence Workspace (VDI instance)
**Environment:** VS Code + GitHub Copilot
**Remote:** [your corporate git remote]
**Skills location:** `.github/prompts/`
**Instructions:** `.github/copilot-instructions.md`

**Constraints:**
- No MCP tools (VDI network restrictions)
- No Python scripts execution (VDI permissions)
- No external API calls
- All state in local files only

**Skill ceiling:** 60 (lean vs 120 for Claude Code — fewer prompts needed)
**Memory file ceiling:** 20 files
**Architecture doc ceiling:** 10 files
```

Add entries to `memory/MEMORY.md`:

```markdown
# Memory Index

- [User Profile](user-profile.md) — Operator role, domain expertise, working style
- [Active Projects](active-projects.md) — Current initiatives and priorities in flight
- [Workspace Setup](workspace-setup.md) — VDI configuration, constraints, conventions
```

### 8.3 Memory Protocol

| Rule | Detail |
|------|--------|
| Read MEMORY.md first | Before any workflow touching workspace state |
| One file per memory type | Don't put everything in one file |
| File ceiling: 20 files | If exceeded, consolidate similar files |
| Line ceiling: 200 in MEMORY.md | Trim stale entries |
| Update on change | When projects complete or priorities shift, update the file |
| Never duplicate | MEMORY.md is index only; content lives in the per-file |

---

## Phase 9: Knowledge System

### 9.1 Initialize KNOWLEDGE-INDEX.md

Create `knowledge/KNOWLEDGE-INDEX.md`:

```markdown
# Knowledge Index

| Title | Domain | File | Tags | Reviewed |
|-------|--------|------|------|---------|
| [Add entries as knowledge is captured] | | | | |
```

### 9.2 Knowledge Entry Format

Every file in `knowledge/<domain>/` uses this structure:

```markdown
---
title: [Concept name]
source: [Book/article/course + author]
domain: [strategy|product|technical|leadership|domain]
tags: [comma, separated]
confidence: [high|medium|low]
reviewed: YYYY-MM-DD
connections: [other entry titles]
---

## Core Insight
[2-3 sentences: the durable idea]

## Why It Matters
[Operational relevance — one sentence]

## Application
[Concrete: how to use this]

## Tensions
[What this conflicts with or where it breaks down]

## Connections
[Links to related entries]
```

### 9.3 Domain Directories

| Directory | What goes here |
|-----------|---------------|
| `knowledge/strategy/` | Strategic frameworks, competitive intelligence, bets |
| `knowledge/product/` | Product thinking, discovery patterns, PM frameworks |
| `knowledge/technical/` | Technical concepts relevant to the product/domain |
| `knowledge/leadership/` | Leadership, influence, communication, org navigation |
| `knowledge/domain/` | Industry-specific knowledge (your sector) |

---

## Phase 10: Runtime State Files

### Initialize active-workflows.json

Create `runtime/state/active-workflows.json`:

```json
{
  "schema_version": "1.0",
  "last_updated": "2026-01-01T00:00:00Z",
  "workflows": []
}
```

### Initialize workflow-history.json

Create `runtime/state/workflow-history.json`:

```json
{
  "schema_version": "1.0",
  "entries": []
}
```

### Initialize TRACE-INDEX.md

Create `traces/TRACE-INDEX.md`:

```markdown
# Trace Index

| Date | Workflow | Outcome | File |
|------|----------|---------|------|
| [Entries added by #trace-capture] | | | |
```

### Initialize decisions-log.md

Create `decision-frameworks/decisions-log.md`:

```markdown
# Decisions Log

Append-only record. Never delete entries. Mark superseded decisions as SUPERSEDED.

---

[First entry added by #decide]
```

### Initialize active-initiatives.md

Create `execution/active-initiatives.md`:

```markdown
# Active Initiatives

| Initiative | Status | Owner | Next Action | Updated |
|------------|--------|-------|------------|---------|
| [Added by #exec-plan or #debrief] | | | | |
```

---

## Phase 11: VS Code Configuration

### 11.1 Workspace Settings

Create `.vscode/workspace.code-workspace` (excluded from git):

```json
{
  "folders": [{ "path": "." }],
  "settings": {
    "editor.wordWrap": "on",
    "editor.lineNumbers": "on",
    "files.defaultLanguage": "markdown",
    "markdown.preview.breaks": true,
    "github.copilot.chat.localeOverride": "en",
    "github.copilot.enable": { "*": true, "markdown": true },
    "github.copilot.chat.scopeSelection": true
  }
}
```

### 11.2 How to Invoke Skills

**Method 1 — Prompt file reference (recommended):**
1. Open Copilot Chat (`Ctrl+Alt+I`)
2. Type `#briefing` and press `Tab` to attach the prompt file
3. Press `Enter`

**Method 2 — Agent mode with prompt:**
1. Open Copilot Chat
2. Switch to Agent mode (dropdown in chat input)
3. Type the intent — Copilot uses `copilot-instructions.md` to route

**Method 3 — Inline in editor:**
1. Select text in any file
2. `Ctrl+I` to open inline chat
3. Reference a prompt: `Run #capture on this selection`

### 11.3 Recommended Extensions

| Extension | Purpose | Required? |
|-----------|---------|-----------|
| GitHub Copilot | Core AI assistant | Yes |
| GitHub Copilot Chat | Chat interface + agent mode | Yes |
| Markdown All in One | Better markdown editing | Recommended |
| GitLens | Git history visibility | Recommended |
| Foam (optional) | Wiki-style `[[links]]` in markdown | Optional |

### 11.4 Git Workflow

```bash
# Daily sync (morning)
git pull origin main

# Capture work throughout day (no ceremony needed)
git add -A
git commit -m "session: YYYY-MM-DD — [one-line summary]"

# Push at end of day
git push origin main

# Never commit:
# - runtime/state/ (ephemeral)
# - runtime/events/ (ephemeral)
# - *.env, *.key (secrets)
```

---

## Phase 12: First Session Validation

### Validation Checklist

Run through this list before declaring the workspace operational:

```
[ ] .github/copilot-instructions.md exists and loads in Copilot Chat
[ ] .github/prompts/briefing.prompt.md invokable via #briefing
[ ] .github/prompts/plan.prompt.md invokable via #plan
[ ] memory/MEMORY.md exists with at least 1 entry
[ ] knowledge/KNOWLEDGE-INDEX.md exists
[ ] execution/active-initiatives.md exists
[ ] decision-frameworks/decisions-log.md exists
[ ] runtime/state/active-workflows.json exists (empty workflows array)
[ ] traces/TRACE-INDEX.md exists
[ ] .gitignore excludes runtime/state/ and secrets
[ ] git remote configured and first push successful
```

### First Session Sequence

```
1. Open VS Code in workspace root
2. Open Copilot Chat (Ctrl+Alt+I)
3. Run: #briefing           ← First operational act
4. Run: #plan               ← Set the day's commitments
5. Do the work
6. At end of day: #shutdown ← Close loops, seed tomorrow
7. git add -A && git commit -m "session: [date]" && git push
```

---

## Operational Conventions

### Daily Rhythm

| Time | Action | Skill |
|------|--------|-------|
| Day start | Morning briefing | `#briefing` |
| Day start | Set commitments | `#plan` |
| Before deep work | Frame the session | `#focus` |
| Before meetings | Prepare | `#prep` |
| After meetings | Process notes | `#debrief` |
| Day end | Close loops | `#shutdown` |

### Weekly Rhythm

| Day | Action |
|-----|--------|
| Monday | Run `#briefing` + `#plan` with weekly context |
| Friday | Run `#weekly` for full weekly review |
| Monthly | Run `#exec-checkpoint` on all active initiatives |
| Quarterly | Manual skill audit — retire any unused prompts |

### Capture Convention

**Capture immediately, promote deliberately.**
- Raw thoughts → `notes/raw/` via `#capture` (takes 30 seconds)
- Promote to knowledge → `#learn` (takes 10 minutes, only when truly durable)
- Never skip capture because promotion feels heavy — raw is fine

### Knowledge Convention

- Every entry needs a `reviewed:` date
- Entries older than 90 days without review: treat as potentially stale
- Review means: re-read, update if needed, update the date
- Connections are high-value — always fill the `connections:` field

### Decision Convention

- Log every non-trivial decision via `#decide`
- Include a `review date` — default 90 days
- Never delete decision log entries — mark as SUPERSEDED if replaced
- Before big decisions: run `#pre-decide` first

### Trace Convention

- After every significant workflow (≥30 min): run `#trace-capture`
- Traces compound — they are the raw material for `#insight` and pattern recognition
- Don't skip capture because the work was messy — messy traces are the most valuable

---

## Simplification Rules

**These are hard constraints. No exceptions.**

| Rule | Constraint |
|------|-----------|
| SR-1 | Skills ceiling: 60 prompt files. Adding the 61st requires retiring one. |
| SR-2 | Memory ceiling: 20 files in `memory/`. Consolidate before adding. |
| SR-3 | Architecture docs ceiling: 10 files in `architecture/`. Archive before adding. |
| SR-4 | No skill without a routing entry in `copilot-instructions.md`. |
| SR-5 | No duplicate skills. If two prompts have >70% overlap, merge them. |
| SR-6 | No skill for a workflow completed <3 times. Prompts earn existence. |
| SR-7 | Quarterly: delete every skill not invoked in the prior 90 days. |
| SR-8 | One file per concept. No parallel files for the same topic. |
| SR-9 | No architecture doc longer than 300 lines. Split if exceeded. |
| SR-10 | copilot-instructions.md stays under 2,000 tokens. Trim if exceeded. |

---

## Anti-Complexity Rules

**What this system must never become.**

| Rule | Prohibition |
|------|-------------|
| AC-1 | No autonomous multi-agent pipelines. One operator, one session. |
| AC-2 | No background processes, schedulers, or event loops. |
| AC-3 | No database. All state is human-readable markdown or JSON files. |
| AC-4 | No prompt that takes longer than 5 minutes to execute. Split it. |
| AC-5 | No skill that requires another skill's output as structured input. |
| AC-6 | No meta-skills that manage other skills. Skills are flat. |
| AC-7 | No skill that writes to more than 2 files per invocation. |
| AC-8 | No workflow with more than 7 steps. Break into sub-initiatives. |
| AC-9 | No memory file that cross-references more than 3 other files. |
| AC-10 | No architecture doc that describes behavior not yet implemented. |

---

## Bounded Autonomy Constraints

**Copilot may not act without explicit operator approval on these.**

| Constraint | Rule |
|-----------|------|
| BAC-1 | Human gate before every workflow step transition. No auto-advance on "OK". |
| BAC-2 | One "continue" approves exactly one step — not the pipeline. |
| BAC-3 | Copilot does not update `memory/` autonomously. Operator-controlled. |
| BAC-4 | Copilot does not delete files. Operator deletes explicitly. |
| BAC-5 | Copilot does not push to git. Operator runs `git push` explicitly. |
| BAC-6 | Copilot does not send emails, messages, or external communications. |
| BAC-7 | Three retry maximum on any failed step. After three: escalate, don't invent. |
| BAC-8 | Copilot does not start a second workflow when one is RUNNING or GATE. |
| BAC-9 | Session end → RUNNING workflows move to PAUSED. Never abandoned silently. |
| BAC-10 | Copilot surfaces uncertainty explicitly. "I don't know" is correct output. |

---

## Long-Term Maintenance Guidance

### Monthly (30 minutes)

- Run `#ops-dashboard` — verify no system drift
- Check `decision-frameworks/decisions-log.md` for entries past their review date
- Check `execution/active-initiatives.md` — close completed, re-priority stalled
- Git: verify remote is current (`git status`, `git push`)

### Quarterly (2 hours)

**Skill audit:**
- List all files in `.github/prompts/`
- Check `traces/TRACE-INDEX.md` — which skills appear in traces?
- Retire any skill not invoked in 90 days (move to `.github/prompts/archive/`)
- Verify every retained skill has an entry in `copilot-instructions.md`

**Memory audit:**
- Count files in `memory/` — must be ≤20
- Read each file — is the content still accurate?
- Update stale entries or delete if superseded

**Knowledge audit:**
- Check `knowledge/KNOWLEDGE-INDEX.md` for entries with `reviewed:` > 90 days old
- Re-read those entries. Update or archive.

**Architecture audit:**
- Count files in `architecture/` — must be ≤10
- Archive any doc describing a system no longer in use

### Ceiling Violations — How to Fix

| Violation | Fix |
|-----------|-----|
| Skills > 60 | Run trace analysis: retire lowest-usage skills first |
| Memory > 20 files | Consolidate: merge similar-topic files into one |
| Arch docs > 10 | Archive: move phase-completion docs to `architecture/archive/` |
| copilot-instructions.md > 2000 tokens | Trim routing table to top-30 most-used skills |

### Signs of Drift — Act Immediately

- You have prompts you can't remember the purpose of
- You're capturing things but never recalling them
- Runtime workflows are PAUSED and haven't been resumed in >7 days
- `copilot-instructions.md` has skills with no prompt file behind them
- Knowledge entries have no connections (isolated islands)

### What Not To Build

As the workspace matures, resist these:

| Temptation | Why to resist |
|-----------|--------------|
| "I should add a prompt for every meeting type" | Generic prompts beat fragmented ones. Use `#prep`. |
| "I should log every micro-decision" | Only non-trivial decisions. Log overhead kills the habit. |
| "I should build a knowledge graph with backlinks" | `[[links]]` in markdown plus KNOWLEDGE-INDEX is sufficient. |
| "I should automate the daily ritual" | The ritual's value is the daily intention-setting, not the output. |
| "I should connect this to my calendar/email" | VDI restrictions aside: manual pull beats automated push for cognition. |
| "I should add more observability metrics" | `#ops-dashboard` is sufficient. Don't instrument what you won't act on. |

---

## Architecture Reference

### Why File-Based (Not Database)

Every piece of state is human-readable markdown or JSON. You can:
- Read any state without tools
- Edit state directly in VS Code
- Version-control everything with Git
- Restore from any prior commit
- Understand the system by reading its files

A database adds operational complexity with no cognitive benefit for one operator.

### Why Prompt Files (Not RAG or Embeddings)

Prompt files are explicit, auditable, and version-controlled. You know exactly what Copilot will do when you invoke a skill. RAG systems introduce retrieval uncertainty and require infrastructure. For one operator's personal workspace, explicit prompts are more reliable and simpler.

### Why Human Gates (Not Autonomous Pipelines)

This system works because you remain in the loop. Copilot is a cognitive amplifier, not a decision-maker. The gates are not bureaucracy — they are the mechanism that makes this a second brain rather than an unpredictable automation.

### Relationship to the Claude Code Version

This playbook adapts the Enterprise Intelligence Workspace (built in Claude Code) for VS Code + Copilot. Structural differences:

| Aspect | Claude Code Version | VS Code + Copilot Version |
|--------|--------------------|-----------------------------|
| Skill invocation | `/briefing` slash commands | `#briefing` prompt file references |
| Session instructions | `CLAUDE.md` | `.github/copilot-instructions.md` |
| MCP tools | Figma, Gmail, Calendar, Vercel | Not available (VDI) |
| Python scripts | Knowledge indexing scripts | Manual index maintenance |
| Skill ceiling | 120 | 60 (leaner; prompts need less scaffolding) |
| Memory ceiling | 30 files | 20 files |

The memory architecture, knowledge system, runtime system, decision framework, trace system, and operational conventions are **identical**.

---

## Quick Reference Card

```
MORNING
  1. #briefing      ← Orient on state
  2. #plan          ← Commit to the day

DURING DAY
  3. #focus         ← Before deep work
  4. #prep          ← Before meetings
  5. #capture       ← Any fleeting thought
  6. #debrief       ← After meetings

EVENING
  7. #shutdown      ← Close loops
  8. git push       ← Persist the day

WEEKLY
  9. #weekly        ← Friday review

AS NEEDED
  #learn            ← Knowledge capture
  #recall           ← Knowledge retrieval
  #decide           ← Log a decision
  #pre-decide       ← Before big decisions
  #think            ← Stress-test a claim
  #exec-plan        ← Build a plan
  #trace-capture    ← After major workflows
  #runtime-start    ← Multi-step workflow
  #pm-prd           ← PRD generation
  #pm-discovery     ← Discovery synthesis
  #pm-rca           ← Root cause analysis
  #ops-dashboard    ← System health check
```

---

*Enterprise Intelligence Workspace — VDI Implementation Playbook*  
*One operator. One session. Everything human-gated.*  
*Version 1.0 — 2026-05-24*
