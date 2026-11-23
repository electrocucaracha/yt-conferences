---
layout: default
title: "Resilient by Design:  Distributed Zones for the Next Gen OpenStack Cloud"
nav_order: 70
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "This session presents a distributed zone architecture for Red Hat OpenStack, leveraging a Kubernetes-native deployment model where the control plane runs as native pods on OpenShift while the data ..."
resource: "https://www.youtube.com/watch?v=XCJLpUCSmNA"
youtube_stats:
  view_count: 102
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

This session presents a distributed zone architecture for Red Hat OpenStack, leveraging a Kubernetes-native deployment model where the control plane runs as native pods on OpenShift while the data plane remains on bare metal nodes.
The primary objective is to deploy OpenStack across multiple failure domains, such as racks or data centers, to ensure workload resilience and mimic public cloud availability zones.
To achieve this, the architecture mandates strict isolation by dedicating specific storage backends, compute resources, and network subnets to each zone, thereby preventing cross-zone traffic and ensuring that a failure in one zone does not impact others.
Key services like Cinder, Glance, and Manila are configured with zone-specific endpoints and affinity rules to maintain local data access, while Nova cells are used to enhance scalability by isolating messaging and database traffic for specific compute groups.
Finally, the presentation details the use of OpenShift topology managers to pin services to specific zones and outlines a routed spine-and-leaf network design with BGP to facilitate secure, isolated connectivity across the distributed environment.

# Main Points

|   # | Main point                                                                                                                                              |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The presentation covers deploying OpenStack across multiple failure domains using Red Hat OpenShift and Kubernetes-native models.                       |
|   2 | OpenStack control plane services run as native pods on OpenShift, while data plane services run on bare metal nodes.                                    |
|   3 | The goal is to ensure that a failure in one zone does not impact workloads in other zones, mimicking public cloud availability zones.                   |
|   4 | A zone can be defined as a rack, row, floor, or data center depending on the desired level of fault isolation.                                          |
|   5 | Three zones are recommended to maintain quorum for components like MariaDB and Kubernetes masters.                                                      |
|   6 | Hardware design requires one Kubernetes master and multiple workers per zone to ensure high availability and recovery.                                  |
|   7 | Data plane isolation involves dedicating compute and storage resources to each zone to prevent cross-zone traffic and failures.                         |
|   8 | Storage backends, such as Ceph, are dedicated per zone, with local pools for Nova and Cinder to avoid cross-zone latency.                               |
|   9 | Cinder API services are spread across zones, while Cinder volume services are pinned to the zone of their respective storage backend.                   |
|  10 | Cinder backup currently supports a single target backend, though improvements are planned to allow per-zone backup services.                            |
|  11 | Glance uses multi-store configuration with one store per zone to ensure local image access and avoid cross-zone traffic.                                |
|  12 | Glance APIs are split into external and internal endpoints, with internal APIs dedicated to specific zones to serve local compute nodes.                |
|  13 | Nova configuration uses Kubernetes ConfigMaps to define localStorage backends and override Glance endpoints for zone-specific image retrieval.          |
|  14 | Manila shares follow a similar pattern to Cinder, with dedicated backends and share services per zone to isolate traffic.                               |
|  15 | Cross-zone attachment of volumes is disabled to prevent latency issues and ensure data locality.                                                        |
|  16 | User experience involves specifying availability zones when creating volumes and booting VMs to ensure resources are provisioned locally.               |
|  17 | Kubernetes topology spread constraints and node affinities are used to schedule services either across zones or pinned to specific zones.               |
|  18 | Nova cells divide compute nodes into groups with dedicated RabbitMQ and Galera clusters to improve scalability in large deployments.                    |
|  19 | Cell zero contains global services like Nova API and scheduler, while other cells handle specific compute node groups.                                  |
|  20 | Network isolation is achieved by creating separate subnets for control plane, internal API, external, tenant, storage, and management traffic per zone. |
|  21 | Physical connectivity uses a routed spine-and-leaf architecture with BGP for inter-zone routing.                                                        |
|  22 | OpenShift capabilities, including NADs and Metal Operator, are used to configure isolated networks on worker nodes.                                     |
|  23 | Octavia load balancers are segregated by zone, with each zone managing its own Amphora instances and control plane.                                     |
|  24 | Keystone remains a single instance for the entire OpenStack installation, scheduled for high availability but not zone-specific.                        |
|  25 | OVN support for Octavia is not yet available but is under internal development.                                                                         |
|  26 | Cell zero RabbitMQ is dedicated to global services, and its placement may need consideration if inter-zone latency is high.                             |

# Video

[![Video thumbnail](https://img.youtube.com/vi/XCJLpUCSmNA/hqdefault.jpg)](https://www.youtube.com/watch?v=XCJLpUCSmNA)

[Watch on YouTube](https://www.youtube.com/watch?v=XCJLpUCSmNA)
