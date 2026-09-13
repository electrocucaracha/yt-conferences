---
type: Video Note
title: "Tutorial: A Cross-Industry Benchmarking Tutorial for Distributed LLM Inference... Multiple Speakers"
description: "The video presents a comprehensive tutorial on cross-industry benchmarking for distributed large language model (LLM) inference on Kubernetes, featuring experts from Red Hat, NVIDIA, IBM, Google, and academia. The speakers introduce various..."
resource: https://www.youtube.com/watch?v=RVQwP-apF-A
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The video presents a comprehensive tutorial on cross-industry benchmarking for distributed large language model (LLM) inference on Kubernetes, featuring experts from Red Hat, NVIDIA, IBM, Google, and academia.
The speakers introduce various open-source benchmarking tools and inference stacks, such as LMD and NVIDIA Dynamo, and discuss the complexities of optimizing LLM deployments for throughput, latency, and cost, particularly when hardware is fixed.
They explain key performance metrics like time to first token and inter-token latency, and highlight the importance of benchmarking tools—including LMD benchmark, inference Perf, and AI Perf—for automating configuration sweeps and comparing deployment strategies.
The session delves into advanced topics like distributed inference, prefill/decode disaggregation, and KV cache management, demonstrating how shared caching and intelligent routing can significantly improve performance.
The presenters showcase live demos of benchmarking workflows, configuration explorers, and real-world traffic replay, emphasizing the need for standardized metrics and collaborative open-source development to address the growing complexity of LLM inference optimization.
The discussion concludes with a call for community involvement and convergence toward unified benchmarking methodologies and tools.
# Main Points

|   # | Main point                                                                                                                                   |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Tutorial covers cross-industry benchmarking for distributed LLM inference on Kubernetes.                                                     |
|   2 | Presenters represent Red Hat, NVIDIA, IBM, Google, and University of Chicago.                                                                |
|   3 | Focus is on optimizing deployment strategies for fixed hardware resources.                                                                   |
|   4 | Performance testing aims to balance throughput, latency, and cost (with cost fixed, focus is on throughput and latency).                     |
|   5 | Key metrics: time to first token (TTFT), inter-token latency (ITL), throughput (tokens/sec).                                                 |
|   6 | Load generation methods: synchronous requests, concurrent streams, constant rate, real-world trace replay.                                   |
|   7 | Benchmarking tools discussed: inference Perf (Kubernetes), GDLM (Red Hat), Neural Magic AI Perf (NVIDIA), VLM benchmarking suite.            |
|   8 | Distributed inference addresses scaling, caching, and workload distribution challenges.                                                      |
|   9 | Two main distributed inference stacks: LMD (Red Hat, Google, IBM, etc.) and NVIDIA Dynamo.                                                   |
|  10 | LMD provides Kubernetes-native distributed inference with configurable components and intelligent routing.                                   |
|  11 | LMD Benchmark automates benchmarking, publishes data, and offers a config explorer for optimal configuration discovery.                      |
|  12 | LMD Benchmark workflow: cluster setup, model download, deployment, workload generation, benchmarking, cleanup.                               |
|  13 | Experiments allow sweeping over deployment parameters (e.g., prefill/decoding, tensor parallelism, replicas).                                |
|  14 | NVIDIA Dynamo splits prefill (compute-intensive) and decode (memory-bound) stages across GPUs, improving throughput.                         |
|  15 | Dynamo features: AI configurator for SLO-based deployment, dynamic scaling of prefill/decode workers, KV-aware routing, KV cache offloading. |
|  16 | KV cache enables reuse of context across requests, reducing prefill time and improving performance.                                          |
|  17 | Open-source projects (LM cache, Mooncake) provide KV cache management and integration with inference engines.                                |
|  18 | Benchmarking tools (e.g., AIFF) support real-time metrics, trace replay, and visualization.                                                  |
|  19 | Prefix cache-aware routing in LMD reduces latency spikes and improves cache hit ra                                                           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=RVQwP-apF-A)