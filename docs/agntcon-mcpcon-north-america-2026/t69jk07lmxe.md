---
layout: default
title: "Building Production-Ready Agents with a Regression Test Suite - Yuki Watanabe, Databricks"
nav_order: 52
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Yuki Watanabe from Databricks presents a framework for building production-ready AI agents by addressing the limitations of generic evaluations, which often fail to capture real-world operational f..."
resource: "https://www.youtube.com/watch?v=t69jk07lMxE"
tags:
  - agntcon-mcpcon-north-america-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-08T02:03:18+00:00
---

# Summary

Yuki Watanabe from Databricks presents a framework for building production-ready AI agents by addressing the limitations of generic evaluations, which often fail to capture real-world operational failures.
He advocates for a "Trace, Failure, and Test" approach, starting with immediate observability using MLflow, an open-source tool under the Linux Foundation, to record detailed execution data such as model calls, latency, and costs.
To transform this raw data into actionable insights, MLflow’s issue detection feature proactively analyzes thousands of traces to identify and cluster common failure modes, providing specific evidence for each issue.
These identified failures are then converted into regression tests using Pytest, creating a CI/CD pipeline that prevents new fixes from causing regressions in other areas.
Finally, the same scoring criteria used for offline testing are reused for continuous production monitoring, establishing a continuous improvement flywheel that iteratively enhances agent reliability and performance.

# Main Points

|   # | Main point                                                                                                                                          |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | , high traffic, and dependency failures, regardless of local test success.                                                                          |
|   2 | (e.g., correctness, hallucination scores) often miss specific production failure modes and do not guarantee user satisfaction or task completion.   |
|   3 | "Trace, Failure, and Test."                                                                                                                         |
|   4 | , model calls, context, metrics, and errors for each request.                                                                                       |
|   5 | , evaluation, and monitoring capabilities for agents.                                                                                               |
|   6 | (via one-line autolog) or the OpenTelemetry SDK, supporting frameworks like LangGraph, Pydantic AI, and CrewAI.                                     |
|   7 | ; MLflow’s "Issue Detection" feature uses an agent to proactively monitor traces, cluster findings, and surface common failure modes with evidence. |
|   8 | "issue" is defined as a specific failure mode plus the trace evidence that proves it occurred.                                                      |
|   9 | , regression tests are necessary to ensure that fixing one issue does not break others.                                                             |
|  10 | /fail assertions, rather than generic scores.                                                                                                       |
|  11 | /evaluators used for offline regression testing can be reused for real-time production monitoring to track pass rates and flag new issues.          |
|  12 | "flywheel" loop: Trace production data, detect issues, fix them, add regression tests, and monitor for regressions.                                 |
|  13 | /CD pipeline for agent quality.                                                                                                                     |
|  14 | , with options for self-hosting or managed services via Databricks, SageMaker, or Red Hat.                                                          |
|  15 | (e.g., focusing on cost or specific domains).                                                                                                       |
|  16 | ; consistent failures are prioritized, while rare occurrences are deprioritized.                                                                    |
|  17 | (GitHub/GitLab) to inspect root causes and improve denoising.                                                                                       |
|  18 | , meaning it is compatible with existing OpenTelemetry instrumentation and can ingest standard spans.                                               |

# Video

[![Video thumbnail](https://img.youtube.com/vi/t69jk07lMxE/hqdefault.jpg)]("https://www.youtube.com/watch?v=t69jk07lMxE")

[Watch on YouTube](https://www.youtube.com/watch?v=t69jk07lMxE)
