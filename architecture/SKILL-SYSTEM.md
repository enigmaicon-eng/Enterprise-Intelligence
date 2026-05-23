# Skill System
## Design Principles, Signal Routing, Capability Taxonomy, and Synthesis

Consolidates: SKILL-ARCHITECTURE.md, SKILL-ROUTING-SYSTEM.md, DYNAMIC-INVOCATION-SYSTEM.md

---

## Skill Design Principles

A skill is a self-contained context bundle for a single, well-defined job. It activates on demand, carries exactly what it needs, and produces defined output to a defined location.

**Five rules every skill must follow:**

1. **One job.** If a skill's description contains "and", it's two skills. Split it.
2. **Declared inputs.** The skill explicitly states which files it reads before proceeding.
3. **Defined output.** Specific location, specific format. No vagueness.
4. **No ambient loading.** Skills don't pre-read CLAUDE.md or memory files — those are already active.
5. **No cross-skill orchestration.** Skills don't call other skills. Pipelines are defined in workflows.

---

## Skill File Structure

```
skills/README.md                ← Catalog (source of truth for skill descriptions)
skills/<name>/SKILL.md          ← Canonical spec (full detail)
.claude/commands/<name>.md      ← Executable command file (what Claude Code loads on invocation)
```

**Two-file pattern:** `SKILL.md` is the design spec. The command file in `.claude/commands/` is the executable. They may be identical or the command file may reference the spec.

---

## Skill Spec Format

```markdown
---
name: skill-name
version: "1.0"
description: >-
  One-paragraph description. When to trigger. What it does NOT cover.
  Trigger phrases included. Third person (injected into system context).
---

# Skill Name

## When to Use
Trigger conditions. When NOT to use (name what to use instead).

## Inputs Required
Explicit file names/paths the skill must read.

## Workflow
Numbered steps. What to do, not how to think about it.

## Output Format
Exact schema or template. No ambiguity.

## Quality Gate
Checklist: 3-5 criteria that separate "done" from "done correctly".
```

---

## Skill Authoring Rules

1. `SKILL.md` stays under 500 lines. Extended content → `references/` subdirectory.
2. YAML frontmatter required: `name` and `description` at minimum.
3. Write in third person.
4. Include "When NOT to Use" — names adjacent skills. This prevents scope creep.
5. Include a Quality Gate — what makes output complete and correct.
6. No hardcoded values — file paths, dates, names come from inputs.
7. Version the skill: bump `version:` on any output format change.

---

## Signal-Based Routing

### Core Operational Signals

**`/capture`** — Raw note, thought, URL, reference without structure.
Signals: "note:", "save this", "capture", "log this", "remember that", fragmentary sentence, URL with no context.
NOT for: meetings (→ `/debrief`), decisions with rationale (→ `/decide`), content needing immediate synthesis.

**`/debrief`** — Meeting notes or transcript.
Signals: "meeting notes", "call transcript", "1:1 notes", file in `meeting-intelligence/raw/`, "just got off a call".
NOT for: pre-meeting prep (→ `/pm-agenda`), single decision (→ `/decide`).

**`/briefing`** — What to work on, what's open, today's priorities.
Signals: "what's on my plate", "what should I focus on", "start my day", "priorities for today".
NOT for: strategy prioritization (→ `/pm-prioritize`), week review (→ `/weekly`).

**`/weekly`** — Structured weekly review.
Signals: "weekly review", "week in review", "what happened this week", Monday trigger.
NOT for: daily briefing, single meeting.

**`/promote`** — Promote a note or meeting extract to permanent knowledge.
Signals: "add to knowledge", "this is worth keeping", "promote this", "permanent note".

**`/decide`** — Log a decision with rationale.
Signals: "I decided", "we're going with", "decision:", "we chose", "logging this decision".
NOT for: evaluating options (→ `/pm-prioritize` or `/pm-opportunity`).

**`/synthesize`** — Cross-domain or cross-file insight.
Signals: "what patterns do you see across", "connect these ideas", "cross-cutting insight".
NOT for: single-topic PM analysis (→ domain-specific `/pm-*`).

**`/observe`** — Workspace health, telemetry, system state.
Signals: "how is the workspace doing", "system health", "workspace audit", "quality scores".

---

## PM Skill Signal Map

### Strategy & Vision
| Skill | Signals |
|-------|---------|
| `/pm-strategy` | "product strategy", "strategic direction", "where should the product go" |
| `/pm-vision` | "product vision", "long-term direction", "what are we building toward" |
| `/pm-press-release` | "working backwards", "press release", "start from the customer outcome" |
| `/pm-zero-to-one` | "0 to 1", "brand new product", "founding hypothesis", "kill conditions" |

