"""
Capability index builder — reads MCP-REGISTRY.json and TOOL-REGISTRY.json, rebuilds CAPABILITY-INDEX.json.

The index is a derived artifact. Always rebuild after any registry change.
Never hand-edit CAPABILITY-INDEX.json (governance rule G-7).

Usage:
    python scripts/capability_index.py              # full rebuild
    python scripts/capability_index.py --check      # verify index is current
    python scripts/capability_index.py --stats      # print capability statistics
    python scripts/capability_index.py --search "browser screenshot"   # keyword search
"""

import json
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

WORKSPACE = Path(__file__).parent.parent
CAPABILITIES_DIR = WORKSPACE / "capabilities"
REGISTRY_PATH = CAPABILITIES_DIR / "MCP-REGISTRY.json"
TOOL_REGISTRY_PATH = CAPABILITIES_DIR / "TOOL-REGISTRY.json"
INDEX_PATH = CAPABILITIES_DIR / "CAPABILITY-INDEX.json"


def load_mcp_registry() -> dict:
    if not REGISTRY_PATH.exists():
        return {"servers": []}
    return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))


def load_tool_registry() -> dict:
    if not TOOL_REGISTRY_PATH.exists():
        return {"tools": []}
    return json.loads(TOOL_REGISTRY_PATH.read_text(encoding="utf-8"))


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z]{2,}", text.lower())


def build_search_terms(tools: list[dict]) -> dict[str, list[str]]:
    """Build a keyword → [tool_id] mapping for fast search."""
    term_map: dict[str, set] = defaultdict(set)

    for tool in tools:
        tool_id = tool["id"]
        # Index from: id, name, description, category, source_server
        for field in ("id", "name", "description", "category", "source_server"):
            for token in tokenize(tool.get(field, "")):
                if len(token) >= 3:
                    term_map[token].add(tool_id)

    return {term: sorted(ids) for term, ids in sorted(term_map.items())}


def build_index(mcp_registry: dict, tool_registry: dict) -> dict:
    tools = tool_registry.get("tools", [])
    servers = mcp_registry.get("servers", [])

    by_category: dict[str, dict] = defaultdict(lambda: {"count": 0, "tools": []})
    by_class: dict[str, dict] = defaultdict(lambda: {"count": 0, "tools": [], "gate_policy": ""})
    by_server: dict[str, list] = defaultdict(list)

    gate_policies = {
        "R": "No gate — auto-allowed",
        "RW": "Gate on first novel use per session; subsequent same-tool uses: auto",
        "NET": "Gate on every invocation or operator pre-authorizes session scope",
        "DESTR": "Gate on every invocation — no exceptions",
    }

    for tool in tools:
        cat = tool.get("category", "uncategorized")
        pclass = tool.get("permission_class", "R")
        server = tool.get("source_server", "unknown")
        tid = tool["id"]

        by_category[cat]["count"] += 1
        by_category[cat]["tools"].append(tid)

        by_class[pclass]["count"] += 1
        by_class[pclass]["tools"].append(tid)
        by_class[pclass]["gate_policy"] = gate_policies.get(pclass, "")

        by_server[server].append(tid)

    # Suspended/retired servers — flag their tools as restricted
    inactive_servers = {
        s["id"] for s in servers if s["status"] in ("suspended", "retired")
    }
    restricted_tools = [
        t["id"] for t in tools if t.get("source_server") in inactive_servers
    ]

    search_terms = build_search_terms(tools)

    return {
        "_schema": "P19 Capability Index v1.0",
        "_note": "Derived from MCP-REGISTRY.json and TOOL-REGISTRY.json. Do not edit manually.",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_capabilities": len(tools),
        "restricted_tools": restricted_tools,
        "by_category": {k: dict(v) for k, v in by_category.items()},
        "by_permission_class": {k: dict(v) for k, v in by_class.items()},
        "by_server": dict(by_server),
        "search_terms": search_terms,
    }


