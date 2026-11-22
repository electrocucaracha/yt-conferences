---
layout: default
title: "Talks - David Hewitt: How Python Harnesses Rust through PyO3"
nav_order: 188
parent: PyCon US 2024
type: Video Note
description: "David Hu, a lead maintainer of PyO3, presents a technical deep dive into how Python harnesses Rust through the PyO3 library, emphasizing Rust’s ability to provide power and precision beyond Python’..."
resource: "https://www.youtube.com/watch?v=UilujdubqVU"
youtube_stats:
  view_count: 1978
  like_count: 72
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

David Hu, a lead maintainer of PyO3, presents a technical deep dive into how Python harnesses Rust through the PyO3 library, emphasizing Rust’s ability to provide power and precision beyond Python’s limits.
He explains that PyO3 uses procedural macros to generate C-compatible bindings, allowing Rust code to be seamlessly imported into Python via the standard `import` statement, a mechanism identical to traditional C and C++ extensions.
The talk traces the execution path of a Python function call, detailing how the interpreter’s `CALL` bytecode invokes `PyObject_Vectorcall`, which resolves to a Rust function pointer through a "trampoline" that manages critical safety invariants, such as preventing Rust panics from crashing the C-based interpreter and handling deferred reference counts.
Hu highlights the rapid growth of Rust in the Python ecosystem, noting that Rust project uploads to PyPI are doubling annually and may soon rival C and C++ in volume.
Finally, he discusses future concurrency challenges, suggesting that Rust’s memory safety model aligns well with Python’s emerging free-threading and sub-interpreter features, potentially requiring deliberate design choices around mutability and locking to ensure safe multi-threaded interoperability.

# Main Points

|   # | Main point                                                                                                                                                                    |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Rust is increasingly used to implement Python software, offering reliability, performance, security, and concurrency benefits that go beyond Python's limits.                 |
|   2 | PyO3 is a Rust library that provides bindings to Python, allowing Rust code to run inside Python programs or vice versa.                                                      |
|   3 | PyO3 uses procedural macros, similar to Python decorators, to generate C API code that creates Python functions, classes, and modules from Rust code.                         |
|   4 | Python's import statement can load native libraries using the C ABI, a mechanism historically used by C and C++ extensions that Rust now utilizes.                            |
|   5 | Over 350 projects upload Rust-based code to PyPI monthly, with over 3 billion annual downloads, and Rust adoption in the Python ecosystem is doubling yearly.                 |
|   6 | A simple word-counting function rewritten in Rust via PyO3 is 2 to 4 times faster than its Python equivalent, with similar syntax and structure.                              |
|   7 | When Python calls a Rust function, the interpreter executes a CALL bytecode that invokes PyObject_VectorCall, which resolves the function pointer to the Rust implementation. |
|   8 | PyO3 generates a trampoline function marked as extern "C" to ensure correct C ABI calling conventions between Python and Rust.                                                |
|   9 | PyO3 prevents Rust panics from crossing into the C-based Python interpreter by using panic traps and converting them into Python BaseException objects.                       |
|  10 | PyO3 defers reference count updates for Python objects held by Rust threads until it is safe to do so, avoiding potential deadlocks related to the Global Interpreter Lock.   |
|  11 | Arguments passed from Python to Rust are structured as a C array of references, a count of positional arguments, and a tuple of keyword names.                                |
|  12 | PyO3 extracts these arguments into Python objects and then converts them into corresponding Rust types using implemented traits for type conversion.                          |
|  13 | The final step in the call chain is a direct function call to the user-defined Rust logic after argument extraction and safety checks are complete.                           |
|  14 | Subinterpreters in Python 3.12 enforce isolation between interpreters, which aligns well with Rust's memory safety model without requiring extensive locking.                 |
|  15 | Free-threading in Python 3.13 presents challenges for Rust interoperability, potentially requiring mutexes around PyO3 objects or encouraging immutable data structures.      |
|  16 | PyO3 aims to provide a seamless interface where Rust extensions behave like native Python modules, maintaining a low barrier to entry for developers.                         |

# Video

[![Video thumbnail](https://img.youtube.com/vi/UilujdubqVU/hqdefault.jpg)](https://www.youtube.com/watch?v=UilujdubqVU)

[Watch on YouTube](https://www.youtube.com/watch?v=UilujdubqVU)
