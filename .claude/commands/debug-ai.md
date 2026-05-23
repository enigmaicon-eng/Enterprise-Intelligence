# /debug-ai — AI System Debugger

Systematically diagnose and locate the root cause of an AI system failure. Follows the 4-class taxonomy: prompt failure, context failure, model failure, infrastructure failure.

## Trigger
`/debug-ai [description of failure]` — diagnose a specific output failure
`/debug-ai --trace [session-id]` — trace a specific session through telemetry
`/debug-ai --prompt [skill-name]` — diagnose a prompt for structural issues

---

## Protocol

### Step 0: Frame the failure (1 min)
Read the failing output. Write one sentence describing what went wrong:
"The output [is wrong / is incomplete / has wrong format / is too shallow / contradicts the source]."

This framing prevents scope creep. Debug the stated failure, not everything that could be improved.

### Step 1: Check telemetry first (3 min)
Read `telemetry/api-log.jsonl` for the relevant session.

Look for:
- Error codes (any non-200?)
- `completion_reason: max_tokens` (output truncated?)
- Latency spike (> 2× normal for this workflow?)
- `cached_tokens: 0` on a workflow that should cache?

**If any of these: you have an infrastructure failure (Class 4).** Go to Step 4-D.
**If telemetry is clean (no errors, normal latency, normal tokens): continue to Step 2.**

### Step 2: Apply the minimum viable isolation test (5 min)
Identify which variable is causing the failure by removing it:

```
Test A — Is it the prompt?
  Run the same prompt with simple, known-good inline context.
  If failure persists: prompt failure (Class 1). Go to Step 4-A.

Test B — Is it the context?
  Add the missing information directly inline to the prompt (bypass retrieval).
  If failure resolves: context failure (Class 2). Go to Step 4-B.

Test C — Is it the model?
  Run the same prompt + context on the next-higher model tier.
  If output quality improves substantially: model failure (Class 3). Go to Step 4-C.

If none of the above isolate it: the failure may be compound. Run all three tests.
```

### Step 3: Classify the failure
Based on Step 1 and Step 2, classify:

```
Class 1 — Prompt Failure
  Signal: Failure persists with simple known-good context
  Sub-type: scope / format / instruction / ambiguity
  
Class 2 — Context Failure
  Signal: Failure resolves when context provided inline
  Sub-type: missing retrieval / stale memory / wrong retrieval mode / over-retrieval
  
Class 3 — Model Failure
  Signal: Higher-tier model produces significantly better output on same input
  Sub-type: tier too low / extended thinking needed / model capability gap
  
Class 4 — Infrastructure Failure
  Signal: Error codes, truncation, latency spike visible in telemetry
  Sub-type: rate limit / timeout / token budget / connection error
```

State the classification explicitly: "This is a Class [X] failure — specifically [sub-type] — because [evidence]."

### Step 4: Root cause by class

#### Step 4-A: Prompt Failure

Read the skill's command file carefully. Apply this checklist:

```
Scope checklist:
  [ ] Does the prompt specify what to INCLUDE?
  [ ] Does the prompt specify what to EXCLUDE or limit?
  [ ] Is the scope consistent with the output format spec?

Format checklist:
  [ ] Is the expected output format specified precisely?
  [ ] Are field names, section headers, and required elements named?
  [ ] Is there an example output or template referenced?

Instruction checklist:
  [ ] Are any instructions ambiguous (can be read two ways)?
  [ ] Do any instructions conflict with each other?
  [ ] Is there a priority order when instructions conflict?

Ambiguity test:
  Read each instruction. Can you read it two ways? If yes: it's ambiguous.
  Ask: "What would the model do if it took the other reading?" That's the failure mode.
```

Fix: Add the missing constraint or clarify the ambiguous instruction. Minimum change that addresses the root cause. Bump the version in PROMPT-REGISTRY.md.

#### Step 4-B: Context Failure

Trace the context assembly:

```
Read the skill file's workflow steps. What files does it load?
For each file: was it actually read in this session?
  - If not read: retrieval failure (missing)
  - If read but wrong content: retrieval failure (stale or wrong file)
  - If read but too much: over-retrieval (attention diluted)

Check memory files used:
  - What was the updated: date on each memory file loaded?
  - Any file > 14 days old (latent)? Was it verified against current state?

Check retrieval mode:
  - Was the correct retrieval mode used? (Direct / Index-First / Grep / Cluster)
  - Was the index checked before the content file?
```

Fix: Correct the retrieval step in the skill file. Add hygiene check. Update stale memory files.

#### Step 4-C: Model Failure

```
What does this task actually require?
  - Extraction or formatting → capture tier (Haiku) is sufficient
  - Analysis, synthesis, reasoning → analysis tier (Sonnet)
  - Strategic judgment, cross-domain connection → strategy tier (Opus)

What tier was used?
  - Check the telemetry: model field in the log entry

Is there a mismatch?
  - Task requires analysis-tier reasoning; capture-tier model was used → update routing
  - Task requires strategy-tier reasoning; analysis-tier used → update routing

Does the task need extended thinking?
  - The model gives a shallow analysis on a genuinely complex question
  - Enable extended thinking for this specific call
```

Fix: Update the model tier in the workflow. If task genuinely requires Opus + thinking: update the Python script or skill to route there.

#### Step 4-D: Infrastructure Failure

```
Identify the specific failure:

HTTP 429: Rate limit hit
  → Add exponential backoff: 1s, 2s, 4s
  → Check if batch workflow can be paced to stay under rate limit

HTTP 5xx: API server error
  → Retry 2-3 times with 2s delay
  → If persistent: check Anthropic status page

Timeout:
  → Increase timeout setting
  → Check if input is abnormally large (trim unnecessary context)

completion_reason: max_tokens:
  → Increase max_tokens budget for this workflow
  → Or: reduce input (trim context) to leave room for output

cached_tokens: 0 on repeated call:
  → Verify cache_control: ephemeral is set on system prompt
  → Check if system prompt is varying between calls (dynamic content)
```

### Step 5: Verify the fix (5 min)
After applying the fix:
- Run `/eval` on the output produced by the fixed version
- Compare to the original failing output
- All 4 dimensions should now pass

If any dimension still fails: re-classify. The first classification was incomplete.

### Step 6: Document
For any fix that took > 10 minutes to find:
- Log the failure class, root cause, and fix to `notes/raw/` with tag: `ai-debug`
- If this is a pattern (same failure mode for same skill), promote to `knowledge/technical/ai-debugging.md` §Pattern Library

---

## Output Format

```
## Debug Report — [Skill] — [Date]

Failure: [one-sentence description]
Classification: Class [1/2/3/4] — [sub-type]
Evidence: [what telemetry or isolation test revealed the class]

Root Cause:
  [Specific finding — quote the broken prompt instruction, stale file, tier mismatch, or error code]

Fix Applied:
  [What changed — file, line, content]

Verified:
  [Eval result before: X/4 → after: X/4]
  
Recurrence Prevention:
  [What change prevents this happening again]
```