### Discovery & Research
| Skill | Signals |
|-------|---------|
| `/pm-discovery` | "user research", "discovery", "what do users need", "synthesize interviews" |
| `/pm-user-interview` | "interview guide", "conversation guide" |
| `/pm-competitive` | "competitive analysis", "landscape", "what are competitors doing" |
| `/pm-teardown` | "competitive teardown", "analyze competitor product" |
| `/pm-market-sizing` | "TAM", "SAM", "market size", "how big is the market" |

### Prioritization & Planning
| Skill | Signals |
|-------|---------|
| `/pm-prioritize` | "rank these", "which first", "prioritize", "trade-offs between initiatives" |
| `/pm-opportunity` | "assess this opportunity", "is this worth pursuing" |
| `/pm-roadmap` | "roadmap", "plan for next quarters", "roadmap narrative" |
| `/pm-okr` | "OKRs", "objectives and key results", "quarterly goals" |
| `/pm-sprint` | "sprint planning", "sprint goal", "acceptance criteria for sprint" |

### Requirements & Specifications
| Skill | Signals |
|-------|---------|
| `/pm-prd` | "PRD", "requirements doc", "write the spec", "product requirements" |
| `/pm-story` | "user story", "acceptance criteria", "as a user I want" |
| `/pm-design-brief` | "design brief", "design requirements for the team" |
| `/pm-wireframe` | "wireframe spec", "annotated wireframe", "layout spec" |
| `/pm-prototype` | "prototype brief", "fidelity decision", "what should we test" |
| `/pm-ml` | "AI feature", "ML feature spec", "evals", "responsible AI" |

### Analytics & Measurement
| Skill | Signals |
|-------|---------|
| `/pm-metric-design` | "success metric", "how do we measure this", "north star" |
| `/pm-experiment` | "A/B test", "experiment design", "test hypothesis" |
| `/pm-anomaly` | "metric drop", "something's off in the data", "investigate this" |
| `/pm-analytics` | "deep dive analytics", "cohort analysis", "funnel", "retention" |
| `/pm-growth` | "growth analysis", "acquisition funnel", "growth lever" |

### Execution & Launch
| Skill | Signals |
|-------|---------|
| `/pm-launch` | "launch readiness", "go/no-go", "are we ready to ship" |
| `/pm-rollout` | "feature flag", "staged rollout", "kill switch" |
| `/pm-gtm` | "go-to-market", "GTM plan", "launch plan for customers" |
| `/pm-beta` | "beta program", "graduation criteria", "beta to GA" |

### Stakeholders & Communication
| Skill | Signals |
|-------|---------|
| `/pm-stakeholders` | "stakeholder map", "DACI", "who owns what" |
| `/pm-exec-brief` | "exec brief", "brief for leadership", "one-pager for execs" |
| `/pm-status` | "status update", "weekly update for the team" |
| `/pm-influence` | "influence without authority", "get buy-in", "stakeholder alignment" |
| `/pm-agenda` | "meeting agenda", "prep for this meeting", "structure this discussion" |
| `/pm-deps` | "dependencies", "cross-team map", "who do we depend on" |

### Retrospective & Learning
| Skill | Signals |
|-------|---------|
| `/pm-retro` | "retro", "retrospective", "post-mortem", "sprint retro" |
| `/pm-rca` | "root cause", "why did this happen", "RCA" |
| `/pm-incident` | "incident", "outage post-mortem", "what went wrong" |
| `/pm-tech-debt` | "tech debt", "investment case for cleanup" |

### Specialized
| Skill | Signals |
|-------|---------|
| `/pm-positioning` | "positioning", "differentiation", "how do we position this" |
| `/pm-pricing` | "pricing strategy", "packaging", "willingness to pay" |
| `/pm-privacy` | "privacy review", "GDPR", "privacy by design" |
| `/pm-fdpm` | "forward deployed PM", "customer engagement", "on-site with customer" |
| `/pm-design-critique` | "design review", "critique this design", "UX review" |

---

## Composite Workflow Detection

When signals span multiple skills, surface a pipeline rather than picking one:

**Discovery → Requirements:** "We did research and need to spec the feature."
→ `/pm-discovery` → `/pm-prd`. Surface and confirm before step 1.

**Incident → Improvement:** "Major bug last week — figure out what happened and prevent it."
→ `/pm-incident` → `/pm-rca` → `/pm-rollout`. Surface sequence.

**Meeting → Action:** "Just out of a strategy session with notes."
→ `/debrief` first. Then `/pm-strategy` if synthesis needed.

**Rule:** Never silently run a pipeline. One sentence, one confirmation.

---

## Ambiguity Resolution

