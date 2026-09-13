---
type: Video Note
title: "Redefining SLIs for LLM Inference: Managing Hybrid Cloud wit... Christopher Nuland & Hilliary Lipsig"
description: "Christopher Nuland and Hillary Lipig from Red Hat discuss redefining service level indicators (SLIs), objectives (SLOs), and agreements (SLAs) for modern AI stacks, particularly those using large language models (LLMs) and small language mo..."
resource: https://www.youtube.com/watch?v=BM4L74qL8zE
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Christopher Nuland and Hillary Lipig from Red Hat discuss redefining service level indicators (SLIs), objectives (SLOs), and agreements (SLAs) for modern AI stacks, particularly those using large language models (LLMs) and small language models (SLMs).
They explain that traditional reliability and performance metrics must adapt to the non-deterministic and stateful nature of AI workloads, emphasizing the importance of new metrics such as KV cache hit rate, time to first token, and end-to-end latency.
The talk highlights the benefits of breaking LLMs into microservices—separating prefill and decode phases—to improve resource allocation, reduce latency, and enhance observability.
They also discuss the complexities introduced by agentic systems, where telemetry and cross-domain collaboration become even more critical, and share a practical example involving reinforcement learning bots playing video games, illustrating how these metrics are applied in real-world scenarios.
The session concludes with a discussion on the evolving landscape of LLMs versus SLMs, the challenges of catastrophic forgetting, and the potential future directions for AI model architectures and observability.
# Main Points

|   # | Main point                                                                                                                                                 |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Christopher Nuland and Hillary Lipig introduced themselves and their roles at Red Hat.                                                                     |
|   2 | The talk focuses on redefining SLIs (Service Level Indicators) in modern LLM-based AI stacks.                                                              |
|   3 | LLMD is a key project discussed, enabling cache-aware routing for fleets of language models.                                                               |
|   4 | Traditional SRE approaches face challenges with the non-deterministic and stateful nature of LLMs.                                                         |
|   5 | AI workloads highlight the imperfect abstraction from hardware, especially regarding GPU vs CPU.                                                           |
|   6 | LLM requests differ from traditional REST: prompts are queued, then processed in prefill and decode phases.                                                |
|   7 | Prefill: time from prompt submission to first response, involving KV (key-value) cache creation.                                                           |
|   8 | Decode: phase where output tokens are generated and streamed to the user.                                                                                  |
|   9 | New metrics and SLIs/SLOs/SLAs are needed to measure reliability, performance, and user experience for AI systems.                                         |
|  10 | KV cache hit rate is critical for optimizing time to first token, especially with model fleets.                                                            |
|  11 | LLMD enables breaking LLMs into microservices (prefill and decode pods), improving latency and GPU utilization.                                            |
|  12 | Goodput is emphasized as an end-to-end, experience-driven metric, not just point-in-time API success.                                                      |
|  13 | Batching similar requests improves efficiency and cost management for both CPU and GPU workloads.                                                          |
|  14 | End-to-end latency (prompt to decode completion) is a key SLO, especially for customer-facing chatbots.                                                    |
|  15 | Agentic systems (multi-agent LLMs) add complexity, requiring new telemetry and cross-domain SLOs.                                                          |
|  16 | Guardrails execution and natural language process scoring are emerging SLIs for agentic systems.                                                           |
|  17 | Example architecture: using LLMD and reinforcement learning to orchestrate multiple LLMs for playing video games, with real-time metric tracking.          |
|  18 | SLMs (Small Language Models) are discussed as cost-effective, purpose-built alternatives to LLMs, with trade-offs in training and catastrophic forgetting. |
|  19 | Debate on future trends: SLMs vs. larger models with mixture-of-experts; both have roles d                                                                 |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=BM4L74qL8zE)