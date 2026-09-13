---
type: Video Note
title: "Project Lightning Talk: From Idle to Ideal: Cross‑Cluster GPU Sharing with CoHDI - Takao Indoh"
description: "Taka Indoor from Fujitsu presents a solution for maximizing GPU utilization across multiple Kubernetes clusters using Kodi, addressing the growing demand for AI workloads and the increasing scarcity and cost of GPUs. Traditionally, Kubernet..."
resource: https://www.youtube.com/watch?v=v6TlA7PNOR4
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Taka Indoor from Fujitsu presents a solution for maximizing GPU utilization across multiple Kubernetes clusters using Kodi, addressing the growing demand for AI workloads and the increasing scarcity and cost of GPUs.
Traditionally, Kubernetes manages hardware within individual clusters, making it difficult to share idle GPUs between clusters.
Kodi introduces a shared GPU and memory pool, allowing dynamic attachment and detachment of GPUs to clusters based on workload needs—allocating more GPUs to inference clusters during the day and to training clusters at night.
This composable infrastructure approach enables flexible, on-demand hardware allocation, reducing idle time and infrastructure costs.
Kodi integrates with the Kubernetes scheduler, and the team has released version 0.0.1.1 along with an emulator for users to try, inviting further engagement with the project.
# Main Points

|   # | Main point                                                                                                        |
| --: | ----------------------------------------------------------------------------------------------------------------- |
|   1 | AI workloads are increasing, while GPUs and memory are becoming more expensive and scarce.                        |
|   2 | Organizations can no longer afford dedicated GPUs for every team or cluster.                                      |
|   3 | The goal is to maximize device utilization across multiple Kubernetes clusters.                                   |
|   4 | Some clusters have idle GPUs while others are GPU-starved, leading to imbalance.                                  |
|   5 | Kubernetes traditionally manages hardware only within each cluster boundary.                                      |
|   6 | There is no straightforward or safe way to lend devices across clusters.                                          |
|   7 | Idle capacity in one cluster cannot easily help another cluster.                                                  |
|   8 | The proposed solution is to keep a shared GPU and memory pool.                                                    |
|   9 | During the day, more GPUs are attached to inference clusters due to heavy inference traffic.                      |
|  10 | At night, devices are detached from inference clusters and attached to training clusters for batch jobs.          |
|  11 | Devices are attached when needed and detached when not needed to reduce idle time and lower infrastructure costs. |
|  12 | GPUs are allocated to where they create the most value at the right time.                                         |
|  13 | The approach uses "codi" (composable hardware in disaggregated infrastructure).                                   |
|  14 | Composable infrastructure allows dynamic attachment and detachment of GPUs to Kubernetes nodes.                   |
|  15 | A resource pool of hardware is managed to compose the right bare metal at the right time.                         |
|  16 | Devices are put in a shared pool and nodes are composed as needed, making hardware flexible.                      |
|  17 | Codi works with the Kubernetes scheduler and Device Resource (DR).                                                |
|  18 | The team is tracking Kubernetes scheduler changes in version 1.36 (beta).                                         |
|  19 | Kodi version 0.0.1.1 has been released.                                                                           |
|  20 | A composable infrastructure emulator is provided for users to try.                                                |
|  21 | More information is available at the project pavilion or via the QR code for code, docs, and joining the project. |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=v6TlA7PNOR4)