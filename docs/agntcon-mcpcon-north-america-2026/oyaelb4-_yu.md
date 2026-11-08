---
layout: default
title: "Programmable LLM Inference for Open Agent Infrastructure - Lin Zhong, Yale University"
nav_order: 93
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Felix, a machine learning engineer and Yale graduate, presents Pi, a programmable inference engine designed to address the limitations of current systems like vLLM and SGLang, which he argues are o..."
resource: "https://www.youtube.com/watch?v=OYAeLb4-_YU"
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

Felix, a machine learning engineer and Yale graduate, presents Pi, a programmable inference engine designed to address the limitations of current systems like vLLM and SGLang, which he argues are outdated for the agentic world.
By drawing an analogy where the LLM is the CPU, Pi functions as an operating system that allows developers to write custom programs called "infralets," providing full control over the inference loop from embeddings to generation, rather than relying on fixed, black-box configurations.
This architecture enables advanced capabilities such as intelligent KV cache management, on-the-fly context editing, and native multi-agent scheduling, which significantly reduce latency and computational overhead in complex workflows.
Despite this high level of programmability, Pi maintains performance parity with or exceeds existing engines through kernel optimizations and polymorphic batching, achieving up to 14 times faster speeds in multi-agent scenarios.
The presentation concludes by highlighting that Pi supports diverse transformer-based models across various GPUs and offers a drop-in API compatible with OpenAI and Anthropic standards, empowering developers to build highly optimized, custom agentic applications.

# Main Points

|   # | Main point                                                                                                                                                                                                                                             |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | , Felix, introduces Pi (Programmable Inference), a new inference engine designed to address the limitations of current systems like vLLM and SGLang, which are optimized for single-stream text completion but lack flexibility for agentic workflows. |
|   2 | , logits, and attention mechanisms, forcing developers to rely on fixed configurations or fork the codebase to implement custom algorithms like beam search or new decoding strategies.                                                                |
|   3 | , allowing developers to write "Infralets"—programs that control the entire inference loop from embeddings to the generation loop, rather than just serving prompts.                                                                                   |
|   4 | , which prevents the cache from being flushed during tool calls in agentic workflows, significantly reducing recomputation costs and improving latency compared to engines that treat each request as a new session.                                   |
|   5 | "polymorphic batching," which allows diverse workflows (such as prefill and decode) to be batched together without performance loss.                                                                                                                   |
|   6 | , with potential for order-of-magnitude improvements in multi-agent scenarios due to native scheduling and cache offloading.                                                                                                                           |
|   7 | , "prefill while you type" for near-instant time-to-first-token, and on-the-fly editing of agent generation without recomputing the KV cache.                                                                                                          |
|   8 | , including text, image, and video generation, and is compatible with Apple Silicon and common GPUs, with new models requiring only about 100 lines of code to add.                                                                                    |
|   9 | , while offering 10–30% performance gains by default and up to 14x improvements in complex multi-agent setups through custom Infralets.                                                                                                                |
|  10 | , though it supports forking agents and context-aware steering, and the developers encourage the community to build the next generation of agentic applications using this programmable infrastructure.                                                |

# Video

[![Video thumbnail](https://img.youtube.com/vi/OYAeLb4-_YU/hqdefault.jpg)]("https://www.youtube.com/watch?v=OYAeLb4-_YU")

[Watch on YouTube](https://www.youtube.com/watch?v=OYAeLb4-_YU)
