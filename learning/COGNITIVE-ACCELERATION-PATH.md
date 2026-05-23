# Cognitive Acceleration Learning Path
## P10 — 5-Level Path to Operational Reasoning Maturity

---

## Overview

This path builds the practices that turn knowledge accumulation into compounding understanding. It is not a reading list. It is a set of exercises that generate prediction error — the mechanism behind durable learning.

Time investment: 2-4 weeks to complete all levels. One level per week is the right pace.

---

## Level 1: Foundation Orientation

**Goal:** Understand how the cognitive acceleration system works and run your first recall test.

**Activities:**
1. Read `architecture/COGNITIVE-ACCELERATION-SYSTEM.md` — understand the 4-layer sequence and the constraint-based philosophy
2. Read `knowledge/systems/learning-science.md` — understand why retrieval beats re-reading
3. Run `/recall-test` on any one knowledge entry you wrote in the last 7 days

**Completion criteria:**
- You can state the 4-layer cognitive sequence from memory: Foundation → Stress-test → Application → Synthesis → Reinforcement
- You've completed one recall test and identified at least one encoding gap
- You understand the distinction between retrieval practice and re-reading

---

## Level 2: Stress-Testing Beliefs

**Goal:** Apply constraint-based challenges to existing beliefs. Surface borrowed confidence.

**Activities:**
1. Read `knowledge/systems/reasoning-quality.md` — internalize the 6 reasoning failure modes
2. Read `knowledge/systems/misconception-patterns.md` — learn all 7 misconception classes
3. Run `/think` on a claim you hold with high confidence in any domain
4. Run `/misconception` on a knowledge entry you haven't reviewed in 30+ days

**Completion criteria:**
- You've run `/think` and received a BREAKS verdict at least once — a held belief didn't survive the constraint
- You've found at least one P1 or P0 misconception in the knowledge base
- You can distinguish between the 7 misconception classes by detection signal

---

## Level 3: Applied Architecture Critique

**Goal:** Check real architecture documents against real principles. Develop architectural intuition grounded in evidence.

**Activities:**
1. Read `knowledge/systems/systems-thinking.md` — particularly leverage points and archetypes
2. Run `/arch-critique architecture/CONTEXT-ENGINEERING-SYSTEM.md` — critique a known system
3. Run `/arch-critique` on any architecture document from a phase you built
4. For any P1+ finding: trace it to the specific principle it violates

**Completion criteria:**
- You've completed two architecture critiques and produced finding reports
- At least one finding was non-obvious (it surprised you)
- You can apply Meadows' leverage point hierarchy to classify an intervention level

---

## Level 4: Cross-Domain Synthesis

**Goal:** Extract connections that aren't yet documented. Build the pattern library.

**Activities:**
1. Read `knowledge/patterns/index.md` — understand what's already there
2. Run `/insight` with no argument — let it find the highest-density opportunity
3. If `/insight` produces a qualifying insight: route it (via `/pattern` or KNOWLEDGE-INDEX.md update)
4. Run `/decision-review` on any 3 decisions from `decision-frameworks/decisions-log.md`

**Completion criteria:**
- You've added at least one new entry to `knowledge/patterns/index.md` or KNOWLEDGE-INDEX.md cross-domain connections
- You've run `/decision-review` and extracted at least one judgment rule
- The judgment rule was checked against `knowledge/decisions/decision-patterns.md` and either confirmed, extended, or added

---

## Level 5: Monthly Review Cadence

**Goal:** Complete a full monthly cognitive review. This is the capstone — all prior levels synthesized into one session.

**Activities:**
1. Read `playbooks/cognitive-review.md` — understand all 5 phases
2. Run the full monthly cognitive review (all 4 required phases + Phase 5 if applicable)
3. Write the 3-line session note to `reviews/monthly/[YYYY-MM]-cognitive.md`
4. Set a reminder for the following month

**Completion criteria:**
- All 4 phases completed in one session
- At least one knowledge entry updated (corrected or re-dated)
- At least one insight routed to patterns or cross-domain connections
- Session note written

---

## After Level 5: Ongoing Practice

The learning path ends; the practice continues. Monthly cognitive review is the core ritual.

Additional practices to layer in over time:
- **Post-learn recall** (automated): every new `/learn` invocation should be followed by `/recall-test` within 48h
- **Post-bet recall**: every closed bet → `/decision-review` → judgment rule within 7 days
- **Quarterly architecture pass**: `/arch-critique` on all architecture documents once per quarter
- **Misconception sweep**: `/misconception` on all high-confidence entries once per quarter

---

## Anti-patterns That Slow Progress

| Anti-pattern | Why It Fails | Correction |
|---|---|---|
| Completing levels without error signals | Going through motions; no encoding | Require at least one BREAKS or WRONG result before advancing |
| Skipping recall in favor of re-reading | Re-reading is comfortable but low-yield | Replace all "review" with recall test → comparison |
| Running insights before completing recall | Synthesis without solid foundation compounds errors | Level 1 and 2 first, every time |
| Monthly review as writing exercise | Producing outputs without generating error signals | Every phase needs a finding or a confirmed pass — not just words |
