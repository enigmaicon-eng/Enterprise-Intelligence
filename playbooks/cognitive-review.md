# Monthly Cognitive Review Playbook

## Purpose
A structured monthly ritual that runs across all four cognitive acceleration layers: recall testing, misconception detection, cross-domain synthesis, and decision quality review. One session, ~60-90 minutes. Produces concrete updates to the knowledge base — not a reflection exercise.

## When to Run
First of each month, or within 3 days of it. Do not run more than once per month — the value compounds with spaced intervals, not frequency.

## Pre-Session Setup
Before starting:
1. Read `memory/MEMORY.md` — orient to what's active
2. Read `execution/active-initiatives.md` — know what's in flight
3. Read `strategy/active-bets.md` — know what bets are live
4. Note today's date. You'll update `reviewed:` fields in knowledge entries as you go.

---

## Phase 1: Recall Testing (15-20 min)

**Goal:** Identify encoding gaps across the knowledge base.

**Step 1:** Open `knowledge/KNOWLEDGE-INDEX.md`. Find the 3 entries with the oldest `reviewed` date in any domain marked `confidence: high`. These are the highest-risk entries — high confidence, not recently verified.

**Step 2:** For each: run `/recall-test [entry path]`. One at a time. Do not run all three simultaneously.

**Step 3:** For each result:
- If PASS (all match): update `reviewed:` to today's date
- If gaps: note the specific delta. Re-read only the delta section.
- If errors: flag for misconception check in Phase 2.

**Output:** List of entries tested, results, and any entries escalated to Phase 2.

---

## Phase 2: Misconception Detection (15-20 min)

**Goal:** Surface structural flaws in the knowledge base before they contaminate decisions.

**Step 1:** Run `/misconception` on:
- Any entry that produced errors in Phase 1
- Any entry in `knowledge/technical/` with `reviewed:` >60 days (technical knowledge ages fast)
- Any entry in `knowledge/strategy/` that has been cited in a recent bet or decision

**Step 2:** For each P0 finding: draft the correction immediately. For P1/P2: log to a running fix list.

**Step 3:** Apply P0 corrections now. Apply P1 corrections before next use. Update `reviewed:` fields.

**Output:** List of findings by severity. P0 corrections applied. P1 fix list written to `notes/raw/` as a capture for follow-up.

---

## Phase 3: Cross-Domain Synthesis (15-20 min)

**Goal:** Surface connections not yet documented. The knowledge base compounds when links are explicit.

**Step 1:** Run `/insight` with no argument. Let it select the highest-density opportunity from the current state of the knowledge base.

**Step 2:** Review each qualifying insight against the specificity/non-obviousness/actionability criteria. Accept only those that pass all three.

**Step 3:** Route accepted insights:
- New pattern → write via `/pattern`
- Cross-domain connection → add to `KNOWLEDGE-INDEX.md` cross-domain table
- Confirms existing pattern → add evidence citation to `knowledge/patterns/index.md`

**Step 4:** Check `knowledge/patterns/index.md` for any patterns with zero evidence links. A pattern with no evidence is a hypothesis, not a pattern. Mark it explicitly or remove it.

**Output:** Number of new connections documented. Pattern library update status.

---

## Phase 4: Decision Quality Review (15-20 min)

**Goal:** Extract judgment rules from the last 30 days of decisions and bets.

**Step 1:** Run `/decision-review` with no argument. It will pull the most recent entries from `decision-frameworks/decisions-log.md` and `strategy/bet-log.md`.

**Step 2:** For each extracted judgment rule: check against `knowledge/decisions/decision-patterns.md`. Add, extend, or flag contradictions.

**Step 3:** Check `strategy/active-bets.md`. For each active bet:
- Is the kill condition still specific (metric + threshold + date)?
- Has any evidence arrived since the last review that should update the evidence log?
- Is the horizon (H1/H2/H3) still correct?

**Output:** Judgment rules extracted. Decision-patterns.md updated. Active bets reviewed.

---

## Phase 5: Architecture Consistency (10 min, optional)

**Run only if:** A new system phase was completed in the last 30 days, or any architecture document was modified.

**Step 1:** Run `/arch-critique [most recently modified architecture doc]`.

**Step 2:** For P0 findings: fix immediately. For P1: add to backlog.

---

## Session Close

After all phases:

1. Update `knowledge/KNOWLEDGE-INDEX.md` — update all `reviewed:` dates touched in this session
2. Check if any domain now has 3+ entries without a cluster: if yes, flag for `/synthesize` cluster creation in next session
3. Write a 3-line session note to `reviews/monthly/[YYYY-MM]-cognitive.md`:
   - Entries tested and results
   - Biggest misconception finding
   - Biggest insight extracted

---

## Anti-patterns to Avoid

| Anti-pattern | Description | Prevention |
|---|---|---|
| Review theater | Going through motions without generating error signal | Every phase must produce a concrete output or finding |
| Exhaustion cascade | All phases in one sitting when tired | Stop after Phase 2 if cognitively depleted; resume next day |
| Selective confidence | Only testing entries you're already confident in | Prioritize by oldest reviewed date, not by comfort |
| Insight hoarding | Noting connections without routing them | Every accepted insight is routed in the same session |
| Correction deferral | Flagging P0 findings but not fixing them | P0 = fix now. No exceptions. |
