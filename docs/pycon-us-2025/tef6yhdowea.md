---
layout: default
title: "Intuition vs. Reality: Surprising Truths in Python Performance - Arthur Pastel & Adrien Cacciaguerra"
nav_order: 17
parent: PyCon US 2025
type: Video Note
description: "In this interactive presentation, software engineers Arthur Pastel and Adrien Kachigua challenge common misconceptions about Python performance by comparing audience intuition against actual benchm..."
resource: "https://www.youtube.com/watch?v=TEF6yhdOwEA"
youtube_stats:
  view_count: 3084
  like_count: 68
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

In this interactive presentation, software engineers Arthur Pastel and Adrien Kachigua challenge common misconceptions about Python performance by comparing audience intuition against actual benchmark results.
They demonstrate that execution speed and memory consumption often involve trade-offs, such as how list comprehensions can be faster than generators but consume more memory, or how string concatenation via `join` is superior to iterative addition due to string immutability.
The speakers also explore the nuances of rewriting code in Rust, revealing that while Rust can offer significant speedups for complex algorithms like Fibonacci, the overhead of data conversion can make it slower than Python for simple tasks or when transferring large lists, unless optimized with PyO3 types.
By analyzing bytecode and context switching costs, they highlight that recursive functions are often slower than iterative stack-based approaches due to interpreter overhead.
Ultimately, the talk emphasizes that human intuition is frequently unreliable regarding performance, and the only definitive way to optimize software is to rigorously measure both execution time and memory usage.

# Main Points

|   # | Main point                                                                                                                                                                            |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The session introduces an interactive talk on Python performance by Arthur Pastel and Adrien Kachigua from Cut Speed, a dev tool for measuring and optimizing software performance.   |
|   2 | Cut Speed integrates with benchmarking libraries like py-benchmark and runs on GitHub runners to provide performance reports directly in pull requests.                               |
|   3 | Performance is critical for user experience, competitive advantage, cost savings in cloud computing, and reducing energy consumption.                                                 |
|   4 | Human intuition often fails to predict code performance accurately, even among experts, necessitating empirical measurement.                                                          |
|   5 | In a warm-up quiz, an async function without an await statement was faster than a time.sleep function because it did not execute the sleep logic.                                     |
|   6 | For counting even numbers in a list, using len with a list comprehension was faster than sum with a generator or a for loop due to reduced context switching overhead.                |
|   7 | However, the len-based approach consumed significantly more memory (approx. 4 MB) compared to the for loop or sum methods (hundreds of bytes), illustrating a speed-memory trade-off. |
|   8 | Memory consumption was measured using the tracemalloc module to determine peak memory usage after forcing garbage collection.                                                         |
|   9 | String concatenation using the join method is faster than using the addition operator because strings are immutable, causing the addition operator to create new objects repeatedly.  |
|  10 | List comprehensions are faster than list(map(lambda...)) because the latter incurs context switching costs between the map function and the lambda, despite having smaller bytecode.  |
|  11 | Recursive factorial implementations are slower than iterative stack-based implementations due to the overhead of pushing and popping call stack frames.                               |
|  12 | Stack-based implementations also avoid recursion depth limits imposed by the interpreter, allowing for deeper computations.                                                           |
|  13 | Rewriting small Python functions in Rust using rust-import can be slower than Python due to the overhead of data conversion between Python and Rust types.                            |
|  14 | For computationally intensive tasks like Fibonacci, Rust is significantly faster than Python because it executes native CPU instructions without the Python interpreter overhead.     |
|  15 | Binary search in Rust was slower than Python when converting the entire Python list to a Rust Vec, as the conversion cost (O(n)) outweighed the algorithm's efficiency (O(log n)).    |
|  16 | Using PyO3 types directly in Rust functions avoids full list conversion, making Rust faster for binary search by only converting accessed elements.                                   |
|  17 | The only reliable way to determine performance is to measure execution time and memory usage, as results depend on architecture, data size, and specific implementation details.      |
|  18 | The speakers released a new performance lab tool at PyCon US and encouraged attendees to provide feedback on the public beta.                                                         |
|  19 | The findings were tested exclusively on CPython, and the speakers noted that JIT-compiled implementations like PyPy might yield different results.                                    |
|  20 | Generators are not always slower than comprehensions; the performance impact depends on data size and whether the final goal is to create a list or stream data.                      |

# Video

[![Video thumbnail](https://img.youtube.com/vi/TEF6yhdOwEA/hqdefault.jpg)](https://www.youtube.com/watch?v=TEF6yhdOwEA)

[Watch on YouTube](https://www.youtube.com/watch?v=TEF6yhdOwEA)
