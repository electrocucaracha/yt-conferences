---
layout: default
title: "GopherCon 2025: Strategies for Auto-Instrumenting Go Applications Without Code Changes - Hannah Kim"
nav_order: 6
parent: GopherCon 2025
type: Video Note
description: "Hannah, a software engineer at DataDog, presents a talk on auto-instrumentation strategies for Go applications that require no manual code changes."
resource: "https://www.youtube.com/watch?v=VytHjiN_un0"
youtube_stats:
  view_count: 1289
  like_count: 45
  channel_subscriber_count: 41100
tags:
  - gophercon-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-21T05:22:37+00:00
---

# Summary

Hannah, a software engineer at DataDog, presents a talk on auto-instrumentation strategies for Go applications that require no manual code changes.
She defines instrumentation as the process of collecting telemetry—logs, metrics, and traces—to answer questions about application performance and user behavior.
The presentation distinguishes between two primary approaches: runtime instrumentation, which often uses eBPF to hook into the kernel and may require source code adjustments, and compile-time instrumentation, which integrates instrumentation code during the build process without touching the kernel.
To compare these methods, Hannah conducts a live benchmark using a simple HTTP endpoint with database interactions, testing scenarios with no instrumentation, manual instrumentation, eBPF-based runtime instrumentation, and DataDog’s Orchestrion compile-time approach.
The results indicate that both auto-instrumentation methods introduce minimal performance overhead compared to the baseline, with compile-time instrumentation offering advantages in stability, security, and portability by avoiding privileged kernel access and Linux-specific dependencies.
The talk concludes by highlighting upcoming developments such as Go’s flight recording feature and the Go compile-time instrumentation SIG, encouraging the community to adopt automated telemetry solutions for better application observability.

# Main Points

|   # | Main point                                                                                                                                                            |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Hannah, a software engineer at Data Dog with one year of experience, presented on auto-instrumentation strategies for Go applications at GoCon.                       |
|   2 | Instrumentation is the process of collecting telemetry to answer questions about application performance, user behavior, and errors.                                  |
|   3 | Telemetry consists of three main pillars: logs (what is happening), metrics (how much and how quickly), and traces (the how of what is happening).                    |
|   4 | Auto-instrumentation is the act of instrumenting code to generate telemetry without making manual code changes.                                                       |
|   5 | Two primary types of auto-instrumentation are defined: runtime instrumentation and compile-time instrumentation.                                                      |
|   6 | Runtime instrumentation often requires source code changes, which is challenging for Go due to its static compilation nature.                                         |
|   7 | Compile-time instrumentation occurs during the build process and never requires source code changes, making it compatible with Go.                                    |
|   8 | EBPF (Extended Berkeley Packet Filter) is a common runtime approach that uses kernel hooks to divert processes into tracing code.                                     |
|   9 | Binary trampolining is an eBPF technique where execution jumps to a different address to call tracing code before returning.                                          |
|  10 | Orchestrion is a compile-time instrumentation project developed by Data Dog that uses the `tool exec` flag to attach instrumentation to the compiler.                 |
|  11 | The presentation compared OpenTelemetry's eBPF approach (runtime) with Orchestrion (compile-time) using a simple HTTP endpoint and database setup.                    |
|  12 | Benchmarks included average load testing and spike testing, with error rates and request latencies measured via a Grafana dashboard.                                  |
|  13 | Results showed that both auto-instrumentation approaches added minimal overhead, with latencies comparable to manual instrumentation and the uninstrumented baseline. |
|  14 | Compile-time instrumentation is considered more stable than eBPF because it does not rely on brittle kernel address hooking.                                          |
|  15 | Compile-time instrumentation is more secure than eBPF because it does not require privileged kernel access, reducing the risk of malicious exploitation.              |
|  16 | Compile-time instrumentation is more portable as it only requires the ability to compile code, whereas eBPF requires a Linux kernel.                                  |
|  17 | The Go 25 release introduced flight recording, which continuously captures a sliding window of traces for automatic analysis during events like panics.               |
|  18 | A compile-time instrumentation Special Interest Group (SIG) is being formed by OpenTelemetry, Data Dog, and Alibaba to create a universal library.                    |
|  19 | The speaker encourages developers to adopt instrumentation for better application visibility and to contribute to open-source auto-instrumentation projects.          |

# Video

[![Video thumbnail](https://img.youtube.com/vi/VytHjiN_un0/hqdefault.jpg)](https://www.youtube.com/watch?v=VytHjiN_un0)

[Watch on YouTube](https://www.youtube.com/watch?v=VytHjiN_un0)
