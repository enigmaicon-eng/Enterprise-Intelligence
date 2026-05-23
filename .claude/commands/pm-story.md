---
name: pm-story
description: Generate user stories with acceptance criteria from a feature or problem description. Applies INVEST criteria and JTBD framing. Produces sprint-ready stories.
version: "1.0"
changed: 2026-05-20
---

# PM Story

**Input:** Feature or problem description, target persona, any known constraints or edge cases.

**Output:** Displayed in terminal. Optionally appended to a sprint backlog file if specified.

---

## Steps

1. **Read context.** Load `knowledge/pm/writing-standards.md` (user story and AC section).

2. **Identify the persona precisely.** "User" is not a persona. Extract or ask for: role, context, specific situation. The story's quality is directly proportional to the persona's specificity.

3. **Apply the JTBD abstraction test.** For the stated goal: is it at the right level?
   - Too concrete: "As a user, I want a button to export PDF" — this is an implementation, not a job
   - Too abstract: "As a user, I want to manage my projects" — this could be 50 different stories
   - Right level: "As a project lead, I want to share a formatted summary of this week's progress with my team without reformatting it manually"

4. **Write the story.** As a [specific persona] / I want to [accomplish goal] / So that [underlying value].

5. **Apply INVEST check:**
   - Independent: can this be built and demoed without other stories?
   - Negotiable: is scope negotiable within the intent?
   - Valuable: does it deliver observable value to the user on its own?
   - Estimable: would an engineer be able to estimate this?
   - Small: completable in a single sprint?
   - Testable: can acceptance criteria be written?
   - If any fail: split the story or reframe it.

6. **Write acceptance criteria.** Given/When/Then format. Cover:
   - Happy path (primary success scenario)
   - Edge case 1: empty state / no data
   - Edge case 2: error or failure condition
   - Edge case 3: boundary condition or concurrent state
   - Performance criterion (if relevant)

7. **Flag any assumptions baked into the story.** These are [ASSUMPTION] markers — things the story assumes true that haven't been validated.

8. **Produce output.**

---

## Output Format

```markdown
## Story: [Short descriptive title]

**Persona:** [Specific user — role + context]
**Epic:** [Parent epic or initiative, if applicable]
**Priority:** P0 | P1 | P2

---

**As a** [specific persona in specific context],  
**I want to** [accomplish a specific goal],  
**So that** [the underlying value this creates for them].

---

### Acceptance Criteria

**Happy path:**
- Given [user is in this context]
- When [user takes this action]
- Then [observable system behavior]
- And [additional observable behavior]

**Edge case — empty state:**
- Given [no data exists]
- When [user takes the action]
- Then [graceful handling]

**Edge case — error condition:**
- Given [system error or bad input]
- When [user takes the action]
- Then [informative error with recovery path]

**Edge case — boundary:**
- Given [boundary condition: max values, concurrent actions, etc.]
- When [action]
- Then [behavior]

**Performance (if applicable):**
- The [action] completes in under [N]ms at p95 under normal load

---

### Out of Scope for This Story
- [What this story explicitly does NOT cover]

### Assumptions
- [ASSUMPTION] [What this story assumes to be true]

### Dependencies
- [What must be completed before this story can begin]
```

---

## Quality Gate

- Persona is specific (role + context, not just "user")
- "So that" clause states the underlying value (JTBD level, not feature level)
- INVEST criteria checked — story would pass all 6
- At minimum 4 acceptance criteria: happy path + 2 edge cases
- All criteria are testable without subjective interpretation
- Out of scope section is populated (even if just one item)
- No technical implementation prescribed in the story or AC
