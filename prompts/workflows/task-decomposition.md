# Prompt: Task Decomposition

You are decomposing a milestone into a concrete task register. Every task in your output must be executable without asking for clarification.

## Your Task

Given the milestone description and execution plan context below, decompose the milestone into tasks using the following rules.

---

## Decomposition Rules

**A task is valid if and only if:**
1. It starts with an action verb (Build, Write, Review, Decide, Define, Test, Deploy, Draft, Map, Research, Configure, Validate...)
2. One person can own it entirely — not a team, one person
3. Done can be assessed by someone who wasn't working on it
4. It can be completed in under 4 hours
5. Its dependencies are explicit (either "none" or "depends on T[NN]")

**If a candidate task fails rule 4**, decompose it further before including it.

**If a candidate task fails rule 3**, rewrite the done condition until it's externally verifiable.

---

## Output Requirements

**Dependency Graph** (ASCII): Show task order visually. Mark the critical path.

**Task Register**: For each task:
- ID: T[NN]
- Action: [Verb + specific object]
- Owner: [single name]
- Done when: [externally verifiable condition]
- Effort: [hours estimate]
- Depends on: [T[NN] or none]
- Risk flag: [yes/no — flag if: novel approach, external dependency, effort > 3h, verification is hard]

**Blocked Tasks**: Tasks that can't start because of an external dependency. Include the specific unblock condition.

**Critical Path**: The longest sequence of dependent tasks. This is the minimum time to complete the milestone.

**Decomposition Health Check**: Before finalizing, confirm:
- [ ] Every task starts with an action verb
- [ ] Every task has a single named owner
- [ ] Every task has an observable done condition
- [ ] All dependencies are named
- [ ] No task is estimated at more than 4 hours
- [ ] Critical path is identified

---

## Milestone Input

**Milestone**: {{MILESTONE_NAME}}
**Done condition**: {{MILESTONE_DONE_CONDITION}}
**Execution plan context**: {{PLAN_ASSUMPTIONS_AND_CONSTRAINTS}}
