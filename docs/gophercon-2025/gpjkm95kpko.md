---
layout: default
title: "GopherCon 2025: Advancing Go Garbage Collection with Green Tea - Michael Knyszek"
nav_order: 22
parent: GopherCon 2025
type: Video Note
description: 'Michael from the Go team introduces "Green Tea," a new garbage collection technique designed to make Go''s GC faster, with plans for general availability in Go 26.'
resource: "https://www.youtube.com/watch?v=gPJkM95KpKo"
youtube_stats:
  view_count: 12830
  like_count: 432
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

Michael from the Go team introduces "Green Tea," a new garbage collection technique designed to make Go's GC faster, with plans for general availability in Go 26.
The talk explains that traditional mark-sweep algorithms suffer from poor CPU cache performance due to random memory access patterns, which becomes increasingly problematic with modern hardware features like NUMA and vector instructions.
Green Tea addresses this by shifting the unit of work from individual objects to entire memory pages, allowing the collector to scan multiple objects in memory order and leverage SIMD vector hardware for efficient bit manipulation.
This approach reduces GC CPU costs by 10% to 40% in benchmarks and improves scalability by minimizing worklist contention.
The feature is currently available as an experiment in Go 25 via the `GODEBUG` environment variable and is expected to become the default in Go 26, representing a significant collaborative effort spanning several years.

# Main Points

|   # | Main point                                                                                                                              |
| --: | --------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Go's garbage collection uses a tracing mark-sweep algorithm that follows pointers to identify reachable objects.                        |
|   2 | The core of the algorithm is a graph flood starting from roots like global and local variables.                                         |
|   3 | Marking is the most expensive phase, consuming at least 35% of time waiting on CPU memory fetches.                                      |
|   4 | The traditional graph flood approach is a poor fit for modern CPU microarchitecture due to unpredictable memory access patterns.        |
|   5 | Modern hardware challenges include Non-Uniform Memory Access, constrained memory bandwidth, and the need for scalable shared worklists. |
|   6 | Green Tea is a new technique that optimizes garbage collection by working with pages rather than individual objects.                    |
|   7 | Instead of scanning objects, Green Tea scans whole pages and tracks pages on the worklist.                                              |
|   8 | Object marking is tracked locally on each page using separate seen and scanned bits in metadata.                                        |
|   9 | The worklist uses a first-in-first-out queue order to allow objects to accumulate on pages before scanning.                             |
|  10 | This approach improves CPU cache locality by processing multiple objects in memory order within a single page.                          |
|  11 | Smaller worklists reduce contention and improve scalability across multiple CPU cores.                                                  |
|  12 | Vector hardware acceleration is enabled by holding page metadata in large registers and using bit manipulation instructions.            |
|  13 | Green Tea reduces garbage collection CPU costs by 10% to 40% in benchmarks, with an additional 10% gain from vectorization.             |
|  14 | Some workloads with low object density per page may not benefit or could regress, though fast paths mitigate this.                      |
|  15 | Green Tea is available as an experiment in Go 25 via the GODEBUG environment variable.                                                  |
|  16 | The feature is planned to become the default in Go 26, including vector acceleration support.                                           |
|  17 | The name Green Tea originated from a prototype developed while drinking matcha in Japan.                                                |
|  18 | The project involved seven years of collaborative effort and iterative design to navigate the complex design space.                     |

# Video

[![Video thumbnail](https://img.youtube.com/vi/gPJkM95KpKo/hqdefault.jpg)](https://www.youtube.com/watch?v=gPJkM95KpKo)

[Watch on YouTube](https://www.youtube.com/watch?v=gPJkM95KpKo)
