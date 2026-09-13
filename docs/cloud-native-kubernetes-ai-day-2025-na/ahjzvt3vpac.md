---
layout: default
title: "Lightning Talk: My Job Says 'Running' but Nothing's Running: Kubernetes
  Status Reality... Ron Kahn"
nav_order: 8
parent: Cloud Native Kubernetes Ai Day 2025 Na
type: Video Note
description:
  "Ron, a senior software developer at Nvidia, discusses a common issue
  faced by AI researchers when running training jobs on Kubernetes: jobs appear to
  be running smoothly, but underlying network or connectivity errors can cause GPUs
  to sit i..."
resource: https://www.youtube.com/watch?v=AHjZvT3vpAc
tags:
  - cloud-native-kubernetes-ai-day-2025-na
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Ron, a senior software developer at Nvidia, discusses a common issue faced by AI researchers when running training jobs on Kubernetes: jobs appear to be running smoothly, but underlying network or connectivity errors can cause GPUs to sit idle, wasting time and money.
He explains that Kubernetes checks pod readiness individually, which works for microservices but not for complex AI applications where pods must communicate effectively as a group.
Problems like DNS failures or network policy blocks can halt progress without Kubernetes detecting the issue, leading researchers to mistakenly believe their jobs are progressing.
Ron recommends performing thorough pre-flight checks for connectivity and GPU communication before and during training, continuously monitoring real progress indicators such as checkpoint creation and GPU utilization, and validating both infrastructure and application health throughout the job’s lifecycle to bridge the gap between perceived and actual job status.

# Main Points

|   # | Main point                                                                                                                    |
| --: | ----------------------------------------------------------------------------------------------------------------------------- |
|   1 | AI researchers often encounter issues where training jobs appear to be running but are actually stalled.                      |
|   2 | Researchers typically use Kubeflow pipelines and submit jobs with "kubectl apply."                                            |
|   3 | Jobs may show as running and pods appear healthy, but underlying errors (e.g., IP network issues) can occur unnoticed.        |
|   4 | This can result in wasted GPU time and unnecessary cloud costs.                                                               |
|   5 | Kubernetes reports job status based on pod readiness, not actual application progress.                                        |
|   6 | Pod readiness is determined by Kubernetes readiness probes, which are designed for microservices, not AI applications.        |
|   7 | The pod lifecycle includes creation, scheduling, init containers, pending phase, running phase, and readiness probes.         |
|   8 | Readiness probes only check if individual pods are ready, not if the AI application as a whole is functioning.                |
|   9 | AI training jobs involve multiple pods that must communicate, but Kubernetes checks pods individually, not collectively.      |
|  10 | Common pod communication patterns include service discovery via DNS, ring topology, broadcast, and point-to-point.            |
|  11 | Network or DNS failures can halt progress, but Kubernetes may still report the job as running.                                |
|  12 | Researchers expect "running" to mean progress is being made, but Kubernetes only checks pod health, not application progress. |
|  13 | The health of the AI application and its network connectivity are not validated by default.                                   |
|  14 | Recommendations:                                                                                                              |
|  15 | Perform pre-flight checks for connectivity and GPU communication before and during training.                                  |
|  16 | Continuously monitor for real-time errors and actual progress indicators (e.g., checkpoint creation, GPU utilization).        |
|  17 | Implement continuous validation and liveness checks to ensure the AI application is truly progressing.                        |
|  18 | Recognize and address the gap between infrastructure status and actual application reality.                                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=AHjZvT3vpAc)
