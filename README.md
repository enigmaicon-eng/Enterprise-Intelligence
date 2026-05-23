# Enterprise Intelligence Workspace

A persistent cognitive operating environment for one operator — built for elite knowledge work across product strategy, execution, learning, and operational intelligence.

---

## What This Is

A structured, file-based workspace that runs inside [Claude Code](https://claude.ai/code). Every session starts with context, every output feeds forward, and every skill is a named, invokable behavior. The system compounds — knowledge connects to knowledge, decisions reference past decisions, execution traces reveal patterns.

**It is three things:**
1. **A skill library** — 124 named commands covering PM work, strategy, execution, knowledge management, cognitive tools, observability, and workspace audit
2. **A file-based operational memory** — structured markdown encoding decisions, knowledge, traces, strategies, and system state across sessions
3. **A governed external tool interface** — MCP capability layer with a 4-class permission model for Figma, Gmail, Google Calendar, Vercel, Playwright, and more

**It is not** an autonomous agent, enterprise AI infrastructure, or a multi-agent system. One operator. One session. Everything human-gated.

---

## Quick Start

```bash
# In Claude Code, type any slash command:
/briefing          # start your day
/plan              # set today's theme + top 3 commitments  
/cognitive-load    # is it safe to do deep work?
/pm-prd            # generate a PRD
/workspace-audit   # check workspace health
```

---

## Skill Catalog (124 skills)

### Daily Operations
`/briefing` `/plan` `/focus` `/prep` `/shutdown` `/weekly`

### Cognitive Load
`/open-loops` `/cognitive-load` `/attention-debt`

### Capture & Synthesis
`/capture` `/debrief` `/promote` `/decide` `/observe` `/synthesize`

### Knowledge
`/learn` `/recall` `/pattern` `/repo-learn` `/analogy` `/contradiction-register` `/knowledge-gap` `/learning-velocity` `/learning-source` `/knowledge-utilization` `/knowledge-connect` `/knowledge-cluster` `/knowledge-graph` `/knowledge-qa` `/recall-test` `/misconception`

### Strategy
`/bet` `/horizon` `/strategy-review` `/strategy-posture` `/signal` `/assumption-register` `/competitive-radar`

### Execution
`/exec-plan` `/exec-prioritize` `/exec-checkpoint` `/exec-decompose` `/exec-review` `/exec-risk` `/exec-throughput` `/exec-allocation` `/exec-friction`

### Trace & Recall
`/trace-capture` `/workflow-journal` `/trace-recall` `/trace-search` `/pattern-mine`

### Cognitive
`/think` `/insight`

### Decision Intelligence
`/pre-decide` `/decision-recall` `/decision-due` `/consequence-map`

### Runtime
`/runtime-start` `/runtime-resume` `/runtime-status` `/runtime-recover`

### Runtime Hardening
`/runtime-validate` `/snapshot-verify` `/reliability-check`

### Observability
`/ops-dashboard` `/exec-inspect` `/skill-stats` `/failure-review` `/retrieval-diag` `/debug-ai`

### Tool Access (MCP)
`/mcp-register` `/mcp-status` `/capability-search` `/capability-audit`

### Skill Management
`/skill-lookup` `/skill-new`

### Workspace Audit
`/workspace-audit` `/skill-overlap` `/simplify`

### PM Work (44 skills)
`/pm-strategy` `/pm-discovery` `/pm-prioritize` `/pm-exec-brief` `/pm-rca` `/pm-launch` `/pm-prd` `/pm-story` `/pm-okr` `/pm-competitive` `/pm-experiment` `/pm-status` `/pm-roadmap` `/pm-gtm` `/pm-retro` `/pm-metric-design` `/pm-opportunity` `/pm-stakeholders` `/pm-design-brief` `/pm-anomaly` `/pm-vision` `/pm-user-interview` `/pm-agenda` `/pm-deps` `/pm-tech-debt` `/pm-incident` `/pm-positioning` `/pm-growth` `/pm-sprint` `/pm-market-sizing` `/pm-wireframe` `/pm-prototype` `/pm-fdpm` `/pm-ml` `/pm-press-release` `/pm-zero-to-one` `/pm-pricing` `/pm-privacy` `/pm-influence` `/pm-teardown` `/pm-beta` `/pm-design-critique` `/pm-rollout` `/pm-analytics`

---

## Directory Structure

```
.
├── CLAUDE.md                    # Behavioral rules + routing table
├── .claude/commands/            # 124 skill files (loaded by Claude Code)
├── architecture/                # 25 reference docs + archive/
├── memory/                      # Orientation facts across sessions
├── knowledge/                   # Permanent knowledge entries by domain
├── strategy/                    # Active bets, OKRs, signals
├── traces/                      # Execution trace history + TRACE-INDEX.md
├── runtime/                     # Workflow state (JSON, atomic writes)
├── execution/                   # Action items, initiatives, risks
├── decision-frameworks/         # Decisions log + PM frameworks
├── notes/                       # Raw captures + structured notes
├── meeting-intelligence/        # Raw + processed meeting files
├── synthesis/                   # Cross-domain synthesis memos
├── prompts/                     # System prompts + workflow prompts
├── templates/                   # Skill and document templates
├── playbooks/                   # Multi-skill orchestration guides
├── workflows/                   # PM workflow definitions
├── scripts/                     # Python utilities (knowledge index, etc.)
├── capabilities/                # MCP registry + tool registry
└── skills/README.md             # Canonical skill registry
```

---

## Architecture

The workspace was built across 30 phases (P1–P30) and audited in P31 (Final Cognitive Runtime Review). Key architectural constraints:

| Constraint | Ceiling | Current |
|-----------|---------|---------|
| Skills | 120 | 124 |
| Architecture docs | 25 | 25 |
| Memory files | 30 | 22 |
| MEMORY.md lines | 200 | 28 |
| Daily ritual stack | 6 | 6 |

**Core architectural documents:**
- `architecture/FINAL-COGNITIVE-RUNTIME-REVIEW.md` — authoritative review + 70 governance rules
- `architecture/FINAL-SIMPLIFICATION-REVIEW.md` — P20 anti-complexity rules (AC-1 through AC-10)
- `architecture/FINAL-OPERATING-RULES.md` — 10 permanent operating rules
- `architecture/RUNTIME-SYSTEM.md` — file-based gated runtime
- `architecture/WORKSPACE-GUIDE.md` — navigation reference

---

## Operational Constraints

The workspace runs under hard limits enforced by `/workspace-audit`:

- **No dual persistence** — runtime state in JSON files only (no database)
- **Human gate before every step** — nothing executes without explicit operator approval
- **One workflow in RUNNING state** — hard system invariant
- **Skill ceiling at 120** — every new skill requires retiring an existing one
- **Architecture docs ceiling at 25** — every new doc requires archiving an existing one
- **Skill ceiling growth requires retirement** — not accumulation

---

## MCP Integrations

| Server | Permission Class | Scope |
|--------|----------------|-------|
| Figma | RW | Design, mockups, UI, FigJam |
| Gamma | NET | Presentations, documents |
| Gmail | NET/DESTR | Email |
| Google Calendar | NET | Scheduling |
| Google Drive | NET | Cloud files |
| Playwright | NET | Browser automation |
| Vercel | DESTR | Deployment, CI/CD |
| IDE | RW | Code execution, diagnostics |

---

## Governance

10 rule sets govern the workspace (70 rules total). Defined in `architecture/FINAL-COGNITIVE-RUNTIME-REVIEW.md`:

1. Non-Negotiable Architectural Rules (NAR-1 through NAR-7)
2. Anti-Drift Rules (ADR-1 through ADR-6)
3. Maximum Complexity Limits
4. Operational Simplicity Rules (OSR-1 through OSR-6)
5. Bounded Autonomy Rules (BAR-1 through BAR-10)
6. Memory Hygiene Rules (MHR-1 through MHR-7)
7. Retrieval Quality Rules (RQR-1 through RQR-6)
8. Skill Creation Constraints (SCC-1 through SCC-7)
9. Orchestration Constraints (OCR-1 through OCR-8)
10. Long-Term Maintenance Rules (LMR-1 through LMR-10)

---

## License

MIT — see [LICENSE](LICENSE)
