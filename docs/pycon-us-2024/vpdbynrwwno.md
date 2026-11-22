---
layout: default
title: "Talks - Kevin Kho, Han Wang: Speed is Not All You Need for Data Processing"
nav_order: 168
parent: PyCon US 2024
type: Video Note
description: 'The session "Speed is not all you need for data processing" by Kevin Cole and Han Wang argues that raw speed benchmarks are often misleading and context-dependent, frequently designed to favor spec...'
resource: "https://www.youtube.com/watch?v=VpDbynrwwNo"
youtube_stats:
  view_count: 291
  like_count: 3
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

The session "Speed is not all you need for data processing" by Kevin Cole and Han Wang argues that raw speed benchmarks are often misleading and context-dependent, frequently designed to favor specific tools rather than reflect real-world utility.
The speakers demonstrate how minor changes in query structure or problem definitions can drastically alter performance rankings between frameworks like Pandas, Polars, DuckDB, and Spark, highlighting that absolute time differences often matter more than relative speedups.
They critique the industry's focus on exclusive tool adoption, noting that vendors push benchmarks to drive conversion, while ignoring critical factors such as developer experience, ecosystem maturity, testability, and total infrastructure costs.
Instead of choosing a single "best" tool, the presenters advocate for a flexible "tool belt" approach that leverages the strengths of both local and distributed engines.
To facilitate this, they introduce Fug, an open-source abstraction layer that allows developers to write code once in Python or SQL and seamlessly execute it across different backends, thereby combining local developer productivity with distributed scalability.

# Main Points

|   # | Main point                                                                                                                                                      |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The data tooling landscape includes small data tools like pandas, Polars, and DuckDB, and big data tools like Spark, Dask, Ray, and Snowflake.                  |
|   2 | Speed benchmarks are prevalent on social media, but results can be misleading if the context is not carefully controlled.                                       |
|   3 | Benchmark outcomes can be manipulated by tweaking the context, such as changing the order of filtering operations or altering specific requirements.            |
|   4 | A benchmark showing Pandas as slow can be reversed by optimizing code structure, demonstrating that good code can significantly improve performance.            |
|   5 | Polars can appear much faster than DuckDB and Pandas in specific scenarios, but the absolute time difference may be negligible for large datasets.              |
|   6 | Spark can process 100GB of data in under a minute using window functions, while DuckDB may run out of memory on the same task.                                  |
|   7 | Changing a requirement from exact sampling to rough sampling can make DuckDB faster than Spark, highlighting the importance of specific use cases.              |
|   8 | The H2O Benchmark excludes I/O time, scientific computing capabilities, and distributed scenarios, limiting its applicability to real-world comparisons.        |
|   9 | Vendors often push benchmarks to drive adoption of their platforms, leading to competitive disputes between companies like Databricks and Snowflake.            |
|  10 | Tools are not mutually exclusive; Snowflake suits data analysts, while Databricks suits data scientists, and they can be used together.                         |
|  11 | Different workloads require different tools; non-urgent pipelines may use big data tools, while parallel machine learning tasks may need distributed compute.   |
|  12 | No single tool is best across all data scales; local tools like Polars and DuckDB excel on single machines, while Spark and Dask excel in distributed clusters. |
|  13 | Benchmarks constrained to SQL interfaces exclude non-SQL operations like matrix calculations, which are common in Python-based workflows.                       |
|  14 | Factors beyond speed, such as ecosystem, developer experience, testability, and scalability, are critical for tool adoption.                                    |
|  15 | Local tools like Pandas and DuckDB fail to scale beyond a single machine, necessitating distributed frameworks for larger workloads.                            |
|  16 | Relative speed improvements, such as 10x faster, may not translate to significant absolute time savings for most data pipelines.                                |
|  17 | Optimizing existing code is often more effective than switching frameworks, and total project cost includes both developer and infrastructure expenses.         |
|  18 | Abstraction layers like Fug allow code written for local engines to be ported to distributed engines like Spark or Dask.                                        |
|  19 | Fug SQL provides an engine-agnostic representation of logic, supporting keywords like load, save, and persist to access underlying engine capabilities.         |
|  20 | Combining Python and SQL in Fug allows for concise code that works across different execution engines, reducing maintenance overhead.                           |
|  21 | The focus should be on the full package of developer productivity, testability, and scalability rather than just raw speed.                                     |
|  22 | Abstraction layers decouple logic from execution, enabling the best of both worlds for small and big data processing.                                           |

# Video

[![Video thumbnail](https://img.youtube.com/vi/VpDbynrwwNo/hqdefault.jpg)](https://www.youtube.com/watch?v=VpDbynrwwNo)

[Watch on YouTube](https://www.youtube.com/watch?v=VpDbynrwwNo)
