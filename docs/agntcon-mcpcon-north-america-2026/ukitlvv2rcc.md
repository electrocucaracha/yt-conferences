---
layout: default
title: "Stop Making Agents Guess: Engineering Context at the Gateway - Amit Naik, CData"
nav_order: 137
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Amit Naik, VP of AI at CData, presents a solution to the problem of AI agents providing confident but incorrect answers or engaging in token-heavy back-and-forth interactions by integrating context..."
resource: "https://www.youtube.com/watch?v=ukItLVv2rCc"
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

Amit Naik, VP of AI at CData, presents a solution to the problem of AI agents providing confident but incorrect answers or engaging in token-heavy back-and-forth interactions by integrating context engineering into the AI gateway.
He explains that while AI gateways solve IT sprawl by centralizing access to LLMs and MCP servers, they do not inherently ensure data accuracy; this requires a context engine that handles both context recall and accurate retrieval.
The context engine aggregates diverse enterprise information, including structural system context, semantic definitions (such as specific revenue calculations), internal documents, and tacit company knowledge, to provide a comprehensive view of the data.
By leveraging CData’s data virtualization layer, this approach translates natural language queries into deterministic SQL queries, allowing the system to accurately join data from sources like Salesforce and ServiceNow without relying on the LLM to guess relationships.
Although this method introduces trade-offs such as increased upfront setup work and potential latency, Naik argues that it is superior to receiving fast but wrong answers, as it enables the gateway to learn from user interactions and maintain a centralized, governed source of truth for accurate AI responses.

# Main Points

|   # | Main point                                                                                                                                                                                                              |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | ,000 customers, focusing on solving AI sprawl in enterprise environments.                                                                                                                                               |
|   2 | , models, and MCP servers without central governance, leading to a lack of visibility for IT teams.                                                                                                                     |
|   3 | , comprising an LLM gateway for model routing and an MCP gateway for federated tool access to enterprise data.                                                                                                          |
|   4 | , guardrails, usage visibility, and the ability to swap models (e.g., adding new decision models) without rip-and-replace infrastructure changes.                                                                       |
|   5 | , token-burning back-and-forth conversations to clarify ambiguous queries.                                                                                                                                              |
|   6 | : context recall (accessing all relevant enterprise information) and context retrieval (accurately selecting the specific data needed to answer the query).                                                             |
|   7 | : system context (structural data like joins and keys), semantic meaning (business definitions like "revenue"), internal documents (policies and playbooks), and company knowledge (human judgment on account risk).    |
|   8 | ’s Connect AI product uses data virtualization to expose enterprise data as deterministic SQL queries, allowing the context engine to map semantic and system contexts accurately.                                      |
|   9 | , determining "at-risk revenue" involves combining system data (contracts, tickets), semantic definitions, and human-derived signals (support escalations, renewal dates, declining usage) to provide a precise answer. |
|  10 | : it requires upfront work to establish connections and may introduce latency, but it prevents the severe consequences of trusted but wrong answers and saves tokens.                                                   |
|  11 | , whereas the gateway allows for centralized learning from every interaction.                                                                                                                                           |
|  12 | , ensuring that definitions and context remain consistent across different departments and agents.                                                                                                                      |
|  13 | (e.g., Salesforce, ServiceNow) as common MCP tools and SQL constructs, enabling the LLM to generate precise queries rather than dumping raw data.                                                                       |
|  14 | , including white papers and a test harness, are available at cdata.com/ai and on GitHub under CData Software.                                                                                                          |

# Video

[![Video thumbnail](https://img.youtube.com/vi/ukItLVv2rCc/hqdefault.jpg)]("https://www.youtube.com/watch?v=ukItLVv2rCc")

[Watch on YouTube](https://www.youtube.com/watch?v=ukItLVv2rCc)
