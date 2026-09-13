---
type: Video Note
title: "When DNS Blinks: Scaling and Hardening CoreDNS in Critical Cloud Infra... Yong Tang & John Belamaric"
description: "In this session, Yan Tang and John Palmer from Google discuss the evolution and current state of CoreDNS, a flexible, plugin-based DNS server that has been widely adopted as the default DNS server in Kubernetes since 2017. They provide an o..."
resource: https://www.youtube.com/watch?v=9UIPskZ07dY
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this session, Yan Tang and John Palmer from Google discuss the evolution and current state of CoreDNS, a flexible, plugin-based DNS server that has been widely adopted as the default DNS server in Kubernetes since 2017.
They provide an overview of CoreDNS’s architecture, highlighting its extensibility, support for multiple protocols, and integration with cloud services.
The speakers detail recent updates, including new plugins, security improvements, and the introduction of multisocket support, which significantly enhances vertical scalability and performance.
They address lessons learned from recent DNS outages, emphasizing configuration options like prefetch, serve-stale, and node-local DNS cache to improve resilience and reduce failure domains.
The session concludes with a discussion on managing multi-tenant environments, recommending strategies such as node-local DNS and dedicated CoreDNS instances per tenant to mitigate the impact of misbehaving users, and encourages community contributions to the open-source project.
# Main Points

|   # | Main point                                                                                                                                                                                                  |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Yan Tang and John Palmer from Google discussed the audience project, specifically CoreDNS.                                                                                                                  |
|   2 | CoreDNS is a flexible, plugin-based DNS server written in Go, developed over 10 years ago.                                                                                                                  |
|   3 | CoreDNS is the default DNS server in Kubernetes since 2017, leading to wide adoption.                                                                                                                       |
|   4 | Supports service discovery, multiple protocols (DNS, DNS-over-TLS, DNS-over-HTTPS, gRPC, QUIC, HTTP/3), and cloud integration.                                                                              |
|   5 | Over 400 contributors, 14,000 stars, 29 maintainers, and a growing list of public adopters.                                                                                                                 |
|   6 | Recent release: 1.14.2, with new plugins (Nomad, DSO83, proxy protocol) and features (connection pooling, multiplex connection, API limiting).                                                              |
|   7 | Addressed several CVEs in the past 5-6 months; more fixes coming in 1.14.3.                                                                                                                                 |
|   8 | DNS outages (e.g., Amazon US East-1) highlight the importance of robust DNS infrastructure.                                                                                                                 |
|   9 | CoreDNS benefits from Go’s memory safety and smaller codebase compared to traditional DNS servers.                                                                                                          |
|  10 | Key configuration options for resilience: prefetch (keeps cache fresh), lame duck (drains requests before shutdown), serve_stale (serves stale records if upstream fails), and multiple upstream providers. |
|  11 | NodeLocal DNS Cache in Kubernetes improves resilience and performance by providing local caching, subdomain configuration, and TCP upgrades to avoid UDP-related issues.                                    |
|  12 | Multisocket support (since 1.12) enables better vertical scaling by distributing packets across multiple sockets, allowing near-linear performance growth with more CPUs.                                   |
|  13 | Cluster proportional autoscaling can be replaced by CPU-based autoscaling due to improved vertical scalability.                                                                                             |
|  14 | CoreDNS community is open-source driven, with contributors often focusing on specific plugins or features.                                                                                                  |
|  15 | For multi-tenant environments, recommendations include using NodeLocal DNS to reduce failure domains and dedicating CoreDNS instances per tenant.                                                           |
|  16 | Scaling out and adding caching layers are effective strategies for handling high loads and misbehaving tenants.                                                                                             |
|  17 | Be aware of cloud provider limits on packets per                                                                                                                                                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=9UIPskZ07dY)