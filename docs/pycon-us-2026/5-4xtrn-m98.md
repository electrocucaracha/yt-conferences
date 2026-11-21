---
layout: default
title: "Don’t Write Polars Code with a Pandas Accent - Joram Montege"
nav_order: 54
parent: PyCon US 2026
type: Video Note
description: "Joram Nyutenge, a data science professional and author of *Deep Analysis with Polars*, presents a PyCon talk focused on avoiding common \"Pandas-accented\" mistakes when writing idiomatic Polars code."
resource: "https://www.youtube.com/watch?v=5-4xTrN-M98"
youtube_stats:
  view_count: 822
  like_count: 26
  channel_subscriber_count: 34500
tags:
  - pycon-us-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-20T08:08:06+00:00
---

# Summary

Joram Nyutenge, a data science professional and author of *Deep Analysis with Polars*, presents a PyCon talk focused on avoiding common "Pandas-accented" mistakes when writing idiomatic Polars code.
He identifies five key errors, including using square bracket notation for column selection, relying on multiple intermediate variables, overusing eager execution, adding columns horizontally in a tedious manner, and using the `drop` method.
Nyutenge demonstrates that idiomatic Polars code utilizes the `select` method, chains operations to leverage the query optimizer, employs lazy evaluation for performance gains through techniques like predicate and projection pushdown, and uses `sum_horizontal` with Polars selectors for efficient aggregation.
He emphasizes that avoiding intermediate variables and using lazy mode can significantly improve speed, as shown by a performance comparison where chained operations outperformed intermediate variable approaches.
Finally, he advises against using `drop` in favor of `exclude` for robustness and encourages developers to think in Polars expressions rather than translating Pandas code directly.

# Main Points

|   # | Main point |
| --: | ---------- |
|   1 | The speaker, Joram Nyutenge, presents five common mistakes made when migrating from Pandas to Polars and offers idiomatic alternatives. |
|   2 | Polars is an open-source data analysis library with a typed API that uses expressions, differing from Pandas in its approach to data manipulation. |
|   3 | Avoid using square bracket notation for column selection; instead, use the select method with column names or expressions for modifications. |
|   4 | Refrain from creating multiple intermediate variables; chain operations to improve code readability and performance, as demonstrated by a speed comparison favoring chained operations. |
|   5 | Utilize lazy mode to leverage the query optimizer, which applies techniques like predicate and projection pushdown to filter rows and select columns before computation. |
|   6 | Use the sum_horizontal expression with Polars selectors to add columns horizontally, which is more efficient and idiomatic than adding columns individually or using index ranges. |
|   7 | Avoid using the drop method to remove columns because it fails if the column does not exist; use the exclude method within select for robust column removal. |
|   8 | Think in Polars expressions rather than translating Pandas code literally to ensure idiomatic usage and better performance. |
|   9 | Leverage the query optimizer by using lazy mode and chaining operations to maximize efficiency and reduce unnecessary computational steps. |
|  10 | Use Polars selectors to dynamically select columns based on data types or names, enhancing code flexibility and reducing manual column listing. |
|  11 | Prefer the get_column method over select when a Series object is required for operations like value_counts, as select returns a DataFrame. |
|  12 | Remove unnecessary square brackets from select method calls to maintain clean and idiomatic Polars code syntax. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/5-4xTrN-M98/hqdefault.jpg)](https://www.youtube.com/watch?v=5-4xTrN-M98)

[Watch on YouTube](https://www.youtube.com/watch?v=5-4xTrN-M98)
