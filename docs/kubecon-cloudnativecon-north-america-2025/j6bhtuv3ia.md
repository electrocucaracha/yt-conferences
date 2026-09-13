---
type: Video Note
title: "OpenTelemetry Logs Driving a Major Shift: Events, Richer Data, and Smarter Semantics - Robert Pająk"
description: "Robert Pyong’s talk focuses on the evolving role of logs in OpenTelemetry, emphasizing their transition from legacy baggage to first-class citizens within the observability ecosystem. He explains that OpenTelemetry logs are structured entit..."
resource: https://www.youtube.com/watch?v=-j6bHtUV3IA
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Robert Pyong’s talk focuses on the evolving role of logs in OpenTelemetry, emphasizing their transition from legacy baggage to first-class citizens within the observability ecosystem.
He explains that OpenTelemetry logs are structured entities, not just strings, containing timestamps, trace context, severities, bodies, attributes, resources, and instrumentation scopes, allowing for rich context and correlation with other signals like traces and metrics.
Pyong highlights the importance of semantic conventions, which provide guidelines for consistent log attributes and enable meaningful cross-service analysis, distinguishing between general log records and well-defined event records.
He introduces the new user-facing OpenTelemetry logging API, which allows developers to emit structured logs directly, bypassing traditional logging libraries and enabling better integration and performance, including the ability to leverage efficient OS-native tracing systems.
The Q&A addresses practical concerns such as batching Windows event logs, the maturity of SDKs across languages, best practices for logging in Kubernetes, and support for syslog, with Pyong noting that while legacy approaches will persist, the adoption of OpenTelemetry’s structured logging and semantics is expected to grow over time.
# Main Points

|   # | Main point                                                                                                                                            |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation by Robert Pyong on open logs in OpenTelemetry, focusing on logs as first-class citizens.                                                 |
|   2 | Robert is an OpenTelemetry Go maintainer, works at Splunk, and contributes mainly to open source.                                                     |
|   3 | OpenTelemetry is an open standard for generating telemetry data: traces, metrics, logs, and profiles (coming soon).                                   |
|   4 | The talk focuses on the present and future of logs in OpenTelemetry.                                                                                  |
|   5 | OpenTelemetry logs are structured data, not just strings or JSON; they include:                                                                       |
|   6 | Two timestamps (event time and capture time)                                                                                                          |
|   7 | Trace context for correlation                                                                                                                         |
|   8 | Severity (text and numeric level)                                                                                                                     |
|   9 | Body (e.g., message)                                                                                                                                  |
|  10 | Attributes (metadata)                                                                                                                                 |
|  11 | Resource (identifies emitting software)                                                                                                               |
|  12 | Instrumentation scope (e.g., logger name, module)                                                                                                     |
|  13 | Log attributes and bodies can be complex (arrays, maps, blobs, etc.).                                                                                 |
|  14 | Complex values are being introduced to all OpenTelemetry signals (logs, spans, metrics).                                                              |
|  15 | OpenTelemetry emphasizes semantics: common patterns and conventions for attributes, log levels, and data modeling.                                    |
|  16 | Semantic conventions are organized into groups: cross-cutting, signal-specific, and domain-specific attributes.                                       |
|  17 | Distinction between logs and events:                                                                                                                  |
|  18 | Log record: general-purpose, human-readable                                                                                                           |
|  19 | Event record: well-defined, follows semantic conventions, intentional, and meaningful                                                                 |
|  20 | Some advocate for "white events"—logs containing all information to derive traces and metrics, but this has tradeoffs (storage, processing, network). |
|  21 | Historically, OpenTelemetry logs bridged existing logging libraries; now, direct OpenTelemetry logging APIs are being developed.                      |
|  22 | OpenTelemetry logging API allows emitting logs directly, supporting semantics and structured data, and reusing attributes across signals.             |
|  23 | Both legacy logging libraries and OpenTelemetry APIs can be used together.                                                                            |
|  24 | Performance improvements: "enabled API" checks if a log is needed before constructing it, reducing overhead.                                          |
|  25 | Enables integration with OS-native tracing systems (e.g., Linux user ev                                                                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=-j6bHtUV3IA)