Ask exactly one question:

| Ambiguous signal | Question |
|-----------------|---------|
| "prioritize" | "Ranking specific initiatives (→ `/pm-prioritize`) or building the roadmap narrative (→ `/pm-roadmap`)?" |
| "analyze" | "A specific metric drop (→ `/pm-anomaly`) or a full analytics deep dive (→ `/pm-analytics`)?" |
| "strategy" | "Product strategy direction (→ `/pm-strategy`) or stakeholder alignment (→ `/pm-influence`)?" |
| "review" | "Weekly review (→ `/weekly`) or design review (→ `/pm-design-critique`) or workspace health (→ `/observe`)?" |

If still unclear after one answer: default to the more general skill.

---

## Skill Overlap Prevention

Never invoke both without a reason:
- `/pm-strategy` (12-month how) vs. `/pm-vision` (3-year what) — choose based on time horizon
- `/pm-prioritize` (scores items) vs. `/pm-roadmap` (narrative from scored items) — prioritize precedes roadmap
- `/pm-rca` (causal deep-dive) vs. `/pm-incident` (operational post-mortem) — RCA follows incident
- `/pm-experiment` (tests intervention) vs. `/pm-metric-design` (defines the metric) — metric design precedes experiment

---

## Capability Taxonomy

Abstract capability names used in routing decisions:

**Operational:** `orient_daily` `/briefing` | `capture_input` `/capture` | `process_meeting` `/debrief` | `log_decision` `/decide` | `review_week` `/weekly` | `audit_workspace` `/observe` | `synthesize_cross_domain` `/synthesize` | `promote_to_knowledge` `/promote`

**Knowledge:** `capture_learning` `/learn` | `document_pattern` `/pattern` | `retrieve_knowledge` `/recall` | `test_recall_quality` `/recall-test` | `extract_repo_intelligence` `/repo-learn`

**Strategy:** `manage_strategic_bet` `/bet` | `scan_horizons` `/horizon` | `review_strategy` `/strategy-review` | `assess_strategic_posture` `/strategy-posture`

**Execution:** `plan_initiative` `/exec-plan` | `decompose_tasks` `/exec-decompose` | `review_execution` `/exec-review` | `checkpoint_initiative` `/exec-checkpoint` | `surface_risks` `/exec-risk` | `prioritize_operations` `/exec-prioritize`

**Cognitive:** `stress_test_thinking` `/think` | `detect_misconceptions` `/misconception` | `critique_architecture` `/arch-critique` | `review_decisions` `/decision-review` | `extract_insights` `/insight`

**MCP Capability:** `create_design` Figma | `build_presentation` Gamma | `send_email` Gmail | `deploy_app` Vercel | `browser_automation` Playwright

---

## Skill Synthesis Flow

When a novel capability gap is confirmed:

```
GATE 1: Gap Validation
  "No existing skill covers [capability]. Is this genuinely new or a variant?"
  ↓ Operator: VALIDATE

GATE 2: Spec Draft
  Draft using templates/skill-spec.md:
  • One-job definition (no "and")
  • Trigger conditions (specific phrases)
  • When NOT to use (names adjacent skills)
  • Declared inputs (explicit file paths)
  • Output: type + location + format
  • Quality gate (3-5 checkboxes)
  ↓ Operator: APPROVE (or REVISE → iterate → APPROVE)

GATE 3: Registration Confirmation
  "Create: .claude/commands/[name].md + register in skills/README.md. Confirm?"
  ↓ Operator: CONFIRM
  → Write files → skill active as /[name]
```

**Synthesis rules:**
- One job per skill. "and" in the spec = split it.
- "When NOT to use" must name at least one adjacent skill.
- New skills start with `status: "draft"` until invoked once and output reviewed.
- Before proposing: run duplicate check — exact match → name existing; partial → classify variant/extension.

---

## Key Data Files

| What | Path |
|------|------|
| Skill catalog | `skills/README.md` |
| Skill registry (machine-readable) | `skills/registry.json` |
| Capability index | `skills/capability-index.json` |
| Canonical skill template | `templates/skill-spec.md` |

---

## Anti-Patterns

| Anti-Pattern | Problem | Fix |
|---|---|---|
| Skill does 3+ distinct things | Skill bloat | Split into focused skills |
| Skill reads files "just in case" | Ambient loading | Declare explicit required inputs |
| Skill says "produces a summary" | Output vagueness | Define exact section structure |
| Skill invokes another skill | Cross-skill coupling | Move orchestration to workflow |
| New skill created for existing-skill variant | Catalog bloat | Classify as variant; adapt invocation |
| Full registry loaded for every request | Token waste | Load registry only for `/skill-lookup` |
