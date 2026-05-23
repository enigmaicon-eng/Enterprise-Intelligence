# MCP Onboarding Playbook
## Safe Addition of External Capabilities to the Workspace

---

## When to Use This Playbook

Use this playbook when adding a new MCP server to the workspace. The playbook enforces governance rules G-1 through G-10 by providing a structured, gate-enforced onboarding flow that prevents unvetted capabilities from entering the active tool pool.

Do NOT bypass this playbook to add a capability quickly. The registration step is lightweight; the safety it provides is not.

---

## Phase 1 — Need Identification

Before opening a terminal or writing any config, answer these three questions:

**1. What operation do you actually need?**
Name the specific primitive: read files, write files, call an external API, trigger a deploy, send a message. Vague answers (e.g., "interact with GitHub") lead to over-permissioned registrations.

**2. Does an existing capability already cover it?**
Run: `/capability-search [keyword]`. If a match exists, use that — do not register a duplicate server.

**3. Could a skill or script handle this without an external MCP?**
Run: `/skill-lookup [keyword]`. If a workspace script or skill produces the same result, prefer it — the trust boundary stays local.

If none of the above applies: proceed to Phase 2.

---

## Phase 2 — Permission Class Assessment

Determine the correct permission class before writing any registration. Choose the highest class that applies.

| If the server... | Minimum class |
|-----------------|--------------|
| Only reads local files or data | `R` |
| Writes local files, modifies the workspace | `RW` |
| Makes any external network call (API, HTTP, auth flow) | `NET` |
| Can deploy to production, send messages, delete data, or any irreversible action | `DESTR` |

**Rule:** When uncertain between two classes, always choose the higher. Permission classes can be downgraded later through re-registration with justification. They cannot be silently lowered.

**Common mis-classifications to avoid:**
- A server with "read-only API" that requires an OAuth flow → still `NET` (auth flows are network operations)
- A server that "writes to a staging environment" → `DESTR` (staging is production-adjacent)
- A server that "just" sends Slack messages → `DESTR` (messages are irreversible and visible to others)

---

## Phase 3 — Registration

Run the registration skill:
```
/mcp-register
```

The skill walks through:
1. Gathering the spec (ID, name, transport, command, capabilities, notes)
2. Classifying the permission class (with rationale)
3. Presenting the full summary for operator approval
4. Writing to `MCP-REGISTRY.json` on approval
5. Rebuilding `CAPABILITY-INDEX.json`

Do not manually edit `MCP-REGISTRY.json`. The registration script handles validation, ID uniqueness, and stats recalculation.

**If the proposed permission class is lower than what this playbook says is appropriate:** state the discrepancy before approving. Example: "This server makes OAuth calls — that's NET, not RW. Proceed with NET?"

---

## Phase 4 — Post-Registration Verification

After registration completes:

```
/mcp-status --server [server_id]
```

Confirm:
- Status: `active`
- Permission class: matches what was assessed in Phase 2
- Capabilities: list is accurate (not empty, not a superset)
- Gate policy: correct for the class

Then verify the capability index is current:
```
python scripts/capability_index.py --check
```

---

## Phase 5 — First Invocation

The first time you invoke a new capability:

1. Check gate policy for the capability's class (see `/capability-search --class [class]`)
2. If `RW`: gate on first use, then auto for the session
3. If `NET`: confirm before invoking; pre-authorize session scope if doing high-volume work
4. If `DESTR`: confirm on every single invocation — no exceptions

After the first invocation, verify it logged correctly:
```
python scripts/capability_audit.py --recent 5
```

Confirm the tool ID, outcome, and `gated` flag appear in the log. If the log shows `gated: false` for a NET or DESTR tool, that is a governance violation (G-4) — investigate before proceeding.

---

## Lifecycle Events

### Suspending a Server

Use when a server is misbehaving (high error rate, unexpected behavior) or when temporarily removing access.

```
/mcp-register --suspend [server_id]
```

Effect: immediate. All capabilities from that server are blocked. The server remains in the registry with status `suspended`. Rebuild the index after:
```
python scripts/capability_index.py
```

### Reactivating a Server

After investigating the issue and confirming it is resolved:

```
/mcp-register --reactivate [server_id]
```

Rebuild the index. Run `/capability-audit --anomalies` to confirm no unresolved anomalies.

### Retiring a Server

Requirements before retiring:
- Status is `active` or `suspended`
- 0 invocations in the last 30 days (checked automatically by the script)

```
/mcp-register --retire [server_id]
```

Retirement is permanent. The record is preserved in `MCP-REGISTRY.json` for audit. The server's capabilities become permanently restricted in the index.

---

## Anti-Patterns in Capability Onboarding

| Pattern | Why It's Forbidden |
|---------|-------------------|
| Invoking a new MCP before completing `/mcp-register` | G-1 violation: unvetted capability in active use |
| Registering as `RW` when the server makes network calls | Under-permission hides real risk; gate policy too permissive |
| Registering as `operator` when the server is already a platform MCP | Duplicate entry; breaks index integrity |
| Skipping the index rebuild after registration | Index becomes stale; capability search returns incorrect results |
| Granting `DESTR` session-level pre-authorization | G-2 violation: destructive operations require per-invocation gates |

---

## Governance Cross-Reference

Full governance rules are in `architecture/MCP-CAPABILITY-LAYER.md` (G-1 through G-10). This playbook implements the operational version of those rules. When in doubt, the architecture document is the authoritative source.
