---
name: pm-roadmap
description: Convert a prioritized initiative list into a communicable roadmap narrative. Produces a time-horizon roadmap with strategic rationale, explicit trade-offs, and stakeholder-ready framing.
version: "1.0"
changed: 2026-05-20
---

# PM Roadmap

**Input:** List of prioritized initiatives (or reference to prioritization output), planning horizon (quarter/half/year), strategic context.

**Output:** Written to `strategy/monthly/YYYY-Q[N]-roadmap.md`

---

## Steps

1. **Read context.** Load `knowledge/pm/product-strategy.md` (three-horizon model). If a prioritization output or quarterly planning doc exists, read it first.

2. **Map initiatives to horizons:**
   - **H1 (Now — this quarter):** Execution confidence. Committed scope. These are being built.
   - **H2 (Next 1-3 quarters):** Directional bets. Validated direction but solution TBD. Confidence: medium.
   - **H3 (Later — 3+ quarters):** Strategic options. Problem space understood, timing uncertain.

3. **Identify the themes.** Group initiatives by strategic theme, not by team or functional area. Themes make the roadmap tell a story; team groupings make it a headcount document. Max 3 themes per horizon.

4. **Write the narrative for each theme.** Not a feature list — an explanation of: what user problem this addresses, why now, what position it advances. One paragraph per theme.

5. **Write the explicit trade-off section.** Name the 3 most significant things NOT on the roadmap and why. This is the hardest and most important part — it demonstrates the roadmap reflects real choices.

6. **Write the confidence-calibrated language.** H1 items use committed language ("we will"). H2 items use directional language ("we plan to"). H3 items use exploratory language ("we're exploring"). Mixing the registers misleads stakeholders.

7. **Add the measurement layer.** For each H1 initiative: the leading indicator that will tell us it's working. For H2 bets: the kill condition.

8. **Write the output.**

---

## Output Format

```markdown
# Roadmap — [Product/Team] — [Quarter/Period]

**Strategy context:** [One sentence — what market moment this roadmap is responding to]  
**Owner:** [PM]  **Updated:** YYYY-MM-DD

---

## Now (H1 — Q[N] YYYY): Delivering on [Theme]

**Theme 1: [Name]**  
[One paragraph: what problem, for whom, why now, what position this advances]

Initiatives:
- [Initiative] — [Confidence: committed] — [Success indicator]
- [Initiative] — [Confidence: committed] — [Success indicator]

**Theme 2: [Name]**  
[Same structure]

---

## Next (H2 — [Period]): Betting on [Direction]

**Theme 3: [Name]**  
[One paragraph: what bet, what assumption, what would confirm direction]

Initiatives:
- [Initiative] — [Confidence: directional] — [Kill condition]
- [Initiative] — [Confidence: directional] — [Kill condition]

---

## Later (H3 — [Period+]): Options We're Holding

- [Problem space] — [Why we're tracking it but not committing yet]
- [Problem space] — [What would accelerate this to H2]

---

## What's NOT on This Roadmap (and Why)

- **[Item]:** [Why excluded — wrong timing / insufficient evidence / resource constraint / strategic deprioritization]
- **[Item]:** [Why excluded]
- **[Item]:** [Why excluded]

---

## Risks to This Roadmap

| Risk | Impact | Mitigation |
|---|---|---|
| [Risk] | H1 timeline | [Action] |
| [Risk] | H2 direction | [Action] |

---

## Roadmap Assumptions

The H2 direction assumes:
1. [Assumption] — we'll know by [date] if this holds
2. [Assumption] — we'll know by [date] if this holds
```

---

## Quality Gate

- Initiatives are grouped by strategic theme, not by team
- H1 uses committed language; H2 directional; H3 exploratory (no mixed registers)
- "Not on the roadmap" section has ≥3 explicit items with rationale
- Each H2 bet has a kill condition
- Each H1 initiative has a success indicator (leading metric)
- Roadmap assumptions are named (the bets the roadmap is making)
