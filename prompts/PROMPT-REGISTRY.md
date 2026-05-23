# Prompt Registry
## Index of all prompts in the workspace

Every prompt is versioned. When a prompt is updated, bump the version and note what changed.

| Name | File | Version | Purpose | Last Used | Quality Score |
|------|------|---------|---------|-----------|--------------|
| System: Analyst | `system/analyst.md` | v1.0 | Analysis and reasoning tasks | — | — |
| System: Synthesizer | `system/synthesizer.md` | v1.0 | Cross-domain synthesis | — | — |
| System: Reviewer | `system/reviewer.md` | v1.0 | Review and critique tasks | — | — |
| System: Strategist | `system/strategist.md` | v1.0 | Long-horizon strategic reasoning | — | — |
| Workflow: Daily Briefing | `workflows/daily-briefing.md` | v1.0 | Morning context assembly | — | — |
| Workflow: Meeting Structure | `workflows/meeting-structure.md` | v1.0 | Raw transcript → structure | — | — |
| Workflow: Meeting Debrief | `workflows/meeting-debrief.md` | v1.0 | Structured meeting → intelligence | — | — |
| Workflow: Promote to Knowledge | `workflows/promote-to-knowledge.md` | v1.0 | Note/extract → knowledge entry | — | — |
| Workflow: Weekly Review | `workflows/weekly-review.md` | v1.0 | Week synthesis and planning | — | — |
| Workflow: Strategy Synthesis | `workflows/strategy-synthesis.md` | v1.0 | Monthly strategy assessment | — | — |
| Workflow: Synthesis Memo | `workflows/synthesis-memo.md` | v1.0 | Deep topic synthesis | — | — |
| Workflow: Compress | `workflows/compress.md` | v1.0 | Context compression | — | — |
| Workflow: Learning Entry | `workflows/learning-entry.md` | v1.0 | Learning capture and structuring | — | — |
| Workflow: Context Compile | `workflows/context-compile.md` | v1.0 | Context assembly manifest for a task | — | — |
| System: Production Analyst | `system/production-analyst.md` | v1.0 | Production review and debugging sessions | — | — |
| Workflow: Production Review | `workflows/prod-review.md` | v1.0 | Quick, full, and incident review prompts | — | — |
| Workflow: AI Debug | `workflows/debug-ai.md` | v1.0 | Failure classification, isolation, root cause, eval | — | — |
| Workflow: Runtime Review | `workflows/runtime-review.md` | v1.0 | Cache efficiency, cost trend, latency regression analysis | — | — |
| Cognitive: Socratic Challenges | `cognitive/socratic.md` | v1.0 | Constraint-based stress-test prompts for empirical, causal, normative, predictive claims | — | — |
| Cognitive: Synthesis | `cognitive/synthesis.md` | v1.0 | Cross-domain connection extraction, cluster synthesis, bet-to-principle extraction | — | — |
| Cognitive: Misconception Detection | `cognitive/misconception.md` | v1.0 | Full entry diagnostic, batch triage, post-decision misconception check, propagation check | — | — |
| Cognitive: Active Recall | `cognitive/recall.md` | v1.0 | Standard recall challenge, triage, post-learn follow-up, forced retrieval | — | — |
| Cognitive: Architecture Critique | `cognitive/architecture.md` | v1.0 | Full critique, quick consistency check, post-build review, principle extraction | — | — |
| Cognitive: Decision Quality | `cognitive/decision-quality.md` | v1.0 | Single decision review, batch pattern extraction, kill condition audit, outcome-to-learning | — | — |
| Workflow: Daily Planning | `workflows/daily-planning.md` | v1.0 | Morning plan, weekly plan, prioritization triage, context load decision | — | — |
| Workflow: Focus Session | `workflows/focus-session.md` | v1.0 | Session frame, done condition sharpener, session close, scope reduction, context switch record | — | — |

---

## Prompt Quality Protocol

After using a prompt, rate the output 1-5 and log to `observability/quality.jsonl`:

```json
{"ts": "2026-05-20T09:00Z", "prompt": "workflows/meeting-debrief", "version": "v1.0", "score": 4, "note": "Good structure, action items slightly verbose"}
```

When average score for a prompt drops below 3.5, treat as a regression and revise the prompt.
