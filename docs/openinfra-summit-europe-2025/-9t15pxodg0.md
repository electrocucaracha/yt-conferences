---
layout: default
title: Lessons learned from replacing Magnum with Gardener on OpenStack
nav_order: 10
parent: OpenInfra Summit Europe 2025
type: Video Note
description: Mitri and Maxim from Cloudification present a session on their experience using Gardener as a provider stack for deploying Kubernetes on OpenStack.
resource: "https://www.youtube.com/watch?v=-9T15pXOdg0"
youtube_stats:
  view_count: 520
  like_count: 5
  channel_subscriber_count: 46800
tags:
  - openinfra-summit-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T23:38:50+00:00
---

# Summary

Mitri and Maxim from Cloudification present a session on their experience using Gardener as a provider stack for deploying Kubernetes on OpenStack.
They explain that their environment requires high automation for day-2 operations, leading them to evaluate Magnum, Cluster API, and Gardener.
While Magnum offered native integration, it suffered from complex debugging and cleanup issues, and Cluster API lacked a user-friendly UI and mature observability features.
Consequently, they selected Gardener for its declarative approach, built-in observability, role-based access control, and support for multiple cloud providers, despite its higher setup complexity.
The speakers detail Gardener’s architecture, which utilizes a "Garden cluster" to host controllers and "Seed clusters" to manage the control planes of end user "Shoot clusters," allowing for efficient resource utilization and multi-cloud support.
They highlight key features such as automatic scaling, scheduled maintenance, hibernation, and an extensible plugin system that allows for custom operating systems and integrations.
The presentation also covers deployment strategies, recommending Helm or the newer Operator method over deprecated shell scripts, and advises against hosting Seed clusters in production Kubernetes environments to avoid resource conflicts.
Finally, they address challenges such as the rapid 14-day release cycle, the need for dedicated management clusters, and the specific upgrade procedures required for both Gardener components and the underlying Kubernetes infrastructure.

# Main Points

|   # | Main point                                                                                                                                                       |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speakers from Cloudification presented lessons learned using Gardener as a provider stack for deploying Kubernetes on OpenStack.                             |
|   2 | Their environment involves deploying Kubernetes at the bare metal level, with OpenStack containerized and managed via Argo CD.                                   |
|   3 | Customer requirements for Kubernetes as a Service include simplicity, automatic upgrades, scaling, and ODC integration.                                          |
|   4 | Magnum with the Heat driver was evaluated but rejected due to debugging complexity, leftover resource issues, and lack of support for all customer needs.        |
|   5 | Cluster API was considered a modern declarative approach but lacked a native UI for end users and had limited observability features at the time.                |
|   6 | Gardener was selected for its declarative approach, support for multiple cloud providers, and built-in observability stack.                                      |
|   7 | Gardener architecture consists of a Garden cluster, Seed clusters for management, and Shoot clusters for end user workloads.                                     |
|   8 | The system uses a "Kubernetes on Kubernetes" model where Seed clusters host the control planes of multiple Shoot clusters.                                       |
|   9 | Gardener provides out-of-the-box features including a web dashboard, CLI, role-based access control, and embedded monitoring.                                    |
|  10 | Autoscaling is supported via cluster autoscaler, Horizontal Pod Autoscaler, and Vertical Pod Autoscaler.                                                         |
|  11 | Lifecycle management includes cluster hibernation, scheduled maintenance for OS and Kubernetes updates, and reconciliation for broken states.                    |
|  12 | Extensions allow for customization, such as supporting different operating systems, CNIs, or pre-installing tools like Flux CD.                                  |
|  13 | Enhanced security features include automatic secret rotation and multi-tenancy through projects and role-based access control.                                   |
|  14 | Deployment complexity is managed using Helm charts or the newer Gardener operator, which is recommended over deprecated shell scripts.                           |
|  15 | It is not recommended to host Seed clusters in production Kubernetes clusters due to resource contention and Gardener's extensive control over cluster entities. |
|  16 | Gardener has a rapid 14-day release cycle, requiring careful upgrade planning for both Gardener components and the underlying Kubernetes cluster.                |
|  17 | DNS integration can be customized per cloud provider or via custom extensions to fit internal corporate DNS structures.                                          |
|  18 | Worker node updates are handled through machine deployments, which roll out new machines and migrate workloads during maintenance windows.                       |

# Video

[![Video thumbnail](https://img.youtube.com/vi/-9T15pXOdg0/hqdefault.jpg)](https://www.youtube.com/watch?v=-9T15pXOdg0)

[Watch on YouTube](https://www.youtube.com/watch?v=-9T15pXOdg0)
