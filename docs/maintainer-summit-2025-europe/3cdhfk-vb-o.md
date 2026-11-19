---
layout: default
title: "Avoiding Breaking Changes in Your Project: Lessons From the OpenTele... Pablo Baeyens & Evan Bradley"
nav_order: 14
parent: "Maintainer Summit 2025 - Europe"
type: Video Note
description: "Evan Bradley and Pablo, software engineers working on the OpenTelemetry Collector, present strategies for managing and communicating breaking changes in open-source software."
resource: "https://www.youtube.com/watch?v=3CDhFk-VB-o"
tags:
  - maintainer-summit-2025-europe
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-15T22:30:54+00:00
---

# Summary

Evan Bradley and Pablo, software engineers working on the OpenTelemetry Collector, present strategies for managing and communicating breaking changes in open-source software.
They emphasize the importance of defining stability levels more granularly than standard semantic versioning, using a model that ranges from "in development" to "stable" to clearly signal to users which components are safe for production use.
For API consumers, they recommend breaking large modules into smaller, independently versioned packages and separating experimental features into distinct "x" prefixed modules to prevent accidental reliance on unstable code.
For end users of binary applications, they advocate for the use of feature gates to decouple breaking changes from routine upgrades, allowing users to migrate at their own pace through alpha, beta, and stable stages.
Additionally, they discuss the value of maintaining a large "contrib" repository to test API changes against real-world usage patterns and propose future tools such as automated configuration schema migration and ecosystem-wide breaking change detection to further reduce the impact of necessary updates.

# Main Points

|   # | Main point                                                                                                                                                        |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The presentation focuses on managing breaking changes in the OpenTelemetry Collector, specifically for API consumers and CLI end users.                           |
|   2 | Software delivery forms include libraries and binary distributions, requiring different communication strategies for developers versus end users.                 |
|   3 | Open source projects face challenges in identifying users and usage patterns due to privacy concerns and lack of analytics.                                       |
|   4 | The project aims for "fearless upgrades" where upgrading from version X to X+1 results in no compilation or configuration errors.                                 |
|   5 | Breaking changes are defined as intentional shifts in expected behavior, distinct from bugs which are unintentional.                                              |
|   6 | Separate changelogs are maintained for API changes and binary features to help different audiences identify relevant updates.                                     |
|   7 | The Go language's lack of certain features necessitates specific strategies for managing API stability and compatibility.                                         |
|   8 | Breaking the collector into smaller, modular packages allows for independent stabilization and versioning of components.                                          |
|   9 | Experimental functionality is separated into distinct modules prefixed with 'x' to clearly indicate pre-1.0 status and potential instability.                     |
|  10 | Stable APIs use the options pattern to allow users to opt into experimental features explicitly without affecting core stability.                                 |
|  11 | The contrib repository serves as a testbed for API changes, providing visibility into ecosystem usage and helping identify potential breakages.                   |
|  12 | Feature gates are used to decouple breaking changes from application upgrades, allowing users to migrate at their own pace.                                       |
|  13 | Feature gates follow a Kubernetes-like model with alpha, beta, and stable stages to manage the rollout of changes.                                                |
|  14 | A significant breaking change involved changing default server addresses from all interfaces to localhost for security, managed via feature gates.                |
|  15 | Configuration defaults involve a trade-off between user burden and the risk of breaking changes, with defaults potentially set at higher levels like Helm charts. |
|  16 | Fine-grained stability levels (in development, alpha, beta, stable) are used to express trust and production readiness beyond semantic versioning.                |
|  17 | Automatic migration tools for configuration schemas are proposed to reduce the cost of unavoidable breaking changes.                                              |
|  18 | The "SER trick" from Rust is suggested for Go to maintain compatibility for unchanged types across major versions by aliasing v1 types to v2.                     |
|  19 | A tool similar to Rust's Crater is proposed to test breaking changes against all public packages in the ecosystem.                                                |
|  20 | Automated CI checks for breaking changes are desired to reduce reliance on manual code review, with tools like API diff needing updates for Go generics.          |
|  21 | Schema versions in configuration files are considered necessary for implementing automatic migration paths between major versions.                                |

# Video

[![Video thumbnail](https://img.youtube.com/vi/3CDhFk-VB-o/hqdefault.jpg)](https://www.youtube.com/watch?v=3CDhFk-VB-o)

[Watch on YouTube](https://www.youtube.com/watch?v=3CDhFk-VB-o)
