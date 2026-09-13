---
type: Video Note
title: "Rearchitecting Compute at Coinbase: Migrating To Karpenter for Fast, Reliable Scali... Frances Chong"
description: "In this talk, Francis, a staff software engineer at Coinbase, discusses the company's migration from EKS managed node groups and cluster autoscaler to Carpenter for Kubernetes cluster scaling. Coinbase initially faced challenges with slow r..."
resource: https://www.youtube.com/watch?v=06MmxgGbg6U
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Francis, a staff software engineer at Coinbase, discusses the company's migration from EKS managed node groups and cluster autoscaler to Carpenter for Kubernetes cluster scaling.
Coinbase initially faced challenges with slow responsiveness, rigid instance definitions, high operational overhead, and complex cluster upgrades using autoscaler and managed node groups, especially as their infrastructure grew to over 160 clusters and 18,000 nodes.
Carpenter was adopted for its dynamic, fast, and flexible node provisioning, reducing management complexity and enabling better bin packing and cost efficiency.
The migration involved creating a custom controller to dynamically manage EC2 node classes and configurations, addressing issues like subnet tagging and security group management.
Lessons learned include handling increased pod disruptions, managing stateful versus stateless workloads, addressing IP exhaustion, and the importance of observability and clear documentation for engineers.
While most workloads now run on Carpenter, some critical infrastructure remains on managed node groups for stability, and future plans include exploring spot instances, dynamic pricing, and multi-cloud support.
# Main Points

|   # | Main point                                                                                                                                                                            |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Coinbase manages ~160 EKS clusters, previously using EKS managed node groups and cluster autoscaler.                                                                                  |
|   2 | Cluster autoscaler required separate node groups for each instance type, leading to high operational overhead.                                                                        |
|   3 | Node provisioning with autoscaler averaged 4 minutes; pod scheduling averaged 30 seconds with buffer capacity.                                                                        |
|   4 | Pain points included slow scaling, rigid instance definitions, high management overhead, complex upgrades, and ASG auto-AZ rebalancing issues.                                        |
|   5 | Migration to Carpenter motivated by need for dynamic, fast, and simplified scaling.                                                                                                   |
|   6 | Carpenter provisions nodes in seconds, selects optimal instance types at runtime, and eliminates need for predefined node groups.                                                     |
|   7 | Carpenter is open source, actively maintained, and has limited multi-cloud support (AWS, GKE preview).                                                                                |
|   8 | Coinbase built a custom controller to dynamically reconcile node classes and manage subnet/security group configurations.                                                             |
|   9 | Node pool configurations are generic, support multiple instance families, and require careful CPU/memory sizing to avoid IP exhaustion.                                               |
|  10 | Disruption budgets and limits are used to control pod movement and minimize impact on critical workloads.                                                                             |
|  11 | Migration timeline: design in Q3 2024, controller rollout in Q4 2024, cluster migration in Q1 2025.                                                                                   |
|  12 | Lessons learned: increased pod movement requires developer education, stateful/stateless workload tuning, ongoing IP exhaustion management, importance of observability and runbooks. |
|  13 | Future plans: explore spot instances, integrate dynamic pricing, expand multi-cloud support.                                                                                          |
|  14 | Carpenter is deployed on managed node groups for stability; info workloads remain on managed node groups, others on Carpenter.                                                        |
|  15 | Migration involved gradually scaling down node groups and shifting workloads to Carpenter-managed nodes.                                                                              |
|  16 | Disruption frequency managed with low-disruption node pools, disruption budgets, and time-based restrictions.                                                                         |
|  17 | Most clusters run 3-4 node pools; controller manages EC2 node classes, not node pools.                                                                                                |
|  18 | Mixed instanc                                                                                                                                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=06MmxgGbg6U)