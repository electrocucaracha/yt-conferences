---
layout: default
title:
  "The 10x DevOps Engineer’s Toolkit: Argo CD + AI-Dr... Alexander Matyushentsev
  & Leonardo Luz Almeida"
nav_order: 353
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this presentation from the Argo maintainers track at KubeCon, Leonardo
  and Alexander introduce MCP for Argo CD, a new open source protocol designed to
  simplify integration between AI clients and third-party services like Argo CD. MCP
  act...
resource: https://www.youtube.com/watch?v=iC15zeOLZQA
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

In this presentation from the Argo maintainers track at KubeCon, Leonardo and Alexander introduce MCP for Argo CD, a new open source protocol designed to simplify integration between AI clients and third-party services like Argo CD.
MCP acts as a universal connector, allowing AI agents to interact with Argo CD through a simple JSON RPC-based protocol, abstracting away the complexities of direct integration and supporting both local and remote deployments.
The speakers demonstrate practical use cases, such as automating application creation and monitoring deployments, highlighting how MCP enables AI agents to perform tasks that would otherwise require manual intervention.
At Intuit, MCP was leveraged to enhance support workflows by integrating with bots in Slack channels, enabling automated troubleshooting and reducing the support burden across thousands of Kubernetes namespaces and services.
The team also discusses ongoing challenges, such as duplicating troubleshooting logic across different agents, and their exploration of agent skills to centralize and standardize these processes, inviting feedback and collaboration from the community.

# Main Points

|   # | Main point                                                                                                                                               |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Introduction of MCP for Argo CD, a new open source project by Argo maintainers.                                                                          |
|   2 | MCP (Model Connector Protocol) acts as a universal connector between AI clients and third-party services like Argo CD.                                   |
|   3 | MCP enables AI clients to interact with third-party services by providing metadata for actions to be executed.                                           |
|   4 | MCP uses a simple, text-based JSON RPC message format.                                                                                                   |
|   5 | MCP abstracts third-party service logic, allowing AI clients to use a unified protocol.                                                                  |
|   6 | Supports two transport methods: STD error (local) and HTTP (remote), including server-sent events and HTTP2.                                             |
|   7 | MCP protocol includes primitives: tools (functions with parameters), resources (read-only lists supporting events), and prompts (instructions for LLMs). |
|   8 | Authentication is optional; typically, MCP relies on third-party service authentication.                                                                 |
|   9 | MCP for Argo CD is available under Argo Project Labs on GitHub; feedback and contributions are encouraged.                                               |
|  10 | Current implementation focuses on tools, mapping to Argo CD CLI/UI actions (sync, inspect, logs, manifests).                                             |
|  11 | MCP for Argo CD is feature complete for main use cases and used in production at Intuit.                                                                 |
|  12 | Example use cases: creating applications via AI prompts, batch application creation, automated deployment with monitoring and rollback.                  |
|  13 | Intuit operates over 350 Kubernetes clusters, 3,000+ production services, and 50,000+ namespaces.                                                        |
|  14 | Support and troubleshooting are bottlenecks due to scale, knowledge gaps, and data silos.                                                                |
|  15 | Argo CD API helps aggregate data (logs, events, states) for troubleshooting.                                                                             |
|  16 | Initial AI-powered troubleshooting extension using Argo CD API had low adoption; users preferred direct log access.                                      |
|  17 | MCP enabled integration with support bots in Slack, improving support by providing actionable insights and troubleshooting steps.                        |
|  18 | MCP deployment as a reverse proxy simplified communication with 40+ Argo CD instances and improved security.                                             |
|  19 | MCP made AI capabilities accessible to developer workstations and support bots.                                                                          |
|  20 | Real-world exam                                                                                                                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=iC15zeOLZQA)
