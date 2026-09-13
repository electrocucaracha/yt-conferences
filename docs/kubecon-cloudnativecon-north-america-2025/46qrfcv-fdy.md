---
type: Video Note
title: "Beyond the Dashboard: Modern Observability... Danielle C, Whitney L, Stevie C, Khallai T & Payal B"
description: "The session explores modern observability in platform engineering, emphasizing the shift from isolated logs, metrics, and traces to a unified, correlated approach enabled by open telemetry standards. Panelists discuss the challenges of mana..."
resource: https://www.youtube.com/watch?v=46qRFcv_FDY
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The session explores modern observability in platform engineering, emphasizing the shift from isolated logs, metrics, and traces to a unified, correlated approach enabled by open telemetry standards.
Panelists discuss the challenges of managing overwhelming volumes of observability data, highlighting the importance of prioritizing actionable signals, reducing alert fatigue, and focusing on customer experience and reliability.
Strategies such as defining golden signals, leveraging AI for dynamic thresholding, and regular alert reviews are shared to improve signal-to-noise ratio.
The conversation also covers the need for consistent instrumentation, developer engagement through value-driven dashboards, and the adoption of semantic conventions to standardize telemetry.
The panel examines the promise of AI in automating diagnostics and remediation, while cautioning against over-reliance, loss of human oversight, and the necessity for robust guardrails and accountability.
Looking ahead, the group expresses excitement about open telemetry’s growing adoption, the move toward machine-first observability, and the integration of observability into real-time development workflows, while underscoring the ongoing need for human judgment and standardized practices.
# Main Points

|   # | Main point                                                                                                                                                   |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Modern observability involves correlating logs, metrics, and traces as a streaming braid of data, not separate pillars.                                      |
|   2 | OpenTelemetry is becoming the industry standard for correlating observability signals and enabling a holistic view.                                          |
|   3 | Instrumenting code, including scripts and CI/CD pipelines, is key to achieving comprehensive observability.                                                  |
|   4 | Excessive telemetry can create noise and alert fatigue; prioritizing user experience and actionable alerts is essential.                                     |
|   5 | Regular review and pruning of alerts help reduce noise and focus on meaningful signals.                                                                      |
|   6 | Defining "important" signals using golden signals (availability, latency, error rate, request count) and customer impact metrics is effective.               |
|   7 | AI Ops can dynamically adjust alert thresholds based on traffic patterns and seasonality.                                                                    |
|   8 | Actionable alerts should be prioritized; non-actionable ones can be moved to FYI dashboards.                                                                 |
|   9 | Balancing deep visibility with cost requires collaboration between observability, operations, and data science teams, ensuring metrics align with SLOs/SLAs. |
|  10 | To encourage developer instrumentation, provide out-of-the-box dashboards, demonstrate value, and standardize telemetry conventions.                         |
|  11 | OpenTelemetry semantic conventions and tools like OpenTelemetry Weaver help standardize and simplify instrumentation.                                        |
|  12 | Resistance to OpenTelemetry can be addressed by showing its direct value to developers.                                                                      |
|  13 | Observability can improve developer experience by providing dashboards that clarify platform status and reduce unnecessary support requests.                 |
|  14 | AI in observability enables correlation of signals, root cause analysis, and automated remediation via intelligent agents.                                   |
|  15 | Concerns with AI include autonomy without accountability, the risk of hallucinations, and overdependence leading to skill atrophy.                           |
|  16 | Guardrails, human oversight, and reversible automated actions are critical when using AI in observability.                                                   |
|  17 | Trends: Growing adoption of OpenTelemetry, standardization of metrics, shift toward machi                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=46qRFcv_FDY)