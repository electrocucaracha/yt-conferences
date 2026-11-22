---
layout: default
title: "Zoom, Enhance: Asyncio's New Introspection Powers - Pablo Galindo Salgado & Yury Selivanov"
nav_order: 43
parent: PyCon US 2025
type: Video Note
description: "At a Python core development sprint, developers Pablo and the speaker addressed a Meta request to introspect asyncio programs using eBPF profiling with zero overhead."
resource: "https://www.youtube.com/watch?v=RrsVi1P6n0w"
youtube_stats:
  view_count: 2172
  like_count: 91
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

At a Python core development sprint, developers Pablo and the speaker addressed a Meta request to introspect asyncio programs using eBPF profiling with zero overhead.
They discovered that standard profilers fail to capture the actual running tasks, showing only generic event loop frames, which they described as "useless." To solve this, they implemented a new `task.awaited_by` attribute and APIs like `print_task_call_graph` to map the complex dependency tree of coroutines and tasks.
Their solution required navigating a notoriously complex data structure, which they humorously named the "whole topology flood" algorithm due to its exponential complexity.
The talk concluded with a demonstration of a new `asyncio-ps` tool that visualizes these task relationships in real-time, a feature set that ships in Python 3.14 to enable the first zero-overhead asyncio profiler.

# Main Points

|   # | Main point                                                                                                                                                      |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The presentation introduces two Python core developers, Pablo and the speaker, who are wearing banana costumes.                                                 |
|   2 | The project originated from a Meta issue requesting zero-overhead introspection of asyncio programs using eBPF profiling.                                       |
|   3 | Standard Python stack traces for asyncio programs are often useless because they only show event loop frames and hide actual task execution.                    |
|   4 | The resulting pull request became one of the most reviewed in CPython history, with 16 approvals and a screenshot 100,000 pixels tall.                          |
|   5 | Asyncio is described as a simple event loop that manages a queue of callbacks, though it is often perceived as complex.                                         |
|   6 | Async functions are functionally similar to generators, requiring an event loop to drive them by sending values and handling yields.                            |
|   7 | Asyncio tasks are wrapper objects that manage coroutines, acting as independent units of work similar to OS processes.                                          |
|   8 | A new attribute, task awaited by, was added to track which tasks are waiting on others, enabling the construction of a dependency graph.                        |
|   9 | Two new APIs, print task call graph and capture call graph, were implemented to expose this task relationship data.                                             |
|  10 | Initial attempts to capture task data from within the process were deemed slow and impractical for external profiling tools.                                    |
|  11 | The final solution uses the process_vm_readv system call to read memory from another process, allowing zero-overhead external introspection.                    |
|  12 | A testing error revealed that tasks are invisible when the event loop is waiting for I/O, meaning snapshots must be taken continuously to capture active tasks. |
|  13 | The team developed an asyncio ps tool to display task trees and relationships, addressing a data structure issue that generated excessive subgraphs.            |
|  14 | The flawed data structure algorithm, named whole topology flood, had a complexity of Big O(2 to the power of n squared).                                        |
|  15 | The tool supports tree and table views of task dependencies and can be used in a watch mode to monitor real-time changes.                                       |
|  16 | The solution enables the creation of the first zero-overhead asyncio profiler that tracks all task relationships.                                               |
|  17 | The features ship in Python 3.14 and require only a process ID and the new tooling to function.                                                                 |
|  18 | The talk concludes with a humorous interaction involving Guido van Rossum, who comments that the situation is totally bananas.                                  |

# Video

[![Video thumbnail](https://img.youtube.com/vi/RrsVi1P6n0w/hqdefault.jpg)](https://www.youtube.com/watch?v=RrsVi1P6n0w)

[Watch on YouTube](https://www.youtube.com/watch?v=RrsVi1P6n0w)
