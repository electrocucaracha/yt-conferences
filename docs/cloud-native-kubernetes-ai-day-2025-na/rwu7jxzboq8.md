---
layout: default
title:
  "This Lying Has To Stop: Keeping AI Honest with OpenTelemetry - Whitney Lee,
  Datadog"
nav_order: 17
parent: Cloud Native Kubernetes Ai Day 2025 Na
type: Video Note
description:
  The speaker introduces Commit Story, an automated engineering journal
  app built with Cloud Code that uses AI to document code changes, commit messages,
  and developer-AI conversations triggered by Git commits. The app is heavily instrumented...
resource: https://www.youtube.com/watch?v=rwu7JXzbOQ8
tags:
  - cloud-native-kubernetes-ai-day-2025-na
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The speaker introduces Commit Story, an automated engineering journal app built with Cloud Code that uses AI to document code changes, commit messages, and developer-AI conversations triggered by Git commits.
The app is heavily instrumented with OpenTelemetry, allowing detailed observability and enabling Cloud Code to understand system behavior solely from telemetry data.
Through a live demo and a dramatized debugging session, the speaker illustrates how development-time telemetry aids in diagnosing issues, validating assumptions, and informing both AI assistants and developers, while also highlighting challenges such as managing data costs and the complexity of instrumentation.
OpenTelemetry is explained as a specification, protocol, and set of tools for standardizing and collecting telemetry data, with the speaker noting its unconventional use in this development context.
The talk concludes by emphasizing the benefits of telemetry for debugging and system understanding, acknowledging some drawbacks, and suggesting that AI-driven tooling could help automate instrumentation in the future.

# Main Points

|   # | Main point                                                                                                                                                              |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presenter introduced an app called Commit Story, an automated engineering journal designed to work with Cloud Code.                                                     |
|   2 | Commit Story runs as a background agent, triggered by Git commits, collecting code changes, commit messages, and Cloud Code conversations to generate journal entries.  |
|   3 | The app uses three AI journal generator functions: summarizing Git commits, extracting development dialogue, and identifying technical decisions.                       |
|   4 | The codebase is heavily instrumented with OpenTelemetry for demonstration purposes.                                                                                     |
|   5 | Telemetry data is sent to a Datadog backend but could work with any OpenTelemetry-compatible backend.                                                                   |
|   6 | Cloud Code can use telemetry data (trace IDs, logs, metrics) to generate system diagrams and understand application flow without reading the codebase.                  |
|   7 | Telemetry data includes traces, logs, and metrics, providing a holistic view of system behavior.                                                                        |
|   8 | OpenTelemetry is a specification, protocol (OTLP), and software (APIs, SDKs, Collector) for standardizing and collecting observability data.                            |
|   9 | Telemetry helped debug an issue where journal generation failed due to excessive raw chat data being passed to generator functions.                                     |
|  10 | The root cause was a recent code change that bypassed existing filtering logic when supporting multiple Cloud Code sessions.                                            |
|  11 | Telemetry validated the fix by confirming reduced input size to generator functions.                                                                                    |
|  12 | Development-time telemetry provided benefits: disproving wrong AI assumptions, aiding debugging, enabling historical comparisons, and giving AI a holistic system view. |
|  13 | Drawbacks include unknown costs, potential for AI to make wrong assumptions, and the challenge of extensive instrumentation.                                            |
|  14 | Auto-instrumentation and AI agents can help with code instrumentation.                                                                                                  |
|  15 | Telemetry data is associated with trace IDs and dates, enabling historical queries.                                                                                     |
|  16 | The session concluded with a Q&A about how telemetry data is queried and associated with commits.                                                                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=rwu7JXzbOQ8)
