# Prompt Failure Analysis Playbook
## Systematic investigation of prompt-level AI failures

Use this when you've confirmed the failure is Class 1 (prompt failure) via isolation test. This playbook identifies the specific root cause within the prompt and produces a minimum fix.

---

## The Four Prompt Failure Sub-Types

Every prompt failure falls into one of four categories. Identify the sub-type before writing any fix. A wrong sub-type diagnosis produces a wrong fix.

| Sub-type | What it means | How to recognize it |
|---------|--------------|---------------------|
| **Scope** | Prompt doesn't specify what to include or exclude | Output has wrong breadth: too broad, too narrow, or drifts into adjacent topics |
| **Format** | Output format not specified precisely enough | Multiple runs produce different structural formats; sections appear/disappear |
| **Instruction** | Instructions are ambiguous or contradictory | Model follows one reading; another reading would produce correct output |
| **Ambiguity** | Prompt can be interpreted multiple valid ways | Output is internally consistent but consistently wrong in the same way |

---

## Protocol

### Step 1: Read the prompt with fresh eyes (3 min)

Before reading the failing output, read the prompt as if you've never seen it. Ask:

- What is this prompt asking the model to do?
- What is it NOT saying? (What has to be inferred?)
- If I were the model, which parts would I be uncertain about?

Write your answers. Don't continue until you've done this.

### Step 2: Apply the scope probe

Read the prompt's task description. Then ask:

> "Given only this prompt, what content should definitely be included? What should definitely be excluded?"

If the answer to either question is "I'm not sure" — that's a scope failure. The prompt doesn't specify the boundary.

**Scope probe signals:**
- Output is longer than expected (scope too broad)
- Output is shorter than expected (scope too narrow)
- Output includes content from adjacent tasks ("also addressing..." — the model padded)
- Output misses a section that should obviously be there

**Common scope fixes:**
- Add explicit include: "Include only [X, Y, Z]"
- Add explicit exclude: "Do not include [A, B]"
- Specify the depth: "For each item, include: [specific fields]"
- Specify the length target: "Output should be 3-5 bullet points per section"

### Step 3: Apply the format probe

Read the output schema (if any) in the prompt. Then ask:

> "Is every structural element of the expected output explicitly defined? Or does some of it have to be inferred from context?"

If any structural element has to be inferred: format failure.

**Format probe signals:**
- Different runs produce different section orders
- Section names vary across runs ("Action Items" vs. "Actions" vs. "Next Steps")
- Output has wrong nesting level (flat when hierarchical expected, or vice versa)
- Output has wrong field types (prose when list expected)

**Common format fixes:**
- Add explicit section names with headers: `### Action Items`
- Add example output structure (2-3 lines of example, not full example)
- Add format constraint per field: "Each action item must be: [Action verb] + [Owner] + [Date]"
- Add a "format exactly as:" note that shows the target schema

### Step 4: Apply the instruction probe

Read every instruction in the prompt. For each:

> "Can this instruction be read two valid ways? What output would each reading produce?"

If any instruction has two readings: instruction failure.

**Instruction probe signals:**
- Output is consistently wrong in the same predictable way (one reading dominates)
- Fixing the output manually would require reading a different interpretation of the instruction
- The model seems to have "chosen" one of two valid interpretations

**Common instruction ambiguities:**
- "Be concise" (concise for what audience? compared to what?)
- "Summarize the meeting" (all topics? only decisions? only action items?)
- "Use a professional tone" (formal? casual-professional? technical?)
- "Include key points" (key = most important? most frequent? most impactful?)
- "Analyze X" (describe X? evaluate X? compare X to alternatives? diagnose X?)

**Fix:** Replace ambiguous instruction with specific constraint:
- "Be concise" → "Each section should be 2-4 sentences. No more."
- "Summarize the meeting" → "Extract: (1) decisions made, (2) action items with owners, (3) open questions"
- "Analyze X" → "For X: state what it is, what changed, what caused the change, and what action is recommended"

### Step 5: Check for instruction conflicts

Read all instructions together. Look for:

> "Is there any pair of instructions that would pull the output in different directions?"

**Common conflicts:**
- "Be thorough" + "Be concise" (can't be both without defining the scope)
- "Include all context" + "Keep under 500 tokens"
- "Be prescriptive" + "Present options for the user to choose from"
- "Format as JSON" + "Write in natural language"

**Fix:** For conflicting instructions, establish priority:
- "Be thorough on [X dimension], concise on [Y dimension]"
- "Include all context up to 500 tokens; after that, summarize"
- Resolution rule: when instructions conflict, [higher-priority instruction] takes precedence

### Step 6: Write the minimum fix

The minimum fix is the smallest change to the prompt that addresses the identified root cause.

**Do not:**
- Rewrite the entire prompt
- Add 5 new constraints when one precise constraint is sufficient
- Add defensive language for failure modes that haven't occurred
- Add examples when a precise specification would suffice

**Do:**
- Add one clear sentence per identified issue
- Be specific (not "be precise" but "include the exact file path")
- Test the fix against the original failing case before concluding

### Step 7: Version and test

1. Update the prompt file with the fix
2. Bump version in PROMPT-REGISTRY.md
3. Run `/eval` on the output produced with the new prompt
4. Confirm: does the originally failing dimension now pass?
5. Confirm: do the previously passing dimensions still pass? (regression check)

---

## Prompt Analysis Reference: Red Flags

These patterns in a prompt reliably produce failures:

| Pattern | Why it fails | Fix |
|---------|-------------|-----|
| "Summarize" without scope | Model decides what's worth summarizing | Specify: what elements to extract |
| "As appropriate" | Model decides what's appropriate | Specify the condition |
| "If relevant, include..." | Model decides relevance | Always include, or don't |
| "Be brief" | Relative term; means different things | Specify token count or section length |
| Multiple conflicting lengths | "Detailed" section + "brief" overall | Resolve: which takes precedence? |
| Implicit output format | Format described in example (brittle) | Format described as constraints (robust) |
| No "do not include" clause | Model fills gaps with plausible content | Specify what stays out |
| "Etc." in examples | Model invents what "etc." means | List completely or add "only these items" |
| "Your judgment" | Fine for Opus; problematic for Haiku/Sonnet | Specify the decision criteria instead |

---

## Prompt Failure Pattern Library

Document recurring failure patterns here as they're found:

**Pattern: Missing exclusion clause in debrief prompts**
The debrief prompt extracts action items but doesn't exclude discussion points. Model includes discussion as "implicit actions."
Fix: "Action items only: explicit tasks with a clear owner. Do not include discussion points, observations, or open questions in the action items section."

**Pattern: Format drift in structured outputs**
Skill prompts that say "Output as: [description]" instead of "Output exactly as: [template]" produce format variation.
Fix: Replace prose format descriptions with structural templates showing exact headers and field names.

---
*Add new patterns as they're discovered. One pattern per incident. Include the specific fix.*
