---
layout: default
title: "Talks - Alex Monahan, Gabor Szarnyas: Python and SQL: Better Together, Powered by DuckDB"
nav_order: 208
parent: PyCon US 2024
type: Video Note
description: "Alex, a data scientist and DuckDB contributor, presents a talk on integrating Python and SQL to move beyond language wars by leveraging DuckDB, an in-process analytical database."
resource: "https://www.youtube.com/watch?v=iQQaBYMZ_mU"
youtube_stats:
  view_count: 3203
  like_count: 98
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

Alex, a data scientist and DuckDB contributor, presents a talk on integrating Python and SQL to move beyond language wars by leveraging DuckDB, an in-process analytical database.
He explains that DuckDB was created to address the inefficiency of using large distributed systems for data science tasks that are too big for Pandas but do not require full-scale infrastructure, positioning it as a "SQLite for analytics" that runs directly within the Python process.
The presentation highlights DuckDB’s key advantages, including its ability to handle datasets larger than RAM by gracefully spilling to disk, its high performance through vectorization and multi-threading, and its seamless interoperability with data frames, allowing users to query Pandas or Polars objects directly without data copying.
Alex demonstrates various integration methods, such as using DuckDB’s Python-inspired SQL dialect, a relational API for composable queries, and experimental PySpark-compatible interfaces, emphasizing that the tool fits into existing workflows for local development, web browsers, and edge computing.
The session concludes with a Q&A addressing technical details like memory management, data persistence formats, and the database’s robustness, reinforcing DuckDB’s role as a fast, easy-to-use, and versatile engine for modern data engineering and science.

# Main Points

|   # | Main point                                                                                                                                                     |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | DuckDB is an in-process analytical SQL database designed to bridge the gap between Python data frames and distributed systems.                                 |
|   2 | It operates within the same memory space as Python, eliminating network latency and enabling zero-millisecond data transfer for interactive analytics.         |
|   3 | The database is MIT licensed, written in C++, and supports over 15 languages, with Python being the most popular integration.                                  |
|   4 | DuckDB is not an in-memory database; it uses a persistent file format to handle datasets larger than RAM, such as two-terabyte problems on a laptop.           |
|   5 | The SQL dialect is inspired by Python, featuring modern syntax like trailing commas, string slicing, and list comprehensions.                                  |
|   6 | It offers seamless reading and writing of Pandas, Polars, and Arrow data frames without copying data, trading pointers in the same memory space.               |
|   7 | DuckDB provides a relational API that allows users to write dataframe-style syntax while leveraging the underlying SQL engine for optimization.                |
|   8 | The system supports user-defined functions using Apache Arrow compute kernels, enabling vectorized processing of large batches without serialization overhead. |
|   9 | An experimental PySpark-compatible API allows users to run Spark syntax on DuckDB without managing a cluster, ideal for local development and testing.         |
|  10 | Performance benchmarks show DuckDB is significantly faster than Spark and Pandas for analytical queries, particularly on complex joins and aggregations.       |
|  11 | The engine uses morsel-driven parallelism to fully utilize all CPU cores and vectorized execution for high-speed processing.                                   |
|  12 | DuckDB gracefully degrades performance when memory limits are reached by spilling data to disk, avoiding crashes and maintaining usability.                    |
|  13 | It supports a wide variety of data formats including CSV, JSON, Parquet, and Apache Iceberg, as well as cloud storage like AWS S3 and Azure Blob.              |
|  14 | The database can run in web browsers via WebAssembly and Pyodide, enabling local data analysis without server infrastructure.                                  |
|  15 | DuckDB integrates with the broader Python ecosystem, including DBT, SQL Alchemy, and visualization libraries, acting as a Swiss Army knife for data workflows. |
|  16 | The project is approaching version 1.0, with a strong focus on robustness, bug fixing, and stability inspired by SQLite's reliability standards.               |
|  17 | Mother Duck, a cloud service built on DuckDB, offers a serverless platform that splits queries between local and cloud resources for enhanced performance.     |

# Video

[![Video thumbnail](https://img.youtube.com/vi/iQQaBYMZ_mU/hqdefault.jpg)](https://www.youtube.com/watch?v=iQQaBYMZ_mU)

[Watch on YouTube](https://www.youtube.com/watch?v=iQQaBYMZ_mU)
