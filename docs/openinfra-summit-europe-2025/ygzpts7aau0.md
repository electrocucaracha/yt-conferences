---
layout: default
title: "Cloud-native computing – When the infra becomes an app"
nav_order: 101
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "This presentation introduces Sunbeam, a project by Canonical that leverages cloud-native principles to simplify the deployment and management of OpenStack infrastructure."
resource: "https://www.youtube.com/watch?v=yGzptS7Aau0"
youtube_stats:
  view_count: 63
  like_count: 3
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

This presentation introduces Sunbeam, a project by Canonical that leverages cloud-native principles to simplify the deployment and management of OpenStack infrastructure.
The speakers explain that while Kubernetes is a successful implementation of cloud-native technology, it does not address all infrastructure challenges, necessitating a unified ecosystem where OpenStack and Kubernetes coexist.
Sunbeam achieves this by using Snap for secure, sandboxed packaging of data plane components like compute, network, and storage, while running the OpenStack control plane on Kubernetes to utilize its native microservice orchestration capabilities.
The system is orchestrated by Juju for lifecycle management and supports reproducible deployments via Terraform-driven manifests, allowing users to enable services like load balancing and observability with simple commands.
This architecture aims to reduce the complexity of traditional OpenStack deployments, providing a scalable, secure, and automated platform that can run both traditional and cloud-native workloads on a single open infrastructure stack.

# Main Points

|   # | Main point                                                                                                                                                              |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The future of software is cloud native, but Kubernetes alone does not address all application challenges, requiring a broader ecosystem.                                |
|   2 | The merger of the Open Infra Foundation and the Linux Foundation unites the OpenStack and Kubernetes communities to create a joint value proposition.                   |
|   3 | OpenStack is fundamentally a software application that can be made cloud native by adhering to CNCF principles such as containers, microservices, and declarative APIs. |
|   4 | Kubernetes is one successful implementation of cloud native technology, not the definition itself, allowing other implementations to exist.                             |
|   5 | A cloud native infrastructure stack requires layers for hardware automation, operating systems, and a cloud native computing foundation.                                |
|   6 | The cloud native computing foundation layer includes software defined storage, networking, virtualization, containerization, packaging, and lifecycle management.       |
|   7 | Canonical’s reference architecture uses Ceph for storage, OVN for networking, QEMU/KVM for virtualization, and Kubernetes for container coordination.                   |
|   8 | Snaps serve as the cloud native packaging mechanism to run these components on the operating system in a fully cloud native way.                                        |
|   9 | Juju is used for lifecycle management to orchestrate and operate the complex stack of technologies post-deployment.                                                     |
|  10 | The Sunbeam project serves as the foundation for building cloud native infrastructure as a service platforms with OpenStack running on top.                             |
|  11 | In the Sunbeam architecture, the OpenStack control plane runs on Kubernetes to leverage native features for high availability and service discovery.                    |
|  12 | The data plane services for compute, network, and storage run directly on bare metal using Snaps to ensure strict security confinement and isolation.                   |
|  13 | Snaps provide a better security model than running everything in Kubernetes by sandboxing processes and limiting resource access.                                       |
|  14 | Sunbeam allows users to enable additional services like load balancers and observability stacks through simple commands.                                                |
|  15 | The observability stack includes Prometheus, Grafana, Loki, and Alertmanager, which can be deployed embedded or externally.                                             |
|  16 | Sunbeam supports reproducible cloud deployments using manifests that define services and configurations without locking specific package revisions.                     |
|  17 | Sunbeam is designed for both small-scale and large-scale deployments, using charms to manage configuration and ensure consistency across the fleet.                     |
|  18 | Terraform is used under the covers by Sunbeam to drive the deployment and layout of Juju models.                                                                        |
|  19 | The architecture aims to reduce the complexity of OpenStack deployment, making it accessible to users who may not know every configuration detail.                      |
|  20 | Third-party integrations, such as storage drivers, are handled through specific Cinder components and relations within the stack.                                       |
|  21 | Autoscaling for Kubernetes clusters within the OpenStack environment is supported through Magnum integration.                                                           |

# Video

[![Video thumbnail](https://img.youtube.com/vi/yGzptS7Aau0/hqdefault.jpg)](https://www.youtube.com/watch?v=yGzptS7Aau0)

[Watch on YouTube](https://www.youtube.com/watch?v=yGzptS7Aau0)
