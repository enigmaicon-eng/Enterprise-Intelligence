# Recovery Playbook
## [Workflow ID] — [YYYY-MM-DD]

Generated during recovery of a disrupted workflow. Records what happened, what was tried, and what succeeded.

---

## Situation

**Workflow ID:** [wf_YYYYMMDD_NNN]
**Workflow Name:** [name]
**Discovered at:** [YYYY-MM-DD HH:MM UTC]
**Status at discovery:** [RUNNING / FAILED / INTERRUPTED]
**Failure class:** [F1 / F2 / F3 / F4 / F5 / none]

**What happened:**
[1-3 sentences describing the failure or interruption.]

---

## Diagnosis

**Last recorded event:** [event_type] @ [timestamp]
**Last valid checkpoint:** [checkpoint_id] (Step [N], trigger: [trigger])
**Artifacts present:** [M] of [T]

**Missing artifacts:**
- [file path] — [reason]

**Journal entries (ERROR/WARN):**
```
[paste relevant journal lines]
```

---

## Recovery Actions Taken

| Step | Action | Outcome | Timestamp |
|------|--------|---------|-----------|
| 1 | [e.g. Ran /exec-diagnose] | [result] | [HH:MM] |
| 2 | [e.g. REWIND to ckpt_...] | [approved/rejected] | [HH:MM] |
| 3 | [e.g. Resumed from Step N] | [success/fail] | [HH:MM] |

**Gate decisions during recovery:**
- [decision 1: what was presented, what was chosen]
- [decision 2]

---

## Outcome

**Recovery status:** SUCCESSFUL / PARTIAL / FAILED

**Workflow state after recovery:** [RESUMED at Step N / ABANDONED / STILL FAILED]

**Artifacts recovered:** [M] of [T] original + [N] reproduced

---

## Root Cause

[What caused this failure? 1-2 sentences. Name the specific trigger: crashed session, missing file, skill error, etc.]

---

## Prevention

[What would prevent this from happening again? e.g. "Run /shutdown before closing Claude Code", "Verify input files before approving step N gate."]

---

## Notes

[Any other relevant observations — partial outputs found, manual edits made, workarounds applied.]
