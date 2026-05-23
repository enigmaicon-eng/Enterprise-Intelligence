# AI Stack
## Integration Layer for Operational Intelligence

---

## Model Selection Strategy

| Use Case | Model | Why |
|----------|-------|-----|
| Quick capture, tagging, classification | `claude-haiku-4-5-20251001` | Sub-second, low cost, sufficient for structure |
| Analysis, synthesis, meeting debrief | `claude-sonnet-4-6` | Best cost/quality for reasoning tasks |
| Strategy, cross-domain, long-horizon | `claude-opus-4-7` | Maximum reasoning, extended thinking for complex synthesis |
| Code generation, automation scripts | `claude-sonnet-4-6` | Strong code, fast feedback loop |

**Never use Opus for:** Daily briefings, note tagging, template filling, or any task where Sonnet suffices. Cost compounds.

---

## Prompt Caching — Non-Negotiable

Every API call must implement prompt caching. The system prompt (including loaded workspace context) is expensive to process repeatedly. Cache it.

```python
import anthropic

client = anthropic.Anthropic()

def call_claude(system_prompt: str, user_message: str, model: str = "claude-sonnet-4-6"):
    response = client.messages.create(
        model=model,
        max_tokens=4096,
        system=[
            {
                "type": "text",
                "text": system_prompt,
                "cache_control": {"type": "ephemeral"}  # Cache the system prompt
            }
        ],
        messages=[{"role": "user", "content": user_message}]
    )
    
    # Log telemetry
    log_api_call(
        model=model,
        input_tokens=response.usage.input_tokens,
        output_tokens=response.usage.output_tokens,
        cache_read_tokens=getattr(response.usage, 'cache_read_input_tokens', 0),
        cache_write_tokens=getattr(response.usage, 'cache_creation_input_tokens', 0),
    )
    
    return response.content[0].text
```

**Cache hit rate target:** >60% on repeated workflow runs. If below 40%, your system prompt is varying too much between calls.

---

## Core Client (`production-ai/claude_client.py`)

