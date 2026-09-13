---
type: Video Note
title: "Jaeger V2: The Maintainers' Guide To OpenTelemetry-Native Tracing - Pavol Loffay, Red Hat"
description: "In this session, Pavle, a maintainer of the Jaeger project, introduces the fundamentals of distributed tracing and observability, focusing on Jaeger and its current version, Jaeger V2. He explains that distributed tracing is essential for u..."
resource: https://www.youtube.com/watch?v=gH_JzIXFshI
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this session, Pavle, a maintainer of the Jaeger project, introduces the fundamentals of distributed tracing and observability, focusing on Jaeger and its current version, Jaeger V2.
He explains that distributed tracing is essential for understanding complex systems, enabling root cause analysis, and improving monitoring and alerting, especially in microservice architectures.
The talk covers Jaeger's architecture, its reliance on OpenTelemetry for instrumentation, and its data model based on traces and spans, highlighting features such as error detection, service diagrams, and advanced visualizations like flame graphs and trace diffs.
Pavle demonstrates Jaeger's UI with a live demo, discusses integration with Prometheus for metrics, and outlines new features in Jaeger V2, including improved storage options, the MCP server for efficient trace querying, and UI enhancements like dark mode and incomplete trace detection.
The session concludes with a discussion of the roadmap, including plans for AI-assisted trace analysis and support for GenAI workloads, and addresses audience questions on data retention, dashboard customization, and modeling complex trace scenarios.
# Main Points

|   # | Main point                                                                                                                                                                                                                        |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Introduction to Jagger project session by Pavle, a Jagger maintainer.                                                                                                                                                             |
|   2 | Session covers observability, distributed tracing, Jagger V2, live demo, Jagger with Prometheus, Jagger MCP, new features, and roadmap.                                                                                           |
|   3 | Jagger is a CNCF graduated project, released about 10 years ago.                                                                                                                                                                  |
|   4 | Distributed tracing helps understand complex systems, pinpoint errors, and perform root cause analysis.                                                                                                                           |
|   5 | Tracing provides a full request lifespan, constructs service diagrams, and helps plan updates.                                                                                                                                    |
|   6 | Tracing is essential for root cause analysis and setting up SLAs in microservice architectures.                                                                                                                                   |
|   7 | Tracing tools use a three-layer architecture: instrumentation (tracer API), collector, and storage/visualization.                                                                                                                 |
|   8 | Jagger handles data collection, storage, and visualization; recommends using OpenTelemetry SDKs for instrumentation.                                                                                                              |
|   9 | Jagger natively supports OTLP ingestion.                                                                                                                                                                                          |
|  10 | Tracing data model: trace (end-to-end invocation), spans (individual operations), and tags (attributes).                                                                                                                          |
|  11 | Tracing differs from logging by providing duration, structure, and correlation between spans.                                                                                                                                     |
|  12 | Demo app simulates Uber-like microservices; Jagger UI visualizes traces, service architecture, and operation timings.                                                                                                             |
|  13 | Jagger UI features: timeline view, flame graph, trace graph, trace statistics, trace diff, and dark mode.                                                                                                                         |
|  14 | Integration with Prometheus enables extracting metrics (latency, error rate, request rate) from spans.                                                                                                                            |
|  15 | Jagger V2 is based on OpenTelemetry Collector; all functionality implemented as collector components.                                                                                                                             |
|  16 | Single binary for Jagger V2; configuration aligned with OpenTelemetry Collector YAML.                                                                                                                                             |
|  17 | Storage extension allows configuring different databases for main and archive storage.                                                                                                                                            |
|  18 | New features: Jagger MCP server (progressive disclosure for efficient trace querying), ClickHouse support, improved database support, Helm chart, live demo updates, dark mode, OpenTelemetry naming, incomplete trace detection. |
|  19 | Roadmap: AI assistant in UI, observability for GenAI workloads, collaboration encouraged via GitH                                                                                                                                 |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=gH_JzIXFshI)