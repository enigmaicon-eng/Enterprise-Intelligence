# System Architecture
## Enterprise AI Operational Intelligence Workspace

---

## Architectural Layers

```
┌─────────────────────────────────────────────────────────────────────┐
│                        INTERFACE LAYER                              │
│   Claude Code CLI  │  Scripts (Python/PS)  │  Scheduled Agents      │
└─────────────────────────────┬───────────────────────────────────────┘
                              │
┌─────────────────────────────▼───────────────────────────────────────┐
│                      ORCHESTRATION LAYER                            │
│   Multi-agent workflows  │  Skill routing  │  Context assembly      │
└─────────────────────────────┬───────────────────────────────────────┘
                              │
┌─────────────────────────────▼───────────────────────────────────────┐
│                       INTELLIGENCE LAYER                            │
│   Claude API  │  Prompt library  │  Memory system  │  Synthesis     │
└─────────────────────────────┬───────────────────────────────────────┘
                              │
┌─────────────────────────────▼───────────────────────────────────────┐
│                         DATA LAYER                                  │
│   Workspace files  │  Knowledge base  │  Templates  │  Schemas      │
└─────────────────────────────┬───────────────────────────────────────┘
                              │
┌─────────────────────────────▼───────────────────────────────────────┐
│                     OBSERVABILITY LAYER                             │
│   Telemetry  │  Usage logs  │  Quality signals  │  Improvement loop │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Core Subsystems

### 1. CLAUDE.md — The Brain Stem

The workspace root `CLAUDE.md` is the single most important file. It is loaded into every Claude Code session. It must:

- Define the workspace purpose and operating principles
- Index all major directories with their contracts
- List active workflows and how to invoke them
- Reference the memory system location
- Define the user's role, context, and working style

**Design rule:** If Claude reads only `CLAUDE.md`, it should be able to execute any workflow without further instruction.

---

### 2. Memory System — Persistent Context

Location: `memory/`

Architecture:
```
memory/
├── MEMORY.md              # Index (loaded every session, <200 lines)
├── user_profile.md        # Who the user is, goals, expertise
├── project_*.md           # Active project context files
├── feedback_*.md          # Behavioral guidance from past sessions
└── reference_*.md         # External system pointers
```

**Frontmatter schema (every memory file):**
```yaml
---
name: short-kebab-slug
description: One-line summary for MEMORY.md index
metadata:
  type: user | feedback | project | reference
  updated: YYYY-MM-DD
---
```

**Critical:** MEMORY.md is an index only. Never write content into MEMORY.md.

---

### 3. Prompt Library — Reusable Intelligence

Location: `prompts/`

Structure:
```
prompts/
├── system/                # System prompts for each agent role
│   ├── analyst.md
│   ├── synthesizer.md
│   ├── reviewer.md
│   └── strategist.md
├── workflows/             # Workflow-specific prompt chains
│   ├── meeting-debrief.md
│   ├── weekly-review.md
│   └── knowledge-synthesis.md
├── templates/             # Fill-in-the-blank prompt templates
└── PROMPT-REGISTRY.md     # Index: name, purpose, version, last-used
```

**Versioning:** Every prompt file includes a version header:
```
<!-- v1.2 | 2026-05-20 | Changed: added output schema constraint -->
```

---

### 4. Multi-Agent Orchestration

The system uses three agent tiers:

**Tier 1 — Capture Agents** (fast, cheap, no synthesis)
- Purpose: Ingest raw input and apply minimal structure
- Model: `claude-haiku-4-5-20251001`
- Use for: Note tagging, meeting transcript parsing, URL metadata extraction

**Tier 2 — Analysis Agents** (medium cost, deep reasoning)
- Purpose: Analyze, compare, synthesize within a domain
- Model: `claude-sonnet-4-6`
- Use for: Meeting debriefs, research synthesis, decision analysis

**Tier 3 — Strategy Agents** (highest cost, extended thinking)
- Purpose: Cross-domain synthesis, long-horizon planning, novel insight generation
- Model: `claude-opus-4-7` with extended thinking enabled
- Use for: Weekly/monthly strategy reviews, architectural decisions, scenario modeling

**Orchestration pattern:**
```python
# Canonical multi-agent pipeline
async def run_pipeline(raw_input: str, pipeline_type: str):
    # Tier 1: structure the input
    structured = await capture_agent(raw_input)
    
    # Tier 2: analyze within domain
    analysis = await analysis_agent(structured, domain=pipeline_type)
    
    # Tier 3: synthesize if threshold met
    if analysis.synthesis_needed:
        insight = await strategy_agent(analysis, memory_context=load_memory())
        write_synthesis(insight)
    
    # Always: update telemetry
    log_pipeline_run(pipeline_type, tokens_used, latency)
