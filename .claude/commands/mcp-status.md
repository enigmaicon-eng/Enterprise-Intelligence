# /mcp-status — View Registered MCP Servers and Capability Health

Show the current state of all registered MCP servers: status, permission class, invocation counts, and gate policy summary.

## Trigger
`/mcp-status` — show all servers.
`/mcp-status --active` — active servers only.
`/mcp-status --server [server_id]` — full detail for one server.
`/mcp-status --classes` — capability counts by permission class.

---

## Protocol

### Default view: all servers

Run:
```
python scripts/capability_register.py --list
```

Display as a clean table:
```
MCP Registry — [N] servers total  (Active: N  Suspended: N  Retired: N)

  ID                             Status       Class   Invocations   Last Used
  ─────────────────────────────────────────────────────────────────────────────
  claude_ai_figma                active       RW      0             never
  claude_ai_gamma                active       NET     0             never
  claude_ai_gmail                active       NET     0             never
  claude_ai_google_calendar      active       NET     0             never
  claude_ai_google_drive         active       NET     0             never
  ide                            active       RW      0             never
  plugin_playwright              active       NET     0             never
  plugin_vercel                  active       DESTR   0             never
```

After the table, note any health conditions:

- Suspended servers: `⚠ [N] server(s) suspended — capabilities from these servers are blocked`
- Servers with anomalies (cross-reference `/capability-audit --anomalies`): `⚠ Anomaly flags pending — run /capability-audit for details`
- Empty log (no invocations ever): `Registry initialized. No invocations logged yet.`

### Filter: `--active`

Run `python scripts/capability_register.py --list --status active`. Same table format, limited to active servers.

### Server detail: `--server [server_id]`

Read `capabilities/MCP-REGISTRY.json`. Find the matching entry. Display:

```
Server: [name] ([server_id])
  Status          : active
  Source          : platform | operator
  Permission class: RW
  Gate policy     : Gate on first novel use per session; subsequent same-tool uses: auto
  Transport       : platform_managed
  Command         : mcp__claude_ai_Figma__*
  Capabilities    : 17 tools
  Invocations     : 0 total
  Last used       : never
  Registered      : 2026-05-22
  Approved by     : platform
  Notes           : [notes field]
```

Gate policy lookup by class:
- `R` → No gate — auto-allowed
- `RW` → Gate on first novel use per session; subsequent same-tool uses: auto
- `NET` → Gate on every invocation, or operator pre-authorizes session scope
- `DESTR` → Gate on every invocation — no exceptions

### Capability class summary: `--classes`

Read `capabilities/CAPABILITY-INDEX.json`. Display:

```
Capabilities by Permission Class:

  R      [N] tools  — no gate required (auto-allowed)
  RW     [N] tools  — gate on first novel use per session
  NET    [N] tools  — gate on every invocation
  DESTR  [N] tools  — gate on every invocation, no exceptions

Total: [N] capabilities across [N] active servers
```

If any servers are suspended or retired, note: `[N] tools restricted (suspended/retired servers)`.

---

## When to Use

- Before invoking an unfamiliar server, to confirm it is active
- After `/mcp-register` to verify the operation took effect
- To check the gate policy that will apply before calling a NET or DESTR tool
- When a tool stops working — check if its server has been suspended
- During `/observe` workspace health review

---

## Related

- `/mcp-register` — register, suspend, reactivate, or retire a server
- `/capability-search` — find tools by keyword, category, or permission class
- `/capability-audit` — invocation log, error rates, and anomaly detection
