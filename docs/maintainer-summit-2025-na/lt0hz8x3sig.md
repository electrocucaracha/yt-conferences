---
layout: default
title: "Taming the Beast: The Move To Declarative API Validation in Kubernetes - Yongrui Lin, Google"
nav_order: 14
parent: "Maintainer Summit 2025 - NA"
type: Video Note
description: "This presentation by Yong Ling from Google introduces a project to move API validation in Kubernetes from hidden, handwritten Go code to declarative tags attached directly to API fields."
resource: "https://www.youtube.com/watch?v=Lt0HZ8X3sig"
tags:
  - maintainer-summit-2025-na
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-16T17:23:58+00:00
---

# Summary

This presentation by Yong Ling from Google introduces a project to move API validation in Kubernetes from hidden, handwritten Go code to declarative tags attached directly to API fields.
The initiative addresses the significant burden on users, who face opaque validation errors, and maintainers, who struggle with reviewing complex, duplicated validation logic across over 19,000 lines of code.
By using a new tool called validation-gen, developers can define rules using simple, self-documenting tags that automatically generate optimized Go code, making the API definition machine-readable and significantly reducing review toil.
The project employs a safe migration strategy involving parallel execution of old and new validation logic to ensure equivalence, along with feature gates and tag stability levels (alpha, beta, stable) to manage backward compatibility and risk.
Contributors are encouraged to adopt these declarative tags for new APIs and migrate existing ones, with the long-term goal of achieving "declarative validation only" APIs that eliminate the need for legacy handwritten validation code entirely.

# Main Points

|   # | Main point                                                                                                                                                                                                                                   |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The project aims to move Kubernetes API validation logic from hidden Go code into explicit API field tags to improve transparency for users and reduce review toil for maintainers.                                                          |
|   2 | Current validation involves 19,000 lines of handwritten imperative Go code duplicated across over 20 files, creating hidden logic that is difficult to understand and maintain.                                                              |
|   3 | The solution introduces a tool called validation-gen that parses Go struct tags to automatically generate optimized validation code, making API definitions self-documenting and machine-readable.                                           |
|   4 | Supported validation tags include simple rules like required and optional, value constraints like minimum and maximum, and complex semantic rules like immutable, one-of, and items for cross-field validation.                              |
|   5 | The generated code includes regression logic to ensure backward compatibility, allowing existing objects with invalid values under new rules to remain valid if the specific field is not being updated.                                     |
|   6 | Tag stability is managed through alpha, beta, and stable phases, with no tags currently promoted to stable in Kubernetes 1.35 to ensure safety for production environments.                                                                  |
|   7 | Two feature gates control the rollout: declarative-validation enables parallel execution of generated and handwritten code, while declarative-validation-takeover allows generated code to override handwritten results for migrated fields. |
|   8 | A migration strategy involves proving equivalence between generated and handwritten validation in phases 1 and 2, followed by graduating beta tags and adopting declarative-only APIs for new types.                                         |
|   9 | Contributors are encouraged to use declarative validation tags for new APIs and to migrate existing handwritten validation code, which serves as a good first issue for new community members.                                               |
|  10 | The project seeks to align validation tags between native Kubernetes types and Custom Resource Definitions (CRDs) to create a consistent set of annotations across both API styles.                                                          |
|  11 | Complex validations that cannot be expressed with simple tags, such as discriminated unions, may still require Cell expressions or handwritten code, though the goal is to minimize these cases.                                             |
|  12 | The team maintains a dev branch for experimenting with new tags and uses markers in handwritten code to track which fields have already been migrated to declarative validation.                                                             |
|  13 | Future work includes integrating declarative validation understanding into the kube-api-linter project to bridge the gap between different API definition methods like CRDs and native types.                                                |
|  14 | Specific use cases like monotonic increase validation are identified as potential candidates for new tags, with the team open to adding tags as concrete use cases emerge from the community.                                                |

# Video

[![Video thumbnail](https://img.youtube.com/vi/Lt0HZ8X3sig/hqdefault.jpg)](https://www.youtube.com/watch?v=Lt0HZ8X3sig)

[Watch on YouTube](https://www.youtube.com/watch?v=Lt0HZ8X3sig)
