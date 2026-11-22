---
layout: default
title: "Bridging Python and Apache Iceberg™: The Power of PyIceberg - Rushan Jiang"
nav_order: 25
parent: PyCon US 2025
type: Video Note
description: "Jonas, a software engineer at Snowflake and PMC member of the Apache Iceberg community, presented on PyIceberg, a pure Python implementation of the Apache Iceberg open table format."
resource: "https://www.youtube.com/watch?v=gUvEwBUKizo"
youtube_stats:
  view_count: 2123
  like_count: 44
  channel_subscriber_count: 34500
tags:
  - pycon-us-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T01:39:37+00:00
---

# Summary

Jonas, a software engineer at Snowflake and PMC member of the Apache Iceberg community, presented on PyIceberg, a pure Python implementation of the Apache Iceberg open table format.
He explained that while traditional data workflows using formats like CSV or Parquet face challenges with schema evolution, multi-writer concurrency, and query optimization as datasets grow, Iceberg addresses these issues by introducing a metadata layer that tracks schema, partitioning, and snapshots.
This structure enables critical features such as schema evolution, hidden partitioning, optimistic concurrency control, and time travel queries, allowing users to manage large-scale data without rewriting existing files.
PyIceberg provides a lightweight, JVM-free interface for creating, reading, and updating tables, supporting various catalog backends and storage systems while leveraging the underlying Iceberg structure to automatically prune unnecessary data files during query planning.
The presentation concluded by highlighting Iceberg’s true power as a unified storage layer that ensures interoperability across diverse tools, including Apache Spark, Flink, Trino, and Snowflake, thereby enabling flexible and scalable data workflows without the need for data duplication or migration.

# Main Points

|   # | Main point                                                                                                                                              |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Apache Iceberg is an open table format for large-scale data management that adds a metadata layer to data files.                                        |
|   2 | Traditional data workflows using CSV, Parquet, or ORC face challenges with schema mismatches, lack of multi-writer guarantees, and manual partitioning. |
|   3 | Iceberg resolves these issues by enabling schema evolution, optimistic concurrency control, built-in partitioning, and time travel queries.             |
|   4 | The Iceberg structure consists of a catalog, a metadata layer containing manifest lists and manifests, and a data layer of files.                       |
|   5 | Manifest files record statistics like min/max values and row counts to enable file pruning during query planning.                                       |
|   6 | The catalog manages table locations and ensures atomic updates to support optimistic concurrency in multi-writer scenarios.                             |
|   7 | PyIceberg is a pure Python implementation of the Iceberg API that does not require a Java Virtual Machine.                                              |
|   8 | PyIceberg supports various catalog backends including AWS, Google, DynamoDB, Hive Metastore, and SQL databases.                                         |
|   9 | Data storage is supported on object stores like S3, GCS, ADLS, and file systems like HDFS.                                                              |
|  10 | Users can create tables, append data, overwrite records, and perform upserts using simple PyIceberg APIs.                                               |
|  11 | The read path optimizes queries by pruning unnecessary manifest and data files based on stored statistics before reading with PyArrow.                  |
|  12 | The write path involves writing data files, generating new manifests and snapshots, and atomically swapping the metadata pointer in the catalog.        |
|  13 | Schema evolution allows adding, renaming, or deleting columns and changing data types without rewriting existing data.                                  |
|  14 | Partition evolution allows changing partition strategies at any time, affecting only new data writes.                                                   |
|  15 | Iceberg supports table-level transactions that commit multiple updates as a single atomic unit.                                                         |
|  16 | Time travel queries allow reading table states from previous snapshots using timestamps or snapshot IDs.                                                |
|  17 | Iceberg provides a unified storage layer interoperable with engines like Spark, Flink, Trino, and Snowflake.                                            |
|  18 | Choosing between Iceberg and Delta Lake depends on organizational needs, with Iceberg often favored for its diverse community and interoperability.     |

# Video

[![Video thumbnail](https://img.youtube.com/vi/gUvEwBUKizo/hqdefault.jpg)](https://www.youtube.com/watch?v=gUvEwBUKizo)

[Watch on YouTube](https://www.youtube.com/watch?v=gUvEwBUKizo)
