---
layout: default
title:
  "Project Lightning Talk: k0s: CNCF Sandbox Distro Updates - Jussi Nummelin,
  Technical lead"
nav_order: 245
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  Yusi introduces Kzer, a Kubernetes distribution and CNCF sandbox project
  designed to simplify Kubernetes into a single, statically compiled binary that runs
  on various Linux distributions and now Windows. Kzer includes essential components...
resource: https://www.youtube.com/watch?v=My5ijmfBQGY
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

Yusi introduces Kzer, a Kubernetes distribution and CNCF sandbox project designed to simplify Kubernetes into a single, statically compiled binary that runs on various Linux distributions and now Windows.
Kzer includes essential components like containerd and supports multiple CNI options, allowing flexibility for different environments such as on-premise, cloud, or edge devices.
Architecturally, Kzer separates the control plane from the worker plane, enabling use cases like running the control plane in the cloud and workers at the network edge.
Since its open source launch in 2020 and joining the CNCF sandbox in February, Kzer has seen steady growth in usage and contributors, with the latest release supporting Windows worker nodes and IPv6-only clusters.
Yusi encourages community participation, inviting users and contributors to join, share their experiences, and visit the project's community booth.

# Main Points

|   # | Main point                                                                                                     |
| --: | -------------------------------------------------------------------------------------------------------------- |
|   1 | Kzer is a Kubernetes distribution and CNCF sandbox project.                                                    |
|   2 | Designed as a single, statically compiled binary that runs on any modern Linux distribution.                   |
|   3 | Supports Red Hat, Ubuntu, Alpine, and other Linux systems with a modern kernel.                                |
|   4 | Provides a Kubernetes node with all essential components included (e.g., containerd, CNI options, kube-proxy). |
|   5 | Allows swapping out components like container runtime and CNI (e.g., install Cilium or other CNIs).            |
|   6 | Suitable for on-premise, cloud, and edge device deployments.                                                   |
|   7 | Architectural choice to separate control plane from worker plane by default.                                   |
|   8 | Controller mode runs only the control plane; kubelet and containerd do not run on controller nodes.            |
|   9 | Prevents running workloads on controller nodes, enabling use cases like edge computing.                        |
|  10 | Control plane can run in the public cloud while workers run on remote edge devices.                            |
|  11 | All use cases are supported with the same single binary.                                                       |
|  12 | Project started as open source in 2020.                                                                        |
|  13 | Steady growth in usage and community since launch.                                                             |
|  14 | Joined CNCF sandbox on February 25.                                                                            |
|  15 | Plans to move to CNCF incubation state in the future.                                                          |
|  16 | Increasing number of contributors; last minor release (1.3.4) had 16 contributors.                             |
|  17 | Version 1.3.4 introduced Windows support with a downloadable executable for Windows worker nodes.              |
|  18 | Supports IPv6-only clusters; works with Calico and QRE CNIs, and likely others.                                |
|  19 | Each release includes various fixes and enhancements.                                                          |
|  20 | Encourages community participation and contributions.                                                          |
|  21 | Invites users to visit the community booth at the project pavilion for demos and feedback.                     |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=My5ijmfBQGY)
