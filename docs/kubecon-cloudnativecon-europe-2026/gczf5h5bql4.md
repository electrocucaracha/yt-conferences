---
layout: default
title: SIG-Windows Updates - Claudiu Belu, Cloudbase Solutions & JR Valdes, Red Hat
nav_order: 322
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this SIG Windows maintainer track session, Claudia and Jar present
  updates on Kubernetes support for Windows, highlighting recent enhancements such
  as improved kube-proxy fixes, expanded platform logic for image selection, and full
  test...
resource: https://www.youtube.com/watch?v=GCzF5h5BQl4
tags:
  - kubecon-cloudnativecon-europe-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

In this SIG Windows maintainer track session, Claudia and Jar present updates on Kubernetes support for Windows, highlighting recent enhancements such as improved kube-proxy fixes, expanded platform logic for image selection, and full test coverage for Windows Server 2025.
They discuss multiple methods for adding Windows nodes to Kubernetes clusters, including cloud provider solutions, tools like OpenShift, Rancher, Tanzu Kubernetes Grid, and manual setup via official documentation.
The session features a demo on deploying Hyper-V isolated containers, which offer enhanced security by running each workload in a microVM, and a demonstration of using K0S and KZCTL to easily set up a mixed Linux and Windows Kubernetes cluster.
The presenters acknowledge community contributions, announce leadership changes within SIG Windows, and encourage participation in meetings and discussions.
The Q&A addresses deployment support across various cloud providers and emphasizes the simplicity of adding Windows nodes with proper SSH access.

# Main Points

|   # | Main point                                                                                                                                                      |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Updates presented for Kubernetes SIG Windows, including demos and Q&A.                                                                                          |
|   2 | Windows GA in Kubernetes since version 1.14 (2019); now supports Windows Server 2025.                                                                           |
|   3 | Multiple ways to add Windows nodes: cloud provider implementations, OpenShift, Rancher, Tanzu Kubernetes Grid, K0S, or manual setup via upstream documentation. |
|   4 | Recent enhancements in kube-proxy, ported to versions 1.36 and 1.35.                                                                                            |
|   5 | Improved platform logic for image selection; added support and full test coverage for Windows Server 2025.                                                      |
|   6 | Hyper-V isolated containers now have end-to-end test coverage; no Kubernetes code changes needed, only Windows host/containerd configuration.                   |
|   7 | Node log query feature (introduced alpha in 1.27) now enabled by default in 1.36; allows log retrieval from any node via kubectl.                               |
|   8 | Upcoming features: Windows graceful shutdown (dependent on Linux counterpart), CPU/memory affinity, cryo-full containers, EMOS pool per runtime class.          |
|   9 | Documentation is regularly updated for latest features and changes.                                                                                             |
|  10 | Hyper-V isolated containers: each workload runs in a microVM, providing kernel isolation; suitable for multi-tenancy and untrusted workloads.                   |
|  11 | To use Hyper-V isolation: Windows Server 2019+, recommended 2022/2025, nested virtualization enabled, containerd 1.7+.                                          |
|  12 | Setup involves configuring containerd, creating a runtime class, and targeting it in pod specs.                                                                 |
|  13 | Demo: Deploying Kubernetes cluster with K0S using SSH access to Linux and Windows nodes; minimal setup required.                                                |
|  14 | K0S automatically detects node OS and installs appropriate components; cluster ready in ~5 minutes.                                                             |
|  15 | Calico required for CNI networking on Windows.                                                                                                                  |
|  16 | Simple deployment of a Windows workload via node port demonstrated.                                                                                             |
|  17 | Community contributions acknowledged: kube-proxy fixes, graceful shutdown, Hyper-V test jobs, cron job for publishing images.                                   |
|  18 | Leadership changes in SIG Windows announced.                                                                                                                    |
|  19 | Weekly SIG Windows meetings on Tuesdays; community encouraged to join and contribute.                                                                           |
|  20 | Support available via Kubernetes S                                                                                                                              |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=GCzF5h5BQl4)
