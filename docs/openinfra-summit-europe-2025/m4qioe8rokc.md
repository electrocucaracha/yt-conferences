---
layout: default
title: "Leveling the Enterprise Cloud Playing Field: Making OpenStack Plug-and-Play for Everyone"
nav_order: 128
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Ajit Nar, founder of Pinatasa Computing, presents a solution to bridge the gap between VMware and OpenStack for enterprise adoption."
resource: "https://www.youtube.com/watch?v=m4QIoE8ROkc"
youtube_stats:
  view_count: 38
  like_count: 1
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

Ajit Nar, founder of Pinatasa Computing, presents a solution to bridge the gap between VMware and OpenStack for enterprise adoption.
He highlights that while OpenStack is mature, enterprises hesitate due to talent scarcity, steep learning curves, and complex deployment processes compared to VMware’s established ecosystem.
To address these challenges, his company offers "Paka ZTI," a 10GB ISO-based, zero-touch deployment tool that allows users to install a large-scale, multi-node private cloud via a USB drive without requiring internet connectivity.
This solution simplifies management through a single console, eliminates the need for SSH access, and includes enterprise-grade features such as high availability, network segregation, and validated bugfixes.
Nar demonstrates successful production deployments, including a migration of over 200 VMs for an Indian cloud service provider and an air-gapped installation for a government agency, emphasizing significant cost savings compared to hyperscalers like AWS.
The presentation concludes with a live demo of the deployment wizard and a discussion on upgrade paths, confirming that the platform supports multi-tenancy and is designed to be a stable, enterprise-ready alternative to VMware.

# Main Points

|   # | Main point                                                                                                                                       |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | The speaker, Ajit Nar of Pinatasa Computing, addresses the challenge of migrating enterprises from VMware to OpenStack.                          |
|   2 | Enterprises exhibit reluctance to adopt OpenStack due to a perceived gap in maturity, stability, and ease of use compared to VMware.             |
|   3 | A significant barrier is the scarcity of skilled OpenStack engineers, whereas VMware has a large, established talent pool.                       |
|   4 | OpenStack has a steep learning curve, often requiring three to six months for engineers to become proficient.                                    |
|   5 | The solution, Paka ZTI, is a 10 GB ISO file that allows zero-touch deployment of multi-node clouds via a USB drive.                              |
|   6 | This approach eliminates the need for internet connectivity, making it suitable for air-gapped and government environments.                      |
|   7 | The platform simplifies management by providing a single console for all operations, removing the need for direct SSH access to nodes.           |
|   8 | Paka ZTI uses a socket-based subscription model, offering a cost-effective alternative to VMware's pricing structure.                            |
|   9 | The solution includes validated and secured code with bugs fixed prior to packaging, ensuring enterprise-grade reliability.                      |
|  10 | Production deployments have successfully migrated over 200 large VMs, with plans to scale to 16,000 logical cores.                               |
|  11 | The platform supports high availability features, including host evacuation and instance migration to surviving nodes.                           |
|  12 | Network redundancy is achieved through interface bonds and segregation of management, API, and storage networks.                                 |
|  13 | The deployment wizard automatically discovers nodes, validates hardware requirements, and assigns roles such as controller, compute, or storage. |
|  14 | Upgrades are managed by replacing container images for minor versions, with major upgrades planned for specific release cycles.                  |
|  15 | The system supports multi-tenancy at the domain, project, and user levels, suitable for cloud service providers and large organizations.         |
|  16 | Future releases plan to integrate AI agents for proactive diagnostics and L1/L2 support within the cluster.                                      |

# Video

[![Video thumbnail](https://img.youtube.com/vi/m4QIoE8ROkc/hqdefault.jpg)](https://www.youtube.com/watch?v=m4QIoE8ROkc)

[Watch on YouTube](https://www.youtube.com/watch?v=m4QIoE8ROkc)
