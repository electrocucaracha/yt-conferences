---
layout: default
title: "GopherCon 2025: Plowing Through Data  Building Flexible Pipelines with Go - Mindy Ratcliff"
nav_order: 12
parent: GopherCon 2025
type: Video Note
description: "Mindy Ratcliffe, a software engineer at Bayer Crop Science, presents a talk at GopherCon on constructing quick and effective data pipelines using Go generics."
resource: "https://www.youtube.com/watch?v=R-P9Ltjc_uw"
youtube_stats:
  view_count: 2268
  like_count: 75
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

Mindy Ratcliffe, a software engineer at Bayer Crop Science, presents a talk at GopherCon on constructing quick and effective data pipelines using Go generics.
She explains that her team faces significant challenges in agricultural technology, including handling massive data volumes from fields and labs, maintaining rigid pipelines during critical harvest periods, and needing to rapidly adapt to changing business requirements.
Ratcliffe illustrates how traditional hardcoded pipelines lead to tight coupling, lack of reusability, and "copypaste crimes," making it difficult to add new data sources or transformations without extensive rewrites.
To solve this, her team developed an internal package leveraging Go generics to create a composable, type-safe pipeline infrastructure that separates business logic from infrastructure concerns.
This approach allows engineers to easily chain generic handlers for ingestion, transformation, and storage, enabling the team to build flexible, maintainable, and scalable data pipelines that can grow with their needs rather than being constantly rebuilt.

# Main Points

|   # | Main point                                                                                                                                                 |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Mindy Ratcliffe presented at GopherCon in New York City, discussing the creation of quick and effective data pipelines using Go generics.                  |
|   2 | The speaker transitioned from a career in English teaching to Bayer Crop Science, where she values communication, creativity, and empathy.                 |
|   3 | Bayer Crop Science handles massive amounts of data from fields, labs, and controlled environments to measure seed efficacy and effectiveness.              |
|   4 | The team of 18 manages 36 APIs, four distributed systems, and 23 asynchronous message processors, serving over 100 internal services.                      |
|   5 | Data throughput spikes significantly during harvest and advancement periods, requiring rapid service adjustments and flexible pipelines.                   |
|   6 | Key challenges include maintaining services during hectic times, debugging quickly, and adding new functionality without blocking R&D.                     |
|   7 | A common initial approach involves hardcoding pipeline functions to specific types, such as soil samples, which leads to rigidity and lack of reusability. |
|   8 | Hardcoded pipelines mix business and infrastructure logic, resulting in tight coupling and "copypaste crimes" when new data types are introduced.          |
|   9 | To solve these issues, the team consolidated pipeline functionality into an internal package using Go generics for maximum reuse.                          |
|  10 | This approach separates infrastructure from business logic, allowing for compile-time safe, reusable, and abstracted code.                                 |
|  11 | The pipeline package includes generic handlers, a feed struct, and functions like start, pipe, and end to manage data flow.                                |
|  12 | The start function reads data from a source, while the pipe function streams data through processing stages using go routines.                             |
|  13 | The end function consumes the final channel of data, completing the pipeline process similar to building a sandwich.                                       |
|  14 | This generic model allows any input or output type, such as strings, structs, or protobufs, to use the same pipeline logic.                                |
|  15 | The new architecture is highly composable, enabling engineers to add new stages or functionality by simply inserting another pipe.                         |
|  16 | Benefits include decoupled error handling, clean separation of concerns, and the ability to handle fluctuating business needs.                             |
|  17 | The solution empowers engineers of all levels to build and adjust pipelines swiftly without rewriting tightly coupled code.                                |
|  18 | Investing time upfront in generic infrastructure allows the team to grow data pipelines rather than constantly rebuilding them.                            |
|  19 | The speaker emphasized that leveraging Go generics helps the team avoid fighting the language and supports idiomatic, performant solutions.                |

# Video

[![Video thumbnail](https://img.youtube.com/vi/R-P9Ltjc_uw/hqdefault.jpg)](https://www.youtube.com/watch?v=R-P9Ltjc_uw)

[Watch on YouTube](https://www.youtube.com/watch?v=R-P9Ltjc_uw)
