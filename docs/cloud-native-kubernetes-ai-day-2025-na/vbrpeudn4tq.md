---
type: Video Note
title: "KServe Next: Advancing Generative AI Model Serving - Yuan Tang, Red Hat & Dan Sun, Bloomberg"
description: "The video features Yan Tan from Red Hat and Dan from Bloomberg introducing Queserve (Queso), a distributed, scalable, and standardized model inference platform for Kubernetes, supporting both generative and predictive AI workloads. They tra..."
resource: https://www.youtube.com/watch?v=vbRpeUDN4TQ
tags: ["cloud-native-kubernetes-ai-day-2025-na", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The video features Yan Tan from Red Hat and Dan from Bloomberg introducing Queserve (Queso), a distributed, scalable, and standardized model inference platform for Kubernetes, supporting both generative and predictive AI workloads.
They trace Queserve’s evolution from its origins as KFServing under the Kubeflow project in 2019, through its rebranding and independence, joining the LFAI & Data Foundation, and most recently, its acceptance as a CNCF incubating project.
Queserve simplifies AI model deployment on Kubernetes, offering features like autoscaling, authentication, monitoring, and intelligent traffic management, and now supports advanced generative AI workloads with efficient GPU utilization, prompt caching, and multi-tenant resource protection.
The latest 0.16 release introduces integration with RMD for optimized large model inference, intelligent routing, prefix caching, and disaggregated serving for improved performance.
Looking ahead, the team aims to provide a unified inference platform for both predictive and generative AI, standardize APIs, enhance manageability, and foster a growing open-source community, inviting users and contributors to participate via GitHub, Slack, and regular community meetings.
# Main Points

|   # | Main point                                                                                                                          |
| --: | ----------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Queso is a distributed, scalable, and standardized model inference platform on Kubernetes for generative and predictive AI.         |
|   2 | Originated in 2019 as KF Serving under Kubeflow, rebranded as Queso in 2021, and became standalone.                                 |
|   3 | Joined LFAI & Data Foundation in 2022, making it vendor-neutral and increasing contributors.                                        |
|   4 | Recently joined CNCF as an incubating project.                                                                                      |
|   5 | Focuses on unifying generative and predictive inference workloads on Kubernetes.                                                    |
|   6 | Simplifies model deployment and provides features like autoscaling, authentication, monitoring, and traffic management.             |
|   7 | Uses CNCF components: KNative for autoscaling, Istio for service mesh, OpenTelemetry for tracing and metrics.                       |
|   8 | Supports autoscaling based on request volume, batching, request/response logging, authentication, and distributed tracing.          |
|   9 | Handles both structured (predictive) and complex (generative) inputs, including text, code, images, and ideas.                      |
|  10 | Optimizes GPU utilization for large models, supports advanced autoscaling based on GPU and KV cache metrics.                        |
|  11 | Integrates with backbone runtimes (VRM, Tensor, RMD) and supports prompt caching to reduce compute costs.                           |
|  12 | Provides intelligent routing and advanced traffic management, especially for multi-tenant environments.                             |
|  13 | Works closely with Envoy for intelligent routing, rate limiting, and observability.                                                 |
|  14 | Integrates with Gateway APIs for advanced routing and inference extension standards.                                                |
|  15 | Features include metric-based autoscaling, token usage limits, and advanced routing for multi-turn conversations and LoRA adapters. |
|  16 | Added RMD integration in 0.16 release for intelligent inference scheduling, prefix caching, and disaggregated serving.              |
|  17 | Supports single-node, multi-node, and disaggregated workloads with various parallelism options.                                     |
|  18 | Roadmap includes unified inference fabric, maturing ARM inference service, standard APIs, and improved out-of-the-box performance.  |
|  19 | Active community with regular meetings, GitHub repo, and Slack channels for users and c                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=vbRpeUDN4TQ)