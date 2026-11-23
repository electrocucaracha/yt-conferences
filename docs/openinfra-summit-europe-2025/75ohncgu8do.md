---
layout: default
title: "Managed Kubernetes Services at OVHcloud, from stability needs to transformation"
nav_order: 86
parent: OpenInfra Summit Europe 2025
type: Video Note
description: 'OVHcloud presented the significant transformation of its Managed Kubernetes Service (MKS) platform, driven by the need to replace the legacy "Shipyard" component, which had become difficult to main...'
resource: "https://www.youtube.com/watch?v=75ohnCGu8do"
youtube_stats:
  view_count: 80
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

OVHcloud presented the significant transformation of its Managed Kubernetes Service (MKS) platform, driven by the need to replace the legacy "Shipyard" component, which had become difficult to maintain and upgrade.
To address these challenges, the team adopted a new architecture based on open-source projects, specifically utilizing Cluster API, the KAMIC provider for control planes, and Argo CD for deployment, while introducing a custom "MKS Operator" to bridge their public API with these underlying resources.
The project began in June 2024, involving a temporary freeze on the public roadmap to allow for a complete rebuild, followed by a beta phase in April 2025 where customer feedback helped prioritize features and identify bugs.
The new stack, branded as the "Standard" offer, was officially released in September 2025, initially deployed in the new Paris data center, offering improved features such as dedicated TCD storage and better service level agreements.
Looking ahead, OVHcloud plans to expand this new infrastructure to new regions like Milan and Rome, migrate legacy clusters to the new stack, and accelerate its roadmap with enhancements including multi-CNI support, improved upgrade strategies, and integrated autoscaling capabilities.

# Main Points

|   # | Main point                                                                                                                                                                                     |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | OVH Cloud has operated public cloud infrastructure using OpenStack for over ten years, offering flexible compute, storage, and multi-region deployments across Europe and internationally.     |
|   2 | The managed Kubernetes service (MKS) has been available since 2019 and is compatible with block storage, object storage, managed databases, and Rancher for multi-cloud management.            |
|   3 | The platform currently supports over 6,500 customer clusters, with a significant footprint in France and growing international presence.                                                       |
|   4 | The legacy infrastructure relied on a monolithic component named Shipyard, written in Python with a workflow engine, which became difficult to maintain, upgrade, and operate over five years. |
|   5 | Shipyard handled control plane deployment, worker node provisioning, and add-on management, but caused outages and operational pain during major changes.                                      |
|   6 | The decision to revamp the platform was driven by the need to support new regions, add CNI options like Cilium, improve upgrade strategies, and keep the platform up to date.                  |
|   7 | The new architecture replaces Shipyard with open-source tools, specifically Cluster API, Karmada, and Argo CD, to leverage reconciliation loops and improve maintainability.                   |
|   8 | Karmada is used for hosted multi-tenancy control planes, while the Cluster API provider for OpenStack (CAPO) manages worker node provisioning.                                                 |
|   9 | Argo CD is utilized to deploy CNI, CSI, and custom components, ensuring a fully functional cluster with minimal custom code.                                                                   |
|  10 | A custom MKS Operator acts as an interface between the public API and the open-source stack, managing custom resources like MKS Cluster and Node Pool.                                         |
|  11 | The transformation project began in June 2024, with a roadmap freeze to focus on the revamp, and a beta phase launched in April 2025.                                                          |
|  12 | Customer feedback during the beta phase helped prioritize features and fix issues, leading to the release of the new stack in September 2025.                                                  |
|  13 | The first region delivered on the new stack was Paris, introducing a new "Standard" offer with dedicated TCD storage and improved service level agreements.                                    |
|  14 | The project took longer than expected due to building new components from scratch, but open-source contributions and community support accelerated development.                                |
|  15 | Future plans include deploying the new stack to new regions like Milan and Rome, migrating legacy clusters, and resuming a faster roadmap.                                                     |
|  16 | Upcoming features include integrating OpenStack floating IPs, supporting multiple CNIs like Calico, improving upgrade strategies, and enhancing the autoscaler.                                |
|  17 | The public roadmap is available on GitHub, and customers are encouraged to create issues to request new features or improvements.                                                              |

# Video

[![Video thumbnail](https://img.youtube.com/vi/75ohnCGu8do/hqdefault.jpg)](https://www.youtube.com/watch?v=75ohnCGu8do)

[Watch on YouTube](https://www.youtube.com/watch?v=75ohnCGu8do)
