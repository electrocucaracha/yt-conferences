---
layout: default
title: "Cluster Management for Large Scale AI and GPUs: Challenges and Oppor... Claudia Misale & David Grove"
nav_order: 9
parent: "Cloud Native & Kubernetes AI Day 2025 - Europe"
type: Video Note
description: "This presentation details the challenges and solutions for managing large-scale GPU clusters for AI workloads, focusing on automated fault detection and recovery to maximize utilization."
resource: "https://www.youtube.com/watch?v=prik7_yha9Q"
tags:
  - cloud-native-kubernetes-ai-day-2025-europe
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-15T17:34:27+00:00
---

# Summary

This presentation details the challenges and solutions for managing large-scale GPU clusters for AI workloads, focusing on automated fault detection and recovery to maximize utilization.
The speakers describe their hardware infrastructure, which includes two generations of clusters equipped with NVIDIA A100 and H100 GPUs, and their software stack built on Red Hat OpenShift, MLBatch, and Kubernetes.
To address the high frequency of hardware failures, they developed "Autopilot," a custom tool that performs periodic health checks on GPUs, networks, and storage, exporting metrics to Prometheus and labeling nodes to indicate their health status.
For fault recovery, they utilize "AppWrapper" to group complex resources and enforce retry policies, which automatically triggers workload resets and migrations away from unhealthy nodes when failures are detected.
By integrating these tools with Kubernetes queue management systems, the cluster dynamically adjusts quotas based on available healthy capacity, ensuring that workloads are steered away from faulty hardware and resources are efficiently reallocated without human intervention.

# Main Points

|   # | Main point                                                                                                                                                                                          |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The presentation covers challenges and opportunities in deploying large-scale GPU clusters for AI workloads, focusing on hardware, software, and fault management.                                  |
|   2 | Two generations of clusters are discussed: the first uses 8 A100 GPUs per node with 800 Gbps network, while the second uses 8 H100 GPUs with 3.2 Tbps network and doubled storage.                  |
|   3 | The software stack includes Red Hat OpenShift, Multus CNI for network access, and ML Batch for workload management on Kubernetes.                                                                   |
|   4 | The system supports the entire AI lifecycle, including data preparation, training, fine-tuning, and model serving, with support for multi-tenancy, priorities, and preemption.                      |
|   5 | Advanced fault tolerance is critical because hardware failures, particularly GPU issues, account for a significant majority of workload crashes, as reported by Meta, Nvidia, and academic studies. |
|   6 | Monitoring utilizes Prometheus for Kubernetes metrics, DCGM exporter for GPU-specific data, and Grafana for visualization.                                                                          |
|   7 | A custom tool called Autopilot was developed to run periodic health checks on GPUs, networks, and storage, identifying issues not visible in standard metrics.                                      |
|   8 | Autopilot exports results via Prometheus and labels nodes with health status, allowing schedulers and queuing systems to steer workloads away from faulty hardware.                                 |
|   9 | Q is used for queuing, quotas, and job admission, utilizing cluster queues and cohorts to manage resource borrowing and maintain cluster utilization.                                               |
|  10 | A Slack cluster queue reserves resources to handle node failures, automatically adjusting lending limits based on Autopilot labels to match actual available capacity.                              |
|  11 | App Wrapper groups multiple resources into a single workload unit, ensuring robust cleanup of resources upon failure and providing a uniform retry and failure policy.                              |
|  12 | The App Wrapper controller monitors workload health, triggers resets if underlying controllers fail to recover, and injects affinities to avoid unhealthy nodes.                                    |
|  13 | A live demo demonstrated the system detecting a labeled node failure, resetting the workload, and rescheduling pods to healthy nodes without human intervention.                                    |
|  14 | The goal is to achieve high cluster utilization and productivity through automation, eliminating the need for manual intervention during faults.                                                    |
|  15 | Both Autopilot and App Wrapper are open-source components of the ML Batch software stack used in these clusters.                                                                                    |

# Video

[![Video thumbnail](https://img.youtube.com/vi/prik7_yha9Q/hqdefault.jpg)](https://www.youtube.com/watch?v=prik7_yha9Q)

[Watch on YouTube](https://www.youtube.com/watch?v=prik7_yha9Q)
