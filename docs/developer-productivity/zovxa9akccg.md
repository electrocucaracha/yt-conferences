---
layout: default
title: Calling Functions Across Languages • Richard Feldman • GOTO 2023
nav_order: 15
parent: Developer Productivity
type: Video Note
description:
  The speaker discusses the challenges of calling functions across languages,
  particularly when trying to optimize performance. They share their experience with
  Scala, JavaScript, and Ruby, highlighting the difficulties of serializing data an...
resource: https://www.youtube.com/watch?v=ZOvxa9aKCCg
tags:
  - developer-productivity
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The speaker discusses the challenges of calling functions across languages, particularly when trying to optimize performance.
They share their experience with Scala, JavaScript, and Ruby, highlighting the difficulties of serializing data and making HTTP requests.
The speaker then introduces the concept of using C as an intermediary language to bridge the gap between different programming languages.
They demonstrate how this approach can be used to call a Ruby function from JavaScript in the same process, eliminating the need for inter-process communication or network calls.
The speaker also touches on the trade-offs involved, including potential overhead and the risk of errors if not implemented correctly.

# Main Points

|   # | Main point                                                                                                                           |
| --: | ------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | The speaker has encountered a task that would be easier to solve by using another language.                                          |
|   2 | They discuss the challenges of calling functions across languages, including inter-process communication and network overhead.       |
|   3 | The speaker presents three approaches to calling functions across languages:                                                         |
|   4 | Inter-process communication (IPC): using IPC to communicate between processes or threads.                                            |
|   5 | Network: making a network request to call a function in another language.                                                            |
|   6 | Same process: executing the function directly within the same process as the caller.                                                 |
|   7 | They discuss the advantages and disadvantages of each approach, including performance, overhead, and complexity.                     |
|   8 | The speaker presents an example of using C as an intermediary between two languages (e.g., JavaScript and Ruby) to call a function.  |
|   9 | They introduce the concept of "binding" or "glue code" that allows different languages to communicate with each other.               |
|  10 | The speaker discusses the importance of type safety and ergonomics when calling functions across languages.                          |
|  11 | They present an example of using Rock, a functional programming language, as a target language for binding.                          |
|  12 | The speaker highlights the benefits of incremental adoption, where a new language is introduced gradually into an existing codebase. |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=ZOvxa9aKCCg)
