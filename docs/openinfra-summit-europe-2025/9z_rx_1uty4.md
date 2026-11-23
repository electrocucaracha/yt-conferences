---
layout: default
title: "OpenStack Sunbeam: A Year of Progress"
nav_order: 21
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Billy Olsen from Canonical presented Sunbeam, an OpenStack deployment tool designed to simplify cloud management for users ranging from beginners to enterprise administrators."
resource: "https://www.youtube.com/watch?v=9z_rX_1UTy4"
youtube_stats:
  view_count: 277
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

Billy Olsen from Canonical presented Sunbeam, an OpenStack deployment tool designed to simplify cloud management for users ranging from beginners to enterprise administrators.
The project aims to make OpenStack accessible by reducing the steep learning curve associated with traditional setups, leveraging a control plane on Kubernetes and a data plane on bare metal.
Key features include a streamlined deployment process via simple commands, robust security through strict Snap confinement, and advanced capabilities such as instance recovery without stonewalling, resource optimization, and support for SR-IOV and DPDK.
Olsen highlighted recent progress, including the addition of LDAP and OpenID identity providers, network-only nodes for security, and file sharing services, while outlining future plans for third-party storage, multi-region support, and broader architecture compatibility.
The presentation emphasized Sunbeam’s commitment to maintaining upstream OpenStack compatibility to avoid vendor lock-in, ensuring that users can easily migrate or integrate with other tools while benefiting from an automated, secure, and scalable cloud infrastructure.

# Main Points

|   # | Main point                                                                                                                                                                                                  |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Sunbeam is an OpenStack project by Canonical designed to simplify deployment, scalability, and operation for users ranging from beginners to enterprise administrators.                                     |
|   2 | The project aims to lower the barrier to entry for OpenStack by targeting users with less specialized experience, such as recent graduates, while maintaining production-grade capabilities.                |
|   3 | Sunbeam runs the control plane on Kubernetes and the data plane on bare metal, distinguishing itself from other Kubernetes-based OpenStack deployments through its focus on simplicity and user experience. |
|   4 | The deployment process is streamlined to a simple command sequence, aiming to reduce the complexity traditionally associated with OpenStack installation and configuration.                                 |
|   5 | Lifecycle management features include easy node addition and removal, automated service balancing, and controlled cluster upgrades to new OpenStack versions.                                               |
|   6 | A maintenance mode feature allows administrators to safely take nodes offline by using the Watcher resource optimizer to migrate instances and services before hardware maintenance.                        |
|   7 | Identity and access management supports LDAP and OpenID Connect providers, including built-in configurations for Google, Okta, and Entra ID, to simplify single sign-on integration.                        |
|   8 | Network-only nodes can be deployed to centralize traffic flow for enhanced security monitoring and packet detection at the cloud ingress and egress points.                                                 |
|   9 | Security is enforced through Snap strict confinement, which sandboxes services like the hypervisor and storage daemons to limit access to only necessary system resources.                                  |
|  10 | Instance high availability is implemented using a console driver approach that avoids the use of Pacemaker or stonith, preventing unnecessary compute node shutdowns during network issues.                 |
|  11 | Container orchestration is provided as a service using the Cluster API drivers, offering long-term support for Kubernetes version 1.32 with full OpenStack integration.                                     |
|  12 | Resource optimization utilizes the Watcher project to balance CPU and storage resources, optimize power consumption, and support maintenance workflows.                                                     |
|  13 | Hardware capabilities such as SR-IOV, DPDK, and GPU passthrough are automatically detected and configured based on host specifications to maximize performance.                                             |
|  14 | File sharing services are being enabled via the Manila project, with initial support for SEFS and future plans for other storage backends like NetApp.                                                      |
|  15 | Cloud validation is supported through automated Tempest and RefStack tests to verify compliance and service health, with options for scheduled background checks.                                           |
|  16 | Current features include Barbican with Vault backend, Ceph, Designate, Glance, Heat, Magnum, Nova, Octavia, and an observability stack.                                                                     |
|  17 | Upcoming features include third-party storage support, multi-region cluster management, Ironic bare metal support, and CloudKitty for billing and rating.                                                   |
|  18 | The project encourages community contributions for documentation, feature development, and feedback to improve the OpenStack ecosystem.                                                                     |
|  19 | Sunbeam uses Terraform under the hood for infrastructure provisioning but recommends using bare metal deployment systems like MAAS for initial node setup.                                                  |
|  20 | The design philosophy prioritizes using upstream OpenStack components to avoid vendor lock-in and ensure compatibility with the broader open-source community.                                              |

# Video

[![Video thumbnail](https://img.youtube.com/vi/9z_rX_1UTy4/hqdefault.jpg)](https://www.youtube.com/watch?v=9z_rX_1UTy4)

[Watch on YouTube](https://www.youtube.com/watch?v=9z_rX_1UTy4)
