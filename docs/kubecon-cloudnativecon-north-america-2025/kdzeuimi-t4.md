---
type: Video Note
title: "Instrumentation Score: The Difference Between Telemetr... Juraci Paixão Kröhling & Michele Mancioppi"
description: "In this presentation, Judas, Mikuel, and Julie introduce the concept of the Instrumentation Score, a knowledge base and open specification designed to help teams assess and improve the quality of their telemetry data, particularly within th..."
resource: https://www.youtube.com/watch?v=kdzeUiMI_t4
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this presentation, Judas, Mikuel, and Julie introduce the concept of the Instrumentation Score, a knowledge base and open specification designed to help teams assess and improve the quality of their telemetry data, particularly within the OpenTelemetry ecosystem.
They discuss common pitfalls of "bad telemetry," such as excessive or irrelevant data, high cardinality metrics, overuse of debug logs in production, and outdated internal spans, emphasizing that up to 90% of collected telemetry is often unused.
The Instrumentation Score encodes industry best practices and opinions into a set of rules, allowing organizations to numerically evaluate and compare the quality of telemetry across services, prioritize improvements, and avoid striving for unattainable perfection.
The presenters stress that good telemetry evolves over time and that the score should be used pragmatically to guide incremental enhancements.
They also highlight the importance of semantic conventions in standardizing telemetry and invite the community to contribute their experiences and feedback to further refine the Instrumentation Score.
# Main Points

|   # | Main point                                                                                                                                                                                       |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Introduced speakers: Mikuel (Dura, OpenTelemetry auto-injector maintainer), Julie (Olig Garden, OpenTelemetry governance, organizer of hotel night Berlin, content creator for Telemetry Drops). |
|   2 | Focus of talk: Instrumentation Score, overview of spec, rule structure, examples, and Q&A.                                                                                                       |
|   3 | Observability defined as the ability to understand what a system is doing and why.                                                                                                               |
|   4 | Telemetry is collected to achieve observability; OpenTelemetry is a primary tool discussed.                                                                                                      |
|   5 | Instrumentation can be automatic (e.g., Java agent) or manual (using OpenTelemetry API).                                                                                                         |
|   6 | Too much telemetry can result in "bad telemetry"—data that is not useful, may contain sensitive info, or is never used (up to 90% is junk).                                                      |
|   7 | Classic telemetry issues:                                                                                                                                                                        |
|   8 | Metric cardinality: Excessive unique combinations (e.g., using HTTP path instead of route) can cause costs to skyrocket.                                                                         |
|   9 | Overuse of debug logs in production; most logs are info (33%), warning (1%), trace (1%), error/fatal (0.4%).                                                                                     |
|  10 | Noisy internal spans: Instrumenting too much detail can become obsolete as systems stabilize.                                                                                                    |
|  11 | "Bad telemetry" is context- and time-dependent; what was useful once may become noise.                                                                                                           |
|  12 | Instrumentation Score:                                                                                                                                                                           |
|  13 | Open, opinionated knowledge base/spec to define good vs. bad telemetry.                                                                                                                          |
|  14 | Provides guidelines and a numerical score (0-100) per service, scoped by service.name.                                                                                                           |
|  15 | Not a tool, but a spec and knowledge base for teams and vendors to use as a baseline or extend.                                                                                                  |
|  16 | Inspired by prior art (CVSS, Google Lighthouse, SSL Labs).                                                                                                                                       |
|  17 | Rules are easy to understand, each with rationale, impact, and calculation logic.                                                                                                                |
|  18 | Not about achieving 100%; aim for a good range (e.g., 75%+), be pragmatic.                                                                                                                       |
|  19 | Fixing bad telemetry can often be done in pipelines (e.g., OTTL in OpenTelemetry Collector).                                                                                                     |
|  20 | Key takeaways:                                                                                                                                                                                   |
|  21 | No telemetry is bad, but too much or irrelevant telemetry is also bad.                                                                                                                           |
|  22 | Start with auto-instrumentation, then prune unnecessary data.                                                                                                                                    |
|  23 | Good telemetry changes over time.                                                                                                                                                                |
|  24 | Use Instrumentation Score as                                                                                                                                                                     |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=kdzeUiMI_t4)