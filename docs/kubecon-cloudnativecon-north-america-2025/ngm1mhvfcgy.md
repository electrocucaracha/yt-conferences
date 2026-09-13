---
type: Video Note
title: "Zero-Downtime Telemetry: Hot Reloading OpenTelemetry Collector Pipel... Amir Jakoby & Shiran Melamed"
description: "The speakers discuss the challenges of managing telemetry data, such as logs, metrics, and traces, at massive scale without data loss or downtime, drawing parallels to navigating crowds in a train station. They highlight incidents where con..."
resource: https://www.youtube.com/watch?v=ngm1mHVfcgY
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The speakers discuss the challenges of managing telemetry data, such as logs, metrics, and traces, at massive scale without data loss or downtime, drawing parallels to navigating crowds in a train station.
They highlight incidents where configuration changes caused widespread outages, emphasizing the risks of traditional approaches that require full restarts of systems like the OpenTelemetry Collector.
To address this, they developed a "hot reload processor" that allows targeted, in-place configuration updates within the collector, minimizing data loss and latency by draining and swapping processors without restarting the entire system.
This solution also introduces observability features and rollback capabilities, though it brings new technical and operational challenges, such as configuration validation and monitoring.
The team has open-sourced their processor, inviting community feedback and collaboration to further improve reliability and flexibility in telemetry data management.
# Main Points

|   # | Main point                                                                                                                                                          |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Telemetry data (logs, metrics, traces) must reliably reach their destinations without loss, similar to guiding people in a train station.                           |
|   2 | Data volume can range from megabytes to petabytes daily, requiring robust handling and speed.                                                                       |
|   3 | Configuration changes in telemetry systems can cause major incidents and widespread outages (examples: CrowdStrike, Microsoft OpenAI).                              |
|   4 | OpenTelemetry Collector is part of the CNCF initiative, used for collecting, standardizing, and exporting telemetry data.                                           |
|   5 | The Collector currently requires a full restart to apply configuration changes, causing data loss and visibility gaps during rollout.                               |
|   6 | JFrog, founded in 2008, created Artifactory and now offers a platform addressing security, machine learning, and AI-powered repository queries.                     |
|   7 | Somals offers an AI telemetry management platform to reduce cost, improve reliability, and enhance data quality.                                                    |
|   8 | OpenTelemetry provides vendor-neutral, scalable, efficient, and customizable telemetry with strong data correlation across logs, metrics, and traces.               |
|   9 | The Collector consists of receivers (protocol translation), processors (data transformation/filtering), and exporters (sending data to destinations).               |
|  10 | Pipelines in the Collector define the flow and processing order; multiple pipelines and configurations are possible.                                                |
|  11 | Current configuration reloads cause data loss, latency, and operational fragility.                                                                                  |
|  12 | A new "hot reload processor" was developed to enable targeted, in-place processor updates without full Collector restarts, minimizing data loss.                    |
|  13 | The hot reload processor loads new configurations from S3, validates them, drains old processors, and swaps them seamlessly, supporting rollback and observability. |
|  14 | Technical challenges include configuration validation, encryption/key rotation, S3 cost management, failure handling, and enhanced monitoring.                      |
|  15 | The solution improves reliability, stability, and operational simplicity, allowing selective processor updates and rollback.                                        |
|  16 | The hot rel                                                                                                                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=ngm1mHVfcgY)