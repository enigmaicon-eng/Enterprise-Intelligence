# AI Debugging Playbook
## Systematic protocol for diagnosing AI system failures

**Read before every debugging session.** The protocol works. Skipping steps wastes time.

---

## Before You Start

Write this down, literally:

> "The failure is: [output description]. I think it's a [Class X] failure because [detection signal]."

If you can't write that sentence, you're not ready to debug yet. Read one more output, read the telemetry, then write it.

---

## Step 1: Classify the Failure (2 min)

Match the symptoms to the failure class:

| What you see | Most likely class |
|-------------|-----------------|
| Wrong format (prose when JSON expected, missing sections) | Class 1: Prompt |
| Correct format, factually wrong content | Class 2: Context |
| Correct format, factually correct, but shallow/superficial | Class 3: Model |
| Empty response, timeout, truncated output | Class 4: Infrastructure |
| Inconsistent format across identical inputs | Class 1: Prompt |
| Claims something not in the source material | Class 2: Context |
| Fails to synthesize; lists but doesn't analyze | Class 3: Model |
| `completion_reason: max_tokens` in telemetry | Class 4: Infrastructure |

Commit to a class. Write it down. You can revise if the isolation test fails.

---

## Step 2: Read Telemetry (3 min)

**Always check this first.** Telemetry tells you immediately if it's infrastructure. If it's infrastructure, you don't need to debug the prompt.

Open `telemetry/api-log.jsonl`. Find the relevant session (grep by timestamp or session_id).

Check:
- `status`: anything other than "success"?
- `completion_reason`: "max_tokens" = truncated output
- `latency_ms`: > 2× typical for this workflow?
- `cached_tokens`: 0 when it shouldn't be?
- Any HTTP error codes logged?

**If yes to any:** Infrastructure failure. Jump to the Infrastructure Playbook section below.
**If no:** Continue.

---

## Step 3: Isolation Test (5 min)

**One test per class. Run the test for your suspected class first.**

**Test for Class 1 (Prompt):**
Take the same prompt. Replace the actual context with 2-3 sentences of simple, factually clear content you've written yourself. Run it.
- Still fails → Prompt failure confirmed
- Fixed → It was context, not prompt. Re-classify as Class 2.

