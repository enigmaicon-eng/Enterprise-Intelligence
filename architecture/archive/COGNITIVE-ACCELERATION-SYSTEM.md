# Cognitive Acceleration System
## P10 Master Architecture

---

## Purpose

This system accelerates the rate at which understanding compounds — not by adding more content, but by surfacing gaps, stress-testing existing knowledge, and forcing synthesis across domains. Every workflow in this system operates against the live knowledge base, not in the abstract.

**Design constraints:**
- No tutorial theater. No simulated teaching sessions.
- No gamification. No streaks, scores, or artificial feedback loops.
- No question chains. Constraint-based challenges only.
- No cognitive exhaustion. One focused workflow at a time.
- No AI tutor simulation. Claude acts as diagnostic instrument, not instructor.

---

## 18 Subsystems

| # | Subsystem | Primary Output | Skill |
|---|-----------|---------------|-------|
| 1 | Socratic Reasoning | Stress-tested belief | `/think` |
| 2 | Misconception Detection | Gap/error diagnosis | `/misconception` |
| 3 | Active Recall | Reconstructed knowledge | `/recall-test` |
| 4 | Architecture Critique | Applied principle check | `/arch-critique` |
| 5 | Decision Quality Review | Retrospective pattern | `/decision-review` |
| 6 | Strategic Insight Accumulation | Cross-domain insight | `/insight` |
| 7 | Guided Debugging | Systematic fault isolation | `/debug-ai` (P9) |
| 8 | Repository Synthesis | Structural intelligence | `/repo-learn` (P5) |
| 9 | Systems Learning | Causal/feedback map | Direct knowledge work |
| 10 | Technical Fluency Acceleration | Applied understanding | `/arch-critique` + `/think` |
| 11 | Long-term Reinforcement | Compounding pattern | Monthly cognitive review |
| 12 | Cognitive Synthesis | Multi-source synthesis | `/synthesize` + `/insight` |
| 13 | Memory Reinforcement | Decay-resistant recall | `/recall-test` |
| 14 | Concept Relationship Mapping | Knowledge graph update | `/pattern` (P5) |
| 15 | Strategic Insight Accumulation | Bet-to-principle extraction | `/insight` |
| 16 | Pattern Recognition | Cross-domain signal | `/pattern` (P5) |
| 17 | AI Systems Reasoning Review | Production mental model | `/prod-review` (P9) |
| 18 | Decision Quality Review | Judgment calibration | `/decision-review` |

---

## Learning Sequence

Cognitive acceleration follows a defined sequence. Do not skip layers.

```
Layer 0: Foundation (what is known?)
  → Read knowledge entries, verify coverage
  → Run /recall-test on any domain with recent additions

Layer 1: Stress-test (what breaks under pressure?)
  → Run /think on any high-confidence belief
  → Run /misconception on recently written knowledge files

Layer 2: Application (does it hold against real systems?)
  → Run /arch-critique against live architecture docs
  → Run /decision-review against decisions-log.md entries

Layer 3: Synthesis (what connects across domains?)
  → Run /insight after completing a domain cluster
  → Update knowledge/patterns/index.md with new cross-domain links

Layer 4: Reinforcement (does it stick over time?)
  → Monthly cognitive review (playbooks/cognitive-review.md)
  → Run /recall-test on any entry not reviewed in 30+ days
```

---

## Workflow Design Principles

### Socratic = Constraint, Not Question Chain
The `/think` skill applies pressure through constraints, not interrogation. A constraint-based challenge forces work: "Defend the claim that X is true using only evidence from [specific file]. No analogies." This produces stress-tested reasoning without a back-and-forth tutoring session.

### Active Recall = File-Based Elaborative Retrieval
The `/recall-test` skill works by having the user reconstruct from memory, then comparing against the source file. The comparison is the learning event — not the reconstruction itself. Comparing creates the error signal; error signal drives encoding.

### Misconception Detection = Internal Consistency Check
The `/misconception` skill reads knowledge files and flags: overconfident claims (stated as fact without qualification), logical gaps (conclusion doesn't follow from premises), stale entries (reviewed date >90 days with rapidly-changing domain), circular definitions (term defined using itself), and unverified analogies (cross-domain comparison without stated basis).

### Architecture Critique = Applied Principle Check
The `/arch-critique` skill loads a target architecture file and checks it against principles stated in existing knowledge entries and architecture docs. It does not assess against an external ideal — it checks for internal consistency and gap coverage.

### Decision Review = Against Real Entries
The `/decision-review` skill reads actual entries from `decision-frameworks/decisions-log.md` and `strategy/bets/`. It identifies patterns across closed decisions, not generic retrospective questions.

### Insight = Cross-Domain Extraction
The `/insight` skill reads across clusters and extracts connections not yet explicitly documented in `knowledge/patterns/index.md`. Output is either a new pattern entry (via `/pattern`) or an update to an existing cross-domain connection in `KNOWLEDGE-INDEX.md`.

---

## Failure Modes to Detect and Prevent

| Failure Mode | Signal | Prevention |
|---|---|---|
| Tutorial theater | Multi-turn Q&A, role-play teaching | Constraint-based challenges; single output deliverable |
| Recall rote drilling | Repeating stored text | Elaborative comparison against source; error-signal focus |
| Misconception accumulation | High-confidence entries not reviewed | `/misconception` on entries >90 days old |
| Synthesis shallowness | Pattern lists without causal mechanism | Require mechanism statement in every insight |
| Architecture critique without evidence | "This design seems off" | Every critique must cite a principle from knowledge files |
| Decision review as autopsy | Documenting what happened, no pattern | Every review must extract a judgment rule |
| Cognitive exhaustion | Multiple cycles in one session | Max one deep workflow per session |

---

## Integration with Existing Systems

| Existing System | Integration Point |
|---|---|
| Knowledge Intelligence (P5) | `/recall-test` loads from knowledge/; `/insight` outputs to knowledge/patterns/ |
| Execution Rigor (P6) | `/decision-review` reads execution/checkpoints/ and decisions-log.md |
| Strategic Intelligence (P7) | `/insight` reads strategy/bets/ for bet-to-principle extraction |
| Context Engineering (P8) | `/arch-critique` checks against architecture/ docs |
| Production AI Learning (P9) | `/arch-critique` checks deployment patterns; `/think` stress-tests reliability claims |

---

## Review Cadence

| Ritual | Trigger | Workflow |
|---|---|---|
| Post-learning recall check | Within 48h of any `/learn` invocation | `/recall-test` on the new entry |
| Knowledge file consistency check | Weekly or on `/weekly` | `/misconception` on any knowledge/ entry |
| Cross-domain insight extraction | After 3+ entries in same domain | `/insight` across that domain |
| Monthly cognitive review | First of month | `playbooks/cognitive-review.md` |
| Architecture consistency audit | After any major system build | `/arch-critique` on relevant architecture docs |
| Decision pattern extraction | After any bet closes or decision logged | `/decision-review` on recent entries |

---

## File Map

```
architecture/
  COGNITIVE-ACCELERATION-SYSTEM.md     ← this file

knowledge/systems/
  reasoning-quality.md
  learning-science.md
  misconception-patterns.md
  systems-thinking.md
  pattern-recognition.md

.claude/commands/
  think.md
  misconception.md
  recall-test.md
  arch-critique.md
  decision-review.md
  insight.md

playbooks/
  cognitive-review.md
  misconception-detection.md

prompts/cognitive/
  socratic.md
  synthesis.md
  misconception.md
  recall.md
  architecture.md
  decision-quality.md

learning/
  COGNITIVE-ACCELERATION-PATH.md
```
