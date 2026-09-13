---
layout: default
title:
  "Evolving Baremetal-as-a-Service: Secure Multi-Cluster Network... Yushiro Furukawa
  & Mitsuhiro Tanino"
nav_order: 106
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The presentation introduces Flava, a next-generation private cloud platform
  developed by Edy Corporation, designed to provide unified, scalable, and reliable
  infrastructure across multiple regions and availability zones. Built on OpenStack...
resource: https://www.youtube.com/watch?v=MgerB2Tl0MQ
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

The presentation introduces Flava, a next-generation private cloud platform developed by Edy Corporation, designed to provide unified, scalable, and reliable infrastructure across multiple regions and availability zones.
Built on OpenStack and Kubernetes, Flava manages over 3,000 bare metal servers and 9,200 virtual machines, offering bare metal as a service (BMaaS) to support use cases such as AI/ML workloads, legacy system migration, storage-intensive applications, and software with CPU-based licensing.
The platform’s architecture is based on three pillars: a unified API for both virtual machines and bare metal servers, a Kubernetes-native control plane for high availability and self-healing, and integrated networking and security through in-house VPC agents and ACL policies.
Key technical improvements include replacing a resource-intensive Ansible-based deployment with Kubernetes custom controllers, reducing deployment time from hours to minutes and significantly lowering operational overhead.
The team also addressed challenges in hardware management, OS installation, and network integration, and discussed their decision to reuse existing in-house tools rather than adopting solutions like Ironic, as well as their current limitations regarding autoscaling for bare metal nodes.
Audience questions focused on deployment strategies, infrastructure-as-code tools, autoscaling, network management, and the transition process, which resulted in substantial efficiency gains and resource savings.

# Main Points

|   # | Main point                                                                                                                                    |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation covers secure multicluster networking and secure identity automation for bare metal as a service (BMaaS)                         |
|   2 | Presenters: Yushiro Furkawa and Iano, senior software engineers at Edy Corporation                                                            |
|   3 | Flava is Edy Corporation’s next-generation private cloud, built on OpenStack and Kubernetes, spanning multiple regions and availability zones |
|   4 | Flava manages over 500 hypervisors, 9,200 VMs, and 3,000+ bare metal servers across two regions and six AZs (as of June 2025)                 |
|   5 | Four key BMaaS use cases: AI/ML workloads, legacy system migration, storage workloads, and software with CPU core-based licensing             |
|   6 | Three pillars of BMaaS:                                                                                                                       |
|   7 | Unified API: Single API for both VMs and bare metal servers; same commands for users, different backend processes                             |
|   8 | Control plane built entirely on Kubernetes: All management components run on Kubernetes for high availability and resilience                  |
|   9 | Integrated network and security: In-house VPCs, ACL policies, and security integrations for both VMs and bare metal                           |
|  10 | Management plane is highly available, distributed across three AZs per region for disaster recovery                                           |
|  11 | IPMI used for physical hardware control; asynchronous pipeline decouples slow hardware operations from API responsiveness                     |
|  12 | OS installation and management automated via Kubernetes controllers, enabling self-healing and declarative management                         |
|  13 | Scalability improvements:                                                                                                                     |
|  14 | Moved from Ansible-based deployment (one pod per server) to Kubernetes custom controllers                                                     |
|  15 | Reduced deployment time from 2 hours to ~10 minutes                                                                                           |
|  16 | Reduced worker nodes from 55+ to ~10                                                                                                          |
|  17 | Configuration managed via Git; changes automated through custom resources and controllers                                                     |
|  18 | Network and security integrations:                                                                                                            |
|  19 | ACL policies between Kubernetes clusters and for bare metal servers via in-house VPC agent                                                    |
|  20 | User scripts and metadata API support for automation during server boot                                                                       |
|  21 | X.509 certificate provisioning for bare metal instances                                                                                       |
|  22 | Transition to new architecture reduced operational costs and deployme                                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=MgerB2Tl0MQ)
