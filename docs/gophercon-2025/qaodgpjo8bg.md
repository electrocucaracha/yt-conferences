---
layout: default
title: "GopherCon 2025: Scaling LLMs with Go: Prod Patterns for Handling Millions of AI Requests - John Wang"
nav_order: 11
parent: GopherCon 2025
type: Video Note
description: "John Wang, CTO and co-founder of Assembled, explains how the company leverages Go to build a high-performance support operations platform that balances AI efficiency with human interaction."
resource: "https://www.youtube.com/watch?v=QaODgpJO8bg"
youtube_stats:
  view_count: 1517
  like_count: 33
  channel_subscriber_count: 41100
tags:
  - gophercon-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-21T05:22:37+00:00
---

# Summary

John Wang, CTO and co-founder of Assembled, explains how the company leverages Go to build a high-performance support operations platform that balances AI efficiency with human interaction.
Assembled handles massive scale, processing approximately 450 million LLM requests and two trillion tokens annually, by using Go’s concurrency features to ensure low latency and reliability.
The system employs a categorized fallback strategy for LLM providers to maintain service during outages and utilizes Go routines to run parallel safety checks, such as adversarial detection and escalation logic, which gate the final AI response to prevent hallucinations or unauthorized actions.
Additionally, Wang details the implementation of real-time voice agents that use a planning agent and specialized sub-agents to manage complex conversations, ensuring realistic turn detection and immediate responses.
By choosing Go over Python, Assembled achieves superior concurrency and performance, allowing them to focus on delivering seamless, production-grade AI experiences for major clients like Fortune 500 companies and startups.

# Main Points

|   # | Main point                                                                                                                                                                                           |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | John Wang, CTO and co-founder of Assembled, presented how the company uses Go to build a support operations platform that balances AI efficiency with human interaction.                             |
|   2 | Assembled serves Fortune 500 companies, government agencies, and startups by providing tools for scheduling, forecasting, and AI chat or voice bots.                                                 |
|   3 | The platform handles approximately 450 million LLM requests per year, two trillion tokens, and peaks at 150 LLM requests per second.                                                                 |
|   4 | Reliability is achieved by categorizing requests and falling back to specific models based on task requirements, such as using fast models for summarization and reasoning models for complex tasks. |
|   5 | Go’s built-in error handling and timeouts are used to manage provider outages and ensure seamless fallbacks between different LLM providers.                                                         |
|   6 | Real-time safety and guardrails are implemented using Go routines to run escalation detection, adversarial detection, and RAG retrieval concurrently.                                                |
|   7 | A gating mechanism ensures that AI-generated answers are not sent until security checks for adversarial inputs and escalation needs are completed.                                                   |
|   8 | This approach prevents issues like unauthorized system prompt retrieval or inappropriate actions, such as refunding high-value items like private jets, by routing such cases to humans.             |
|   9 | Latency and unified interfaces across chat, voice, and email channels are critical challenges addressed by the platform’s architecture.                                                              |
|  10 | Voice AI systems use a speech-to-text pipeline where audio packets are converted to text, processed by agents, and converted back to speech.                                                         |
|  11 | A planning agent coordinates with specialized sub-agents to handle different conversation states, ensuring low latency and appropriate responses.                                                    |
|  12 | Go routines allow the planning agent and current sub-agent to run in concert, with gates controlling when responses are sent to the user.                                                            |
|  13 | Dynamic filler messages are used to maintain conversational flow and perceived realism when processing times exceed acceptable thresholds.                                                           |
|  14 | The team chose Go over Python for its superior concurrency capabilities, which simplify the implementation of complex, low-latency AI systems.                                                       |
|  15 | This technical foundation allows Assembled to focus on providing high-quality customer experiences rather than managing basic concurrency issues.                                                    |

# Video

[![Video thumbnail](https://img.youtube.com/vi/QaODgpJO8bg/hqdefault.jpg)](https://www.youtube.com/watch?v=QaODgpJO8bg)

[Watch on YouTube](https://www.youtube.com/watch?v=QaODgpJO8bg)
