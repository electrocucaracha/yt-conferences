---
layout: default
title: Enterprise Multi Cluster GPU Allocation for enabling Gen AI Research
nav_order: 139
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "This presentation explores the integration of GPU workloads with Kubernetes, addressing the challenges of multi-tenancy and resource efficiency in AI infrastructure."
resource: "https://www.youtube.com/watch?v=KLghkASY16M"
tags:
  - openinfra-summit-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T23:38:50+00:00
---

# Summary

This presentation explores the integration of GPU workloads with Kubernetes, addressing the challenges of multi-tenancy and resource efficiency in AI infrastructure.
The speaker explains that unlike CPUs, GPUs operate at the device level without kernel-level preemption, necessitating specific scheduling mechanisms such as the NVIDIA GPU Operator, time slicing, Multi-Process Service (MPS), and Multi-Instance GPU (MIG) to manage allocation and prevent resource contention.
While these methods improve utilization, they often lack strict enforcement of resource limits and data isolation, leading to potential security risks and inefficient sharing among tenants.
To resolve these issues, the talk introduces vCluster, an open-source solution that creates virtual Kubernetes clusters on top of a shared host cluster, providing full API server isolation, custom resource definition autonomy, and enhanced security boundaries for different business units.
By combining vCluster with schedulers like Kai, organizations can achieve better GPU sharing, cost savings through reduced control plane expenses, and secure, isolated environments for diverse AI workloads such as inference, fine-tuning, and distributed processing.

# Main Points

|   # | Main point                                                                                                                                                                                 |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | The talk covers GPU application mechanics and multi-tenancy strategies for Kubernetes clusters.                                                                                            |
|   2 | GPU demand is rising due to increased AI use cases such as agentic AI, real-time agents, and autonomous systems.                                                                           |
|   3 | GPUs are preferred for AI workloads because they contain many arithmetic logic units for high-throughput vector calculations, unlike CPUs which rely on control logic for task preemption. |
|   4 | Kubernetes is widely adopted by major companies to manage the distributed systems required for model development, training, deployment, and monitoring.                                    |
|   5 | GPU scaling in Kubernetes does not occur at the kernel level but through a stack involving the NVIDIA device plugin, container toolkit, and drivers.                                       |
|   6 | A seven-step background process handles GPU allocation, including device mounting, driver library connection, and environment variable injection.                                          |
|   7 | The NVIDIA GPU Operator is essential for managing the lifecycle of GPU components since GPU scheduling happens outside the kernel.                                                         |
|   8 | Large language models are expensive to run, and idle GPUs represent wasted cost, necessitating efficient sharing mechanisms.                                                               |
|   9 | Time slicing allows multiple tasks to share a GPU but does not enable true parallel processing as tasks are scheduled sequentially.                                                        |
|  10 | Multi-Process Service (MPS) enables concurrent GPU sharing but poses data isolation risks for secure datasets.                                                                             |
|  11 | NVIDIA Multi-Instance GPU (MIG) partitions GPUs into isolated instances but is limited to specific hardware and offers fixed segmentation.                                                 |
|  12 | Existing sharing methods often fail to enforce resource limits, allowing one workload to monopolize the GPU and block others.                                                              |
|  13 | Enterprise requirements for GPU clusters include autoscaling, observability, hybrid deployments, custom resource definition isolation, and security auditing.                              |
|  14 | Traditional multi-tenant setups using namespaces lack sufficient isolation for custom resources and can lead to inefficient GPU utilization.                                               |
|  15 | VCluster creates virtual clusters on top of a host cluster, providing isolated API servers for different business units while sharing underlying hardware.                                 |
|  16 | Virtual clusters allow teams to have independent custom resource definitions and access controls without creating separate physical clusters.                                              |
|  17 | GPU labeling enables specific workloads, such as benchmarks or inference, to be assigned to appropriate GPU types like T4 or high-performance cards.                                       |
|  18 | Cost optimization is achieved by using cheaper GPU providers for private nodes and reducing control plane costs by sharing a single host cluster.                                          |
|  19 | VCluster supports multi-use-case inference, GPU-as-a-service, and distributed inference across remote sites.                                                                               |
|  20 | Combining Kai Scheduler for GPU sharing with vCluster for control plane isolation provides both high throughput and secure tenant separation.                                              |
|  21 | Using vCluster reduces infrastructure costs by avoiding the need to pay for multiple control planes in managed Kubernetes services like EKS.                                               |
|  22 | GPU scheduling cannot be enforced via standard Kubernetes resource quotas because it occurs at the device level rather than the kernel level.                                              |
|  23 | NVIDIA GPU features and vCluster are open source and do not require specific NVIDIA licenses for basic usage.                                                                              |
|  24 | The team is currently benchmarking solutions for large-scale architectures like NVIDIA DGX and SuperPOD.                                                                                   |

# Video

[![Video thumbnail](https://img.youtube.com/vi/KLghkASY16M/hqdefault.jpg)](https://www.youtube.com/watch?v=KLghkASY16M)

[Watch on YouTube](https://www.youtube.com/watch?v=KLghkASY16M)
