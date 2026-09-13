---
layout: default
title:
  "Prometheus V3 One Year In: OpenMetrics 2.0 and More! - Jan Fajerski & Bartłomiej
  Płotka"
nav_order: 302
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The presentation provides an overview of recent developments and future
  directions for Prometheus since version 3, highlighting major updates, experimental
  features, and community initiatives. Key technical advancements include the stabiliz...
resource: https://www.youtube.com/watch?v=6vE9b6StC0g
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

The presentation provides an overview of recent developments and future directions for Prometheus since version 3, highlighting major updates, experimental features, and community initiatives.
Key technical advancements include the stabilization of native histograms, improvements to OTLP ingestion, experimental PromQL extensions (such as outer joins and new keywords), and the introduction of start timestamps and enhanced storage formats like XOR 2.
The team is also working on native support for delta metrics, exploring Parquet-based storage for better scalability, and developing composite sample storage to streamline histograms and improve efficiency.
Community updates cover the adoption of new governance to encourage contributions, increased activity following the V3 release, and efforts to responsibly manage AI-generated contributions.
The session concludes with a call for user feedback, ongoing work on metric schematization, and an invitation to participate in proposal discussions, emphasizing the project's commitment to continuous improvement and community engagement.

# Main Points

|   # | Main point                                                                                                                                                           |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation covers Prometheus updates since V3 and future plans                                                                                                     |
|   2 | Yan and Bartek introduced themselves and their roles in Prometheus and Google                                                                                        |
|   3 | Agenda: recap, recent changes, upcoming features, community updates, requests for feedback                                                                           |
|   4 | Prometheus overview: TSDB core, service discovery, PromQL query interface, rules/alerts, dashboards                                                                  |
|   5 | Prometheus V3: first major release in 7 years, many new features, new UIs, breaking changes, migration guide available                                               |
|   6 | Native histograms are now stable; since 3.9, require scrape-level configuration; exporters (e.g., Kubernetes) need to support them                                   |
|   7 | OTLP endpoint improvements: initial delta ingestion support, direct TSDB ingestion (up to 25% faster), resource attributes can be promoted to metric labels          |
|   8 | PromQL experimental extensions: info function, improved outer joins, timestamp access, duration arithmetic, type/unit labels, new keywords "smoothed" and "anchored" |
|   9 | Ongoing optimizations and fixes for performance and efficiency                                                                                                       |
|  10 | Start timestamp: native storage implementation in 3.11, improves rate accuracy, supports delta metrics, requires SD storage flag                                     |
|  11 | XOR2 compression format: improved encoding, better support for staleness/jitter, faster reads/writes, available for testing (not production)                         |
|  12 | Native delta metric support coming, enabled by start timestamp storage                                                                                               |
|  13 | Parquet storage: prototypes exist, benefits for high cardinality and scalability, ongoing work in Thanos and related projects                                        |
|  14 | Metadata storage improvements: better resource attribute integration, type/unit support, scrape interval tracking                                                    |
|  15 | Composite sample storage: native histograms with custom buckets, easier migration from classic histograms, PromQL HCBS classic feature for compatibility             |
|  16 | OpenMetrics 2.0: supports composite samples, more efficient, release candidate coming soon                                                                           |
|  17 | Upcoming: optional metric schematization, experimental PromQL syntax with variables/pipes, stochastic reliability models                                             |
|  18 | Community: new governance to ease contributor onbo                                                                                                                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=6vE9b6StC0g)
