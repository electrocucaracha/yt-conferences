---
layout: default
title:
  "Feature Flag Driven Development: Seamlessly Integrate Feature Flags... Kris
  Coleman & Michael Beemer"
nav_order: 74
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  Chris Coleman from Testify SAC discussed feature flag-driven development,
  a solution to improve the adoption process of feature flags in software delivery
  life cycles. Feature flags allow for runtime control, progressive rollouts, experimen...
resource: https://www.youtube.com/watch?v=YjAgUlhBV90
tags:
  - kubecon-cloudnativecon-north-america-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Chris Coleman from Testify SAC discussed feature flag-driven development, a solution to improve the adoption process of feature flags in software delivery life cycles.
Feature flags allow for runtime control, progressive rollouts, experimentation, precise targeting, and separation of deployments from releases.
However, traditional approaches can lead to issues like runtime errors, typos, and context switching.
To address this, Chris introduced the concept of a "flag manifest," a simple list of feature flags with default values, descriptions, and types.
This declarative approach treats feature flags as first-class citizens in software delivery life cycles, generating type-safe code bindings and validating flag configurations in CI processes.
The open feature CLI can be used to create and manage flag manifests, and the open feature GitHub action can automate flag creation upon pull request merge.
Future directions include adding generated aspects, local flag overrides, and support for more languages and MCP integrations.

# Main Points

|   # | Main point |
| --: | ---------- |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=YjAgUlhBV90)
