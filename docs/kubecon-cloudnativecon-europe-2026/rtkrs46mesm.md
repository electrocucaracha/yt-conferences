---
layout: default
title:
  "The Missing Half of Performance Profiling: Understanding Memory in Cloud Native
  Syste... Dom Delnano"
nav_order: 363
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The speaker introduces the topic of memory profiling in cloud-native
  systems, highlighting its importance alongside traditional CPU profiling for understanding
  and debugging performance issues. They review the evolution of profiling tools...
resource: https://www.youtube.com/watch?v=rTkrS46meSM
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

The speaker introduces the topic of memory profiling in cloud-native systems, highlighting its importance alongside traditional CPU profiling for understanding and debugging performance issues.
They review the evolution of profiling tools, from early CPU profilers requiring recompilation to modern, always-on continuous profilers, and explain key memory concepts such as stack and heap allocations using a sample C program.
The talk covers various memory profiling techniques—allocation sampling, in-use profiling, full heap dumps, and object introspection—detailing their trade-offs in overhead and use cases, and discusses tools like Parka, Pyroscope, and Pixie that implement these methods.
The speaker notes that while CPU profiling is mature and standardized, memory profiling remains fragmented, with sampling-based approaches like those using the PROF format offering a good balance of insight and low overhead for production use.
Finally, they emphasize that as AI and cloud architectures evolve to include more complex memory hierarchies and device memory, understanding and profiling memory usage will become increasingly critical.

# Main Points

|   # | Main point                                                                                                                                                |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presenter has six years of experience in the eBPF space, mainly with CNCF Pixie and currently works at Gimlet Labs.                                       |
|   2 | Debugging slow programs has been a persistent challenge since early computing.                                                                            |
|   3 | Performance profiling began with CPU profiling, starting with tools like GPROF in the 1980s-90s, which required recompilation and had high overhead.      |
|   4 | Sampling profilers like Perf in the 2000s-2010s reduced overhead and expanded scope to single hosts.                                                      |
|   5 | Continuous profilers now provide always-on profiling across fleets, improving accessibility and scope.                                                    |
|   6 | Memory issues, such as creeping usage and pod restarts in Kubernetes, are hard to diagnose with static metrics alone.                                     |
|   7 | Understanding program memory involves stack and heap allocations, with metrics like total allocations, object representation, and in-use metrics.         |
|   8 | Allocation sampling profiles memory by sampling allocations, identifying hotspots, and capturing call stacks; used in tools like gopro, g-perf, tcmalloc. |
|   9 | In-use profiling tracks memory still allocated, helping detect leaks; often paired with allocation sampling.                                              |
|  10 | Full heap dumps provide a complete memory snapshot but have high overhead and pause the program; used in tools like Valgrind and JVM heap dumps.          |
|  11 | Object introspection analyzes container types to optimize stack vs. heap allocations; pioneered by Meta and being explored by Pixie.                      |
|  12 | The PROF format is a standard for profiling data, supporting CPU and memory profiles, and enables visualization of allocation-heavy code.                 |
|  13 | Parka supports PROF format, provides allocation sampling and in-use profiling, and supports Go, Rust, Python, and Node.js.                                |
|  14 | Pyroscope uses an SDK push model for profiling, supports Go, Java, and .NET, and provides temporal allocation views and flame graphs.                     |
|  15 | Pixie is developing memory profiling, supports dynamic instrumentation, and is prototyping object introspection for optimizing memory footprint.          |
|  16 | Allocation sampling and in-use profiling are low overhead and widely support                                                                              |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=rTkrS46meSM)
