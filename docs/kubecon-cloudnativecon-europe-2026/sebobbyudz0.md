---
type: Video Note
title: "Achieving Resilient Multi-Cluster AI Inference on Kubernetes With Kar... Wei-Cheng Lai & Han-Ju Chen"
description: "Hanuch Chen and Wan Lai present a practical approach for running AI inference serving reliably at scale on Kubernetes, addressing challenges such as bursty traffic, strict latency targets, GPU scarcity, and regional failure risks. They prop..."
resource: https://www.youtube.com/watch?v=SEBoBbyUdz0
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Hanuch Chen and Wan Lai present a practical approach for running AI inference serving reliably at scale on Kubernetes, addressing challenges such as bursty traffic, strict latency targets, GPU scarcity, and regional failure risks.
They propose a two-layer architecture: a fleet orchestration layer across clusters using Carmada for workload placement, replica spreading, cluster-specific overrides, and automated failover, and a serving layer within each cluster using Ray Serve via KubeRay for request-driven autoscaling, safe upgrades, and advanced features.
The solution enables efficient GPU utilization through fractional allocation and model multiplexing, independent scaling of pipeline components, and seamless development-to-production transitions with framework and cloud agnosticism.
Ray provides a unified compute framework for distributed AI workloads, while KubeRay manages Ray applications on Kubernetes, supporting in-place updates, zero-downtime upgrades, high availability, and multi-layer autoscaling.
The ecosystem integrates with existing Kubernetes tools for scheduling and observability, and introduces a history server for post-mortem debugging of ephemeral clusters.
# Main Points

|   # | Main point                                                                                                                                                                                                                                |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation by Hanuch Chen (AnyScale) and Wan Lai (Bloomberg) at KubeCon Europe on running AI serving reliably at scale on Kubernetes under uneven GPU capacity and regional failure risks                                               |
|   2 | Production challenges: bursty traffic, strict P95/P99 latency targets, GPU scarcity, regional failure risks                                                                                                                               |
|   3 | Single-cluster Kubernetes limitations: single blast radius, GPU capacity cliffs, inability to meet global latency and data residency requirements, lack of inference-serving features, risk of interrupting long-lived inference requests |
|   4 | Proposed two-layer architecture:                                                                                                                                                                                                          |
|   5 | Fleet orchestration layer (across clusters) using Karmada for multicluster control, policy-based placement, replica spreading, per-cluster overrides, and automated failover                                                              |
|   6 | Inference serving layer (inside each cluster) using Ray Serve via KubeRay RayService for request-driven autoscaling, safe upgrades, and advanced features                                                                                 |
|   7 | Karmada enables:                                                                                                                                                                                                                          |
|   8 | Placement with cluster affinity for latency/compliance                                                                                                                                                                                    |
|   9 | Spreading services across clusters to reduce failure domain risk                                                                                                                                                                          |
|  10 | Replica scheduling (duplicated or divided)                                                                                                                                                                                                |
|  11 | Per-cluster overrides for heterogeneous environments without duplicating YAMLs                                                                                                                                                            |
|  12 | Dual-level failover: cluster-level and workload-level, using resource interpreter for health signals                                                                                                                                      |
|  13 | Ray Serve features:                                                                                                                                                                                                                       |
|  14 | Model composition: compose entire pipeline as a single Python app with independently scalable components                                                                                                                                  |
|  15 | Fractional GPU allocation: specify exact GPU fraction per model to maximize utilization                                                                                                                                                   |
|  16 | Model multiplexing: host multiple model variants in GPU memory, load/evict on demand, efficient for low-rank adaptation                                                                                                                   |
|  17 | Independent scaling of pipeline stages based on request queue depth, not just CPU/memory                                                                                                                                                  |
|  18 | Seamless development-to-production transition: same Python code, minimal changes                                                                                                                                                          |
|  19 | Framework and cloud agnostic: supports any Python code, runs on any cloud or on-prem                                                                                                                                                      |
|  20 | Ray overview:                                                                                                                                                                                                                             |
|  21 | Unified compute framework for distributed AI workloads                                                                                                                                                                                    |
|  22 | Five native librari                                                                                                                                                                                                                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=SEBoBbyUdz0)