```python
"""
Core Claude API client for the operational intelligence workspace.
Handles model selection, prompt caching, telemetry, and retry logic.
"""

import asyncio
import json
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Literal

import anthropic

WORKSPACE_ROOT = Path(__file__).parent.parent
TELEMETRY_LOG = WORKSPACE_ROOT / "telemetry" / "api-log.jsonl"
PROMPTS_DIR = WORKSPACE_ROOT / "prompts"
MEMORY_DIR = WORKSPACE_ROOT / "memory"

ModelTier = Literal["capture", "analysis", "strategy"]

MODEL_MAP: dict[ModelTier, str] = {
    "capture": "claude-haiku-4-5-20251001",
    "analysis": "claude-sonnet-4-6",
    "strategy": "claude-opus-4-7",
}


def load_prompt(name: str) -> str:
    """Load a prompt template by name from the prompts directory."""
    path = PROMPTS_DIR / f"{name}.md"
    if not path.exists():
        raise FileNotFoundError(f"Prompt not found: {name}")
    return path.read_text(encoding="utf-8")


def load_memory_context() -> str:
    """Load all memory files as context string."""
    memory_index = MEMORY_DIR / "MEMORY.md"
    if not memory_index.exists():
        return ""
    
    parts = [memory_index.read_text(encoding="utf-8")]
    for f in MEMORY_DIR.glob("*.md"):
        if f.name != "MEMORY.md":
            parts.append(f"\n\n---\n{f.read_text(encoding='utf-8')}")
    
    return "\n".join(parts)


def _log_api_call(data: dict) -> None:
    TELEMETRY_LOG.parent.mkdir(parents=True, exist_ok=True)
    with open(TELEMETRY_LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps(data) + "\n")


class WorkspaceClient:
    def __init__(self):
        self.client = anthropic.Anthropic()
    
    def call(
        self,
        user_message: str,
        tier: ModelTier = "analysis",
        workflow: str = "general",
        prompt_name: str | None = None,
        extra_system: str = "",
        max_tokens: int = 4096,
        include_memory: bool = True,
    ) -> str:
        model = MODEL_MAP[tier]
        
        # Build system prompt
        system_parts = []
        if prompt_name:
            system_parts.append(load_prompt(prompt_name))
        if include_memory:
            memory = load_memory_context()
            if memory:
                system_parts.append(f"\n\n## Workspace Memory\n{memory}")
        if extra_system:
            system_parts.append(extra_system)
        
        system_text = "\n\n".join(system_parts) if system_parts else "You are an operational intelligence assistant."
        
        start = time.monotonic()
        response = self.client.messages.create(
            model=model,
            max_tokens=max_tokens,
            system=[
                {
                    "type": "text",
                    "text": system_text,
                    "cache_control": {"type": "ephemeral"},
                }
            ],
            messages=[{"role": "user", "content": user_message}],
        )
        latency_ms = int((time.monotonic() - start) * 1000)
        
        usage = response.usage
        _log_api_call({
            "ts": datetime.now(timezone.utc).isoformat(),
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
    ) -> str:
        """Strategy-tier call with extended thinking enabled."""
        system_text = load_prompt("system/strategist") + "\n\n" + load_memory_context()
        
        start = time.monotonic()
        response = self.client.messages.create(
            model=MODEL_MAP["strategy"],
            max_tokens=16000,
            thinking={"type": "enabled", "budget_tokens": budget_tokens},
            system=[{"type": "text", "text": system_text, "cache_control": {"type": "ephemeral"}}],
            messages=[{"role": "user", "content": user_message}],
        )
        latency_ms = int((time.monotonic() - start) * 1000)
        
        # Extract text blocks only (not thinking blocks)
        text = " ".join(
            block.text for block in response.content if block.type == "text"
        )
        
        _log_api_call({
            "ts": datetime.now(timezone.utc).isoformat(),
            "workflow": workflow,
            "model": MODEL_MAP["strategy"],
            "prompt_version": "strategist+thinking",
            "thinking_budget": budget_tokens,
            "input_tokens": response.usage.input_tokens,
            "output_tokens": response.usage.output_tokens,
            "latency_ms": latency_ms,
        })
        
        return text


# Singleton for import reuse
workspace = WorkspaceClient()
```

---

## Batch Processing (`production-ai/batch_processor.py`)

For non-time-sensitive synthesis (e.g., end-of-week knowledge base updates), use the Anthropic Batch API. Cost is ~50% of synchronous calls.

```python
"""
Batch processor for non-urgent synthesis tasks.
Submits jobs to Anthropic Message Batches API, polls for completion.
"""

import anthropic
import json
import time
from pathlib import Path

client = anthropic.Anthropic()


def submit_knowledge_synthesis_batch(notes_dir: Path) -> str:
    """Submit a batch job to synthesize all raw notes into knowledge entries."""
    
    notes = list(notes_dir.glob("*.md"))
    if not notes:
        return None
    
    requests = []
    for note in notes:
        content = note.read_text(encoding="utf-8")
        requests.append(
            anthropic.types.message_create_params.Request(
                custom_id=note.stem,
                params=anthropic.types.MessageCreateParamsNonStreaming(
                    model="claude-sonnet-4-6",
                    max_tokens=2048,
                    messages=[{
                        "role": "user",
                        "content": f"Synthesize this raw note into a structured knowledge entry:\n\n{content}"
                    }],
                    system="You are a knowledge synthesis agent. Convert raw notes into well-structured knowledge base entries with frontmatter, clear concept definition, connections to related topics, and practical implications."
                )
            )
        )
    
    batch = client.messages.batches.create(requests=requests)
    return batch.id


def poll_batch(batch_id: str, max_wait_minutes: int = 30) -> dict[str, str]:
    """Poll batch until complete, return results by custom_id."""
    deadline = time.time() + max_wait_minutes * 60
    
    while time.time() < deadline:
        batch = client.messages.batches.retrieve(batch_id)
        
        if batch.processing_status == "ended":
            results = {}
            for result in client.messages.batches.results(batch_id):
                if result.result.type == "succeeded":
                    results[result.custom_id] = result.result.message.content[0].text
            return results
        
        time.sleep(30)
    
    raise TimeoutError(f"Batch {batch_id} did not complete within {max_wait_minutes} minutes")
```

