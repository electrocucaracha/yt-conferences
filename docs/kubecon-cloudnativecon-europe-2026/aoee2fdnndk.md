---
type: Video Note
title: "OpenTelemetry Logs Driving a Major Shift: Events, Richer Data, and Smarter Semantics - Robert Pająk"
description: "The speaker, Robert Pajonk, introduces updates to logging in OpenTelemetry, emphasizing the need for better logging standards due to the inefficiency and noise of traditional, unstructured logs. He explains that OpenTelemetry now treats log..."
resource: https://www.youtube.com/watch?v=aoEe2FDnnDk
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The speaker, Robert Pajonk, introduces updates to logging in OpenTelemetry, emphasizing the need for better logging standards due to the inefficiency and noise of traditional, unstructured logs.
He explains that OpenTelemetry now treats logs as structured, first-class citizens, supporting complex attributes and enabling better correlation with traces and metrics.
The new logging API allows direct log emission, improved performance through an "enabled" check, and reduces reliance on third-party logging libraries.
A significant change is the planned deprecation of span events in favor of log-based events, with a focus on providing a smooth migration path for users.
Pajonk highlights the importance of following OpenTelemetry's semantic conventions to ensure consistency, interoperability, and richer, more efficient telemetry data across systems.
# Main Points

|   # | Main point                                                                                                                         |
| --: | ---------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presenter: Robert Pajonk, OpenTelemetry Go maintainer, contributor to OpenTelemetry logs since Nov 2023, works at Splunk.          |
|   2 | Many developers encounter unhelpful, noisy logs that impact performance and increase storage costs.                                |
|   3 | Better logging standards are needed; existing systems (kernel tracepoints, BPF, ETW) offer structured, efficient logging.          |
|   4 | OpenTelemetry is a framework for tracing, metrics, logs, profiles, and telemetry.                                                  |
|   5 | OpenTelemetry logs are structured, not just strings or JSON; they include:                                                         |
|   6 | Timestamps (event and observed time)                                                                                               |
|   7 | Trace correlation fields                                                                                                           |
|   8 | Event name                                                                                                                         |
|   9 | Severity number (logging level)                                                                                                    |
|  10 | Human-readable body                                                                                                                |
|  11 | Additional attributes (including complex types like maps and arrays)                                                               |
|  12 | Resource attributes (software emitting the log)                                                                                    |
|  13 | Instrumentation scope (component/unit emitting telemetry)                                                                          |
|  14 | Complex attributes are now supported in all OpenTelemetry signals.                                                                 |
|  15 | Event name distinguishes between legacy logs and logs with system semantics; events should have a well-known, versioned structure. |
|  16 | OpenTelemetry logging now supports direct log emission via APIs, not just bridging from other libraries.                           |
|  17 | Direct API use avoids format conversion, allows attribute reuse, and increases consistency.                                        |
|  18 | Instrumentation library authors and application developers benefit from not relying on third-party logging libraries.              |
|  19 | New "enabled" API allows efficient log emission by checking if a log should be emitted before incurring overhead.                  |
|  20 | Enabled API also added to metrics and tracing APIs.                                                                                |
|  21 | OpenTelemetry is shifting from span events to log-based events:                                                                    |
|  22 | Span events are being deprecated in favor of log events.                                                                           |
|  23 | Log events are richer (support severity, etc.).                                                                                    |
|  24 | Migration guidance and support will be provided; APIs are deprecated, not removed.                                                 |
|  25 | OpenTelemetry semantic conventions provide guidance for naming, structuring, and emitting logs/events.                             |
|  26 | Semantic conventions include registries of cross-cutting, signal-specific, and domain-speci                                        |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=aoEe2FDnnDk)