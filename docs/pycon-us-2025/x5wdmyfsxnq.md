---
layout: default
title: "Notes, Groups and Stars: exceptional new features of Python 3.11! - Zac Hatfield-Dodds"
nav_order: 28
parent: PyCon US 2025
type: Video Note
description: "Zach Hatfield Dods presents an overview of exception handling in Python, contrasting the language’s exception-based approach with error-value returns used in other languages to highlight the benefi..."
resource: "https://www.youtube.com/watch?v=x5WdMYfsxnQ"
youtube_stats:
  view_count: 1146
  like_count: 25
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

Zach Hatfield Dods presents an overview of exception handling in Python, contrasting the language’s exception-based approach with error-value returns used in other languages to highlight the benefits of automatic traceback propagation.
The talk details new features in Python 3.11, including enhanced tracebacks that pinpoint specific expressions, the `add_note` method for annotating exceptions without altering their type, and the introduction of exception groups to manage multiple concurrent errors.
A key focus is the new `except*` syntax, which allows developers to catch specific exception types within a group, though it requires careful handling to avoid losing critical traceback context when extracting individual errors.
Dods warns against common pitfalls, such as naively raising the first exception from a group, which can corrupt stack traces, and proposes helper methods to safely destructure exception groups.
The session concludes with a Q&A addressing the complexities of managing cancellation errors in asynchronous code and clarifying how unmatched exceptions continue to propagate when using the new syntax.

# Main Points

|   # | Main point                                                                                                                                    |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Python 3.11 introduces new exception handling features including notes, exception groups, and the except star syntax.                         |
|   2 | Exceptions are preferred over error return values in Python because they automatically propagate and provide tracebacks.                      |
|   3 | Python 3.11 tracebacks now highlight the specific part of an expression that caused the error, aiding debugging.                              |
|   4 | Exception chaining allows tracking the cause of an error using the from syntax or by raising an exception while another is active.            |
|   5 | The raise from none syntax suppresses the previous exception context to reduce traceback volume, but should be used with care.                |
|   6 | Dunder attributes like **traceback**, **context**, and **cause** manage exception metadata and chaining internally.                           |
|   7 | The add_note method allows annotating exceptions with additional context without changing the exception type, useful for libraries.           |
|   8 | Exception groups handle multiple concurrent errors by grouping them into a tree structure, common in async frameworks and test teardowns.     |
|   9 | The except star syntax catches either a bare exception or a subset of an exception group matching the specified type.                         |
|  10 | When catching an exception group, the handler receives an exception group object, not the individual exceptions directly.                     |
|  11 | Extracting a single leaf exception from a group can lose stack trace information and may increase traceback size due to context preservation. |
|  12 | Helper methods like split and subgroup allow isolating specific parts of an exception group for targeted handling.                            |
|  13 | Proposed future enhancements include a leaf_exceptions method to iterate over leaf exceptions with complete tracebacks.                       |
|  14 | Context managers do not require changes for these new features, as exception handling within them follows standard try-except-finally logic.  |
|  15 | Unhandled subsets of an exception group continue to propagate if they do not match any except star handlers.                                  |
|  16 | Raising exceptions within except star blocks results in those exceptions being grouped with other unhandled or newly raised errors.           |

# Video

[![Video thumbnail](https://img.youtube.com/vi/x5WdMYfsxnQ/hqdefault.jpg)](https://www.youtube.com/watch?v=x5WdMYfsxnQ)

[Watch on YouTube](https://www.youtube.com/watch?v=x5WdMYfsxnQ)
