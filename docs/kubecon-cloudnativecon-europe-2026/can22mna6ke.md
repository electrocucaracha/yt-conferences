---
layout: default
title:
  "Cloud Native Theater | EnvoyCon: Inside Spotify’s Envoy Architecture: What
  We Le... Leonardo da Mata"
nav_order: 59
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Leonardo Damata, an engineer at Spotify, shared insights from migrating
  Spotify’s production architecture to use Envoy Proxy more efficiently. Historically,
  Spotify routed every request through a custom Envoy proxy and a Java sidecar for
  re...
resource: https://www.youtube.com/watch?v=CAn22mnA6kE
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

Leonardo Damata, an engineer at Spotify, shared insights from migrating Spotify’s production architecture to use Envoy Proxy more efficiently.
Historically, Spotify routed every request through a custom Envoy proxy and a Java sidecar for request decoration, which caused significant latency and limited throughput to 500 requests per second per CPU core—far below the community benchmark of 10,000.
To address this, the team migrated features from the Java sidecar into Envoy filters, aiming to align more closely with open-source practices and improve performance.
The migration involved careful side-by-side comparisons, iterative rollouts, and multiple reversions due to unexpected issues, such as a major incident caused by filter order changes.
Ultimately, the changes increased throughput to 4,500 requests per second per core, simplified the architecture, and fostered greater involvement with the Envoy community, though some bottlenecks remain due to legacy patterns.

# Main Points

|   # | Main point                                                                                                                                                              |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Leonardo Damata, engineer at Spotify, shared learnings from using Envoy in production.                                                                                  |
|   2 | Spotify handles 11 million requests per second, using a custom version of Envoy as the front door.                                                                      |
|   3 | Previously, a Java sidecar process (X out Z) was used to decorate requests, adding authentication and metadata, increasing latency.                                     |
|   4 | Spotify aimed to standardize architecture, move closer to open source Envoy, and reduce reliance on the Java sidecar.                                                   |
|   5 | Initial performance was 500 requests per second per CPU, far below the community benchmark of 10,000.                                                                   |
|   6 | Migrated Java sidecar features into Envoy filters; ported features to open source where possible.                                                                       |
|   7 | Migration plan involved enabling/disabling features regionally, using canaries, and side-by-side comparisons of old and new paths.                                      |
|   8 | Compared metrics by duplicating requests and counting header differences to validate changes.                                                                           |
|   9 | Faced multiple rollbacks due to unexpected API usage and non-standard practices by internal teams.                                                                      |
|  10 | Encountered issues with token prefetching; resolved by using Kubernetes init containers instead of implementing fully in filters.                                       |
|  11 | Major incident occurred due to filter order change, causing a bug in rate limiting filter, leading to Envoy crashes and out-of-memory errors.                           |
|  12 | Lessons learned: filter order matters, C++ lacks Java garbage collection, use Envoy’s threading model, simplify image building, and stick close to community standards. |
|  13 | Achieved performance improvement from 500 to 2,000, then 4,500 requests per second per core after migration.                                                            |
|  14 | Remaining bottleneck attributed to previous Java process and external calls; filters improved architecture utilization.                                                 |
|  15 | Sidecar was removed; logic moved into Envoy process, written in C++ due to language support at the time.                                                                |
|  16 | Envoy is used not only at the perimeter but also for service discovery and complex features inside Spotify’s infrastructure.                                            |
|  17 | Side-by-side comparison and formalizing undocumented decisions were key to successful migration.                                                                        |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=CAn22mnA6kE)
