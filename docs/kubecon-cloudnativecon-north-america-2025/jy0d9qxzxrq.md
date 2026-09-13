---
layout: default
title:
  Debugging Your Cluster When It’s on Fire - Nikola Grcevski, Grafana Labs &
  Tyler Yahn, Splunk
nav_order: 55
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  In this presentation, Tyler Yan from Splunk and Mario Matias from Grafana
  Labs introduce OBI, an open source project that brings eBPF-based automatic instrumentation
  to OpenTelemetry for observability in production systems. They discuss the...
resource: https://www.youtube.com/watch?v=Jy0d9QXZXrQ
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

In this presentation, Tyler Yan from Splunk and Mario Matias from Grafana Labs introduce OBI, an open source project that brings eBPF-based automatic instrumentation to OpenTelemetry for observability in production systems.
They discuss the challenges of debugging complex, unfamiliar clusters during incidents, emphasizing the limitations of traditional observability approaches that require code changes, redeployments, and restarts—actions that are risky and time-consuming during outages.
OBI leverages eBPF technology to provide immediate, cluster-wide visibility without code modifications or service restarts, enabling rapid root cause analysis across multiple languages and services.
Through a live demo, they show how deploying OBI in under 30 seconds surfaces distributed traces and service topologies, allowing engineers to quickly identify and resolve issues—such as distinguishing between misleading database errors and actual rate-limiting problems—thereby reducing mean time to resolution from days to minutes.
The session concludes with practical details on OBI’s compatibility, supported protocols, and integration with open source observability stacks, as well as a Q&A addressing deployment scenarios and interoperability with other OpenTelemetry tools.

# Main Points

|   # | Main point                                                                                                                                                                                    |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation on debugging clusters during incidents, focusing on observability.                                                                                                               |
|   2 | Presenters: Tyler Yan (Splunk, OpenTelemetry maintainer) and Mario Matias (Grafana Labs, OpenTelemetry eBPF contributor).                                                                     |
|   3 | Traditional observability requires code changes, redeployments, and restarts, which are risky and slow during incidents.                                                                      |
|   4 | Limited visibility and lack of instrumentation increase stress and slow down root cause analysis.                                                                                             |
|   5 | OpenTelemetry provides vendor-agnostic APIs and SDKs but often still needs code changes for many languages.                                                                                   |
|   6 | eBPF (extended Berkeley Packet Filter) enables kernel-level, high-performance, language-agnostic instrumentation without code changes or restarts.                                            |
|   7 | OBI (OpenTelemetry eBPF Instrumentation) is a new open source project that auto-discovers services, generates distributed traces, and provides service topology maps with zero configuration. |
|   8 | OBI deploys quickly (under 30 seconds), requires no code changes, and works cluster-wide.                                                                                                     |
|   9 | Demo: OBI deployed via Helm in a Kubernetes cluster with multiple microservices; immediately provided visibility into service errors and latency.                                             |
|  10 | OBI identified the real root cause (rate limiting on an external API) rather than misleading database errors.                                                                                 |
|  11 | OBI supports HTTP, REST, gRPC, databases (Postgres, MySQL, MongoDB, Redis), and message queues (Kafka); more protocols being added.                                                           |
|  12 | OBI does not support custom spans but can coexist with manual OpenTelemetry SDK instrumentation.                                                                                              |
|  13 | Requirements: Linux kernel 5.8+ (or Red Hat/CentOS 8 with backports), 64-bit Intel/ARM, major cloud providers supported.                                                                      |
|  14 | OBI runs as a DaemonSet on each node; works on Kubernetes and non-Kubernetes infrastructure.                                                                                                  |
|  15 | Can trace across clusters if trace context is preserved and not stripped by intermediaries.                                                                                                   |
|  16 | Grafana Tempo and LGTM stack used for visualization; dashboards are part of open source offerings.                                                                                            |
|  17 | Community encouraged to try OBI, contribute, and join SIG meetings for support and development.                                                                                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Jy0d9QXZXrQ)
