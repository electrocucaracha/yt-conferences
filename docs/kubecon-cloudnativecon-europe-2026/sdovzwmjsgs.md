---
layout: default
title:
  "How Telemetry Data Moves: Lessons From Building a High-Performance Open Source
  Agent - Eduardo Silva"
nav_order: 144
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this session, Eduardo discusses the fundamental concepts of how data
  moves within real systems, particularly focusing on the flow between user space
  and kernel space in operating systems. He explains that data pipelines typically
  involve...
resource: https://www.youtube.com/watch?v=SdovZWMJsgs
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

In this session, Eduardo discusses the fundamental concepts of how data moves within real systems, particularly focusing on the flow between user space and kernel space in operating systems.
He explains that data pipelines typically involve collecting data from various sources, processing and normalizing it—often using efficient binary formats like MessagePack—and then delivering it to endpoints, with considerations for buffering, batching, and serialization to optimize performance and resource usage.
Eduardo emphasizes the importance of understanding system calls, memory management, and the roles of event loops, multi-threading, and coroutines in building scalable and resilient data processing applications.
He uses the architecture of Fluent Bit as an example, highlighting its evolution toward high performance and low resource consumption by adopting asynchronous I/O and event-driven models, similar to advancements seen in web servers like Apache and NGINX.
The talk concludes by encouraging developers to anticipate bottlenecks, design for failure scenarios, and leverage concurrency to efficiently handle increasing data volumes.

# Main Points

|   # | Main point                                                                                                                |
| --: | ------------------------------------------------------------------------------------------------------------------------- |
|   1 | Session focused on how data moves in real systems, not a product pitch                                                    |
|   2 | Speaker: Eduardo, involved in Fluent ecosystem for over 10 years                                                          |
|   3 | Data movement involves kernel space (hardware abstraction) and user space (applications)                                  |
|   4 | Applications interact with the kernel via system calls, which can be expensive in terms of CPU time                       |
|   5 | Data transfer between user space and kernel space often involves copying buffers for safety                               |
|   6 | Understanding the full data cycle (application → system call → kernel → hardware) is crucial                              |
|   7 | Data sources vary (firewall, log files, systemd, etc.), requiring normalization for analysis                              |
|   8 | Data normalization often uses binary formats like MessagePack (schemaless) or Protocol Buffers (schema-based)             |
|   9 | Fluent Bit/Fluentd use MessagePack for internal data chunks, optimizing storage and transfer                              |
|  10 | Data sent to endpoints like Elasticsearch must be converted to expected formats (e.g., JSON)                              |
|  11 | Frequent system calls and data copies are expensive; batching and buffering are recommended for efficiency                |
|  12 | Hardware components like network cards use buffers to optimize data transfer                                              |
|  13 | Buffering and batching reduce the number of operations and improve performance                                            |
|  14 | Data pipelines involve threads for receiving, buffering, scheduling, retrying, filtering, and sending data                |
|  15 | Multi-threading and separating processing tasks reduce contention and bottlenecks                                         |
|  16 | Event loops and asynchronous I/O allow efficient handling of events and retries without blocking threads                  |
|  17 | Coroutines (lightweight threads) enable segmented, efficient code execution                                               |
|  18 | Combining multi-threading, coroutines, and event loops allows high-scale data movement                                    |
|  19 | Telemetry systems rely on data movement, buffering, concurrency, and scalability for performance and stability            |
|  20 | Fluent Bit architecture evolved from process-per-connection (like Apache v1) to threads and asynchronous I/O (like Nginx) |
|  21 | Project principles: high performance, low resource usage, broad ecosystem support, vendor neutrality                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=SdovZWMJsgs)
