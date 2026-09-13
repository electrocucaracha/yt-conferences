---
layout: default
title:
  "MCP Traffic Handling at Scale: Stateless Design, Proxies, and the Roa... Erica
  Hughberg & Boteng Yao"
nav_order: 59
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  The speakers discuss the continued relevance and challenges of running
  MCP (Multi-Channel Protocol) at scale in production environments, highlighting issues
  such as session affinity, policy enforcement, and observability gaps when integrati...
resource: https://www.youtube.com/watch?v=vmlyP862lB8
tags:
  - mcp-dev-summit-na-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The speakers discuss the continued relevance and challenges of running MCP (Multi-Channel Protocol) at scale in production environments, highlighting issues such as session affinity, policy enforcement, and observability gaps when integrating MCP with microservices and enterprise systems.
They explain how Envoy Proxy, an open-source, extensible network proxy, addresses these challenges through features like core filters for MCP awareness, policy enforcement, and observability, as well as mechanisms for converting existing REST APIs to be MCP-compatible.
The conversation emphasizes Envoy’s extensibility through WASM extensions, dynamic modules, and external processes, enabling organizations to adapt legacy systems without extensive rewrites.
They also introduce the Envoy AI Gateway and MCP router, which facilitate scalable, agent-ready architectures and aggregation of multiple MCP servers.
The speakers encourage community involvement, noting that collaboration across companies and expertise is essential for evolving network and AI infrastructure, and invite participants to join the ongoing development and discussion around Envoy and MCP integration.

# Main Points

|   # | Main point                                                                                                                                                |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | MCP is actively used in production, including at high scale.                                                                                              |
|   2 | Production use of MCP introduces issues such as session management and policy enforcement.                                                                |
|   3 | Key production challenges include:                                                                                                                        |
|   4 | Session affinity: MCP is stateful, complicating distributed systems with multiple load balancers.                                                         |
|   5 | Policy enforcement: Determining which agent can call which tools; MCP uses JSON RPC in HTTP body, making policy enforcement at the gateway layer complex. |
|   6 | Observability gap: Difficulty in monitoring MCP traffic compared to traditional HTTP/OpenTelemetry.                                                       |
|   7 | Migration: Need to convert existing REST APIs to MCP for agent discoverability without major rewrites.                                                    |
|   8 | Aggregation: Need to aggregate multiple MCP servers under a single URL.                                                                                   |
|   9 | Envoy Proxy is a mature, open-source, extensible network proxy used widely (including at Google).                                                         |
|  10 | Envoy supports extensibility via WASM extensions, dynamic modules (e.g., Rust, Go), and external processes.                                               |
|  11 | MCP filter in Envoy enables MCP awareness, allowing extraction of tool names and attributes for policy enforcement and observability.                     |
|  12 | MCP2REST bridge in Envoy allows quick conversion of REST APIs to MCP-aware services.                                                                      |
|  13 | MCP router filter enables aggregation of multiple MCP servers/endpoints.                                                                                  |
|  14 | Envoy AI Gateway provides user-friendly, Kubernetes-native control planes for managing Envoy proxies.                                                     |
|  15 | Envoy AI Gateway can run standalone for local traffic processing and supports horizontal scalability while maintaining session context.                   |
|  16 | Ongoing innovations include support for steel transport, gRPC transport, async task support, and improved server/agent discovery and registry.            |
|  17 | Emphasis on security, identity-based policy control, and enhanced observability for MCP traffic.                                                          |
|  18 | Community involvement is encouraged via Slack and direct contact with maintainers.                                                                        |
|  19 | Envoy is critical infrastructure at Google and widely used across cloud services.                                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=vmlyP862lB8)
