---
layout: default
title: "Talks - Sebastian Buczyński: Having fun with pydantic and pattern matching"
nav_order: 187
parent: PyCon US 2024
type: Video Note
description: "Sebastian Bąski presents a technical talk on leveraging Python’s `match-case` syntax and Pydantic for robust pattern matching in event-driven systems."
resource: "https://www.youtube.com/watch?v=MfUuHYi2jgY"
youtube_stats:
  view_count: 1223
  like_count: 42
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

Sebastian Bąski presents a technical talk on leveraging Python’s `match-case` syntax and Pydantic for robust pattern matching in event-driven systems.
He argues that `match-case` is significantly more powerful than a traditional switch statement because it supports matching on types and attributes, not just equality, though the order of cases is critical to avoid logic errors.
To address the fragility of handling raw dictionaries, Bąski demonstrates how Pydantic models can validate and type data, using `TypeAdapter` and unions to automatically parse incoming messages into specific classes.
He further refines the architecture by employing `functools.singledispatch` to route events to specialized handlers based on their type, thereby adhering to the open-closed principle and minimizing the need to modify core logic when new event types are introduced.
The session concludes with a discussion on the trade-offs between performance and type safety, noting that while Pydantic adds overhead, it provides essential validation and clarity for complex data structures.

# Main Points

|   # | Main point                                                                                                                                                                               |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker, Sebastian Bąski, is a software architect from Poland who focuses on educating Python developers about software engineering principles.                                      |
|   2 | Python's match-case statement is significantly more powerful than a traditional switch statement because it supports pattern matching on types and attributes, not just equality checks. |
|   3 | The order of case statements in match-case is critical, as patterns are evaluated from top to bottom, similar to exception handling blocks.                                              |
|   4 | A case study demonstrates handling a stream of events (e.g., Kafka or RabbitMQ) where messages vary in type and may be malformed.                                                        |
|   5 | Using if-else statements for event handling leads to deeply nested code that is difficult to maintain and prone to silent failures when new message types or statuses are introduced.    |
|   6 | Refactoring with match-case allows for clearer logic by matching specific dictionary structures and literal values for message types.                                                    |
|   7 | Pydantic models can replace untyped dictionaries by providing validation, data conversion, and type safety for event payloads.                                                           |
|   8 | Pydantic v2's TypeAdapter and Union types enable pattern matching on types, allowing developers to validate incoming data against specific model classes.                                |
|   9 | Adding Any to the Union type and including a catch-all case in match-case prevents crashes when malformed or unexpected messages are received.                                           |
|  10 | Specialized Pydantic models can be created for specific state transitions, such as changing from trial to paid status, to further refine handling logic.                                 |
|  11 | Functools.singledispatch allows for dynamic dispatch of functions based on argument types, reducing the need to modify a central handler function when adding new event types.           |
|  12 | This approach aligns with the Open-Closed Principle, making the system easy to extend with new handlers without altering existing code.                                                  |
|  13 | Match-case syntax for type matching, such as case AccountCreated(), does not instantiate the class or execute its **init** method; it only checks the type.                              |
|  14 | Pydantic Union discriminants can optimize performance by checking a specific field first rather than trying each model in the union sequentially.                                        |
|  15 | Nested Pydantic models are a standard and scalable pattern, though developers should be cautious about reusing models in nested contexts to avoid type issues.                           |
|  16 | While Pydantic adds overhead compared to simple if-else checks, this is often negligible in production environments where other processes are slower.                                    |

# Video

[![Video thumbnail](https://img.youtube.com/vi/MfUuHYi2jgY/hqdefault.jpg)](https://www.youtube.com/watch?v=MfUuHYi2jgY)

[Watch on YouTube](https://www.youtube.com/watch?v=MfUuHYi2jgY)
