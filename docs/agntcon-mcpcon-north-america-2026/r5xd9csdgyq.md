---
layout: default
title: "The MCP Cold-Start Problem: When Your Agent Has 100 Tools and Has to... - Karthik Karunanithi, Ibm"
nav_order: 124
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Karthik Karunanithi from IBM presents a framework for securing and optimizing agentic systems in regulated industries, arguing that while MCP servers simplify tool integration, they create signific..."
resource: "https://www.youtube.com/watch?v=R5xD9csdGyQ"
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

Karthik Karunanithi from IBM presents a framework for securing and optimizing agentic systems in regulated industries, arguing that while MCP servers simplify tool integration, they create significant security and performance challenges as tool catalogs scale from demos to hundreds of enterprise tools.
He highlights that the primary bottleneck is not model accuracy, which remains high even with many tools, but rather the "cold start" problem where agents must read large tool descriptions, causing latency spikes—up to 21 seconds if tool order is unstable—and exposing systems to prompt injection attacks via manipulated tool descriptions.
To address this, Karunanithi proposes a four-step playbook: authorize access to limit visible tools, rank them using a search-first approach to reduce context load, enforce guardrails to prevent unauthorized actions, and audit every step to ensure traceability.
He emphasizes that security should not rely on the model’s judgment alone but on external layers like MCP gateways and control planes that manage permissions, short-lived keys, and structured logging.
Ultimately, he advises building robust guardrails around the "black box" of AI models to ensure scalability and trust in production environments, summarizing the core mantra as "authorize, rank, and audit."

# Main Points

|   # | Main point                                                                                                                                                                                                                                                                |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | :** Enterprise agentic systems face significant security and auditability challenges when scaling from demo environments (3 tools) to production (60–800+ tools), where permissions and boundaries often become undefined.                                                |
|   2 | "Black Box" Problem:** AI models operate as opaque neural networks; unlike physical structures with known load limits, there is no definitive threshold for how many tools an agent can handle before performance or safety degrades.                                     |
|   3 | :** While controlled experiments showed high accuracy (22/22 correct tool selections) even with many tools, real-world industry data (e.g., Anthropic) indicates significant accuracy drops (up to 46%) and increased latency when tool catalogs are large or disordered. |
|   4 | & Latency:** Agents must read the entire tool catalog before acting. Shuffling tool order during execution can increase latency from ~1 second to ~21 seconds, highlighting the critical need for stable tool ordering to leverage caching.                               |
|   5 | :** Tool descriptions act as ranking hints. Malicious or accidental changes to descriptions can manipulate tool selection (prompt injection/gaming), as the model relies on text to determine relevance.                                                                  |
|   6 | :** Tools can be modified (e.g., description changes) without explicit notification in the payload. This can cause unexpected agent behavior and invalidate caches, necessitating fingerprinting of every tool to detect changes.                                         |
|   7 | :** Implementing a search-based discovery layer (exposing only 3 meta-tools: search, get details, call) significantly improves performance. Anthropic evaluations showed accuracy improving from 49% to 76% using this approach.                                          |
|   8 | :**                                                                                                                                                                                                                                                                       |
|   9 | :** Use stateless MCP requests with identity to filter tools based on user/agent permissions.                                                                                                                                                                             |
|  10 | :** Search only within the authorized subset of tools, not the entire catalog.                                                                                                                                                                                            |
|  11 | :** Implement guardrails to verify actions, as models may claim refusal while tools execute in the background.                                                                                                                                                            |
|  12 | :** Log every metric and decision to create a true audit trail, not just a record of what ran.                                                                                                                                                                            |
|  13 | :** Deploy a control plane and MCP gateway to manage rules, guardrails, and short-lived keys (Vault) with TTLs to minimize long-term credential risks.                                                                                                                    |
|  14 | :** Logs must explain _why_ an action occurred (rule engine decisions, versions), not just _what_ happened, to satisfy compliance in regulated industries.                                                                                                                |
|  15 | :** Do not rely solely on model judgment. Build robust layers of authorization, ranking, enforcement, and auditing around the "black box" to ensure scalability and security in production.                                                                               |

# Video

[![Video thumbnail](https://img.youtube.com/vi/R5xD9csdGyQ/hqdefault.jpg)]("https://www.youtube.com/watch?v=R5xD9csdGyQ")

[Watch on YouTube](https://www.youtube.com/watch?v=R5xD9csdGyQ)
