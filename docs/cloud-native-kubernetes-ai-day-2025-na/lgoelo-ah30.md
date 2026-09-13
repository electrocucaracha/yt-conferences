---
type: Video Note
title: "Sponsored Keynote: Autoscaling GPU Clusters Anywhere — Hyperscalers, Neoclouds & Ba... Lukas Gentele"
description: "The speaker discusses the challenges of providing Kubernetes access on GPUs to engineering teams, highlighting the significantly higher costs compared to CPUs and the need for efficient resource allocation. To address this, the speaker intr..."
resource: https://www.youtube.com/watch?v=LGOELO-ah30
tags: ["cloud-native-kubernetes-ai-day-2025-na", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The speaker discusses the challenges of providing Kubernetes access on GPUs to engineering teams, highlighting the significantly higher costs compared to CPUs and the need for efficient resource allocation.
To address this, the speaker introduces VCluster, a Kubernetes distribution that enables rapid, cost-effective creation of virtual clusters within a single pod or as a standalone binary, making it easier to manage dev and CI environments.
VCluster now integrates with Carpenter, an autoscaling tool from AWS, allowing dynamic scaling and optimization of GPU resources across multiple cloud providers through a central vcluster platform and node providers, with full lifecycle management of nodes.
This setup supports hybrid and multi-cloud environments using Terraform and Open Tofu, and includes direct integrations with Nvidia BCM and Cubeword, enabling deployment on high-performance Nvidia DGX super pods.
The speaker invites attendees to learn more at their booth and participate in related events.
# Main Points

|   # | Main point                                                                                                  |
| --: | ----------------------------------------------------------------------------------------------------------- |
|   1 | Traditional CPU-based Kubernetes access involves complex enterprise processes and static CPU allocation.    |
|   2 | CPU costs are manageable for large engineering teams; example: 4-CPU EC2 VM costs ~$1,600/year.             |
|   3 | GPU costs in AWS are significantly higher, making static allocation less feasible.                          |
|   4 | Autoscaling is essential to provide GPU access to engineers without excessive costs.                        |
|   5 | VCluster is a Kubernetes distribution that allows spinning up entire clusters in a single pod.              |
|   6 | VCluster supports running on EKS, OpenShift, Rancher, VMs, or bare metal.                                   |
|   7 | VCluster enables rapid, cost-effective creation of dev and CI environments.                                 |
|   8 | Static node joining leads to high GPU costs (~$60k per GPU node).                                           |
|   9 | VCluster recently integrated with Carpenter, an open-source autoscaling project from AWS.                   |
|  10 | Carpenter is now baked into VCluster as "VCluster auto nodes," providing autoscaling out of the box.        |
|  11 | VCluster with Carpenter works across multiple environments, not just AWS EC2.                               |
|  12 | VCluster Platform acts as a central fleet management system, communicating with node providers.             |
|  13 | Node providers provision nodes, which are joined into clusters; full node lifecycle management is included. |
|  14 | Carpenter optimizes clusters by suggesting node changes based on cost and requirements.                     |
|  15 | Integration leverages Terraform and Open Tofu, supporting most cloud providers and hybrid clusters.         |
|  16 | Supports hybrid cloud bursting (e.g., OpenStack to AWS EC2 or Nebus).                                       |
|  17 | Direct integration with Nvidia BCM and Cubeword for running on Nvidia DGX super pods.                       |
|  18 | Reference architecture for running VCluster on Nvidia super pods is available.                              |
|  19 | Invitation to visit the booth and join a happy hour event on AI and Kubernetes with Nvidia and JP Morgan.   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=LGOELO-ah30)