# Scheduling Setup
## How to Automate Recurring Workflows

Two scheduling approaches: Claude Code CronCreate (native, recommended) and Windows Task Scheduler (external fallback).

---

## Option 1 — Claude Code CronCreate (Recommended)

CronCreate schedules automated Claude Code agent runs. No external setup needed — the scheduler is built into the tool.

### Weekly Review (Monday 08:00)

In a Claude Code session, run:

```
/schedule Create a recurring task: every Monday at 08:00, run the weekly review workflow
by reading all processed meeting files from the past week, open action items, and the
decisions log, then call /weekly to produce reviews/weekly/YYYY-WW.md and update
action-items.md with next week's priorities.
```

### Observability Report (Monday 08:30)

```
/schedule Create a recurring task: every Monday at 08:30 (after weekly review completes),
run /observe to generate the observability dashboard at observability/dashboard.md from
the telemetry logs.
```

### Knowledge Decay Scan (Monthly, first Monday)

```
/schedule Create a monthly task: on the first Monday of each month, read
knowledge/KNOWLEDGE-INDEX.md and flag any entries with reviewed: date older than 90 days.
Append the flagged entries to execution/action-items.md as low-priority items.
```

---

## Option 2 — Python Scripts via Windows Task Scheduler

For running the Python workflow scripts on a schedule without Claude Code open.

### Prerequisites

```powershell
# Install Python dependencies
pip install anthropic tenacity

# Set API key (add to your PowerShell profile for persistence)
$env:ANTHROPIC_API_KEY = "sk-ant-..."
# To persist: Add-Content $PROFILE "`n`$env:ANTHROPIC_API_KEY = 'sk-ant-...'"
```

### Create Weekly Review Task

```powershell
$action = New-ScheduledTaskAction `
    -Execute "python" `
    -Argument "C:\Users\DELL\Enterprise-Intelligence-Workspace\scripts\run_weekly.py" `
    -WorkingDirectory "C:\Users\DELL\Enterprise-Intelligence-Workspace"

$trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Monday -At 8:00am

$settings = New-ScheduledTaskSettingsSet -ExecutionTimeLimit (New-TimeSpan -Hours 1)

Register-ScheduledTask `
    -TaskName "EIW-WeeklyReview" `
    -Action $action `
    -Trigger $trigger `
    -Settings $settings `
    -Description "Enterprise Intelligence Workspace — Weekly Review"
```

### Create Observability Task

```powershell
$action = New-ScheduledTaskAction `
    -Execute "python" `
    -Argument "C:\Users\DELL\Enterprise-Intelligence-Workspace\scripts\run_observe.py" `
    -WorkingDirectory "C:\Users\DELL\Enterprise-Intelligence-Workspace"

$trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Monday -At 8:30am

Register-ScheduledTask `
    -TaskName "EIW-Observability" `
    -Action $action `
    -Trigger $trigger `
    -Description "Enterprise Intelligence Workspace — Observability Report"
```

### Verify Tasks

```powershell
Get-ScheduledTask | Where-Object {$_.TaskName -like "EIW-*"} | Format-Table TaskName, State
```

---

## Manual Runs (Any Time)

All workflows can also be run manually:

```powershell
# Daily briefing (run at session start)
python scripts/run_briefing.py

# Debrief a specific meeting file
python scripts/run_debrief.py 2026-05-21-product-sync.md

# Weekly review (run any time, --force to regenerate)
python scripts/run_weekly.py
python scripts/run_weekly.py --force

# Observability report
python scripts/run_observe.py

# Telemetry quick summary
python scripts/telemetry_reader.py
python scripts/telemetry_reader.py --days 14
python scripts/telemetry_reader.py --workflow meeting-debrief

# Health check
python scripts/bootstrap.py
```

---

## Environment Variable Setup (One-Time)

```powershell
# Temporary (this session only)
$env:ANTHROPIC_API_KEY = "sk-ant-api03-..."

# Permanent (survives shell restart)
[System.Environment]::SetEnvironmentVariable(
    "ANTHROPIC_API_KEY",
    "sk-ant-api03-...",
    [System.EnvironmentVariableTarget]::User
)

# Verify
python -c "import os; print('Key set:', bool(os.environ.get('ANTHROPIC_API_KEY')))"
```
