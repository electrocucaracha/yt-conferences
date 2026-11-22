---
layout: default
title: "Talks - Arun Suresh Kumar: Sync vs. Async in Python: Tools, Benchmarks, and ASGI/WSGI Explained"
nav_order: 179
parent: PyCon US 2024
type: Video Note
description: "Arun Suresh Kumar, a Python expert with over ten years of experience, presents a comprehensive analysis of synchronous versus asynchronous programming in Python, focusing on the transition from WSG..."
resource: "https://www.youtube.com/watch?v=UgoY3ChdqUU"
youtube_stats:
  view_count: 1019
  like_count: 20
  channel_subscriber_count: 34500
tags:
  - pycon-us-2024
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T10:18:11+00:00
---

# Summary

Arun Suresh Kumar, a Python expert with over ten years of experience, presents a comprehensive analysis of synchronous versus asynchronous programming in Python, focusing on the transition from WSGI to ASGI.
He explains that while synchronous applications handle one task at a time using blocking code, asynchronous applications utilize event loops and coroutines to manage multiple concurrent tasks efficiently, which is particularly beneficial for I/O-bound operations.
The talk details the architectural differences, noting that WSGI frameworks like Flask rely on multiple threads and processes to handle connections, leading to higher CPU and memory costs, whereas ASGI frameworks like FastAPI and Falcon can handle thousands of concurrent connections within a single worker using non-blocking code.
Kumar shares insights from his team’s migration of production applications, highlighting that moving to native asynchronous libraries significantly improves scalability and reduces infrastructure costs, although it requires careful management of memory usage and the avoidance of blocking code within async contexts.
He concludes by demonstrating benchmarking techniques using tools like Locust, showing that ASGI implementations can handle substantially more users and requests per second compared to their synchronous counterparts, and recommends ASGI for modern, high-concurrency web applications.

# Main Points

|   # | Main point                                                                                                                 |
| --: | -------------------------------------------------------------------------------------------------------------------------- |
|   1 | The talk covers synchronous versus asynchronous programming in Python, including ASGI, WSGI, and performance benchmarks.   |
|   2 | Synchronous programming executes one task at a time, while asynchronous programming handles multiple tasks simultaneously. |
|   3 | Python introduced async support in version 3.4 and added the async and await keywords in version 3.5.                      |
|   4 | Asynchronous programming is recommended for real-time systems and applications with high I/O operations.                   |
|   5 | Synchronous programming is easier to debug and suitable for CPU-bound tasks.                                               |
|   6 | The event loop monitors tasks, moving I/O operations to a separate queue to handle them concurrently.                      |
|   7 | WSGI applications handle a single request at a time and do not support websockets or long-polling connections.             |
|   8 | ASGI supports multiple simultaneous connections and is non-blocking, making it suitable for modern web applications.       |
|   9 | Frameworks like Django support WSGI, while FastAPI and Sanic support ASGI; Falcon supports both.                           |
|  10 | ASGI allows workers to handle hundreds of coroutines in a single worker, reducing server costs.                            |
|  11 | Migrating from synchronous to asynchronous code requires ensuring all code is non-blocking.                                |
|  12 | Blocking code in asynchronous applications should be isolated in separate threads to avoid impacting scaling.              |
|  13 | The asgiref library can be used to wrap synchronous libraries for use in asynchronous contexts.                            |
|  14 | Benchmarking should account for containerization constraints, such as CPU shares and memory limits in Docker.              |
|  15 | Performance tests using Locust showed ASGI handling significantly more users and requests per second than WSGI.            |
|  16 | Unexpected performance dips in load tests may indicate blocking code or excessive thread pool usage.                       |
|  17 | Native asynchronous libraries, such as asyncpg, offer better performance than synchronous-to-asynchronous wrappers.        |
|  18 | Websockets or HTTP/2 streaming are recommended for real-time data transmission, such as in chat applications.              |
|  19 | Asynchronous applications may experience higher memory and CPU usage compared to synchronous ones under load.              |

# Video

[![Video thumbnail](https://img.youtube.com/vi/UgoY3ChdqUU/hqdefault.jpg)](https://www.youtube.com/watch?v=UgoY3ChdqUU)

[Watch on YouTube](https://www.youtube.com/watch?v=UgoY3ChdqUU)
