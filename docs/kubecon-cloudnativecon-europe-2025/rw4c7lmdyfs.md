---
type: Video Note
title: "How To Rename Metrics Without Impacting Somebody’s Observabili... Bartłomiej Płotka & Arianna Vespri"
description: "The video discusses the challenges of renaming metrics in a system, particularly when it affects queries, dashboards, and alerts. The speakers propose a solution using a schema definition that captures metric changes, including name, unit..."
resource: https://www.youtube.com/watch?v=Rw4c7lmdyFs
tags: ["kubecon-cloudnativecon-europe-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The video discusses the challenges of renaming metrics in a system, particularly when it affects queries, dashboards, and alerts.
The speakers propose a solution using a schema definition that captures metric changes, including name, unit, label names, and values.
This allows for automatic transformation of queries to use the new metric version, ensuring seamless updates without disrupting users.
The proposed solution leverages existing tools like OpenTelemetry's Weaver CLI, which can validate schemas, generate documentation, and perform transformations.
The speakers demonstrate how this approach enables efficient and flexible renaming of metrics in Prometheus, supporting both Prometheus and OpenTelemetry users.
# Main Points

|   # | Main point                                                                                     |
| --: | ---------------------------------------------------------------------------------------------- |
|   1 | Renaming metrics is problematic because it breaks user queries, dashboards, and automation.    |
|   2 | Changing a metric name can cause issues with labels, units, and sample values.                 |
|   3 | Renaming metrics can be necessary due to changes in naming conventions or new recommendations. |
|   4 | There are five main strategies for renaming metrics:                                           |
|   5 | No change strategy: Avoid changing the metric.                                                 |
|   6 | Documented change: Generate documentation for the change.                                      |
|   7 | Version read: Pin a metric to a certain version when querying it.                              |
|   8 | Writing all known versions of the same metric.                                                 |
|   9 | Transforming queries on the fly using a transformation file.                                   |
|  10 | Having a schema for your metric can help mitigate issues with renaming.                        |
|  11 | Open telemetry's Weaver CLI is an amazing tool for working with schemas and transformations.   |
|  12 | The ecosystem needs to work together to improve the seamless renames in Prometheus.            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Rw4c7lmdyFs)