---
layout: default
title: "Processing large JSON files without running out of memory - Itamar Turner-Trauring"
nav_order: 105
parent: PyCon US 2025
type: Video Note
description: "Itamar Turner-Torring begins his talk by emphasizing the ethical responsibility of software developers, arguing that optimizing harmful software, such as AI systems used for military targeting, onl..."
resource: "https://www.youtube.com/watch?v=th3vsCDhujo"
youtube_stats:
  view_count: 5995
  like_count: 192
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

Itamar Turner-Torring begins his talk by emphasizing the ethical responsibility of software developers, arguing that optimizing harmful software, such as AI systems used for military targeting, only amplifies the resulting damage.
He then shifts focus to the technical challenge of processing large JSON files in Python, noting that the standard library’s `json` module can consume up to four times the file size in memory, which risks system crashes when handling multi-gigabyte datasets.
To address this, he presents four solutions: purchasing more RAM, using more efficient in-memory representations like Arrow via `awkward-array`, loading only necessary data subsets using `msgspec`, and streaming data incrementally with `ijson`.
The speaker demonstrates that streaming is the most effective method, reducing peak memory usage to nearly zero regardless of file size, while also recommending Newline Delimited JSON (NDJSON) as a more stream-friendly alternative to standard JSON.
Finally, he stresses the critical importance of actively measuring peak memory usage, as libraries like Pandas and Polars may unexpectedly consume more memory than expected, and advises developers to verify performance rather than relying on assumptions.

# Main Points

|   # | Main point                                                                                                                                                          |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker warns against optimizing software that causes harm, such as AI systems used for military targeting with high error rates.                               |
|   2 | Loading a 50 MB JSON file using Python's standard library results in 200 MB of peak memory usage, a four-fold increase.                                             |
|   3 | High peak memory usage can cause operating systems to kill processes when available RAM is insufficient, leading to program failure.                                |
|   4 | Measuring peak memory usage is critical and can be done using tools like `user bin time`, Python's `resource` module, or memory profilers.                          |
|   5 | Buying more RAM is a hardware solution but may be cost-prohibitive, impossible on certain hardware, or impractical for unpredictable data sizes.                    |
|   6 | Using Apache Arrow via the `awkward-array` library reduces peak memory usage to 100 MB by using a more efficient columnar data representation.                      |
|   7 | Switching to Arrow-based libraries like Pandas or Polars changes the programming paradigm and may not always reduce memory usage compared to standard JSON loading. |
|   8 | Loading only a subset of required fields using the `msgspec` library reduces peak memory usage to 100 MB by ignoring irrelevant data.                               |
|   9 | Streaming data using the `ijson` library allows processing records one at a time, reducing peak memory usage to approximately 1 MB regardless of file size.         |
|  10 | Streaming requires that the data structure supports chunking and that the processing logic does not require all data to be in memory simultaneously.                |
|  11 | Newline-delimited JSON (NDJSON) allows for simple streaming by parsing each line as an independent JSON document using standard libraries.                          |
|  12 | Memory usage is often overlooked and non-linear in its impact, so it must be explicitly measured rather than assumed based on library design.                       |
|  13 | JSON is not ideal for streaming or efficiency compared to binary formats like Parquet or NDJSON, which offer better performance and lower memory overhead.          |

# Video

[![Video thumbnail](https://img.youtube.com/vi/th3vsCDhujo/hqdefault.jpg)](https://www.youtube.com/watch?v=th3vsCDhujo)

[Watch on YouTube](https://www.youtube.com/watch?v=th3vsCDhujo)