def search_index(index: dict, query: str, top_n: int = 10) -> list[dict]:
    """Keyword search against the capability index. Returns ranked tool entries."""
    query_tokens = set(tokenize(query))
    search_terms = index.get("search_terms", {})
    tool_scores: dict[str, int] = defaultdict(int)

    for token in query_tokens:
        if token in search_terms:
            for tool_id in search_terms[token]:
                tool_scores[tool_id] += 1

    # Load tool details for result enrichment
    tool_registry = load_tool_registry()
    tool_map = {t["id"]: t for t in tool_registry.get("tools", [])}

    ranked = sorted(tool_scores.items(), key=lambda x: x[1], reverse=True)
    results = []
    for tool_id, score in ranked[:top_n]:
        tool = tool_map.get(tool_id, {"id": tool_id})
        results.append({
            "score": score,
            "id": tool_id,
            "name": tool.get("name", tool_id),
            "source_server": tool.get("source_server", "?"),
            "category": tool.get("category", "?"),
            "permission_class": tool.get("permission_class", "?"),
            "requires_gate": tool.get("requires_gate", True),
            "description": tool.get("description", ""),
        })
    return results


def main() -> int:
    args = sys.argv[1:]

    if "--search" in args:
        idx = args.index("--search")
        query = args[idx + 1] if idx + 1 < len(args) else ""
        if not query:
            print("--search requires a query string")
            return 1
        if not INDEX_PATH.exists():
            print("CAPABILITY-INDEX.json not found. Run without --search to build.")
            return 1
        index = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
        results = search_index(index, query)
        if not results:
            print(f"\n  No results for: \"{query}\"")
            print("  → Use /mcp-register to add a new capability.")
        else:
            gate_labels = {"R": "no gate", "RW": "session gate", "NET": "per-call gate", "DESTR": "always gate"}
            print(f"\n  Capability search: \"{query}\" ({len(results)} matches)")
            print(f"  {'Tool ID':<35} {'Class':<6} {'Gate':<14} {'Source':<22} Description")
            print("  " + "-" * 100)
            for r in results:
                gate = gate_labels.get(r["permission_class"], "?")
                desc = r["description"][:45] + ("..." if len(r["description"]) > 45 else "")
                print(f"  {r['id']:<35} {r['permission_class']:<6} {gate:<14} {r['source_server']:<22} {desc}")
        print()
        return 0

    if "--check" in args:
        if not INDEX_PATH.exists():
            print("  [MISSING] CAPABILITY-INDEX.json not found. Run without --check to build.")
            return 1
        index = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
        tool_registry = load_tool_registry()
        index_count = index.get("total_capabilities", 0)
        registry_count = len(tool_registry.get("tools", []))
        if index_count != registry_count:
            print(f"  [STALE] Index has {index_count} capabilities; {registry_count} in TOOL-REGISTRY.")
            return 1
        print(f"  [OK] Index is current: {index_count} capabilities indexed.")
        return 0

    if "--stats" in args:
        if not INDEX_PATH.exists():
            print("  CAPABILITY-INDEX.json not found. Run without --stats to build first.")
            return 1
        index = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
        print(f"\nCapability Index Stats")
        print("=" * 40)
        print(f"  Total capabilities: {index['total_capabilities']}")
        print(f"\n  By category:")
        for cat, data in sorted(index["by_category"].items()):
            print(f"    {cat:<20} {data['count']} tools")
        print(f"\n  By permission class:")
        for pclass, data in sorted(index["by_permission_class"].items()):
            print(f"    {pclass:<6} {data['count']} tools  — {data.get('gate_policy', '')}")
        if index.get("restricted_tools"):
            print(f"\n  Restricted (suspended/retired server): {len(index['restricted_tools'])}")
        print()
        return 0

    # Full rebuild
    mcp_registry = load_mcp_registry()
    tool_registry = load_tool_registry()
    index = build_index(mcp_registry, tool_registry)
    INDEX_PATH.write_text(json.dumps(index, indent=2), encoding="utf-8")
    print(f"\n  [OK] CAPABILITY-INDEX.json rebuilt")
    print(f"       Capabilities: {index['total_capabilities']}  |  Categories: {len(index['by_category'])}  |  Classes: {len(index['by_permission_class'])}")
    if index.get("restricted_tools"):
        print(f"  [WARN] {len(index['restricted_tools'])} tools restricted (suspended/retired servers)")
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
