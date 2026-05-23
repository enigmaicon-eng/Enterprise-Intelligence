# AI System Incident Response Playbook
## From detection to postmortem in under 60 minutes

An AI incident is any event where AI system outputs degrade below the quality SLO, infrastructure failures persist beyond a single retry, or costs spike anomalously. AI incidents are different from traditional software incidents: they often have no error signal, can persist for days before detection, and require quality reasoning to resolve — not just a rollback.

---

## Incident Severity Levels

| Level | Definition | Response Time | Who Acts |
|-------|-----------|--------------|---------|
| S1 — Critical | AI system producing wrong outputs on high-stakes decisions; complete service failure; runaway cost spike (> 10× normal) | Immediate | Stop using the system; fix before resuming |
| S2 — High | Quality SLO breach confirmed (< 80% pass rate); persistent infrastructure errors; significant cost anomaly (> 3×) | Within the session | Investigate and fix; eval before resuming |
| S3 — Medium | Quality degradation detected but SLO not yet breached; intermittent errors; moderate cost increase (1.5-3×) | Within 24 hours | Document; schedule fix |
| S4 — Low | Single anomalous output; one-off error; minor format compliance failure | This week | Log; add to debugging backlog |

---

## Phase 1: Detection (0-10 min)

**How AI incidents are usually detected:**
- User reports: "The /debrief output seems wrong" (late detection — incident may have been ongoing)
- Eval failure: `/eval` pass rate drops below threshold (early detection)
- Telemetry anomaly: cost spike, latency spike, error rate increase
- Manual review: you notice a quality issue while using an output

**Detection quality matters:** The later you detect, the more outputs have been affected. Build early detection into the system:
- Run `/eval` after every 5 outputs for high-stakes workflows
- Check telemetry weekly for cost/error anomalies
- Set a quality threshold alert in the weekly review

**On detection, write this down immediately:**
```
Incident opened: [timestamp]
Detected by: [who / how]
Symptom: [what was observed]
Scope estimate: [which workflows, how long, how many outputs]
Initial severity: [S1/S2/S3/S4]
```

---

## Phase 2: Containment (10-20 min)

**For S1/S2:** Stop using the affected workflow until the root cause is confirmed and fixed. AI incidents are self-reinforcing if uncontained — every output produced during the incident is potentially wrong.

**For S3/S4:** Flag outputs produced during the suspected incident window for review. Don't use them for decisions until the incident is resolved.

**Containment actions by failure class:**

| Suspected class | Containment |
|----------------|------------|
| Prompt failure | Stop using the current prompt version; revert to last known good if available |
| Context failure | Disable the retrieval path; provide context inline until fixed |
| Model failure | Switch to next-higher tier while investigating |
| Infrastructure failure | Implement retry logic; if persistent, pause the workflow |

---

## Phase 3: Investigation (20-40 min)

**Start with telemetry:** Read `telemetry/api-log.jsonl` for the incident window.

```
1. When did the anomaly start in the telemetry? (Find the first entry that looks different)
2. What changed before it started?
   - Check git history of .claude/commands/ for recent prompt changes
   - Check PROMPT-REGISTRY.md for recent version bumps
   - Check if the model ID changed
   - Check if CLAUDE.md was recently updated
3. What's the failure pattern?
   - Is it all calls or specific workflows?
   - Is it all inputs or specific input types?
   - Is it correlated with time, volume, or input size?
```

**Apply the 4-class debugging protocol** from `playbooks/ai-debugging.md`.

**For quality incidents (not infrastructure):**
Run `/eval` on 3-5 outputs from the incident window and 3-5 outputs from before the incident. Compare dimension-level pass rates. The dimension that changed tells you the failure class.

**Timeline reconstruction:**
```
[Timestamp] Last known good output (eval passes)
[Timestamp] First suspected degraded output  
[Timestamp] What changed between these two timestamps?
[Timestamp] Incident detected
```

---

## Phase 4: Resolution (40-55 min)

**Apply the minimum fix.** Don't rewrite the system; fix the specific root cause.

**Fix verification protocol (non-negotiable):**
1. Apply the fix
2. Run the original failing case
3. Run `/eval` on the output
4. All 4 dimensions must pass
5. Run a second case from the same workflow
6. Run `/eval` on that output too
7. Both must pass before declaring resolution

**Do not declare resolution based on one passing output.** AI systems can appear fixed on a single case while the root cause is still present. Two cases, two evals, both pass = resolution.

**Resolution communication (if others are affected):**
```
Resolved: [timestamp]
Root cause: [one sentence]
Fix: [what changed]
Verification: eval pass rate before [X%] → after [Y%]
Outputs affected during incident: [count or range — flag these for re-review]
```

---

## Phase 5: Postmortem (within 7 days)

**Every S1/S2 incident requires a postmortem.** S3/S4 are optional but recommended for new failure patterns.

The postmortem's value is in the prevention, not the RCA. A postmortem that produces only a timeline is worthless. One that produces a system change that prevents recurrence is valuable.

**Postmortem structure:**

```markdown
## Postmortem — [Date] — [Brief Title]

### Incident summary
- Severity: [S1/S2/S3/S4]
- Duration: [start] → [end]  
- Detection lag: [time from incident start to detection]
- Outputs affected: [count or estimate]
- Impact: [what decisions were made on affected outputs, if any]

### Timeline
[Chronological sequence: cause → onset → detection → containment → resolution]

### Root cause
Classification: Class [1/2/3/4] — [sub-type]
Specific cause: [exact finding — the prompt line, the stale file, the tier mismatch]
Why it was introduced: [what created the root cause]

### Contributing factors
[Factors that made this worse or harder to detect]
- Detection lag: [why was this not caught sooner?]
- No baseline: [was there an eval baseline to compare against?]
- Missing constraint: [what would have prevented this class of failure?]

### Resolution
Fix applied: [what changed]
Verified: eval [before X%] → [after Y%]

### Prevention
For each contributing factor, a specific system change:

1. Prevention for root cause: [specific change to prompt/context/model/infra]
2. Earlier detection: [what monitoring or eval cadence would have caught this at S3 instead of S1]
3. Faster resolution: [what documentation or playbook would reduce resolution time next time]

### Lessons
[1-2 non-obvious insights. Not "we should test more." Specific and actionable.]
```

**Save to:** `strategy/postmortems/[YYYY-MM-DD]-[slug].md`

---

## Anti-Patterns in Incident Response

**Don't:**
- Keep using the system while investigating (S1/S2)
- Declare resolution without running eval
- Write a postmortem that doesn't produce prevention actions
- Fix symptoms (the specific output) without addressing the root cause (the prompt/context/model)
- Add monitoring *after* an incident without first understanding why monitoring didn't catch this one

**Do:**
- Contain first, investigate second
- Two evals to verify resolution
- Prevention actions that address contributing factors, not just the root cause
- Track the detection lag in every postmortem (it's always improvable)

---

## Incident Log

Track all S1/S2 incidents:

| Date | Severity | Failure Class | Detection Lag | Resolution Time | Prevention Implemented |
|------|---------|--------------|--------------|----------------|----------------------|
| — | — | — | — | — | — |

Review this table quarterly: are the same failure classes recurring? Is detection lag improving? If the same class appears 3 times: there's a systemic gap in your prevention approach.
