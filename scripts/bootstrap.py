"""
Bootstrap script — run once to verify workspace is ready.
Checks: API key, SDK installed, directory structure, required files, telemetry writeable.
"""

import os
import sys
from pathlib import Path

WORKSPACE = Path(__file__).parent.parent

REQUIRED_DIRS = [
    "architecture", "decision-frameworks", "docs", "execution",
    "knowledge", "learning", "meeting-intelligence/raw",
    "meeting-intelligence/processed", "memory", "notes/raw",
    "notes/structured", "notes/archive", "observability", "production-ai",
    "prompts/system", "prompts/workflows", "reviews/weekly", "scripts",
    "skills", "strategy", "synthesis/weekly-insights",
    "synthesis/monthly-insights", "systems-thinking", "technical-fluency",
    "telemetry", "templates", "workflows",
    ".claude/commands",
    "runtime/persistence",
]

REQUIRED_FILES = [
    # Phase 1 — Core Architecture
    "CLAUDE.md",
    "architecture/SYSTEM-ARCHITECTURE.md",
    "architecture/DATA-FLOWS.md",
    "architecture/CONTEXT-ARCHITECTURE.md",
    "architecture/SKILL-ARCHITECTURE.md",
    "architecture/MEMORY-MAP.md",
    "architecture/WORKFLOW-ROUTING.md",
    "architecture/ANTI-PATTERNS.md",
    "architecture/MAINTENANCE-CONVENTIONS.md",
    "workflows/CORE-WORKFLOWS.md",
    "skills/README.md",
    "prompts/PROMPT-REGISTRY.md",
    "prompts/system/analyst.md",
    "prompts/system/synthesizer.md",
    "prompts/system/strategist.md",
    "observability/TELEMETRY-STRATEGY.md",
    "execution/action-items.md",
    "knowledge/KNOWLEDGE-INDEX.md",
    "decision-frameworks/decisions-log.md",
    # Phase 2 — PM OS
    ".claude/commands/pm-strategy.md",
    ".claude/commands/pm-discovery.md",
    ".claude/commands/pm-prioritize.md",
    ".claude/commands/pm-exec-brief.md",
    ".claude/commands/pm-rca.md",
    ".claude/commands/pm-launch.md",
    # Phase 3 — Autonomous Orchestration
    "architecture/AUTONOMOUS-ORCHESTRATION.md",
    "architecture/SKILL-ROUTING-SYSTEM.md",
    "architecture/MCP-ROUTING-SYSTEM.md",
    "architecture/MEMORY-CONTINUITY-SYSTEM.md",
    "architecture/CONTEXT-SELECTION-SYSTEM.md",
    "architecture/EXECUTION-ORCHESTRATION.md",
    "architecture/DYNAMIC-CAPABILITY-GENERATION.md",
    "architecture/AUTONOMOUS-OPERATIONAL-FLOWS.md",
    "memory/MEMORY.md",
    "memory/user_profile.md",
    # Phase 4 — Execution Layer
    "production-ai/claude_client.py",
    "scripts/run_briefing.py",
    "scripts/run_debrief.py",
    "scripts/run_weekly.py",
    "scripts/run_observe.py",
    "scripts/telemetry_reader.py",
    "scripts/SCHEDULING.md",
    "prompts/workflows/daily-briefing.md",
    "prompts/workflows/meeting-structure.md",
    "prompts/workflows/meeting-debrief.md",
    "prompts/workflows/promote-to-knowledge.md",
    "prompts/workflows/strategy-synthesis.md",
    "prompts/workflows/synthesis-memo.md",
    "prompts/workflows/compress.md",
    "prompts/workflows/weekly-review.md",
    "prompts/system/reviewer.md",
    "execution/follow-ups.md",
    # Phase 13 — Bounded Runtime
    "architecture/BOUNDED-RUNTIME.md",
    "architecture/RUNTIME-STATE-SCHEMA.md",
    "runtime/state/active-workflows.json",
    "runtime/state/workflow-history.json",
    "runtime/events/queue.json",
    ".claude/commands/runtime-start.md",
    ".claude/commands/runtime-resume.md",
    ".claude/commands/runtime-status.md",
    ".claude/commands/runtime-recover.md",
    # Phase 14 — Dynamic Invocation
    "architecture/DYNAMIC-INVOCATION-SYSTEM.md",
    "skills/registry.json",
    "skills/capability-index.json",
    ".claude/commands/skill-lookup.md",
    ".claude/commands/skill-invoke.md",
    ".claude/commands/skill-deps.md",
    ".claude/commands/skill-gaps.md",
    ".claude/commands/skill-new.md",
    # Phase 15 — Persistent Execution
    "architecture/PERSISTENT-EXECUTION-SYSTEM.md",
    "architecture/RECOVERY-PLAYBOOKS.md",
    "runtime/persistence/schema.sql",
    "scripts/db_init.py",
    "scripts/event_store.py",
    "scripts/checkpoint_manager.py",
    "scripts/recovery_engine.py",
    "scripts/artifact_tracker.py",
    "scripts/timeline_viewer.py",
    ".claude/commands/exec-journal.md",
    ".claude/commands/exec-timeline.md",
    ".claude/commands/exec-snapshot.md",
    ".claude/commands/exec-diagnose.md",
    # Core operational skills
    ".claude/commands/briefing.md",
    ".claude/commands/capture.md",
    ".claude/commands/debrief.md",
    ".claude/commands/promote.md",
    ".claude/commands/decide.md",
    ".claude/commands/weekly.md",
    ".claude/commands/observe.md",
    ".claude/commands/synthesize.md",
]


