---
layout: default
title: "Talks - Pat Viafore: Extensible Python: Robustness Through Addition"
nav_order: 164
parent: PyCon US 2024
type: Video Note
description: Pat For presents a session on achieving extensible Python robustness by prioritizing empathy for future developers and reducing commit complexity.
resource: "https://www.youtube.com/watch?v=p3frDvA6iNQ"
youtube_stats:
  view_count: 304
  like_count: 5
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

Pat For presents a session on achieving extensible Python robustness by prioritizing empathy for future developers and reducing commit complexity.
He advocates for the Open/Closed Principle to minimize modifications to existing code, suggesting that developers separate business logic (policies) from implementation details (mechanisms) to enhance reusability and ease of change.
The talk explores the trade-offs between physical dependencies, which are easy to trace but hard to modify, and logical dependencies, which are flexible but harder to debug, recommending the use of dependency injection to decouple components.
For architectural extensibility, For demonstrates how event-driven architectures using message brokers and pluggable systems via entry points allow new features to be added without altering core code, similar to attaching accessories to a stand mixer.
He concludes by advising against overengineering, urging developers to apply these extensibility patterns judiciously where changes are frequent to maintain a manageable and efficient codebase.

# Main Points

|   # | Main point                                                                                                                                 |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Software development requires balancing immediate value delivery with long-term maintainability for future developers.                     |
|   2 | The primary goal of extensibility is to make simple changes easy and complex changes hard to implement.                                    |
|   3 | Reduce commit complexity by avoiding shotgun surgery, where a single logical change requires modifying many files.                         |
|   4 | Adhere to the Open/Closed Principle by designing code that is open for extension but closed for modification.                              |
|   5 | Separate business policies from technical mechanisms to allow mechanisms to be reused across different contexts.                           |
|   6 | Utilize data-driven designs by storing policies in declarative formats like configuration files or databases rather than hardcoding them.  |
|   7 | Develop internal libraries with the same rigor as open-source projects, including clear documentation, tests, and defined opinions.        |
|   8 | Ensure code composability by creating modular building blocks that can be combined in various ways to support diverse use cases.           |
|   9 | Distinguish between physical dependencies, which are hardcoded and easy to trace, and logical dependencies, which are resolved at runtime. |
|  10 | Use dependency injection to reverse physical dependencies into logical ones, allowing for easier substitution and mocking.                 |
|  11 | Implement event-driven architectures using message brokers to decouple producers from consumers, enabling independent scaling.             |
|  12 | Apply pluggable architectures by defining clear interfaces that allow third-party code to extend core functionality without modification.  |
|  13 | Use Python entry points and packages like pluggy or stor to discover and load plugins dynamically from installed dependencies.             |
|  14 | Avoid overengineering by applying extensibility patterns only where changes are frequent and justified by business needs.                  |
|  15 | Prioritize empathy for human users and maintainers when making technical decisions about code structure and design.                        |

# Video

[![Video thumbnail](https://img.youtube.com/vi/p3frDvA6iNQ/hqdefault.jpg)](https://www.youtube.com/watch?v=p3frDvA6iNQ)

[Watch on YouTube](https://www.youtube.com/watch?v=p3frDvA6iNQ)
