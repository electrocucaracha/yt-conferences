---
type: Video Note
title: "Smart Routing at Scale: How Spotify’s XDS Control Plane Cut 75%... Yannick Epstein & Anya Hristova"
description: "In this CubeCon presentation, Ana Christoa and Yanikai from Spotify describe how they reduced cross-zone egress costs by 75% using an XDS-based control plane for service discovery and routing. They explain the challenges of optimizing traff..."
resource: https://www.youtube.com/watch?v=oFdW1yAoaHc
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this CubeCon presentation, Ana Christoa and Yanikai from Spotify describe how they reduced cross-zone egress costs by 75% using an XDS-based control plane for service discovery and routing.
They explain the challenges of optimizing traffic within a large, multi-region, multi-zone infrastructure, where naive solutions can compromise reliability or overload zones.
Initially, Spotify used DNS-based service discovery and a custom load balancer (ELS), but this approach was limited by its lack of zone awareness.
By adopting XDS, they implemented a two-level routing system that uses real-time load reports to dynamically assign traffic weights to zones, maximizing same-zone traffic without overloading any zone.
They further improved reliability by developing a dynamic capacity model that accounts for real server capacity and slow-starting instances, addressing issues encountered in production.
The result was a significant reduction in cross-zone traffic and costs, with the new system proving robust even during scaling events and failures.
# Main Points

|   # | Main point                                                                                                                                            |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Spotify operates a large-scale, multi-region, multi-zone infrastructure with over 2 million nodes.                                                    |
|   2 | Cross-zone traffic incurs significant costs at scale.                                                                                                 |
|   3 | Initial service discovery used DNS-based "Nameless," providing flat IP lists without zone awareness.                                                  |
|   4 | Custom load balancer ELS (Expected Latency Selector) was blind to zones due to similar latencies.                                                     |
|   5 | Introducing zone data via ORCA allowed ELS to apply a synthetic penalty to cross-zone traffic, reducing cross-zone traffic from 70% to 40%.           |
|   6 | Local optimizations risked overloading zones; a global solution was needed.                                                                           |
|   7 | Adopted XDS control plane (originally for Envoy proxies), enabling typed resource discovery and weighted, locality-based routing.                     |
|   8 | Implemented two-level routing: control plane selects zone, ELS selects endpoint.                                                                      |
|   9 | Used Envoy’s “fill local and spill the rest” heuristic to maximize same-zone traffic without overloading zones.                                       |
|  10 | Heuristic assumes server capacity and client traffic are evenly distributed by host count, which often isn’t true in complex networks.                |
|  11 | XDS load reports enabled measurement of actual traffic distribution, removing the need for assumptions about client distribution.                     |
|  12 | System architecture includes Shameless (XDS control plane) and Zonus (global aggregator for zonal load reports).                                      |
|  13 | Key optimizations: hash-based suppression of duplicate responses, cancellation of outdated tasks, and staleness guards to fail open if data is stale. |
|  14 | Achieved a 75% reduction in cross-zone traffic overall; some high-volume services saw 82% cost reduction.                                             |
|  15 | Incident: uneven server distribution and slow-starting pods led to overloads due to static capacity assumptions.                                      |
|  16 | Developed a dynamic capacity model using queue-adjusted host counts and distrust of new hosts, adjusting traffic based on real-time signals.          |
|  17 | Dynamic model reduced errors by 91% in degraded scenarios and improved reliability during scaling and deployments.                                    |
|  18 | The improved algorithm is now widely deployed at Spotify, providing ro                                                                                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=oFdW1yAoaHc)