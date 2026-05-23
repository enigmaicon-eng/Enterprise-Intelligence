# Execution Rigor System
## Structured Execution, Operational Discipline, Delivery Quality

---

## Design Philosophy

Execution rigor is not process compliance — it is the practice of reducing ambiguity before work starts, surfacing drift during work, and capturing learning after work ends so the next cycle is faster and clearer.

Three anti-patterns this system is designed against:

1. **Process theater**: rituals that generate artifacts but don't change decisions.
2. **Bureaucratic tracking**: systems that cost more to maintain than the value they provide.
3. **Over-management**: reviewing and refining instead of doing.

Three principles this system is built on:

1. **Decompose until ownership is unambiguous.** A task is not decomposed until one person can say "I own the output and I know when it's done." Anything larger is a project, not a task.
2. **Reviews answer "what changes now?"** A review that ends with "keep going" and no changes was either premature or unnecessary.
3. **Checkpoints are gates, not ceremonies.** Every strategic checkpoint produces one of three outputs: continue (no changes needed), pivot (change approach), or stop (cancel the work). "Keep an eye on it" is not a checkpoint output.

---

## System Map

```
Intent / Initiative
        │
        ▼
exec-plan ──────────── Creates: execution-plan.md
        │               Covers: goal, constraints, milestones, risks, success criteria
        │
        ▼
exec-decompose ─────── Creates: task-decomposition.md  
        │               Covers: task tree, owners, dependencies, effort, acceptance
        │
        ▼
execution loop ─────── Daily: action-items.md + briefing
        │               Weekly: review-loop + exec-review
        │               Per-milestone: exec-checkpoint
        │
        ▼
exec-review ────────── Creates: inline review in deliverable or review note
        │               Covers: quality vs. criteria, gaps, what changes
        │
        ▼
exec-checkpoint ─────── Creates: checkpoint record in execution/checkpoints/
        │                Gate: continue | pivot | stop
        │
        ▼
exec-risk ──────────── Creates: risk entries in execution/risks/
        │               Covers: probability, impact, owner, trigger, mitigation
        │
        ▼
operational-retro ───── Monthly: `templates/operational-retro.md`
                        Updates: work-patterns.md, friction-points.md
```

---

## Execution State Files

Three lean files track execution state. Nothing is tracked that isn't read and acted on.

| File | Purpose | Updated |
|------|---------|---------|
| `execution/action-items.md` | Concrete tasks with owner, due date, status | Daily |
| `execution/active-initiatives.md` | In-flight initiatives with milestone status | Weekly |
| `execution/risks.md` | Active risks being tracked | Per risk event |

Closed action items are archived (not deleted) to `execution/archive/action-items-YYYY-MM.md` monthly.

---

## Decomposition Protocol

Work is decomposed at two levels:

**Level 1 — Initiative**: A cluster of work with a named outcome, owner, and deadline. Lives in `execution/active-initiatives.md`. Examples: "Implement KIS Phase 5", "Prepare Q3 strategy review."

**Level 2 — Task**: A unit of work completable in one session (≤4 hours). Has: action verb, single owner, verifiable done condition, due date. Lives in `execution/action-items.md`.

