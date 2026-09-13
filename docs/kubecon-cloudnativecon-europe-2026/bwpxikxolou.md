---
type: Video Note
title: "Project Lightning Talk: Fluent Bit V5 - Eduardo Silva, Maintainer"
description: "Eduardo Silva introduces himself and the Fluent Bit project, explaining that it is a telemetry pipeline designed to collect, process, and route observability data such as logs, metrics, and traces from various sources to different analysis..."
resource: https://www.youtube.com/watch?v=BwpXIkXOLOU
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Eduardo Silva introduces himself and the Fluent Bit project, explaining that it is a telemetry pipeline designed to collect, process, and route observability data such as logs, metrics, and traces from various sources to different analysis backends.
Fluent Bit operates through a plugin-based architecture, supporting inputs, processors, and outputs, and can run on a wide range of devices and environments.
The project emphasizes high performance, low resource usage, and vendor neutrality, and has been active for ten years.
Eduardo announces the release of Fluent Bit V5, highlighting new features such as updated OpenTelemetry protocol support, a new processor for converting cumulative metrics to delta, improved trace sampling, enhanced HTTP server scalability, and a generic OAuth2 implementation for security.
Performance benchmarks show Fluent Bit V5 outperforms previous versions and other solutions in CPU and memory efficiency, and Eduardo invites attendees to visit the Fluent Bit kiosk and participate in the community.
# Main Points

|   # | Main point                                                                                                                                                          |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Eduardo Silva introduces himself and the Fluent Bit project.                                                                                                        |
|   2 | Fluent Bit is a telemetry pipeline for collecting, processing, and routing data from logs, metrics, and traces.                                                     |
|   3 | Data is collected through "inputs," processed (e.g., deduplication, obfuscation), and routed to various backends like Splunk, Google Stackdriver, or Elasticsearch. |
|   4 | Fluent Bit uses a plugin-based architecture with plugins for inputs, processors, outputs, scripting (Lua), and Kubernetes metadata fetching.                        |
|   5 | Runs on IoT devices, Linux nodes, bare metal machines, or as a gateway for data aggregation.                                                                        |
|   6 | Project principles: high performance, low resource usage, vendor neutrality, broad ecosystem support.                                                               |
|   7 | Fluent Bit has been running for 10 years.                                                                                                                           |
|   8 | Fluent Bit V5 is being released.                                                                                                                                    |
|   9 | Key V5 topics: open telemetry, data processing, platform security, performance.                                                                                     |
|  10 | Updated support for OpenTelemetry protocol v1.10 with alpha profiling support.                                                                                      |
|  11 | Focus on high performance, low CPU/memory overhead, and security.                                                                                                   |
|  12 | New processor for metrics: cumulative to delta conversion.                                                                                                          |
|  13 | New processor for data analytics: topological data analysis.                                                                                                        |
|  14 | Improved trace sampling performance; supports head and tail sampling and processing of all autolog attributes.                                                      |
|  15 | Internal HTTP server rearchitected for better scalability.                                                                                                          |
|  16 | Generic OAuth2 implementation for secure secret sharing across the pipeline.                                                                                        |
|  17 | Performance optimizations reduce cloud deployment costs.                                                                                                            |
|  18 | Benchmark: Fluent Bit V5 outperforms previous versions and OpenTelemetry Collector in CPU and memory usage.                                                         |
|  19 | Invitation to visit the Fluent Bit kiosk, chat with maintainers, get t-shirts, and attend extra presentations.                                                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=BwpXIkXOLOU)