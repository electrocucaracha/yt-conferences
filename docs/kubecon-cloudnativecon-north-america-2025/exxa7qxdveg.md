---
layout: default
title:
  "Kubernetes IP Management: From Core Concepts To Strategic Solutions - Ivy
  Zhuang & Whitney Jenkins"
nav_order: 139
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  In this presentation, Whitney Jenkins and Ivy from Google discuss Kubernetes
  IP management in Google Kubernetes Engine (GKE), focusing on core concepts, challenges,
  and recent solutions. They explain GKE’s flat network model, where each pod...
resource: https://www.youtube.com/watch?v=EXxa7Qxdveg
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

In this presentation, Whitney Jenkins and Ivy from Google discuss Kubernetes IP management in Google Kubernetes Engine (GKE), focusing on core concepts, challenges, and recent solutions.
They explain GKE’s flat network model, where each pod receives a unique, routable IP from the VPC, enabling direct integration with Google Cloud services and enhancing observability.
The speakers outline complexities in IP planning, especially with IPv4 scarcity, and describe strategies to mitigate IP exhaustion, such as leveraging additional RFC1918 ranges, non-RFC1918 ranges, and the Class E address space.
They introduce new features like multipod CIDR, multi-subnet clusters, multi-service CIDR, and auto IPAM, which automate and simplify IP allocation and scaling.
The session also covers improved observability tools, such as the GKE IP masquerading analyzer and subnet utilization metrics, and addresses common misconceptions and questions about IP management, load balancing, and network models in GKE.

# Main Points

|   # | Main point                                                                                                                                                                                  |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | GKE uses a flat, fully integrated network where each pod receives a unique, routable IP from the VPC's IP range.                                                                            |
|   2 | Pod IPs are visible throughout the network, enhancing observability and simplifying debugging.                                                                                              |
|   3 | Pod IP ranges can be accessed on-prem via GCP tools like CloudVPN or Cloud Interconnect.                                                                                                    |
|   4 | Kubernetes delegates network implementation to plugins; CNI provides a pluggable interface for networking.                                                                                  |
|   5 | GKE’s default networking mode is VPC-native; pods get real IPs from VPC secondary ranges.                                                                                                   |
|   6 | GKE uses standard CNI plugins, with DPv2 using Cilium/eBPF for higher performance and security.                                                                                             |
|   7 | When configuring a GKE cluster, you must plan IP ranges for pods, nodes, and services, considering future growth.                                                                           |
|   8 | Subnet stack type (IPv4 or dual stack) determines cluster type; dual stack supports both IPv4 and IPv6.                                                                                     |
|   9 | Default max pods per node is 110, requiring a /24 (256 IPs) per node.                                                                                                                       |
|  10 | IPv4 clusters use only IPv4; Google reserves over 4,000 IPs for services.                                                                                                                   |
|  11 | Dual stack clusters assign both IPv4 and IPv6 addresses to pods and nodes; requires DPv2.                                                                                                   |
|  12 | IPv6 clusters offer a vast address space, reducing IP planning concerns.                                                                                                                    |
|  13 | GKE can be wasteful with IPv4 due to allocation inefficiencies (e.g., 2x pod IP requirement).                                                                                               |
|  14 | IP exhaustion and observability are common challenges; spreadsheets are often used for tracking.                                                                                            |
|  15 | Strategies to mitigate IPv4 exhaustion: use all RFC1918 ranges, leverage 100.64.0.0/10, and use Class E (240.0.0.0/4) addresses.                                                            |
|  16 | Class E addresses can be used with many Google services and have no performance limitations.                                                                                                |
|  17 | New features: multipod CIDR (add pod IP ranges), multi-subnet clusters (add subnets for nodes/pods), multi-service CIDR (multiple service ranges), and auto IPAM (automatic IP allocation). |
|  18 | GKE IP masquerading analyzer is integrated into Network Intelligence Center for diagnosing egress issues.                                                                                   |
|  19 | Subnet utilization feature shows IPv4/IPv6 usage and warns about high utilization during VM creation.                                                                                       |
|  20 | Documentation and blog posts are AVA                                                                                                                                                        |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=EXxa7Qxdveg)
