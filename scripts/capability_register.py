"""
MCP capability registration and invocation logging — P19 MCP + Tool Capability Layer.

Manages the MCP server lifecycle: register, activate, suspend, reactivate, retire.
Also provides log_invocation() — called by skills to record tool use in INVOCATION-LOG.jsonl.

Usage:
    python scripts/capability_register.py --list                         # list all servers
    python scripts/capability_register.py --list --status active         # filter by status
    python scripts/capability_register.py --add <json_file>              # register from JSON spec
    python scripts/capability_register.py --suspend <server_id>          # suspend a server
    python scripts/capability_register.py --reactivate <server_id>       # reactivate suspended
    python scripts/capability_register.py --retire <server_id>           # retire (requires 0 recent invocations)
    python scripts/capability_register.py --log <tool_id> <outcome>      # log a single invocation
"""

import json
import sys
import uuid
from datetime import datetime, date, timezone, timedelta
from pathlib import Path

WORKSPACE = Path(__file__).parent.parent
CAPABILITIES_DIR = WORKSPACE / "capabilities"
REGISTRY_PATH = CAPABILITIES_DIR / "MCP-REGISTRY.json"
INVOCATION_LOG_PATH = CAPABILITIES_DIR / "INVOCATION-LOG.jsonl"

RETIRE_INACTIVE_DAYS = 30


def load_registry() -> dict:
    if not REGISTRY_PATH.exists():
        return {"servers": []}
    return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))


def save_registry(registry: dict) -> None:
    registry["generated_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    active = sum(1 for s in registry["servers"] if s["status"] == "active")
    suspended = sum(1 for s in registry["servers"] if s["status"] == "suspended")
    retired = sum(1 for s in registry["servers"] if s["status"] == "retired")
    pending = sum(1 for s in registry["servers"] if s["status"] == "pending_approval")
    registry["stats"] = {
        "total_servers": len(registry["servers"]),
        "active": active,
        "suspended": suspended,
        "retired": retired,
        "pending_approval": pending,
    }
    REGISTRY_PATH.write_text(json.dumps(registry, indent=2), encoding="utf-8")


def log_invocation(
    tool_id: str,
    source_server: str,
    permission_class: str,
    gated: bool,
    outcome: str,
    duration_ms: int = 0,
    session_id: str = "",
    notes: str = "",
) -> None:
    """Append a single invocation record to INVOCATION-LOG.jsonl."""
    record = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "tool_id": tool_id,
        "source_server": source_server,
        "permission_class": permission_class,
        "gated": gated,
        "outcome": outcome,
        "duration_ms": duration_ms,
        "session_id": session_id or "unknown",
        "notes": notes,
    }
    with INVOCATION_LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")

    # Update last_used and invocation_count in registry
    registry = load_registry()
    today = date.today().isoformat()
    for server in registry["servers"]:
        if server["id"] == source_server:
            server["last_used"] = today
            server["invocation_count"] = server.get("invocation_count", 0) + 1
            break
    save_registry(registry)


def register_server(spec: dict) -> tuple[bool, str]:
    """Add a new MCP server to the registry. Returns (success, message)."""
    registry = load_registry()
    existing_ids = {s["id"] for s in registry["servers"]}

    server_id = spec.get("id", "").strip()
    if not server_id:
        return False, "spec.id is required"
    if server_id in existing_ids:
        return False, f"Server '{server_id}' already registered. Use --suspend or --reactivate to manage it."

    permission_class = spec.get("permission_class", "RW")
    if permission_class not in ("R", "RW", "NET", "DESTR"):
        return False, f"Invalid permission_class '{permission_class}'. Must be one of: R, RW, NET, DESTR"

    today = date.today().isoformat()
    entry = {
        "id": server_id,
        "name": spec.get("name", server_id),
        "source": "operator",
        "transport": spec.get("transport", "stdio"),
        "command": spec.get("command", ""),
        "status": "active",
        "permission_class": permission_class,
        "approved_by": "operator",
        "approved_at": today,
        "capabilities": spec.get("capabilities", []),
        "registered_at": today,
        "last_used": None,
        "invocation_count": 0,
        "notes": spec.get("notes", ""),
    }
    registry["servers"].append(entry)
    save_registry(registry)
    return True, f"Registered: {server_id} (permission_class={permission_class}, status=active)"


