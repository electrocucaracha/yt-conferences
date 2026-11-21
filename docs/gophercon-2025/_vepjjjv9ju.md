---
layout: default
title: "GopherCon 2025: Analysis and Transformation Tools for Go Codebase Modernization - Alan Donovan"
nav_order: 18
parent: GopherCon 2025
type: Video Note
description: "The speaker, a member of the Go team, presents tools for modernizing Go codebases to leverage newer language features while maintaining compatibility."
resource: "https://www.youtube.com/watch?v=_VePjjjV9JU"
youtube_stats:
  view_count: 3091
  like_count: 110
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

The speaker, a member of the Go team, presents tools for modernizing Go codebases to leverage newer language features while maintaining compatibility.
The talk highlights two primary approaches: first, "modernizers," which are static analysis tools that automatically suggest and apply fixes for specific patterns, such as replacing deprecated functions or simplifying loops using new iterators.
The speaker emphasizes the importance of these tools not only for improving code clarity and performance but also for addressing the issue of Large Language Models (LLMs) defaulting to outdated coding styles due to their training data.
To ensure safety, the development of these modernizers requires rigorous testing to avoid subtle bugs, as even simple transformations can introduce latent errors if edge cases are not handled correctly.
Second, the presentation introduces a more general and safer approach using a source-level inliner triggered by special comments, allowing developers to migrate their own codebases by inlining calls to deprecated functions.
This method handles complex semantic issues, such as side effects and evaluation order, systematically, making it a robust solution for large-scale refactoring.
The speaker notes that while bespoke modernizers are limited to core language features, the inliner offers a flexible, self-service mechanism for custom migrations.
Both tools are currently available for interactive use in the Go language server, with plans to integrate them into the standard `go fix` command in future releases, aiming to make code modernization easier, safer, and more accessible for both human developers and AI agents.

# Main Points

|   # | Main point                                                                                                                                   |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker works on the Go team in New York, focusing on static analysis tools like vet and go please.                                      |
|   2 | Go's compatibility promise ensures old code works indefinitely, but modernizing code to use newer features improves clarity and performance. |
|   3 | New Go features like range over functions, slices.contains, and range over int allow for simpler and more efficient code.                    |
|   4 | Automating code modernization saves time in code reviews and educates developers on new language features.                                   |
|   5 | Large language models often fail to use newer Go features, sticking to older patterns due to training on existing code.                      |
|   6 | Improving training data by modernizing existing Go code is essential to help AI models generate up-to-date code.                             |
|   7 | The Go analysis framework allows analyzers to run in various drivers, including CI systems, code review tools, and editors.                  |
|   8 | A modernizer is an analyzer that suggests safe fixes using newer Go features, requiring only cursory review.                                 |
|   9 | Approximately 20 modernizers were developed and released in go please 1.8, with user feedback indicating positive reception.                 |
|  10 | Even simple modernizers contain subtle bugs, such as changing variable types or ignoring side effects in loop limits.                        |
|  11 | Correctness in code transformations is critical because the benefit of each fix is small, so the risk of introducing bugs must be minimal.   |
|  12 | Direct syntax manipulation for modernizers is complex and requires careful handling of edge cases to avoid breaking code.                    |
|  13 | An alternative approach uses a source-level inliner triggered by special comments to safely inline deprecated function calls.                |
|  14 | This inlining method handles semantic complexity systematically, preventing bugs related to side effects and evaluation order.               |
|  15 | The inliner is approximately 7,000 lines of dense code and is already available for interactive use in go please.                            |
|  16 | Future plans include integrating these tools into the go fix command for batch processing in Go 1.26 or 1.27.                                |
|  17 | Comment handling remains a challenge for refactoring tools, with ongoing work to improve systematic comment preservation.                    |
|  18 | The inliner aims to be smarter to avoid unnecessary pedantic changes while maintaining safety and correctness.                               |
|  19 | Both modernizers and the inliner are released for interactive use, with batch commands planned for future Go releases.                       |

# Video

[![Video thumbnail](https://img.youtube.com/vi/_VePjjjV9JU/hqdefault.jpg)](https://www.youtube.com/watch?v=_VePjjjV9JU)

[Watch on YouTube](https://www.youtube.com/watch?v=_VePjjjV9JU)
