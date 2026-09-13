---
layout: default
title:
  "Lightning Talk: Getting (and Staying) up To Speed on DRA With the DRA Example
  Driver - Jon Huhn"
nav_order: 148
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  John Hune, a software engineer at Microsoft, introduces dynamic resource
  allocation (DRA) in Kubernetes, which enables workloads with specialized hardware
  requirements, such as AI and ML, to better express and fulfill their needs. DRA
  is im...
resource: https://www.youtube.com/watch?v=GVuutzZ5rHY
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

John Hune, a software engineer at Microsoft, introduces dynamic resource allocation (DRA) in Kubernetes, which enables workloads with specialized hardware requirements, such as AI and ML, to better express and fulfill their needs.
DRA is implemented through new Kubernetes APIs that manage resource slices (available resources) and resource claims (workload requirements), allowing the scheduler to match pods with appropriate devices, similar to the persistent volume model.
DRA drivers, typically developed by device vendors, advertise and configure devices for workloads, but for those without access to specialized hardware, the DRA example driver offers a simple way to experiment with DRA on any Kubernetes cluster, including local setups.
The example driver provides mock devices and sample configurations, making it a valuable tool for learning, testing integrations, and supporting projects like SIG scalability and Slinky.
John encourages feedback and contributions to the example driver to help demonstrate new DRA features and invites users to connect via Slack or GitHub for support.

# Main Points

|   # | Main point                                                                                                                                                           |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | John Hune is a software engineer at Microsoft working on upstream Kubernetes projects.                                                                               |
|   2 | The talk focuses on dynamic resource allocation (DRA) and the DRA example driver.                                                                                    |
|   3 | DRA helps maximize hardware usage in Kubernetes clusters, especially for workloads needing specialized hardware and topological constraints (e.g., AI/ML workloads). |
|   4 | Existing mechanisms like node selectors are insufficient for expressing these requirements.                                                                          |
|   5 | DRA has become important in the last 18 months and is required for Kubernetes AI conformance certification.                                                          |
|   6 | DRA introduces new Kubernetes APIs to express generic resource requirements for workloads.                                                                           |
|   7 | Resources can be physical or virtual devices like GPUs, TPUs, or network devices.                                                                                    |
|   8 | Resource slice objects describe available resources in a cluster.                                                                                                    |
|   9 | Resource claim objects describe what resources a pod requires.                                                                                                       |
|  10 | The Kubernetes scheduler matches resource claims to devices in resource slices to assign pods to nodes.                                                              |
|  11 | The pattern is similar to persistent volumes and persistent volume claims.                                                                                           |
|  12 | Once a pod is allocated a device, it must be plugged into the right container.                                                                                       |
|  13 | DRA drivers are third-party components, usually from device vendors, that advertise devices and configure containers to access allocated devices.                    |
|  14 | Existing DRA drivers support various devices from multiple vendors.                                                                                                  |
|  15 | The DRA example driver allows users to experiment with DRA without specialized hardware, even on a Kind cluster.                                                     |
|  16 | The example driver enables requests for mock GPUs and includes examples for sharing devices and defining device configurations.                                      |
|  17 | The tutorial in the official Kubernetes docs by Laura Loren provides more detail on DRA components using the example driver.                                         |
|  18 | The DRA example driver is useful for testing integrations with autoscaling, batch scheduling, and scalability (e.g., SIG scalability tests, Slinky project).         |
|  19 | The example driver is recommended for projects integrating with DRA for tests and experiments.                                                                       |
|  20 | Feedback and feature requests for                                                                                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=GVuutzZ5rHY)
