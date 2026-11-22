---
layout: default
title: "Talks - Juan Altmayer Pizzorno: Near Zero-Overhead Python Code Coverage"
nav_order: 198
parent: PyCon US 2024
type: Video Note
description: "Juan Altamirano from the University of Massachusetts Amherst Lab presents SlipCover, a tool designed to provide near-zero overhead Python code coverage by addressing the significant performance pen..."
resource: "https://www.youtube.com/watch?v=3dwNaOaWqnk"
youtube_stats:
  view_count: 338
  like_count: 4
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

Juan Altamirano from the University of Massachusetts Amherst Lab presents SlipCover, a tool designed to provide near-zero overhead Python code coverage by addressing the significant performance penalties associated with traditional tracing mechanisms like `sys.settrace`.
The project achieves this by instrumenting bytecode with native extension probes that record execution only once per line, reducing overhead from a median 200% to approximately 5% for line and branch coverage on Python versions 3.8 through 3.11.
For Python 3.12 and later, SlipCover leverages the new `sys.monitoring` API to register specific callbacks for line and branch events, further optimizing performance to 3% for line coverage and 12% for branch coverage by disabling events for already-covered code.
The tool also supports advanced applications such as guiding property-based testing and detecting dead code in production environments, with over 106,000 downloads indicating its utility.
While SlipCover aims to improve upon existing tools rather than replace them, it highlights the potential of `sys.monitoring` to make high-performance coverage analysis more accessible, though challenges remain in accurately mapping bytecode branches to source code for consistent coverage metrics.

# Main Points

|   # | Main point                                                                                                                                 |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | The speaker presents SlipCover, a tool designed to provide near-zero overhead Python code coverage.                                        |
|   2 | Traditional line coverage identifies executed lines, while branch coverage tracks taken and untaken conditional paths.                     |
|   3 | Standard tools like Coverage.py incur significant performance overhead, measured at a median of 200% for CPython and up to 1600% for PyPy. |
|   4 | High overhead slows down tests and continuous integration, potentially leading to less frequent testing.                                   |
|   5 | SlipCover achieves approximately 5% overhead for line and branch coverage on CPython and 31% on PyPy.                                      |
|   6 | The high cost of standard tracing APIs is inherent to the mechanism, adding 130% overhead even with empty callbacks.                       |
|   7 | SlipCover instruments bytecode by inserting probes that call into a native extension module to minimize overhead.                          |
|   8 | Recording coverage only once per line significantly reduces overhead by avoiding repeated native calls.                                    |
|   9 | Python code objects are read-only, requiring complex copying and reference updating to remove probes efficiently.                          |
|  10 | A batching mechanism triggers de-instrumentation based on a threshold, leaving only probes for unreached paths.                            |
|  11 | Supporting multiple Python versions (3.8 to 3.11) required handling varying bytecode formats and jump adjustments.                         |
|  12 | Python 3.12 introduced sys.monitoring, which allows high-performance monitoring without extensive bytecode editing.                        |
|  13 | SlipCover was rewritten to use sys.monitoring for Python 3.12 and later, achieving 3% overhead for line coverage.                          |
|  14 | Branch coverage via sys.monitoring provides bytecode-level jumps that differ from conceptual source code branches.                         |
|  15 | Direct implementation of branch events can alter coverage percentages, potentially causing confusion for users.                            |
|  16 | SlipCover inserts phantom lines to map bytecode branches to source code, maintaining consistent coverage metrics.                          |
|  17 | This approach reduces branch coverage overhead from 300% to 12% on Python 3.12.                                                            |
|  18 | Coverage.py also supports sys.monitoring for line coverage with about 9% overhead on Python 3.12.                                          |
|  19 | Coverage.py's branch coverage implementation via sys.monitoring is incomplete, showing 2000% overhead.                                     |
|  20 | SlipCover is available on GitHub and PyPI, aiming to improve existing tools rather than replace them.                                      |
|  21 | The project supports Python versions 3.8 through 3.13, using optimized bytecode instrumentation for older versions.                        |
|  22 | Future work includes better mapping of branch events to source code and integrating technology into Coverage.py.                           |

# Video

[![Video thumbnail](https://img.youtube.com/vi/3dwNaOaWqnk/hqdefault.jpg)](https://www.youtube.com/watch?v=3dwNaOaWqnk)

[Watch on YouTube](https://www.youtube.com/watch?v=3dwNaOaWqnk)