def check(label: str, ok: bool, detail: str = "") -> bool:
    status = "OK  " if ok else "FAIL"
    msg = f"  [{status}] {label}"
    if detail:
        msg += f" — {detail}"
    print(msg)
    return ok


def main():
    print("\n=== Workspace Bootstrap Check ===\n")
    failures = 0

    # 1. API Key
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    ok = bool(api_key and api_key.startswith("sk-ant-"))
    if not check("ANTHROPIC_API_KEY", ok, "Set via: $env:ANTHROPIC_API_KEY='sk-ant-...'"):
        failures += 1

    # 2. SDK installed
    try:
        import anthropic
        check("anthropic SDK", True, f"v{anthropic.__version__}")
    except ImportError:
        check("anthropic SDK", False, "Run: python -m pip install anthropic tenacity")
        failures += 1

    # 3. Directories
    print()
    missing_dirs = []
    for d in REQUIRED_DIRS:
        path = WORKSPACE / d
        if not path.exists():
            missing_dirs.append(d)
            path.mkdir(parents=True, exist_ok=True)

    if missing_dirs:
        check(f"Directories ({len(missing_dirs)} created)", True, f"Created: {', '.join(missing_dirs[:3])}{'...' if len(missing_dirs) > 3 else ''}")
    else:
        check(f"All {len(REQUIRED_DIRS)} directories present", True)

    # 4. Required files
    print()
    missing_files = []
    for f in REQUIRED_FILES:
        path = WORKSPACE / f
        if not path.exists():
            missing_files.append(f)

    if missing_files:
        print(f"  [FAIL] Missing files ({len(missing_files)}):")
        for f in missing_files[:10]:
            print(f"         - {f}")
        if len(missing_files) > 10:
            print(f"         ... and {len(missing_files) - 10} more")
        failures += 1
    else:
        check(f"All {len(REQUIRED_FILES)} required files", True)

    # 5. Telemetry writable
    print()
    try:
        tel_dir = WORKSPACE / "telemetry"
        tel_dir.mkdir(exist_ok=True)
        test_file = tel_dir / ".write_test"
        test_file.write_text("ok")
        test_file.unlink()
        check("Telemetry writable", True)
    except OSError as e:
        check("Telemetry writable", False, str(e))
        failures += 1

    # 6. Memory system
    memory_index = WORKSPACE / "memory" / "MEMORY.md"
    if not memory_index.exists():
        print("\n  [WARN] memory/MEMORY.md not initialized — Claude will create it on first use")
    else:
        check("Memory index", True)

    # 7. Skills
    print()
    commands_dir = WORKSPACE / ".claude" / "commands"
    skill_files = list(commands_dir.glob("*.md")) if commands_dir.exists() else []
    check(f"Skills ({len(skill_files)} commands)", len(skill_files) >= 52,
          f"Found: {', '.join(f.stem for f in skill_files[:8])}{'...' if len(skill_files) > 8 else ''}")
    if len(skill_files) < 52:
        failures += 1

    # 8. CLAUDE.md token estimate
    print()
    claude_md = WORKSPACE / "CLAUDE.md"
    if claude_md.exists():
        size = len(claude_md.read_text(encoding="utf-8"))
        token_est = size // 4
        ok = token_est <= 1200
        check(f"CLAUDE.md size (~{token_est} tokens)", ok,
              "Target: <1,200 tokens" if not ok else "Within budget")
        if not ok:
            failures += 1

    # Summary
    print(f"\n{'='*33}")
    if failures == 0:
        print("Workspace ready. Start with: /briefing")
    else:
        print(f"{failures} issue(s) to resolve.")
    print()
    return failures


if __name__ == "__main__":
    sys.exit(main())
