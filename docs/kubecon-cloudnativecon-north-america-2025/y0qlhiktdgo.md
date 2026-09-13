---
type: Video Note
title: "TikTok's IPv6 Journey To Cilium: Pitfalls and Lessons Learned - Giri Kuncoro & Joseph Pallamidessi"
description: "In this session, TikTok’s security engineering team detailed their two-year journey migrating Kubernetes clusters to IPv6-only networking using Cilium. Their infrastructure spans over 130 globally distributed virtual data centers, requiring..."
resource: https://www.youtube.com/watch?v=y0qlhiKtDGo
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this session, TikTok’s security engineering team detailed their two-year journey migrating Kubernetes clusters to IPv6-only networking using Cilium.
Their infrastructure spans over 130 globally distributed virtual data centers, requiring a robust, high-performance CNI to handle millions of packets per second and strict security and observability needs.
Initially, Cilium lacked IPv6-only support, leading the team to use Calico as a workaround while collaborating with the open source community and Cilium maintainers to address issues such as lack of IPv6 encapsulation, DNS proxy bugs, and service handling failures.
Through iterative testing and community engagement, key features like IPv6 underlay encapsulation and improved debugging tools were added in Cilium 1.18, enabling successful production rollout in several clusters.
The team emphasized the value of open source collaboration, the importance of encapsulation mode for ease of deployment, and the necessity of IPv6 due to IPv4 exhaustion and TikTok’s rapid growth, while also sharing practical debugging techniques and lessons learned for others pursuing similar migrations.
# Main Points

|   # | Main point                                                                                                                                                                                         |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | TikTok's Security Engineering team manages Kubernetes clusters for internal security services.                                                                                                     |
|   2 | Infrastructure spans ~130 virtual data centers across 10 logical regions, using a globally distributed, multi-DC architecture.                                                                     |
|   3 | Security services include authentication, authorization, identity management, key management, signing, and encryption.                                                                             |
|   4 | Clusters handle 300-400K concurrent connections each, with high data throughput and low-latency requirements.                                                                                      |
|   5 | Chose Cilium as CNI for high performance, security features, observability, and ecosystem support.                                                                                                 |
|   6 | TikTok uses a flat network with 4-5 million globally unique IPs; running out of IPv4 addresses prompted move to IPv6-only data centers.                                                            |
|   7 | Initial attempts to run Cilium on IPv6-only clusters (v1.12, 2023) failed due to lack of IPv6 encapsulation support.                                                                               |
|   8 | Native routing mode required BGP for pod routing, but cluster admins lacked network control; cluster-level BGP with kube-router was partially successful but caused packet loss due to NDP issues. |
|   9 | NDP packet drop issue fixed in Cilium v1.14, but DNS proxy checksum bug blocked IPv6 DNS (fixed in v1.15).                                                                                         |
|  10 | Service handling and NodePort issues persisted due to encapsulation limitations; raised issues with Cilium community.                                                                              |
|  11 | Cilium v1.18 (May 2025) introduced IPv6 underlay encapsulation and improved kube-proxy replacement, resolving major issues.                                                                        |
|  12 | Successfully rolled out Cilium IPv6-only clusters in production (4 clusters as of now).                                                                                                            |
|  13 | Key debugging tools: Hubble for observability, Cilium CLI debug, and pwru for eBPF tracing.                                                                                                        |
|  14 | Encapsulation/tunnel mode is easier to operate than native routing in environments without network control.                                                                                        |
|  15 | Cilium's ecosystem and community support were crucial for success.                                                                                                                                 |
|  16 | Main driver for IPv6-only: exhaustion of IPv4 addresses due to rapid growth.                                                                                                                       |
|  17 | Access control is managed via Cilium Network Policies at L3/L4/L7.                                                                                                                                 |
|  18 | Largest clusters have ~50 large nodes; complexity is in workload scale, not node count.                                                                                                            |
|  19 | Migration from Calico to Cil                                                                                                                                                                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=y0qlhiKtDGo)