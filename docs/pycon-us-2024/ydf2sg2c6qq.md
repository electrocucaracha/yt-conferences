---
layout: default
title: "Talks - Vinícius Gubiani Ferreira: PEP 683: Immortal Objects - A new approach for memory managing"
nav_order: 183
parent: PyCon US 2024
type: Video Note
description: 'Venicius Goani Fera presents PEP 683, "Immortal Objects," a new approach to Python memory management designed to improve performance and resolve concurrency issues.'
resource: "https://www.youtube.com/watch?v=ydf2sg2C6qQ"
youtube_stats:
  view_count: 1143
  like_count: 18
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

Venicius Goani Fera presents PEP 683, "Immortal Objects," a new approach to Python memory management designed to improve performance and resolve concurrency issues.
The talk explains that standard Python objects rely on reference counting, which can lead to memory leaks, CPU cache invalidation, and data races when shared across threads or processes, particularly in pre-forking server architectures like those used by Instagram.
To address these problems, PEP 683 introduces "immortal objects"—such as `None`, `True`, `False`, and small integers—that are marked with a specific high reference count value, effectively making them immutable and exempt from garbage collection and the Global Interpreter Lock (GIL).
This change allows these objects to be safely shared across multiple threads and processes without the overhead of reference count adjustments, resulting in reduced memory consumption and increased shared memory usage in large-scale applications.
While the implementation introduces a slight performance trade-off of approximately 2% due to modified increment and decrement macros, it paves the way for future advancements like PEP 703, which aims to make the GIL optional by leveraging sub-interpreters and further utilizing the concept of immortal objects for true multicore parallel processing.

# Main Points

|   # | Main point                                                                                                                                                      |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Everything in Python is an object, defined by a type, value, and reference count.                                                                               |
|   2 | Python reuses existing objects for small integers and constants, resulting in shared memory addresses.                                                          |
|   3 | The garbage collector releases memory when a variable is reassigned, goes out of scope, or is explicitly deleted.                                               |
|   4 | Using sys.getrefcount is preferred over sys.getrefcount for accurate reference counting without creating temporary references.                                  |
|   5 | Threads and processes are used for concurrency, but sharing memory can lead to reference count errors and memory leaks.                                         |
|   6 | PEP 683 was created by Instagram engineers to address CPU cache invalidation, data races, and copy-on-write issues.                                             |
|   7 | CPU cache invalidation occurs when reference counts change, forcing the CPU to fetch data from main memory again.                                               |
|   8 | Data races can cause reference counts to fail reaching zero, leading to memory leaks, though the Global Interpreter Lock (GIL) currently prevents this.         |
|   9 | Copy-on-write mechanisms in operating systems can increase memory usage when shared objects are modified or their reference counts change.                      |
|  10 | PEP 683 proposes "Immortal objects" that remain unchanged throughout program execution to bypass reference counting.                                            |
|  11 | The term "Immortal" is used to distinguish these objects from standard immutable types like strings and tuples, which can still have changing reference counts. |
|  12 | Immortal objects are marked by setting the reference count field to a specific high value, effectively freezing it.                                             |
|  13 | Py_INCREF and Py_DECREF macros are modified to do nothing for Immortal objects, as their reference counts do not change.                                        |
|  14 | Examples of Immortal objects include None, True, False, empty strings, and small integers from -5 to 256.                                                       |
|  15 | Implementing PEP 683 results in decreased memory consumption and increased shared memory during high-request workloads.                                         |
|  16 | Immortal objects bypass the GIL, allowing safe sharing across threads and processes without data race concerns.                                                 |
|  17 | Challenges include ensuring backwards compatibility, preventing accidental immortality, and maintaining platform compatibility across different architectures.  |
|  18 | Performance degradation of roughly 2% was observed due to changes in reference counting macros, representing a trade-off between CPU and memory efficiency.     |
|  19 | PEP 684 introduces sub-interpreters to enable multicore parallel processing by isolating interpreter states.                                                    |
|  20 | PEP 703 makes the GIL optional, utilizing Immortal objects and introducing deferred and biased reference counting.                                              |
|  21 | A GIL-less Python version may be slower and requires recompiling libraries, with potential performance damage of up to 8% depending on the processor.           |
|  22 | Thread safety issues may emerge in existing code when the GIL is removed, requiring careful testing and static analysis.                                        |
|  23 | Library developers should expect feedback from users regarding compatibility and performance differences between GIL and non-GIL versions.                      |
|  24 | The list of Immortal objects is currently fixed but may expand in future releases based on usage frequency and memory efficiency criteria.                      |
|  25 | Creating custom Immortal objects currently requires modifying CPython code at the C level, with no direct Python API available yet.                             |
|  26 | Marking objects as Immortal is effectively a memory leak, so developers must exercise extreme caution to avoid unintended memory retention.                     |

# Video

[![Video thumbnail](https://img.youtube.com/vi/ydf2sg2C6qQ/hqdefault.jpg)](https://www.youtube.com/watch?v=ydf2sg2C6qQ)

[Watch on YouTube](https://www.youtube.com/watch?v=ydf2sg2C6qQ)
