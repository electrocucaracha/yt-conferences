---
layout: default
title: "DataComPy - Dataframe Comparisons made Explicit (Sponsor: Capital One)"
nav_order: 71
parent: PyCon US 2025
type: Video Note
description: "Datacomp, an open-source Python library maintained by Capital One’s data science team, was created to facilitate data validation during the company’s transition from closed-source SAS tools to the ..."
resource: "https://www.youtube.com/watch?v=jxKNY4d4SMQ"
youtube_stats:
  view_count: 835
  like_count: 12
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

Datacomp, an open-source Python library maintained by Capital One’s data science team, was created to facilitate data validation during the company’s transition from closed-source SAS tools to the Python ecosystem.
The library, which has been downloaded nearly 27 million times, simplifies the comparison of data frames by performing outer joins, handling null values, and generating human-readable reports that detail discrepancies in rows, columns, and specific values.
A key recent development is the introduction of native in-database comparisons for Snowflake using Snowpark, which addresses significant performance and resource management challenges associated with loading large datasets into in-memory structures like Pandas or Polars.
Benchmarks presented in the talk indicate that while Pandas and Polars are more efficient for smaller datasets, Snowflake and Spark scale significantly better for large data loads, offering consistent results without the need for complex local resource provisioning.
Looking ahead, the team plans to release version 1.0, which will include refactors to allow users greater flexibility in defining custom equality logic for their specific business use cases.

# Main Points

|   # | Main point                                                                                                                                                          |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Datacomp is a Capital One open-source Python library maintained by the data science team in Canada since its release.                                               |
|   2 | The library was created to replicate SAS PROC COMPARE functionality during Capital One's transition from closed-source software to Python.                          |
|   3 | Datacomp has been downloaded nearly 27 million times since 2025 and holds critical status on PyPI.                                                                  |
|   4 | The core comparison process involves an outer join on user-specified keys, data cleaning, record categorization, and NumPy-based value comparison.                  |
|   5 | Users can generate human-readable reports or access comparison results programmatically for unit testing and automation.                                            |
|   6 | Native support extends beyond pandas to include PySpark, Polars, and Snowflake, with Fugue enabling cross-framework comparisons.                                    |
|   7 | New in-database comparisons for Snowflake use Snowpark to avoid the overhead and resource constraints of loading data into local memory.                            |
|   8 | Previous methods of loading Snowflake data into pandas or Polars caused performance issues, resource management challenges, and potential inconsistencies.          |
|   9 | Snowpark allows programmatic logic on Snowflake tables and implicitly supports Snowpark data frames for direct comparison.                                          |
|  10 | Benefits of native Snowflake comparisons include consistent comparison objects, better scalability for large datasets, and leveraging existing Snowflake resources. |
|  11 | Benchmarks indicate pandas and Polars perform better for datasets under 10 million rows, while Snowflake and Spark scale better for hundreds of millions of rows.   |
|  12 | Pandas comparisons failed at approximately 50 million rows and Polars at 500 million rows in benchmark tests with 16 CPUs and 64 GB RAM.                            |
|  13 | Snowflake comparison runtime scales linearly with row size, but performance degrades significantly with very large horizontal column counts.                        |
|  14 | A planned 1.0 refactor aims to allow users to define custom equality logic and comparison methods for greater flexibility.                                          |
|  15 | The team acknowledges the challenges of maintaining a critical open-source library alongside day-to-day data science responsibilities.                              |
|  16 | Datacomp supports comparing tables without join columns, a feature recently resolved or in progress.                                                                |
|  17 | Cross-platform comparisons, such as between pandas and Snowflake, are possible through the Fugue integration.                                                       |
|  18 | The team encourages continued use of the library and assures ongoing maintenance despite it being a side project for the data science team.                         |

# Video

[![Video thumbnail](https://img.youtube.com/vi/jxKNY4d4SMQ/hqdefault.jpg)](https://www.youtube.com/watch?v=jxKNY4d4SMQ)

[Watch on YouTube](https://www.youtube.com/watch?v=jxKNY4d4SMQ)
