---
layout: default
title:
  "Project Lightning Talk: Multi-Cluster Orchestration System: Karmada Updates
  A... Joe Nathan Abellard"
nav_order: 278
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Joe, a senior software engineer at Bloomberg and core owner of the Kamada
  project, provides an overview of Kamada, a CNCF project designed for Kubernetes-native
  multicluster management. Kamada enables organizations to orchestrate workloads...
resource: https://www.youtube.com/watch?v=IlXsx4lMrQU
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

Joe, a senior software engineer at Bloomberg and core owner of the Kamada project, provides an overview of Kamada, a CNCF project designed for Kubernetes-native multicluster management.
Kamada enables organizations to orchestrate workloads across clusters, regions, and clouds, offering features such as advanced scheduling policies, cross-cluster application failover, unified authentication and auditing, global resource views, and multi-cluster service discovery.
Architecturally, Kamada resembles a Kubernetes cluster setup, with a control plane and member clusters, and is cloud agnostic, supporting both private and public cloud environments.
Since its open-source release in 2021, Kamada has progressed through CNCF’s project stages and has seen wide adoption by companies like Bloomberg and Trip.com.
Joe invites attendees to learn more at upcoming Kamada talks and the project booth, emphasizing Kamada’s value for distributed AI infrastructure, public cloud platforms, and evolving Kubernetes environments.

# Main Points

|   # | Main point                                                                                                       |
| --: | ---------------------------------------------------------------------------------------------------------------- |
|   1 | Joe is a senior software engineer at Bloomberg and a core owner of the Kamada project.                           |
|   2 | Kamada is a CNCF project for Kubernetes-native multicluster management.                                          |
|   3 | Enables running workloads across multiple clusters, regions, and clouds.                                         |
|   4 | Kamada setup is similar to Kubernetes cluster setup, with a control plane joined to member clusters.             |
|   5 | Kamada is cloud agnostic; clusters can be on-premises or across multiple cloud providers.                        |
|   6 | The control plane uses the standard kube API server for integration with Kubernetes toolchain.                   |
|   7 | Kamada scheduler replaces kube-scheduler for intelligent workload placement across clusters.                     |
|   8 | Key features:                                                                                                    |
|   9 | Powerful multicluster management                                                                                 |
|  10 | Advanced policies for various scheduling requirements                                                            |
|  11 | Cross-cluster application failover for disaster scenarios                                                        |
|  12 | Unified authentication, authorization, and auditing                                                              |
|  13 | Global resource view for querying resources across all clusters                                                  |
|  14 | Multicluster service discovery                                                                                   |
|  15 | Kamada was open-sourced in 2021, became a CNCF sandbox project the same year, and an incubating project in 2023. |
|  16 | Currently on track to become a CNCF graduate project.                                                            |
|  17 | Fast-growing community with contributors from many companies; widely adopted in production.                      |
|  18 | Notable adopters include Hallway, Bloomberg, and Trip.com.                                                       |
|  19 | Upcoming Kamada-related talks at KubeCon:                                                                        |
|  20 | Decomposing and governing giant LLM jobs across clusters managed by Kamada                                       |
|  21 | Kamada maintainer track talk with more project details                                                           |
|  22 | Zero downtime migration from engineext to multicluster Kubernetes at Bloomberg                                   |
|  23 | Running disaster-resilient Chino on multicluster Kubernetes powered by Kamada                                    |
|  24 | Kamada project booth available for more information and discussions on multicluster orchestration.               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=IlXsx4lMrQU)
