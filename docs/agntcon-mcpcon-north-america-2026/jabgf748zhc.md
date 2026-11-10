---
layout: default
title: "Where Did All My Tokens Go? Using Agentgateway to Keep Your AI Usage... - Shane O'Donnell, solo.io"
nav_order: 78
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Shane, VP of Engineering at Solo.io, presents Agent Gateway as an AI-native solution to address the challenge of tracking and controlling LLM token consumption."
resource: "https://www.youtube.com/watch?v=jABgf748zHc"
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

Shane, VP of Engineering at Solo.io, presents Agent Gateway as an AI-native solution to address the challenge of tracking and controlling LLM token consumption.
The talk highlights three core capabilities: attributing every API call to specific users or agents, converting token usage into accurate US dollar costs, and enforcing budget limits to prevent overspending.
By centralizing access through virtual API keys, the gateway eliminates the need for direct provider keys, enabling fine-grained metadata tracking and cost attribution that goes beyond simple provider-level billing.
The presentation includes a live demonstration of installing Agent Gateway, configuring providers like Anthropic and OpenAI, and implementing user-specific budget constraints and model access restrictions.
Additionally, the speaker showcases advanced features such as semantic routing, context trimming, and guardrails for content moderation, emphasizing that Agent Gateway is an open-source project designed to provide both robust AI-specific controls and traditional API gateway reliability.

# Main Points

|   # | Main point                                                                                                                                                                                                                                          |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | :** Organizations struggle to attribute LLM API calls to specific users or agents, convert token usage into accurate US dollar costs, and enforce spending budgets, often resulting in opaque top-level provider bills.                             |
|   2 | :** Implementing a centralized AI-native gateway (Agent Gateway) between users/agents and LLM providers to serve as a single point for observability, security, and policy enforcement.                                                             |
|   3 | :** Built by Solo.io, it combines traditional API gateway capabilities (timeouts, retries, failover) with AI-specific features like inference routing, LLM management, and MCP server control.                                                      |
|   4 | & Security:** Replaces direct provider API keys with gateway-issued "virtual keys," allowing fine-grained access control, metadata tagging (e.g., team, user), and centralized key management to prevent leaks and simplify onboarding/offboarding. |
|   5 | :** Includes a built-in cost catalog that converts input/output tokens, cache reads/writes, and different model prices into dollar amounts, supporting overrides for bulk discounts and real-time analytics.                                        |
|   6 | :** Enables granular rate limiting and budget caps (e.g., 5-hour or weekly windows) per user or agent, allowing for tiered budgets and self-service visibility to prevent overspending.                                                             |
|   7 | :** Restricts specific users or agents to particular models (e.g., limiting interns to cheaper models like GPT-5 Mini or Haiku while reserving frontier models for senior engineers).                                                               |
|   8 | :** Offers semantic routing to direct simple queries to cheaper models, semantic caching to avoid repeated token costs, and context trimming to reduce payload size by filtering irrelevant tools or data.                                          |
|   9 | & Safety:** Integrates with major cloud providers (AWS, Azure, Google, OpenAI) for content moderation, supports custom webhook callouts, and allows regex-based filtering to block sensitive data (e.g., PII) in requests or responses.             |
|  10 | & Community:** Agent Gateway is open-source, part of the Agentic AI Foundation, and can be installed via a simple cURL command; it supports both UI-based configuration and GitOps via configuration files.                                         |
|  11 | :** The presentation demonstrated installing the gateway, configuring Anthropic and OpenAI providers, enforcing budget limits on a "nightly agent," restricting model access for an "intern," and blocking phone numbers via guardrails.            |

# Video

[![Video thumbnail](https://img.youtube.com/vi/jABgf748zHc/hqdefault.jpg)](https://www.youtube.com/watch?v=jABgf748zHc)

[Watch on YouTube](https://www.youtube.com/watch?v=jABgf748zHc)
