---
layout: default
title:
  "Freedom Through Boundaries: Building Configurations That Age Well - Bogdan
  Stancu, Adobe"
nav_order: 113
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Bogdan, from Adobe's observability team, discusses the importance of
  building configuration management systems that "age well" by establishing clear
  boundaries and best practices. Using the analogy of training his dog to illustrate
  how boun...
resource: https://www.youtube.com/watch?v=H1g0jnmjJN8
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

Bogdan, from Adobe's observability team, discusses the importance of building configuration management systems that "age well" by establishing clear boundaries and best practices.
Using the analogy of training his dog to illustrate how boundaries enable greater freedom, he describes how configuration sprawl and complexity can result from continually saying yes to user requests without a guiding specification.
He highlights common pitfalls such as silent failures, mutually exclusive options, lack of documentation, and over-accommodation of advanced users, which can lead to unmanageable and confusing configurations.
Bogdan recommends maintaining an up-to-date specification, enforcing validation, designing for user outcomes rather than internal convenience, and treating backward compatibility as a limited resource.
In the Q&A, he emphasizes the need to justify the cost of good practices through governance, balance flexibility with sensible defaults, and communicate clear boundaries and support levels to users, focusing on the needs of the majority while allowing advanced users some unsupported flexibility.

# Main Points

|   # | Main point                                                                                                          |
| --: | ------------------------------------------------------------------------------------------------------------------- |
|   1 | Building configurations that age well requires setting boundaries and rules for users.                              |
|   2 | Drawing analogy between dog training (setting boundaries for freedom) and configuration management.                 |
|   3 | Example based on Helm charts for Kubernetes, focusing on deploying three sets of collectors.                        |
|   4 | Initial configuration works but quickly becomes complex as exceptions are made for individual user requests.        |
|   5 | Multiple ways to handle secrets were added due to user and security demands, leading to increased complexity.       |
|   6 | Internal features exposed to users can become permanent, even if not intended for public use.                       |
|   7 | Over time, constant "yes" to user requests leads to bloated, unmanageable configurations (e.g., 1500-line configs). |
|   8 | Mutually exclusive configuration options can cause confusion if not validated or enforced.                          |
|   9 | Reluctance to remove old options prevents breaking changes and version upgrades.                                    |
|  10 | Lack of proper testing, documentation, changelogs, and release notes leads to user confusion and blame.             |
|  11 | Key lessons:                                                                                                        |
|  12 | Always create and update a product specification.                                                                   |
|  13 | Enforce boundaries and reject changes not aligned with the spec.                                                    |
|  14 | Mutually exclusive options should fail validation.                                                                  |
|  15 | Design configuration for users, not maintainers; avoid exposing internals.                                          |
|  16 | Defaults should be explicit and visible to users.                                                                   |
|  17 | Same config should always yield the same outcome unless a major version changes.                                    |
|  18 | Document breaking changes and provide migration paths.                                                              |
|  19 | Treat backward compatibility as a budget; deprecate unused features.                                                |
|  20 | Comprehensive testing is essential; CI time is less important than reliability.                                     |
|  21 | Validate configs strictly; fail on typos or unexpected fields.                                                      |
|  22 | Make upgrades predictable and "boring" to encourage adoption.                                                       |
|  23 | Allow advanced users flexibility, but clarify unsupported options.                                                  |
|  24 | Focus on supporting the majority of users; rare needs can be handled separately.                                    |
|  25 | Saying "no" to user requests requires clear explanations and boundaries.                                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=H1g0jnmjJN8)
