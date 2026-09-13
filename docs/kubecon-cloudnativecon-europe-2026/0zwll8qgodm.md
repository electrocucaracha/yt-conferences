---
layout: default
title:
  "OpenTelemetry Collector SIG: Project Updates - Jade G, Dmitrii A, Alex B,
  Evan B & Antoine T"
nav_order: 232
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The OpenTelemetry Collector team provided a comprehensive update on the
  project's progress, focusing on stabilization efforts and key component improvements.
  They discussed the organization of the collector across three main repositories—co...
resource: https://www.youtube.com/watch?v=0zwLl8QGOdM
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

The OpenTelemetry Collector team provided a comprehensive update on the project's progress, focusing on stabilization efforts and key component improvements.
They discussed the organization of the collector across three main repositories—core, contrib, and releases—and highlighted the ongoing work to stabilize APIs, core libraries, and configurations, with 25 modules stabilized so far.
Major updates include performance improvements and memory reductions in Kubernetes components, deprecation of the batch processor in favor of exporter-based batching, enhancements to internal telemetry for better component-level insights, and the introduction of experimental features like entities and profiling support.
The team also addressed the challenges of maintaining a large number of contrib components, encouraging users to build custom distributions with the collector builder for better efficiency and security, while acknowledging the convenience of the all-in-one contrib distribution.
Finally, they invited feedback and questions, noting ongoing discussions around further optimizations, such as improved load balancing and data compression, and encouraged community involvement in shaping future developments.

# Main Points

|   # | Main point                                                                                                                                                                                                                                     |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | OpenTelemetry Collector project is in its seventh year; this is the first major update session.                                                                                                                                                |
|   2 | The Collector is a multi-tool binary for receiving, processing, and sending telemetry data.                                                                                                                                                    |
|   3 | The project is organized into three main repositories: core (core libraries, OTLP receiver/exporter, batch processor, builder), contrib (most components, e.g., Prometheus receiver), and releases (packaged binaries, containers, manifests). |
|   4 | Stability is the top user-requested feature; significant effort has gone into stabilizing core modules and APIs.                                                                                                                               |
|   5 | 25 modules have been stabilized; more remain.                                                                                                                                                                                                  |
|   6 | Stabilization efforts focus on key components based on user surveys, with requirements like stable config, benchmarks, clear ownership, and documentation.                                                                                     |
|   7 | Kubernetes components (e.g., k8sattributes processor) are being consolidated and improved, including ~20% memory reduction in recent versions.                                                                                                 |
|   8 | Leader election extension prevents over-scraping Kubernetes API; Kubernetes events receiver will not be deprecated.                                                                                                                            |
|   9 | Prometheus receiver stabilization is in progress; metric start time now requires a dedicated processor; Prometheus remote write receiver added.                                                                                                |
|  10 | OTTL and transform processor promoted to beta; inferred context feature simplifies data access.                                                                                                                                                |
|  11 | Batch processor is deprecated; batching now handled at the exporter level, with improved configurability (events/items and bytes).                                                                                                             |
|  12 | Performance optimizations: internal data model (pdata) no longer depends on goproto, reducing allocations and binary size.                                                                                                                     |
|  13 | Internal telemetry improvements: component attributes tagging, universal pipeline metrics, basic error logs, and metric views for customization.                                                                                               |
|  14 | Experimental "entities" feature introduced to better represent relationships between resources; available in Kubernetes cluster receiver.                                                                                                      |
|  15 | Profiling support (profiles signal) added in alpha; prof receiver can report collector’s own profiles.                                                                                                                                         |
|  16 | Contrib repo has many components; efforts underway to raise the bar for new additions an                                                                                                                                                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=0zwLl8QGOdM)
