---
layout: default
title: "The Zen of Polymorphism: Choosing between isinstance(), methods, and @singledispatch - Brett Slatkin"
nav_order: 29
parent: PyCon US 2025
type: Video Note
description: 'In a PyCon talk, Brett Sladen explores the "Zen of Polymorphism" by comparing four strategies for handling recursive data structures, using a calculator program as a practical example.'
resource: "https://www.youtube.com/watch?v=hidy15rK2a4"
youtube_stats:
  view_count: 3074
  like_count: 111
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

In a PyCon talk, Brett Sladen explores the "Zen of Polymorphism" by comparing four strategies for handling recursive data structures, using a calculator program as a practical example.
He begins by critiquing the "one big function" approach, which relies on `isinstance` checks, noting that while simple, it becomes brittle and leads to significant code duplication when adding new operations.
Next, he examines Object-Oriented Programming (OOP), highlighting its benefit of keeping behavior close to data but pointing out its drawbacks, such as scattering related functionality across multiple classes and creating complex dependency graphs that hinder maintenance.
Sladen then introduces Python’s `functools.singledispatch` as a superior alternative for many cases, allowing developers to organize code by behavior (e.g., all calculation logic in one module) rather than by data type, which simplifies debugging and isolates dependencies.
Finally, he explains catamorphisms (or the visitor pattern for trees) as an advanced technique that eliminates duplicated traversal logic by separating structure from behavior, enabling highly testable and extensible code.
The talk concludes with a recommendation to start with simple functions, use OOP for cohesion, and adopt dynamic dispatch or catamorphisms when managing complex, shared data structures with diverse behaviors.

# Main Points

|   # | Main point                                                                                                                                                                                         |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The talk compares four polymorphism techniques: one big function, object-oriented programming, dynamic dispatch, and catamorphisms.                                                                |
|   2 | The one big function approach uses isinstance checks to determine behavior, which is simple but becomes brittle and hard to maintain as the codebase grows.                                        |
|   3 | Object-oriented programming places behavior next to data, which aids cohesion but scatters related functionality across multiple classes, leading to dependency hell and difficult debugging.      |
|   4 | Dynamic dispatch, implemented via functools.singledispatch, allows functions to be specialized based on the type of the first argument, keeping related behaviors together in separate modules.    |
|   5 | Dynamic dispatch decouples dependencies by organizing code by behavior rather than data, making it easier to isolate functionality like pretty printing or calculation.                            |
|   6 | Catamorphisms, or the visitor pattern for recursive data structures, separate the traversal logic from the specific operations applied to the data.                                                |
|   7 | This separation allows for easy addition of new behaviors, such as complexity calculation or type checking, without duplicating traversal code.                                                    |
|   8 | The speaker recommends starting with a simple function, using OOP for cohesion, dynamic dispatch for shared data types with different systems, and catamorphisms for complex recursive structures. |
|   9 | Python’s method resolution order (MRO) underpins dynamic dispatch, ensuring predictable behavior similar to OOP method lookup.                                                                     |
|  10 | Performance differences between these approaches are minimal compared to the maintenance benefits of choosing the right structure.                                                                 |
|  11 | Debugging is often easier with dynamic dispatch and catamorphisms because the call stack is explicit and related code is grouped together.                                                         |

# Video

[![Video thumbnail](https://img.youtube.com/vi/hidy15rK2a4/hqdefault.jpg)](https://www.youtube.com/watch?v=hidy15rK2a4)

[Watch on YouTube](https://www.youtube.com/watch?v=hidy15rK2a4)
