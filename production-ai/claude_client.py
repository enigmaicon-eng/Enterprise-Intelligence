"""
Core Claude API client for the Enterprise Intelligence Workspace.
Handles model selection, prompt caching, telemetry logging, and retry logic.

Usage:
    from production_ai.claude_client import workspace
    result = workspace.call("Summarize these notes", tier="analysis", workflow="capture")
"""

import asyncio
import json
import secrets
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Literal

import anthropic
from tenacity import retry, stop_after_attempt, wait_exponential

WORKSPACE_ROOT = Path(__file__).parent.parent
TELEMETRY_LOG = WORKSPACE_ROOT / "telemetry" / "api-log.jsonl"
WORKFLOW_LOG = WORKSPACE_ROOT / "telemetry" / "workflow-log.jsonl"
PROMPTS_DIR = WORKSPACE_ROOT / "prompts"
MEMORY_DIR = WORKSPACE_ROOT / "memory"

ModelTier = Literal["capture", "analysis", "strategy"]

MODEL_MAP: dict[ModelTier, str] = {
    "capture": "claude-haiku-4-5-20251001",
    "analysis": "claude-sonnet-4-6",
    "strategy": "claude-opus-4-7",
}

# Session ID shared across all calls in a single script run
SESSION_ID = secrets.token_urlsafe(8)


def load_prompt(path: str) -> str:
    """Load a prompt by relative path from prompts/. E.g. 'workflows/meeting-debrief'."""
    full_path = PROMPTS_DIR / f"{path}.md"
    if not full_path.exists():
        raise FileNotFoundError(f"Prompt not found: {full_path}")
    return full_path.read_text(encoding="utf-8")


def load_memory_context(files: list[str] | None = None) -> str:
    """
    Load memory context. If files is None, loads MEMORY.md index + user_profile.
    Pass specific filenames (without path) for selective loading.
    """
    parts = []

    index = MEMORY_DIR / "MEMORY.md"
    if index.exists():
        parts.append(index.read_text(encoding="utf-8"))

    if files is None:
        profile = MEMORY_DIR / "user_profile.md"
        if profile.exists():
            parts.append(profile.read_text(encoding="utf-8"))
    else:
        for filename in files:
            path = MEMORY_DIR / filename
            if path.exists():
                parts.append(path.read_text(encoding="utf-8"))

    return "\n\n---\n\n".join(parts)


def load_file(relative_path: str) -> str:
    """Load a workspace file by relative path from workspace root."""
    path = WORKSPACE_ROOT / relative_path
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def _ensure_telemetry_dir() -> None:
    TELEMETRY_LOG.parent.mkdir(parents=True, exist_ok=True)


def _log_api(record: dict) -> None:
    _ensure_telemetry_dir()
    with open(TELEMETRY_LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")


def log_workflow(workflow: str, status: str, details: dict | None = None) -> None:
    """Log a workflow run event to the workflow log."""
    _ensure_telemetry_dir()
    record = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "session_id": SESSION_ID,
        "workflow": workflow,
        "status": status,
    }
    if details:
        record.update(details)
    with open(WORKFLOW_LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")


class WorkspaceClient:
    def __init__(self) -> None:
        self._client = anthropic.Anthropic()

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=60),
        reraise=True,
    )
    def _create(self, **kwargs) -> anthropic.types.Message:
        try:
            return self._client.messages.create(**kwargs)
        except anthropic.RateLimitError:
            raise
        except anthropic.APIStatusError as e:
            if e.status_code >= 500:
                raise
            raise RuntimeError(f"Non-retryable API error {e.status_code}: {e.message}") from e

    def call(
        self,
        user_message: str,
        tier: ModelTier = "analysis",
        workflow: str = "general",
        prompt_name: str | None = None,
        extra_system: str = "",
        memory_files: list[str] | None = None,
        include_memory: bool = True,
        max_tokens: int = 4096,
    ) -> str:
        model = MODEL_MAP[tier]

        system_parts: list[str] = []
        if prompt_name:
            system_parts.append(load_prompt(prompt_name))
        if include_memory:
            memory = load_memory_context(memory_files)
            if memory:
                system_parts.append(f"## Workspace Memory\n\n{memory}")
        if extra_system:
            system_parts.append(extra_system)

        system_text = "\n\n---\n\n".join(system_parts) or "You are an operational intelligence assistant."

        start = time.monotonic()
        response = self._create(
            model=model,
            max_tokens=max_tokens,
            system=[{
                "type": "text",
                "text": system_text,
                "cache_control": {"type": "ephemeral"},
            }],
            messages=[{"role": "user", "content": user_message}],
        )
        latency_ms = int((time.monotonic() - start) * 1000)

        usage = response.usage
        _log_api({
            "ts": datetime.now(timezone.utc).isoformat(),
            "session_id": SESSION_ID,
            "workflow": workflow,
            "model": model,
            "prompt_version": prompt_name or "inline",
            "input_tokens": usage.input_tokens,
            "output_tokens": usage.output_tokens,
            "cache_read_tokens": getattr(usage, "cache_read_input_tokens", 0),
            "cache_write_tokens": getattr(usage, "cache_creation_input_tokens", 0),
            "latency_ms": latency_ms,
        })

        return response.content[0].text

    async def call_async(self, **kwargs) -> str:
        """Async wrapper for parallel pipeline stages."""
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, lambda: self.call(**kwargs))

    def call_with_thinking(
        self,
        user_message: str,
        budget_tokens: int = 10000,
        workflow: str = "strategy",
        prompt_name: str | None = None,
    ) -> str:
        """Opus call with extended thinking for deep strategic synthesis."""
        system_parts = [load_prompt("system/strategist")]
        memory = load_memory_context()
        if memory:
            system_parts.append(f"## Workspace Memory\n\n{memory}")
        if prompt_name:
            system_parts.append(load_prompt(prompt_name))

        system_text = "\n\n---\n\n".join(system_parts)

        start = time.monotonic()
        response = self._create(
            model=MODEL_MAP["strategy"],
            max_tokens=16000,
            thinking={"type": "enabled", "budget_tokens": budget_tokens},
            system=[{"type": "text", "text": system_text, "cache_control": {"type": "ephemeral"}}],
            messages=[{"role": "user", "content": user_message}],
        )
        latency_ms = int((time.monotonic() - start) * 1000)

        text = " ".join(b.text for b in response.content if b.type == "text")

        usage = response.usage
        _log_api({
            "ts": datetime.now(timezone.utc).isoformat(),
            "session_id": SESSION_ID,
            "workflow": workflow,
            "model": MODEL_MAP["strategy"],
            "prompt_version": f"{prompt_name or 'inline'}+thinking",
            "thinking_budget": budget_tokens,
            "input_tokens": usage.input_tokens,
            "output_tokens": usage.output_tokens,
            "latency_ms": latency_ms,
        })

        return text


# Module-level singleton — import and reuse rather than reinstantiating
workspace = WorkspaceClient()
