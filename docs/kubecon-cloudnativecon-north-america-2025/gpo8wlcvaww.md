---
layout: default
title:
  But What About Reliability? - The Multi-Million Dollar Kubernetes Cost Op...
  Zain Malik & Nibir Bora
nav_order: 35
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  In this talk, Zan Malik and Nibir discuss the challenges organizations
  face in balancing cost savings with reliability in cloud-native platforms, particularly
  Kubernetes. They highlight the common misconception that reliability always requi...
resource: https://www.youtube.com/watch?v=GPo8WLCvaWw
tags:
  - kubecon-cloudnativecon-north-america-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

In this talk, Zan Malik and Nibir discuss the challenges organizations face in balancing cost savings with reliability in cloud-native platforms, particularly Kubernetes.
They highlight the common misconception that reliability always requires high costs and describe how fear of outages often leads to overprovisioning and significant waste, as seen in their own experience with $22 million in unused cloud resources.
Through a combination of technical solutions—such as extending Kubernetes with custom controllers, implementing multi-cluster operators for safe pod evictions, and adopting advanced optimization techniques like automatic resource tuning and custom bin packing—they achieved both improved reliability and substantial cost reductions.
The speakers emphasize the importance of radical visibility, developer control, and cultural change to overcome organizational resistance and fear, ultimately saving $13 million on their cloud bill.
Their key lessons are that there is no silver bullet; success requires deep understanding of application behavior, investment in observability, and a thoughtful balance between automation, control, and human factors.

# Main Points

|   # | Main point                                                                                                                                                                                       |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Balancing cost-saving with reliability is a common organizational challenge.                                                                                                                     |
|   2 | Cost-saving initiatives often risk reliability if not carefully managed.                                                                                                                         |
|   3 | Overprovisioning is used as a safety blanket, leading to significant waste (e.g., $22 million cloud bill waste).                                                                                 |
|   4 | Fear of outages leads to resistance against optimization and automation.                                                                                                                         |
|   5 | Technical solutions included extending Kubernetes with a multicluster operator to coordinate pod evictions, improving reliability and reducing costs.                                            |
|   6 | Basic optimization techniques: multi-tenant clusters, node pool autoscaling, enforcing resource requests/limits, and enabling horizontal pod autoscaling.                                        |
|   7 | Intermediate techniques: cost visibility (FinOps), use of spot nodes, aligning node shape with workload demands, and custom metric-based autoscaling.                                            |
|   8 | Advanced techniques: automatic request tuning, custom bin packing, cluster autoscaler optimization, and enabling controlled evictions.                                                           |
|   9 | Roadblocks include technical blockers (e.g., HPA vs. VPA incompatibility, node sizing issues, Flink on spot nodes) and organizational resistance (fear, sacred workloads, eviction blockers).    |
|  10 | Solutions: radical visibility (dashboards, leaderboards), developer control (opt-in/out for automation), improved telemetry, and disruption probes for safe evictions.                           |
|  11 | Incentive structures shifted optimization from top-down mandates to bottom-up motivation, tying efficiency to team goals and rewards.                                                            |
|  12 | Achieved $13 million in cloud cost savings.                                                                                                                                                      |
|  13 | Key lessons: no silver bullet—understand application needs; progress is non-linear; visibility is essential; balance cost, performance, and reliability.                                         |
|  14 | Kubernetes should be extended and customized for platform needs.                                                                                                                                 |
|  15 | Fear, not compute, is the most expensive infrastructure cost.                                                                                                                                    |
|  16 | Additional Q&A covered VPA recommender data sources, network cost optimization, min replicas defaults, pod sizing, custom eviction tooling, and multicluster resource recommendation management. |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=GPo8WLCvaWw)
