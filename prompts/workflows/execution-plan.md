# Prompt: Execution Plan Builder

You are building a structured execution plan for an initiative. Your job is to convert a goal statement into a plan that is concrete enough to execute without ambiguity.

## Your Task

Given the initiative description below, produce a complete execution plan using the following structure.

---

## Output Requirements

**Goal** (1 sentence): State what done looks like. Must be observable — someone who wasn't in the planning meeting can verify it. Rewrite vague goals before proceeding. "Improve X" is not a goal. "X achieves [observable condition] by [date]" is.

**Not done until**: The explicit done condition. No ambiguity.

**Why This, Why Now** (2 sentences max): What would be lost by not doing this, or not doing it now?

**In Scope** (list): What this initiative explicitly covers.

**Out of Scope** (list): What this initiative explicitly does NOT cover. At least 2 items — anything ambiguous gets explicitly excluded.

**Assumptions** (list): What must be true for this plan to be valid. Name the load-bearing ones — these are what checkpoints will verify.

**Constraints**: Time (hard deadline vs. soft target), resources (what's available), external dependencies.

**Milestones** (2-5): Each milestone must have:
- A name
- An observable done condition (not just a phase name)
- A target date

**Success Criteria** (2-3): Observable outcomes that prove the goal was achieved. Not process criteria ("we completed the plan") — outcome criteria ("X is now able to do Y").

**Top 3 Risks**: Each risk needs: description, probability (H/M/L), impact (H/M/L), owner name, and one mitigation action.

---

## Quality Rules

- If the goal contains "improve," "work on," "continue," or "explore" without a measurable endpoint, rewrite it.
- If the done condition could only be assessed by the person who did the work, it's not a valid done condition — make it externally verifiable.
- If Out of Scope is empty, add at least the 2 most likely scope creep vectors.
- Risks without owners are not tracked risks — assign one or remove them.

---

## Initiative Input

{{INITIATIVE_DESCRIPTION}}
