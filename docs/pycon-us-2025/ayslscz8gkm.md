---
layout: default
title: "Building a NoGIL Load Balancer in 30 minutes - Alvaro Duran"
nav_order: 82
parent: PyCon US 2025
type: Video Note
description: "Alvaro from kiwi.com presents a technical exploration of Python’s free-threaded (no-GIL) build, demonstrating its impact on performance through the construction of a load balancer."
resource: "https://www.youtube.com/watch?v=AYSlsCz8gKM"
youtube_stats:
  view_count: 1705
  like_count: 55
  channel_subscriber_count: 34500
tags:
  - pycon-us-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T01:39:37+00:00
---

# Summary

Alvaro from kiwi.com presents a technical exploration of Python’s free-threaded (no-GIL) build, demonstrating its impact on performance through the construction of a load balancer.
He begins by explaining that the Global Interpreter Lock (GIL) historically prevented true parallel execution of CPU-bound tasks, but the no-GIL version allows threads to run simultaneously on different CPU cores.
By stress-testing a Fibonacci server, he shows that while the no-GIL build eliminates the "long request" bottleneck where a single slow task blocks others, it introduces "load sensitivity," where increasing the number of clients reduces per-client throughput.
This issue is traced to the `random` library, which uses a hidden fine-grain lock for memory safety, causing contention; replacing it with a "least connections" algorithm using an explicit threading lock resolves this specific bottleneck.
The talk concludes that the no-GIL build is superior for CPU-bound workloads as it scales with available cores, whereas the GIL remains more efficient for highly I/O-bound tasks, and users should be aware of hidden locks in standard libraries when migrating to free-threaded Python.

# Main Points

|   # | Main point                                                                                                                                           |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The Global Interpreter Lock (GIL) historically prevented Python threads from executing simultaneously on multiple CPU cores.                         |
|   2 | In 2021, Sam Gross introduced a proof of concept for a no-GIL Python build to enable true parallel execution.                                        |
|   3 | CPU-bound tasks are bottlenecked by code execution, while I/O-bound tasks are bottlenecked by waiting for external data.                             |
|   4 | A load balancer serves as a relevant test case because it combines CPU-bound proxying with I/O-bound response waiting.                               |
|   5 | A threaded Fibonacci server using the standard GIL build achieves high throughput for fast requests but stalls when a slow request occupies the CPU. |
|   6 | The no-GIL build eliminates the stall caused by slow requests, allowing other threads to continue running on separate CPU cores.                     |
|   7 | Increasing the number of clients in the no-GIL build initially causes a throughput drop per client, a phenomenon termed load sensitivity.            |
|   8 | Using the random library in a multi-threaded no-GIL environment introduces a hidden fine-grain lock that reduces performance.                        |
|   9 | Replacing random selection with a least-connections algorithm using an explicit threading lock restores expected throughput levels.                  |
|  10 | For I/O-bound workloads with fast requests, the standard GIL build often provides better throughput per client than the no-GIL build.                |
|  11 | For CPU-bound workloads with slower requests, the no-GIL build scales better by utilizing multiple CPU cores independently.                          |
|  12 | Performance benefits of the no-GIL build diminish when the number of active threads exceeds the number of available CPU cores.                       |
|  13 | Python libraries may contain hidden locks or lack memory safety, creating unexpected bottlenecks in no-GIL environments.                             |
|  14 | The no-GIL Python build is currently experimental and intended for evaluation rather than immediate production use.                                  |

# Video

[![Video thumbnail](https://img.youtube.com/vi/AYSlsCz8gKM/hqdefault.jpg)](https://www.youtube.com/watch?v=AYSlsCz8gKM)

[Watch on YouTube](https://www.youtube.com/watch?v=AYSlsCz8gKM)
