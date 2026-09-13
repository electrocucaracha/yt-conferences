---
type: Video Note
title: "Fluent Bit V5: Pushing the Limits of Observability at Scale - Eduardo Silva"
description: "Eduardo presents the latest advancements in the Fluent Bit project, emphasizing its evolution as a high-performance, vendor-neutral telemetry pipeline for collecting, processing, and routing observability data. He explains the core architec..."
resource: https://www.youtube.com/watch?v=w1pj0Lz1mW4
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Eduardo presents the latest advancements in the Fluent Bit project, emphasizing its evolution as a high-performance, vendor-neutral telemetry pipeline for collecting, processing, and routing observability data.
He explains the core architecture—inputs, processors, routing, and outputs—and highlights new features in version 5, such as enhanced OpenTelemetry integration, multi-threaded input plugins, improved buffering and storage, conditional processing and routing, and the ability to route internal logs through the pipeline.
The project maintains backward compatibility with filters and focuses on performance optimizations, security enhancements like OAuth2 and JWT validation, and broad platform support.
Eduardo addresses community questions on integration, performance benchmarking, configuration flexibility, and project maintenance, encouraging users to choose solutions that best fit their environments while reaffirming Fluent Bit’s commitment to extensibility, efficiency, and community-driven development.
# Main Points

|   # | Main point                                                                                                                                                                    |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation focuses on pushing the limits of the Fluent Bit project.                                                                                                         |
|   2 | Telemetry data is everywhere, requiring centralized data analysis.                                                                                                            |
|   3 | Fluent Bit acts as a telemetry pipeline: inputs (data collection), processors (data modification/enrichment), routing, and outputs (connectors to backends).                  |
|   4 | Inputs include log files, syslog, OpenTelemetry, Prometheus scraping, Kubernetes events, and systemd logs.                                                                    |
|   5 | Processors support Lua scripting, Kubernetes metadata enrichment, sampling, and over 100 plugins.                                                                             |
|   6 | Outputs connect to various endpoints (OpenTelemetry, Splunk, etc.).                                                                                                           |
|   7 | Fluent Bit has a pluggable architecture, allowing extension with custom plugins.                                                                                              |
|   8 | Major contributors include Splunk, Amazon, and Microsoft.                                                                                                                     |
|   9 | Features: high concurrency, safe buffering (including file system storage), extensibility (Lua, Go, Zig SDK), and broad deployment options (Kubernetes, edge, VMs, gateways). |
|  10 | Core principles: high performance, low CPU/memory, vendor neutrality, broad ecosystem support.                                                                                |
|  11 | Fluent Bit v5 evolves into a data plane for observability, supporting more processing and aggregation.                                                                        |
|  12 | Strong integration with OpenTelemetry: supports OTLP protocol, logs, metrics, traces, and profiling (alpha).                                                                  |
|  13 | Security updates: new OIDC implementation, JWT validation with caching, and improved authorization.                                                                           |
|  14 | New processors: cumulative-to-delta, topological data analysis, enhanced metric processing.                                                                                   |
|  15 | YAML configuration and native processors offer faster, more granular data processing and conditional routing.                                                                 |
|  16 | Multi-threaded HTTP server and input plugins (Splunk, Elastic, OT, Prometheus) for higher throughput.                                                                         |
|  17 | Internal logs and metrics can now be routed through the pipeline.                                                                                                             |
|  18 | Performance optimizations: SIMD, faster trace sampling, reduced memory/CPU usage.                                                                                             |
|  19 | Fluent Bit v5 outperforms v4.2 and OT collector in throughput and efficiency.                                                                                                 |
|  20 | Backward compatibility for filters; filters can be attached as processors.                                                                                                    |
|  21 | Vendor-neutral approach; integrates with OpenTelemetry Collector b                                                                                                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=w1pj0Lz1mW4)