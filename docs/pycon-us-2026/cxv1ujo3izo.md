---
layout: default
title: "Memory management in CPython, fast or slow? - Mark Shannon"
nav_order: 35
parent: PyCon US 2026
type: Video Note
description: "This transcript provides a detailed overview of CPython’s memory management, focusing on object lifetimes, reference counting, and the internal mechanisms of allocation and deallocation."
resource: "https://www.youtube.com/watch?v=Cxv1ujO3izo"
youtube_stats:
  view_count: 379
  like_count: 10
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

This transcript provides a detailed overview of CPython’s memory management, focusing on object lifetimes, reference counting, and the internal mechanisms of allocation and deallocation.
It explains that while Python uses reference counting to determine when objects are no longer reachable, the actual memory management relies on a hierarchy of free lists, pages, and arenas to efficiently handle memory chunks without moving them, which is crucial for C extensions.
The speaker highlights current inefficiencies, such as memory fragmentation, the overhead of retrieving thread state for every allocation, and the limited effectiveness of class-specific free lists, which only handle about half of all allocations.
Proposed improvements include transitioning to size-class-based free lists to reduce fragmentation and increase the hit rate for fast allocations, as well as leveraging JIT compiler optimizations like unboxing integers and floats to eliminate unnecessary object creation.
Finally, the talk addresses the limitations of reference counting regarding cyclic references and explains how the cyclic garbage collector identifies and frees unreachable objects by adjusting reference counts and performing a transitive closure.

# Main Points

|   # | Main point |
| --: | ---------- |
|   1 | CPython object lifecycle involves allocation via `__new__`, initialization via `__init__`, and cleanup via `__del__`, with explicit freeing handled implicitly by the VM. |
|   2 | Reference counting determines object liveness; objects are deallocated when their reference count reaches zero, making them unreachable garbage. |
|   3 | Memory allocation primarily uses free lists, which are linked lists of pre-allocated memory chunks, to avoid moving memory and accommodate C extensions. |
|   4 | Free lists are finite and require fallback mechanisms; when empty or full, CPython allocates from pages, which are fixed-size chunks of memory usually 4 kilobytes. |
|   5 | Pages are grouped into arenas, currently 2 megabytes in size, which serve as the interface for requesting memory from the operating system. |
|   6 | Each page contains chunks of a uniform size class; CPython defines 32 size classes ranging from 16 to 256 bytes, with larger allocations using the system allocator. |
|   7 | Allocation from a page involves taking a chunk from its internal free list, while deallocation returns the chunk to the list, leading to potential fragmentation. |
|   8 | Three types of fragmentation exist: internal fragmentation within chunks, external fragmentation from unused chunks in pages, and leftover space from imperfect division. |
|   9 | Thread state holds free list information; in free-threaded builds, free lists are per-thread to reduce contention, whereas default builds use per-interpreter pointers. |
|  10 | Inefficiencies arise from the C API requiring thread state retrieval for allocation and freeing, which is expensive due to dynamic linking and thread-local storage access. |
|  11 | Current CPython uses 41 distinct free lists for specific types like tuples and floats, but only about half of allocations utilize them, forcing others to use the slower page/arena path. |
|  12 | Reference count elision optimizes stack-based references by omitting counts for lower stack frames that outlive higher ones, removing up to 90% of unnecessary reference tracking. |
|  13 | Future improvements include consolidating free lists by size class rather than object type to reduce fragmentation and increase the percentage of allocations served by free lists. |
|  14 | Fast allocation paths check free list pointers directly, while slow paths handle empty lists; debug features like trace malloc can force slow paths by setting capacities to zero. |
|  15 | JIT compilers can optimize memory usage by unboxing integers and floats and eliminating tuple allocations for simple pair returns, reducing object creation overhead. |
|  16 | Cyclic garbage collection resolves reference cycles by temporarily decrementing reference counts for internal heap references to identify unreachable objects. |
|  17 | The GC algorithm performs a transitive closure from live external references to restore correct reference counts, then frees objects that remain at zero. |
|  18 | Free lists store pre-initialized class pointers, requiring only a single write for the class during allocation, which is efficient compared to full object re-initialization. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/Cxv1ujO3izo/hqdefault.jpg)](https://www.youtube.com/watch?v=Cxv1ujO3izo)

[Watch on YouTube](https://www.youtube.com/watch?v=Cxv1ujO3izo)
