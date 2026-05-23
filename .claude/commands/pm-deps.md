---
name: pm-deps
description: Map cross-team and external dependencies for an initiative. Produces a dependency log with owners, timelines, risk classification, and unblocking actions.
version: "1.0"
changed: 2026-05-20
---

# PM Dependencies

**Input:** Initiative name, known dependencies (cross-team, platform, data, external), and target timeline.

**Output:** Written to `notes/structured/deps-YYYY-MM-DD-<initiative-slug>.md` and appended to `execution/action-items.md` for at-risk dependencies.

---

## Steps

1. **Read context.** Load `decision-frameworks/pm/risk-radar.md` (execution risks section). If an execution audit for this initiative exists, read it.

2. **Run the dependency discovery checklist.** For each area:
   - **Platform / infrastructure:** Are we depending on any shared platform capability that another team owns?
   - **Data / analytics:** Does this initiative require data pipelines, models, or schemas owned by another team?
   - **Design:** Does design need to deliver assets before engineering starts? What is the design schedule?
   - **Legal / compliance / security:** Does this feature require legal review, security audit, or compliance sign-off?
   - **External / vendor:** Does this depend on a third-party API, vendor delivery, or partner integration?
   - **Cross-team features:** Does this initiative rely on a feature being built by another team?
   - **Content / localization:** Does this require content, copy, or translation that another team produces?

3. **For each dependency, assess:**
   - Who is the named owner (person, not team)?
   - What exactly is needed?
   - When does it need to be ready for us to start the work that depends on it?
   - Has the owner confirmed they can deliver by that date?
   - What is the risk level if it's late?

4. **Classify risk:**
   - **P0 (Critical path):** Initiative cannot launch without this. If late, launch slips.
   - **P1 (Significant):** Delays this dependency significantly reduces scope or quality.
   - **P2 (Minor):** Late delivery causes workaround; doesn't block launch.

5. **For all P0 and P1 dependencies not yet confirmed:** Generate an immediate action item — owner to confirm by a specific date.

6. **Identify the dependency that has the highest failure probability.** This is the risk to focus mitigation effort on.

7. **Write the output.**

---

## Output Format

```markdown
# Dependency Map — [Initiative Name] — [Date]

**Initiative:** [Name]  **Target launch:** [Date]  
**PM owner:** [name]

---

## Dependency Log

| ID | Dependency | What's needed | Owner | Needed by | Confirmed? | Risk |
|---|---|---|---|---|---|---|
| D-01 | [Platform / Data / Design / Legal / External] | [Specific deliverable] | [Name] | [Date] | Yes / No / TBD | P0/P1/P2 |
| D-02 | | | | | | |

---

## P0 Dependencies (Critical Path)

For each P0 dependency:

**[D-01] [Dependency name]**  
**Owner:** [Name] | **Needed by:** [Date] | **Confirmed:** [Yes/No]  
**What's needed:** [Specific — not "design" but "final Figma frames for the onboarding flow, all states"]  
**Current status:** [On track / At risk / Unknown]  
**Risk if late:** [What slips — specific]  
**Mitigation:** [What PM is doing to protect this dependency]  
**Contingency:** [What we do if this doesn't land — scope cut, date slip, alternative approach]

---

## P1 Dependencies (Significant)

[Same structure, abbreviated]

---

## Unconfirmed Dependencies (action required)

| Dependency | Owner | Action | Due |
|---|---|---|---|
| [D-xx] | [Name] | Confirm delivery by [date] | [ASAP date] |

---

## Dependency Risk Summary

**Highest-risk dependency:** [D-xx — why — probability × impact]  
**Most likely failure mode:** [Specific dependency that has the highest probability of missing its date]  
**Recommended mitigation focus:** [What PM should do this week to reduce dependency risk]

---

## Dependency Health (weekly update area)

| Date | D-01 | D-02 | D-03 | Overall |
|---|---|---|---|---|
| [YYYY-MM-DD] | ✓/⚠/✗ | | | |
```

---

## Quality Gate

- Every dependency has a named person (not a team) as owner
- Every P0 dependency has a confirmation status
- "What's needed" is specific enough to be deliverable (not "design support")
- Every P0 dependency has a contingency plan
- Unconfirmed P0/P1 dependencies have action items generated
- Highest-risk dependency is identified and a mitigation is named
