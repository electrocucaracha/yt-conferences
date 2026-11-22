---
layout: default
title: "Sponsor Presentations - Introducing Pydantic's new platform (Sponsor: Pydantic)"
nav_order: 48
parent: PyCon US 2024
type: Video Note
description: "The speaker from Pydantic explains the rationale behind building Logfire, an observability platform, by addressing the limitations of traditional linear logging in complex applications."
resource: "https://www.youtube.com/watch?v=kns4Qlvl3vk"
youtube_stats:
  view_count: 1146
  like_count: 22
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

The speaker from Pydantic explains the rationale behind building Logfire, an observability platform, by addressing the limitations of traditional linear logging in complex applications.
He argues that standard logs lack the necessary context to understand relationships between events, such as which specific database query or API call caused a failure, whereas Logfire uses a tree-structured tracing model to provide immediate clarity on application flow and performance.
Built on OpenTelemetry but designed for ease of use, Logfire simplifies setup with minimal code, offering Python-specific features like automatic function tracing, F-string attribute extraction, and rich visualization of Pydantic models and LLM interactions.
The platform also supports distributed tracing across multiple services and languages, allows for SQL-based querying of observability data, and integrates with existing tools like FastAPI, Django, and OpenAI to help developers identify bottlenecks and errors without extensive manual instrumentation.

# Main Points

|   # | Main point                                                                                                                                                           |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Logfire is an observability platform built by the Pydantic team to address the limitations of traditional linear logging in complex applications.                    |
|   2 | Traditional logging lacks context, making it difficult to correlate events, measure duration, or understand nested operations within a request.                      |
|   3 | Logfire introduces a tree structure for traces, allowing developers to visualize the hierarchy of operations, durations, and associated attributes.                  |
|   4 | The platform is built on OpenTelemetry standards but abstracts away complex configuration, requiring only a few lines of code to initialize.                         |
|   5 | Logfire offers Python-specific features like auto-tracing, which automatically instruments function calls to identify performance bottlenecks without manual coding. |
|   6 | F-string magic allows developers to use standard Python f-strings for logging, automatically extracting variables as structured attributes for better IDE support.   |
|   7 | The platform provides rich rendering of Python objects, such as Pydantic models and dataclasses, displaying type information and collapsible structures in the UI.   |
|   8 | Database instrumentation is supported for multiple engines via OpenTelemetry integrations, enabling visualization of SQL queries, execution times, and results.      |
|   9 | Web framework integrations, including FastAPI and Django, automatically capture request details, headers, and response codes with minimal setup.                     |
|  10 | Outgoing HTTP requests are instrumented to track duration and status, and OpenTelemetry headers are injected to enable distributed tracing across services.          |
|  11 | Distributed tracing works across different languages and services, such as Python, Go, and JavaScript, by leveraging standard OpenTelemetry instrumentation.         |
|  12 | Pydantic validation is instrumented to log success or failure details, including input data, schema names, and specific validation errors.                           |
|  13 | Generative AI integrations, particularly for OpenAI, provide detailed views of LLM interactions, token usage, and image generation results.                          |
|  14 | Custom UI panels allow developers to build specialized visualizations within Logfire using TypeScript, enhancing the display of complex data.                        |
|  15 | Users can query observability data using standard SQL, enabling complex aggregations, filtering, and the creation of custom dashboards and alerts.                   |
|  16 | Logfire supports metrics recording for high-volume scenarios, allowing for the monitoring of numeric values like validation failure rates.                           |
|  17 | The platform includes a scrubbing mechanism to handle sensitive data, though it is currently described as somewhat aggressive in its default behavior.               |
|  18 | Logfire is a closed-source, hosted service that is currently free during its beta phase, with plans for enterprise hosting and paid tiers.                           |
|  19 | The team emphasizes ease of use and developer experience over raw data volume, focusing on providing actionable insights rather than exhaustive logging.             |
|  20 | Integrations with existing logging libraries like standard logging, structlog, and loguru are supported to ease migration from current setups.                       |
|  21 | Task queue systems like Celery and ARQ are supported via OpenTelemetry links to trace jobs that may execute asynchronously outside the initial request span.         |
|  22 | The platform collects process IDs to help identify when operations move between subprocesses, though this feature is still being refined.                            |
|  23 | Logfire aims to provide a superior user experience compared to raw OpenTelemetry or competitors like DataDog by simplifying setup and enhancing data visualization.  |

# Video

[![Video thumbnail](https://img.youtube.com/vi/kns4Qlvl3vk/hqdefault.jpg)](https://www.youtube.com/watch?v=kns4Qlvl3vk)

[Watch on YouTube](https://www.youtube.com/watch?v=kns4Qlvl3vk)
