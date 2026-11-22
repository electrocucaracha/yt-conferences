---
layout: default
title: "Lightning Talk: Benchmarking Your Distributed ML Training on the K8s Platform - Liang Yan, CoreWeave"
nav_order: 14
parent: "Cloud Native & Kubernetes AI Day 2025 - Europe"
type: Video Note
description: "Leang Yan from CoreWeave presents a benchmarking tool for distributed machine learning on Kubernetes, designed to address the unique performance and reliability challenges of pure GPU cloud infrast..."
resource: "https://www.youtube.com/watch?v=6DKpI8pc3m0"
youtube_stats:
  view_count: 168
  like_count: 4
  channel_subscriber_count: 141000
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

Leang Yan from CoreWeave presents a benchmarking tool for distributed machine learning on Kubernetes, designed to address the unique performance and reliability challenges of pure GPU cloud infrastructure.
The presentation highlights the difficulty of detecting subtle performance degradations, such as a 5% drop in a 1,000-GPU cluster caused by a single faulty GPU, which often goes unnoticed by standard monitoring alarms.
After evaluating existing solutions like MLPerf, TorchBench, and NVIDIA DDX, the team found them unsuitable due to excessive test duration, lack of distributed support, or outdated designs, leading them to develop their own open-source tool.
This tool utilizes an Argo Workflow-based operator to control the environment, configure system parameters, and launch MPI jobs, while integrating Prometheus, DCGM, and TensorBoard for comprehensive online monitoring and offline profiling.
Currently focused on validating Megatron-based workloads, the project aims to provide a controlled, automated baseline for cluster validation and debugging, with plans to expand model support and release a unified dashboard.

# Main Points

|   # | Main point                                                                                                                                                                          |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The presentation focuses on benchmarking distributed machine learning training on the Kubernetes platform, specifically for AI infrastructure rather than model performance.        |
|   2 | The speaker is a performance and reliability engineer at Cowhe, a pure GPU cloud provider that builds purpose-built clusters for efficiency and stability.                          |
|   3 | Distributed machine learning training platforms include traditional options like Slurm and newer Kubernetes-based solutions such as Kubeflow, KubeSlurm, and Volcano.               |
|   4 | Existing benchmarks like MLPerf, TorchBench, and NVIDIA DDX Cloud Benchmarking have limitations, including long execution times, complex results, or a lack of distributed support. |
|   5 | KubeBench was considered but rejected because it is archived and difficult to adapt to the latest Kubernetes versions.                                                              |
|   6 | The team developed an internal tool called KerAnalysis to create a controlled environment for cluster validation, regression testing, and debugging.                                |
|   7 | The tool focuses on distributed machine learning, online monitoring, offline profiling, and automation to address subtle performance degradations that do not trigger alarms.       |
|   8 | The design uses an Argo Workflow-based operator to manage configuration, shared storage PVCs, and node environment settings via DaemonSets before launching jobs.                   |
|   9 | The system utilizes the MPI Operator to launch machine learning workloads and integrates Prometheus, Grafana, and DCGM for node-level monitoring.                                   |
|  10 | Detailed analysis is supported through Torch Profiler and TensorBoard to examine model-level performance and correlate it with node metrics.                                        |
|  11 | The project is currently an ongoing effort that uses the Megatron workload for GPT training, with plans to add Llama 70B in the future.                                             |
|  12 | The tool is built on open-source components and is intended to be released as open source once a unified dashboard is completed.                                                    |

# Video

[![Video thumbnail](https://img.youtube.com/vi/6DKpI8pc3m0/hqdefault.jpg)](https://www.youtube.com/watch?v=6DKpI8pc3m0)

[Watch on YouTube](https://www.youtube.com/watch?v=6DKpI8pc3m0)
