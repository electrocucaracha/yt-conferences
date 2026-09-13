---
type: Video Note
title: "Accelerating Thanos at Scale: Faster and Cheaper Queries With Parquet - Giedrius Statkevičius"
description: "The speaker discusses efforts to accelerate Thanos at scale by adopting the Parquet file format, which offers faster queries and significant storage savings compared to the current TSDB format. Thanos, which manages vast amounts of metrics..."
resource: https://www.youtube.com/watch?v=PySEmqtrvL8
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The speaker discusses efforts to accelerate Thanos at scale by adopting the Parquet file format, which offers faster queries and significant storage savings compared to the current TSDB format.
Thanos, which manages vast amounts of metrics data, faces challenges such as slow and unpredictable query performance, memory issues at startup, and difficulties in sizing resources.
Parquet, being a column-oriented format with efficient data page structures and built-in statistics, allows selective data fetching, better compression, and concurrent decoding, resulting in substantial storage reductions (up to 85% in some cases) and query speed improvements—up to five times faster for typical queries.
The migration process to Parquet is gradual and tenant-based, with mechanisms to ensure consistency and minimize disruption.
While the compactor is still required for now, future plans include native Parquet file production and further architectural improvements.
The speaker encourages community contributions and assures that ongoing enhancements to the Parquet ecosystem will be adopted transparently, making it a promising direction for Thanos users.
# Main Points

|   # | Main point                                                                                                                                                         |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Presentation covers accelerating Thanos at scale with faster and cheaper queries using Parquet format.                                                             |
|   2 | Parquet enables faster queries and reduces storage space compared to the current format.                                                                           |
|   3 | Thanos users store over 700TB of metrics data in the largest region.                                                                                               |
|   4 | Previous related talks by Phillip and others discussed TSDB format issues and Parquet benefits.                                                                    |
|   5 | Thanos, Mimir, and Cortex upload objects to object storage and share similar issues.                                                                               |
|   6 | Key issues with Thanos store: slow queries, offset/symbol table size limits, compactor workarounds, difficulty sizing store gateway, high memory usage at startup. |
|   7 | Parquet is a column-oriented, schema-based data format from the Hadoop ecosystem.                                                                                  |
|   8 | Parquet allows fetching only needed columns, improving query efficiency and compression.                                                                           |
|   9 | Concurrent decoding and efficient data page fetching are possible with Parquet.                                                                                    |
|  10 | In the current format, queries require multiple random reads; Parquet reduces random reads by fetching matching pages.                                             |
|  11 | Parquet statistics help filter out unnecessary data pages during queries.                                                                                          |
|  12 | Parquet schema includes a bitmap for label columns, hashes for projections, chunk data, and each label as a column.                                                |
|  13 | Production data shows storage reduction: 85% (low churn), 42% (node exporter), 60% (alerting rules); overall, 700TB reduced to 400TB.                              |
|  14 | Migration involves a converter and a serve gateway; gradual tenant-by-tenant migration is supported.                                                               |
|  15 | Thanos store unloads converted blocks using new metadata files.                                                                                                    |
|  16 | Object storage structure: external labels hash, date, labels file, chunk files, metadata, stream file, and sharding for optimal file sizes.                        |
|  17 | Compactor is still required; native Parquet file production is a future goal.                                                                                      |
|  18 | Benchmarks: Parquet queries are up to 5x faster, especially with multiple matchers; projections provide a 25% speedup.                                             |
|  19 | Most Grafana queries benefit from Parquet’s projections and efficient data access.                                                                                 |
|  20 | Roadmap: improvements will come via the Parquet Go library; migration to mai                                                                                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=PySEmqtrvL8)