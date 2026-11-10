---
layout: default
title: "Workshop: Stack It Yourself: Open Infrastructure for AI... - Brian Benz & Pamela Fox, Microsoft"
nav_order: 121
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "This workshop demonstrates how to build and manage a local AI agent application using Docker Compose, Python, and the Pydantic AI framework."
resource: "https://www.youtube.com/watch?v=3b2FC5FdL3M"
tags:
  - agntcon-mcpcon-north-america-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-08T02:03:18+00:00
---

# Summary

This workshop demonstrates how to build and manage a local AI agent application using Docker Compose, Python, and the Pydantic AI framework.
The session begins by establishing a local inference baseline with the Qwen 1.7B model via Ollama, illustrating how to switch from the legacy Chat Completions API to the modern OpenAI Responses API without altering the underlying application code.
The presenters then integrate observability using the LGTM stack (Loki, Grafana, Tempo, and Prometheus) to visualize agent loops, trace requests, and monitor performance metrics.
A key focus is on durable state management, where Redis is implemented to store conversation history, ensuring that context persists even if the agent container is destroyed or restarted.
Finally, the workshop incorporates Model Context Protocol (MCP) servers to provide the agent with grounded tools for retrieving specific conference data and current time, demonstrating how to enhance agent accuracy and traceability through external tool integration.

# Main Points

|   # | Main point                                                                                                                                             |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | , Ollama, and a Python backend (Pydantic AI and FastAPI).                                                                                              |
|   2 | , selected for its open-source license and CPU compatibility.                                                                                          |
|   3 | , allowing the model to be stopped or swapped without losing the agent process.                                                                        |
|   4 | , which is now an open standard donated to the Agentic AI Foundation.                                                                                  |
|   5 | (Loki, Grafana, Tempo, Prometheus) fed by OpenTelemetry traces.                                                                                        |
|   6 | , model calls, token usage, and timing, enabling performance troubleshooting and accountability.                                                       |
|   7 | , ensuring context persists even if the agent container is destroyed or restarted.                                                                     |
|   8 | , trimming history to a maximum of 50 turns and setting expiration times.                                                                              |
|   9 | (Model Context Protocol) tools are integrated to provide grounded data, such as listing workshops or checking current time, improving answer accuracy. |
|  10 | , with configuration changes handled via Docker Compose profiles and environment files rather than code changes.                                       |
|  11 | , and FastAPI for asynchronous handling of LLM calls.                                                                                                  |
|  12 | , with provided scripts for scaling agents, Redis, and inference tiers across cloud platforms.                                                         |
|  13 | , noting that models do not inherently store conversation state; an external context engine is required.                                               |
|  14 | , telemetry state, and conversation IDs for tracking.                                                                                                  |
|  15 | , demonstrating the feasibility of building complex agent harnesses with modern tools.                                                                 |
|  16 | , observable, and durable agent applications that can be deployed on-premise or in the cloud.                                                          |

# Video

[![Video thumbnail](https://img.youtube.com/vi/3b2FC5FdL3M/hqdefault.jpg)](https://www.youtube.com/watch?v=3b2FC5FdL3M)

[Watch on YouTube](https://www.youtube.com/watch?v=3b2FC5FdL3M)
