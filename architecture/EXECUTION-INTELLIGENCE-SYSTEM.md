# Execution Intelligence System

Analytics layer on top of the execution trace infrastructure. Answers the performance questions the trace capture system accumulates data for but never surfaces: Is execution output improving? Is actual work aligned with intentions? What friction patterns recur?

## Existing Execution Coverage (Do Not Duplicate)

| Skill | What It Covers |
|-------|---------------|
| `/exec-plan` | Building an execution plan |
| `/exec-prioritize` | Prioritizing work: commitment → leverage → reversibility |
| `/exec-checkpoint` | Continue / pivot / stop decision |
| `/exec-risk` | Surfacing and tracking execution risks |
| `/exec-review` | Reviewing a completed execution |
| `/trace-capture` | Recording an execution trace after a session |
| `/workflow-journal` | Quick daily session log |
| `/trace-recall` | Retrieving past traces before starting similar work |
| `/trace-search` | Searching execution history by keyword or filter |
| `/pattern-mine` | Detecting recurring operational patterns for codification |
| `/ops-dashboard` | Overall execution health: 30-day counts, runtime state, pattern coverage, flags |
| `/exec-inspect` | Deep dive on ONE specific trace |
| `/failure-review` | Non-completed outcome analysis; recurring failure modes |
| `/skill-stats` | Skill invocation frequency and session-type distribution |

## New Skills (P27)

| Skill | Fills Gap | Core Question |
|-------|----------|--------------|
| `/exec-throughput` | Throughput trend is never measured across time | "Is my execution output improving, stable, or declining?" |
| `/exec-allocation` | Work-type distribution is never analyzed | "Where is my actual execution time going vs where I intend it to go?" |
| `/exec-friction` | Non-failure impediments are never catalogued | "What keeps slowing me down, and what's the structural pattern?" |

## Capability Distinctions

```
Is the workspace operationally healthy right now?
→ /ops-dashboard  (30-day snapshot, runtime state, flags)

Am I executing more or less effectively over time?
→ /exec-throughput  (trend line: completion rate, output rate, improvement direction)

Where is my execution time actually going vs where I plan it to go?
→ /exec-allocation  (work-type distribution, reactive vs proactive ratio)

What's causing slowdowns, pivots, and replanning (short of full failure)?
→ /exec-friction  (friction taxonomy, recurring impediment patterns)

What specifically failed and why?
→ /failure-review  (non-completed outcomes only: failed / partial / abandoned)

What operational patterns have I developed?
→ /pattern-mine  (codification: 2+ instance threshold, operator-gated)
```

## Throughput Model

`/exec-throughput` reads TRACE-INDEX.md time series. Requires ≥10 episodes for trend signal.

```
Unit of measure: "productive session" = trace with outcome = completed
Time windows:
  Last 30 days vs prior 30 days → momentum (improving / stable / declining)
  Weekly rate: completed sessions ÷ weeks in period
  Completion rate: completed ÷ total episodes per period

Trend classifications:
  Improving    — completion rate last-30 > prior-30 by >10 percentage points
  Stable       — completion rate within 10pp in both periods
  Declining    — completion rate last-30 < prior-30 by >10pp
  Insufficient — <10 total episodes (not enough for trend)
```

## Work Allocation Model

`/exec-allocation` reads trace files for session type + tag metadata. Session types map to work categories:

| Session Type Tag | Work Category |
|-----------------|---------------|
| planning, strategy | Proactive/Strategic |
| execution, build, implement | Productive/Output |
| review, retrospective, audit | Reflective/Maintenance |
| research, learn, explore | Generative/Input |
| reactive, urgent, interrupt | Reactive/Unplanned |
| support, meeting, admin | Overhead/Coordination |

Intention proxy: weekly journal entries (from `/workflow-journal`) may state intended work type. Where available, compare stated intent vs actual session type distribution.

Reactive work ratio = reactive/unplanned sessions ÷ total sessions. High (>30%) = structural problem.

## Friction Taxonomy

Used by `/exec-friction`:

| Friction Type | Definition | Signal in Traces |
|--------------|-----------|----------------|
| **Dependency block** | Work halted waiting for external input | Blocked state noted; outcome = partial; resumed later |
| **Clarity block** | Work replanned mid-session due to unclear requirements | Pivot noted; goal changed during execution |
| **Scope creep** | Session expanded beyond original goal; completion rate drops | Actual work ≫ original goal; partial or overrun |
| **Context switch** | Session interrupted or changed type unexpectedly | Two distinct goals in one trace; abandoned rate elevated |
| **Energy depletion** | Work abandoned despite no external block | Abandoned without external reason; repeated at same session time |
| **Tool friction** | Repeated workflow delays from tooling issues | Failure notes cite tool or environment; not knowledge/skill gaps |

Friction ≠ failure: many friction events end in completion, just slower than expected. The signal is the pivot/replan/block note, not the outcome.

## Data Sources

```
traces/
  TRACE-INDEX.md         ← session metadata, outcomes, dates (all 3 skills)
  executions/            ← full trace files: session type, tags, goal, blockers, pivots
  journal/               ← workflow journal entries: intended work type (exec-allocation)
  patterns/              ← codified patterns (exec-friction cross-references)
```

## Recommended Cadence

- **Weekly**: `/exec-throughput` — check if completion rate is moving
- **Monthly**: `/exec-allocation` — is actual time distribution drifting from intention?
- **Monthly**: `/exec-friction` — which friction types are accumulating?
- **Trigger**: run `/exec-friction` before any structural workflow change decision

## Anti-Patterns

| Anti-pattern | Why it fails |
|-------------|-------------|
| Optimizing for session count over completion rate | More sessions with lower completion is deterioration, not improvement |
| Treating all friction as fixable | Some friction (dependency blocks from external factors) cannot be eliminated — manage it, don't fight it |
| Running /exec-throughput on <10 episodes | Trend analysis below critical mass produces noise; build the trace history first |
| Resolving friction patterns by adding process | Most friction is reduced by removing ambiguity or constraint, not adding step |
| Using /exec-allocation without session type tags in traces | If traces lack type metadata, allocation is uncomputable — fix trace capture hygiene first |
