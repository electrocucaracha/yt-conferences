---
layout: default
title:
  "Project Lightning Talk: OVN-Kubernetes: Scalable, Production-Grade Networking...
  Surya Seetharaman"
nav_order: 233
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  Surya, an engineer at Red Hat and maintainer of the OVN Kubernetes project,
  introduces OVN Kubernetes as a scalable, production-grade networking plugin for
  Kubernetes clusters, currently adopted by companies like Nvidia and Red Hat. He
  clar...
resource: https://www.youtube.com/watch?v=5SP7RS_DnIE
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

Surya, an engineer at Red Hat and maintainer of the OVN Kubernetes project, introduces OVN Kubernetes as a scalable, production-grade networking plugin for Kubernetes clusters, currently adopted by companies like Nvidia and Red Hat.
He clarifies that OVN Kubernetes is distinct from similarly named projects and is built on OpenVSwitch (OVS) and OVN, both Linux Foundation projects, to abstract and manage complex networking topologies within Kubernetes.
The project, founded in 2016 and recently added to the CNCF as a sandbox project, translates Kubernetes events into OVN logical constructs, enabling features such as port-to-port networking, network policies, egress and bandwidth controls, hardware offload, and user-defined networks for multi-tenancy and BGP route advertisement.
OVN Kubernetes also collaborates with the KubeVirt community to support VM networking use cases, including persistent static IPs and consistent egress IPs.
Looking ahead, the project aims to add support for EVPN to extend network isolation to provider fabrics, further bridging traditional and Kubernetes networking, and invites contributors and adopters to join via their site, Slack channel, or at their CubeCon kiosk.

# Main Points

|   # | Main point                                                                                                                                                                   |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | OVN Kubernetes is a CNCF project providing a production-grade, scalable networking plugin for Kubernetes clusters.                                                           |
|   2 | Main adopters include Nvidia (cloud gaming environments) and Red Hat (OpenShift).                                                                                            |
|   3 | OVN Kubernetes is often confused with kube-ovn, but they are separate projects.                                                                                              |
|   4 | Uses Open vSwitch (OVS) as the data plane on every node.                                                                                                                     |
|   5 | OVN is an abstraction on top of OVS, simplifying networking constructs into logical network topologies.                                                                      |
|   6 | Both OVN and OVS are Linux Foundation projects; OVN Kubernetes leverages both.                                                                                               |
|   7 | Project founded in 2016; joined CNCF as a sandbox project last year.                                                                                                         |
|   8 | OVN Kubernetes architecture watches Kubernetes events/objects and translates them into OVN logical constructs (e.g., node creation results in virtual routers and switches). |
|   9 | Supports core Kubernetes networking features: port-to-port networking via Geneva encapsulation tunnels, services, network policies, admin network policies.                  |
|  10 | Advanced features include egress controls, bandwidth controls, hardware offload for wire-speed networking, and enhanced security.                                            |
|  11 | New release features user-defined networks, allowing creation of multiple isolated networks per cluster/namespace for multi-tenancy.                                         |
|  12 | User-defined networks can be advertised using BGP for route import/export.                                                                                                   |
|  13 | Collaborates with the KubeVirt community for VM networking use cases, including static IPs for VMs and persistent source IPs for egress traffic.                             |
|  14 | Supports both Geneva encapsulation (overlay) and BGP (no overlay) networking modes.                                                                                          |
|  15 | Adding support for EVPN to extend user-defined networks to provider network fabrics for greater isolation.                                                                   |
|  16 | Aims to bridge data center, traditional, and enterprise networking with Kubernetes networking.                                                                               |
|  17 | Community involvement: site QR code, CNCF Slack channel, alternate Monday community meetings, kiosk 15A at CubeCon.                                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=5SP7RS_DnIE)
