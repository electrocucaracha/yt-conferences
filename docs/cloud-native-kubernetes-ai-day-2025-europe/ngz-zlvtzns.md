---
layout: default
title: "Serving the Future: KServe’s Next Chapter Hosting LLMs & GenAI Models... Alexa Griffith & Tessa Pham"
nav_order: 5
parent: "Cloud Native & Kubernetes AI Day 2025 - Europe"
type: Video Note
description: Alexa Griffith and Tessa Fam from Bloomberg’s AI inference team presented how KServe is evolving to support the next generation of generative AI workloads.
resource: "https://www.youtube.com/watch?v=ngz-ZlvtZNs"
youtube_stats:
  view_count: 1544
  like_count: 143
  channel_subscriber_count: 141000
tags:
  - cloud-native-kubernetes-ai-day-2025-europe
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-15T17:34:27+00:00
---

# Summary

Alexa Griffith and Tessa Fam from Bloomberg’s AI inference team presented how KServe is evolving to support the next generation of generative AI workloads.
They highlighted that while traditional predictive inference focuses on request-based scaling, generative models require handling massive compute demands, complex latency optimization, and efficient resource management.
To address these challenges, KServe has introduced several key features, including local model caching to reduce startup times, metric-based autoscaling using LLM-specific indicators like token throughput, and multi-node inference capabilities for models exceeding single-node memory limits.
The platform also integrates with vLLM for prompt caching and KV cache management, and supports OpenAI protocol compatibility to streamline API interactions.
Furthermore, the speakers discussed the integration of Envoy AI Gateway and Gateway API extensions to enable hybrid cloud serving, intelligent traffic routing, and enhanced observability, ultimately positioning KServe as a robust, enterprise-grade platform for treating LLMs as a service.

# Main Points

|   # | Main point                                                                                                                                                    |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Kserve simplifies AI deployment on Kubernetes by abstracting infrastructure complexity and supporting multiple generative AI and machine learning frameworks. |
|   2 | The platform addresses Gen AI challenges such as high compute costs, scalability struggles, and the need to balance performance with efficiency.              |
|   3 | New features include LM metric-based autoscaling, model caching, multi-node inference, and OpenAI protocol compatibility for chat completions and embeddings. |
|   4 | Kserve runs on Kubernetes using Knative and Istio to provide serverless capabilities and a service mesh layer for streamlined inference.                      |
|   5 | Generative models require significant compute power, dynamic scaling for traffic spikes, and optimized latency for real-time applications like chatbots.      |
|   6 | Model caching utilizes local persistent volumes to reduce download times, featuring a self-healing mechanism that automatically redownloads missing models.   |
|   7 | Autoscaling is enhanced to trigger based on LM-specific metrics like token throughput, KV cache size, or time to first token rather than just request counts. |
|   8 | Multi-node inference is supported via Ray clusters with vLLM, enabling tensor and pipeline parallelism for models exceeding single-node memory capacity.      |
|   9 | Prompt caching leverages KV cache to reuse computations, while the planned LM cache system shares context across instances to reduce time to first token.     |
|  10 | Integration with Envoy AI Gateway enables hybrid cloud model serving, resilient routing, token-based rate limiting, and standardized observability.           |
|  11 | The Gateway API inference extension provides Kubernetes-native routing based on model name, load, and serving priority for optimized resource use.            |
|  12 | Batch inference and the separation of prefill and decoding stages are being developed to further optimize throughput and hardware utilization.                |
|  13 | Platform teams should provide engineers with tuning knobs for latency versus throughput trade-offs to fit specific model use cases.                           |
|  14 | Observability is critical for GPU capacity planning, benchmarking, and ensuring efficiency through metrics like time to first token.                          |
|  15 | Kserve is moving away from Knative for autoscaling in favor of KEDA to allow scaling based on arbitrary metrics for greater flexibility.                      |
|  16 | Bloomberg integrates with open-source projects like vLLM and aims to support topology-aware scheduling for multi-node inference workloads.                    |

# Video

[![Video thumbnail](https://img.youtube.com/vi/ngz-ZlvtZNs/hqdefault.jpg)](https://www.youtube.com/watch?v=ngz-ZlvtZNs)

[Watch on YouTube](https://www.youtube.com/watch?v=ngz-ZlvtZNs)
