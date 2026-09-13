---
layout: default
title:
  "Tutorial: Build, Operate, and Use a Multi-Tenant AI Cluster Base... C. Misale,
  O. Tardieu & D. Grove"
nav_order: 349
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description: Here is a summary of the video transcript in 3-5 sentences.
resource: https://www.youtube.com/watch?v=Ab7mRoJYsMo
tags:
  - kubecon-cloudnativecon-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Here is a summary of the video transcript in 3-5 sentences: IBM Research Principal Research Scientist Olivia Tardu and colleagues Dave Groove and Claudia Misali discuss how to build, operate, and use GPU clusters for AI.
They introduce an open-source platform called MLB Batch that provides a turnkey solution for managing quotas, queuing, and fault detection for AI workloads on Kubernetes clusters with GPUs.
The platform uses Q, a Kubernetes-native system for queuing and quota management, and autopilot, which detects faults in the cluster and triggers recovery actions.
The team demonstrates the platform's capabilities using various examples, including fine-tuning a model, running batch inference, and managing quotas for multiple teams.

# Main Points

|   # | Main point                                                                                                                       |
| --: | -------------------------------------------------------------------------------------------------------------------------------- |
|   1 | IBM Research has developed a point of view on building, operating, and using GPU clusters for AI.                                |
|   2 | The approach is based on open-source tools and leverages Kubernetes and OpenShift AI.                                            |
|   3 | The system includes:                                                                                                             |
|   4 | A queuing system (Q) to manage workloads and quotas                                                                              |
|   5 | An app wrapper to harden workloads and enable fault recovery                                                                     |
|   6 | Autopilot to detect faults and trigger recovery                                                                                  |
|   7 | Prometheus and Grafana for monitoring and visualization                                                                          |
|   8 | Key features include:                                                                                                            |
|   9 | Workload-aware quotas                                                                                                            |
|  10 | Fair sharing and prioritization of jobs                                                                                          |
|  11 | Mechanisms for fair borrowing and trade-offs between teams                                                                       |
|  12 | Fault detection and recovery using autopilot                                                                                     |
|  13 | Monitoring and visualization using Prometheus and Grafana                                                                        |
|  14 | The system is designed to be self-maintaining and self-configure, with minimal human intervention required.                      |
|  15 | It has been tested on a 1200-GPU cluster with 20 teams, achieving high utilization rates while maintaining quotas for each team. |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Ab7mRoJYsMo)
