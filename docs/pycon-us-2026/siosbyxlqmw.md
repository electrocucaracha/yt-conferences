---
layout: default
title: "Every Obvious Approach Failed: Building an Async Database Client...(Sponsor: Clickhouse)"
nav_order: 107
parent: PyCon US 2026
type: Video Note
description: "Joe Spidola, a senior Python integrations engineer at ClickHouse, presents a technical deep dive into building a high-performance asynchronous native database client that scales effectively."
resource: "https://www.youtube.com/watch?v=SIOSBYxLQmw"
youtube_stats:
  view_count: 1302
  like_count: 5
  channel_subscriber_count: 34500
tags:
  - pycon-us-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-20T08:08:06+00:00
---

# Summary

Joe Spidola, a senior Python integrations engineer at ClickHouse, presents a technical deep dive into building a high-performance asynchronous native database client that scales effectively.
He explains that while asynchronous programming excels at managing I/O waiting, the primary bottleneck in their database response pipeline was CPU-intensive parsing of bytes into Python objects, a task that does not benefit from standard async syntax.
After demonstrating that naive approaches—such as buffering entire responses or parsing on the event loop—failed due to memory constraints or blocking behavior, Spidola introduces the "half-sync half-async" pattern.
This design separates the I/O-bound network reading on the async event loop from the CPU-bound parsing on a synchronous worker thread, bridging the two with a bounded queue that provides essential back pressure and maintains data order.
The implementation required careful handling of race conditions, error propagation, and cross-thread wake-up mechanisms to ensure reliability.
Benchmark results show that this new client achieves a geometric mean speedup of 1.16x over the legacy thread-pool executor client, with significantly improved P95 latencies and reduced variance, proving that separating I/O from CPU work yields faster, more consistent performance under high concurrency.

# Main Points

|   # | Main point |
| --: | ---------- |
|   1 | The core bottleneck in the database client was not waiting for I/O but the CPU-heavy parsing of bytes into Python objects. |
|   2 | Wrapping a synchronous blocking client in an async API using a thread pool executor provides async syntax but lacks true async performance benefits. |
|   3 | The legacy approach drained the thread pool under high concurrency because each query held a worker thread for the entire duration of the request and parse cycle. |
|   4 | Four naive approaches to building a new async client failed due to issues like unbounded memory buffering, blocking the event loop, or preventing overlap between reading and parsing. |
|   5 | The successful design utilizes the half-sync half-async pattern, which separates I/O operations from CPU-bound work using a bounded queue as a bridge. |
|   6 | The async side handles network I/O and pushes data chunks into the queue, while the synchronous side consumes the queue to perform parsing in a worker thread. |
|   7 | A bounded queue provides essential back pressure, preventing unbounded memory growth by suspending the producer when the queue is full and the consumer when it is empty. |
|   8 | Cross-thread communication requires specific mechanisms to wake sleeping threads, using threading conditions for the sync side and asyncio call_soon_threadsafe for the async side. |
|   9 | A single lock is required to safely mutate the shared queue, ensuring that data integrity is maintained while both sides access the bridge concurrently. |
|  10 | Error handling and cleanup are complex because exceptions must be packaged to cross the thread boundary, and both sides must be woken up to prevent permanent hangs. |
|  11 | The parser must handle data that spans multiple chunks by buffering bytes until enough data is available to complete the parsing of a specific type. |
|  12 | Benchmark results show a geometric mean speedup of 1.16x over the legacy client, with significantly improved P95 latencies and lower standard deviation. |
|  13 | The new design achieves better tail latency and reliability under high concurrency, making results more consistent for production workloads. |
|  14 | The implementation took several months, with the majority of time spent on ensuring race-safe wakeups, proper cleanup, and handling edge cases like deadlocks. |
|  15 | The solution maintains functional parity with the previous client, allowing users to switch without changing their application code or query logic. |
|  16 | The half-sync half-async pattern is a foundational concept from systems programming that effectively bridges different concurrency models. |
|  17 | The design allows for a streaming API where rows can be yielded to the caller before the entire query is complete, improving time to first row. |
|  18 | The queue bridge can theoretically work in reverse for data insertion, allowing the sync side to produce bytes and the async side to upload them. |
|  19 | Testing involved stress suites, synthetic workloads generated by LLMs, and manual edge case creation to identify and fix potential deadlocks. |
|  20 | The final implementation ensures that the parser remains unchanged, preserving the stability and efficiency of the existing transform logic. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/SIOSBYxLQmw/hqdefault.jpg)](https://www.youtube.com/watch?v=SIOSBYxLQmw)

[Watch on YouTube](https://www.youtube.com/watch?v=SIOSBYxLQmw)
