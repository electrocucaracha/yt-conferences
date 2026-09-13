---
type: Video Note
title: "Navigating the Rapid Evolution of Large Mod... Jiaxin Shan, Yuan Tang, Sergey Kanzhelev & Rita Zhang"
description: "The session, led by members from Google, Red Hat, Bance, and Microsoft, introduced the Working Group Serving, which focuses on adapting Kubernetes for evolving inference workloads, particularly in the context of rapid advancements in large..."
resource: https://www.youtube.com/watch?v=bphNDWE8rGE
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The session, led by members from Google, Red Hat, Bance, and Microsoft, introduced the Working Group Serving, which focuses on adapting Kubernetes for evolving inference workloads, particularly in the context of rapid advancements in large model architectures and their orchestration needs.
The group discussed new challenges for 2025, such as the increasing complexity of model roles, the need for network topology-aware scheduling, KV cache management, and improved fault tolerance in GPU clusters.
Updates were provided on several subprojects, including the Gateway API Inference Extension for standardized routing, the Inference Proof benchmarking tool, and the Serving Catalog for deployment examples.
The session also highlighted key Kubernetes initiatives like LWS for multi-node scheduling, Dynamic Resource Allocation (DRA), and unified model weight distribution, as well as open-source solutions such as Airbricks, LMD, KServe, Kaiito, and Dynamo, each addressing different aspects of scalable, efficient, and flexible model serving.
The group emphasized ongoing collaboration, the importance of transitioning to new resource management paradigms, and invited community participation to further shape the future of AI inference on Kubernetes.
# Main Points

|   # | Main point                                                                                                                                                                                        |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Session introduces the Working Group Serving and its members from Google, Red Hat, Bance, and Microsoft.                                                                                          |
|   2 | Working Group Serving was created to address inference and serving workloads on Kubernetes, adapting Kubernetes for these new workload types.                                                     |
|   3 | Multiple working groups exist for specific workloads: serving, batch, integration, device management, networking, and conformance.                                                                |
|   4 | Key 2025 challenges identified:                                                                                                                                                                   |
|   5 | Rapidly evolving model inference architectures, requiring orchestration improvements.                                                                                                             |
|   6 | Model roles as first-class concepts in Kubernetes, needing rollout, autoscaling, and network topology-aware scheduling.                                                                           |
|   7 | KV cache management is now critical; requires state declaration, router awareness, and hot cache migration.                                                                                       |
|   8 | Network resource contention among workflows; careful resource allocation and NUMA binding needed.                                                                                                 |
|   9 | Fault tolerance for GPU failures; proposals for in-process fault tolerance in inference engines.                                                                                                  |
|  10 | Subproject updates:                                                                                                                                                                               |
|  11 | Gateway API Inference Extension: standardizes routing for model inference; supports prefix-aware routing and PDD segregation.                                                                     |
|  12 | Inference Proof Project: benchmarking tool for inference deployments; recent updates include load generators, new metrics, and dataset support.                                                   |
|  13 | Serving Catalog Project: provides working examples for model servers, deployment patterns, and orchestration frameworks; recent additions include KV cache offloading and cloud template support. |
|  14 | Kubernetes enhancements:                                                                                                                                                                          |
|  15 | LWS (Leader Work Set): schedules multiple nodes as a single unit for large models; moving towards native Kubernetes integration.                                                                  |
|  16 | DRA (Dynamic Resource Allocation): enables flexible hardware resource allocation; transition from device plugins is a priority.                                                                   |
|  17 | Unified model weight distribution via image-backed volumes; checkpoint/restore functionality in development.                                                                                      |
|  18 | Solution highlights:                                                                                                                                                                              |
|  19 | Airbricks: cost-efficient, pluggable control plane with enterprise features and KV cache offloading.                                                                                              |
|  20 | LMD: native Kubern                                                                                                                                                                                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=bphNDWE8rGE)