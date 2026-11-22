---
layout: default
title: "Keeping up with Python: what makes upgrades hard, and what can we do about it - Jason Fried"
nav_order: 110
parent: PyCon US 2025
type: Video Note
description: "Jason Frerieded, a Python modernization engineer at Meta, discusses the persistent challenges of upgrading Python versions within large-scale monorepos, comparing the endless cycle to the myth of S..."
resource: "https://www.youtube.com/watch?v=2b-SeACd3tM"
youtube_stats:
  view_count: 2917
  like_count: 61
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

Jason Frerieded, a Python modernization engineer at Meta, discusses the persistent challenges of upgrading Python versions within large-scale monorepos, comparing the endless cycle to the myth of Sisyphus.
He argues that delaying upgrades exacerbates technical debt, as developers subconsciously build in deprecated behaviors, making future migrations significantly harder.
To mitigate these issues, Frerieded advises against ignoring deprecation warnings, recommending that teams actively fix them to avoid emergency refactors later.
He highlights the utility of automated code modification tools like LibCST and PyUpgrade, while cautioning against over-reliance on generative AI due to potential hallucinations.
Furthermore, he emphasizes the importance of code hygiene, such as avoiding private APIs and implementation details, and suggests that third-party package maintainers should provide source distributions that allow for easy regeneration of Cython sources to support new Python versions.
Ultimately, he advocates for a proactive upgrade cadence, noting that while upgrades are painful, they are necessary for performance gains and long-term system stability.

# Main Points

|   # | Main point                                                                                                                                                                  |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Jason Frerieded, a Python modernization engineer at Meta, has professionally upgraded Python versions from 2.7 to 3.12 over 13 years.                                       |
|   2 | Skipping Python versions does not simplify upgrades; instead, it allows deprecated behaviors to accumulate, making future transitions more difficult.                       |
|   3 | Monorepos at Meta facilitate code reuse and testing but create dependency bloat and require maintaining a consistent version universe across thousands of contributors.     |
|   4 | Python upgrades are necessary for performance gains in CPU and memory efficiency, as well as access to new language features.                                               |
|   5 | Common upgrade challenges include syntax changes, standard library modifications, runtime exceptions for previously legal code, and C API breakages in compiled extensions. |
|   6 | Upgrading third-party dependencies simultaneously with Python versions is complex due to API changes and subtle behavior shifts.                                            |
|   7 | Developers should avoid suppressing deprecation warnings, as they indicate issues that will become exceptions in future versions.                                           |
|   8 | Setting the PYTHONWARNINGS environment variable to "once" ensures developers see warnings without being overwhelmed, motivating timely fixes.                               |
|   9 | Manual code fixes are inefficient at scale; automated tools like regular expressions are crude and prone to errors.                                                         |
|  10 | LibCST allows for syntax-respecting and type-aware code mods, though writing them requires time and thorough testing.                                                       |
|  11 | Pre-made tools like pyupgrade can automate syntax upgrades, but Meta prefers reviewing diffs via code mods before committing.                                               |
|  12 | Generative AI can assist with upgrades but requires well-constructed prompts and careful verification to avoid hallucinated APIs.                                           |
|  13 | Code hygiene rules include avoiding access to private variables (prefixed with underscores) and not relying on undocumented implementation details.                         |
|  14 | Early adoption of unstable libraries like asyncio or dataclasses can lead to significant refactoring when APIs change.                                                      |
|  15 | When using private APIs or implementation details is unavoidable, developers must add verbose comments and unit tests to document the risk for future maintainers.          |
|  16 | Third-party packages often require major version jumps to support new Python versions, causing API incompatibilities.                                                       |
|  17 | Long-Term Support (LTS) models for libraries can help by guaranteeing API stability and providing builds for new Python versions.                                           |
|  18 | Pre-generated Cython sources are discouraged; generating them during the build process ensures compatibility with new Python versions.                                      |
|  19 | Closed-source Python wrappers for C libraries should be open-sourced or generated via Cython to allow regeneration for new Python versions.                                 |
|  20 | Meta sometimes backports changes from newer third-party packages to support new Python versions without accepting breaking API changes.                                     |
|  21 | Pitching upgrades to executives involves highlighting existential risks, such as loss of upstream support and security vulnerabilities.                                     |
|  22 | The upcoming Python 3.13 GIL removal will require adding mutexes to C++ code that previously relied on the GIL for thread safety.                                           |
|  23 | Internal benchmarking and Profile Guided Optimization (PGO) are used to detect performance regressions during upgrades.                                                     |
|  24 | A new project is underway to collect warnings during unit tests and display them as signals in code diffs to improve visibility.                                            |

# Video

[![Video thumbnail](https://img.youtube.com/vi/2b-SeACd3tM/hqdefault.jpg)](https://www.youtube.com/watch?v=2b-SeACd3tM)

[Watch on YouTube](https://www.youtube.com/watch?v=2b-SeACd3tM)
