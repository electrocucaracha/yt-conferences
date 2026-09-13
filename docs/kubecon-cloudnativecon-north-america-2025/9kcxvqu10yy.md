---
layout: default
title:
  "The OS Behind the Curtain: What Happens on Your Nodes When Things Happen in
  Your Clu... Joe Thompson"
nav_order: 315
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  Joe Thompson introduces himself and outlines his background in IT and
  Kubernetes, noting his previous talks and current role as a cloud native architect
  at Clarity Business Solutions. He explains that the session will focus on foundational...
resource: https://www.youtube.com/watch?v=9KCXvQU10yY
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

Joe Thompson introduces himself and outlines his background in IT and Kubernetes, noting his previous talks and current role as a cloud native architect at Clarity Business Solutions.
He explains that the session will focus on foundational Linux features—such as kernel namespaces, control groups (cgroups), IP tables, and overlay filesystems—that underpin Kubernetes but predate it.
Thompson describes how these features provide isolation, resource management, networking, and storage for Kubernetes workloads, using practical examples and audience interaction to illustrate concepts like service networking and file system mounts.
He emphasizes that understanding these Linux underpinnings demystifies Kubernetes operations and aids troubleshooting, highlighting that most of these technologies are longstanding and knowable.
The talk concludes with a brief demo, audience Q&A, and encouragement to explore further, reinforcing that there is no magic—just established Linux mechanisms at work beneath Kubernetes.

# Main Points

|   # | Main point                                                                                                                                                                                      |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Speaker is Joe Thompson, experienced in IT for 30 years, focused on Kubernetes for the last decade, currently Cloud Native Architect at Clarity Business Solutions.                             |
|   2 | Session time is shortened; aims to leave time for questions and a possible demo.                                                                                                                |
|   3 | Audience includes many first-time CubeCon attendees; advice to stay hydrated and use water bottles from CNCF store.                                                                             |
|   4 | Talk covers low-level Linux features that power Kubernetes: kernel namespaces, control groups (cgroups), IP tables, overlay file systems.                                                       |
|   5 | Kernel namespaces discussed: mount, UTS, IPC, PID, network, user, time; allow process isolation and different views of system aspects.                                                          |
|   6 | Example: containers in a pod share network namespace but have separate mount namespaces.                                                                                                        |
|   7 | Control groups (cgroups) originated at Google, merged into Linux in 2007, used for resource constraints and quality of service in Kubernetes.                                                   |
|   8 | cgroups v2 is current; adoption in Kubernetes took time due to slow Linux ecosystem uptake.                                                                                                     |
|   9 | Networking: IP tables, IPVS, and NF tables are used for traffic routing and filtering; Kubernetes supports all, with NF tables likely to become default.                                        |
|  10 | kube-proxy evolved from an actual proxy to just managing IP tables rules; service addresses and ports are virtual, managed by IP tables.                                                        |
|  11 | Networking implementation details depend on CNI; tools like route, ip addr, and ip route are used for inspection.                                                                               |
|  12 | EKS nodes use AWS VPC CNI, assigning pod IPs from the VPC subnet.                                                                                                                               |
|  13 | Data storage: mounts are foundational in Unix/Linux; secrets are mounted as tempfs (not persisted), config maps injected into overlay file system, PVs are block devices mounted in containers. |
|  14 | Overlay file systems (unionfs, aufs, overlayfs) enable layered file systems for containers, supporting image layering and storage efficiency.                                                   |
|  15 | Demo showed how to inspect IP tables rules for a Kubernetes service on the host.                                                                                                                |
|  16 | Emphasis: underlying technologies (IP tables, mounts, cgroups) are old and knowable; understanding them demystifies Kubernetes                                                                  |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=9KCXvQU10yY)
