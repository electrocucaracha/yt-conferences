---
layout: default
title: "GopherCon 2025: Go Plays Nice With Your Computer - Race Detection and Freedom! - Raghav Roy"
nav_order: 8
parent: GopherCon 2025
type: Video Note
description: "Ragavoy, a UCL student researching formal methods, explains how Go’s memory model guarantees sequentially consistent execution for data-race-free code, a concept known as DRFSC."
resource: "https://www.youtube.com/watch?v=-jZrRXlPsy8"
youtube_stats:
  view_count: 1590
  like_count: 50
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

Ragavoy, a UCL student researching formal methods, explains how Go’s memory model guarantees sequentially consistent execution for data-race-free code, a concept known as DRFSC.
To enforce this, Go utilizes a race detector based on ThreadSanitizer (TSAN), which employs vector clocks to model causality and identify concurrent memory accesses that lack a "happens-before" relationship.
The speaker draws an analogy between vector clocks and Minkowski light cones to illustrate how events in distributed systems are partially ordered, allowing the detector to distinguish between causal dependencies and true concurrency.
A significant update in Go 1.19 introduced TSAN v3, which removes the previous limit of 8,000 concurrent goroutines and improves performance by replacing spin locks with lock-free data structures.
Benchmarking results demonstrate that TSAN v3 is approximately six times faster than its predecessor, significantly reducing runtime overhead while maintaining accurate race detection capabilities.

# Main Points

|   # | Main point                                                                                                                                                             |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker is a UCL student researching formal methods and applying them to the Go compiler and runtime.                                                              |
|   2 | Multi-processor systems break the assumption that valid optimizations are invisible to valid programs, causing visibility issues in multi-threaded code.               |
|   3 | Hardware-specific behaviors, such as instruction reordering on ARM versus x86, lead to unpredictable results in concurrent programs.                                   |
|   4 | A memory model serves as a contract between programmers, compilers, and hardware to define deterministic program results.                                              |
|   5 | Sequentially consistent (SC) memory models ensure that multi-processor execution behaves as if it were on a single processor, preserving instruction order per thread. |
|   6 | Go guarantees data race-free sequential consistency (DRFSC), meaning race-free programs behave as if they are sequentially consistent.                                 |
|   7 | The happens-before relationship formalizes synchronization, allowing deterministic ordering of events across threads via transitivity.                                 |
|   8 | The Go race detector identifies data races by checking for conflicting memory accesses that are not ordered by a happens-before relationship.                          |
|   9 | Time is a partial order where not all events can be ordered relative to each other, a concept derived from Einstein's speed of light limit.                            |
|  10 | Minkowski light cones model causality, defining past, future, and elsewhere regions where events are causally disconnected.                                            |
|  11 | Lamport clocks fail to capture concurrency because they impose a total order on events that may be causally unrelated.                                                 |
|  12 | Vector clocks solve this by using multi-dimensional clocks per goroutine to accurately track causal dependencies and identify concurrent events.                       |
|  13 | Race detection using vector clocks identifies races when clock values are not strictly ordered, indicating events are in each other's elsewhere region.                |
|  14 | Go 1.19 introduced ThreadSanitizer (TSAN) v3, which supports an unlimited number of goroutines and offers improved performance.                                        |
|  15 | Testing confirmed that Go 1.18 fails at approximately 8,000 simultaneous goroutines, while Go 1.19 handles over 9,000 successfully.                                    |
|  16 | Benchmarking shows the race detector in Go 1.19 is approximately six times faster than in Go 1.18.                                                                     |
|  17 | CPU profiling reveals that TSAN v2 overhead is dominated by spin locks in the scheduler, whereas TSAN v3 uses lock-free data structures for parallelism.               |
|  18 | The Go race detector has shortcomings, such as limited detection of races in multi-word structures and reliance on runtime execution.                                  |
|  19 | Vector clocks effectively model Einsteinian time, providing the most accurate method for identifying concurrent events in distributed systems.                         |
|  20 | Programmers and compilers should avoid overly clever optimizations to prevent introducing subtle data races.                                                           |

# Video

[![Video thumbnail](https://img.youtube.com/vi/-jZrRXlPsy8/hqdefault.jpg)](https://www.youtube.com/watch?v=-jZrRXlPsy8)

[Watch on YouTube](https://www.youtube.com/watch?v=-jZrRXlPsy8)
