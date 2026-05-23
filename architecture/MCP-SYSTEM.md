# MCP System
## Capability Layer, Permission Model, Routing, and Governance
## Consolidates: MCP-ROUTING-SYSTEM.md · MCP-CAPABILITY-LAYER.md

---

## What This System Is

The MCP capability layer governs all external tool access — connections beyond the workspace boundary (design tools, calendar, email, deployment, browsers). It answers three questions:

1. **What can this workspace invoke?** → `capabilities/TOOL-REGISTRY.json`
2. **Has this been approved?** → `capabilities/MCP-REGISTRY.json`
3. **What has been invoked, with what outcome?** → `capabilities/INVOCATION-LOG.jsonl`

---

## Active MCP Servers

| MCP | Permission Class | Capability Scope |
|-----|----------------|-----------------|
| **Figma** | `RW` | Design creation, UI mockups, components, design↔code, FigJam |
| **Gamma** | `NET` | Presentations, documents, webpages |
| **Gmail** | `NET` / `DESTR` for send | Email drafting, reading, organizing |
| **Google Calendar** | `NET` | Event creation, scheduling, availability |
| **Google Drive** | `NET` | Cloud document creation and file access |
| **Playwright** | `NET` | Browser automation, web testing, screenshots |
| **Vercel** | `DESTR` | Deployment, CI/CD, preview URLs, environment vars |
| **IDE** | `RW` | Code execution, diagnostics in local IDE |

---

## Permission Model

| Class | Symbol | Definition | Gate policy |
|-------|--------|-----------|-------------|
| Read-only | `R` | No side effects (read files, query) | No gate — auto-allowed |
| Read-write | `RW` | Modifiable local state (write files, update graphs) | Gate on first novel use per session; subsequent same-tool uses auto |
| Network | `NET` | External network calls, API reads/writes | Gate every invocation OR per-session pre-authorization |
| Destructive | `DESTR` | Irreversible or high-blast-radius (deploy, send, delete) | Gate every invocation — no exceptions |

**Hard rules:**
- Silence is not a gate signal — no response means no invocation
- NET-class: per-session pre-authorization acceptable
- DESTR-class: per-invocation confirmation required, no blanket approval, ever
- Never send email or create calendar events without explicit operator confirmation

---

## Intent → MCP Routing

### Design and Visual
| Intent | MCP | Rule |
|--------|-----|------|
| "Create a mockup", "design a screen/UI" | Figma | Always run `get_design_context` before generating |
| "Make a diagram" | Figma (FigJam) | Clarify diagram type |
| "Update this design" | Figma | Need the Figma URL or file key first |
| "Make a presentation", "create a deck" | Gamma | Ask about slide count, theme, audience |
| "Write a report for sharing" | Gamma or Google Drive | Gamma = visual; Drive = collaborative |

### Communication and Calendar
| Intent | MCP | Rule |
|--------|-----|------|
| "Send an email" | Gmail | Confirm before sending — always |
| "Draft an email" | Gmail | Draft and show before sending |
| "Schedule a meeting" | Google Calendar | Confirm before creating event |
| "Check availability" | Google Calendar | Read-only; no confirmation needed |

### Development and Deployment
| Intent | MCP | Rule |
|--------|-----|------|
| "Deploy this" | Vercel | Ask: preview or production? |
| "Deploy to production" | Vercel | Extra confirmation — production is irreversible |
| "Check deploy status" | Vercel | Read-only |
| "Test in a browser", "run UI tests" | Playwright | Confirm scope before executing |
| "Take a screenshot" | Playwright | Read-only; proceed |

---

## Registry Architecture

```
capabilities/
├── MCP-REGISTRY.json       ← registered MCP servers (status, permission class, approval record)
├── TOOL-REGISTRY.json      ← individual tool capabilities per server
├── CAPABILITY-INDEX.json   ← searchable index by category + permission class (derived, never hand-edited)
└── INVOCATION-LOG.jsonl    ← append-only audit log of all invocations
```

**MCP-REGISTRY.json entry schema:**
```json
{
  "id": "server_id",
  "name": "Human-readable name",
  "source": "platform | operator",
  "permission_class": "R | RW | NET | DESTR",
  "status": "active | inactive | suspended | retired | pending_approval",
  "approved_by": "operator | platform",
  "approved_at": "YYYY-MM-DD",
  "capabilities": ["tool_a", "tool_b"],
  "last_used": "YYYY-MM-DD | null",
  "invocation_count": 0
}
```

**INVOCATION-LOG.jsonl entry schema:**
```json
{"ts": "ISO8601", "tool_id": "server.tool", "permission_class": "NET", "gated": true, "outcome": "success | error | blocked", "duration_ms": 0, "session_id": "..."}
```

---

## Capability Lifecycle

```
Proposed → /mcp-register (validation + approval gate) → Pending Approval
    ↓ operator confirms
Active → used normally (invocation logged)
    ↓ operator suspends OR anomaly detected
Suspended (cannot be invoked; must return to active before use)
    ↓ 0 invocations in last 30 days
Retired (permanent record preserved for audit)
```

---

## Governance Rules (G-Series)

| Rule | Statement |
|------|-----------|
| G-1 | No operator-sourced MCP server may be invoked before completing `/mcp-register` |
| G-2 | DESTR-class requires explicit per-invocation operator confirmation; no blanket approval |
| G-3 | NET-class requires per-session pre-authorization OR per-invocation gate; never auto-approved |
| G-4 | Every invocation logged to INVOCATION-LOG.jsonl with outcome; no silent invocations |
| G-5 | Suspended servers cannot be invoked regardless of capability |
| G-6 | TOOL-REGISTRY is the definitive list of invokable tools; absent = cannot invoke |
| G-7 | CAPABILITY-INDEX is derived — rebuild via `scripts/capability_index.py`, never hand-edit |
| G-8 | Skill produces content first; MCP renders/transmits after — never invoke write-capable MCP without skill output |
| G-9 | HIGH_ERROR_RATE anomaly (≥3 errors in 10 invocations) triggers suspension pending investigation |
| G-10 | Retiring a capability requires 0 invocations in last 30 days |

---

## Skill Interface

| Skill | Purpose |
|-------|---------|
| `/mcp-register` | Register and configure a new MCP server |
| `/mcp-status` | Health check and status of registered MCP servers |
| `/capability-search` | Find available tools by keyword, category, or permission class |
| `/capability-audit` | Audit invocation history and detect anomalies |