---

## Agent Orchestration Patterns

### Pattern 1 — Sequential Pipeline

```python
async def meeting_intelligence_pipeline(transcript: str) -> dict:
    ws = WorkspaceClient()
    
    # Stage 1: Structure (Haiku — fast)
    structured = ws.call(
        user_message=transcript,
        tier="capture",
        workflow="meeting-structure",
        prompt_name="workflows/meeting-structure",
    )
    
    # Stage 2: Deep analysis (Sonnet)
    analysis = ws.call(
        user_message=structured,
        tier="analysis",
        workflow="meeting-debrief",
        prompt_name="workflows/meeting-debrief",
    )
    
    return {"structured": structured, "analysis": analysis}
```

### Pattern 2 — Parallel Fan-Out

```python
async def weekly_review_pipeline() -> str:
    ws = WorkspaceClient()
    
    # Load all inputs in parallel
    tasks = [
        ws.call_async(user_message=load_action_items(), tier="analysis", workflow="action-review"),
        ws.call_async(user_message=load_meeting_summaries(), tier="analysis", workflow="meeting-patterns"),
        ws.call_async(user_message=load_knowledge_additions(), tier="analysis", workflow="learning-review"),
    ]
    
    results = await asyncio.gather(*tasks)
    
    # Synthesize all parallel outputs (Opus if warranted)
    combined = "\n\n---\n\n".join(results)
    synthesis = ws.call(
        user_message=combined,
        tier="strategy",
        workflow="weekly-synthesis",
        prompt_name="workflows/weekly-synthesis",
    )
    
    return synthesis
```

### Pattern 3 — Recursive Compression

When context grows beyond 100K tokens, use compression before synthesis:

```python
def compress_context(documents: list[str], target_tokens: int = 20000) -> str:
    ws = WorkspaceClient()
    
    chunks = chunk_documents(documents, max_tokens=40000)
    compressed_chunks = []
    
    for chunk in chunks:
        compressed = ws.call(
            user_message=chunk,
            tier="analysis",
            workflow="context-compression",
            prompt_name="workflows/compress",
        )
        compressed_chunks.append(compressed)
    
    if len(compressed_chunks) == 1:
        return compressed_chunks[0]
    
    # Recurse if still too large
    return compress_context(compressed_chunks, target_tokens)
```

---

## Error Handling Standards

```python
import anthropic
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=4, max=60),
    reraise=True,
)
def resilient_call(client: anthropic.Anthropic, **kwargs):
    try:
        return client.messages.create(**kwargs)
    except anthropic.RateLimitError:
        raise  # tenacity will retry
    except anthropic.APIStatusError as e:
        if e.status_code >= 500:
            raise  # retry on server errors
        raise RuntimeError(f"Non-retryable API error: {e.status_code}") from e
```

---

## Cost Model

Approximate costs per workflow at current API pricing:

| Workflow | Model | Est. Input Tokens | Est. Output Tokens | Est. Cost |
|----------|-------|-------------------|-------------------|-----------|
| Daily briefing | Sonnet | 8,000 | 500 | ~$0.03 |
| Meeting debrief | Sonnet | 12,000 | 2,000 | ~$0.05 |
| Weekly review | Opus | 40,000 | 5,000 | ~$0.85 |
| Monthly strategy | Opus+thinking | 80,000 | 10,000 | ~$3.50 |
| Note capture (batch) | Sonnet batch | 2,000 | 500 | ~$0.004 |

**Monthly budget estimate (active use):** $30–80/month  
**Prompt caching reduces this by 40–60%** on repeated workflow patterns.
