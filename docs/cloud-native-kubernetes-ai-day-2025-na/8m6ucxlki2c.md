---
type: Video Note
title: "You Got a Match! LLM Prefix Aware Routing With Kubernetes - Ricardo Noriega & Cong Liu"
description: "The presentation discusses the Gateway API Inference Extension, a Kubernetes project that enables AI-aware routing for inference workloads by transforming traditional gateways into smart proxies, known as inference gateways. This extension..."
resource: https://www.youtube.com/watch?v=8M6uCXlKI2c
tags: ["cloud-native-kubernetes-ai-day-2025-na", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The presentation discusses the Gateway API Inference Extension, a Kubernetes project that enables AI-aware routing for inference workloads by transforming traditional gateways into smart proxies, known as inference gateways.
This extension allows for intelligent request routing based on model names, latency sensitivity, real-time metrics, and supports features like gradual model updates and traffic splitting.
The LLMD project builds on this by providing a distributed platform for large-scale AI model serving, implementing advanced routing strategies such as prefix-aware routing, which tracks cached prefixes across servers to maximize cache hits and optimize latency and throughput.
The speakers compare various routing strategies, highlighting the benefits of prefix-aware routing and the use of a scoring framework that balances cache affinity and load to prevent server overload.
Benchmarks demonstrate significant improvements in cache hit rates, response times, and throughput, and the solution is production-ready with ongoing enhancements for multi-tier caching and automated cache management.
# Main Points

|   # | Main point                                                                                                                                                                              |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Principal Software Engineer from Red Hat's Office of the CTO presented on the Gateway API Inference Extension for Kubernetes.                                                           |
|   2 | The Gateway API Inference Extension adds AI-awareness to Kubernetes gateways, enabling smart routing of AI workloads.                                                                   |
|   3 | The extension is protocol-based, allowing reuse of traditional gateways (e.g., Envoy) as inference gateways.                                                                            |
|   4 | Inference gateways are extensible; custom policies can be written.                                                                                                                      |
|   5 | LLMD is a Kubernetes-native project implementing the inference extension, providing distributed inference and default configurations for large generative AI models.                    |
|   6 | Key features include directing requests by model name, prioritizing latency-sensitive tasks, gradual model updates, traffic splitting, and intelligent routing using real-time metrics. |
|   7 | The inference flow: client sends request → gateway selects servers from inference pool → picks model server based on criteria → sends request for inference.                            |
|   8 | Moves beyond round-robin to intelligent, real-time routing decisions.                                                                                                                   |
|   9 | Uses Kubernetes CRDs: InferencePool (groups model servers) and InferenceObjective (defines serving objectives, e.g., priority).                                                         |
|  10 | LLMD implements endpoint pickers with scorers and filters (load, KV cache, SLAs).                                                                                                       |
|  11 | Supports PD disaggregated configuration (separating prefill and decode phases for LLM inference).                                                                                       |
|  12 | Prefix-aware caching and variant autoscaler features are included or planned.                                                                                                           |
|  13 | Distributed inference challenges: isolated caches per pod lead to cache misses and recomputation, wasting GPU cycles and increasing latency.                                            |
|  14 | Prefix-aware routing optimizes cache hit rates, reducing cost, increasing throughput, and lowering latency.                                                                             |
|  15 | Evolution of routing: round-robin → load-aware → session affinity → prefix-aware routing.                                                                                               |
|  16 | Prefix-aware routing maintains a global index of cached prefixes per pod for optimal routing.                                                                                           |
|  17 | Three approaches to cache-aware routing: session affinity, estimated cache index, and exact cache index via KV events.                                                                  |
|  18 | Estimated cache index uses req                                                                                                                                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=8M6uCXlKI2c)