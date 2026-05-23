---
type: failure
id: fail_YYYYMMDD_NNN
title: Short failure description (1 line)
failure_class: F1 | F2 | F3 | F4 | F5 | custom
custom_class:
first_seen: YYYY-MM-DD
last_seen: YYYY-MM-DD
recurrence_count: 1
linked_to: []
severity: low | medium | high
tags: []
review_date: YYYY-MM-DD
---

## What Failed
[Precise description of the failure. What symptom appeared? What was the context?]

## Root Cause
[What actually caused it. Not the symptom — the underlying mechanism. "JSON file was corrupted" is a symptom. "JSON written before SQLite on a step that crashed between writes" is a root cause.]

## Context (When This Happens)
[The conditions under which this failure occurs. Be specific enough that future-me can recognize it.]

## Symptoms
- [Observable indicator 1 — what you see before/during the failure]
- [Observable indicator 2]

## What Not To Do
[The intuitive but wrong response. What you might try first that makes things worse.]

## What To Do Instead
[The correct response. Specific enough to execute without extra context.]

## Recovery Used
[How this specific occurrence was recovered from. Link to recovery playbook if applicable.]

## Recurrence Log
| Date | Context | Outcome |
|------|---------|---------|
| YYYY-MM-DD | [describe the specific occurrence] | [how it resolved] |
