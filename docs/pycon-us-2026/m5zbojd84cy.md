---
layout: default
title: "Text is not text: a history of strings in Python - Daniel Hervás"
nav_order: 21
parent: PyCon US 2026
type: Video Note
description: "This presentation explores the historical evolution of string handling in programming, tracing the progression from simple ASCII byte representations to the complex Unicode standards required for g..."
resource: "https://www.youtube.com/watch?v=m5ZboJD84CY"
youtube_stats:
  view_count: 148
  like_count: 2
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

This presentation explores the historical evolution of string handling in programming, tracing the progression from simple ASCII byte representations to the complex Unicode standards required for global text support.
The speaker explains how early systems like C treated strings as contiguous memory regions, leading to security vulnerabilities such as buffer overflows, and how the transition to Unicode and UTF-8 encoding solved issues of character representation and memory efficiency.
In the context of Python, the talk contrasts Python 2’s confusing distinction between bytes and Unicode strings with Python 3’s "Unicode Sandwich" model, where internal text is always Unicode and only converted to bytes at input/output boundaries.
The discussion then shifts to the evolution of string formatting tools, moving from `printf`-style substitution and the `format` method to f-strings, highlighting how these approaches often lose the structural distinction between literal text and interpolated variables.
Finally, the speaker introduces T-strings in Python 3.14 as a significant advancement that preserves this structural information, allowing for safer operations like SQL injection prevention by maintaining clear boundaries between static templates and dynamic values.

# Main Points

|   # | Main point |
| --: | ---------- |
|   1 | The talk explores the historical evolution of string handling, moving from raw bytes to modern abstractions like T strings. |
|   2 | Jol Spolski's 2003 article on Unicode is recommended as foundational context for understanding string complexity. |
|   3 | String length is not always intuitive; for example, a family emoji has a length of seven due to invisible zero-width joiners. |
|   4 | ASCII represents 128 characters in one byte, which is insufficient for non-English languages and emojis. |
|   5 | In C, strings are contiguous memory regions terminated by a null byte, leading to security risks like buffer overflows. |
|   6 | Unicode expands the character set to fit in four bytes, solving the limitation of ASCII for global languages. |
|   7 | Naive Unicode encoding wastes memory by padding bytes, while variable-length encoding creates ambiguity in byte boundaries. |
|   8 | UTF-8 is backward compatible with ASCII and uses control bits to efficiently encode multi-byte characters without wasting memory. |
|   9 | The family emoji measures seven characters because it consists of four individual emojis joined by three invisible zero-width joiners. |
|  10 | Python 2 treated strings as bytes and Unicode separately, causing errors when mixing encodings or calculating lengths. |
|  11 | Python 3 standardizes strings as Unicode code points, enforcing a clear distinction between bytes and text. |
|  12 | The Unicode Sandwich model in Python 3 ensures all internal text is Unicode, with encoding and decoding occurring only at I/O boundaries. |
|  13 | Python string formatting has evolved from printf-style substitution to format methods, then f-strings, and finally T strings. |
|  14 | F-strings perform immediate substitution, resulting in a final string where the distinction between literal text and variables is lost. |
|  15 | T strings in Python 3.14 preserve the template structure, allowing values to be bound while maintaining information about literal and interpolated parts. |
|  16 | T strings enable safer operations like SQL injection prevention by allowing libraries to sanitize interpolated values before execution. |
|  17 | PEP 393 describes Python's internal optimization for string memory usage, ensuring characters occupy only the necessary space. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/m5ZboJD84CY/hqdefault.jpg)](https://www.youtube.com/watch?v=m5ZboJD84CY)

[Watch on YouTube](https://www.youtube.com/watch?v=m5ZboJD84CY)
