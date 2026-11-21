---
layout: default
title: "GopherCon 2025: Understanding Escape Analysis to Speed Up Your Code - Bill Kennedy"
nav_order: 9
parent: GopherCon 2025
type: Video Note
description: 'The speaker presents a case study on Go escape analysis, comparing two algorithms designed to find and replace the name "Elvis" in a data stream.'
resource: "https://www.youtube.com/watch?v=FUm0pfgWehI"
youtube_stats:
  view_count: 3703
  like_count: 100
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

The speaker presents a case study on Go escape analysis, comparing two algorithms designed to find and replace the name "Elvis" in a data stream.
Initially, the speaker’s implementation using the `io` package resulted in two heap allocations, while a colleague’s simpler approach achieved zero allocations.
By utilizing memory profiling and the Go compiler’s escape analysis report, the speaker identified that an interface conversion in the `io` package forced the data onto the heap.
After refactoring the code to use direct method calls instead of the `io` package, the speaker successfully eliminated all allocations, matching the colleague’s performance.
The talk concludes by emphasizing that while these micro-optimizations are valuable for understanding compiler behavior and tooling, the actual performance difference of a few hundred nanoseconds is often negligible in real-world applications, serving primarily as a lesson in using Go’s diagnostic tools effectively.

# Main Points

|   # | Main point                                                                                                                                      |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker created a problem to learn the Go IO package by searching for the name "Elvis" and correcting its capitalization.                   |
|   2 | The speaker wrote an initial algorithm using a buffer and the IO package, which resulted in two memory allocations.                             |
|   3 | A friend named Tyler provided an alternative solution using a reader and method set calls, which achieved zero allocations.                     |
|   4 | Benchmarks revealed that Tyler's zero-allocation algorithm was significantly faster than the speaker's two-allocation version.                  |
|   5 | The speaker used a memory profile to identify the specific lines of code causing the allocations in their algorithm.                            |
|   6 | An escape analysis report generated with the -gcflags="-m=2" flag was used to investigate why allocations were occurring.                       |
|   7 | The report indicated that a function was being inlined, which contradicted the initial assumption that the function call caused the allocation. |
|   8 | The speaker discovered that the terminal version of the profiling tool did not display inlining optimizations, while the browser version did.   |
|   9 | Using the -no-inline flag in the terminal revealed that the allocation was flat rather than cumulative due to inlining.                         |
|  10 | The root cause of one allocation was identified as an interface conversion when passing concrete data to the IO package's ReadFull function.    |
|  11 | Tyler's algorithm avoided allocations by using the method set of the reader directly instead of relying on the IO package interfaces.           |
|  12 | The speaker modified their code to remove the IO package dependency and use direct method calls, which eliminated both allocations.             |
|  13 | Despite achieving zero allocations, the speaker's algorithm remained slower than Tyler's, prompting further investigation into CPU performance. |
|  14 | The speaker noted that Go 1.25 optimizes allocations under 32 bytes to the stack even if the size is not known at compile time.                 |
|  15 | The escape analysis report helps determine if a function is inlined based on its complexity score, with a budget of 80 or less.                 |
|  16 | The speaker emphasized that micro-optimizations like saving 400 nanoseconds are often irrelevant to real-world performance and driven by ego.   |
|  17 | The talk demonstrated how to use Go's built-in tools for benchmarking, memory profiling, and escape analysis to diagnose performance issues.    |
|  18 | The speaker advised against attempting such deep micro-analysis in Go 1.25 without prior experience and proper tooling support.                 |

# Video

[![Video thumbnail](https://img.youtube.com/vi/FUm0pfgWehI/hqdefault.jpg)](https://www.youtube.com/watch?v=FUm0pfgWehI)

[Watch on YouTube](https://www.youtube.com/watch?v=FUm0pfgWehI)
