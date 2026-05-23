---
name: pm-launch
description: Run a launch readiness audit. Produces a go/no-go assessment across problem clarity, technical readiness, instrumentation, user readiness, go-to-market, and organizational readiness dimensions.
version: "1.0"
changed: 2026-05-20
---

# PM Launch

**Input:** Launch name, tier (1/2/3), and any known status on readiness areas. Provide inline or reference a launch brief doc.

**Output:** Written to `execution/launch-YYYY-MM-DD-<launch-slug>.md`

**Also updates:** `decision-frameworks/decisions-log.md` (go/no-go decision entry)

---

## Steps

1. **Read context.** Load `workflows/pm/launch-readiness.md`. Load `decision-frameworks/pm/risk-radar.md` for the risk section.

2. **Confirm tier.** Ask for tier if not provided. Tier determines which sections are required vs. optional:
   - Tier 1: all 6 sections required, executive sponsor sign-off required
   - Tier 2: sections 1-4 required, section 5-6 abbreviated
   - Tier 3: sections 1-3 required, 4-6 as applicable

3. **Run readiness audit per section.** For each item in the checklist:
   - Status: Complete / Incomplete / At risk / N/A
   - If incomplete or at risk: document the gap and proposed disposition (fix before launch / accept risk with owner / delay)

4. **Compile open items.** Any item marked Incomplete or At risk with no accepted disposition = blocking.

5. **Run go/no-go decision logic:**
   - Any blocking item in sections 1 or 2 (problem/technical) = No-go
   - Any blocking item in sections 3-6 with no named owner for post-launch remediation = No-go
   - All blocking items have named owner and accepted risk = Conditional go
   - No blocking items = Go

6. **Write rollback criteria.** Must be specific observable conditions, not judgment calls.

7. **Write the output.**

---

## Output Format

```markdown
# Launch Readiness — [Launch Name] — [Date]
**Tier:** [1/2/3] | **Target launch:** [Date]

---

## Section 1 — Problem & Hypothesis
- [x/o] Success hypothesis explicit and agreed on
- [x/o] Primary success metric named and accepted by PM + engineering + leadership
- [x/o] Guardrail metrics named
- [x/o] Baseline captured pre-launch
Open items: [list]

## Section 2 — Technical Readiness
- [x/o] End-to-end tested in staging
- [x/o] Load testing at 2x peak — result: [pass/fail, p99 latency]
- [x/o] Rollback procedure tested — time to rollback: [N min]
- [x/o] Feature flags in place
- [x/o] Monitoring and alerting configured
- [x/o] Data migration validated (if applicable)
- [x/o] Security review complete (if applicable)
Open items: [list]

## Section 3 — Instrumentation
- [x/o] All events instrumented and verified end-to-end
- [x/o] Experiment design complete (if A/B)
- [x/o] Dashboard or query ready for day-1 measurement
Open items: [list]

## Section 4 — User Readiness
- [x/o] User research informed the design (≥3 conversations)
- [x/o] Usability tested, critical issues resolved
- [x/o] Help content and docs updated
- [x/o] Edge cases mapped and handled
Open items: [list]

## Section 5 — Go-to-Market (Tier 1/2)
- [x/o] Launch communication plan exists
- [x/o] Support team trained
- [x/o] Sales enablement complete (if commercial)
- [x/o] Customer commitments cross-checked
Open items: [list]

## Section 6 — Organizational Readiness (Tier 1/2)
- [x/o] Launch timing risk assessed
- [x/o] Regulatory review complete (if applicable)
- [x/o] Executive visibility confirmed (Tier 1)
- [x/o] Post-launch monitoring schedule set
- [x/o] Escalation path clear
Open items: [list]

---

## Risk Summary (from risk-radar framework)
| Risk | Category | Priority | Owner | Mitigation |
|---|---|---|---|---|
| [risk] | technical/market/org | P0/P1/P2 | [name] | [action] |

---

## Go/No-Go Decision

**Decision: GO | NO-GO | CONDITIONAL GO**

Open items accepted as risk:
- [Item] — Disposition: [accepted/mitigated] — Owner: [name]

Conditions for conditional go (if applicable):
- [Specific observable condition] by [date]

**Post-launch monitoring owner:** [Name]
**First check-in:** [Time after launch]

**Rollback criteria (automatic):**
- Error rate > [N]% for [M] consecutive minutes
- [Other automatic trigger]

**Rollback criteria (discussion-required):**
- [Observable condition requiring team conversation]

**Approvers:** [Names]
```

---

## Quality Gate

- Every open item has a named disposition (fix / accept / delay) — no orphaned open items
- Rollback criteria are specific observable conditions, not judgment calls
- Go/no-go decision is stated explicitly — not implied
- Tier 1 launches have executive sponsor named
- Post-launch monitoring owner and first check-in time specified for all go decisions
