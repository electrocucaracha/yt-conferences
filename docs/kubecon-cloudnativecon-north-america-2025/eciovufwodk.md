---
layout: default
title: Bringing OCI Into the GitOps World - Jesse Suen, Akuity
nav_order: 28
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  The speaker discusses how Open Container Initiative (OCI) is becoming
  a universal distribution format for cloud-native artifacts, expanding beyond its
  original purpose of making Docker images portable and consistent across runtimes.
  OCI ena...
resource: https://www.youtube.com/watch?v=eCIovuFwodk
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

The speaker discusses how Open Container Initiative (OCI) is becoming a universal distribution format for cloud-native artifacts, expanding beyond its original purpose of making Docker images portable and consistent across runtimes.
OCI enables the deployment of various types of cloud-native artifacts, such as Helm charts, WM modules, Lambda functions, policy bundles, and machine learning models, from OCI registries instead of Git repositories.
This allows for immutable deployments, improved performance and redundancy in air-gapped networks or offline clusters, and enhanced collaboration through versioning and packaging.
However, there are trade-offs between using Git and OCI, including differences in versioning, security, and delivery.
The speaker presents two workflows: one mimicking the existing GitOps workflow with OCI, and another that goes fully immutable by utilizing tools like Cargo to set the target revision explicitly.

# Main Points

|   # | Main point |
| --: | ---------- |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=eCIovuFwodk)
