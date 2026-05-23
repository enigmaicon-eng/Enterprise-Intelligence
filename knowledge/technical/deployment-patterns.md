---
title: Deployment Patterns for AI Services
domain: technical
created: 2026-05-22
reviewed: 2026-05-22
tags: [deployment, FastAPI, Docker, architecture, AI-ops, microservices, runtime]
connections: [reliability, observability, tracing, ai-debugging, telemetry]
confidence: high
source: original synthesis
---

## Definition
Deployment patterns for AI services are the structural approaches for packaging, running, and operating AI systems in a way that is reproducible, observable, and recoverable. They differ from generic web service patterns because AI services have unique requirements: large, stateful model contexts; non-deterministic behavior; external API dependencies; and quality (not just availability) as an operational concern.

## Why It Matters
How you deploy an AI service determines how easy it is to debug, scale, and improve. Poor deployment choices create systems that are hard to observe, brittle under load, and expensive to change. Good deployment patterns are not about premature production scale — they're about keeping the system legible at every stage.

## The Three-Layer AI Service Architecture

Every AI service has three logical layers. Understanding which layer you're working in is the first step in every architectural decision.

```
┌─────────────────────────────────────┐
│  Layer 1 — Inference Layer          │
│  Makes calls to the model API       │
│  Handles: model selection, caching, │
│  retry logic, cost tracking         │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│  Layer 2 — Memory Layer             │
│  Stores and retrieves context       │
│  Handles: session state, vector     │
│  search, structured history         │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│  Layer 3 — Routing Layer            │
│  Decides what to call and with what │
│  Handles: skill routing, context    │
│  assembly, output dispatch          │
└─────────────────────────────────────┘
```

**Reference implementation:** claude-mem implements all three:
- Inference: SDKAgent → Claude Agent SDK
- Memory: SQLite (structured) + ChromaDB (semantic)
- Routing: hook-command.ts (orchestrator)

## FastAPI for AI Services

FastAPI is the standard framework for Python AI microservices. Its key advantages for AI work: async-native (handles concurrent model calls without blocking), dependency injection (threads config and connections through the service), and automatic OpenAPI docs (makes the API self-documenting).

**Minimal AI service skeleton:**

```python
from fastapi import FastAPI, Depends
from pydantic import BaseModel
import anthropic

app = FastAPI()

# Dependency: shared client with caching
def get_client() -> anthropic.Anthropic:
    return anthropic.Anthropic()

# Request model: typed input
class AnalysisRequest(BaseModel):
    content: str
    tier: str = "analysis"  # capture | analysis | strategy

# Health endpoint: always implement
@app.get("/health")
def health():
    return {"status": "ok"}

# Inference endpoint
@app.post("/analyze")
async def analyze(request: AnalysisRequest, client: anthropic.Anthropic = Depends(get_client)):
    model_map = {
        "capture": "claude-haiku-4-5-20251001",
        "analysis": "claude-sonnet-4-6",
        "strategy": "claude-opus-4-7"
    }
    # Always cache system prompt
    response = client.messages.create(
        model=model_map[request.tier],
        max_tokens=2000,
        system=[{"type": "text", "text": SYSTEM_PROMPT, "cache_control": {"type": "ephemeral"}}],
        messages=[{"role": "user", "content": request.content}]
    )
    return {"output": response.content[0].text}
```

**Required endpoints for any AI service:**
- `GET /health` — returns 200 if service is up
- `GET /metrics` — returns key operational metrics (call count, error rate, cache hit rate)
- `POST /[primary-action]` — the main inference endpoint
- `GET /status` — returns current service state (model connected, memory connected, etc.)

**Middleware to always include:**
- Request ID injection (generates trace_id for each request)
- Request logging (input size, response time, status code)
- Rate limit handling (429 retry with backoff)
- CORS (if serving browser clients)

## Docker for AI Services

Docker solves the AI environment reproducibility problem. Model APIs, SDK versions, dependency combinations, and system libraries must match exactly between development and production. Docker makes this deterministic.

**Minimal Dockerfile for a Python AI service:**

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install dependencies first (layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Non-root user for security
RUN adduser --disabled-password --gecos '' appuser
USER appuser

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

# Start command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Key Dockerfile rules for AI services:**
- Pin all dependency versions (`anthropic==0.49.0`, not `anthropic`)
- Include a HEALTHCHECK — Docker won't know the service is ready without it
- Run as non-root — model API keys shouldn't be accessible to the root user
- Layer dependencies before code — this caches pip installs across code-only changes

**Environment variables (never hardcode):**
```bash
ANTHROPIC_API_KEY=sk-ant-...
MODEL_TIER=analysis
LOG_LEVEL=info
MAX_TOKENS=4000
```

Pass these at runtime: `docker run -e ANTHROPIC_API_KEY=$ANTHROPIC_API_KEY myservice`

## Runtime Diagnostic Endpoints

Every production AI service should expose diagnostic endpoints that answer: "Is everything configured correctly right now?"

```python
@app.get("/status")
async def status():
    return {
        "service": "ok",
        "model_connected": check_model_connection(),
        "memory_connected": check_memory_connection(),
        "cache_status": get_cache_stats(),
        "recent_errors": get_recent_error_count(minutes=5),
        "build": {
            "version": APP_VERSION,
            "model_tier": MODEL_TIER,
            "deployed_at": DEPLOY_TIME
        }
    }
```

This endpoint should return in < 100ms (don't make model API calls in health checks). Cache the connection status with a 10s TTL.

## Deployment Anti-Patterns

| Anti-Pattern | What Goes Wrong | Fix |
|---|---|---|
| Hardcoded API keys | Security exposure; can't rotate without redeploy | Environment variables only |
| No health check | Container appears healthy while service is broken | Add `/health` endpoint; configure HEALTHCHECK |
| Synchronous model calls in web handler | Request queue backs up under load | Use async/await; add request queuing |
| No retry logic | Single transient error causes permanent failure | Implement exponential backoff for 429s and 5xx |
| Mutable system prompt | Cache invalidates on every change | Stabilize the system prompt; version it |
| No request ID | Can't correlate logs across service calls | Inject request_id in middleware; propagate through all logs |
| Logging to stdout only | Logs lost on container restart | Structured JSONL to a mounted volume or log service |
| No /metrics endpoint | Can't monitor without instrumenting | Add prometheus-compatible metrics endpoint |

## Key Principles

- **Three layers, one job each.** Inference layer calls the model. Memory layer stores state. Routing layer decides what to call. Don't mix responsibilities.
- **Environment variables, always.** API keys, model IDs, config values — never in code. Always in the environment.
- **Health check is contract.** A service that doesn't have a working `/health` endpoint is not observable and should not be in production.
- **Pin everything.** Model IDs, SDK versions, dependency versions. Unpinned dependencies break in ways that are hard to reproduce. The Anthropic SDK changes; pin it.
- **Design for the restart.** AI services restart. Containers restart. Design stateless inference layers so restart doesn't corrupt state. Persist state in the memory layer.

## Connections
- [[reliability]] — circuit breakers and retry patterns are implemented in the deployment layer
- [[observability]] — health endpoints and metrics endpoints are the observability surface of the deployment
- [[tracing]] — request ID middleware in FastAPI generates the trace IDs that flow through the system
- [[telemetry]] — logging middleware produces the telemetry stream
- [[ai-debugging]] — diagnostic endpoints are the first stop in infrastructure debugging

## Open Questions
- When does adding a message queue (e.g., Redis) between routing and inference layers become worth the complexity?
- How do you handle model API key rotation in a production service without downtime?
