---
type: Video Note
title: "Lightning Talk: Tracing the Untraceable: OpenTelemetry for ‘Vibe-Coded’ LLM Apps - Pranay Prateek"
description: "Prane, a co-founder of Signos, introduces the importance of tracing and monitoring large language model (LLM) applications using open telemetry, an open-source standard that avoids vendor lock-in and is rapidly growing in popularity. He exp..."
resource: https://www.youtube.com/watch?v=dprArlELOBU
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Prane, a co-founder of Signos, introduces the importance of tracing and monitoring large language model (LLM) applications using open telemetry, an open-source standard that avoids vendor lock-in and is rapidly growing in popularity.
He explains that LLM apps are often black boxes with unpredictable behaviors that can only be fully understood and tested in production, making robust observability essential.
Through a demo, Prane shows how Signos, built on open telemetry, can monitor a LangChain-based LLM app to identify bottlenecks such as backend slowdowns, server errors, or LLM rate limits, and detect issues like infinite loops or excessive tool calls.
He emphasizes that open telemetry enables real-time monitoring of metrics like latency, error rates, and tool usage without relying on third-party vendors, allowing developers to set effective alerts and guardrails.
Prane concludes by encouraging the audience to adopt open telemetry for better insight and reliability in LLM applications.
# Main Points

|   # | Main point                                                                                                                 |
| --: | -------------------------------------------------------------------------------------------------------------------------- |
|   1 | Prane is a co-founder and maintainer at Signos.                                                                            |
|   2 | The talk focuses on tracing LLM (Large Language Model) apps using OpenTelemetry.                                           |
|   3 | Signos is an open source observability platform based natively on OpenTelemetry.                                           |
|   4 | Signos has around 24,000 GitHub stars.                                                                                     |
|   5 | Signos provides traces, metrics, and logs in a single pane.                                                                |
|   6 | OpenTelemetry is the second fastest growing project in CNCF after Kubernetes.                                              |
|   7 | OpenTelemetry offers no vendor lock-in and is a completely open source standard for instrumentation.                       |
|   8 | Instrumenting apps with OpenTelemetry helps understand app behavior, especially for LLM apps, which are often black boxes. |
|   9 | LLM apps are non-deterministic and require testing in production.                                                          |
|  10 | Better guardrails are needed for agentic AI, as it can break unexpectedly.                                                 |
|  11 | Demo involved a Signos MCP instance connected to a LangChain-based LLM app.                                                |
|  12 | Monitoring is done using Signos.                                                                                           |
|  13 | Potential bottlenecks include the LangChain app, the MCP server, or the LLM model (e.g., rate limits).                     |
|  14 | Identifying issues requires monitoring each step in the process.                                                           |
|  15 | Example given where a tool call gets stuck in a loop, sending 40 spans instead of 1-2.                                     |
|  16 | Important to monitor tool call frequency, token consumption, and performance metrics in production.                        |
|  17 | OpenTelemetry enables this monitoring without third-party vendor libraries.                                                |
|  18 | Dashboards can show P95 latency, error rates, tool call distribution, and other metrics.                                   |
|  19 | Observability helps identify where LLM agents misbehave.                                                                   |
|  20 | Setting up alerts and guardrails allows detection and remediation of issues.                                               |
|  21 | Understanding bottlenecks can improve user experience.                                                                     |
|  22 | Encouragement to explore OpenTelemetry for LLM monitoring.                                                                 |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=dprArlELOBU)