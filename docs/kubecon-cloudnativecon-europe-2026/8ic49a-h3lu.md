---
layout: default
title:
  "Project Lightning Talk: k0s - CNCF Sandbox Distro Updates - Jussi Nummelin,
  Maintainer"
nav_order: 299
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Jussi, a core maintainer at Mirantis, introduces K0s, a lightweight Kubernetes
  distribution similar to K3s, notable for packaging all necessary components into
  a single, statically compiled binary that runs across various Linux distribution...
resource: https://www.youtube.com/watch?v=8iC49a-h3LU
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

Jussi, a core maintainer at Mirantis, introduces K0s, a lightweight Kubernetes distribution similar to K3s, notable for packaging all necessary components into a single, statically compiled binary that runs across various Linux distributions.
K0s distinguishes itself architecturally by clearly separating the control plane and worker plane; the controller node runs only essential processes like the API server and scheduler, while worker nodes handle workloads, allowing flexible and distributed cluster deployments.
Jussi also highlights Kosmodrome, a sibling project that enables declarative management of control planes and infrastructure using custom resources, simplifying large-scale cluster management without the need for dedicated VMs.
Recent updates include improved Windows support, enhanced Helm extensions, and better operability for Containerd, with the project seeing growing community contributions and an upcoming incubation application.
Jussi encourages community involvement and invites attendees to visit their booth for demonstrations and discussions.

# Main Points

|   # | Main point                                                                                                                  |
| --: | --------------------------------------------------------------------------------------------------------------------------- |
|   1 | Jussi is a K0s core maintainer at Mirantis.                                                                                 |
|   2 | K0s is similar to K3s: slim, versatile, and packaged as a single statically compiled binary.                                |
|   3 | The binary includes all dependencies and works on various Linux distributions (Alpine, Red Hat, Ubuntu).                    |
|   4 | Users can swap out included components, e.g., use CRI-O instead of Containerd.                                              |
|   5 | K0s architecture separates control plane and worker plane clearly.                                                          |
|   6 | By default, K0s controller nodes do not run kubelet or Containerd, only controller processes (API server, scheduler, etc.). |
|   7 | This separation allows flexible cluster deployments (e.g., control plane in the cloud, workers on Raspberry Pis).           |
|   8 | K0s uses reverse tunneling for connectivity between nodes.                                                                  |
|   9 | Kosmodrome is a sibling project providing declarative management of control planes as custom resources.                     |
|  10 | Kosmodrome acts as a set of Cluster API providers for full-stack, declarative cluster management.                           |
|  11 | Enables managing hundreds or thousands of clusters without spinning up VMs for control planes.                              |
|  12 | Recent release highlights: Windows support is nearly on par with Linux; adding a file enables Windows worker nodes.         |
|  13 | Improvements made to Helm extensions and Containerd operability (e.g., surfacing deprecation warnings).                     |
|  14 | K0s is a CNCF sandbox project for about a year, with an incubation application submitted during KubeCon Atlanta.            |
|  15 | The community is growing; last minor release had 20 contributors.                                                           |
|  16 | Users are encouraged to join the community, share use cases, and fill in the adopters PR.                                   |
|  17 | K0s team will be present at the project pavilion booth during KubeCon.                                                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=8iC49a-h3LU)
