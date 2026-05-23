# /capability-search — Discover Capabilities by Keyword, Category, or Permission Class

Search registered external tool capabilities. Use this when a skill doesn't cover what you need — the capability index shows what the workspace can invoke beyond its own skill library.

## Trigger
`/capability-search [keyword]` — ranked keyword search (e.g., `/capability-search browser screenshot`)
`/capability-search --category [category]` — browse a category
`/capability-search --class [R|RW|NET|DESTR]` — browse by permission class
`/capability-search --all` — complete capability list

---

## Protocol

### Keyword search (default)

Run:
```
python scripts/capability_index.py --search "[keyword]"
```

Display results ranked by relevance:

```
Capability search: "[keyword]"  ([N] matches)

  Tool ID                              Class   Gate           Source                Description
  ─────────────────────────────────────────────────────────────────────────────────────────────
  playwright.screenshot                NET     per-call gate  plugin_playwright     Take a screenshot of the current browser view.
  figma.get_screenshot                 R       no gate        claude_ai_figma       Capture a screenshot of a Figma frame...
```

If 0 results:
```
No capabilities found for: "[keyword]"

  Available categories: design, presentation, communication, productivity,
                        browser, deployment, ide, knowledge, execution

  → Browse a category: /capability-search --category design
  → Add a missing capability: /mcp-register
```

### Category browse: `--category [category]`

Read `capabilities/CAPABILITY-INDEX.json` → `by_category.[category]`. Display all tools in the category with permission class and gate policy.

Available categories:
- `design` — Figma tools (read designs, write designs, diagrams)
- `presentation` — Gamma tools (generate, read presentations)
- `communication` — Gmail (auth, send, read)
- `productivity` — Google Calendar, Google Drive
- `browser` — Playwright (navigate, screenshot, network, form fill, click)
- `deployment` — Vercel (auth, deploy)
- `ide` — IDE execute code, diagnostics
- `knowledge` — workspace knowledge scripts
- `execution` — workspace execution scripts

### Permission class browse: `--class [class]`

Read `CAPABILITY-INDEX.json` → `by_permission_class.[class]`. Show all tools in the class, grouped by server.

Display the gate policy for the class:
- `R` → No gate — auto-allowed
- `RW` → Gate on first novel use per session; auto on repeat
- `NET` → Gate on every invocation, or pre-authorize session scope
- `DESTR` → Gate on every single invocation — no exceptions

### Full list: `--all`

Read `CAPABILITY-INDEX.json`. Display all capabilities grouped by category, with permission class shown inline. Show totals per category and overall.

---

## Interpreting Results

**Before invoking any result:** confirm the gate policy applies per the class shown.

If a capability is listed but the server is suspended (see `/mcp-status`), invocation will be blocked regardless of what appears in search results. The index includes restricted tools; suspended server tools are flagged in the `restricted_tools` field of `CAPABILITY-INDEX.json`.

**If the capability you need isn't listed:**
1. Try broader search terms (e.g., `email` instead of `send message`).
2. Check if a skill handles it instead (`/skill-lookup [keyword]`).
3. If truly missing, document the gap and register a new MCP: `/mcp-register`.

---

## Keeping the Index Current

The capability index is a derived artifact — it is rebuilt from `MCP-REGISTRY.json` and `TOOL-REGISTRY.json` by `capability_index.py`. It does not auto-update. Rebuild after any registry change:

```
python scripts/capability_index.py
```

Governance rule G-7: never hand-edit `CAPABILITY-INDEX.json`.

---

## Related

- `/mcp-status` — server health, status, and invocation counts
- `/mcp-register` — add a new capability or manage server lifecycle
- `/capability-audit` — invocation history, error rates, and anomaly detection
- `/skill-lookup` — search the skill library (internal skills, not external tools)
