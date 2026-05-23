---
title: Risk Register — [Initiative Name or Workspace]
scope: initiative | workspace
initiative_id: INIT-YYYY-NNN | workspace
last_reviewed: YYYY-MM-DD
owner: [name]
---

## Active Risks

Each risk requires: named owner, specific trigger condition, concrete mitigation action. Generic background risks without owners are not tracked here.

---

### RISK-[YYYY]-001 — [Short Risk Name]
- **Description**: What specifically could go wrong?
- **Probability**: High / Medium / Low — [brief rationale]
- **Impact if realized**: High / Medium / Low — [what happens if this materializes?]
- **Owner**: [name — the person watching for the trigger and acting on mitigation]
- **Trigger condition**: [The specific observable event that means this risk has materialized or is imminent]
- **Mitigation**: [The pre-planned action to take when triggered — not "we'll deal with it"]
- **Status**: open | monitoring | triggered | resolved | accepted
- **Opened**: YYYY-MM-DD
- **Close by**: YYYY-MM-DD (risks not resolved or accepted within 30 days must be re-evaluated)

---

### RISK-[YYYY]-002 — [Short Risk Name]
*(copy block above)*

---

## Risk Matrix

Probability (rows) × Impact (columns). Place risk IDs in cells.

|  | Low Impact | Medium Impact | High Impact |
|--|-----------|--------------|------------|
| **High Probability** | | | |
| **Medium Probability** | | | |
| **Low Probability** | | | |

High probability + High impact risks require a mitigation plan before work starts.

---

## Closed Risks
*(Move resolved risks here — preserve the record)*

| Risk ID | Name | Resolution | Closed Date |
|---------|------|-----------|------------|
| | | | |

---

## Risk vs. Dependency Distinction
If a condition must be met before work can start → it's a **dependency** (lives in task decomposition, not here).
If a condition might not be met and requires monitoring → it's a **risk** (lives here).
If a condition is certain to arise and requires planning → it's a **constraint** (lives in execution plan scope section).
