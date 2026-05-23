---
name: pm-stakeholders
description: Map stakeholders for an initiative using DACI and power/interest analysis. Produces engagement plan with pre-alignment strategy, communication cadence, and risk flags.
version: "1.0"
changed: 2026-05-20
---

# PM Stakeholders

**Input:** Initiative name, known stakeholders or functions involved, any known political dynamics or alignment risks.

**Output:** Written to `notes/structured/stakeholders-YYYY-MM-DD-<initiative-slug>.md`

---

## Steps

1. **Read context.** Load `knowledge/pm/org-dynamics.md` (stakeholder patterns and alignment architecture sections).

2. **List all stakeholders.** Cast wide first — who is affected by this initiative, who has authority over any part of it, who will need to support it, who could block it? Include people who might not be obvious (legal, finance, a senior engineer who has strong opinions).

3. **Apply DACI.** For each significant decision in this initiative, assign:
   - **D — Driver:** Does the work, proposes the decision. Only one person per decision.
   - **A — Approver:** Can veto. Only one person. Two approvers = broken governance.
   - **C — Consulted:** Required input before decision. Must be consulted, not just informed.
   - **I — Informed:** Needs to know after. Does not need to be in the decision.

4. **Plot the power/interest matrix.** For each stakeholder:
   - High power + High interest = Manage closely (pre-align, regular updates, involve in decisions)
   - High power + Low interest = Keep satisfied (brief updates, don't overload)
   - Low power + High interest = Keep informed (regular updates, they're advocates)
   - Low power + Low interest = Monitor (minimal engagement)

5. **Identify stakeholder archetypes.** From `knowledge/pm/org-dynamics.md`:
   - Blocker, Skeptic, Advocate, Politically motivated, Absentee
   - For each archetype: what does this stakeholder need to feel, and how do you address that?

6. **Build the engagement plan.** Pre-alignment sequence (who to meet before the official review), communication cadence (frequency and format per stakeholder), and decisions requiring stakeholder input before they're made.

7. **Flag alignment risks.** Where is misalignment most likely? What's the fallback if a key stakeholder doesn't align?

8. **Write the output.**

---

## Output Format

```markdown
# Stakeholder Map — [Initiative Name] — [Date]

**PM:** [name]  **Initiative scope:** [One-line description]

---

## Stakeholder Registry

| Name | Role | Function | DACI | Power | Interest | Archetype |
|---|---|---|---|---|---|---|
| [Name] | [Title] | [Eng/Design/Sales/etc] | D/A/C/I | H/M/L | H/M/L | [Archetype] |

---

## DACI by Decision Type

| Decision | Driver | Approver | Consulted | Informed |
|---|---|---|---|---|
| Technical approach | Engineering Lead | CTO | PM, Design | All |
| Scope and requirements | PM | PM Lead | Eng, Design, CS | All |
| Launch go/no-go | PM | PM Lead + Eng Lead | Design, QA, CS | All |
| [Other key decision] | | | | |

**DACI health check:** Are there any decisions with 2+ Approvers? (Flag as governance risk)

---

## Power/Interest Matrix

**Manage closely (High power, High interest):**
- [Name] — What they need: [specific] — Cadence: [weekly 1:1 / bi-weekly brief]

**Keep satisfied (High power, Low interest):**
- [Name] — What they need: [specific] — Cadence: [monthly update / milestone alerts]

**Keep informed (Low power, High interest):**
- [Name] — Format: [Slack updates / shared doc / weekly email]

**Monitor (Low power, Low interest):**
- [Name] — Format: [Email at major milestones]

---

## Engagement Plan

**Pre-alignment sequence (before official review):**
1. [Stakeholder] — Topic: [what to align on] — By: [date]
2. [Stakeholder] — Topic: [what to align on] — By: [date]
3. [Stakeholder] — Topic: [what to align on] — By: [date]

**Communication cadence:**
| Stakeholder | Format | Frequency | Owner |
|---|---|---|---|
| [Name] | [1:1 / email / Slack] | [Weekly / Bi-weekly] | PM |

---

## Alignment Risks

| Risk | Stakeholder | What they need to feel | Mitigation |
|---|---|---|---|
| [Risk of blocking] | [Name] | [Respected / heard / in control] | [Specific action] |

**Worst-case scenario:** If [key stakeholder] does not align, the fallback is [action].

---

## Skeptic/Blocker Management

For each stakeholder classified as Skeptic or Blocker:
- **What is their underlying concern?** (Not their stated position — the deeper concern)
- **What evidence would address it?**
- **Who in the organization has influence with them?**
- **What's the escalation path if direct alignment fails?**
```

---

## Quality Gate

- Every stakeholder has a DACI role for at least one decision
- No decision has 2+ Approvers (governance red flag if it does)
- Power/interest classification completed for all named stakeholders
- Pre-alignment sequence is ordered (most important influencers first)
- Skeptics and Blockers have a named underlying concern (not just "they're resistant")
- Alignment risks have a named mitigation and a fallback
