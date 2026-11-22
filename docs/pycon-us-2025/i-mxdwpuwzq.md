---
layout: default
title: "What's New in the Linux Kernel... from Python - Geoffrey Thomas"
nav_order: 93
parent: PyCon US 2025
type: Video Note
description: Dr.
resource: "https://www.youtube.com/watch?v=i-mXdwPUwzQ"
youtube_stats:
  view_count: 2476
  like_count: 72
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

Dr.
Jeffrey Thomas presents a talk on utilizing new Linux kernel features from Python, clarifying that the focus is on accessing kernel APIs rather than writing the kernel itself.
He begins by demonstrating how to use the `F_CREATED_QUERY` operation, introduced in kernel 6.12, to determine if a file was newly created or already existed, a feature requested by systemd to resolve race conditions.
By searching the kernel source code, he identifies the necessary constant and implements a simple Python wrapper using the `fcntl` module to retrieve this status.
The presentation then explores a more complex API, `procmap_query`, added in kernel 6.11, which provides binary access to process memory mappings, offering a robust alternative to parsing the text-based `/proc/self/maps` file.
To implement this, Thomas explains the use of Python’s `struct` module for packing and unpacking binary data according to C structure definitions and the `ctypes` module for managing memory buffers and obtaining pointers.
He further details how to derive architecture-specific ioctl constants by compiling a small C helper program, as these values cannot be easily evaluated in Python alone.
The talk concludes with resources for tracking kernel changes, such as LWN and kernelnewbies.org, and discusses advanced interoperability options like CFFI, Cython, and PyO3 for developers requiring deeper integration or performance.

# Main Points

|   # | Main point                                                                                                                                            |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The talk focuses on using new Linux kernel features from Python rather than writing the kernel in Python.                                             |
|   2 | The kernel API is defined in C, requiring minimal C knowledge to access new features directly from Python.                                            |
|   3 | A new `fcntl` operation, `F_CREATED_QUERY`, allows applications to determine if a file opened with `O_CREAT` was actually created or already existed. |
|   4 | This feature was added to address a problem faced by systemd regarding reliable file creation status.                                                 |
|   5 | The `F_CREATED_QUERY` constant value is derived from kernel source code as `F_LINUX_SPECIFIC_BASE + 4`, which equals 1028.                            |
|   6 | Python's `fcntl` module does not yet document this new operation, requiring users to search kernel source code for implementation details.            |
|   7 | Tools like GitHub code search, Sourcegraph, and `git grep` are effective for finding undocumented kernel features in source code.                     |
|   8 | The `proc` filesystem exposes kernel information as plain text files, enabling tools like `ps` and `top` to function.                                 |
|   9 | Reading `/proc/self/maps` provides a list of memory mappings and loaded libraries for the current process.                                            |
|  10 | Parsing text-based proc files can be error-prone due to special characters in filenames, motivating the need for binary APIs.                         |
|  11 | Kernel 6.11 introduced a binary API for querying process memory maps to improve performance and reliability for profilers.                            |
|  12 | This binary API uses a C structure with input and output fields, requiring manual memory management for buffers.                                      |
|  13 | Python's `struct` module is used to pack and unpack data between Python objects and binary byte sequences.                                            |
|  14 | Byte order (endianness) must be considered when packing data, with the native order typically used for local kernel interactions.                     |
|  15 | The `ioctl` system call is used to invoke the binary proc map query, as it handles file-type-specific operations.                                     |
|  16 | Constants for `ioctl` operations are architecture-specific and may require compiling a small C program to determine their integer values.             |
|  17 | The `ctypes` module is used to create memory buffers and obtain their addresses for passing to kernel system calls.                                   |
|  18 | A loop using the `PROC_MAP_QUERY_NEXT_VMA` flag allows iterating through all virtual memory areas of a process.                                       |
|  19 | The `PROC_MAP_QUERY_FILEBACKED_VMA` flag filters results to include only file-backed mappings, such as shared libraries.                              |
|  20 | LWN and kernelnewbies.org are recommended resources for tracking new Linux kernel features and changes.                                               |
|  21 | Alternative approaches for accessing C APIs from Python include CFFI, Cython, and writing extension modules in C or Rust.                             |
|  22 | CFFI can compile C code to automatically handle struct offsets and alignment, reducing manual error risk.                                             |
|  23 | Checking if a file exists before opening it is unreliable in multi-process environments, making kernel-provided status queries necessary.             |

# Video

[![Video thumbnail](https://img.youtube.com/vi/i-mXdwPUwzQ/hqdefault.jpg)](https://www.youtube.com/watch?v=i-mXdwPUwzQ)

[Watch on YouTube](https://www.youtube.com/watch?v=i-mXdwPUwzQ)
