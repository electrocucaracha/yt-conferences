---
layout: default
title: "Sponsor Presentations - Rethinking How We're Linking: What to do when speeding... (Sponsor: Meta)"
nav_order: 41
parent: PyCon US 2024
type: Video Note
description: "Lauren, a software engineering manager at Meta, presents a technical talk on optimizing Python application performance by statically linking C extensions into the interpreter."
resource: "https://www.youtube.com/watch?v=TsnMD354q6w"
youtube_stats:
  view_count: 635
  like_count: 10
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

Lauren, a software engineering manager at Meta, presents a technical talk on optimizing Python application performance by statically linking C extensions into the interpreter.
She demonstrates that while C extensions significantly outperform pure Python implementations for data-intensive tasks, importing large numbers of these extensions causes severe slowdowns due to the expensive dynamic loading of shared objects via `dlopen`.
To address this, she explains the process of embedding C extensions directly into the Python binary using the `PyImport_AppendInittab` API, which eliminates the need for dynamic linking and drastically reduces import times for applications with thousands of modules.
The presentation also covers the trade-offs of static linking, including faster runtime data access and smaller binary sizes due to linker optimizations, while acknowledging that startup times for small applications may increase due to larger initial binary loads.
Finally, she addresses the challenge of symbol collisions when statically linking multiple extensions by using tools like `llvm-objcopy` to rename conflicting symbols, ensuring that distinct modules can coexist within a single statically linked binary.

# Main Points

|   # | Main point                                                                                                                                          |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker, Lauren, is a software engineering manager at Meta working on the Python language foundation.                                           |
|   2 | The talk focuses on statically linking C extensions into Python applications to improve performance.                                                |
|   3 | Implementing this at Instagram saved approximately 2 megawatts of energy, equivalent to the usage of 1,600 homes.                                   |
|   4 | The solution has been rolled out to over 990,000 applications, saving more than 5,000 hours of build time per week.                                 |
|   5 | A banana order counting example demonstrates that C implementations are significantly faster than pure Python for multiple lookups.                 |
|   6 | Python C extensions are shared libraries on disk that require a PyInit function to initialize the module.                                           |
|   7 | Building C extensions requires compiling with the Python header and linking against the correct shared libraries.                                   |
|   8 | Importing many C extensions is slow because the dl_open function, which loads shared objects, consumes about 92% of the time.                       |
|   9 | Static linking copies code and data directly into the binary, avoiding the overhead of loading shared objects at runtime.                           |
|  10 | Dynamic linking uses shared objects, which can cause performance issues due to expensive lookups and data relocations.                              |
|  11 | An analogy compares static linking to having all ingredients at a cooking station and dynamic linking to fetching them from a shared fridge.        |
|  12 | Embedding C extensions involves using PyImport_AppendInittab to register modules as built-ins.                                                      |
|  13 | Embedded extensions allow importing modules without loading shared objects from disk, significantly speeding up imports.                            |
|  14 | Benchmarking shows that importing 8,000 embedded C extensions is much faster than importing the same number of dynamic ones.                        |
|  15 | Static linking allows the linker to optimize binaries by including only necessary symbols, resulting in smaller output files.                       |
|  16 | Data relocations, which are costly during dynamic import, are avoided with static linking, improving runtime performance.                           |
|  17 | Symbol collisions can occur when statically linking multiple extensions with identical function names.                                              |
|  18 | The tool llvm-obj-copy can be used to rename symbols in object files to resolve collisions.                                                         |
|  19 | Using a generated C++ map for lookups instead of a linear init tab further improves import speed.                                                   |
|  20 | The build tool used at Meta, Buck2, facilitates these optimizations and handles the complex linking process.                                        |
|  21 | Static linking may increase startup time for small applications due to larger binary sizes but improves overall efficiency for large-scale systems. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/TsnMD354q6w/hqdefault.jpg)](https://www.youtube.com/watch?v=TsnMD354q6w)

[Watch on YouTube](https://www.youtube.com/watch?v=TsnMD354q6w)
