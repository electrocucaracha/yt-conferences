---
layout: default
title:
  "When OTTL Goes Off the Rails: Debugging Transformations wit... Edmo Vamerlatti
  Costa & Tyler Helmuth"
nav_order: 402
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this session, Tyler Helmouth and Aimo provide an intermediate-level
  overview of debugging the OpenTelemetry Transformation Language (OTTL) with confidence,
  emphasizing the importance of understanding the OpenTelemetry (OTEL) data model
  a...
resource: https://www.youtube.com/watch?v=465RlwgsNHg
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

In this session, Tyler Helmouth and Aimo provide an intermediate-level overview of debugging the OpenTelemetry Transformation Language (OTTL) with confidence, emphasizing the importance of understanding the OpenTelemetry (OTEL) data model and its internal representation, P data, within the collector.
They explain that OTTL operates strictly on P data, not on receiver or exporter payloads, and highlight the significance of using correct data paths as documented, since incorrect paths will cause statements to fail.
The presenters demonstrate three key debugging tools: the debug exporter, which outputs telemetry data for inspection; debug logs, which provide detailed step-by-step audit trails of data transformations; and the OTTL playground, a web-based tool for experimenting with OTTL statements and visualizing changes.
Through several live examples, they illustrate common pitfalls such as case sensitivity in conditions, manipulating shared resources, and the importance of selecting the appropriate context for efficient transformations.
The session concludes with key takeaways: always inspect and understand your data as seen by the collector, leverage the available debugging tools, and experiment safely to ensure reliable OTTL transformations.
Audience questions address topics like integrating OTTL into CI/CD pipelines and the current limitations of debug log granularity within the collector.

# Main Points

|   # | Main point                                                                                                                                                                                          |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Session focuses on debugging OTTL (OpenTelemetry Transformation Language) for users familiar with OpenTelemetry and its collector.                                                                  |
|   2 | Agenda: review OpenTelemetry data models, debugging tools, and live debugging scenarios.                                                                                                            |
|   3 | OpenTelemetry data model is hierarchical: signals (logs, metrics, traces) contain resources, instrumentation scopes, and items (log records, metrics, spans).                                       |
|   4 | Key fields (e.g., log body, metric type, span name) are top-level fields, not attributes.                                                                                                           |
|   5 | Collector transforms all incoming data into its internal "P data" model; OTTL operates only on P data.                                                                                              |
|   6 | OTTL context provides access to relevant data paths and hierarchy for transformation statements.                                                                                                    |
|   7 | All valid OTTL paths are documented online; using undefined paths causes errors.                                                                                                                    |
|   8 | Three main debugging tools: debug exporter (prints telemetry data to console), debug logs (provides step-by-step audit trail), and OTTL playground (web UI for experimenting with transformations). |
|   9 | Debug exporter shows final data after pipeline processing; useful for inspecting field names, paths, and values.                                                                                    |
|  10 | Debug logs show before/after snapshots for each statement and data item, indicating condition matches and changes.                                                                                  |
|  11 | OTTL playground allows running and visualizing transformations in the browser using real collector code.                                                                                            |
|  12 | Example 1: Case sensitivity in string matching can cause conditions to fail; always check actual data in the collector.                                                                             |
|  13 | Example 2: Parsing JSON in log bodies requires correct cache usage and path referencing.                                                                                                            |
|  14 | Example 3: Promoting log attributes to resource attributes can cause unexpected results due to shared resource data; last value wins or values are appended.                                        |
|  15 | Example 4: Choosing the correct context (e.g., metric vs. data point) improves efficiency and correctness; context inference can optimize execution.                                                |
|  16 | Key takeaways: OTTL works on P data, understand the data model, inspect data before writing statements, use debug tools, and experiment safely.                                                     |
|  17 | OTTL transform processor is a                                                                                                                                                                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=465RlwgsNHg)
