---
layout: default
title: "Unlearning SQL - Steven Lott"
nav_order: 32
parent: PyCon US 2025
type: Video Note
description: "Steve argues that while SQL provides valuable design patterns, using a database engine for transient data processing introduces unnecessary overhead and complexity."
resource: "https://www.youtube.com/watch?v=sFAxHLaVKxk"
youtube_stats:
  view_count: 2237
  like_count: 58
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

Steve argues that while SQL provides valuable design patterns, using a database engine for transient data processing introduces unnecessary overhead and complexity.
He proposes translating core SQL concepts like SELECT, FROM, WHERE, and GROUP BY into native Python code using higher-order functions such as `itertools.product`, `filter`, and `map`.
This approach allows developers to leverage the full power of the Python ecosystem, including advanced data structures and libraries, to perform operations like joins and aggregations more efficiently than traditional database engines.
By treating SQL as a design language rather than an implementation choice, developers can avoid the administrative burdens of database management, such as index optimization and statistics, while maintaining code readability that mirrors familiar SQL logic.
The talk concludes with a call to action to stop using persistence engines for temporary data transformation and instead utilize Python’s in-memory capabilities for faster, more flexible data processing.

# Main Points

|   # | Main point                                                                                                                                                                                                |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | SQL design patterns are valuable for defining data processing logic, but using a database engine for transient data introduces significant overhead and complexity.                                       |
|   2 | Python's functional programming tools, specifically itertools.product, filter, and map, can directly implement the FROM, WHERE, and SELECT clauses of SQL queries.                                        |
|   3 | Using lazy generator expressions in Python allows for efficient data processing without the need to create, load, and drop temporary database tables.                                                     |
|   4 | The FROM clause in SQL corresponds to a Cartesian product in Python, but this can be optimized using sort-merge joins or lookup joins to improve performance.                                             |
|   5 | Lookup joins in Python, implemented via dictionary mappings, can be faster than database engines for in-memory data because they avoid serialization and deserialization overhead.                        |
|   6 | The GROUP BY operation in SQL can be implemented in Python by partitioning data into a default dictionary of lists and then applying aggregate functions to each group.                                   |
|   7 | The HAVING clause is functionally equivalent to a WHERE clause applied to grouped data, which can be implemented using the filter function in Python.                                                     |
|   8 | Python provides access to the full ecosystem of data structures and libraries, offering more flexibility and computing power than the limited operations available in standard SQL.                       |
|   9 | SQL should be used as a design language to structure logic and mental models, while Python should be used as the implementation choice for actual data transformation.                                    |
|  10 | Object-Relational Mappers (ORMs) are useful for persistent data but are often unnecessary and problematic for transient data pipelines where data is only temporarily stored.                             |
|  11 | In-memory Python processing is often faster than in-memory databases like SQLite or DuckDB for small to medium datasets because it avoids the cost of moving data between memory and the database engine. |
|  12 | Alternative algorithms such as using the bisect library or tools from the toolz package can provide more efficient grouping and joining strategies depending on the data distribution.                    |
|  13 | The primary goal is to stop using persistence engines for transient data processing and instead leverage Python's native capabilities for cleaner, faster, and more maintainable code.                    |

# Video

[![Video thumbnail](https://img.youtube.com/vi/sFAxHLaVKxk/hqdefault.jpg)](https://www.youtube.com/watch?v=sFAxHLaVKxk)

[Watch on YouTube](https://www.youtube.com/watch?v=sFAxHLaVKxk)
