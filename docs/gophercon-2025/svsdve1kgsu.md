---
layout: default
title: "GopherCon 2025: An Operating System in Go - Patricio Whittingslow"
nav_order: 19
parent: GopherCon 2025
type: Video Note
description: 'Patricia Orderingslow presents a talk on the concept of "GOOS=NOOS," a proposed change to the Go runtime that enables bare-metal support by eliminating dependencies on an operating system.'
resource: "https://www.youtube.com/watch?v=SvsdVe1kgSU"
youtube_stats:
  view_count: 12105
  like_count: 507
  channel_subscriber_count: 41100
tags:
  - gophercon-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-21T05:22:37+00:00
---

# Summary

Patricia Orderingslow presents a talk on the concept of "GOOS=NOOS," a proposed change to the Go runtime that enables bare-metal support by eliminating dependencies on an operating system.
She explains that while standard Go programs rely on OS syscalls for tasks like TCP connections, embedded systems often require direct hardware control, which is currently achieved through projects like TinyGo, Tamago, and the Embedded Go project.
Orderingslow highlights academic benchmarks showing that TinyGo generates significantly smaller executables than Rust or C and offers jitter-free, constant-time performance, making it highly suitable for real-time applications on microcontrollers.
She argues that TinyGo effectively performs many operating system tasks, such as multicore processing and networking, without the configuration overhead or complexity associated with traditional embedded OSs like FreeRTOS.
Finally, she shares practical wisdom for embedded Go developers, including idioms for avoiding heap allocations and using the `print alloc` flag to monitor memory usage, emphasizing that Go’s design principles are well-suited for software engineering in resource-constrained environments.

# Main Points

|   # | Main point                                                                                                                                                           |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The GOOS environment variable tells the Go compiler which operating system the program targets, influencing low-level system calls like dial TCP.                    |
|   2 | A proposal exists to add bare-metal support to the Go runtime, eliminating the dependency on an operating system for specific tasks.                                 |
|   3 | Bare-metal Go allows programs to run directly on microcontroller units (MCUs) without an OS, giving users control over hardware limits and potentially removing Cgo. |
|   4 | Embedded Go projects like TinyGo, Tamago, and the Embedded Go project focus on stripping OS dependencies to target small devices and WebAssembly.                    |
|   5 | Academic benchmarks indicate TinyGo executables are significantly smaller than Rust and C, though performance may be slightly slower in some cryptographic tests.    |
|   6 | TinyGo programs exhibit zero jitter compared to languages running on FreeRTOS, providing constant execution time suitable for real-time embedded systems.            |
|   7 | TinyGo supports multicore processing, goroutines, and a userspace networking stack on MCUs, approaching the functionality of traditional embedded operating systems. |
|   8 | The speaker advocates for Go in embedded systems due to its lightweight nature, lack of configuration overhead, and focus on software engineering principles.        |
|   9 | A "reuse slice" idiom is recommended to avoid heap allocations by reusing underlying memory buffers when capacity is sufficient.                                     |
|  10 | Generational indices are a useful pattern for invalidating multiple pointers to an object simultaneously, which is critical for networking stacks and file systems.  |
|  11 | TinyGo can detect heap allocations using the print allocs flag, revealing that even simple programs have baseline allocations for stacks and task data.              |
|  12 | The embedded Go ecosystem is growing, with contributors actively developing support for various development boards and microcontroller architectures.                |

# Video

[![Video thumbnail](https://img.youtube.com/vi/SvsdVe1kgSU/hqdefault.jpg)](https://www.youtube.com/watch?v=SvsdVe1kgSU)

[Watch on YouTube](https://www.youtube.com/watch?v=SvsdVe1kgSU)
