# Execution Audit
## The Weekly Health Check That Catches Drift Before It Becomes Crisis

Execution drift is the silent killer of quarterly plans. It doesn't announce itself — it accumulates in the gap between what was committed and what's actually happening. The execution audit is the practice that closes that gap weekly rather than discovering it at the end of the quarter.

---

## When to Run

**Weekly:** 30-minute working session, best run Thursday before the stakeholder pulse.

**Trigger immediately when:**
- A dependency was supposed to land this week and didn't
- Scope is being informally negotiated without going through prioritization
- "Done" is being redefined on an in-flight initiative
- The team's sprint velocity has dropped for two consecutive sprints without explanation

---

## The Execution Audit Framework

Five dimensions. Each has a health signal and a diagnostic question.

---

### Dimension 1 — Commitment Tracking

**What it checks:** Are we delivering what we said we'd deliver, when we said we'd deliver it?

**Inputs:** Sprint plan, quarterly roadmap, action items from `execution/action-items.md`

**Health signals:**
- Green: >80% of sprint commitments completed per sprint
- Yellow: 60-80% completion, or 2 consecutive sprints below 80%
- Red: <60%, or a quarterly milestone is at risk

**Diagnostic questions:**
- Which commitments slipped this week? What was the root cause?
- Are slips one-time events or part of a pattern?
- Is "done" shifting? (i.e., are items being marked complete but still needing rework?)
- What was committed but isn't in the sprint plan?

**Output:** A delta: what moved vs. what was committed. Name what slipped. Name the root cause. Don't soften it.

---

### Dimension 2 — Dependency Health

**What it checks:** Are cross-team and external dependencies on track?

**Inputs:** Dependency log (from initiative planning), engineering sync notes, stakeholder updates

**Health signals:**
- Green: All dependencies tracked, owners identified, no blocked items
- Yellow: 1-2 dependencies at risk, mitigation in progress
- Red: A dependency failure is blocking critical path work, or a dependency has no owner

**Diagnostic questions:**
- Which dependencies were due this week? Did they land?
- Which dependencies are due next 2 weeks? Are owners aware and on track?
- Are there new dependencies that emerged this sprint that weren't in the original plan?
- Is any team waiting on us that we haven't surfaced yet?

**Dependency log format:**
```yaml
dependency_id: D-YYYYMM-NN
description: [What we need and from whom]
owner: [Named person, not team]
needed_by: YYYY-MM-DD
status: on-track | at-risk | blocked | complete
blocker: [If at-risk or blocked: specific obstacle]
escalation_needed: true | false
```

---

### Dimension 3 — Scope Integrity

**What it checks:** Is the initiative still solving the original problem at the original scope?

**Inputs:** Original scope document, current sprint tickets, engineering conversations

**Health signals:**
- Green: Scope is stable, changes went through prioritization process
- Yellow: Informal scope additions have occurred, or scope is being quietly reduced
- Red: Scope has shifted enough that the original value proposition may not be achievable

**Diagnostic questions:**
- Are there features in the sprint that weren't in the original scope? How did they get there?
- Are there features from the original scope that have been quietly dropped? Why?
- Has "MVP" shifted since the initiative started? Is the new MVP still viable?
- Is engineering solving a different problem than the one PM scoped?

**Scope integrity rule:** Every scope change — addition or reduction — goes through an explicit decision. Even small changes. The decision doesn't need to be elaborate, but it needs to be deliberate and documented.

---

### Dimension 4 — Hypothesis Validity

**What it checks:** Is the underlying assumption behind the initiative still sound?

**Inputs:** Recent discovery conversations, metrics review, customer feedback, competitive signals

**Health signals:**
- Green: Assumption is being validated by evidence; early signals align with hypothesis
- Yellow: Assumption is untested or there's mixed evidence; hypothesis needs refinement
- Red: Evidence has emerged that directly contradicts the core assumption

