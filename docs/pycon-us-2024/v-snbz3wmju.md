---
layout: default
title: "Tutorials - Daksh Gupta: The world of High Performance Distributed & Async Task Queue(s) with Celery"
nav_order: 10
parent: PyCon US 2024
type: Video Note
description: "This tutorial, led by software consultant D."
resource: "https://www.youtube.com/watch?v=v-Snbz3WmJU"
youtube_stats:
  view_count: 4168
  like_count: 75
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

This tutorial, led by software consultant D.
Gupta, provides a comprehensive guide to implementing distributed and asynchronous task queues using Python Celery.
The session begins by establishing the necessity of decoupling systems, such as separating a banking operating system from its SMS notification service, to avoid tight coupling and improve scalability.
Gupta explains that Celery, a pure Python framework, is ideal for this purpose, particularly when teams are already proficient in Python, as it allows for the best utilization of features compared to using third-party clients for other languages.
The core mechanics involve using a message broker, primarily RabbitMQ, to manage task queues where producers send tasks and Celery workers consume them, enabling asynchronous execution and parallel processing across multiple CPU cores to bypass Python’s Global Interpreter Lock.
The tutorial covers advanced topics essential for production-level code, including managing concurrency through worker scaling, utilizing `apply_async` for parameters like countdowns, and implementing two-way communication via backends to retrieve task results.
It also delves into complex task orchestration using signatures, groups for parallel execution, and chains for sequential data flow, while emphasizing the critical importance of state management for debugging and reliability in distributed systems.
Additionally, the session demonstrates how to manage multiple queues for different task types, monitor performance using tools like Flower and Prometheus, and switch between brokers like RabbitMQ and Redis, noting that Redis offers additional capabilities such as chords for complex task dependencies.
By the end, participants are equipped with the knowledge to build robust, scalable, and maintainable asynchronous systems using Celery.

# Main Points

|   # | Main point                                                                                                                                                                                      |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The tutorial covers distributed and asynchronous task queues using Python Celery, targeting both basic and production-level implementation.                                                     |
|   2 | Celery is recommended for Python ecosystems because it is pure Python, avoiding the limitations of using Python clients for non-Python tools like Kafka.                                        |
|   3 | Task queues decouple systems, such as separating a banking operating system from an SMS notification service to prevent tight coupling.                                                         |
|   4 | Celery tasks are managed by a message broker, primarily RabbitMQ or Redis, which stores tasks even if Celery workers are temporarily down.                                                      |
|   5 | The `delay` method is the simplest way to enqueue a task, while `apply_async` allows for additional parameters like `countdown` to schedule execution without blocking workers.                 |
|   6 | Passing keyword arguments requires `apply_async` because `delay` treats all inputs as positional arguments, which can cause debugging issues.                                                   |
|   7 | Celery handles Python's Global Interpreter Lock (GIL) by forking multiple worker processes by default, equal to the number of CPU cores.                                                        |
|   8 | Concurrency can be controlled via the `--concurrency` flag, but exceeding system file descriptor limits (ulimit) can cause crashes.                                                             |
|   9 | Auto-scaling allows Celery to dynamically adjust the number of workers based on the load in the message broker queue, reducing resource usage during low traffic.                               |
|  10 | Two-way communication is achieved by configuring a backend (e.g., RPC) to retrieve task results, enabling confirmation of task completion for auditing or legal purposes.                       |
|  11 | Signatures act as templates for task invocations, allowing for reusable parameter sets and the creation of groups or chains of tasks.                                                           |
|  12 | Chaining tasks ensures sequential execution where the output of one task becomes the input for the next, unlike groups which execute tasks in parallel.                                         |
|  13 | State management is critical for production systems; developers should implement state machines to track task status and facilitate debugging across multiple workers.                          |
|  14 | Multiple queues can be created using the `-Q` parameter to isolate different types of work, such as separating SMS and WhatsApp notifications.                                                  |
|  15 | Queue assignment can be specified on the client-side via the `queue` parameter or on the server-side within the `@app.task` decorator.                                                          |
|  16 | Monitoring is supported via Flower, which can be integrated with time-series databases like Prometheus and visualization tools like Grafana for alerting and historical data analysis.          |
|  17 | Redis can be used as an alternative broker to RabbitMQ, offering additional capabilities like storing state data and supporting the `chord` functionality for complex task workflows.           |
|  18 | Distributed deployment is straightforward as multiple Celery instances connecting to the same broker automatically detect each other and distribute tasks without complex infrastructure setup. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/v-Snbz3WmJU/hqdefault.jpg)](https://www.youtube.com/watch?v=v-Snbz3WmJU)

[Watch on YouTube](https://www.youtube.com/watch?v=v-Snbz3WmJU)
