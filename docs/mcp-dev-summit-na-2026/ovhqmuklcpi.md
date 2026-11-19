---
layout: default
title: Small Language Models Need a Different MCP
nav_order: 85
parent: MCP Dev Summit NA 2026
type: Video Note
description: "Chiara Dotson argues that the Model Context Protocol (MCP), currently optimized for cloud environments, is ill-suited for the growing Edge AI market due to its reliance on high bandwidth, persisten..."
resource: "https://www.youtube.com/watch?v=ovhQMuKLcpI"
tags:
  - mcp-dev-summit-na-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-15T16:54:07+00:00
---

# Summary

Chiara Dotson argues that the Model Context Protocol (MCP), currently optimized for cloud environments, is ill-suited for the growing Edge AI market due to its reliance on high bandwidth, persistent connectivity, and large compute budgets.
To address these limitations, she proposes three key enhancements: first, replacing JSON-RPC with binary Protocol Buffers to reduce payload sizes by up to 25 times and accelerate parsing; second, implementing MQTT-based transport with local persistence and session continuity to ensure reliable communication over intermittent networks; and third, introducing content-addressable caching and local-first resource discovery to minimize redundant data transfers and separate high-volume media streams from the MCP analysis layer.
These additive, backward-compatible changes allow MCP to operate efficiently on constrained devices in sectors like manufacturing and healthcare, ensuring that critical AI applications can function reliably in the physical world without waiting for broader consensus.

# Main Points

|   # | Main point                                                                                                                                                                                                   |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | The Model Context Protocol (MCP) was designed for cloud environments but is increasingly being deployed at the edge, where constrained devices and unreliable networks create significant challenges.        |
|   2 | Current MCP design assumes high bandwidth, persistent connectivity, and ample compute resources, which are often unavailable in edge scenarios involving small language models with limited context windows. |
|   3 | Binary MCP proposes replacing JSON-RPC with Protocol Buffers to reduce payload sizes by 20 to 25 times and improve parsing speeds by 10 to 50 times.                                                         |
|   4 | This binary approach maintains backward compatibility through capability negotiation during connection setup, allowing legacy servers to continue using JSON while new systems utilize binary transport.     |
|   5 | Semantic tool compression allows clients to request concise tool descriptions during discovery, reducing context consumption, with the option to fetch full schemas only when necessary.                     |
|   6 | Relevance-based tool filtering enables clients to pass session context so servers return only relevant tools, reducing the probability of tool hallucination and minimizing the attack surface.              |
|   7 | Standard transports like SSE and standard IO are fragile against intermittent connectivity, causing session loss and failed tool calls during network blips or device sleep cycles.                          |
|   8 | A resilient transport architecture using MQTT and local persistence layers ensures tool calls are durable, surviving crashes and network drops by storing intents in a local outbox before transmission.     |
|   9 | Session continuity is achieved by including session IDs and sequence numbers in message headers, allowing servers to replay missed notifications and enabling models to resume reasoning after reconnection. |
|  10 | Context content-addressable caching uses resource hashes to prevent redundant data transfers, allowing clients to skip downloads if local data matches the server's current state.                           |
|  11 | Local-first resource discovery separates data transportation from analysis, using specialized URIs to stream high-volume data like video directly to models without passing through the MCP server envelope. |
|  12 | This separation ensures the MCP server acts as the intelligent decision layer while raw media flows directly to processing units, optimizing for latency and bandwidth in real-time applications.            |
|  13 | These proposals are additive and backward-compatible, allowing existing cloud deployments to remain unchanged while edge deployments gain necessary optimizations for constrained environments.              |
|  14 | The edge AI market is projected to reach 80 billion dollars by 2029, driving the need for protocol adaptations that address physical world constraints such as power management and network instability.     |

# Video

[![Video thumbnail](https://img.youtube.com/vi/ovhQMuKLcpI/hqdefault.jpg)](https://www.youtube.com/watch?v=ovhQMuKLcpI)

[Watch on YouTube](https://www.youtube.com/watch?v=ovhQMuKLcpI)
