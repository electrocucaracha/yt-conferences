---
layout: default
title: "Techniques and Insights To Test Kubernetes Limits With Kind - Antonio Ojea & Katarzyna Lach, Google"
nav_order: 18
parent: "Maintainer Summit 2025 - Europe"
type: Video Note
description: "This presentation demonstrates how to use Kind (Kubernetes in Docker) for debugging scalability and performance issues by leveraging Kubernetes APIs to emulate large-scale environments without requ..."
resource: "https://www.youtube.com/watch?v=HcTcxwkKg2E"
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

This presentation demonstrates how to use Kind (Kubernetes in Docker) for debugging scalability and performance issues by leveraging Kubernetes APIs to emulate large-scale environments without requiring physical clusters.
The speakers explain that scalability is a multi-dimensional problem, and Kind allows developers to isolate specific components, such as DNS resolution or network data path programming, by mocking endpoints and services.
A key use case involves identifying a bug in the Go resolver library where large DNS responses were mishandled, which was successfully reproduced and verified using a minimal Kind cluster with fake IP endpoints.
Another case study compares the performance of kube-proxy in iptables mode versus nftables mode, showing that nftables significantly reduces programming latency and CPU usage when handling tens of thousands of endpoints.
The session concludes by emphasizing that while Kind is an essential tool for rapid iteration and regression testing, it is not a substitute for production-scale testing, as its high-speed, buffered environment may mask latency-related issues that only appear in real-world, slower systems.

# Main Points

|   # | Main point                                                                                                                                                                                                                         |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Performance is defined as system deficiency measured by low latency or high throughput, while scalability is the capacity to grow while maintaining or improving performance.                                                      |
|   2 | Scalability is a multi-dimensional problem where limits depend on interacting factors like namespaces, pods per second, and services, making debugging complex due to many interacting components.                                 |
|   3 | Common anti-methodologies for debugging include assuming network issues from timeouts, blindly applying tools, random changes, and relying solely on benchmarking results without context.                                         |
|   4 | Kubernetes architecture uses APIs and interfaces for all components, allowing tools like kind to mock these interfaces and emulate large clusters without needing physical hardware.                                               |
|   5 | Kind enables the creation of minimal clusters with fake objects, such as 10,000 node objects or endpoint slices, to test scalability problems on a laptop.                                                                         |
|   6 | Effective use of kind requires breaking down complex problems into isolated pieces and identifying specific APIs to emulate, which demands a deep understanding of Kubernetes internals.                                           |
|   7 | A DNS resolution issue was identified where the Go resolver mishandled truncated bits in responses from headless services with many endpoints, a bug fixed in Go 1.23.                                                             |
|   8 | This DNS issue was reproduced using kind by creating a headless service with fake IP endpoints and testing resolution with different Go versions to isolate the library bug.                                                       |
|   9 | Kube-proxy performance was tested by comparing iptables and nftables modes, revealing that iptables suffers from high programming latency due to linear search and rule copying.                                                   |
|  10 | In the kube-proxy test, creating a service with 50,000 endpoints caused iptables to consume high CPU and timeout, while nftables completed the data path programming significantly faster.                                         |
|  11 | Kind allows easy switching between different cluster configurations, such as iptables and nftables modes, using kubectl contexts to compare performance without affecting other clusters.                                          |
|  12 | Kind is a necessary but not sufficient condition for release testing because it simulates a perfect scenario with low latency and high throughput, which may hide issues that occur in slower, real-world production environments. |
|  13 | Real-world scalability problems often involve kernel limits, network drivers, and external API dependencies that only manifest when systems are large and slow, which kind may not replicate.                                      |
|  14 | Users should define specific Service Level Indicators (SLIs) and understand the metrics they aim to optimize before running tests to ensure results are meaningful and not just environment-specific.                              |
|  15 | Kind is versatile for CI/CD pipelines, such as GitHub Actions, where it can spin up clusters for functional testing and regression checks of controllers and components.                                                           |
|  16 | The key takeaway is that kind allows for rapid, isolated reproduction of specific scalability and performance issues, but it must be used with a clear understanding of the problem being tested.                                  |

# Video

[![Video thumbnail](https://img.youtube.com/vi/HcTcxwkKg2E/hqdefault.jpg)](https://www.youtube.com/watch?v=HcTcxwkKg2E)

[Watch on YouTube](https://www.youtube.com/watch?v=HcTcxwkKg2E)