**Test for Class 2 (Context):**
Take the same prompt. Add the information you think was missing directly, inline (don't use retrieval). Run it.
- Fixed → Context failure confirmed (retrieval was the issue)
- Still fails → It wasn't missing context. Re-classify as Class 1 or 3.

**Test for Class 3 (Model):**
Run the exact same prompt + context on Sonnet if you were using Haiku, or Opus if you were using Sonnet.
- Significantly better output → Model failure (tier too low)
- Same quality → Not a model issue. Re-classify.

---

## Step 4: Root Cause by Class

### Class 1 — Prompt Root Cause

Read the failing prompt slowly. Apply:

**Scope probe:** "If I were a model reading this, what exactly am I supposed to include?" If the answer is "it's unclear" — that's the bug.

**Format probe:** "Is the exact output format specified? With exact section names?" If any section has to be inferred, that's the bug.

**Instruction probe:** "Are there any instructions that can be read two ways?" If yes, that's the bug. Find both readings; the one that produces the bad output is the one the model is taking.

**Common prompt root causes:**
- Missing "do not include" clause (model adds unrequested content)
- Output format described in prose instead of showing the schema
- "Be concise" without specifying what concise means
- No explicit instruction for what to do when information is missing
- Conflicting instructions (be thorough in section X, be brief overall)

### Class 2 — Context Root Cause

Trace the context assembly step by step:

1. What files should have been loaded for this workflow?
2. Were they actually loaded? (Look at the session's read sequence)
3. Were any files loaded that shouldn't have been?
4. What were the `updated:` dates on memory files? Anything > 14 days old?

**Common context root causes:**
- Index wasn't checked first; wrong file was read
- Memory file was loaded but was stale (reflects old state)
- Retrieval returned relevant file, but also 4 irrelevant files that diluted attention
- Required file exists but wasn't in the skill's retrieval protocol

### Class 3 — Model Root Cause

**Tier checklist:**
- Capture tasks (extraction, tagging, formatting): Haiku is sufficient
- Analysis tasks (synthesis, reasoning, recommendation): Sonnet required
- Strategy tasks (cross-domain analysis, long-horizon judgment): Opus required
- Extended uncertainty: Opus with extended thinking

**What tells you you need a higher tier:**
- The output is *syntactically complete but semantically empty* — all the right sections, no insight
- The model lists options but won't recommend
- Analysis doesn't go beyond what's explicitly stated in the source (no inference)

### Class 4 — Infrastructure Root Cause

**429 Rate Limit:**
- Add exponential backoff: 1s → 2s → 4s → give up
- Check: is a batch workflow hitting limits? Space calls to stay under rate limits.

**5xx Server Error:**
- Retry 2-3 times with 2s delay
- If persistent: check Anthropic status page

**Timeout:**
- Check input token count: is input unusually large?
- Trim unnecessary context from the prompt
- Increase timeout setting if input is legitimately large

**max_tokens truncation:**
- The output budget is too small for the task
- Option A: Increase `max_tokens` parameter
- Option B: Reduce input (trim context) to leave more room for output
- Check: is the output format requesting more content than the budget allows?

**Zero cache tokens (when caching should work):**
- Verify `cache_control: {"type": "ephemeral"}` is set on system prompt block
- Check: is the system prompt static or does it include dynamic content (timestamps, session IDs)?
- Dynamic content in the system prompt breaks caching. Move dynamic content to user message.

---

## Step 5: Verify the Fix (5 min)

Don't declare success until you've verified:

1. Re-run the original failing case with the fix applied
2. Run `/eval` on the new output
3. All 4 eval dimensions should pass
4. If any dimension still fails: the fix addressed a symptom, not the root cause. Repeat from Step 1.

**Common verification failures:**
- Format now passes, but actionability still fails → the fix fixed format, not the real bug
- Factual accuracy improved, but completeness now fails → context fix broke scope
- The original case passes but a similar case still fails → root cause was too narrowly fixed

---

## Step 6: Document (2 min, only if > 10 min debugging session)

If finding the root cause took > 10 minutes, the pattern is worth recording:

```
File: notes/raw/debug-[YYYY-MM-DD]-[skill].md
Content:
  Failure: [one sentence]
  Class: [1/2/3/4]
  Root cause: [specific finding]
  Fix: [what changed]
  Prevention: [what would catch this earlier]
```

If the same failure class appears in the same skill more than once: add it to the prompt (as a defensive constraint) and note the pattern in `knowledge/technical/ai-debugging.md`.

---

## Retrieval Diagnostics (Supplement)

When debugging Class 2 (context failures) involving retrieval:

**Retrieval failure indicators:**
- Output is wrong in a way that would be fixed by reading the right file
- Output mentions things from old state (stale memory)
- Output is superficial despite the knowledge file having relevant depth

**Retrieval diagnosis steps:**

1. Identify what the model *should have known* to produce the correct output
2. Identify *which file* contains that information
3. Check whether that file was read in the session
4. If not read: why not? (wrong index lookup, wrong retrieval mode, file not indexed)
5. If read but wrong result: why? (file is stale, retrieval returned wrong file, attention diluted)

**Retrieval repair:**
- Wrong retrieval mode: update the skill's retrieval step to use index-first instead of direct
- File not indexed: add to KNOWLEDGE-INDEX.md
- Stale file: update the memory file before the next session
- Attention diluted: reduce the number of files loaded in that workflow step

---

## Context Debugging (Supplement)

When the failure is context-related but specifically about context assembly (not retrieval):

**Context assembly failure indicators:**
- Model seems unaware of behavioral instructions it should know
- Model's output contradicts what's in its active context
- Output quality varies depending on position in conversation (Lost-in-Middle effect)

**Context assembly diagnosis:**

1. What's the estimated total context overhead? (CLAUDE.md + memory + skill + files)
2. Is it within the 4,000-token budget?
3. If over budget: what's taking the most space? That's what's diluting attention.
4. Where in the context does the relevant information appear? (First = most attended; middle = least)

**Context assembly repair:**
- Over-budget: apply compression or remove speculative context
- Important information buried in middle: move it earlier in the context
- Conflicting instructions at different positions: consolidate into one clear instruction

---

## When to Escalate

Stop trying to debug and escalate (change approach) when:
- You've tried all 4 isolation tests and none confirm a class
- The same failure recurs despite fixing the apparent root cause 3 times
- The failure only appears in production with real data and can't be reproduced with test data
- The fix requires a capability the model demonstrably doesn't have at any tier

Escalation options:
- Add a human review step for the affected output type
- Break the task into smaller, more targeted sub-tasks
- Use a different output format that's less ambiguous to evaluate
- Accept the failure mode as a known limitation and document it
