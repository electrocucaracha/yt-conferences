---
layout: default
title: "Project Lightning Talk: MCP Routing In Linkerd - Flynn, Technical Evangelist"
nav_order: 275
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Flynn, a technical evangelist for the Linkerd project, discusses MCP
  routing in Linkerd, a service mesh that enhances application security, reliability,
  and observability. He explains that MCP is a protocol enabling agents to access
  externa...
resource: https://www.youtube.com/watch?v=tb8rSQz1MGE
tags:
  - kubecon-cloudnativecon-europe-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Flynn, a technical evangelist for the Linkerd project, discusses MCP routing in Linkerd, a service mesh that enhances application security, reliability, and observability.
He explains that MCP is a protocol enabling agents to access external tools, and Linkerd was the first mesh to support it.
Implementing MCP routing in Linkerd required handling stateful routing, as MCP sessions must consistently connect to the same server, and dealing with the protocol’s use of JSON-RPC inside HTTP, where critical information and errors are found in the body rather than headers.
This necessitated advanced payload processing and the ability to parse JSON-RPC, as well as new approaches to authentication and routing based on specific tools.
Flynn concludes by mentioning the introduction of a new resource called MCP route and invites further discussion at the Linkerd booth.

# Main Points

|   # | Main point                                                                                         |
| --: | -------------------------------------------------------------------------------------------------- |
|   1 | Flynn is a technical evangelist for the Linkerd project.                                           |
|   2 | Linkerd is a service mesh focused on security, reliability, and observability for applications.    |
|   3 | Linkerd is the first service mesh to announce support for MCP.                                     |
|   4 | MCP is a protocol that allows agents to access external tools.                                     |
|   5 | In Linkerd, agents communicate with MCP servers via Linkerd proxies running in pods.               |
|   6 | Each pod gets its own Linkerd proxy.                                                               |
|   7 | MCP is a stateful protocol; requests in a session must go to the same MCP server.                  |
|   8 | Stateful routing is required for MCP, which is familiar to infrastructure components.              |
|   9 | MCP uses JSON-RPC inside HTTP; important information is in the body, not headers.                  |
|  10 | Error responses from tools may still return HTTP 200, requiring inspection of the body for errors. |
|  11 | HTTP-only observability is insufficient for MCP; payload processing is necessary.                  |
|  12 | Headers are predictable, but JSON bodies can be large and unordered, making parsing challenging.   |
|  13 | Determining when to give up on incomplete or stalled request bodies is an open question.           |
|  14 | Linkerd treats connections as streams; a single request is a degenerate stream.                    |
|  15 | Supporting MCP required teaching Linkerd to parse JSON-RPC and handle payload processing.          |
|  16 | Linkerd had to address issues with degenerate bodies and stateful routing.                         |
|  17 | Linkerd now supports routing and authentication based on specific tools.                           |
|  18 | A new resource called MCPRoute was added for this functionality.                                   |
|  19 | Additional information is available about Linkerd on EKS and at the escape room party event.       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=tb8rSQz1MGE)
