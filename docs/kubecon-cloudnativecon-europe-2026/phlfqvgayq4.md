---
layout: default
title: Let Your Network Speak! - Nadia Pinaeva, NVIDIA & Joel Takvorian, Red Hat
nav_order: 201
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this presentation, Nadia from NVIDIA and Joel from Red Hat introduce
  NetObserve, an open-source, mostly CNI-agnostic Kubernetes operator for network
  observability that uses eBPF agents to collect and correlate network traffic data
  with K...
resource: https://www.youtube.com/watch?v=PHLfqvgaYq4
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

In this presentation, Nadia from NVIDIA and Joel from Red Hat introduce NetObserve, an open-source, mostly CNI-agnostic Kubernetes operator for network observability that uses eBPF agents to collect and correlate network traffic data with Kubernetes resources.
They demonstrate NetObserve’s features, such as collecting network flows, DNS decoding, TCP latency, packet drops, NAT tracking, and customizable metrics and alerts, as well as its integration with OVN-Kubernetes for enhanced network policy debugging.
Through live and recorded demos, they show how NetObserve helps users visualize network flows, identify issues like DNS errors or misconfigured network policies, and trace the reasons for allowed or dropped traffic, even in complex environments with multiple overlapping policies.
The integration between NetObserve and networking plugins enables mapping of low-level ACL decisions back to Kubernetes network policies, greatly improving the ability to debug and secure network connectivity.
The Q&A covers topics such as data retention (handled by external storage solutions), openness to supporting other CNIs, potential integration with OpenStack, and the need for collaboration between observability tools and networking plugins for full functionality.

# Main Points

|   # | Main point                                                                                                                                        |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Introduction to network observability and integration with observability tools                                                                    |
|   2 | Presenters: Nadia (NVIDIA, Kubernetes networking) and Joel Tagan (Red Hat, network observability)                                                 |
|   3 | Introduction of NetObserve: open source Kubernetes operator for network traffic observation using eBPF agents                                     |
|   4 | NetObserve installs eBPF agents on each node to collect network traffic data and send to collectors                                               |
|   5 | Mostly CNI-agnostic, but some features depend on specific CNIs (e.g., network policy correlation)                                                 |
|   6 | Originated at Red Hat, moving toward vendor-neutral, possibly CNCF sandbox project                                                                |
|   7 | Features:                                                                                                                                         |
|   8 | Collects network flows from packet headers (IPs, ports)                                                                                           |
|   9 | Correlates flows with Kubernetes resources (pods, services, nodes)                                                                                |
|  10 | DNS decoding and error capture                                                                                                                    |
|  11 | TCP latency and packet drop detection                                                                                                             |
|  12 | NAT tracking and cloud availability zone info                                                                                                     |
|  13 | Upcoming: TLS and QUIC usage tracking                                                                                                             |
|  14 | Network events (policy allow/deny) visible in flows                                                                                               |
|  15 | API extension for custom metrics and alerts                                                                                                       |
|  16 | Demo:                                                                                                                                             |
|  17 | NetObserve UI displays network flows, source/destination, ports, DNS info                                                                         |
|  18 | Topology view visualizes traffic between namespaces/resources                                                                                     |
|  19 | Overview provides high-level metrics and charts                                                                                                   |
|  20 | Network health shows alerts/issues with predefined rules                                                                                          |
|  21 | Filtering and runbooks help diagnose issues (e.g., DNS typos)                                                                                     |
|  22 | Pain point: Debugging Kubernetes network policies is complex due to multiple overlapping policies (namespace and cluster-wide)                    |
|  23 | Integration with OVN-Kubernetes:                                                                                                                  |
|  24 | Network policies translated to ACLs (Access Control Lists)                                                                                        |
|  25 | New feature: sampling packets at ACL decision points, sending samples with ACL info                                                               |
|  26 | eBPF agent hooks into np_sample function, aggregates data, correlates ACL IDs with flows                                                          |
|  27 | User space correlation maps ACL IDs back to Kubernetes network policies                                                                           |
|  28 | Second demo:                                                                                                                                      |
|  29 | Shows how NetObserve and OVN-Kubernetes integration helps debug network policy issues (e.g., dropped/allowed connections, misconfigured policies) |
|  30 | Demonstrates update                                                                                                                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=PHLfqvgaYq4)
