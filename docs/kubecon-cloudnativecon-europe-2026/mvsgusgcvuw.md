---
layout: default
title:
  OpenTelemetry Project Update and 'Ask the Experts' - Pablo B, Juraci P, Marylia
  G & Severin N
nav_order: 234
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The OpenTelemetry product update session covered several major advancements
  and ongoing initiatives within the project. The team announced the stabilization
  of declarative configuration, allowing users to manage complex settings across mult...
resource: https://www.youtube.com/watch?v=mvSGusgcVuw
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

The OpenTelemetry product update session covered several major advancements and ongoing initiatives within the project.
The team announced the stabilization of declarative configuration, allowing users to manage complex settings across multiple languages using a unified YAML file, reducing reliance on environment variables.
They introduced Weaver, a tool for defining and validating custom telemetry conventions, and highlighted the OpenTelemetry Injector, which streamlines auto-instrumentation across Java, Node.js, .NET, and Python without code changes.
Performance improvements, particularly in the Go SDK, and the deprecation of the span event API in favor of log-based events were discussed, alongside efforts to enhance stability and reliability across the ecosystem.
The session also emphasized community involvement, new SIGs (special interest groups), and projects like Blueprints and the Ecosystem Explorer, while addressing questions on roadmap priorities, client instrumentation, and the impact of AI-generated contributions.

# Main Points

|   # | Main point                                                                                                                                                                          |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | OpenTelemetry site has been redesigned to reflect its status as the open standard for telemetry.                                                                                    |
|   2 | Declarative configuration is now stable, allowing configuration via a unified YAML file across languages (Java, JavaScript, Python, C++, Go, PHP).                                  |
|   3 | Declarative config reduces reliance on environment variables and centralizes options in a single file.                                                                              |
|   4 | Migration examples and support are available; feature parity across SDKs is in progress.                                                                                            |
|   5 | Weaver is a tool for defining, validating, and evolving custom telemetry conventions using registries and YAML schemas.                                                             |
|   6 | Weaver supports custom policy rules and live checks for policy violations.                                                                                                          |
|   7 | OpenTelemetry Injector enables auto-instrumentation without code changes using LD_PRELOAD for Java, Node.js, .NET, and opt-in for Python.                                           |
|   8 | Injector simplifies instrumentation setup across languages.                                                                                                                         |
|   9 | Go SDK metric performance improved 4-30x; further enhancements in progress.                                                                                                         |
|  10 | Span event API is deprecated in favor of log-based events; span events will be phased out gradually.                                                                                |
|  11 | Cross-project initiative "stable by default" focuses on stability, documentation, and reliability.                                                                                  |
|  12 | Profiling support is going alpha in OTLP 1.11; eBPF instrumentation aims for 1.0 release this year.                                                                                 |
|  13 | Collector SIG focuses on stability of most-used components; Kubernetes semantic conventions have a release candidate.                                                               |
|  14 | Community initiatives include blueprints for instrumentation guidance, new SIGs (Collector MCP, Browser SIG, Zigzag, PHP DRO, Kotlin), and the Ecosystem Explorer for SDK metadata. |
|  15 | Over 50 OpenTelemetry-related talks and sessions available.                                                                                                                         |
|  16 | Governance committee is addressing challenges from low-effort AI contributions.                                                                                                     |
|  17 | Graduation process is ongoing; end user feedback is encouraged.                                                                                                                     |
|  18 | Browser and client instrumentation (RUM) is being actively developed by the Browser SIG.                                                                                            |
|  19 | Community contributions and feedback are welcomed, especially for demo updates and stability efforts.                                                                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=mvSGusgcVuw)
