---
layout: default
title: "Talks - Patrick Hoefler: Pandas + Dask DataFrame 2.0 - Comparison to Spark, DuckDB and Polars"
nav_order: 207
parent: PyCon US 2024
type: Video Note
description: "Patrick from Coiled presented a comprehensive overview of recent improvements to Dask DataFrames, highlighting significant performance gains achieved over the past 12 to 18 months."
resource: "https://www.youtube.com/watch?v=g_P2yFBW5uE"
youtube_stats:
  view_count: 770
  like_count: 9
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

Patrick from Coiled presented a comprehensive overview of recent improvements to Dask DataFrames, highlighting significant performance gains achieved over the past 12 to 18 months.
Key enhancements include the adoption of Arrow-backed strings, which reduced memory usage by up to 70% and improved string operation speeds, and a complete rewrite of the shuffle algorithm to ensure linear scaling and efficient disk usage for large datasets.
The introduction of a query optimizer has further boosted performance by enabling column projection, predicate pushdown, and the elimination of redundant shuffles, resulting in a total 19x speedup for specific complex queries.
In benchmarks comparing Dask against Spark, DuckDB, and Polars, Dask demonstrated superior scalability and reliability on 10TB datasets, outperforming Spark on most queries while Spark struggled with resource constraints and failed on several tasks.
Although DuckDB remains highly competitive for single-node workloads up to 1TB, Dask is positioned as the more robust choice for distributed environments requiring massive scale, with future improvements expected to address remaining overheads and further optimize shuffle operations.

# Main Points

|   # | Main point                                                                                                                                                                        |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Dask data frames have improved significantly over the last 12 to 18 months, becoming faster and easier to use compared to previous versions.                                      |
|   2 | The talk compares Dask performance against Spark, DuckDB, and Polars using TPC-H style benchmarks at scales of 100 GB, 1 TB, and 10 TB.                                           |
|   3 | Replacing NumPy object strings with Arrow-backed strings in pandas and Dask yields up to 10x speed improvements and reduces memory usage by 60-70%.                               |
|   4 | A new peer-to-peer shuffle algorithm was implemented in Dask, changing scaling from logarithmic to linear and enabling efficient disk usage for large datasets.                   |
|   5 | Query planning was added to Dask, introducing optimizations such as column projection and predicate pushdown to reduce unnecessary data reading and network transfer.             |
|   6 | The query optimizer now handles partition sizing by squashing small Parquet files to maintain healthy partition sizes, resulting in a 3x performance improvement.                 |
|   7 | Merge operations are optimized to avoid redundant shuffles when joining on the same column, which can speed up queries by up to 4x.                                               |
|   8 | Overall performance for a specific one-terabyte query improved by 19x, reducing runtime from 950 seconds to 50 seconds.                                                           |
|   9 | At the 100 GB scale, DuckDB generally outperforms Dask, while Spark and Polars show mixed results with Polars struggling on complex queries.                                      |
|  10 | At the 1 TB scale, DuckDB remains competitive on a single large VM, but Dask is more reliable for distributed workloads.                                                          |
|  11 | At the 10 TB scale, Dask outperforms Spark on most queries, whereas Spark struggles with out-of-core processing and fails to complete several queries even with increased memory. |
|  12 | DuckDB fails on complex 10 TB queries due to memory allocation issues, making Dask the better choice for scaling out beyond single-machine limits.                                |
|  13 | Dask currently experiences up to 50% overhead on some 10 TB queries, which is expected to be resolved in upcoming updates.                                                        |
|  14 | Future improvements include a new shuffle algorithm draft that promises 25-30% overall performance gains and a more intelligent query optimizer.                                  |
|  15 | Dask is recommended for workloads that exceed single-machine memory limits or require distributed scaling, while DuckDB is suitable for smaller datasets fitting in memory.       |
|  16 | The query optimizer covers 90-95% of optimization cases, with some complex data-dependent optimizations remaining difficult in distributed settings.                              |

# Video

[![Video thumbnail](https://img.youtube.com/vi/g_P2yFBW5uE/hqdefault.jpg)](https://www.youtube.com/watch?v=g_P2yFBW5uE)

[Watch on YouTube](https://www.youtube.com/watch?v=g_P2yFBW5uE)
