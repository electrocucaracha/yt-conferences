---
type: Video Note
title: "AI Workload Preemption in a Multi-Cluster Scheduling System at Bloomberg - Leon Zhou & Wei-Cheng Lai"
description: "Bloomberg's AI workflow management system utilizes a multicluster Kubernetes orchestration tool, Carmada, to efficiently manage thousands of AI training jobs across multiple clusters. The system prioritizes workloads based on business urgen..."
resource: https://www.youtube.com/watch?v=LrL5AcS2d5g
tags: ["kubecon-cloudnativecon-europe-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Bloomberg's AI workflow management system utilizes a multicluster Kubernetes orchestration tool, Carmada, to efficiently manage thousands of AI training jobs across multiple clusters.
The system prioritizes workloads based on business urgency and employs preemptive scheduling to ensure critical tasks are executed promptly, even when resources are limited.
To balance platform efficiency with user experience, the system caches model checkpoints locally, provides clear visibility into expected queuing times, and offers practical recommendations for optimizing job outcomes.
# Main Points

|   # | Main point                                                                                                                                                                                               |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Bloomberg uses AI to parse financial documents and news articles, identify important details, and enhance extracted data.                                                                                |
|   2 | The company relies on its robust data science platform, which includes Kubernetes for managing GPU-intensive workloads.                                                                                  |
|   3 | Carmada is an open-source orchestration tool used to efficiently manage multiple clusters and prioritize workloads based on business urgency.                                                            |
|   4 | Priority-based scheduling ensures critical AI workloads get resources when needed, while preemptive scheduling allows higher-priority jobs to reclaim resources from lower-priority jobs when necessary. |
|   5 | The scheduler uses a priority-based scheduling feature that controls the enablement of preemptive scheduling.                                                                                            |
|   6 | Resource binding and override policies are used to manage workload priorities and resource allocation.                                                                                                   |
|   7 | The system balances platform efficiency with user experience by minimizing disruptions and providing clear visibility into expected queuing times.                                                       |
|   8 | Estimated queuing time is calculated based on historical data, including running averages of previous jobs submitted using the same GPU size.                                                            |
|   9 | Cost model and cost-effectiveness are tied to resource usage and budget management, with a focus on reducing waste and optimizing resource utilization.                                                  |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=LrL5AcS2d5g)