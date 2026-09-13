---
layout: default
title:
  "The Future of Kubernetes Scalability: Challenges of the GigaWatt... Maciek
  Różacki & Artur Rodrigues"
nav_order: 358
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this talk, Arthur Rodriguez from Anthropic and Mati Kjatski from Google
  discuss the evolving challenges and future directions of Kubernetes scalability,
  particularly in the context of large-scale AI workloads. They emphasize that traditi...
resource: https://www.youtube.com/watch?v=Y7FDWmLbLa4
tags:
  - kubecon-cloudnativecon-europe-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

In this talk, Arthur Rodriguez from Anthropic and Mati Kjatski from Google discuss the evolving challenges and future directions of Kubernetes scalability, particularly in the context of large-scale AI workloads.
They emphasize that traditional metrics like node count are less relevant than the mutation rate—the rate at which pods are created, updated, or deleted—which is often limited by the underlying storage system.
The speakers highlight the increasing heterogeneity of workloads, hardware, and cloud environments, noting that AI training workloads introduce unique scheduling and scaling challenges compared to microservices.
They share experiences developing custom solutions, such as topology-aware schedulers and CRDs, to address these needs, and stress the importance of making Kubernetes more modular and customizable while ensuring that innovations are upstreamed for community benefit.
Looking ahead, they predict continued growth in cluster sizes, greater adoption of multicluster and self-hosted architectures, and a lowering barrier to building bespoke Kubernetes components, urging the community to invest in controller sharding, improved API server resilience, and standardized workload-aware scheduling to keep Kubernetes relevant in the rapidly advancing AI era.

# Main Points

|   # | Main point                                                                                                                                           |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Kubernetes scalability must evolve to remain relevant in the gigawatt AI computing era.                                                              |
|   2 | Node count is no longer the main scalability metric; mutation rate (pod mutations per second) is now a key constraint.                               |
|   3 | Mutation rate ceilings are often dictated by the storage backend (e.g., etcd), not node count.                                                       |
|   4 | Scalability should be viewed as a combination of node count, workload churn, and workload heterogeneity.                                             |
|   5 | Real-world incidents show that high write loads from controllers can bottleneck clusters.                                                            |
|   6 | Microservices have historically driven Kubernetes scalability, but AI training workloads now present new challenges.                                 |
|   7 | AI training workloads require gang scheduling, long runtimes, and can scale to tens of thousands of nodes.                                           |
|   8 | Power and hardware availability are major constraints for scaling clusters.                                                                          |
|   9 | Heterogeneity exists across clouds (GKE, EKS), chip architectures (TPUs, Nvidia, Amazon Trainium), and workload types (training, inference, RL, CI). |
|  10 | Custom solutions are often needed for topology-aware scheduling and workload management.                                                             |
|  11 | Anthropic and others have built custom controllers, CRDs, and DNS plugins to address scaling needs.                                                  |
|  12 | Largest clusters are managed by hyperscalers, often requiring backend storage changes (e.g., Spanner instead of etcd).                               |
|  13 | The barrier to customizing Kubernetes is dropping due to better tools and AI assistance.                                                             |
|  14 | Bespoke solutions are proliferating; there is a need for better upstreaming of innovations.                                                          |
|  15 | AI hardware is rapidly improving, but demand for compute continues to outpace hardware gains.                                                        |
|  16 | Workload patterns (e.g., RL, mixture of experts) are changing infrastructure requirements.                                                           |
|  17 | Large clusters (potentially 250,000+ nodes) will persist, but bring risks like blast radius and reliability.                                         |
|  18 | Multicluster architectures mitigate risk but add management complexity.                                                                              |
|  19 | Kubernetes must remain modular and easy to customize, while improving the process for standardizing innovations.                                     |
|  20 | Controller sharding and work queue partitioning                                                                                                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Y7FDWmLbLa4)
