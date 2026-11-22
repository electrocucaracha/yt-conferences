---
layout: default
title: "GopherCon 2025: Porting the TypeScript Compiler to Go for a 10x Speedup V2 - Jake Bailey"
nav_order: 1
parent: GopherCon 2025
type: Video Note
description: "Jake, a TypeScript developer at Microsoft, explains the decision to rewrite the TypeScript compiler in Go to overcome JavaScript’s inherent performance limitations, such as memory constraints and t..."
resource: "https://www.youtube.com/watch?v=PZm_YbE3fcA"
youtube_stats:
  view_count: 7065
  like_count: 225
  channel_subscriber_count: 41100
tags:
  - gophercon-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-21T05:22:37+00:00
---

# Summary

Jake, a TypeScript developer at Microsoft, explains the decision to rewrite the TypeScript compiler in Go to overcome JavaScript’s inherent performance limitations, such as memory constraints and the lack of shared-memory concurrency.
The team selected Go for its speed, cross-platform capabilities, and structural similarity to TypeScript, which facilitated a direct port of the codebase.
By leveraging Go’s concurrency features and optimizing data structures, the new compiler achieves significant speedups, reducing VS Code’s build time from 80 seconds to just 7 seconds.
The project also transitions the language server to the standard Language Server Protocol (LSP), enabling asynchronous operations and improved editor responsiveness.
With major companies like Slack and Figma already experiencing substantial performance gains, the Go-based compiler is set to become TypeScript 7.0, marking a major evolution in the language’s tooling.

# Main Points

|   # | Main point                                                                                                                                       |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | TypeScript is a superset of JavaScript with a rich type system that verifies code before execution.                                              |
|   2 | The TypeScript compiler is written in TypeScript, which is unusual for a compiler written in a high-level language.                              |
|   3 | JavaScript limitations, such as single-threading and memory constraints, caused performance issues with large codebases.                         |
|   4 | The team decided to rewrite the TypeScript compiler in Go to improve speed and enable shared memory concurrency.                                 |
|   5 | Go was chosen because it is fast, cross-platform, supports garbage collection, and has a syntax similar to TypeScript.                           |
|   6 | A tool called TS-to-Go was created to automatically transform TypeScript code into Go code to aid the porting process.                           |
|   7 | The new Go-based compiler achieves 3 to 4 times faster single-threaded performance and over 10 times faster with concurrency.                    |
|   8 | Extensive testing with nearly 100,000 tests and baseline comparisons ensured behavioral parity between the old and new compilers.                |
|   9 | The Abstract Syntax Tree representation was changed from interfaces to embedded structs to reduce memory overhead and avoid boxing nil pointers. |
|  10 | A node allocation pool was implemented to reduce runtime allocations by 96% during parsing.                                                      |
|  11 | Concurrency was added to parsing, binding, and emitting phases, while type checking uses multiple independent checkers.                          |
|  12 | The language server protocol was adopted to replace the old synchronous protocol, enabling asynchronous and concurrent request handling.         |
|  13 | The Go race detector helped identify and fix concurrency bugs that were not present in the single-threaded JavaScript version.                   |
|  14 | Specific Go performance issues, such as method value allocations and string concatenation, were optimized for better efficiency.                 |
|  15 | Major users like Slack and Figma have reported significant build time reductions, with Slack seeing a nine-fold speedup.                         |
|  16 | TypeScript 7.0 will be the first release to include the Go-based compiler, following deprecations in TypeScript 6.0.                             |

# Video

[![Video thumbnail](https://img.youtube.com/vi/PZm_YbE3fcA/hqdefault.jpg)](https://www.youtube.com/watch?v=PZm_YbE3fcA)

[Watch on YouTube](https://www.youtube.com/watch?v=PZm_YbE3fcA)
