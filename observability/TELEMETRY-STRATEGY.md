# Telemetry Strategy
## Observability for the Operational Intelligence Workspace

---

## What We're Measuring and Why

This is not application monitoring. This is system-level feedback on whether the workspace is producing value. Every metric should answer one of three questions:

1. **Cost:** Are we spending wisely on AI?
2. **Quality:** Is the intelligence we're producing actually good?
3. **Utilization:** Which parts of the system are being used, and which are dead weight?

---

## Signal Taxonomy

### Tier 1 — Automated (captured per API call)

Logged automatically by `production-ai/claude_client.py` for every API call.

Stored in `telemetry/api-log.jsonl`:
```json
{"ts": "ISO-UTC", "session_id": "8-char ID", "workflow": "name", "model": "model-id",
 "prompt_version": "path or inline", "input_tokens": 0, "output_tokens": 0,
 "cache_read_tokens": 0, "cache_write_tokens": 0, "latency_ms": 0}
```

Stored in `telemetry/workflow-log.jsonl`:
```json
{"ts": "ISO-UTC", "session_id": "8-char ID", "workflow": "name",
 "status": "started|completed|failed", "file": "input file", "error": "if failed"}
```

`session_id` groups all API calls from a single script invocation. Same ID shared across multi-stage workflows in one run.

### Tier 2 — Human-Rated (captured after reviewing outputs)

Stored in `observability/quality.jsonl`:
- `prompt` — prompt file name
- `version` — prompt version
- `score` — 1-5 (1=useless, 3=acceptable, 5=excellent)
- `note` — optional one-line note on what was good/bad
- `ts` — ISO timestamp

**Target frequency:** Rate at least 3 outputs per week. This is the highest-leverage observability action.

**Manual rating (Python):**
```python
import json
from datetime import datetime, timezone
from pathlib import Path

Path("observability/quality.jsonl").parent.mkdir(exist_ok=True)
with open("observability/quality.jsonl", "a") as f:
    f.write(json.dumps({
        "ts": datetime.now(timezone.utc).isoformat(),
        "prompt": "workflows/meeting-debrief",
        "version": "v1.0",
        "workflow": "meeting-debrief",
        "score": 4,
        "note": "Good structure, action items slightly verbose"
    }) + "\n")
```

### Tier 3 — Derived (computed weekly by observability agent)

Computed from Tier 1+2 and written to `observability/dashboard.md`:
- Cache hit rate by workflow (`cache_read / (cache_read + cache_write)`)
- Token cost per workflow (aggregated from api-log)
- Quality score trend per prompt (7-day rolling average)
- Workflow utilization (which W0x fired this week)
- P95 latency per model tier

---

## Alert Thresholds

| Metric | Warning | Critical | Action |
|--------|---------|---------|--------|
| Cache hit rate | <60% | <40% | Review system prompt variability |
| Sonnet cost/week | >$15 | >$25 | Audit which workflows are overrunning |
| Opus cost/week | >$30 | >$50 | Reduce extended thinking budget |
| Prompt quality score | <3.5 | <3.0 | Trigger prompt revision sprint |
| Workflow dead time | >14 days | >30 days | Evaluate if workflow should be removed |
| Knowledge decay | >90 days no review | >180 days | Flag for review or archive |

---

## Improvement Loop

The observability system is only valuable if it drives change. The loop:

```
Telemetry logged → Weekly dashboard generated → Flags surface in weekly review
       ↑                                                       │
       │                                                       ▼
System improved ← Specific change made ← Human decision on flagged metric
```

**Rule:** Every flag in the dashboard must result in one of three dispositions in the weekly review:
1. **Fix now** — change the prompt, workflow, or configuration
2. **Monitor** — watch for another week before acting
3. **Accept** — consciously decide the metric is acceptable as-is

No flag should be ignored without a decision.

---

## Dashboard Template (`observability/dashboard.md`)

Generated weekly by observability agent from telemetry files:

```markdown
# Workspace Dashboard — Week YYYY-WW

## Cost Summary
- Total API cost this week: $X.XX
  - Haiku: $X.XX (X% of total)
  - Sonnet: $X.XX (X% of total)
  - Opus: $X.XX (X% of total)
- Cache hit rate: X% (target: >60%)
- Cost vs. prior week: +/-X%

## Workflow Utilization
| Workflow | Runs | Avg Duration | Avg Tokens |
|----------|------|-------------|------------|
| W01 Daily Briefing | X | Xs | X |
| ... | | | |

## Quality Scores (human-rated)
| Prompt | Version | Avg Score | Trend |
|--------|---------|-----------|-------|
| ... | | | |

## Flags
- [ ] [COST] Sonnet workflow X running 2x expected tokens — investigate prompt bloat
- [ ] [QUALITY] meeting-debrief-v1.0 scored 2.8 this week — revise
- [ ] [DEAD] W08 synthesis-memo not triggered in 21 days — still needed?
- [ ] [DECAY] knowledge/concepts/X.md not reviewed in 95 days

## Recommended Actions
1. ...
2. ...
```

---

## Privacy Model

Telemetry logs contain no personally identifiable information:
- Meeting participants are replaced with role labels (e.g., "peer-1") at log time
- Note content is not logged — only token counts and workflow metadata
- Quality scores are prompt-level, not content-level
