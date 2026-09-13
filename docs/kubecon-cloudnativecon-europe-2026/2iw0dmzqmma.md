---
layout: default
title:
  "Tutorial: Full-Stack Observability on a Budget: A Guide to Strategic Sampling
  and Da... Pavol Loffay"
nav_order: 381
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The tutorial builds on previous sessions about Kubernetes observability,
  focusing this time on achieving full-stack observability on a budget. The presenter
  guides participants through setting up a Kubernetes cluster, deploying observabilit...
resource: https://www.youtube.com/watch?v=2iW0DMZqMMA
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

The tutorial builds on previous sessions about Kubernetes observability, focusing this time on achieving full-stack observability on a budget.
The presenter guides participants through setting up a Kubernetes cluster, deploying observability tools like Jaeger, Prometheus, and the OpenTelemetry operator, and instrumenting a demo microservices application.
Key topics include understanding and configuring head-based and tail-based sampling strategies to manage telemetry data volume and cost, profiling telemetry to identify and filter unnecessary or "malicious" data such as excessive spans, debug logs, and health check traces, and using processors like the count connector and filter processor for optimization.
The session also covers best practices for sampling configuration, memory considerations for tail-based sampling, log deduplication, and emphasizes the importance of addressing issues at the source code or configuration level when possible.
The tutorial concludes with a mention of ongoing work to automate cost optimization in observability workflows using agentic skills.

# Main Points

|   # | Main point                                                                                                                                                                            |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Tutorial continues previous sessions on Kubernetes observability, metrics, and tracing.                                                                                               |
|   2 | Focus is on achieving full stack observability on a budget.                                                                                                                           |
|   3 | Session duration: approximately 1–1.25 hours.                                                                                                                                         |
|   4 | All materials and instructions are available in a repository (QR code/URL provided).                                                                                                  |
|   5 | Agenda includes: introduction, setup, sampling overview, demo app deployment, telemetry data profiling, data optimization, head-based and tail-based sampling, and log deduplication. |
|   6 | Setup steps:                                                                                                                                                                          |
|   7 | Requires a Kubernetes cluster (instructions for kind provided).                                                                                                                       |
|   8 | Deploy observability backend: Jaeger (in-memory), Prometheus, OpenTelemetry Collector.                                                                                                |
|   9 | Install OpenTelemetry Operator and configure instrumentation CR.                                                                                                                      |
|  10 | Clone repository to modify manifest files.                                                                                                                                            |
|  11 | Demo application:                                                                                                                                                                     |
|  12 | Microservices in Node.js, Python, Java, and Go.                                                                                                                                       |
|  13 | Instrumented using OpenTelemetry auto-instrumentation via annotations.                                                                                                                |
|  14 | Telemetry data sent via OTLP to collectors, then to Jaeger and Prometheus.                                                                                                            |
|  15 | Sampling overview:                                                                                                                                                                    |
|  16 | Sampling reduces storage costs, resource usage, and improves troubleshooting.                                                                                                         |
|  17 | Head-based sampling: decision made at request start, propagated downstream, configured in SDKs (probability sampler recommended).                                                     |
|  18 | Tail-based sampling: all data sent to collector, decision made after collecting full trace, more resource-intensive, adds latency.                                                    |
|  19 | Profiling telemetry:                                                                                                                                                                  |
|  20 | Use count connector to measure logs, metrics, and spans per service/namespace.                                                                                                        |
|  21 | Identify noisy services and unnecessary telemetry (e.g., health check spans, debug logs, large log bodies).                                                                           |
|  22 | Data optimization:                                                                                                                                                                    |
|  23 | Use filter processor to drop unwanted logs (debug, large bodies) and health check spans.                                                                                              |
|  24 | Best practice: remove unnecessary telemetry at source code/configuration level.                                                                                                       |
|  25 | Head-based sampling configuration:                                                                                                                                                    |
|  26 | Adjust sampling rate via instrumentation CR and environment variables.                                                                                                                |
|  27 | Jaeger remote sampler allows centralized, per-endpoint sampling (Java/Go support).                                                                                                    |
|  28 | Collector can perform                                                                                                                                                                 |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=2iW0DMZqMMA)
