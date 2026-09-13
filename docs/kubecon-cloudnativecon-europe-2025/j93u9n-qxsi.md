---
layout: default
title:
  "Don't Let Your Kubernetes Cluster Go Wild: Ensuring Etcd Reli... Arka Saha
  & Chun-Hung (Henry) Tseng"
nav_order: 75
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  The ATC (Aerospike Time-Series Database) team presents a robustness test
  framework to ensure the consistency of their distributed key-value store. The framework
  generates random valid input, simulates race conditions, and injects failures t...
resource: https://www.youtube.com/watch?v=J93U9n_qxSI
tags:
  - kubecon-cloudnativecon-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The ATC (Aerospike Time-Series Database) team presents a robustness test framework to ensure the consistency of their distributed key-value store.
The framework generates random valid input, simulates race conditions, and injects failures to test the system's behavior under various scenarios.
It uses tools like Goofail, LazyFS, and network proxy to introduce errors and collects output from both client and server sides.
The robustness test also leverages a state machine to verify intermediate states and a linearizability checker to ensure consistency.
The team plans to integrate anti-thesis integration to improve the test suite and explore more formal proof verification tools in the future.

# Main Points

|   # | Main point |
| --: | ---------- |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=J93U9n_qxSI)
