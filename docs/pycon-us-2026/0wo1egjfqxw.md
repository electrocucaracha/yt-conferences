---
layout: default
title: "What's so hard about writing a type checker? A tour of ty - Carl Meyer"
nav_order: 1
parent: PyCon US 2026
type: Video Note
description: "Carl, an author of the Python type checker Ty (now part of OpenAI), presents a deep dive into Ty’s architecture at PyCon, emphasizing its speed and incremental nature."
resource: "https://www.youtube.com/watch?v=0Wo1eGjfQxw"
youtube_stats:
  view_count: 3165
  like_count: 29
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

Carl, an author of the Python type checker Ty (now part of OpenAI), presents a deep dive into Ty’s architecture at PyCon, emphasizing its speed and incremental nature.
Ty utilizes a query-based, on-demand approach powered by the Salsa library to perform fine-grained laziness, ensuring that only the minimal necessary code is analyzed for each keystroke or full project check, thereby avoiding the high costs of full recompilation.
The system builds a semantic index per file to track control flow via use-def chains and narrowing conditions without resolving types, allowing for efficient invalidation and reuse of cached data when files change.
Ty employs set-theoretic types, including unions, intersections, and negations, to handle complex type narrowing scenarios, such as discriminating between union members based on attribute checks, by simplifying types into disjunctive normal form.
Finally, the talk highlights Ty’s sophisticated diagnostic system, which lazily collects detailed, nested error contexts only when an error is confirmed and enabled, providing users with precise, "five whys" style explanations for type mismatches while maintaining performance.

# Main Points

|   # | Main point                                                                                                                         |
| --: | ---------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Ty is a Python type checker and language server developed by Astral, which is now part of OpenAI.                                  |
|   2 | The tool operates as a command-line checker for static analysis and as an LSP server providing real-time feedback in editors.      |
|   3 | Ty prioritizes speed through a lazy, query-based architecture that computes only the necessary information for requested feedback. |
|   4 | Fine-grained laziness allows Ty to check only the minimal portion of dependencies used by the code, ignoring unused parts.         |
|   5 | Salsa, a Rust library for incremental computation, manages caching and invalidation to avoid stale results and redundant work.     |
|   6 | Salsa uses a dependency graph where queries are automatically memoized and invalidated only when their inputs change.              |
|   7 | Semantic indexing extracts control flow information from a single file in isolation to prevent cross-file invalidation.            |
|   8 | Use-def chains record live bindings for variables to track possible values at specific points in control flow.                     |
|   9 | Semantic indexing records pointers to AST nodes and narrowing conditions rather than resolving types immediately.                  |
|  10 | Type inference uses live bindings to determine variable types, creating unions for multiple possible bindings.                     |
|  11 | Narrowing conditions from control flow create intersection types, representing values that satisfy multiple constraints.           |
|  12 | Set-theoretic types include unions, intersections, and negations, which map directly to set theory concepts.                       |
|  13 | Ty normalizes types into disjunctive normal form, allowing intersections inside unions but not vice versa.                         |
|  14 | Union filtering for sum types is achieved through general intersection type simplification rather than special casing.             |
|  15 | Diagnostics include severity levels, codes, summaries, and detailed context such as related code locations.                        |
|  16 | Ty performs a "five whys" analysis to provide nested explanations for complex assignability errors.                                |
|  17 | Diagnostic context collection is lazy to avoid performance overhead when errors are not present or suppressed.                     |
|  18 | The "possibly unresolved reference" diagnostic is disabled by default due to the difficulty of avoiding false positives.           |
|  19 | Ty is MIT licensed and developed in the open, welcoming contributions from the community.                                          |
|  20 | Support for frameworks like Django is currently evaluated through improved stubs rather than built-in special cases.               |
|  21 | Ty experiments with non-standard typing features like intersection types to test their practical utility.                          |
|  22 | Dynamic attribute checks using variables work if the variable has a literal string type, otherwise no narrowing occurs.            |

# Video

[![Video thumbnail](https://img.youtube.com/vi/0Wo1eGjfQxw/hqdefault.jpg)](https://www.youtube.com/watch?v=0Wo1eGjfQxw)

[Watch on YouTube](https://www.youtube.com/watch?v=0Wo1eGjfQxw)
