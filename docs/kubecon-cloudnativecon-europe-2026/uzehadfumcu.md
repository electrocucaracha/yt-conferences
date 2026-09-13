---
type: Video Note
title: "Keynote: Rules of the Road for Shared GPUs: AI Inference Scheduling at Wayve - Mukund Muralikrishnan"
description: "The speaker from Wave discusses their work in developing end-to-end AI for autonomous driving, emphasizing the need to process vast amounts of driving data collected daily from their fleet and partners. To handle this, they operate large Ku..."
resource: https://www.youtube.com/watch?v=uZeHADfumCU
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The speaker from Wave discusses their work in developing end-to-end AI for autonomous driving, emphasizing the need to process vast amounts of driving data collected daily from their fleet and partners.
To handle this, they operate large Kubernetes clusters across Azure regions, running over 1,000 GPU nodes and managing up to 100,000 concurrent workloads.
They recently adopted Kueue, a Kubernetes-native job queuing system, which improved GPU cluster utilization from 85% to over 95% and significantly reduced wait times for all teams, especially smaller ones.
Kueue enabled fair resource allocation without requiring code changes and maintained high scheduler performance even during heavy workload bursts.
The speaker encourages attendees to learn more about Kueue at KubeCon and invites those interested in Wave’s work to connect with them at the event.
# Main Points

|   # | Main point                                                                                                        |
| --: | ----------------------------------------------------------------------------------------------------------------- |
|   1 | Wave builds end-to-end AI for autonomous driving using one AI model that generalizes across vehicles and regions. |
|   2 | The fleet collects thousands of hours of driving data daily from partners, dashcam OEMs, and taxis.               |
|   3 | Processing this data requires massive compute resources.                                                          |
|   4 | Wave operates Kubernetes clusters across multiple Azure regions, each with over 1,000 GPU nodes.                  |
|   5 | Clusters process a wide variety of workloads across teams, GPU hardware, priorities, and SLAs.                    |
|   6 | At peak, about 100,000 concurrent workloads are handled.                                                          |
|   7 | Heavy reliance on open source technologies to operate at scale.                                                   |
|   8 | Recently adopted Kueue to schedule AI inferencing workloads.                                                      |
|   9 | Kueue improved GPU cluster utilization from 85% to over 95%.                                                      |
|  10 | Kubernetes lacked granular controls for fairness in multi-tenant environments.                                    |
|  11 | High churn led to tens of thousands of pending pods and degraded scheduler performance.                           |
|  12 | Kueue is a Kubernetes-native job queuing system with advanced resource management controls.                       |
|  13 | Kueue complements the Kubernetes scheduler and is highly scalable (tested up to 100,000 pods).                    |
|  14 | Integration required no code changes.                                                                             |
|  15 | Each team receives a guaranteed allocation; unused capacity can be used by other teams.                           |
|  16 | Kueue ensures fair distribution of resources.                                                                     |
|  17 | Average wait times dropped across all teams, with smaller teams seeing up to 70% reduction.                       |
|  18 | Kubernetes scheduler performance improved during heavy bursts.                                                    |
|  19 | GPU cluster utilization increased from 85% to 97%.                                                                |
|  20 | Full production implementation of Kueue took less than a month, including alerting and monitoring.                |
|  21 | Recommendation to check out Kueue contributor talks at KubeCon.                                                   |
|  22 | Wave is hiring globally; speaker available at the Microsoft booth.                                                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=uZeHADfumCU)