---
type: Video Note
title: "Cloud Native Theater | EnvoyCon: External Processing, Internal Leverage: MCP Tool Calls... Jens Kat"
description: "In this talk, Jen Scott, a senior software engineer at ING, explains how ING leverages Envoy’s external processing feature to support agentic AI use cases within its mature service mesh, which connects over 2,000 services across various tec..."
resource: https://www.youtube.com/watch?v=4XciSKk-Rek
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Jen Scott, a senior software engineer at ING, explains how ING leverages Envoy’s external processing feature to support agentic AI use cases within its mature service mesh, which connects over 2,000 services across various technologies.
To enable AI agents to securely and reliably access ING-specific data, the team adopted the Model Context Protocol (MCP), an open standard that bridges AI agents with external systems using JSON RPC.
Rather than requiring each team to implement MCP servers, ING integrates MCP support into Envoy via external processors, which transform and route requests between AI agents and HTTP services, utilizing existing OpenAPI specifications.
This approach centralizes business logic, enhances observability, and avoids burdening individual teams, while also allowing for flexible configuration and governance through an API marketplace.
The solution is running in production at ING, and the team plans to open source their OpenAPI MCP external processor to benefit the wider community.
# Main Points

|   # | Main point                                                                                                            |
| --: | --------------------------------------------------------------------------------------------------------------------- |
|   1 | ING is a bank serving around 40 million customers, with about 60,000 employees, a third in tech.                      |
|   2 | The service mesh team supports over 2,000 services in production.                                                     |
|   3 | ING uses Envoy to enable agentic AI use cases, not to build AI itself.                                                |
|   4 | AI agents at ING require access to ING-specific data to be meaningful.                                                |
|   5 | Model Context Protocol (MCP) is used to connect AI agents with external systems; it's an open JSON RPC standard.      |
|   6 | MCP enables AI agents to interact with ING data via a standardized protocol.                                          |
|   7 | ING decided to bridge MCP (JSON RPC) to HTTP using Envoy, leveraging existing open API documents.                     |
|   8 | Two options considered: off-the-shelf products (like Envoy AI Gateway) or custom implementation using Envoy.          |
|   9 | MCP support is being developed in the Envoy community (MCP filter).                                                   |
|  10 | ING implemented MCP-to-HTTP translation in Envoy using the external processing feature.                               |
|  11 | External processing in Envoy is a gRPC interface allowing request/response transformation.                            |
|  12 | The external processor can send direct responses, abort calls, and access dynamic metadata.                           |
|  13 | MCP initialization and tool listing are handled via direct responses; tool calls are intercepted and transformed.     |
|  14 | The external processor maps JSON RPC tool calls to appropriate HTTP endpoints and wraps responses back into JSON RPC. |
|  15 | Envoy is configured with an HTTP filter chain and points to the gRPC external processor.                              |
|  16 | Mutations like rewriting host headers and HTTP methods require explicit opt-in in Envoy.                              |
|  17 | Observability is integrated; trace context is forwarded and spans are created for each mutation.                      |
|  18 | The solution allows business logic to evolve independently of Envoy releases.                                         |
|  19 | MCP servers are configured per use case, avoiding burden on individual teams.                                         |
|  20 | ING plans to open source the OpenAPI MCP external processor server.                                                   |
|  21 | AI agents can be triggered autonomously or by user interaction; tools are configured per use case.                    |
|  22 | API governance and marketplace ensure correct mapping and prevent unwanted cross-talk                                 |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=4XciSKk-Rek)