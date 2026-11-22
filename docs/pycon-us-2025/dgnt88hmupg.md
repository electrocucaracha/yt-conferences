---
layout: default
title: "The chaotic locals() and how we fixed it - Tian Gao"
nav_order: 100
parent: PyCon US 2025
type: Video Note
description: "In this presentation, Python core developer Tim explains the complex and often confusing behavior of the `locals()` built-in function and `frame.f_locals` in CPython."
resource: "https://www.youtube.com/watch?v=dGNt88HMUpg"
youtube_stats:
  view_count: 1726
  like_count: 65
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

In this presentation, Python core developer Tim explains the complex and often confusing behavior of the `locals()` built-in function and `frame.f_locals` in CPython.
He details how the introduction of "fast locals" (C arrays) for performance optimization broke the traditional two-way street between local variables and dictionaries, leading to unexpected side effects where reading `locals()` could revert changes made to local variables, particularly causing issues for debuggers like PDB.
To resolve these semantic ambiguities and ensure backward compatibility while improving reliability, the speaker introduces PEP 667, which splits the functionality into two distinct operations.
Under this new standard, `locals()` always returns a simple, immutable snapshot dictionary that does not affect the underlying state, while `frame.f_locals` is redefined as a write-through proxy that allows immediate and transparent modification of local variables.
This change empowers debuggers to execute code and modify variables safely without relying on fragile caching mechanisms or implicit refresh behaviors, ultimately providing clearer semantics and reducing surprising bugs in Python applications.

# Main Points

|   # | Main point                                                                                                                                                                               |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker, a Python core developer, discusses the chaotic behavior of the `locals` built-in function and its pitfalls.                                                                 |
|   2 | A bug in PDB was identified where the `ll` command reverted changes to local variables because it implicitly called `locals`, which refilled the cached dictionary with original values. |
|   3 | Historically, Python local scopes used dictionaries, but for performance, optimized scopes now use C arrays called fast locals.                                                          |
|   4 | The `locals` function creates a cached dictionary snapshot of fast locals, but modifying this dictionary does not update the underlying C array variables.                               |
|   5 | Calling `locals` multiple times returns the same dictionary object, which is refilled with current variable values, causing unexpected overwrites of user modifications.                 |
|   6 | The `exec` function implicitly calls `locals` when no namespace is provided, leading to inconsistent results depending on whether variables are defined as locals.                       |
|   7 | Debuggers like PDB rely on a `locals_to_fast` mechanism that runs after trace callbacks to write changes from the dictionary back to the C array.                                        |
|   8 | This mechanism is fragile because any explicit read of `locals` or `frame.f_locals` between writes can revert debugger changes.                                                          |
|   9 | PEP 667 was introduced to clarify semantics by splitting the behavior of `locals` and `frame.f_locals`.                                                                                  |
|  10 | Under PEP 667, `locals` in optimized scopes always returns a new, independent dictionary snapshot that does not affect underlying variables.                                             |
|  11 | Frame.f_locals` now returns a write-through proxy mapping that allows immediate modification of underlying local variables.                                                              |
|  12 | This change enables debuggers to execute statements and modify variables directly via `frame.f_locals` without relying on implicit trace callback synchronization.                       |
|  13 | The `locals_to_fast` function is retained for backward compatibility but no longer performs any actions.                                                                                 |
|  14 | Locals` was kept as a standard dictionary to maintain compatibility with user code that expects dictionary-specific behaviors.                                                           |
|  15 | Frame.f_locals` was changed to a proxy because it is primarily used by advanced tools like debuggers that require direct variable manipulation.                                          |
|  16 | The compiler cannot optimize frames based on `locals` usage because the function can be passed dynamically as a variable.                                                                |

# Video

[![Video thumbnail](https://img.youtube.com/vi/dGNt88HMUpg/hqdefault.jpg)](https://www.youtube.com/watch?v=dGNt88HMUpg)

[Watch on YouTube](https://www.youtube.com/watch?v=dGNt88HMUpg)
