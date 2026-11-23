---
layout: default
title: Steps down the OpenAPI Path
nav_order: 133
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Steven Fenno and Adam War system presented a detailed overview of their efforts to integrate OpenAPI 3.1 schemas into various OpenStack services, addressing the significant challenges of maintainin..."
resource: "https://www.youtube.com/watch?v=ohhaufetp5w"
youtube_stats:
  view_count: 31
  channel_subscriber_count: 46800
tags:
  - openinfra-summit-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T23:38:50+00:00
---

# Summary

Steven Fenno and Adam War system presented a detailed overview of their efforts to integrate OpenAPI 3.1 schemas into various OpenStack services, addressing the significant challenges of maintaining SDKs for a complex, 15-year-old API surface.
They explained that while previous attempts using Swagger and OpenAPI 2.0 faced community resistance, the adoption of OpenAPI 3.1 offers critical advantages such as superset adjacent schemas and better extension support, which are essential for handling OpenStack-specific features like API micro-versions.
The team employs a "schema-on-top" approach, using Python decorators to validate request and response bodies against handwritten schemas, ensuring that the specifications accurately reflect the actual behavior of existing services rather than driving the application design.
Adam War system further demonstrated how a code generator leverages these schemas to automatically produce API documentation, Rust-based CLI and TUI tools, and SDK bindings, significantly reducing manual maintenance efforts and enabling rapid onboarding of new services.
The presentation concluded with a discussion on ongoing challenges, including the difficulty of describing headers in JSON schemas, the need for standardized handling of enums and micro-versions, and the future goal of generating OpenAPI specs directly from source code to create a seamless, automated pipeline for client tooling.

# Main Points

|   # | Main point                                                                                                                                                                         |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Steven and Adam presented the integration of OpenAPI schemas into OpenStack services and their practical applications.                                                             |
|   2 | Writing and maintaining OpenStack SDKs is difficult due to the huge API surface, legacy code, and API micro-versions that prevent removal of obsolete endpoints.                   |
|   3 | OpenAPI 3.1 is preferred over previous attempts like Swagger because it supports superset adjacent schemas and extensions, which are critical for OpenStack's specific needs.      |
|   4 | The team chose to layer schemas on top of existing applications rather than generating applications from schemas, as OpenStack services are already established.                   |
|   5 | Integration is achieved using Python decorators to wrap controller methods for request and response validation against handwritten schema files.                                   |
|   6 | Response body validation is enabled in CI for projects with native schemas to ensure accuracy, though it is not recommended for production use.                                    |
|   7 | Adam demonstrated generated API documentation that combines OpenAPI specs with traditional OpenStack styles to minimize disruption for users.                                      |
|   8 | A code generator tool extracts schema information from service source code to create OpenAPI specs and generates SDKs and CLIs for languages like Rust.                            |
|   9 | The Rust CLI and SDK are fully generated from these specs, reducing maintenance overhead and allowing developers to focus on features like caching and authentication.             |
|  10 | Metadata extensions are used to map API operations to CLI commands, handling complex cases where a single HTTP method serves multiple logical actions.                             |
|  11 | The code generator normalizes JSON schema variations into Abstract Data Types (ADTs) before converting them to target-specific types for code generation.                          |
|  12 | A pipeline is being developed for Keystone NG to automatically generate OpenAPI specs from source code, triggering immediate updates in SDKs and CLIs.                             |
|  13 | Micro-versions are handled by adding metadata to OpenAPI paths, allowing clients to target specific API versions, though this results in large spec files.                         |
|  14 | Go for Cloud currently does not use code generation, and a major version update is planned to address missing fields and align with the new approach.                              |
|  15 | Client-side validation is challenging because different clouds may have different configurations and server-side validation behaviors, making static schema validation unreliable. |
|  16 | Headers such as service tokens and request IDs are difficult to describe in JSON schemas, requiring workarounds in the code generator to support them.                             |

# Video

[![Video thumbnail](https://img.youtube.com/vi/ohhaufetp5w/hqdefault.jpg)](https://www.youtube.com/watch?v=ohhaufetp5w)

[Watch on YouTube](https://www.youtube.com/watch?v=ohhaufetp5w)
