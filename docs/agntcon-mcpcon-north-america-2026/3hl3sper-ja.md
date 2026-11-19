---
layout: default
title: "Self-Hosting Agents: What Changes When Models Become Infrastructure - Miriah Peterson, SchoolAI"
nav_order: 4
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Mariah Peterson defines AI agents as models operating in loops to observe, decide, and execute tool calls, categorizing them into one-off, secondary, autonomous, and always-on types."
resource: "https://www.youtube.com/watch?v=3Hl3Sper-jA"
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

Mariah Peterson defines AI agents as models operating in loops to observe, decide, and execute tool calls, categorizing them into one-off, secondary, autonomous, and always-on types.
She highlights that agents are expensive due to token economics, repeated loops, and high compute costs, recommending open-weight models and serverless GPUs like RunPod to reduce expenses.
The presentation details hardware considerations, distinguishing between unified memory systems like Mac Studios and split memory configurations, while explaining how inference engines like vLLM and llama.cpp interact with models to manage reasoning and tool invocation.
Peterson emphasizes the critical role of the "harness" in defining workflows and enforcing guardrails, introducing the open-source Forge project to improve tool call accuracy and error handling for smaller models.
She demonstrates that adding guardrails significantly enhances the performance of small dense models, proving that better enforcement can yield results comparable to larger models, and concludes with practical advice on optimizing context management, KV cache, and self-hosting strategies for cost-effective AI deployment.

# Main Points

|   # | Main point                                                                                                                                                             |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | # Key Points                                                                                                                                                           |
|   2 | • Speaker: Mariah Peterson, founder of a startup with a podcast about AI agents                                                                                        |
|   3 | • Definition: Agents are models executing in loops performing actions of observing, deciding, calling tools, and inspecting results                                    |
|   4 | • Agent types: single tasks, background tasks, autonomous agents on schedules, always-active agents (Grok bots, Discord bots)                                          |
|   5 | • Agents are costly due to: token economics, repetitive loops increasing tokens, provider computational costs, GPU idle capacity, and cloud scheduling issues          |
|   6 | • Cost reduction strategies: use open-weight models, start with serverless GPU (RunPod) - pay-per-compute not per-token, or self-host hardware                         |
|   7 | • Hardware types: unified memory (Nvidia, Mac Studios - GPU and CPU share interface) vs split memory (traditional PCs with separate RAM and VRAM)                      |
|   8 | • Inference engines for production: vLLM and llama.cpp; for hobbyists: Ollama or LM Studio                                                                             |
|   9 | • Use Hugging Face for models - faster updates, all open weights, flexible for hardware constraints                                                                    |
|  10 | • Harness: infrastructure defining what agents do, tool calls, validation, execution, observation, retry/stop logic, and telemetry                                     |
|  11 | • Forge: open-source safety guardrails repository for harnesses including response validation, nudges, error handling, context management                              |
|  12 | • Small dense models (Qwen 27B, Nemotron) perform excellently at tool calling, comparable to or better than large models                                               |
|  13 | • MoE models load only active expert portions to VRAM, enabling smaller VRAM requirements                                                                              |
|  14 | • Reasoning/thinking tags enable models to interpret requests, evaluate results, and improve debugging                                                                 |
|  15 | • API middleware rescue calls between inference engine and tool response prevent wasted turns through error handling                                                   |
|  16 | • vLLM advantages: tensor parallelization, multiple concurrent requests, transformer layer distribution across GPUs                                                    |
|  17 | • llama.cpp advantages: configurability, supports any GGUF file, single-machine preference                                                                             |
|  18 | • Cost factors: conversations with multiple turns/steps, context maintenance per workflow, tool result efficiency, poor compaction, rescue analysis                    |
|  19 | • Self-hosting: fixed cost calculations vs token pricing, GPU utilization optimization, context and KV cache control, but idle GPU still costs more than token pricing |
|  20 | • Cold start: loading large models (2TB+) takes significant time, argument for keeping GPUs always-on                                                                  |
|  21 | • Region rotation strategy: allocate GPU availability across US, Asia, Middle East, Europe time zones to maximize utilization                                          |
|  22 | • Small teams (100 people) can handle BI workflows on two Sparks cost-effectively                                                                                      |
|  23 | • Custom environments often necessary for small models due to different training data (Bash vs other tool calls)                                                       |

# Video

[![Video thumbnail](https://img.youtube.com/vi/3Hl3Sper-jA/hqdefault.jpg)](https://www.youtube.com/watch?v=3Hl3Sper-jA)

[Watch on YouTube](https://www.youtube.com/watch?v=3Hl3Sper-jA)
