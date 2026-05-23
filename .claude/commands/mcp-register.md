# /mcp-register — Register or Manage an MCP Server

Register a new operator-added MCP server, or manage the lifecycle of existing ones (suspend, reactivate, retire).

## Trigger
`/mcp-register` — interactive registration flow for a new MCP server.
`/mcp-register --suspend [server_id]` — suspend a server (prevents all invocations).
`/mcp-register --reactivate [server_id]` — reactivate a suspended server.
`/mcp-register --retire [server_id]` — retire a server (requires 30+ days inactive).
`/mcp-register --update [server_id]` — update notes or capabilities list (not permission class).

## Governance Rules in Effect
- **G-1:** No operator MCP may be invoked before completing this registration + approval flow.
- **G-8:** A server's permission class can only be elevated (e.g., RW → NET) through a new registration. Downgrading requires re-registration and justification.
- **G-10:** Retire requires 0 invocations in the last 30 days.

## Protocol

### Register a new server (interactive flow)

**Step 1: Gather registration details.**

Ask the operator for (or accept as arguments):
```
MCP server registration:
  Server ID     : [unique slug, e.g. github_mcp]
  Display name  : [human-readable name]
  Transport     : stdio | sse | http
  Command/URL   : [e.g. npx @modelcontextprotocol/server-github]
  Capabilities  : [comma-separated list of tool names, if known]
  Notes         : [purpose, known risks, any path restrictions]
```

**Step 2: Classify the permission class.**

Based on what the server does, propose the correct class:

```
Permission class assessment:
  The server you described [reads/writes/calls external APIs/modifies production].

  Proposed class: [R | RW | NET | DESTR]

  Why: [1-sentence rationale]

  Gate policy if approved:
    R:     No gate required — auto-allowed
    RW:    Gate on first use per session; subsequent uses: auto
    NET:   Gate on every invocation (or pre-authorize session scope)
    DESTR: Gate on every invocation — no exceptions
```

If the operator proposes a lower class than warranted, name the risk explicitly:
```
⚠ Classifying this server as RW instead of NET means network calls will not require
  per-invocation gates. Are you certain this server never makes external network requests?
```

**Step 3: Present the full registration summary for operator approval.**

```
Registration summary:
  ID              : [server_id]
  Name            : [name]
  Transport       : [transport]
  Command         : [command]
  Permission class: [class]
  Gate policy     : [policy description]
  Capabilities    : [N] listed
  Source          : operator

Approve this registration? (yes / adjust class / cancel)
```

Do not write to MCP-REGISTRY.json until the operator explicitly approves.

**Step 4 (on approval): Write the registration.**

Create a spec JSON in a temp location, then run:
```
python scripts/capability_register.py --add <spec.json>
```

If the tool was added successfully, rebuild the capability index:
```
python scripts/capability_index.py
```

**Step 5: Confirm and instruct.**

```
  [OK] Registered: [server_id]
       Status: active  |  Permission class: [class]
       Capabilities indexed: [N]

  To use capabilities from this server, they will appear in /capability-search results.
  Gate policy is in effect immediately.
```

---

### Suspend: `/mcp-register --suspend [server_id]`

Suspending a server blocks all invocations from it — the server remains registered but cannot be called.

Present:
```
Suspend [server_id]?
  Status will change: active → suspended
  Effect: all [N] capabilities from this server will be blocked immediately.

Confirm? (yes / cancel)
```

On confirmation: run `python scripts/capability_register.py --suspend [server_id]`. Rebuild index.

---

### Reactivate: `/mcp-register --reactivate [server_id]`

Load the server record. Confirm it is currently suspended. Present:
```
Reactivate [server_id]?
  Status will change: suspended → active
  Permission class: [class] (unchanged)

Confirm? (yes / cancel)
```

On confirmation: run `python scripts/capability_register.py --reactivate [server_id]`. Rebuild index.

---

### Retire: `/mcp-register --retire [server_id]`

Retirement is permanent (status = retired, record preserved for audit).

Check last invocation. If last_used was within 30 days:
```
Cannot retire [server_id]:
  Last used: [date] ([N] days ago)
  Required: 30+ days inactive

Suspend it first if you want to prevent further use while waiting to retire.
```

If eligible, confirm:
```
Retire [server_id] permanently?
  Last used: [date] ([N] days ago)
  Total invocations: [N]
  This is irreversible. The record is preserved for audit.

Confirm? (yes / cancel)
```

On confirmation: run `python scripts/capability_register.py --retire [server_id]`.

---

## What This Is Not

- `/mcp-register` manages the MCP server lifecycle. To see what's registered and its status, use `/mcp-status`.
- Capability discovery (searching for what exists) is `/capability-search`.
- Platform MCPs (Figma, Gamma, Playwright, Vercel, etc.) are pre-registered as `source: platform`. You cannot register, suspend, or retire them through this skill — they are managed by Claude Code settings.
