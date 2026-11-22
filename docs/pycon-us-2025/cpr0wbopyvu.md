---
layout: default
title: "The PyArrow revolution in Pandas - Reuven M. Lerner"
nav_order: 39
parent: PyCon US 2025
type: Video Note
description: 'Ruvun Lerner presents a comprehensive overview of the "PyArrow Revolution" in pandas, explaining how the integration of Apache Arrow addresses significant memory and performance limitations inheren...'
resource: "https://www.youtube.com/watch?v=Cpr0wbopYvU"
youtube_stats:
  view_count: 4608
  like_count: 135
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

Ruvun Lerner presents a comprehensive overview of the "PyArrow Revolution" in pandas, explaining how the integration of Apache Arrow addresses significant memory and performance limitations inherent in the traditional NumPy backend.
The talk highlights three key areas of improvement: drastically faster CSV reading and writing, the adoption of efficient binary file formats like Parquet and Feather, and the transition to PyArrow as a backend for data storage.
Lerner demonstrates that using PyArrow can reduce memory usage by up to 75% and accelerate data loading by tenfold, while also introducing nullable data types that prevent unnecessary type conversions and overflow errors.
Although PyArrow currently exhibits slower performance for row-oriented operations compared to NumPy, it excels in column-based tasks and string processing, with ongoing improvements closing the performance gap.
Ultimately, the presentation argues that pandas is evolving from a standalone library into a flexible platform where PyArrow serves as a swappable, high-performance backend, offering users a path to greater efficiency without abandoning the familiar pandas API.

# Main Points

|   # | Main point                                                                                                                                                                             |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The PyArrow revolution in pandas aims to improve performance, memory usage, and interoperability by replacing NumPy as the underlying storage engine.                                  |
|   2 | PyArrow is a columnar data structure that enables faster data retrieval, reduced overhead between systems, and better utilization of modern multi-threaded hardware.                   |
|   3 | Reading and writing CSV files using the PyArrow engine is approximately 10 times faster than the default engine and automatically detects datetime columns.                            |
|   4 | Binary file formats like Feather and Parquet, defined by Arrow, offer significantly faster load times and smaller file sizes compared to CSV, with Parquet providing high compression. |
|   5 | Swapping the NumPy backend for PyArrow in pandas can drastically reduce memory usage, such as reducing a 15.6 GB dataset to 3.7 GB, and speeds up many operations.                     |
|   6 | PyArrow introduces nullable data types that prevent automatic conversion to float or object types when missing values are present, preserving integer and string dtypes.               |
|   7 | PyArrow automatically promotes integer types to larger sizes during arithmetic operations to prevent overflow, unlike NumPy which may silently wrap around values.                     |
|   8 | Row-oriented operations, such as using .loc or .iloc, are currently slower in PyArrow than in NumPy, while column-oriented operations are generally faster or comparable.              |
|   9 | Pandas is evolving into a platform with swappable backends and frontends, allowing users to retain the familiar pandas API while benefiting from modern data processing technologies.  |
|  10 | Users can enable PyArrow-backed strings immediately by setting pd.options.future.infer_string to true, resulting in faster string handling and lower memory usage.                     |
|  11 | The transition to PyArrow is experimental but will become the default in pandas 3.0, with ongoing improvements closing performance gaps with NumPy over time.                          |

# Video

[![Video thumbnail](https://img.youtube.com/vi/Cpr0wbopYvU/hqdefault.jpg)](https://www.youtube.com/watch?v=Cpr0wbopYvU)

[Watch on YouTube](https://www.youtube.com/watch?v=Cpr0wbopYvU)
