---
layout: default
title:
  "[Session] Scaling MCP Observability: How Natoma Monitors Thousands of MCP
  Servers"
nav_order: 4
parent: Mcp Dev Summit Eu 2025
type: Video Note
description:
  Capil, a software engineer at Numa Labs, discusses the observability
  challenges and solutions within their MCP platform, which serves as a hosted agent
  access fabric for enterprise adoption. He outlines key challenges such as lack of
  visibi...
resource: https://www.youtube.com/watch?v=09OrzbZC3AU
tags:
  - mcp-dev-summit-eu-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Capil, a software engineer at Numa Labs, discusses the observability challenges and solutions within their MCP platform, which serves as a hosted agent access fabric for enterprise adoption.
He outlines key challenges such as lack of visibility into client-server interactions, difficulties in debugging and tracing requests, and ensuring server quality and security, especially given the variety of server types and the scale of their operations.
To address these, Numa Labs has implemented detailed activity and audit logs at the user and tool level, developed both manual and automated server vetting processes—including static code analysis tools to detect vulnerabilities like tool poisoning and prompt injection—and established policies for managing connections and enforcing security.
Capil also shares examples of how these measures have improved debugging, server safety, and customer transparency, and notes ongoing efforts to enhance observability through open telemetry and more granular analytics.
The talk concludes with a demonstration of their activity dashboard and server scanning tool, highlighting their commitment to robust, scalable observability and security practices.

# Main Points

|   # | Main point                                                                                                                  |
| --: | --------------------------------------------------------------------------------------------------------------------------- |
|   1 | Capil, software engineer at Numa Labs, discusses observability in client-server interactions on the MCP platform.           |
|   2 | Agenda includes platform intro, observability challenges, solutions, and demos.                                             |
|   3 | MCP platform is called Agent Access Fabric, a hosted MCP platform for enterprise adoption.                                  |
|   4 | Focus on scaling, policies, audit logs, data controls, and server registry processes.                                       |
|   5 | Major challenges:                                                                                                           |
|   6 | Lack of visibility in client-server communication.                                                                          |
|   7 | Three server categories: official GitHub repos, remote servers (proxy), and bring-your-own-server.                          |
|   8 | Difficulty tracing which tools are called, call success/failure, and debugging client/customer issues.                      |
|   9 | Quantifying server quality and trust score, especially for community and remote servers.                                    |
|  10 | Debugging issues due to lack of stack traces and request logs in early MVP; improved in current state.                      |
|  11 | Performance monitoring is challenging due to variable tool calls and prompt complexity.                                     |
|  12 | Managing public endpoint latency and scaling connections (personal and managed).                                            |
|  13 | Solutions:                                                                                                                  |
|  14 | Customer-facing activity logs provide granular tracing and audit logs at user and action level.                             |
|  15 | Engineers use logs for server selection, publishing, debugging, and tracing.                                                |
|  16 | Activity logs help customers monitor server/tool usage and predict tool call counts.                                        |
|  17 | Plans to implement OpenTelemetry for more standardized and granular event types and client-server correlation.              |
|  18 | Server vetting process:                                                                                                     |
|  19 | Manual and automatic vetting (static code analysis using a custom tool).                                                    |
|  20 | Tool references vulnerability databases and generates reports on severity, attack categories, and remediation.              |
|  21 | Manual code review for comprehensive security analysis.                                                                     |
|  22 | Example: Slack server required modification for multi-tenancy to prevent cross-tenant data leakage.                         |
|  23 | Common issues found: tool poisoning, prompt injection, hardcoded credentials, protocol compliance, unnecessary permissions. |
|  24 | Request flow: client POST → OAuth/DCR → policy enfo                                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=09OrzbZC3AU)
