---
layout: default
title: "Talks - Arthur Pastel: Demystifying AsyncIO: Building Your Own Event Loop in Python"
nav_order: 190
parent: PyCon US 2024
type: Video Note
description: "Arthur Pastel, a software engineer from France, presents a talk on demystifying Python’s asyncio by explaining the core mechanics of the event loop."
resource: "https://www.youtube.com/watch?v=8I9Rc2Zaos4"
youtube_stats:
  view_count: 2151
  like_count: 48
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

Arthur Pastel, a software engineer from France, presents a talk on demystifying Python’s asyncio by explaining the core mechanics of the event loop.
He details how the event loop manages execution through a queue of callbacks, scheduled tasks, and futures, allowing the program to suspend and resume operations efficiently.
The presentation contrasts synchronous I/O, which blocks execution, with asynchronous I/O, which leverages the GIL’s behavior during I/O waits to process multiple tasks in parallel using selectors and file descriptors.
Pastel demonstrates building a custom event loop to run a FastAPI server, highlighting the relationship between coroutines, tasks, and the underlying system calls that enable non-blocking operations.
Finally, he discusses performance optimizations, noting that while pure Python implementations are slower than the default CPython loop, alternatives like uvloop offer significant speed improvements, and he introduces his project, cpit, for consistent performance benchmarking in continuous integration.

# Main Points

|   # | Main point                                                                                                                                                                         |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker introduces himself as a software engineer from France who has contributed to open source projects, including a MongoDB ORM and CPython performance improvements.       |
|   2 | The core principle of asyncio is suspending program execution to allow other tasks to run while waiting for I/O operations.                                                        |
|   3 | Synchronous I/O blocks the Global Interpreter Lock (GIL), whereas asynchronous I/O allows the GIL to be released during waits, enabling parallel execution of non-CPU-bound tasks. |
|   4 | The event loop is the central mechanism that schedules and executes callbacks, manages futures, and handles I/O operations.                                                        |
|   5 | Basic event loop functionality involves scheduling callbacks into a ready queue, which are then popped and executed in an asynchronous manner.                                     |
|   6 | Scheduling callbacks for future execution requires a sorted queue to manage timing, using binary insertion to maintain order.                                                      |
|   7 | Futures represent pending operations that can hold a result or an exception, allowing code to react when an operation completes.                                                   |
|   8 | The asyncio.sleep function is implemented by creating a future scheduled to complete after a delay, allowing the event loop to process other tasks during the wait.                |
|   9 | The gather function aggregates multiple futures into a single future, completing only when all individual futures have finished.                                                   |
|  10 | I/O operations are handled by mapping file descriptors to callbacks, allowing the event loop to wait for read or write readiness.                                                  |
|  11 | Selectors, such as the select system call, monitor multiple file descriptors for readiness and trigger the associated callbacks when data is available.                            |
|  12 | The async/await syntax provides a convenient way to manage coroutines, which are functions that can be suspended and resumed.                                                      |
|  13 | Tasks link coroutines to futures, scheduling the initial execution of a coroutine and managing its lifecycle within the event loop.                                                |
|  14 | A custom event loop implementation was shown to be significantly slower than the default CPython implementation due to lack of optimizations.                                      |
|  15 | Uvloop, a drop-in replacement built with libuv, offers performance improvements of two to four times over the default event loop.                                                  |
|  16 | Performance measurement tools like cpit help track consistent performance metrics in continuous integration environments.                                                          |
|  17 | Testing asynchronous code can be challenging due to non-deterministic execution order, but pytest fixtures and callback scheduling can aid in deterministic testing.               |
|  18 | Creating a task schedules its first step for the next event loop tick, but it does not execute immediately until the loop runs.                                                    |
|  19 | Tasks and futures can be cancelled, and mechanisms like shielding can be used to prevent immediate cancellation and allow for graceful shutdown.                                   |

# Video

[![Video thumbnail](https://img.youtube.com/vi/8I9Rc2Zaos4/hqdefault.jpg)](https://www.youtube.com/watch?v=8I9Rc2Zaos4)

[Watch on YouTube](https://www.youtube.com/watch?v=8I9Rc2Zaos4)
