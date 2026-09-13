---
layout: default
title:
  "Tutorial: DRA-matically Simple: On-Demand GPUs for MLOps - Doug Smith & Miguel
  Duarte Barroso"
nav_order: 380
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this workshop, Doug Smith and Miguel introduce and demonstrate Dynamic
  Resource Allocation (DRRA), a new feature in Kubernetes 1.35 designed to improve
  resource management and efficiency. They explain the motivation behind DRRA, highlight.
resource: https://www.youtube.com/watch?v=BTSvZ3E82_w
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

In this workshop, Doug Smith and Miguel introduce and demonstrate Dynamic Resource Allocation (DRRA), a new feature in Kubernetes 1.35 designed to improve resource management and efficiency.
They explain the motivation behind DRRA, highlighting limitations of previous approaches like device plugins, such as manual node labeling and inefficient resource usage, especially with expensive hardware like GPUs.
DRRA enables intent-based resource requests, allowing users to specify requirements (e.g., memory size or driver version) rather than exact devices, and introduces concepts like digital receipts for better observability and lifecycle management.
The presenters outline the roles of driver developers, Kubernetes admins, and application developers in the DRRA workflow, using analogies like a restaurant's inventory, menu, and orders to clarify responsibilities.
The hands-on portion guides participants through reserving and using virtual GPUs, modifying code, and observing resource claims, demonstrating how DRRA streamlines resource allocation, improves cluster efficiency, and simplifies administration compared to previous methods.
The session concludes with practical troubleshooting and a Q&A, emphasizing the benefits of DRRA for both users and administrators.

# Main Points

|   # | Main point                                                                                                                                                                                                       |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Workshop introduces DRRA (Dynamic Resource Allocation) in Kubernetes 1.35, now GA after years of development.                                                                                                    |
|   2 | DRRA addresses lack of proper resource semantics in Kubernetes; allows intent-based resource requests rather than explicit device selection.                                                                     |
|   3 | Enables resource sharing (e.g., multiple workloads using portions of a GPU), improving cluster resource efficiency.                                                                                              |
|   4 | Simplifies admin tasks by providing digital receipts (resource claims) for tracking resource allocation and usage.                                                                                               |
|   5 | DRRA provides a Kubernetes-native interface: cluster declares capabilities, admins define policy, developers express hardware needs via standardized YAML.                                                       |
|   6 | Device plugins (legacy approach) required manual node labeling and worked best in homogeneous environments; DRRA supports heterogeneous, evolving hardware.                                                      |
|   7 | DRRA allows expressing requirements (e.g., memory size, driver version) without specifying exact devices.                                                                                                        |
|   8 | Supports consumable capacity: resources like GPUs can be sliced for multiple workloads; supports request policies and distinct attributes for redundancy.                                                        |
|   9 | DRRA introduces topology awareness, enabling scheduling based on NUMA node locality for performance.                                                                                                             |
|  10 | Three main roles: driver developer (stocks inventory), admin (curates device classes/menu), application developer (requests resources via claims).                                                               |
|  11 | Admins can audit inventory, monitor usage, and troubleshoot stuck pods more easily.                                                                                                                              |
|  12 | Observability improved: resource claims show which pod is using what, with health/status updates.                                                                                                                |
|  13 | Workshop includes hands-on lab: participants SSH into a Kubernetes cluster, use GitHub accounts/SSH keys, and follow tutorial steps from a provided repository.                                                  |
|  14 | Participants experience DRRA from three perspectives: data scientist (uses CLI to reserve/release GPUs), VLM developer (modifies code, runs workloads), Kubernetes admin (monitors and manages resource claims). |
|  15 | Example workflow: reserve GPU with CLI, run workload, release resource; resource claims persist beyond pod lifecycle until e                                                                                     |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=BTSvZ3E82_w)
