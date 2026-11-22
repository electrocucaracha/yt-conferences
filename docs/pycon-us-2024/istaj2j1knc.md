---
layout: default
title: "Talks - Reuven M. Lerner: Times and dates in Pandas"
nav_order: 147
parent: PyCon US 2024
type: Video Note
description: "In this session, Ruben Learner explores the comprehensive handling of dates and times in pandas, distinguishing between specific moments (datetime objects) and durations (timedelta objects)."
resource: "https://www.youtube.com/watch?v=IsTaJ2J1KNc"
youtube_stats:
  view_count: 460
  like_count: 12
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

In this session, Ruben Learner explores the comprehensive handling of dates and times in pandas, distinguishing between specific moments (datetime objects) and durations (timedelta objects).
He demonstrates how to efficiently import and convert textual date data into datetime formats using `pd.to_datetime` or the `parse_dates` parameter in `read_csv`, highlighting the memory savings and new functionalities this conversion provides.
The presentation covers advanced data manipulation techniques, including extracting specific time components via the `.dt` accessor, performing chronological grouping with `pd.Grouper`, and creating time series by setting datetime columns as the index.
Additionally, Learner addresses time zone management through localization and conversion, as well as the use of resampling for aggregating data over fixed time intervals.
The session concludes with a Q&A discussing best practices for data extraction, the deprecation of `inplace=True` in favor of method chaining, and considerations for handling out-of-range dates and preserving precision in data I/O.

# Main Points

|   # | Main point                                                                                                                                                             |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Time in Python and pandas refers to two distinct concepts: a specific moment (datetime) and a span of duration (timedelta).                                            |
|   2 | Datetime objects represent specific points in time, while timedelta objects represent the length of time between two points.                                           |
|   3 | Arithmetic operations allow converting between these types, such as subtracting two datetimes to get a timedelta or adding a timedelta to a datetime.                  |
|   4 | Pandas does not automatically recognize date strings in CSV files as datetime objects; they are initially read as object types.                                        |
|   5 | The `pd.to_datetime` function converts string columns to datetime objects, which reduces memory usage and enables date-specific functionality.                         |
|   6 | Invalid date strings can be handled by setting the `errors` parameter to 'coerce', which converts invalid entries to NaT (Not a Time) instead of raising an exception. |
|   7 | The `parse_dates` parameter in `pd.read_csv` allows for direct conversion of specified columns to datetime during the import process.                                  |
|   8 | Date format ambiguity can be resolved using the `dayfirst` parameter or by specifying an explicit `date_format` string using strftime codes.                           |
|   9 | The `.dt` accessor provides methods to extract components like year, month, day, hour, and boolean flags such as leap year status.                                     |
|  10 | Datetime columns support standard aggregation methods like mean, min, and max, as well as sorting and filtering operations.                                            |
|  11 | Timedelta columns are created by subtracting one datetime column from another and can be analyzed using the `.dt` accessor or `total_seconds`.                         |
|  12 | Timezone handling includes localizing naive datetimes with `tz_localize`, converting between zones with `tz_convert`, and parsing zones directly from data.            |
|  13 | GroupBy operations can use datetime components, such as hour or day of week, as categorical keys for aggregations.                                                     |
|  14 | Pivot tables can utilize datetime components for both row indices and column headers to create two-dimensional summaries.                                              |
|  15 | The `pd.Grouper` object enables chronological grouping by frequency (e.g., weekly or monthly) rather than by unique values.                                            |
|  16 | Setting a datetime column as the index creates a Time Series, allowing for flexible row retrieval using partial date strings.                                          |
|  17 | Resampling allows for aggregating data at a specified frequency (e.g., monthly means) when a datetime index is present.                                                |
|  18 | Using `inplace=True` is discouraged in favor of method chaining and returning new DataFrames to avoid side effects and improve code clarity.                           |
|  19 | Best practices for data exchange include preserving timezones, preferably using UTC, and standardizing on ISO formats to ensure consistency.                           |

# Video

[![Video thumbnail](https://img.youtube.com/vi/IsTaJ2J1KNc/hqdefault.jpg)](https://www.youtube.com/watch?v=IsTaJ2J1KNc)

[Watch on YouTube](https://www.youtube.com/watch?v=IsTaJ2J1KNc)
