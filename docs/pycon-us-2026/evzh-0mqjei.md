---
layout: default
title: "Scaling Python to Saturate the Hypercube (Sponsor: Hudson River Trading)"
nav_order: 103
parent: PyCon US 2026
type: Video Note
description: "Hasham, manager of the Python infrastructure team at Hudson River Trading (HRT), introduces the firm’s algorithmic trading operations, which process massive data volumes to provide liquidity and pr..."
resource: "https://www.youtube.com/watch?v=EvzH-0MqJEI"
youtube_stats:
  view_count: 558
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

Hasham, manager of the Python infrastructure team at Hudson River Trading (HRT), introduces the firm’s algorithmic trading operations, which process massive data volumes to provide liquidity and price discovery across global markets.
He explains that HRT’s mission to "saturate the hyper cube" drives their engineering culture, leading to significant investments in Python infrastructure, including a custom type checker, lazy imports for Python 3.12, and a shift from C++ to Python for data science and research.
The presentation then features deep dives by colleagues Shinuan and Yuttian, who detail their distributed compute API that mimics `concurrent.futures` but executes tasks on a massive cluster, utilizing optimizations like batching, worker tagging, and fork servers to minimize overhead.
Jia discusses the evolution of HRT’s testing harness, which now uses static analysis and a custom FUSE filesystem to track dependencies and run only affected tests, significantly improving developer workflow efficiency.
Finally, Tim shares an anecdote about migrating C++ bindings from Boost.Python to Pybind11 and then to Nanobind, illustrating how HRT adapts its engineering strategies to scale with organizational growth and technical needs.

# Main Points

|   # | Main point |
| --: | ---------- |
|   1 | Hudson River Trading (HRT) is an algorithmic trading firm founded in 2002 by Harvard and MIT graduates, currently employing approximately 1,200 people. |
|   2 | The company trades stocks, bonds, and futures across over 200 global markets, accounting for 15% of all US equities trades daily. |
|   3 | HRT’s unofficial mission is to "saturate the hyper cube," meaning they aim to trade everything, everywhere, and all the time using fully automated models without human intervention. |
|   4 | The firm provides market liquidity and facilitates price discovery by ingesting massive amounts of raw data feeds from exchanges to predict price movements. |
|   5 | HRT operates its own data centers, including a power-efficient facility in Norway built in an old mine and chilled by fjord water. |
|   6 | The company transitioned from a C++-centric shop to heavily utilizing Python, driven by the data science ecosystem and explosive growth in Python codebase size. |
|   7 | Key Python milestones include completing the Python 3 upgrade in 2020, forming a dedicated Python infrastructure team in 2021, and contributing to the lazy imports PEP for Python 3.12. |
|   8 | HRT is a PSF visionary sponsor and is increasing its open-source contributions and donations to the Python ecosystem. |
|   9 | The distributed compute API mimics the concurrent futures interface but executes tasks on a massive internal cluster rather than local subprocesses. |
|  10 | Optimizations for distributed computing include batching short-running jobs to reduce overhead, tagging futures to reuse in-memory states on the same worker, and running child futures as subprocesses on the parent machine to prevent scheduler deadlocks. |
|  11 | A custom UI tracks millions of in-flight jobs using a tree view, with state events written to NFS and pushed to a sharded PostgreSQL database for visualization. |
|  12 | Progress tracking for long-running tasks uses a shared memory segment exposed via C++ and nanobind, allowing cheap atomic writes for progress bars. |
|  13 | The system relies heavily on Python pickles for job serialization, using custom logic to handle main module references and splice pickle statements for import path setup. |
|  14 | To combat slow imports in short-running jobs, HRT uses a fork server paradigm that preloads all necessary libraries, making process creation nearly instantaneous. |
|  15 | The internal testing harness, Auto Test, orchestrates parallel test runs across the cluster and integrates with pytest and C++ frameworks. |
|  16 | Dependency tracking was added to Auto Test to skip unaffected tests, using static analysis via internal Tango tools to build a dependency graph without requiring manual annotations. |
|  17 | The dependency graph generation was rewritten in Rust and C++ to improve speed, and validation is performed using a custom FUSE filesystem to sandbox test environments. |
|  18 | HRT migrated its C++ to Python bindings from Boost.Python to Pybind11, and is currently converting to nanobind to address performance and complexity issues. |
|  19 | The nanobind conversion is being done incrementally over several years, with modifications to both libraries to allow them to coexist during the transition. |
|  20 | The organization emphasizes that engineering strategies must evolve with company size, shifting from big-bang rewrites to sustainable, incremental improvements as the team grows. |
|  21 | HRT uses a mix of on-premise and cloud infrastructure, collocating with markets where possible and leveraging cloud providers for hardware acquisition when beneficial. |
|  22 | The company is rebuilding many upstream PyPI wheels in-house to create a more coherent, faster, and less redundant Python environment for developers. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/EvzH-0MqJEI/hqdefault.jpg)](https://www.youtube.com/watch?v=EvzH-0MqJEI)

[Watch on YouTube](https://www.youtube.com/watch?v=EvzH-0MqJEI)
