# /capability-audit — Capability Invocation Audit and Anomaly Detection

Read and analyze `capabilities/INVOCATION-LOG.jsonl` for usage patterns, error rates, gate compliance, and governance anomalies.

## Trigger
`/capability-audit` — recent 20 invocations + anomaly check (default)
`/capability-audit --stats` — aggregate statistics: total invocations, error rates, top tools, gate compliance
`/capability-audit --anomalies` — anomalies only (error spikes, volume spikes, gate bypasses)
`/capability-audit --tool [tool_id]` — filter to a specific tool
`/capability-audit --since YYYY-MM-DD` — filter to a date range
`/capability-audit --ungated` — show all NET/DESTR invocations without an operator gate (governance violations)

---

## Protocol

### Default: recent invocations + anomaly check

Run:
```
python scripts/capability_audit.py
```

Display the invocation table. After the table, run anomaly detection and surface any findings:

```
⚠ [N] anomalies detected:
  [HIGH_ERROR_RATE] playwright.navigate — 45% error rate over last 20 invocations
  → Investigate before next invocation. Check server status with /mcp-status.
```

If no invocations yet: "No invocations logged. Invocation log will populate as capabilities are used."

### Statistics: `--stats`

Run `python scripts/capability_audit.py --stats`. Display the aggregate table. After stats, append anomaly summary if any detected.

### Anomalies only: `--anomalies`

Run `python scripts/capability_audit.py --anomalies`. Two anomaly types and their response:

| Anomaly | Condition | Required Action |
|---------|-----------|----------------|
| `HIGH_ERROR_RATE` | >30% errors in last 20 invocations for a tool | Do not invoke the tool again until investigated. Check `/mcp-status --server [id]` and tool documentation. Consider suspending the server with `/mcp-register --suspend [id]` if systemic. |
| `VOLUME_SPIKE` | >100 invocations of one tool in a single session | Verify this was intentional. Check for runaway loops in the session. |

**Governance rule G-9:** A `HIGH_ERROR_RATE` anomaly flag must be surfaced to the operator before the next use of that tool. Do not silently proceed.

### Tool filter: `--tool [tool_id]`

Run `python scripts/capability_audit.py --tool [tool_id]`. Shows the full invocation history for one tool: outcomes, timing, gate compliance, and any anomalies specific to it.

### Date filter: `--since YYYY-MM-DD`

Append `--since YYYY-MM-DD` to any of the above to restrict to a date window.

---

## Anomaly Thresholds (Reference)

These are the thresholds baked into `scripts/capability_audit.py`:

| Metric | Threshold |
|--------|-----------|
| Error rate (HIGH_ERROR_RATE) | >30% over last 20 invocations; requires ≥5 records to trigger |
| Volume spike (VOLUME_SPIKE) | >50 invocations of one tool in one session |
| Gate bypass (GATE_BYPASS) | Any NET/DESTR invocation with `gated=false` |

---

## When to Run

- After any session that used NET or DESTR tools
- When a tool starts returning unexpected errors
- As part of `/observe` workspace health — include capability stats in the observability sweep
- Before retiring a server: confirm 0 invocations in the last 30 days (`--stats`)
- Periodic governance hygiene: run `--ungated` weekly to verify gate compliance

---

## Related

- `/mcp-status` — server-level status and invocation counts
- `/mcp-register --suspend` — suspend a server with a HIGH_ERROR_RATE anomaly
- `/capability-search` — find what's available to invoke
- `architecture/MCP-CAPABILITY-LAYER.md` — full governance rules (G-1 through G-10)
