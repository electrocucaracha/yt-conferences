---
type: Video Note
title: "Hello World, Meet the Spanimals: Observability for Beginners - Tiffany Jernigan & Matthias Haeussler"
description: "In this beginner-friendly talk on observability, Tiffany Jernigan and Matias introduce the core concepts using playful animal analogies to represent the four main observability signals: traces (Tracy), logs (Logy), metrics (Metric), and pro..."
resource: https://www.youtube.com/watch?v=_bLAN_mzxIs
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this beginner-friendly talk on observability, Tiffany Jernigan and Matias introduce the core concepts using playful animal analogies to represent the four main observability signals: traces (Tracy), logs (Logy), metrics (Metric), and profiling (Flamy), along with Collie, the collector.
They demonstrate a demo application composed of distributed components that generate and process animal facts and images, showing how each component emits different telemetry data.
The presenters walk through how these signals are collected, correlated, and visualized using the OpenTelemetry collector and Grafana stack, highlighting the importance of being able to trace requests, view logs, analyze metrics, and profile performance to diagnose issues.
They emphasize the flexibility of OpenTelemetry in exporting data to various backends and the value of dashboards that bring all signals together for comprehensive monitoring.
The session concludes with a live demo, configuration examples, and encouragement for attendees to explore the provided repository and continue learning about observability.
# Main Points

|   # | Main point                                                                                                                                                     |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The talk is an introduction to observability, aimed at beginners.                                                                                              |
|   2 | Presenters: Tiffany Jernigan (Grafana Labs) and Matias (CGI).                                                                                                  |
|   3 | Used animal-themed analogies to explain observability concepts:                                                                                                |
|   4 | Tracy: traces (end-to-end journey)                                                                                                                             |
|   5 | Spannies: spans (smaller steps within traces)                                                                                                                  |
|   6 | Logy: logs (chatty, various formats, need filtering)                                                                                                           |
|   7 | Metric: metrics (numbers, gauges, trends, rates)                                                                                                               |
|   8 | Flamy: profiling (flame graphs, detailed performance insights)                                                                                                 |
|   9 | Collie: collector (collects and groups signals)                                                                                                                |
|  10 | Observability signals covered: traces, logs, metrics, profiling.                                                                                               |
|  11 | Demo application built with multiple components (fact generator, image generator, image database, runner) to illustrate observability in a distributed system. |
|  12 | Application uses OpenAI for generating facts and images, stores data in Postgres, and is built with both Python and Java.                                      |
|  13 | OpenTelemetry Collector (Collie) collects and exports telemetry data to various backends (Prometheus, Tempo, Loki, Pyroscope).                                 |
|  14 | Grafana is used for visualization; supports dashboards for traces, metrics, logs, and profiles.                                                                |
|  15 | Demonstrated how traces show end-to-end requests, with spans representing individual operations.                                                               |
|  16 | Logs can be correlated with traces for easier debugging.                                                                                                       |
|  17 | Metrics provide statistical data (e.g., CPU, memory, database metrics).                                                                                        |
|  18 | Profiling (flame graphs) helps identify performance bottlenecks (e.g., CPU/memory usage).                                                                      |
|  19 | OpenTelemetry is open source and vendor-neutral; collectors can be configured to export to different backends.                                                 |
|  20 | Emphasized the importance of correlating signals for effective troubleshooting.                                                                                |
|  21 | Provided a GitHub repo for the demo application and configurations.                                                                                            |
|  22 | Encouraged audience to explore dashboards and automation features in Grafana.                                                                                  |
|  23 | Q&A and further resources offered at the end.                                                                                                                  |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=_bLAN_mzxIs)