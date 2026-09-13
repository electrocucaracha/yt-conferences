---
layout: default
title:
  "Redesigning Ingress: Docker’s Transition To the Next-Gen Gate... Kateryna
  Nezdolii & Ryan Hristovski"
nav_order: 281
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  Katina Onesik and Ryan, an infrastructure engineer at Docker, presented
  their migration journey from a legacy standalone Harroxy and EngineX stack to a
  modern Envoy Gateway solution. They simplified their ingress system by consolidating
  mul...
resource: https://www.youtube.com/watch?v=Ea5OuNjpi9M
tags:
  - kubecon-cloudnativecon-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Katina Onesik and Ryan, an infrastructure engineer at Docker, presented their migration journey from a legacy standalone Harroxy and EngineX stack to a modern Envoy Gateway solution.
They simplified their ingress system by consolidating multiple proxy technologies into a single Envoy Proxy stack, reducing technology fragmentation and improving user experience with a Kubernetes-native unified routing API.
The new system improved request latency, throughput, and observability, while offering fine-grained control over traffic routing and canary deployments.
Despite challenges such as a learning curve and limitations in the Envoy Gateway documentation, they contributed to the community by discovering bugs and implementing features like global rate limiting and configurable panic thresholds.
They are now planning to work on zone-aware routing, deprecating EngineX, and joining the Envoy Gateway steering committee to increase their involvement with the project.

# Main Points

|   # | Main point |
| --: | ---------- |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Ea5OuNjpi9M)
