---
type: Video Note
title: "Routing Stateful AI Workloads in Kubernetes - Maroon Ayoub, IBM & Michey Mehta, Red Hat"
description: "In this talk, Aruna Yub from IBM Research and Mishi Ma from Red Hat discuss the challenges of routing stateful AI workloads in Kubernetes, focusing on the importance of the KV cache for efficient AI inference. They explain that standard Kub..."
resource: https://www.youtube.com/watch?v=-C76naL3PRc
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Aruna Yub from IBM Research and Mishi Ma from Red Hat discuss the challenges of routing stateful AI workloads in Kubernetes, focusing on the importance of the KV cache for efficient AI inference.
They explain that standard Kubernetes load balancing is unaware of the stateful nature of AI workloads, leading to duplicated computation, increased latency, and underutilized hardware.
The speakers introduce LMD, a Kubernetes-native solution that provides real-time, global visibility into KV cache states across instances, enabling prefix cache-aware scheduling and significantly improving performance metrics such as time to first token and throughput.
Benchmark data demonstrates that precise cache-aware scheduling outperforms random and load-aware strategies by maximizing cache reuse and minimizing queuing.
The session concludes with a discussion of cache management strategies, offloading options, and future work on autoscaling and more granular cache control, emphasizing that making Kubernetes AI-aware is essential for cost-effective and performant AI inference.
# Main Points

|   # | Main point                                                                                                                                                                     |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | The talk focuses on routing stateful AI workloads in Kubernetes, highlighting where Kubernetes fails and presenting data.                                                      |
|   2 | The single most important metric in AI inference production is the KV cache hit rate, directly impacting latency and cost.                                                     |
|   3 | Standard Kubernetes load balancing fails for AI inference because it is unaware of stateful KV cache, leading to duplicated computation and wasted resources.                  |
|   4 | KV cache is used in transformer models to avoid recomputation during inference by reusing previously computed keys and values.                                                 |
|   5 | Without KV cache reuse, inference latency and costs increase significantly, up to 10x.                                                                                         |
|   6 | KV cache reuse is critical in conversational AI and agentic workflows, where context accumulates over multiple turns or steps.                                                 |
|   7 | In multi-instance production environments, naive load balancing destroys KV cache optimizations by routing requests to pods without the relevant cache.                        |
|   8 | LMD provides a Kubernetes-native solution with a global view of KV cache states, enabling prefix cache-aware scheduling.                                                       |
|   9 | LMD’s scheduler uses KV event streams to maintain an efficient index of cache blocks and combines prefix cache affinity with load-aware scoring for balanced scheduling.       |
|  10 | Benchmark data shows that precise prefix cache-aware scheduling achieves the lowest latency and highest throughput compared to approximate, random, and load-aware schedulers. |
|  11 | Precise scheduling maximizes cache hits and minimizes queuing, while random and load-aware methods underperform.                                                               |
|  12 | LMD supports KV cache offloading to CPU and persistent storage, extending memory capacity.                                                                                     |
|  13 | KV cache is managed using LRU (least recently used) policies, with ongoing work on more granular cache management.                                                             |
|  14 | LMD is developing features for autoscaling and improved decode length prediction for better scheduling.                                                                        |
|  15 | Four scheduling methods discussed: random, load-aware, approximate previous caching, and precise prefix cache-aware (the most effective).                                      |
|  16 | AI workloads are inherently stateful; effectiv                                                                                                                                 |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=-C76naL3PRc)