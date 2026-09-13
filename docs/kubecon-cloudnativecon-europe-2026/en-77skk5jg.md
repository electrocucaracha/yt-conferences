---
layout: default
title:
  "10 Years of Cilium: Connecting, Securing, and Simplifying the... Bill M, Paul
  A, Marcelo M & Neha A"
nav_order: 2
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The session marked the 10th anniversary of Cilium, a CNI project that
  has become a standard for cloud-native networking, security, and observability,
  powered by eBPF. The speakers highlighted Cilium’s growth to over 1,000 contributors
  and i...
resource: https://www.youtube.com/watch?v=EN_77SkK5jg
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

The session marked the 10th anniversary of Cilium, a CNI project that has become a standard for cloud-native networking, security, and observability, powered by eBPF.
The speakers highlighted Cilium’s growth to over 1,000 contributors and its widespread adoption, with two-thirds of Kubernetes users selecting it as their CNI.
Marcelo from Celonis shared their migration journey to Cilium, emphasizing the need for a unified, scalable solution to manage complex, multi-cloud environments and detailing their phased migration strategy and lessons learned.
Paul introduced Tetragon, Cilium’s runtime security sibling, which leverages eBPF for deep observability and enforcement, and described its rapid feature development since 2022.
Niha from Microsoft discussed major investments in Cilium, including multicluster scalability, hybrid routing, and the integration of Z tunnel and Spire for native, sidecarless MTLS encryption, enhancing security for AI-era workloads.
The session concluded with community updates, new resources, and an invitation for further contributions to the Cilium ecosystem.

# Main Points

|   # | Main point                                                                                                                                                                          |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Psyllium is a CNI providing observability and security, powered by eBPF.                                                                                                            |
|   2 | Project is 10 years old, with over 1,000 contributors and nearly 50,000 GitHub stars.                                                                                               |
|   3 | In the latest Kubernetes networking report, Psyllium is the top CNI, used by two-thirds of respondents.                                                                             |
|   4 | Key features include gateway API, multicluster connectivity, eBPF-based capabilities, and MTLS with Zunnel.                                                                         |
|   5 | Only graduated CNI project in CNCF; continues to innovate with each release.                                                                                                        |
|   6 | Recent 1.19 release added Zunnel integration, Gateway API 1.14 support, improved IPv6/dual stack, BGP integration, multi-pool IPAM, DNS host firewall, and enhanced packet tracing. |
|   7 | Salonus uses Psyllium for large-scale, multi-cloud infrastructure (AWS, Azure, GCP), handling 3.5TB daily bandwidth and 360 million daily requests across 160+ clusters.            |
|   8 | Migration to Psyllium involved hybrid CNI mode, gradual workload migration, and eventual exclusive Psyllium operation.                                                              |
|   9 | Key migration lessons: redesign network policies, monitor BPF maps, and support development teams with policy ownership.                                                            |
|  10 | Tetragon is Psyllium’s runtime security tool, providing process execution, network/file access, and layer 7 observability via eBPF.                                                 |
|  11 | Tetragon features: Kubernetes identity-aware policies, reduction filters, support for cryo/containerd, persistent enforcement, user space hooks, event throttling.                  |
|  12 | Microsoft is heavily investing in Psyllium, contributing to scalability and multicluster features.                                                                                  |
|  13 | New hybrid routing mode and identity filtering improve multicluster scalability and performance.                                                                                    |
|  14 | MTLS and workload-level identity now natively integrated via Zunnel and Spire, enabling end-to-end encryption without sidecars.                                                     |
|  15 | Community updates: new books, case studies, white papers, and EBPF meetup program.                                                                                                  |
|  16 | Invitation to join the community, attend meetings, and contribute.                                                                                                                  |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=EN_77SkK5jg)
