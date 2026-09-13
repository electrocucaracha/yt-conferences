---
layout: default
title:
  "Cloud Native Theater | Data on Kubernetes Day: From VMs to Ku... Gabriele
  Bartolini & Laurent Parodi"
nav_order: 53
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The video discusses the evolving role of database administrators (DBAs)
  in the cloud-native era, focusing on HSBC's journey transitioning from virtual machines
  to a Kubernetes-based PostgreSQL platform. Contrary to predictions that the DBA...
resource: https://www.youtube.com/watch?v=m0LBKjlxrog
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

The video discusses the evolving role of database administrators (DBAs) in the cloud-native era, focusing on HSBC's journey transitioning from virtual machines to a Kubernetes-based PostgreSQL platform.
Contrary to predictions that the DBA role would become obsolete, HSBC's DBAs led the design and implementation of a sovereign, fully automated, and self-service internal database platform using open-source tools, specifically CloudNativePG.
The speakers detail the technical and organizational challenges faced, such as regulatory constraints, the need for digital sovereignty, and the shift from manual, DBA-dependent operations to automated, scalable, and secure processes.
They emphasize the importance of community-driven development, robust patching and compliance strategies, and advanced observability, while highlighting the ongoing evolution of both the technology and the DBA role.
The session concludes with a Q&A addressing high availability, failover, and performance tuning, reinforcing that DBAs remain essential by adapting their expertise to new cloud-native paradigms and platform engineering.

# Main Points

|   # | Main point                                                                                                                                                                                                                                               |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The DBA role is not dying; at HSBC, DBAs led the move to Kubernetes and co-designed the internal database platform.                                                                                                                                      |
|   2 | HSBC operates in 56 countries, serving 40 million clients with thousands of IT engineers.                                                                                                                                                                |
|   3 | HSBC managed PostgreSQL on VMs with complex tooling, but this created bottlenecks and required DBAs to be constantly involved.                                                                                                                           |
|   4 | Application teams wanted databases as a commodity, focusing on development, not operations.                                                                                                                                                              |
|   5 | Public cloud offered speed and features, but HSBC faced regulatory constraints requiring on-premises solutions and strict controls.                                                                                                                      |
|   6 | HSBC aimed to eliminate technical debt and reduce total cost of ownership with five pillars: sovereign DBaaS (100% open source, no vendor lock-in), agility (provisioning in minutes), self-healing, compliance (auditing, patching), and observability. |
|   7 | Chose CloudNativePG for its native Kubernetes approach, minimal external dependencies, and strong community governance (CNCF project).                                                                                                                   |
|   8 | Adopted multi-tenant Kubernetes clusters, with plans for dedicated clusters; strict namespace isolation and declarative API interactions.                                                                                                                |
|   9 | Integrated HashiCorp Vault for secrets management and automated credential rotation.                                                                                                                                                                     |
|  10 | Disaster recovery managed via replica clusters; patching is automated, phased, and minimizes risk.                                                                                                                                                       |
|  11 | CloudNativePG leverages Kubernetes API directly, removes need for external managers, and uses a lightweight instance manager for health and lifecycle.                                                                                                   |
|  12 | Design reduces attack surface and simplifies security audits.                                                                                                                                                                                            |
|  13 | Uses direct volume management for role-aware lifecycle; supports pluggable backup interfaces and Kubernetes volume snapshots.                                                                                                                            |
|  14 | Logs are streamed in JSON to prevent tampering; Prometheus exporter provides over 50 native metrics.                                                                                                                                                     |
|  15 | Moving toward CNCF incubation, portable PostgreSQL extensions, leaner operator, and full OpenSSF compliance.                                                                                                                                             |
|  16 | DBA role evolved to require deep Kubernetes and GitOps expertise; DBAs now core to platform engineering.                                                                                                                                                 |
|  17 | Day 2 operations governed by strict guardrails, l                                                                                                                                                                                                        |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=m0LBKjlxrog)
