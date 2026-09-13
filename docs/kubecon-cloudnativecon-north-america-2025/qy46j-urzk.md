---
layout: default
title:
  "Prepare for Disruptions: How We Upgrade the Whole ML Training Fleet Bi-week...
  Cong Gu & Ankit Goyal"
nav_order: 201
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  In this presentation, Monkit and Frank from LinkedIn’s AI Platforms team
  provide an overview of their on-premises training platform, focusing on how they
  manage disruptions in large-scale machine learning clusters. They describe the archite...
resource: https://www.youtube.com/watch?v=qY46j--UrZk
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

In this presentation, Monkit and Frank from LinkedIn’s AI Platforms team provide an overview of their on-premises training platform, focusing on how they manage disruptions in large-scale machine learning clusters.
They describe the architecture, which includes dynamic job routing, hierarchical quota management, and integrated observability, and explain that disruptions—such as planned maintenance, unplanned hardware failures, and job preemptions—are handled through standardized processes requiring jobs to be “disruption ready” via checkpoint and restore mechanisms.
The team has implemented strategies like maintenance zone-aware scheduling to minimize the number of jobs affected by maintenance, early notification and approval systems to reduce downtime, and a disruption-specific priority queue to ensure disrupted jobs are rescheduled promptly without preempting others.
These optimizations have reduced the percentage of disrupted jobs to less than 1%, and the platform provides libraries and protocols to help users integrate checkpointing easily.
The team is also exploring elastic training to further reduce the need for job restarts, and they address user questions about SLAs, enforcement of checkpointing, and technical details of their maintenance and scheduling systems.

# Main Points

|   # | Main point                                                                                                                                                                                                     |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | LinkedIn's AI platform manages on-prem clusters across multiple regions with heterogeneous GPU/CPU capacity.                                                                                                   |
|   2 | Platform dynamically routes jobs based on data and resource availability.                                                                                                                                      |
|   3 | Over 1 million task executions per month.                                                                                                                                                                      |
|   4 | Training stack includes fleet/cluster management, in-cluster scheduling, hierarchical quota management, multiple operators (open source and in-house), multi-region job routing, and integrated observability. |
|   5 | Disruptions are events where running jobs are forcefully killed, typically due to planned maintenance, unplanned maintenance (e.g., hardware errors), or preemption by higher-priority jobs.                   |
|   6 | Planned maintenance (e.g., OS/kernel upgrades) occurs bi-weekly; unplanned maintenance is triggered by health check failures; preemption occurs for high-priority jobs.                                        |
|   7 | All jobs must be disruption-ready (support checkpoint/restore and seamless restarts).                                                                                                                          |
|   8 | Platform provides a 24-hour uninterrupted runtime SLA for high-priority jobs.                                                                                                                                  |
|   9 | Jobs receive notifications and time to checkpoint before being killed; no more than 10% of the cluster is unhealthy at any time.                                                                               |
|  10 | Platform provides libraries for checkpointing, supporting major frameworks (PyTorch, TensorFlow) and custom trainers.                                                                                          |
|  11 | Hierarchical checkpointing is used for large models; all workers checkpoint in parallel.                                                                                                                       |
|  12 | Maintenance events trigger a process: annotate jobs, create checkpoint signal file, evict pods, checkpoint at step boundary, and system-level restart with automatic retries.                                  |
|  13 | Maintenance zones (20 per cluster) are defined by physical fault domains; each zone is ~5% of cluster capacity.                                                                                                |
|  14 | Maintenance zone aware scheduling packs jobs into the same zone to minimize disruption impact.                                                                                                                 |
|  15 | Early notification (24 hours) and early approval mechanisms reduce repeated disruptions and idle resources.                                                                                                    |
|  16 | Disrupted jobs are pushed to the front of the queue using special disruption-only priority layers, reducing average queue wait time by 38%.                                                                    |
|  17 | Periodic checkpointing is recommended due to hig                                                                                                                                                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=qY46j--UrZk)
