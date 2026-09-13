---
type: Video Note
title: "Multi-Cluster Wars: The Scheduler Awakens - Dejan Pejchev & Priyanka Ravi, G-Research"
description: "In this talk, Dan Pachev and Priyanka Ravi discuss the importance of batch scheduling and the limitations of single-cluster setups, such as performance bottlenecks, control plane pressure, single points of failure, and data locality challen..."
resource: https://www.youtube.com/watch?v=R0gDne5CuKs
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Dan Pachev and Priyanka Ravi discuss the importance of batch scheduling and the limitations of single-cluster setups, such as performance bottlenecks, control plane pressure, single points of failure, and data locality challenges.
They explain how multicluster scheduling addresses these issues by improving high availability, disaster recovery, data compliance, workload isolation, and scalability.
The presenters then provide a deep dive into three multicluster batch schedulers: Volcano Global, which leverages Carmada for multicluster control and placement; MultiQ, a Kubernetes-native scheduler that uses admission checks and resource mirroring for seamless multicluster operation; and Armada, designed for high-throughput, large-scale scheduling with an event-driven architecture and robust preemption and fairness mechanisms.
The session concludes with a Q&A, clarifying technical details such as resource reservation in MultiQ and confirming that Armada supports running a single workload across multiple clusters.
The presenters emphasize that multicluster scheduling brings balance and efficiency to large-scale compute environments, likening it to opening multiple doors to ease congestion.
# Main Points

|   # | Main point                                                                                                         |
| --: | ------------------------------------------------------------------------------------------------------------------ |
|   1 | Introduction by Dan Pachev and Priyanka Ravi (Pinky) from G Research and Jurarch open source software team         |
|   2 | Focus of talk: multicluster batch schedulers, deep dive into approaches                                            |
|   3 | Batch scheduling coordinates workloads that start, run, and complete (e.g., training jobs, simulations, pipelines) |
|   4 | Core primitives of batch schedulers:                                                                               |
|   5 | Queuing and prioritization: critical jobs prioritized, fair access                                                 |
|   6 | Bin packing: efficient resource utilization (CPUs, GPUs, memory)                                                   |
|   7 | Gang scheduling: atomic start for related workloads                                                                |
|   8 | Fair share: prevents resource hogging, ensures predictable access                                                  |
|   9 | Preemption and backfilling: urgent jobs prioritized, short jobs fill gaps                                          |
|  10 | Placement and locality: move compute to data, optimize for latency and compliance                                  |
|  11 | Single cluster drawbacks:                                                                                          |
|  12 | Performance bottlenecks and overhead at scale                                                                      |
|  13 | Control plane pressure (API server, ETCD)                                                                          |
|  14 | Single point of failure, maintenance risks                                                                         |
|  15 | Data gravity, compliance, and latency issues                                                                       |
|  16 | Multicluster benefits:                                                                                             |
|  17 | High availability and disaster recovery                                                                            |
|  18 | Data locality for compliance and latency                                                                           |
|  19 | Workload isolation and multi-tenancy                                                                               |
|  20 | Scalability beyond single cluster limits                                                                           |
|  21 | Scheduler deep dives:                                                                                              |
|  22 | Volcano Global:                                                                                                    |
|  23 | Uses Carmada for multicluster control plane                                                                        |
|  24 | Volcano handles batch scheduling per cluster                                                                       |
|  25 | Carmada propagates workloads/policies, supports autoscaling, failover, placement controls                          |
|  26 | Volcano Global uses webhook and controller for cross-cluster scheduling decisions                                  |
|  27 | Q / MultiQ:                                                                                                        |
|  28 | Kubernetes-native, no external dependencies                                                                        |
|  29 | Management cluster interacts with multiple worker clusters                                                         |
|  30 | Uses "managed by" field in job spec for multicluster support                                                       |
|  31 | Concepts: local queue, cluster queue, resource flavor, admission checks                                            |
|  32 | MultiQ clones jobs to worker clusters, syncs status                                                                |
|  33 | Admission checks gate workload admission; if not ready, job is suspended                                           |
|  34 | Armada:                                                                                                            |
|  35 | CNCF sandbox project, high throughput/large scale                                                                  |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=R0gDne5CuKs)