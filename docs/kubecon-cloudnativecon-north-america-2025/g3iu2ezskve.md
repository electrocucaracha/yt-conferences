---
layout: default
title:
  "Project Lightning Talk: 5 Key Lessons From 8 Years of Building Kgateway -
  Yuval Kohavi"
nav_order: 204
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  Yuval Kohave, chief architect at Solo.io and K Gateway maintainer, shares
  five key lessons from eight years of developing K Gateway, an API gateway designed
  for diverse workloads including AI and microservices. First, he emphasizes that
  ope...
resource: https://www.youtube.com/watch?v=G3Iu2ezSkVE
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

Yuval Kohave, chief architect at Solo.io and K Gateway maintainer, shares five key lessons from eight years of developing K Gateway, an API gateway designed for diverse workloads including AI and microservices.
First, he emphasizes that open governance, specifically donating the project to the CNCF, significantly accelerated community engagement and growth, and he regrets not doing it sooner.
Second, he advises focusing on core use cases rather than trying to support every edge scenario, as excessive features can harm performance, overwhelm users, and increase maintenance burdens.
Third, Kohave highlights the importance of scalable and maintainable extensibility, favoring in-process approaches over gRPC webhooks and leveraging standard Envoy interfaces for custom use cases.
Fourth, he notes that attempting to tightly integrate with sibling projects like service meshes introduced friction, so making K Gateway composable allowed users to adopt it without unnecessary dependencies.
Finally, he stresses the need to define scalability goals early, rigorously test against them, and clearly communicate expectations to users, as real-world use cases often reveal unforeseen bottlenecks.

# Main Points

|   # | Main point                                                                                                                                              |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Yuval Kohave is the chief architect at Solo.io and K Gateway maintainer.                                                                                |
|   2 | K Gateway is an API gateway based on the new ingress API, routing traffic into clusters and workloads.                                                  |
|   3 | Supports AI workloads, regular workloads, microservices, lambda functions, multiple data planes, Envoy proxy, and a new agent gateway for AI workloads. |
|   4 | Lesson 1: Open governance accelerated growth.                                                                                                           |
|   5 | Initially hesitant to donate K Gateway to a foundation due to fear of losing control.                                                                   |
|   6 | After donating to CNCF, saw immediate improvement in engagement across channels (GitHub, Slack).                                                        |
|   7 | Regret not donating sooner.                                                                                                                             |
|   8 | Lesson 2: Focus on the core.                                                                                                                            |
|   9 | Initially tried to support many edge use cases (Kubernetes, Nomad, console, file, VM, NAT).                                                             |
|  10 | Adding many features led to performance issues, user confusion, and increased maintenance burden.                                                       |
|  11 | New philosophy: focus on the 80% of users and say no to niche features.                                                                                 |
|  12 | Lesson 3: Extensibility.                                                                                                                                |
|  13 | Many users require tweaks to standard features.                                                                                                         |
|  14 | Approach is to keep extensibility scalable and maintainable.                                                                                            |
|  15 | Uses in-process extensibility, avoids gRPC webhooks.                                                                                                    |
|  16 | Data plane uses standard Envoy interfaces (xDS, xAuth) for custom use cases.                                                                            |
|  17 | Lesson 4: Composability.                                                                                                                                |
|  18 | Attempted to build on top of a sibling service mesh project (io), but it introduced friction.                                                           |
|  19 | Ingress use cases are more diverse; users did not want a service mesh just for ingress.                                                                 |
|  20 | Solution: make K Gateway composable and pluggable as a waypoint to io.                                                                                  |
|  21 | Lesson 5: Scalability.                                                                                                                                  |
|  22 | Previous version (Glue Edge) scaled up to a point; version 2 and agent gateway improved scalability.                                                    |
|  23 | Scaling involves handling user config and requires significant engineering.                                                                             |
|  24 | Bottlenecks often only appear with real user use cases.                                                                                                 |
|  25 | Advice: define scale goals early, test against them, and set clear expectations with users.                                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=G3Iu2ezSkVE)
