---
layout: default
title: Building an open compute ecosystem  a software stack to enable AI tasks to run on any AI infrastruct
nav_order: 136
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Chu Jao from China Mobile presents a solution to the fragmentation of AI hardware ecosystems, arguing that the dominance of NVIDIA CUDA stems from its robust software stack rather than just hardwar..."
resource: "https://www.youtube.com/watch?v=FIs7aDeIhMc"
youtube_stats:
  view_count: 28
  channel_subscriber_count: 46800
tags:
  - openinfra-summit-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T23:38:50+00:00
---

# Summary

Chu Jao from China Mobile presents a solution to the fragmentation of AI hardware ecosystems, arguing that the dominance of NVIDIA CUDA stems from its robust software stack rather than just hardware performance.
He highlights the inefficiencies caused by "silos" in current AI infrastructure, where developers must rewrite code for different accelerators, leading to low utilization rates for non-NVIDIA hardware and complex resource planning for cloud providers.
To address this, China Mobile has developed "Kana" (Cross Architecture Migrating Application), a software stack designed to function like an "Android for AI," enabling applications to run on any heterogeneous accelerator without code rewriting.
The system achieves this through four key technologies: computing resource abstraction, an adaptive runtime that manages multiple vendor runtimes, a unified programming model allowing single-source code development, and cross-architecture compilation that translates code into a standard intermediate representation.
The resulting "Shinhu" platform supports live migration of applications across eight types of AI accelerators, including NVIDIA, Intel, and AMD, with a migration time of under 20 seconds and over 95% source-to-source conversion accuracy, with plans to open-source the platform under the OCF working group.

# Main Points

|   # | Main point                                                                                                                                                                                                |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The session presents a software stack to enable AI tasks to run on any AI infrastructure, addressing the dominance of Nvidia GPUs and the need for heterogeneous accelerator support.                     |
|   2 | Hardware performance alone is insufficient; a robust software ecosystem, similar to Android's success over iOS, is critical for developer adoption and market share.                                      |
|   3 | Users choose heterogeneous hardware based on specific requirements, such as general computing, gaming, deep learning, cost efficiency, or high performance.                                               |
|   4 | Current AI frameworks and hardware tool chains operate in silos, causing significant challenges for application developers who must rewrite code when migrating between different accelerators.           |
|   5 | These silos create resource planning and utilization dilemmas for operators and cloud service providers, who struggle to balance diverse hardware needs with low utilization rates on less popular chips. |
|   6 | New hardware manufacturers face a dilemma between following the Nvidia ecosystem or creating new ones, which limits their ability to gain customers and ecosystem support.                                |
|   7 | China Mobile is developing a tool chain named Kana, which stands for Cross Architecture Migrating Application, to act as an Android-like operating system for intelligent computing.                      |
|   8 | The goal of Kana is to allow developers to write code once and compile it once, enabling execution on multiple vendor and multi-type accelerators without rewriting code.                                 |
|   9 | The core implementation involves building a unified and abstracted hardware model and defining standard runtime interfaces for heterogeneous accelerators.                                                |
|  10 | An adaptive runtime layer is injected between the framework and hardware layers to hide hardware differences and manage various vendor-specific runtimes without replacing them.                          |
|  11 | A unified programming model allows developers to write single-source code for heterogeneous hardware, eliminating the need to switch between host and device-specific languages like CUDA.                |
|  12 | Cross-architecture compilation uses LLVM and MLIR to compile single-source code into a standard intermediate representation called a native program.                                                      |
|  13 | This native program, which follows the ELF structure, can be adaptively linked and executed on different hardware runtimes by the adaptive runtime system.                                                |
|  14 | Implementing cross-architecture support at the framework level is deemed impractical due to the countless APIs and use cases, whereas the toolchain level provides a scalable solution.                   |
|  15 | The computing resource abstraction follows the OpenCL model but upgrades it by launching tasks containing multiple kernels and using a unified shared memory zone for data transfer.                      |
|  16 | The adaptive runtime manages all vendor runtimes, adaptively loading and linking the relevant intermediate representation to the specific device runtime for execution.                                   |
|  17 | The platform, named Shinhu, includes four major components: unified programming skills, source-to-source conversion tools, a cross-architecture compiler, and an adaptive runtime.                        |
|  18 | The Shinhu platform has been adapted to eight types of AI accelerators, including Nvidia, Intel, AMD, Ascend, and other Chinese chips.                                                                    |
|  19 | Live migration of applications across these eight accelerator types takes less than 20 seconds, and the source-to-source conversion tool achieves over 95% translation accuracy.                          |
|  20 | The team is planning to open-source the entire Shinhu platform under the OCF working group, with some components already available and full source code expected later this year or next year.            |

# Video

[![Video thumbnail](https://img.youtube.com/vi/FIs7aDeIhMc/hqdefault.jpg)](https://www.youtube.com/watch?v=FIs7aDeIhMc)

[Watch on YouTube](https://www.youtube.com/watch?v=FIs7aDeIhMc)
