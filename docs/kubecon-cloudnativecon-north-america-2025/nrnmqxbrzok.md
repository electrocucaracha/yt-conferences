---
layout: default
title:
  "Designing Platforms With Judgment: Agentic Flows With MCP - Shivay Lamba &
  Ekansh Gupta"
nav_order: 60
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  In this session, Ianch and Shai discuss the evolution of platform engineering
  from traditional, reactive approaches—where human intervention is heavily required
  for tasks like deployment, observability, and incident management—towards more...
resource: https://www.youtube.com/watch?v=nrNmqxbRzok
tags:
  - kubecon-cloudnativecon-north-america-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

In this session, Ianch and Shai discuss the evolution of platform engineering from traditional, reactive approaches—where human intervention is heavily required for tasks like deployment, observability, and incident management—towards more proactive, agentic workflows enabled by the Model Context Protocol (MCP).
They explain that while large language models (LLMs) can provide suggestions, they lack the ability to execute tasks autonomously, which MCP addresses by allowing LLMs to interact with external tools and APIs through standardized protocols.
The presenters demonstrate how MCP servers, equipped with various tools, can automate tasks such as debugging, scaling infrastructure, and even creating pull requests to fix issues, thereby reducing manual intervention.
They showcase practical examples using open-source tools like Kagent and Docker MCP toolkit, highlighting how these systems can proactively identify and resolve problems in cloud-native environments.
Despite these advancements, they caution that MCP is still maturing, with security and reliability concerns necessitating continued human oversight and rigorous testing before full production adoption.

# Main Points

|   # | Main point                                                                                                                                                              |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Ianch and Shai introduce themselves and their backgrounds in software engineering and cloud-native communities.                                                         |
|   2 | The session focuses on designing proactive, judgment-driven platforms using agentic flows and MCP (Model Context Protocol).                                             |
|   3 | Traditional platform engineering relies heavily on human intervention, especially for CI/CD, observability, and incident management.                                    |
|   4 | Observability typically uses OpenTelemetry and backends like Signoz, Prometheus, and Grafana to collect metrics, events, logs, and traces.                              |
|   5 | Incident management tools like PagerDuty and Slack require engineers to be on call, leading to pain points and reactive workflows.                                      |
|   6 | Platform engineering has evolved in the last five years with declarative, event-driven systems (e.g., GitOps), infrastructure as code, and explosion of telemetry data. |
|   7 | LLMs (Large Language Models) like ChatGPT provide suggestions but still require manual intervention for fixes.                                                          |
|   8 | MCP is an open standard protocol enabling LLMs to connect with tools, databases, APIs, and automate tasks.                                                              |
|   9 | MCP servers host tools (function calls) that LLMs can use to perform operations (e.g., database queries, Slack alerts).                                                 |
|  10 | MCP clients allow LLMs to interact with multiple MCP servers using various protocols (e.g., remote MCP, SSC).                                                           |
|  11 | Platform engineers can use MCP to automate scaling, cost management, security scanning, and incident response.                                                          |
|  12 | Demo shows MCP-enabled GitOps operator and KAgent automating error detection and fixes via GitHub PRs.                                                                  |
|  13 | Docker MCP toolkit allows hosting and managing MCP servers, including secret management.                                                                                |
|  14 | MCP can automate root cause analysis by analyzing logs and traces, and trigger alerts or fixes.                                                                         |
|  15 | Cape (Community AI Platform Engineering) is a CNCF project providing multi-agent AI systems for platform engineering.                                                   |
|  16 | Cape integrates with tools like Backstage, VS Code, ArgoCD, PagerDuty, GitHub, and Jira via agents.                                                                     |
|  17 | Agent-to-agent (A2A) protocol complements MCP for agent communication and proactive workflows.                                                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=nrNmqxbRzok)
