---
type: Video Note
title: "Tutorial: KV-Cache Wins You Can Feel: Building AI-Aware... Tyler S, Kay Y, Vita B, Nili G & Maroon A"
description: "The presentation provides a deep dive into LMD, focusing on KV cache management and intelligent inference scheduling for large language model (LLM) deployments. The speakers introduce LMD’s architecture, highlighting how it optimizes hardwa..."
resource: https://www.youtube.com/watch?v=RWOtYFMAnHI
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The presentation provides a deep dive into LMD, focusing on KV cache management and intelligent inference scheduling for large language model (LLM) deployments.
The speakers introduce LMD’s architecture, highlighting how it optimizes hardware utilization by efficiently managing KV caches across distributed VLM instances, using techniques like prefix cache-aware and load-aware routing.
They explain the importance of separating prefill and decode phases in LLM inference, leveraging Kubernetes for scalable deployments, and demonstrate how naive load balancing can lead to cache inefficiencies and reduced throughput.
The hands-on tutorial guides participants through simulating LMD deployments, benchmarking standard Kubernetes routing versus LMD’s intelligent scheduler, and showcases real-world use cases such as token factories.
The session concludes with discussion on future directions, including agentic inference support, and encourages community contributions to further enhance LMD’s capabilities.
# Main Points

|   # | Main point                                                                                                                             |
| --: | -------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation covers LMD, KV cache, and improvements for LLM inference routing.                                                         |
|   2 | Presenters: Maruna Yub (LMD maintainer, IBM), Tyler (VLM core maintainer), K from Dcloud.                                              |
|   3 | Tutorial includes hands-on with Kubernetes naive routing vs. LMD intelligent inference scheduling.                                     |
|   4 | Prerequisites: kind, kubectl, helm, helmfile, yq, jq, docker, lmd deps.                                                                |
|   5 | LMD simulator used for local deployment; no real GPUs required.                                                                        |
|   6 | Transformers process: tokenization, embedding, multiple layers (attention and feed-forward), LM head.                                  |
|   7 | Attention mechanism is stateful; cost grows quadratically with sequence length.                                                        |
|   8 | KV cache encodes previous token states, reducing recomputation.                                                                        |
|   9 | VLM introduces page detention, managing KV cache like virtual memory.                                                                  |
|  10 | Automatic prefix caching enables KV cache reuse across multi-turn conversations.                                                       |
|  11 | Two main inference phases: prefill (prompt processing, compute intensive) and decode (token generation, bandwidth limited).            |
|  12 | LLMD architecture: requests enter inference gateway, routed by endpoint picker based on metrics and KV cache state.                    |
|  13 | Prefill/decode disaggregation allows specialized deployments for different inference phases.                                           |
|  14 | Wide expert parallelism enables scaling across many GPUs, maximizing KV cache space and throughput.                                    |
|  15 | Standard load balancing fails for inference workloads due to distributed KV cache; naive routing causes cache misses and inefficiency. |
|  16 | LMD intelligent inference scheduling balances prefix cache-aware routing and load-aware routing for optimal hardware utilization.      |
|  17 | Gateway API inference extension enables pluggable routing via scorers and filters.                                                     |
|  18 | KV cache management includes offloading to CPU/storage and sharing across pods for sustained throughput.                               |
|  19 | Dcloud uses LMD for on-premise token factories, supporting diverse models and hardware.                                                |
|  20 | LMD roadmap focuses on agentic inference, context-aware KV cache management, and semantic routing.                                     |
|  21 | Guides and benchmarks available for deploying and testing LMD in real clusters.                                                        |
|  22 | Co                                                                                                                                     |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=RWOtYFMAnHI)