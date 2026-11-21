---
layout: default
title: "GopherCon 2025: Go’s Trace Tooling and Concurrency - Bill Kennedy"
nav_order: 16
parent: GopherCon 2025
type: Video Note
description: "The video demonstrates how to use Go’s tracing tool to identify performance bottlenecks in a single-threaded program that processes 4,000 RSS feeds, revealing that the application is not utilizing ..."
resource: "https://www.youtube.com/watch?v=Gqo0oCfZSjg"
youtube_stats:
  view_count: 3925
  like_count: 208
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

The video demonstrates how to use Go’s tracing tool to identify performance bottlenecks in a single-threaded program that processes 4,000 RSS feeds, revealing that the application is not utilizing available CPU cores.
The presenter converts the code to a concurrent "fan-out" model using goroutines and a wait group, which significantly reduces execution time from approximately 1,000 milliseconds to 264 milliseconds, though it introduces a data race that is resolved using atomic operations and local variable counting to minimize cache thrashing.
A subsequent attempt to optimize further by limiting concurrency to a worker pool of 16 goroutines results in slower performance (388 milliseconds) due to excessive garbage collection overhead, highlighting the trade-off between memory efficiency and speed.
By adjusting the `GOGC` environment variable to allow the heap to grow to 40MB, the program achieves its best performance at 136 milliseconds with minimal GC impact, demonstrating that providing the runtime with more memory can be more effective than strictly limiting concurrency.
The session concludes by emphasizing that Go’s scheduler and garbage collector are highly optimized for high-concurrency scenarios, suggesting that developers should leverage the runtime’s capabilities rather than prematurely restricting goroutine counts.

# Main Points

|   # | Main point                                                                                                                                                                                              |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The Go tracing tool helps identify performance issues by revealing what is not happening in a program, unlike CPU profiling which only shows active processes.                                          |
|   2 | A sample single-threaded program processing 4,000 RSS feeds took over one second, with system calls identified as the primary bottleneck via profiling.                                                 |
|   3 | The trace tool visualizes goroutines, heap usage, garbage collection, and pacing across processors, revealing that the initial program utilized only one of sixteen available cores.                    |
|   4 | Converting the program to a concurrent fan-out model using 4,000 goroutines reduced execution time to approximately 289 milliseconds.                                                                   |
|   5 | A data race was detected when multiple goroutines accessed a shared counter variable, which was resolved by using the atomic package for safe integer increments.                                       |
|   6 | Memory thrashing occurred due to frequent cache line invalidations when incrementing a shared variable, mitigated by using local variables for counting and aggregating results at the end.             |
|   7 | The concurrent fan-out approach resulted in higher garbage collection overhead, with 65% of wall-clock time spent in GC despite faster overall execution.                                               |
|   8 | Implementing a worker pool with a fixed number of goroutines equal to the core count reduced memory usage but increased GC frequency to 74% of total runtime.                                           |
|   9 | Adjusting the GOGC environment variable to 1000 allowed the heap to grow to 40 megabytes, reducing GC time to 13% and improving performance to 136 milliseconds.                                        |
|  10 | Using the GOMEMLIMIT environment variable to set a 60-megabyte memory cap achieved similar performance to GOGC adjustments while providing a more explicit memory boundary.                             |
|  11 | The Go runtime reserves a portion of the allocated memory limit for its own operations, meaning the heap may not utilize the full specified limit.                                                      |
|  12 | Disabling the garbage collector entirely yielded no significant performance difference when sufficient memory was allocated, indicating the GC was not a bottleneck under these conditions.             |
|  13 | The Go scheduler and garbage collector are highly optimized for scenarios with many concurrent goroutines, making fan-out strategies effective for I/O-bound workloads.                                 |
|  14 | Developers should leverage the Go runtime's concurrency capabilities by spawning goroutines for parallel tasks rather than manually limiting concurrency, as the runtime efficiently manages resources. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/Gqo0oCfZSjg/hqdefault.jpg)](https://www.youtube.com/watch?v=Gqo0oCfZSjg)

[Watch on YouTube](https://www.youtube.com/watch?v=Gqo0oCfZSjg)