```

---

### 5. Knowledge Graph (File-Based)

The knowledge base uses a flat-file graph: every knowledge file can reference others via `[[filename]]` links.

```
knowledge/
├── KNOWLEDGE-INDEX.md     # Master index by domain
├── concepts/              # Atomic concept definitions
├── domains/               # Domain-level overviews
├── research/              # Research summaries and source links
└── connections/           # Explicit cross-domain connection maps
```

**Promotion workflow:** Notes → (synthesis agent) → Knowledge  
**Decay policy:** Knowledge files get a `reviewed:` field. Files not reviewed in 90 days get flagged.

---

### 6. Template System

Every directory has a `_template.md` in `templates/` that defines:
- Required frontmatter fields
- Mandatory sections
- Example content (commented out)
- Links to related templates

This enforces schema consistency so synthesis scripts don't break on format drift.

---

### 7. Telemetry & Observability

Location: `telemetry/` + `observability/`

What to track:
| Signal | Storage | Frequency |
|--------|---------|-----------|
| API calls (model, tokens, latency) | `telemetry/api-log.jsonl` | Per call |
| Workflow runs (type, duration, output size) | `telemetry/workflow-log.jsonl` | Per run |
| Memory reads/writes | `telemetry/memory-log.jsonl` | Per session |
| Quality scores (human rating of outputs) | `observability/quality.jsonl` | Weekly |
| Prompt performance | `observability/prompt-metrics.jsonl` | Per version |

**Dashboard:** `observability/dashboard.md` — weekly summary generated by analysis agent from telemetry JSONLs.

---

## Technology Stack

| Layer | Technology | Rationale |
|-------|-----------|-----------|
| AI backbone | Anthropic Claude API | Best reasoning, native tool use, prompt caching |
| Scripting | Python 3.12+ | anthropic SDK, async, rich ecosystem |
| Automation | PowerShell 5.1 + Bash | Cross-platform for Windows host |
| Storage | Flat files (MD, YAML, JSONL) | Git-versionable, Claude-readable, zero infra |
| Scheduling | Claude Code CronCreate | Native to the tool, no external scheduler needed |
| Search | ripgrep (via Claude Code Grep tool) | Fast, regex-capable, no index needed |
| Version control | Git | Track all workspace evolution |

---

## Security Model

- API keys in environment variables only (`$env:ANTHROPIC_API_KEY`), never in files
- No PII in JSONL telemetry logs — abstract to session IDs
- `settings.local.json` excluded from any future git init
- Sensitive strategy files go in `.gitignore` if repo is made public
- Memory files contain behavioral preferences, not credentials

---

## Failure Modes & Recovery

| Failure | Detection | Recovery |
|---------|-----------|---------|
| Memory index corruption | Claude reports missing files on load | Rebuild from individual memory files |
| Prompt version regression | Quality score drop >20% in observability | Roll back to previous prompt version |
| Synthesis agent timeout | Telemetry latency spike | Retry with Tier 2 agent; flag for manual review |
| Template schema drift | Synthesis script parse error | Re-run template validation script |
| Context window overflow | Claude truncation warning | Trigger context compression workflow |
