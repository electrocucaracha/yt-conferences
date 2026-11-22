---
layout: default
title: "GopherCon 2025: Goroutines and Cells: Lessons in Goal-Directed Systems - Carlisia Campos"
nav_order: 2
parent: GopherCon 2025
type: Video Note
description: "Khalia Compos presents a talk exploring the application of biological principles, specifically decentralized goal pursuit observed in cell regeneration, to software engineering using Go routines."
resource: "https://www.youtube.com/watch?v=ddHxUhJoo1A"
youtube_stats:
  view_count: 1365
  like_count: 24
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

Khalia Compos presents a talk exploring the application of biological principles, specifically decentralized goal pursuit observed in cell regeneration, to software engineering using Go routines.
Inspired by research from Dr.
Michael Levin, who demonstrates that cells coordinate without central control, Compos developed a library called "emerge" that enables independent Go routine agents to synchronize and achieve collective goals.
The library utilizes a synchronization algorithm based on the Kuramoto model from physics to manage time-based workloads, such as API call batching and distributed load balancing, without requiring additional infrastructure or central schedulers.
Through a live simulation, the presentation visualizes how these agents adjust their timing to optimize efficiency, either by clustering for batch processing or distributing evenly for load balancing, depending on the specific goal.
Compos also outlines future plans for related libraries, "navigate" and "glue," which will handle search and failure diagnosis tasks, respectively, all grounded in the concept of decentralized, goal-based intelligence.

# Main Points

|   # | Main point                                                                                                                                                                                         |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker draws inspiration from biological research showing that cells pursue goals and communicate via bioelectrical signals without central control, such as in salamander limb regeneration. |
|   2 | This biological model of decentralized, goal-based coordination inspired the creation of a Go library named "emerge" that enables goroutines to synchronize and coordinate tasks.                  |
|   3 | The library uses a synchronization algorithm based on the Kuramoto model from physics to allow independent agents to coordinate without a central scheduler or orchestrator.                       |
|   4 | The core concept is collective problem solving where agents adjust their timing or phase to achieve a target coherence, optimizing workloads that require synchronization.                         |
|   5 | The "emerge" library is designed for time-based tasks such as batching API calls, distributed load balancing, consensus, and latency reduction.                                                    |
|   6 | For API batching, agents synchronize closely to accumulate tasks into larger, more efficient batches, whereas for load balancing, agents distribute themselves evenly to balance the workload.     |
|   7 | The library provides presets and a builder pattern to configure clients with specific goals, scales, and target coherence levels for different operational needs.                                  |
|   8 | A simulation package is included to visualize agent behavior, distinguishing between simulated workload data and real-time synchronization metrics from the emerge library.                        |
|   9 | The simulation displays a swarm of agents where their proximity to a central target indicates their synchronization status relative to the desired coherence.                                      |
|  10 | The speaker plans to develop two additional libraries: "navigate" for finding optimal configurations or paths, and "glue" for identifying parameter combinations causing system failures.          |
|  11 | The overall system is decentralized, requiring no additional infrastructure, and allows users to measure coherence gaps and optimize task execution based on biological principles.                |
|  12 | The speaker encourages users to explore the library's documentation, quick start guide, and repository to experiment with the synchronization mechanisms and provide feedback.                     |

# Video

[![Video thumbnail](https://img.youtube.com/vi/ddHxUhJoo1A/hqdefault.jpg)](https://www.youtube.com/watch?v=ddHxUhJoo1A)

[Watch on YouTube](https://www.youtube.com/watch?v=ddHxUhJoo1A)
