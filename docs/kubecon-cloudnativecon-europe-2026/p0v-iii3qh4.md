---
layout: default
title:
  "Cloud Native Theater | KubeVirt Summit: Bridging Islands: EVPN Overlays for
  Multi-C... Miguel Duarte"
nav_order: 71
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Miguel from Red Hat’s networking team presents on implementing EVPN overlays
  for multicluster KubeVirt environments. He explains the motivation for this approach,
  highlighting challenges with legacy applications that require L2 adjacency, t...
resource: https://www.youtube.com/watch?v=P0V_IiI3Qh4
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

Miguel from Red Hat’s networking team presents on implementing EVPN overlays for multicluster KubeVirt environments.
He explains the motivation for this approach, highlighting challenges with legacy applications that require L2 adjacency, the need for resiliency and hybrid cloud scenarios, and the scalability limitations of traditional VLANs.
EVPN, built on top of BGP, enables stretched layer 2 networks across clusters, efficient routing, reduced broadcast traffic, and seamless workload mobility, particularly for live VM migration.
The solution integrates existing components like KubeVirt, OpenP Router (using FRR), Linux bridges, and various CNIs, aiming for a Kubernetes-native, declarative API to simplify configuration.
In a demo, Miguel shows live migration of a VM between clusters with minimal packet loss, demonstrating that workloads remain accessible via their IP addresses throughout the process, thus validating the effectiveness of the EVPN-based multicluster networking solution.

# Main Points

|   # | Main point                                                                                           |
| --: | ---------------------------------------------------------------------------------------------------- |
|   1 | Presenter: Miguel from Red Hat networking team, focusing on downstream distribution of KubeVirt.     |
|   2 | Topic: EVPN overlays for multicluster KubeVirt environments.                                         |
|   3 | Agenda: Motivation, goals, EVPN overview, implementation, demo, conclusions.                         |
|   4 | Motivation:                                                                                          |
|   5 | Legacy applications require L2 adjacency; VMs often tied to specific IP/MAC addresses.               |
|   6 | Multicluster setups increase resiliency and support hybrid cloud scenarios.                          |
|   7 | Problems with multicluster:                                                                          |
|   8 | Scalability: VLANs are limited (4094 max), not suitable for large/multi-tenant environments.         |
|   9 | Efficiency: High ARP/neighbor discovery traffic with many workloads.                                 |
|  10 | Network convergence: Need immediate service availability after migration.                            |
|  11 | Solution: EVPN (Ethernet VPN)                                                                        |
|  12 | Enables stretched L2 networks across clusters.                                                       |
|  13 | Supports routing between networks.                                                                   |
|  14 | Reduces broadcast/bomb traffic (ARP, NDP).                                                           |
|  15 | Enables seamless workload mobility (live migration).                                                 |
|  16 | EVPN details:                                                                                        |
|  17 | Control plane protocol using multiprotocol BGP.                                                      |
|  18 | Type 2 routes: Advertise MAC/IP for stretched L2 and live migration.                                 |
|  19 | Type 5 routes: Advertise network prefixes for routing between networks.                              |
|  20 | Data plane: Uses VXLAN; can support SRv6, MPLS.                                                      |
|  21 | Implementation principles:                                                                           |
|  22 | Integrate existing solutions; avoid reinventing the wheel.                                           |
|  23 | Support multiple CNIs; user can choose preferred CNI.                                                |
|  24 | Building blocks: KubeVirt, OpenP Router (FRR-based), various CNIs (OVS, bridge, etc.).               |
|  25 | OpenP Router runs on each Kubernetes node, exposes networking via veth pairs to bridges.             |
|  26 | Currently supports secondary network attachments; working on cluster default network support.        |
|  27 | Uses Linux VRFs, veth pairs, and bridges for integration.                                            |
|  28 | Kubernetes-native, declarative API for user intent; generates FRR and network configs automatically. |
|  29 | Demo:                                                                                                |
|  30 | Two kind clusters interconnected via routers.                                                        |
|  31 | External client accesses VMs in both clusters using direct IP.                                       |
|  32 | Live migration of VM from cluster A to B; minimal packet loss (~400ms).                              |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=P0V_IiI3Qh4)
