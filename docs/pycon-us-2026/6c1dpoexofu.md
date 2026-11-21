---
layout: default
title: "Lazy imports and the art of interpreter procrastination - Brittany Reynoso"
nav_order: 73
parent: PyCon US 2026
type: Video Note
description: "Britney Rhodenizer, a Python runtime engineer at Meta, presents lazy imports, a new feature in CPython 3.15 that defers module loading until first use to reduce startup time and memory overhead."
resource: "https://www.youtube.com/watch?v=6C1dPOeXOfU"
youtube_stats:
  view_count: 498
  like_count: 14
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

Britney Rhodenizer, a Python runtime engineer at Meta, presents lazy imports, a new feature in CPython 3.15 that defers module loading until first use to reduce startup time and memory overhead.
She explains that while the previously rejected PEP 690 proposed a global lazy import flag, the new implementation uses an explicit `lazy` keyword to ensure granular, local control and backward compatibility.
The mechanism works by creating lightweight proxy objects that are only reified into actual modules when accessed, a process optimized by Python’s adaptive interpreter to minimize runtime checks.
Rhodenizer highlights significant performance gains observed at Meta, including a 70% reduction in startup time and improved stability for large-scale applications like Instagram.
She also introduces Lifeguard, a static analysis tool designed to help developers safely adopt lazy imports by identifying potential side effects and compatibility issues, while noting that the feature is free-threading compatible and supports cleaner code structures by eliminating the need for nested imports.

# Main Points

|   # | Main point                                                                                                                                                                 |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Lazy imports are a new feature in CPython 3.15 that defers module loading until the imported name is actually used.                                                        |
|   2 | The speaker, Britney Rhodenizer, has worked on Python performance projects at Meta, including Pyro, Skybison, and Cinder.                                                  |
|   3 | Traditional Python imports execute top-level code immediately, causing cascading execution that can lead to slow startup times and high memory usage.                      |
|   4 | At Meta, Instagram’s Django tier loaded over 28,000 modules at startup, resulting in reloads taking up to two minutes and circular dependency issues.                      |
|   5 | An aggressive internal implementation of lazy imports at Meta reduced module loading by 12x, cut startup time by 70%, and improved memory stability.                       |
|   6 | PEP 690, which proposed global lazy imports via a runtime flag, was rejected due to unclear semantics, lack of granularity, and reliance on mutating core data structures. |
|   7 | The new approach in Python 3.15 uses an explicit `lazy` keyword to mark specific imports, ensuring behavior is local and does not cascade recursively.                     |
|   8 | Lazy imports create a lightweight proxy object instead of loading the module immediately, storing it in `sys.lazy_modules` for debugging.                                  |
|   9 | The module is only loaded and added to `sys.modules` when the imported name is first accessed during execution.                                                            |
|  10 | Implementation involves modifying four bytecodes: `IMPORT_NAME`, `IMPORT_FROM`, `LOAD_GLOBAL`, and `LOAD_NAME` to handle lazy proxy checks.                                |
|  11 | The adaptive interpreter optimizes away lazy import checks after observing reification, allowing direct access to the module dictionary.                                   |
|  12 | Backwards compatibility is supported through specialized containers that allow string-based lazy imports to behave semantically like standard imports.                     |
|  13 | Lazy imports are beneficial for reducing import overhead, improving startup times, and lowering memory usage in large projects.                                            |
|  14 | They also simplify code by removing the need for explicit typing imports and nested imports within functions.                                                              |
|  15 | Restrictions include incompatibility with functions, classes, try-except blocks, `import *`, and `from __future__` imports.                                                |
|  16 | Import-time side effects, such as registry patterns, are deferred until the module is loaded, requiring explicit registration to avoid missed registrations.               |
|  17 | Developers should be cautious when mutating `sys.modules` or relying on implicit submodule imports when using lazy imports.                                                |
|  18 | Lifeguard is a static analysis tool built-in Rust that detects lazy import compatibility by analyzing side effects conservatively.                                         |
|  19 | Lazy imports can help untangle circular dependencies if modules do not completely rely on each other at import time.                                                       |
|  20 | The feature is free-threading compatible, as the import lock is acquired during the bytecode operations that handle lazy loading.                                          |
|  21 | Adoption is recommended for projects with high import overhead, slow startup, or high memory usage, using profiling tools to identify candidates.                          |

# Video

[![Video thumbnail](https://img.youtube.com/vi/6C1dPOeXOfU/hqdefault.jpg)](https://www.youtube.com/watch?v=6C1dPOeXOfU)

[Watch on YouTube](https://www.youtube.com/watch?v=6C1dPOeXOfU)
