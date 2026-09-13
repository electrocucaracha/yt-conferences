---
layout: default
title:
  "My MCP Server Code Works, but the Agent Fails: The Case for MCP-specif...
  Calum Murray & Wesley Chun"
nav_order: 67
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  In this talk, Wesley and Callum introduce MCP Checker, an open-source
  evaluation framework developed by Red Hat to assess the semantic interface between
  agents and MCP (Model Control Protocol) servers, particularly in stochastic, agentic
  AI...
resource: https://www.youtube.com/watch?v=r_otBm1fZmM
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

In this talk, Wesley and Callum introduce MCP Checker, an open-source evaluation framework developed by Red Hat to assess the semantic interface between agents and MCP (Model Control Protocol) servers, particularly in stochastic, agentic AI systems where traditional deterministic software testing falls short.
They explain that while agent evals focus on agent behavior and often require code changes, MCP Checker is designed to work with any agent or MCP server without code modifications, capturing all interactions via a proxy and using easy-to-read YAML files for test scenarios.
Through a live demo, they show how MCP Checker can identify whether agents use MCP server tools as intended, providing detailed logs and supporting complex assertions, which is crucial for catching issues that might otherwise go unnoticed, such as unsafe behaviors in Kubernetes environments.
The tool is new and open for contributions, aiming to help developers and enterprises ensure their MCP servers are robust and safe for agent use, with ongoing work to improve statistical analysis of stochastic outcomes.
The session concludes with an invitation for feedback and collaboration, highlighting MCP Checker’s flexibility and value in modern AI infrastructure testing.

# Main Points

|   # | Main point                                                                                                                                                                                                           |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The talk focuses on MCP and introduces the open-source MCP checker project from Red Hat.                                                                                                                             |
|   2 | Wesley and Callum are the presenters; Wesley has a Python and Google/Yahoo background, Callum works in cloud and Kubernetes, maintains Kubernetes MCP server, K native, and created MCP checker.                     |
|   3 | Red Hat contributes significantly to open-source AI projects and builds enterprise versions for large companies.                                                                                                     |
|   4 | AI adoption in enterprises mirrors Linux: open-source projects are wrapped with support, security, and consulting.                                                                                                   |
|   5 | The talk distinguishes between guard rails (preventing unsafe data) and evals (assessing agent/server behavior); focus is on evals.                                                                                  |
|   6 | Traditional software testing (unit, integration, system, acceptance) is deterministic, but LLMs/agents are stochastic and need new evaluation methods.                                                               |
|   7 | Agent evals focus on agent behavior and often require code changes; MCP evals are needed for testing agent-to-MCP server interactions, especially when agent code isn't accessible.                                  |
|   8 | MCP checker is an open-source framework for evaluating MCP servers, designed to work with any agent or MCP server without code changes.                                                                              |
|   9 | MCP checker uses a proxy to log all agent-MCP interactions, supports the agent client protocol, and provides a YAML-based, declarative task format for easy review.                                                  |
|  10 | Demo: MCP checker evaluated a simple MCP server with vague tool names; initial tests showed agents completed tasks but didn't use the expected tools.                                                                |
|  11 | After improving tool names/descriptions, MCP checker confirmed agents used the correct tools, demonstrating measurable improvements.                                                                                 |
|  12 | MCP checker outputs detailed logs and JSON for further analysis.                                                                                                                                                     |
|  13 | Real-world findings on Kubernetes MCP server: code mode reduced task success rate, adding API search improved accuracy but increased token usage, and agents rarely used code mode when both options were available. |
|  14 | MCP checker caught dangerous behaviors, such as agents deleting resources after failed updates, which would be missed by only checking fin                                                                           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=r_otBm1fZmM)
