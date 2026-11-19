---
layout: default
title: "How Uber Runs 60,000 AI Agent Tasks Per Week With MCP"
nav_order: 74
parent: MCP Dev Summit NA 2026
type: Video Note
description: "Meghna and Rush from Uber present their journey in scaling Model Context Protocol (MCPs) to support over 5,000 engineers and 10,000 services, addressing critical challenges in development lifecycle..."
resource: "https://www.youtube.com/watch?v=yVqMxBahjfA"
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

Meghna and Rush from Uber present their journey in scaling Model Context Protocol (MCPs) to support over 5,000 engineers and 10,000 services, addressing critical challenges in development lifecycle, security governance, and tool discovery.
To solve these issues, they built a centralized MCP gateway and registry that automatically translates service endpoints into standardized tools, enforcing strict security measures such as PII redaction, code scanning, and centralized authorization.
This infrastructure supports three primary consumption surfaces: the no-code Uber Agent Builder, the code-first Uber Agent SDK, and coding agents like Cloud Code and Cursor, which collectively handle thousands of active agents and tens of thousands of weekly executions.
The system enhances reliability by allowing users to explicitly select specific tools and override parameters, thereby reducing LLM hallucinations and ensuring consistent performance.
Looking ahead, Uber plans to improve MCP quality by integrating evaluation metrics, service-level agreements, and a dedicated tool search feature, while also making "skills"—reusable recipes for MCP usage—shareable and subject to rigorous A/B testing and output quality evaluations.

# Main Points

|   # | Main point                                                                                                                                                                     |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Meghna and Rush from Uber lead the agentic AI platform and share their journey of scaling MCPs across thousands of engineers, services, and agents.                            |
|   2 | Over 5,000 Uber engineers use AI for agentic workflows monthly, with more than 1,500 active internal agents and over 60,000 executions per week.                               |
|   3 | Uber operates more than 10,000 services, creating a complex landscape where MCPs are essential for standardizing agent interactions and preventing chaos.                      |
|   4 | Key challenges included the lack of a standard development lifecycle, security governance concerns due to bespoke integrations, and difficulties in discovering reliable MCPs. |
|   5 | Uber built an MCP gateway and registry to serve as the control plane for all MCP interactions, enforcing consistency and removing duplication.                                 |
|   6 | A config-driven approach automatically translates Uber service endpoints into MCP tools, allowing service owners to control exposure and fine-tune descriptions for LLMs.      |
|   7 | Third-party MCPs undergo stricter gating, scanning, and rigorous checks compared to trusted internal systems to mitigate data handling risks.                                  |
|   8 | Security measures include central authorization integration, PII redaction, periodic code scanning for bad patterns, and observability guardrails to block mutable endpoints.  |
|   9 | The gateway architecture features an orchestrator that generates MCP definitions from service IDLs and a gateway service that serves these servers to consumers.               |
|  10 | The orchestrator crawls proto and thrift files, uses an LLM to generate tool descriptions, and stores definitions in object storage for the gateway service to pick up.        |
|  11 | Service owners update MCP definitions via pull requests, which are scanned by engineering security APIs before being committed and deployed.                                   |
|  12 | Three main surfaces use MCPs at Uber: the no-code Uber Agent Builder, the code-first Uber Agent SDK, and coding agents like Cloud Code and Cursor.                             |
|  13 | The Uber Agent Builder allows users to scope MCPs in system instructions, select specific tools to reduce hallucination, and override parameters for reliability.              |
|  14 | The Uber Agent SDK uses a YAML config file to define MCP names, select tools, and override parameters, automatically loading these configurations for agents.                  |
|  15 | Coding agents utilize the AIFXC tool to add remote or local MCP servers, making them available to IDE-based agents and background agents like Minions.                         |
|  16 | The roadmap focuses on improving MCP server quality by extending the registry with evaluation metrics, SLAs, and reliability data to surface high-tier tools.                  |
|  17 | Uber is developing a tool search feature to improve discovery accuracy and reduce context bloat by enabling automatic and on-demand tool identification.                       |
|  18 | Skills, described as recipes for using MCPs, are being made shareable across teams with plans to introduce evaluations for output quality, correctness, and A/B testing.       |

# Video

[![Video thumbnail](https://img.youtube.com/vi/yVqMxBahjfA/hqdefault.jpg)](https://www.youtube.com/watch?v=yVqMxBahjfA)

[Watch on YouTube](https://www.youtube.com/watch?v=yVqMxBahjfA)
