---
type: Video Note
title: "Cloud Native Theater | EnvoyCon: Zone Aware Routing With Per-Locality Load Awareness- Isaac Wilson"
description: "Isaac from The Trade Desk discusses challenges and solutions related to zone-aware routing within Envoy in their on-premise data centers, where workloads are distributed across multiple racks and zones using Kubernetes and Envoy Gateway. He..."
resource: https://www.youtube.com/watch?v=ZTacKbmGfMI
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Isaac from The Trade Desk discusses challenges and solutions related to zone-aware routing within Envoy in their on-premise data centers, where workloads are distributed across multiple racks and zones using Kubernetes and Envoy Gateway.
He explains that while Envoy’s zone-aware routing generally works well by preferring local traffic for efficiency and reduced latency, issues arise when traffic is unevenly distributed across zones, leading to overloaded backends in certain areas.
To address this, Isaac explores using dynamic modules and a central load reporting service (LRS) to aggregate load data and enable real-time, client-side weighted round robin routing that accounts for actual load per zone.
He also describes ongoing work to add locality-aware picking policies within Envoy, allowing for more balanced request distribution without sacrificing local preference.
Isaac highlights the benefits of dynamic modules for extending Envoy without custom builds, shares experiences with Orca metrics and probe traffic for better load awareness, and answers audience questions about migration from HAProxy, dynamic module implementation, and comparisons to similar solutions like Spotify’s proxyless approach.
# Main Points

|   # | Main point                                                                                                                                                       |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Isaac from The Trade Desk discussed zone aware routing within Envoy and related challenges in their environment.                                                 |
|   2 | Their architecture runs on-premise data centers with 100-200 racks per center, each rack containing multiple nodes running Kubernetes.                           |
|   3 | Envoy Gateway is used for traffic routing; Isaac is also an Envoy Gateway maintainer.                                                                            |
|   4 | They use least request routing and enable zone aware routing, scheduling workloads roughly equally per rack.                                                     |
|   5 | Envoy routes 100% of traffic locally per rack, based on the number of Envoy pods and upstream hosts per zone.                                                    |
|   6 | Issues arise when incoming traffic is unevenly distributed across zones, leading to overloaded backends in some zones.                                           |
|   7 | BGP anycast is used so every Envoy node advertises the same IP, aiming for equal network flows per host, but this is not guaranteed.                             |
|   8 | Poor load distribution can occur if one zone receives more traffic, as Envoy lacks awareness of other zones' loads.                                              |
|   9 | The goal is to achieve true load awareness per zone without sacrificing local preference for efficiency and reduced latency.                                     |
|  10 | Dynamic modules and a central load service using LRS (Load Reporting Service) can aggregate load data and inform routing decisions.                              |
|  11 | Isaac implemented a client-side weighted round robin policy using dynamic modules, adjusting traffic distribution in real time based on zone load.               |
|  12 | Orca metrics can be used for load reporting, but not all users may support it.                                                                                   |
|  13 | Another approach is adding a locality-level picking policy in Envoy to consider load per locality using Orca metrics.                                            |
|  14 | A challenge with in-band reporting is lack of data from zones not receiving traffic; Isaac's solution is to send a small percentage of probe traffic cross-zone. |
|  15 | Out-of-band reporting is a desired future feature to avoid unnecessary probe traffic.                                                                            |
|  16 | Dynamic modules are powerful, allowing custom business logic without maintaining custom Envoy binaries.                                                          |
|  17 | Migration from HAProxy to Envoy was motivated by the desire for Kubernetes-native load balanc                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=ZTacKbmGfMI)