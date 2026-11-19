---
layout: default
title: "Simplifying API Review - A Tool Based Approach for Kubernetes and Beyond - Bryce Palmer & Joel Speed"
nav_order: 16
parent: "Maintainer Summit 2025 - NA"
type: Video Note
description: "Bryce and Joel discuss the complexities of Kubernetes API reviews, highlighting the need to balance consistency, backward compatibility, and end-user usability against over 2,200 lines of establish..."
resource: "https://www.youtube.com/watch?v=2Bz-vtIBQlc"
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

Bryce and Joel discuss the complexities of Kubernetes API reviews, highlighting the need to balance consistency, backward compatibility, and end user usability against over 2,200 lines of established conventions.
They explain that manual reviews are difficult due to intricate serialization rules, versioning constraints, and the risk of breaking existing client workflows.
To address these challenges, they introduce two new tools: kube-api-lint, a static analysis plugin that enforces mechanical API conventions, and certify, a standalone binary that detects potentially breaking schema changes and versioning incompatibilities.
Both projects aim to automate routine checks, allowing reviewers to focus on higher-level design and user experience issues.
The speakers invite the community to contribute to these tools, which are currently in early development, to help standardize API quality across the Kubernetes ecosystem.

# Main Points

|   # | Main point                                                                                                                         |
| --: | ---------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Bryce and Joel discuss API review challenges and new tools for Kubernetes and OpenShift.                                           |
|   2 | API reviews ensure consistency, prevent breaking changes, and improve end user usability based on 2200 lines of conventions.       |
|   3 | Reviewers require deep knowledge of API patterns, client impacts, and rapid ramp-up on new features.                               |
|   4 | Implementation considerations include consistency, serialization, and avoiding past mistakes like using Go durations or booleans.  |
|   5 | Schema considerations involve invalidation of valid values, client expectations, and strict versioning guidelines.                 |
|   6 | Serialization complexity arises from pointers, zero values, and differences between CRDs and built-in types.                       |
|   7 | Kube API Lint is a Go plugin that automates mechanical checks like comments, list types, and serialization rules.                  |
|   8 | Kube API Lint allows projects to self-service API reviews, freeing reviewers to focus on user experience.                          |
|   9 | Certify is a standalone binary that codifies schema change compatibility based on Kubernetes API conventions.                      |
|  10 | Certify checks for breaking changes in validations and ensures data roundtrips without loss during versioning.                     |
|  11 | Both tools originated from discussions in Salt Lake City and are used by projects like Cluster API and Operator Lifecycle Manager. |
|  12 | The team aims for 0.10 releases and seeks community feedback to fix bugs and improve rule coverage.                                |
|  13 | Tim highlights that strictly speaking, every API change is breaking, requiring careful risk assessment for readers and writers.    |
|  14 | The team discusses the importance of preserving unknown fields to help backward-compatible clients detect new features.            |
|  15 | Advanced validations like CEL are difficult to analyze statically, so tools may flag changes for manual review.                    |
|  16 | The goal is to move toward declarative validation to reduce reliance on complex CEL rules.                                         |
|  17 | Differences between CRD and built-in type behaviors, such as optional versus required fields, need reconciliation.                 |
|  18 | The team encourages users to open issues for missing rules or bugs in Kube API Lint and Certify.                                   |

# Video

[![Video thumbnail](https://img.youtube.com/vi/2Bz-vtIBQlc/hqdefault.jpg)](https://www.youtube.com/watch?v=2Bz-vtIBQlc)

[Watch on YouTube](https://www.youtube.com/watch?v=2Bz-vtIBQlc)
