---
layout: default
title: "GopherCon 2025: My Protobuf Module is Faster than Yours (Because I Cheated) - Tom Lyons"
nav_order: 14
parent: GopherCon 2025
type: Video Note
description: "Tom, a senior engineer at CrowdStrike, presents a custom Protobuf decoder designed to handle the extreme throughput of 35 million messages per second, where standard libraries incur excessive CPU a..."
resource: "https://www.youtube.com/watch?v=eWZ8pNMpqcU"
youtube_stats:
  view_count: 1968
  like_count: 63
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

Tom, a senior engineer at CrowdStrike, presents a custom Protobuf decoder designed to handle the extreme throughput of 35 million messages per second, where standard libraries incur excessive CPU and memory costs due to frequent allocations.
To achieve zero allocations in steady state, the team implemented several optimizations, including pre-validating definitions to avoid recursive checks on every decode cycle and using `sync.Pool` to reuse result structures and field slices.
They further improved efficiency by replacing maps with sorted slices for binary search lookups and leveraging Go’s `unsafe` package to convert byte slices to strings without copying memory, a feature that is disabled by default to ensure safety.
While these techniques significantly outperform standard decoders and reduce infrastructure costs, Tom strongly advises against adopting such complex, unsafe optimizations unless the scale of operations justifies the high maintenance burden and risk of memory corruption.

# Main Points

|   # | Main point                                                                                                                                    |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Tom from CrowdStrike developed a custom protobuf decoder to handle 35 million messages per second efficiently.                                |
|   2 | Protobuf is a sequential, machine-readable format that is significantly smaller than JSON, reducing network overhead.                         |
|   3 | The decoder supports dynamic parsing without requiring static Go struct definitions, allowing for flexible event processing.                  |
|   4 | Definition validation was moved out of the hot path by creating a reusable decoder instance that validates the schema only once.              |
|   5 | A sync.Pool was implemented to reuse result and field pointers, eliminating allocations in steady state.                                      |
|   6 | Callers must explicitly close results to return them to the pool, preventing pointer collisions and memory corruption.                        |
|   7 | Maps were replaced with sorted slices for tags and fields to improve iteration speed and enable binary search lookups.                        |
|   8 | Unsafe conversions were used to avoid copying byte slices into strings, reusing underlying memory when safe.                                  |
|   9 | Pre-allocated slices for booleans, floats, and integers within field structures prevented repeated memory allocations.                        |
|  10 | These optimizations achieved zero allocations in steady state, outperforming standard protobuf decoders.                                      |
|  11 | The speaker advises against adopting these techniques unless allocation costs exceed engineering salaries due to high maintenance complexity. |
|  12 | Unsafe modes are disabled by default to ensure safety for general library users and prevent memory corruption.                                |
|  13 | The code relies on rigorous internal code reviews and trusted users to manage the risks of unsafe memory operations.                          |

# Video

[![Video thumbnail](https://img.youtube.com/vi/eWZ8pNMpqcU/hqdefault.jpg)](https://www.youtube.com/watch?v=eWZ8pNMpqcU)

[Watch on YouTube](https://www.youtube.com/watch?v=eWZ8pNMpqcU)
