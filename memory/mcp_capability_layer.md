---
name: mcp-capability-layer
description: P19 MCP + Tool Capability Layer — governance, registry, and observability for all external tool capabilities in the workspace
metadata:
  type: project
---

P19 is complete as of 2026-05-23. Adds governed, observable, bounded expansion of external tool capabilities.

**Why:** All prior phases (P0–P18) operated within the workspace boundary. P19 extends governance to external capabilities (MCP servers, workspace scripts) with the same rigor as internal workflows — so capability growth remains traceable and safe.

**How to apply:** Before invoking any external tool, confirm it is in the registry and active. For NET/DESTR tools, confirm the gate policy is in effect. When adding a new MCP, use `/mcp-register` (never ad hoc).

## What Was Built

Architecture: `architecture/MCP-CAPABILITY-LAYER.md` — full governance model (G-1 through G-10).

Registry files in `capabilities/`:
- `MCP-REGISTRY.json` — 8 platform MCP servers (Figma RW, Gamma NET, Gmail NET, Google Calendar NET, Google Drive NET, IDE RW, Playwright NET, Vercel DESTR)
- `TOOL-REGISTRY.json` — 36 individual tool capabilities across servers + workspace scripts
- `CAPABILITY-INDEX.json` — derived searchable index (rebuilt by `capability_index.py`, never hand-edited — G-7)
- `INVOCATION-LOG.jsonl` — append-only audit log (never modified — G-4)

Scripts in `scripts/`:
- `capability_register.py` — register, suspend, reactivate, retire servers; log invocations
- `capability_index.py` — rebuild CAPABILITY-INDEX.json; keyword search; staleness check
- `capability_audit.py` — invocation stats, anomaly detection (HIGH_ERROR_RATE, VOLUME_SPIKE, GATE_BYPASS)

Skills:
- `/mcp-register` — lifecycle management (add, suspend, reactivate, retire)
- `/mcp-status` — view server health, invocation counts, gate policies
- `/capability-search` — discover tools by keyword, category, or permission class
- `/capability-audit` — invocation log, error rates, gate compliance, anomaly surfacing

Playbook: `playbooks/mcp-onboarding.md` — 5-phase flow for safely adding new capabilities.

## Permission Model Summary

| Class | Gate | Examples |
|-------|------|---------|
| R | None | figma.get_design_context, ide.get_diagnostics |
| RW | First use per session | figma.use_figma, ide.execute_code, workspace scripts |
| NET | Every invocation | gamma.generate, playwright.navigate, gmail.authenticate |
| DESTR | Every invocation, no exceptions | vercel.authenticate, vercel.complete_authentication |

## Key Governance Rules

G-1: No operator MCP may be invoked before `/mcp-register` approval.
G-2: DESTR tools require per-invocation confirmation — no blanket session approval.
G-4: Every invocation logged — no silent tool use.
G-7: CAPABILITY-INDEX is derived — never hand-edit.
G-9: HIGH_ERROR_RATE anomaly must be surfaced before next use of that tool.
G-10: Retire requires 0 invocations in last 30 days.

## Links

- [[dynamic-invocation-system]] — P14 skill routing; P19 extends it to external capabilities
- [[bounded-runtime]] — P13 B-rules; G-rules extend the autonomy model to external tools
- [[persistent-execution-system]] — P15 execution journal; INVOCATION-LOG is the capability-layer parallel