**Decomposition stops when:**
- Every task has an action verb at the start (Build, Write, Review, Decide, Define...)
- Every task has a done condition that isn't "make progress on"
- No task requires more than one person to complete
- Dependencies between tasks are explicit (Task B can't start until Task A is done)

**Anti-pattern**: Tasks like "Work on the roadmap" or "Continue API work." These are undecomposed — they have no done condition and no ownership boundary.

---

## Refinement Loop

Refinement is structured iteration on a specific output. It is not infinite polish.

Each refinement cycle answers:
1. **Against what criteria?** — Specify the quality bar before reviewing.
2. **What specifically is wrong?** — Not "it could be better" — name the gap.
3. **What change eliminates the gap?** — A concrete action, not a direction.
4. **When is done done?** — State the exit condition before starting the cycle.

Maximum refinement cycles per deliverable: 3 (unless explicitly extended). After 3 cycles, either ship or kill. Continued refinement past this point is usually criteria ambiguity, not quality deficit.

---

## Review Protocol

Reviews happen at three scopes:

| Scope | Trigger | Output | Tool |
|-------|---------|--------|------|
| Task review | Task marked complete | Verified done condition met | Manual or `/exec-review` |
| Milestone review | Milestone reached | Assessment of milestone quality, next milestone go/no-go | `/exec-checkpoint` |
| Initiative review | Monthly or on pivot signal | Continue/pivot/stop decision + lessons | `/exec-checkpoint` |

A review is not a review unless it produces a concrete output (verified, adjusted, or stopped).

---

## Strategic Checkpoint Protocol

Checkpoints are run at milestones or when a signal indicates the plan is drifting from reality. The output is always one of:

- **Continue**: Plan is on track. No changes to approach, resources, or timeline.
- **Pivot**: The approach needs to change. Specify what changes and why.
- **Stop**: The initiative should be cancelled or paused. Specify what triggered this and what happens to the work.

"Continue with caveats" is a pivot. "Stop and revisit" is a stop. Checkpoint outputs must be binary-adjacent — not narrative.

---

## Risk Surface Protocol

A risk is tracked when:
- Probability × Impact > threshold (use judgment: would this risk cause a pivot if it materialized?)
- There is a named owner who can act on it
- There is a specific trigger condition (not "if things go wrong")

A risk is not tracked when:
- It's a generic background risk that applies to everything
- There is no action the owner can take
- It's actually a dependency (dependencies live in `task-decomposition.md`, not the risk register)

Risks are reviewed weekly and closed (resolved, accepted, or converted to action item) within 30 days of opening.

---

## Prioritization Protocol

Operational prioritization uses three criteria — in this order:

1. **Commitment**: Is this committed to someone else? If yes, it ranks above uncommitted work.
2. **Leverage**: Does this unblock other work or compound forward? High leverage ranks above isolated work.
3. **Reversibility**: Is the cost of delaying this decision rising? Rising-cost delays rank above stable-cost work.

Do not use urgency as the primary criterion — urgency is often manufactured or poorly calibrated. Use commitment, leverage, and reversibility instead.

The output of prioritization is a **ranked list** — not a matrix, not a score, not a "tier." One list. First item is the highest priority. No ties.

---

## Operational Rituals Cadence

| Ritual | Trigger | Skill | Time Budget |
|--------|---------|-------|-------------|
| Daily orientation | Session start | `/briefing` | <2 min |
| Weekly execution review | Monday | `/exec-review` (weekly scope) | 15 min |
| Milestone checkpoint | Per milestone | `/exec-checkpoint` | 20 min |
| Monthly operational retro | Month end | `templates/operational-retro.md` | 30 min |
| Quarterly strategy checkpoint | Quarter end | `/exec-checkpoint` (strategic scope) | 45 min |

---

## Anti-Pattern Catalog (Execution-Specific)

| Anti-Pattern | Symptom | Fix |
|---|---|---|
| Zombie initiative | In `active-initiatives.md` for 60+ days with no progress | Force a checkpoint — continue or stop |
| Infinite refinement | 4+ review cycles on same deliverable | Name the acceptance criteria explicitly, then ship |
| Dependency fog | Tasks blocked without a named trigger condition | Every blocked task gets: "blocked by [task X], unblocked when [condition]" |
| Risk theater | Risk register with 20+ items, none actioned | Close all risks that can't be acted on; keep only what has an owner and a trigger |
| Prioritization paralysis | Can't pick top item because "everything is important" | Apply the three-criterion stack: commitment → leverage → reversibility. First matching item wins. |
| Checkpoint theater | Checkpoints that always produce "continue" with caveats | If the answer is always continue, checkpoints are happening too early or criteria are too vague |