def set_status(server_id: str, new_status: str, require_inactive_days: bool = False) -> tuple[bool, str]:
    """Update server status. Returns (success, message)."""
    registry = load_registry()
    for server in registry["servers"]:
        if server["id"] == server_id:
            if require_inactive_days:
                last_used = server.get("last_used")
                if last_used:
                    last_used_date = datetime.strptime(last_used, "%Y-%m-%d").date()
                    days_inactive = (date.today() - last_used_date).days
                    if days_inactive < RETIRE_INACTIVE_DAYS:
                        return False, (
                            f"Cannot retire '{server_id}': last used {days_inactive} days ago. "
                            f"Requires {RETIRE_INACTIVE_DAYS}+ days inactive."
                        )
                elif server.get("invocation_count", 0) > 0:
                    return False, (
                        f"Cannot retire '{server_id}': has {server['invocation_count']} invocations "
                        f"but no last_used date recorded."
                    )
            old_status = server["status"]
            server["status"] = new_status
            save_registry(registry)
            return True, f"  {server_id}: {old_status} → {new_status}"
    return False, f"Server not found: {server_id}"


def main() -> int:
    args = sys.argv[1:]

    if not args:
        print("Usage: capability_register.py [--list] [--add <spec.json>] [--suspend ID] [--reactivate ID] [--retire ID] [--log TOOL_ID OUTCOME]")
        return 1

    if "--list" in args:
        registry = load_registry()
        status_filter = None
        if "--status" in args:
            idx = args.index("--status")
            if idx + 1 < len(args):
                status_filter = args[idx + 1]

        servers = registry["servers"]
        if status_filter:
            servers = [s for s in servers if s["status"] == status_filter]

        print(f"\nMCP Registry ({len(servers)} servers{' status=' + status_filter if status_filter else ''}):")
        print(f"  {'ID':<30} {'Status':<12} {'Class':<6} {'Invocations':<12} {'Last Used'}")
        print("  " + "-" * 75)
        for s in sorted(servers, key=lambda x: x["status"]):
            last = s.get("last_used") or "never"
            print(f"  {s['id']:<30} {s['status']:<12} {s['permission_class']:<6} {s.get('invocation_count', 0):<12} {last}")
        stats = registry.get("stats", {})
        print(f"\n  Total: {stats.get('total_servers', 0)}  "
              f"Active: {stats.get('active', 0)}  "
              f"Suspended: {stats.get('suspended', 0)}  "
              f"Retired: {stats.get('retired', 0)}")
        print()
        return 0

    if "--add" in args:
        idx = args.index("--add")
        if idx + 1 >= len(args):
            print("--add requires a path to a JSON spec file")
            return 1
        spec_path = Path(args[idx + 1])
        if not spec_path.exists():
            print(f"Spec file not found: {spec_path}")
            return 1
        spec = json.loads(spec_path.read_text(encoding="utf-8"))
        ok, msg = register_server(spec)
        print(f"\n  {'[OK]' if ok else '[FAIL]'} {msg}\n")
        return 0 if ok else 1

    if "--suspend" in args:
        idx = args.index("--suspend")
        if idx + 1 >= len(args):
            print("--suspend requires a server_id")
            return 1
        ok, msg = set_status(args[idx + 1], "suspended")
        print(f"\n  {'[OK]' if ok else '[FAIL]'} {msg}\n")
        return 0 if ok else 1

    if "--reactivate" in args:
        idx = args.index("--reactivate")
        if idx + 1 >= len(args):
            print("--reactivate requires a server_id")
            return 1
        ok, msg = set_status(args[idx + 1], "active")
        print(f"\n  {'[OK]' if ok else '[FAIL]'} {msg}\n")
        return 0 if ok else 1

    if "--retire" in args:
        idx = args.index("--retire")
        if idx + 1 >= len(args):
            print("--retire requires a server_id")
            return 1
        ok, msg = set_status(args[idx + 1], "retired", require_inactive_days=True)
        print(f"\n  {'[OK]' if ok else '[FAIL]'} {msg}\n")
        return 0 if ok else 1

    if "--log" in args:
        idx = args.index("--log")
        if idx + 2 >= len(args):
            print("--log requires: tool_id outcome [source_server] [permission_class]")
            return 1
        tool_id = args[idx + 1]
        outcome = args[idx + 2]
        source = args[idx + 3] if idx + 3 < len(args) else "unknown"
        pclass = args[idx + 4] if idx + 4 < len(args) else "R"
        log_invocation(tool_id, source, pclass, False, outcome)
        print(f"  Logged: {tool_id} → {outcome}")
        return 0

    print("Unknown arguments. Run with no args for usage.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
