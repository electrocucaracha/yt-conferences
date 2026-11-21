---
layout: default
title: "Container-enabled Asyncio is All You Need (to Build Pythonic AI Workflows at Scale) - Niels Bantlin"
nav_order: 61
parent: PyCon US 2026
type: Video Note
description: "The speaker, a core maintainer of Flyte and author of Pandera, argues that production AI workflows should be built using Python’s standard library `asyncio` rather than adopting complex domain-spec..."
resource: "https://www.youtube.com/watch?v=YF1Dgp0jZrM"
youtube_stats:
  view_count: 376
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

The speaker, a core maintainer of Flyte and author of Pandera, argues that production AI workflows should be built using Python’s standard library `asyncio` rather than adopting complex domain-specific languages (DSLs) or rigid orchestrators.
He posits that modern AI and ML workloads are effectively dynamic execution graphs of "waits," where the primary challenge is coordinating concurrent I/O operations, such as parallel LLM calls, API requests, and data retrieval, rather than heavy computation.
While DSLs can impose unnecessary constraints on control flow and complicate debugging, `asyncio` provides the necessary tools for concurrency, backpressure, and error handling through constructs like `asyncio.gather`, semaphores, and task groups.
To address the limitations of local hardware and the need for strong isolation, heterogeneous compute resources, and multi-tenancy, the speaker advocates for combining `asyncio` with a container orchestrator like Kubernetes.
This approach allows developers to write standard Python code that can be locally debugged and then deployed to a distributed infrastructure, where the orchestrator handles resource provisioning and isolation while the application logic remains in plain Python.
The talk concludes with a demonstration of Flyte 2, a reference implementation that integrates seamlessly with `asyncio` to manage distributed tasks, emphasizing that learning `asyncio` is essential for understanding and debugging the underlying mechanics of modern AI frameworks.

# Main Points

|   # | Main point |
| --: | ---------- |
|   1 | The speaker is the author of Pandera and core maintainer of Flyte, presenting on async IO for production AI workflows. |
|   2 | Production AI workflows often fail at scale due to rate limits, connection pileups, and out-of-memory errors that kill entire processes. |
|   3 | Traditional orchestrators often impose a Domain Specific Language (DSL), which the speaker argues is unnecessary for many use cases. |
|   4 | Production AI workflows are effectively dynamic execution graphs where the primary coordination task is waiting for compute to complete elsewhere. |
|   5 | Async IO is the standard library solution for expressing concurrency and parallelism in plain Python without a new grammar. |
|   6 | Container orchestration is required to solve production-scale problems like heterogeneous compute requirements, isolation, and back pressure. |
|   7 | The recommended architecture combines async Python for logic and data flow with a container orchestrator for scheduling and isolation. |
|   8 | Async IO constructs like asyncio.gather, task groups, and semaphores allow for bounded concurrency and handling partial failures. |
|   9 | Queues and timeouts in async IO provide mechanisms for back pressure and preventing application stalls during API calls. |
|  10 | Streaming responses using async iterators ensures constant memory usage by processing tokens individually rather than buffering entire outputs. |
|  11 | Container orchestration enables arbitrary scaling, GPU provisioning, and multi-tenancy, which are not possible with local hardware alone. |
|  12 | Flyte 2 serves as a reference implementation where Python functions are decorated with tasks and run on Kubernetes clusters. |
|  13 | Flyte uses Python type hints to determine serialization methods and manages state via blob stores like S3 or MinIO. |
|  14 | A key trade-off of distributed systems is the inability to share global Python objects or state directly between isolated containers. |
|  15 | The speaker advises learning async IO to better debug and understand the internals of modern AI and ML libraries. |
|  16 | The core message is to distinguish between needing isolation (solved by containers) and needing a DSL (often unnecessary). |

# Video

[![Video thumbnail](https://img.youtube.com/vi/YF1Dgp0jZrM/hqdefault.jpg)](https://www.youtube.com/watch?v=YF1Dgp0jZrM)

[Watch on YouTube](https://www.youtube.com/watch?v=YF1Dgp0jZrM)
