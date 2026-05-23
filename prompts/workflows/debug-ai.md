# AI Debugging Workflow Prompts
## Version: v1.0

Reusable prompts for each phase of AI system debugging.

---

## Prompt: Failure Classification

```
Classify this AI output failure using the 4-class taxonomy.

Failing output:
[paste output here]

Source material the model was given:
[paste context here, or write "unavailable"]

Skill/prompt used:
[paste prompt or reference the skill name]

Telemetry entry (if available):
[paste JSONL log entry]

Instructions:
1. Match the symptoms to the most likely failure class:
   - Class 1 (Prompt): wrong format, scope drift, instruction misreading
   - Class 2 (Context): factually wrong but internally consistent; contradicts source
   - Class 3 (Model): correct format, correct facts, but shallow/no synthesis
   - Class 4 (Infrastructure): truncated, empty, error codes, latency spike

2. State which isolation test would confirm your classification.
3. State: "This is most likely Class [X] because [specific observation]."
4. Do NOT propose a fix yet. Classification first.
```

---

## Prompt: Isolation Test

```
Run an isolation test to confirm the failure class for this AI output failure.

Suspected class: [1 / 2 / 3 / 4]

For Class 1 (Prompt):
  Rewrite the input with simple, known-good inline context (2-3 clear sentences).
  Run it against the same prompt.
  Does the failure persist? If yes: confirmed Class 1. If no: reclassify.

For Class 2 (Context):
  Add the information you think was missing directly inline to the prompt (not via retrieval).
  Run it with the same prompt + inline context.
  Does the failure resolve? If yes: confirmed Class 2. If no: reclassify.

For Class 3 (Model):
  Identify the tier currently in use. 
  If capture tier: suggest running with analysis tier.
  If analysis tier: suggest running with strategy tier.
  State what capability difference would explain the failure.
  
For Class 4 (Infrastructure):
  Check the telemetry entry for: error codes, completion_reason, latency, cached_tokens.
  State specifically which telemetry signal confirms this is infrastructure.

Report: confirmed class, evidence, and the specific sub-type.
```

---

## Prompt: Prompt Root Cause Analysis

```
Analyze this prompt for structural failures.

Prompt to analyze:
[paste prompt here]

Failing output (example):
[paste failing output]

Apply these four probes:

SCOPE PROBE: Is the scope of what to include and exclude explicitly specified?
  - Quote any instruction that could be interpreted as broader or narrower than intended.
  - Identify: does the output contain content that should be excluded? Or miss content that should be included?

FORMAT PROBE: Is the exact output format specified with named sections and field structures?
  - Quote the format specification (if any).
  - Could the format have been inferred differently? How?

INSTRUCTION PROBE: Is any instruction ambiguous (readable two ways)?
  - For each instruction, read it two ways. Do both readings produce the same output?
  - Quote any instruction that has two valid readings.

CONFLICT PROBE: Do any two instructions pull in opposite directions?
  - Identify any pair of instructions that conflict.
  - State which resolution rule (if any) the prompt provides.

Output:
- Sub-type: [scope / format / instruction / ambiguity]
- Specific finding: [exact quote + what's wrong with it]
- Minimum fix: [exactly what to add or change — one sentence max]
```

---

## Prompt: Context Assembly Audit

```
Audit the context assembly for this workflow failure.

Workflow: [skill name]
Failing output: [paste or describe]
Files loaded in this session: [list from session, or "unknown"]

Read: architecture/CONTEXT-SELECTION-SYSTEM.md
Read: architecture/RETRIEVAL-SYSTEM.md

Assess:

1. RETRIEVAL COMPLETENESS: What files should have been loaded for this workflow? Were they all loaded?
   - Check the skill command file for the required file list.
   - For each required file: was it read in this session?

2. RETRIEVAL MODE: Was the correct retrieval mode used (Direct / Index-First / Grep / Cluster)?
   - Was the relevant index read before the content file?

3. FRESHNESS: What were the updated: dates on any memory files loaded?
   - Any file with updated: > 14 days ago is latent — was it verified?

4. DILUTION: How many files were loaded total? Is any file irrelevant to this workflow?
   - Files > 4 for a single workflow step is a dilution risk.

5. CONTEXT BUDGET: Estimate total non-conversation overhead. Is it > 4,000 tokens?

Output: identified context failure, specific file or retrieval step, and the minimum fix.
```

---

## Prompt: Eval and Comparison

```
Evaluate this AI output against the 4-dimension quality rubric.

Output to evaluate:
[paste output]

Source material:
[paste context or reference file]

Expected output schema:
[paste skill's output format spec, or reference the skill]

Apply each dimension:

D1 FACTUAL ACCURACY: For every factual claim in the output, can you trace it to the source material?
  Pass: all claims are traceable and correct.
  Fail: at least one claim can't be traced or contradicts the source.
  Evidence: [quote the specific claim that fails, and what the source actually says]

D2 COMPLETENESS: Are all required sections present and substantive?
  Compare output sections against the skill's required output schema.
  Pass: all required sections present with substantive content.
  Fail: at least one section missing or contains placeholder/stub content.
  Evidence: [which section is missing or insufficient]

D3 FORMAT COMPLIANCE: Does the output structure match the expected format?
  Pass: structure matches exactly.
  Fail: structural deviation that would require manual correction.
  Evidence: [what's different from the expected format]

D4 ACTIONABILITY: Can a reader act on this immediately?
  Pass: every action has owner + date; every recommendation has a specific next step.
  Fail: vague actions, missing owners, conclusions that require further analysis.
  Evidence: [specific element that isn't actionable]

Final verdict: [X/4 pass] — [Meets threshold (≥ 3/4) / Needs revision (< 3/4)]
Priority fix: [the single most impactful fix if any dimension fails]
```
