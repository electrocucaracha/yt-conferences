---
layout: default
title: "Django Asíncrono: Desbloqueando el Poder de la Programación Async - Luis Martinez"
nav_order: 31
parent: PyCon US 2025
type: Video Note
description: "The speaker, Luis Martínez, introduces the concepts of synchronous and asynchronous programming in Python using a restaurant analogy to illustrate how blocking I/O operations cause inefficiencies a..."
resource: "https://www.youtube.com/watch?v=pfxOrDx8Pwk"
youtube_stats:
  view_count: 474
  like_count: 17
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

The speaker, Luis Martínez, introduces the concepts of synchronous and asynchronous programming in Python using a restaurant analogy to illustrate how blocking I/O operations cause inefficiencies and scalability issues.
He explains that while traditional Python code waits for external responses, the `asyncio` module allows for concurrent task execution via an event loop, utilizing `async` and `await` keywords to manage pauses without blocking the entire application.
The presentation then focuses on Django's integration of asynchrony, noting that although the framework was originally built for synchronous WSGI, it now supports ASGI to enable async views and ORM methods prefixed with 'a'.
However, significant limitations remain, such as the inability to use standard transactions in async contexts, which requires workarounds like `sync_to_async` to run blocking code in separate threads.
Finally, the speaker demonstrates a practical example comparing synchronous and asynchronous API requests, showing that while async code improves performance by overlapping I/O waits, it does not execute tasks in true parallelism on a single thread, a nuance clarified during the Q&A session regarding the behavior of `await` versus `gather`.

# Main Points

|   # | Main point                                                                                                                                                              |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Synchronous programming blocks execution while waiting for I/O operations, similar to a waiter waiting for a chef to finish a dish before attending other tables.       |
|   2 | Python's default behavior causes accumulated slowness, potential blocking if APIs fail without timeouts, and poor scalability requiring additional servers or threads.  |
|   3 | Asynchronous programming uses the asyncio module to define tasks that execute in parallel, allowing the code to perform other actions while waiting for I/O responses.  |
|   4 | Key advantages of async code include handling more simultaneous requests, reducing wait times, and improving scalability without needing extra server instances.        |
|   5 | The event loop in asyncio manages a stack of tasks, checking for new tasks to execute or completed tasks to return values indefinitely.                                 |
|   6 | Web applications like Django traditionally use WSGI for synchronous execution, but running an event loop requires ASGI-compatible servers like Daphne or Uvicorn.       |
|   7 | Writing async Python code requires using the async keyword to define functions and the await keyword to pause execution during I/O operations.                          |
|   8 | The time.sleep function must be replaced with asyncio.sleep to maintain asynchronous behavior within the event loop.                                                    |
|   9 | Django began implementing async support in version 3.0, adding ASGI support in December 2019 and allowing async views in August 2020.                                   |
|  10 | Django's ORM supports async operations by adding an 'a' prefix to methods like aget and acreate, while filters remain synchronous as they return querysets.             |
|  11 | Async transactions are not directly supported in Django views, requiring the use of sync_to_async to execute synchronous transaction code in a separate thread.         |
|  12 | Using sync_to_async creates a new thread, which is less efficient than true asynchrony but necessary for compatibility with synchronous code.                           |
|  13 | The requests library is synchronous, so async HTTP calls require libraries like httpx to enable concurrent API requests.                                                |
|  14 | Performance tests show that async views reduce execution time compared to synchronous views when handling multiple external API requests.                               |
|  15 | Django's ORM compatibility with databases that do not support asynchrony limits the ability to fully migrate to async contexts without breaking backward compatibility. |
|  16 | Sequential await statements do not execute tasks simultaneously; using asyncio.gather is required to run multiple tasks concurrently.                                   |
|  17 | The event loop creates wait points for tasks, allowing other tasks to execute while waiting for I/O completion, rather than blocking the entire thread.                 |

# Video

[![Video thumbnail](https://img.youtube.com/vi/pfxOrDx8Pwk/hqdefault.jpg)](https://www.youtube.com/watch?v=pfxOrDx8Pwk)

[Watch on YouTube](https://www.youtube.com/watch?v=pfxOrDx8Pwk)
