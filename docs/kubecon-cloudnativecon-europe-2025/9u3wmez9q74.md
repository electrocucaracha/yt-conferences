---
type: Video Note
title: "Journey at the New York Times: Is Sidecar-Less Service Mesh Disappearing I... Lin Sun & Ahmed Bebars"
description: "Lynn and Ahmed from the New York Times presented their journey with service mesh, specifically ambient, which they used to improve their platform's infrastructure and scalability. They started by defining workflows for their engineers and r..."
resource: https://www.youtube.com/watch?v=9U3WMez9q74
tags: ["kubecon-cloudnativecon-europe-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Lynn and Ahmed from the New York Times presented their journey with service mesh, specifically ambient, which they used to improve their platform's infrastructure and scalability.
They started by defining workflows for their engineers and routing traffic through a shared Kubernetes cluster.
However, they realized that this approach had limitations, such as requiring manual retries, timeouts, and custom logic for routing traffic between services.
To address these issues, they adopted ambient, which introduced the concept of a zero-trust tunnel (Z-tunnel) that provides fine-grained routing, canary deployments, and layer 7 security policies.
The Z-tunnel is a node agent running on each Kubernetes node that serves all paths in ambient, providing identity for pods through spiffy and mutual TLS encryption.
Ambient also introduced the concept of waypoints, which are layer 7 proxies that control traffic into namespaces or egress to external services.
The team tested ambient with a multicluster setup, but encountered issues with CPU utilization and certificate rotation.
Despite these challenges, they were able to resolve them through benchmarking and debugging.
The presentation concluded with a live demo of ambient, showcasing its capabilities in routing traffic between services and controlling policies for external services.
# Main Points

|   # | Main point |
| --: | ---------- |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=9U3WMez9q74)