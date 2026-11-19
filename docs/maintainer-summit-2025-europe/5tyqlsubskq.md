---
layout: default
title: "Custom Resource Definitions: Let's Talk About Versioning and Releases - Nick Young, Isovalent"
nav_order: 13
parent: "Maintainer Summit 2025 - Europe"
type: Video Note
description: "This presentation explores the complexities of versioning and releasing Custom Resource Definitions (CRDs) in Kubernetes, distinguishing between implementation-specific CRDs, which are tightly coup..."
resource: "https://www.youtube.com/watch?v=5TYqlsubsKQ"
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

This presentation explores the complexities of versioning and releasing Custom Resource Definitions (CRDs) in Kubernetes, distinguishing between implementation-specific CRDs, which are tightly coupled to controllers, and upstream CRDs like Gateway API, which are developed as community specifications.
The speaker emphasizes that safe API changes require "round-trip" compatibility, ensuring that objects can be converted between versions without data loss, a challenge that is significantly more difficult for upstream CRDs due to the decoupling of the API specification from controller implementations.
To manage this, Gateway API employs a "channel" system with standard and experimental install manifests, allowing cluster owners to opt into unstable features while maintaining a stable core, though this approach introduces friction for implementations and users when features are promoted or changed.
The team is currently transitioning new experimental objects to a separate API group prefixed with "x-" to allow safe coexistence and removal of experimental resources, a deliberate trade-off that increases implementation overhead to prevent breaking changes in production environments.
Future work includes exploring Validating Admission Policies to restrict experimental fields in standard channels and addressing the "dead fields" problem, where persisted data from removed experimental features may unexpectedly reappear, while acknowledging that these solutions are iterative improvements rather than perfect fixes.

# Main Points

|   # | Main point                                                                                                                                                                                                                       |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | API changes in Kubernetes Custom Resource Definitions are complex due to the need for safe storage version conversion and round-trip compatibility.                                                                              |
|   2 | CRD deployments are classified as implementation-specific, which simplifies versioning through tight coupling with controllers, or upstream, which increases complexity by decoupling the specification from the implementation. |
|   3 | Key versioning concepts include the API version, schema version, and storage version, with the storage version being critical for safely persisting data to etcd.                                                                |
|   4 | A fundamental requirement for safe API changes is that objects must be round-trip capable, meaning data can be converted between versions without loss of information.                                                           |
|   5 | An API change may be round-trip capable in theory, but specific objects using new features may become non-round-trip capable if those features cannot be represented in older schema versions.                                   |
|   6 | Traditional feature flags are not feasible for upstream CRDs because fields cannot be defined but disabled, requiring alternative mechanisms to manage experimental functionality.                                               |
|   7 | Gateway API approximates feature flags using two installation channels: standard, which contains only stable objects and fields, and experimental, which includes all fields and objects.                                        |
|   8 | Moving from the standard to the experimental channel is safe because experimental is a superset of standard, allowing users to opt into new features without breaking existing configurations.                                   |
|   9 | Moving from the experimental to the standard channel is unsafe because experimental features may be broken or changed, potentially causing data loss or functional issues for users relying on them.                             |
|  10 | Managed Kubernetes providers often restrict the use of the experimental channel to prevent users from encountering breaking changes or unstable features.                                                                        |
|  11 | Adding new experimental objects to the standard API group creates risks, such as the dead fields problem, where data persists in etcd and may unexpectedly reappear after rollbacks.                                             |
|  12 | To mitigate these risks, Gateway API is moving new experimental objects to a separate API group prefixed with 'x', such as x-k8s.io, to enforce deliberate adoption and safe removal.                                            |
|  13 | This approach introduces overhead for implementations, requiring code refactoring when features move from experimental to standard, but ensures that standard channel objects remain stable and safe.                            |
|  14 | The separation allows clusters to run standard and experimental objects simultaneously, enabling safe transitions and easier cleanup of experimental resources.                                                                  |
|  15 | Future work includes using Validating Admission Policies to prevent the use of experimental fields in the standard channel, enhancing stability and preventing accidental usage.                                                 |
|  16 | The current approach avoids the operational burden of conversion webhooks, which are difficult to maintain and often ignored by implementations, by relying on built-in CRD specification features.                              |
|  17 | The goal is to make the standard channel as stable as possible, ensuring that users can rely on it without fear of breaking changes, while treating the experimental channel as inherently unstable.                             |
|  18 | This strategy is intended to prepare Gateway API for potential default installation in Kubernetes, requiring a robust and secure versioning model that minimizes risk for end users.                                             |

# Video

[![Video thumbnail](https://img.youtube.com/vi/5TYqlsubsKQ/hqdefault.jpg)](https://www.youtube.com/watch?v=5TYqlsubsKQ)

[Watch on YouTube](https://www.youtube.com/watch?v=5TYqlsubsKQ)
