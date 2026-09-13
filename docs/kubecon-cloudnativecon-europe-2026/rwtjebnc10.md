---
layout: default
title:
  Is the Agent in the Room with Us Right Now? - Nick Rutigliano & Andrew Halaney,
  Netflix
nav_order: 158
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this talk, Andrew Heleni and Nicotiano, senior engineers at Netflix,
  discuss the architecture and isolation strategies of Titus, Netflix’s internal container
  platform built atop Kubernetes. They explain that Titus workloads are not stand...
resource: https://www.youtube.com/watch?v=-rwTJebNC10
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

In this talk, Andrew Heleni and Nicotiano, senior engineers at Netflix, discuss the architecture and isolation strategies of Titus, Netflix’s internal container platform built atop Kubernetes.
They explain that Titus workloads are not standard Kubernetes workloads and require unique isolation measures at the data plane level, such as user namespaces, custom networking via their ITMAN CNI, and resource controls to prevent issues like noisy neighbors.
The team describes a real-world incident involving INotify resource exhaustion, which led to upstream changes in containerd to ensure proper user namespace isolation.
They also detail their approaches to storage, CPU, and network isolation, including the use of bind-mount ID maps, XFS quotas, and bandwidth enforcement, as well as the injection of custom init processes and dynamic security profiles.
The presentation concludes with recommendations for enabling user namespaces, setting resource limits, and leveraging extensibility points like NRI and OCI hooks for advanced isolation in multi-tenant environments.

# Main Points

|   # | Main point                                                                                                                           |
| --: | ------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Titus is Netflix's internal container platform, built on Kubernetes but with non-standard workloads.                                 |
|   2 | The compute runtime team manages Titus, Kubernetes/Titus data plane, and the base OS.                                                |
|   3 | Titus workloads are not Kubernetes-aware and have unique expectations, resembling VMs to users.                                      |
|   4 | Titus injects processes like SSH and systemd into containers, allows root-like behavior, and supports custom storage.                |
|   5 | Strong resource isolation is implemented to prevent noisy neighbor issues in a multi-tenant environment.                             |
|   6 | Data plane isolation is emphasized, focusing on pod creation stages: run pod sandbox, pull image, create container, start container. |
|   7 | Node Resource Interface (NRI), OCI runtime spec hooks, and an OCI wrapper are used for lifecycle customization and isolation.        |
|   8 | User namespaces are enabled so pods appear to run as root but are mapped to non-root UIDs on the host.                               |
|   9 | An incident revealed that INotify user limits were not properly isolated, allowing a pod to exhaust host resources.                  |
|  10 | Solution involved patching runC and containerd to ensure each pod's user namespace is truly isolated, fixing resource accounting.    |
|  11 | Custom CNI plugin "ITMAN" provides strong network isolation, allowing pods to have unique security groups, subnets, and VPCs.        |
|  12 | Bandwidth is enforced per pod using TC with EDT and eBPF, preventing network resource abuse.                                         |
|  13 | OverlayFS is configured with the "volatile" option for performance; bind mount ID maps are used for efficient UID shifting.          |
|  14 | Systemd and mount namespace performance issues are addressed with new kernel APIs and optimizations.                                 |
|  15 | Container creation involves multiple extension points for process coordination, security profiles, and resource limits.              |
|  16 | "Tiny" (init) is injected into containers for process coordination and sidecar synchronization.                                      |
|  17 | Dynamic seccomp and AppArmor profiles are applied based on declared capabilities.                                                    |
|  18 | CPU and storage isolation are enforced; IO Max and XFS quotas prevent resource contention.                                           |
|  19 | Volumes are bin                                                                                                                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=-rwTJebNC10)
