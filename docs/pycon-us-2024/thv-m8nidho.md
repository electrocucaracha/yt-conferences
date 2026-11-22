---
layout: default
title: "Tutorials - Reuven M. Lerner: All about decorators"
nav_order: 23
parent: PyCon US 2024
type: Video Note
description: "In this comprehensive tutorial, instructor Ruben explores Python decorators, clarifying that they are distinct from design patterns and are instead powerful tools for adhering to the DRY principle ..."
resource: "https://www.youtube.com/watch?v=THv-m8niDho"
youtube_stats:
  view_count: 3746
  like_count: 89
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

In this comprehensive tutorial, instructor Ruben explores Python decorators, clarifying that they are distinct from design patterns and are instead powerful tools for adhering to the DRY principle by wrapping functions to add functionality without modifying the original code.
The session begins by demonstrating how to manually create a decorator using closures, where an outer function returns an inner wrapper function that has access to the outer scope’s variables, a mechanism that allows for state persistence across multiple function calls.
The instructor then introduces the official `@` syntax, explaining that it is syntactic sugar for reassigning a function to the result of a decorator, and highlights the necessity of using `*args` and `**kwargs` to ensure the wrapper can handle any number of arguments passed to the decorated function.
Practical exercises are provided to implement specific decorators, such as one that converts output to uppercase, another that logs execution time to a file, and a third that restricts function execution to once per minute using the `nonlocal` keyword to update state stored in the outer function.
The tutorial further advances to decorators that accept arguments, which require a three-level nested function structure, and demonstrates how to stack multiple decorators to apply various transformations sequentially.
Finally, the session covers decorating classes, showing how decorators can intercept class instantiation to add attributes or enforce patterns like singletons, while also addressing best practices such as using `functools.wraps` to preserve the original function’s metadata.

# Main Points

|   # | Main point                                                                                                                                |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Python decorators are distinct from design pattern decorators and function as higher-order functions that wrap other functions.           |
|   2 | The core mechanism involves an outer function that takes a function as an argument and returns an inner wrapper function.                 |
|   3 | The inner wrapper function executes every time the decorated function is called, allowing for pre- and post-processing logic.             |
|   4 | The `@` syntax is equivalent to reassigning the function name to the result of the decorator function call.                               |
|   5 | Decorators enable the DRY principle by extracting common functionality like logging, timing, or security checks into reusable components. |
|   6 | The `*args` and `**kwargs` parameters are essential in the wrapper to ensure the decorator works with functions of any signature.         |
|   7 | Closures allow the inner wrapper function to access local variables from the outer decorator function's scope.                            |
|   8 | The `nonlocal` keyword is required to modify variables defined in the outer function scope from within the inner wrapper.                 |
|   9 | Outer function storage persists across multiple calls to the decorated function, enabling features like call counting or caching.         |
|  10 | Memoization decorators can cache function results based on arguments to improve performance for pure functions.                           |
|  11 | Decorators can filter or modify input arguments before passing them to the original function, such as restricting types.                  |
|  12 | Decorators that accept arguments require a three-level nested function structure: decorator, middle function, and wrapper.                |
|  13 | Multiple decorators can be stacked on a single function, executing in a specific order from bottom to top during definition.              |
|  14 | The `functools.wraps` decorator preserves the original function's metadata, such as name and docstring, when wrapping.                    |
|  15 | Decorators can be applied to classes, where the outer function runs at class definition and the wrapper at instance creation.             |
|  16 | Class decorators can add attributes or methods to instances after `__init__` has executed.                                                |
|  17 | Python's scoping rules (LEGB) govern how inner functions access variables from enclosing scopes.                                          |
|  18 | Global variables and function objects persist in memory, which can lead to memory usage considerations with extensive decorator use.      |
|  19 | Custom exceptions can be raised within decorators to enforce constraints, such as rate limiting function execution.                       |
|  20 | The `isinstance` function is preferred over type equality checks for flexible type validation in decorators.                              |
|  21 | Decorators provide a mechanism to hijack function behavior at both definition time and runtime.                                           |
|  22 | The `functools.lru_cache` module offers a built-in implementation of memoization with cache size limits.                                  |
|  23 | Inner functions are not limited to decorators and can be used for other closure-based patterns in Python.                                 |
|  24 | Decorators are particularly useful for cross-cutting concerns like logging, authentication, and performance monitoring.                   |

# Video

[![Video thumbnail](https://img.youtube.com/vi/THv-m8niDho/hqdefault.jpg)](https://www.youtube.com/watch?v=THv-m8niDho)

[Watch on YouTube](https://www.youtube.com/watch?v=THv-m8niDho)
