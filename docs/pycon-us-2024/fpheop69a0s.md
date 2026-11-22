---
layout: default
title: "Sponsor Presentations - Python Powered Serverless Observability (Sponsor: Capital One)"
nav_order: 46
parent: PyCon US 2024
type: Video Note
description: "At PyCon 2024, Capital One engineers Dan Furman and Brian McNamara presented a comprehensive guide to implementing serverless observability using Python, emphasizing that while serverless architect..."
resource: "https://www.youtube.com/watch?v=fPhEOp69a0s"
youtube_stats:
  view_count: 455
  like_count: 4
  channel_subscriber_count: 34500
tags:
  - pycon-us-2024
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T10:18:11+00:00
---

# Summary

At PyCon 2024, Capital One engineers Dan Furman and Brian McNamara presented a comprehensive guide to implementing serverless observability using Python, emphasizing that while serverless architectures eliminate infrastructure management, they require intentional design for monitoring and troubleshooting.
The speakers detailed the three core pillars of observability—logs, metrics, and traces—demonstrating how to leverage AWS Lambda Power Tools to implement structured JSON logging, emit custom business metrics via the Embedded Metrics Format, and utilize AWS X-Ray for distributed tracing.
They highlighted the performance and cost advantages of Python in serverless environments, noting its fast cold starts and low total cost of ownership compared to containerized solutions.
Additionally, the presentation introduced OpenTelemetry (OTel) as a vendor-agnostic alternative, showcasing a "zero-code" instrumentation approach using AWS Lambda layers to export telemetry data to third-party providers like Honeycomb without modifying application code.
The session concluded with best practices for log retention, metric aggregation, and the importance of designing observability into applications from the start to ensure efficient troubleshooting and business insight.

# Main Points

|   # | Main point                                                                                                                                                                                                |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Python is highly effective for serverless computing due to its fast startup time, which allows for millisecond-level event processing and significant cost savings compared to container-based solutions. |
|   2 | Serverless architecture shifts infrastructure management, scaling, and security responsibilities to the cloud provider, allowing developers to focus exclusively on application code and dependencies.    |
|   3 | Observability is distinct from monitoring; it involves understanding a system's internal state through logs, metrics, and traces to facilitate troubleshooting and holistic system analysis.              |
|   4 | Structured logging using JSON formats, such as those provided by AWS Lambda Power Tools, enables efficient searching and aggregation of log data compared to unstructured text logs.                      |
|   5 | AWS Lambda integrates with CloudWatch Logs to provide default execution details, but developers should implement structured logging to capture specific business context and user actions.                |
|   6 | Metrics provide data measured over time to track performance and business events, such as successful payments, and should be designed into the application from the start.                                |
|   7 | Developers should use appropriate statistical aggregations, such as P99 latency rather than averages, to accurately reflect customer experience and identify performance issues.                          |
|   8 | The Embedded Metrics Format (EMF) allows for the asynchronous publication of custom business metrics to CloudWatch, avoiding the performance penalties of synchronous API calls.                          |
|   9 | Tracing via AWS X-Ray provides visibility into distributed interactions and cold start durations, helping developers optimize initialization times and understand service dependencies.                   |
|  10 | OpenTelemetry (OTel) is a vendor-agnostic framework for collecting telemetry data, allowing teams to switch observability backends without modifying application code.                                    |
|  11 | Zero-code instrumentation is achievable in AWS Lambda by using Lambda layers that include OpenTelemetry SDKs and collectors, eliminating the need for manual code instrumentation.                        |
|  12 | AWS Lambda Power Tools simplifies the implementation of best practices for logging, metrics, and tracing by wrapping standard libraries and providing decorators for context injection.                   |
|  13 | Annotations in tracing are indexed and searchable, making them suitable for filtering traces by specific data fields, whereas metadata is not searchable but adds descriptive context.                    |
|  14 | Log retention policies should be configured to manage costs, with operational data kept for troubleshooting and long-term data archived to more cost-effective storage solutions like S3 or Glacier.      |
|  15 | Observability-driven development, similar to test-driven development, encourages designing instrumentation into the codebase early to answer business questions without requiring new deployments.        |
|  16 | The choice between vendor-specific tools like X-Ray and open standards like OpenTelemetry depends on organizational needs, with both supporting rich tracing and metric capabilities.                     |
|  17 | Developers should minimize instrumentation code to maintain readability while ensuring that critical business logic and performance metrics are captured for effective monitoring.                        |

# Video

[![Video thumbnail](https://img.youtube.com/vi/fPhEOp69a0s/hqdefault.jpg)](https://www.youtube.com/watch?v=fPhEOp69a0s)

[Watch on YouTube](https://www.youtube.com/watch?v=fPhEOp69a0s)
