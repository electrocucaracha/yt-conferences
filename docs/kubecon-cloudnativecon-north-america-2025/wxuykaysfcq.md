---
layout: default
title:
  "Fast and the Furious: CICD Pipeline for eBPF Programs at Meta S... Theophilus
  Benson & Prankur Gupta"
nav_order: 73
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  The presentation discusses the challenges and solutions involved in building
  a fast and reliable CI/CD pipeline for eBPF programs at Meta’s scale. The speaker
  outlines the complexity of managing and deploying numerous eBPF programs across
  d...
resource: https://www.youtube.com/watch?v=wXuykaYSFCQ
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

The presentation discusses the challenges and solutions involved in building a fast and reliable CI/CD pipeline for eBPF programs at Meta’s scale.
The speaker outlines the complexity of managing and deploying numerous eBPF programs across diverse kernel versions, hardware, and services, emphasizing that most of Meta’s eBPF programs actively modify packet and connection states rather than just monitoring them.
The talk details Meta’s multi-stage testing pipeline—including unit tests, integration tests, production simulations, and mini-production releases—to ensure safe and effective rollouts, while highlighting the difficulties posed by kernel heterogeneity, overlapping attach points, and multiple teams managing their own eBPF programs.
To address these, Meta developed specialized tools for testing, observability, and rapid mitigation, such as decoupling control and data planes, building custom chaining and monitoring solutions, and implementing auditors to validate rollout intent.
The speaker concludes that eBPF pipelines require tailored infrastructure and continuous evolution to handle the high variability and potential blast radius of changes, stressing the importance of robust tooling for both deployment confidence and quick recovery.

# Main Points

|   # | Main point                                                                                                                                   |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation covers CI/CD pipeline for eBPF programs at Meta's scale                                                                         |
|   2 | Meta's net binary manages and deploys eBPF programs for packet/connection tuning and congestion control                                      |
|   3 | Majority of Meta's eBPF programs actively change packet/connection state, not just monitor                                                   |
|   4 | eBPF adoption driven by performance wins: 40% P99 latency improvement, 30% faster image generation, 100% faster storage read (older metrics) |
|   5 | eBPF deployed on 99% of Meta machines; at least two versions rolled out monthly                                                              |
|   6 | eBPF enables dynamic, safe, efficient kernel customization without kernel changes/reboots                                                    |
|   7 | eBPF consists of kernel verifier (ensures safety) and JIT compiler (improves performance)                                                    |
|   8 | Attach points/hook points connect eBPF to kernel (e.g., TC, XDP, cgroup, syscalls, tracepoints)                                              |
|   9 | eBPF maps enable fast data sharing and communication between programs and user space                                                         |
|  10 | Example issue: combination of stacking, jumbo frames, and multiple eBPF programs caused five distinct service issues                         |
|  11 | eBPF changes can have large, hard-to-triage blast radius; robust observability and fast mitigation tools are essential                       |
|  12 | Meta uses a multi-stage CI/CD pipeline:                                                                                                      |
|  13 | Unit testing: isolated, controlled, tests BPF interfaces and code paths, but alert thresholds are challenging                                |
|  14 | Integration testing: coexistence testing of multiple features on diverse dedicated servers                                                   |
|  15 | Production simulation: tests production-like setups with shadow workloads and compatibility with other teams' binaries                       |
|  16 | Mini production release: daily rollout to thousands of servers for AB testing and regression detection                                       |
|  17 | Kernel and service heterogeneity (many kernel versions, diverse attach points) present unique challenges                                     |
|  18 | Multiple teams manage BPF programs; attach order and program interactions can cause unpredictable behavior                                   |
|  19 | Developed internal tools for dynamic map naming, program chaining, monitoring, and priority enforcement                                      |
|  20 | Observability: decoupled metric collection/export, external services for exporting BPF coun                                                  |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=wXuykaYSFCQ)
