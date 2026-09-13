---
layout: default
title:
  "The Fourth Pillar Arrives: OpenTelemetry Profiling Alpha in A... Felix Geisendörfer
  & Florian Lehner"
nav_order: 356
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The presentation introduces the alpha release of OpenTelemetry profiling,
  highlighting its significance as a new observability signal alongside logs, metrics,
  and traces. Profiling is explained as a tool for understanding code performance...
resource: https://www.youtube.com/watch?v=TKp2snmgvtQ
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

The presentation introduces the alpha release of OpenTelemetry profiling, highlighting its significance as a new observability signal alongside logs, metrics, and traces.
Profiling is explained as a tool for understanding code performance, diagnosing incidents, reducing costs, and optimizing performance, with flame graphs and other visualizations aiding analysis.
The speakers detail the technical evolution of the profiling format, emphasizing efficiency improvements like deduplication and dictionary support, as well as the ability to correlate profiles with other telemetry signals.
They demonstrate the eBPF-based profiler, which enables frictionless, low-overhead, whole-system profiling across multiple languages without requiring application changes, and showcase its practical use in identifying a real-world production issue.
The talk concludes with a discussion of ongoing and future work, including broader SDK support, improved interoperability, and enhanced symbolication, and invites community feedback and contributions as profiling moves toward beta and stable releases.

# Main Points

|   # | Main point                                                                                                                           |
| --: | ------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | OpenTelemetry profiling signal (profiles) has reached alpha stage.                                                                   |
|   2 | Profiling provides insights into CPU, memory, and performance issues.                                                                |
|   3 | Main use cases: incident investigation, cost optimization, and performance tuning.                                                   |
|   4 | Profiles help identify code paths responsible for resource spikes or regressions.                                                    |
|   5 | Flame graphs are the primary visualization, showing function-level resource usage.                                                   |
|   6 | Additional visualizations (thread timelines, flame scope) are enabled by extra sample dimensions (timestamps, thread IDs).           |
|   7 | Profiling format optimized for efficiency: uses dictionaries to avoid repeated strings, reducing payload size by up to 40%.          |
|   8 | Supports correlation with other OpenTelemetry signals (metrics, logs, traces) via links containing span and trace IDs.               |
|   9 | eBPF-based profiler enables frictionless, system-wide profiling on Linux without code changes or restarts.                           |
|  10 | Custom stack unwinding supports interpreted languages (Java, NodeJS, Python, PHP, Perl, etc.).                                       |
|  11 | eBPF profiler typically incurs ~1% CPU overhead.                                                                                     |
|  12 | Profiling receiver can be deployed as a DaemonSet; collector configuration is separate due to elevated privileges.                   |
|  13 | Demo showed profiling of Python and NodeJS programs, including mixed-language stack traces.                                          |
|  14 | Real-world example: profiling identified an infinite loop bug introduced by an AI refactor in a production e-commerce app.           |
|  15 | Next steps: move to beta/stable, add units to resource attributes, extend OTLP for symbolication (debug symbols for native code).    |
|  16 | Instrumentation work is ongoing: receivers exist for Go (net/http/prof, Go Flight Recorder), Java (async-profiler, SDK in progress). |
|  17 | OpenTelemetry profiling improves on pprof by supporting stack trace references and better timestamp handling.                        |
|  18 | Community contributions and feedback are encouraged; blog post and documentation available.                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=TKp2snmgvtQ)