**Diagnostic questions:**
- What assumption is this initiative testing? Have we gotten any signal on it?
- Has anything in discovery or metrics changed what we believe about the problem?
- Is a competitor doing something that changes the value of solving this problem?
- If we learned today that the assumption was wrong, what would we do?

**The hard question:** "Would we start this initiative today if we were starting fresh?" If the answer is no, the initiative deserves a kill criteria review — not necessarily a kill, but an honest look.

---

### Dimension 5 — Team Health

**What it checks:** Is the team in a state that can sustain execution quality?

**Inputs:** 1:1 signals, sprint retrospective themes, velocity trends, PTO/availability

**Health signals:**
- Green: Velocity stable, team has capacity for unplanned work, no sustained crunch
- Yellow: Signs of overload, recurring rework suggesting quality under pressure, key person bottlenecks
- Red: Attrition risk, morale signals, velocity declining for 3+ weeks without explanation

**Diagnostic questions:**
- Is anyone operating at 100% capacity for more than 2 weeks? (Zero slack = fragile system)
- Is rework increasing? (Often a quality signal — people shipping fast and fixing later)
- Are there single points of failure on the team? What happens if that person is out?
- What's the energy level around the initiative? Is the team still bought in to the problem?

**PM responsibility:** PMs don't manage engineering capacity — engineering leads do. But PMs are responsible for noticing the signals and having the conversation early.

---

## The Execution Audit Output

Write a brief execution health summary. Not a status report — a diagnostic output.

```markdown
# Execution Health — Week of YYYY-MM-DD

## Overall Status: GREEN | YELLOW | RED

## Commitment Tracking
Status: [GREEN/YELLOW/RED]
Slips: [What slipped and why]
Pattern: [Is this isolated or recurring?]

## Dependency Health
Status: [GREEN/YELLOW/RED]
At-risk dependencies: [List with owner and needed-by date]
Action: [What's being done]

## Scope Integrity
Status: [GREEN/YELLOW/RED]
Changes: [What changed, was it through process or informal?]

## Hypothesis Validity
Status: [GREEN/YELLOW/RED]
New signal: [What evidence came in this week?]
Implication: [Does it change what we're building?]

## Team Health
Status: [GREEN/YELLOW/RED]
Signals: [What's notable]

## Top 3 Actions This Week
1. [Action] — Owner: [name] — Due: [date]
2. [Action] — Owner: [name] — Due: [date]
3. [Action] — Owner: [name] — Due: [date]
```

**File to:** `execution/audit-YYYY-WW.md`

---

## When to Escalate from the Audit

The execution audit produces escalation signals. Use the escalation framework from `decision-frameworks/pm/escalation-framework.md`.

**Escalate immediately when:**
- A dependency failure puts a quarterly milestone at risk and the dependency owner hasn't acknowledged it
- Scope has expanded by >20% without going through prioritization and engineering lead/PM lead aren't aware
- A core assumption has been invalidated and the initiative hasn't been reassessed
- Team health signals suggest attrition risk or quality failure is imminent

**Escalation is not failure.** The failure is discovering a RED signal in the execution audit and treating it as YELLOW because escalating feels uncomfortable.

---

## Execution Audit Anti-Patterns

**The status report disguised as an audit:** Listing what happened this week without diagnosing root causes or identifying patterns. Status reports describe; audits diagnose.

**The green audit on a failing initiative:** Every dimension is green in the written audit, but everyone in the room knows something is wrong. If the room knows but the document says green, the document is lying. Name what's wrong.

**Audit without action:** Completing the audit but not surfacing the top actions with named owners. Audits produce clarity; actions produce outcomes.

**Skipping the audit on a "good" week:** Execution drift happens even on good weeks — just more quietly. The weeks where nothing seems wrong are when assumptions go unchallenged longest.

**Team health avoidance:** Skipping Dimension 5 because it feels soft or outside PM's scope. Team health is an execution risk. Treat it like one.
