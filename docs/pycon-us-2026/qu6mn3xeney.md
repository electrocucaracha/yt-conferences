---
layout: default
title: "pathlib: why and how to use it - Trey Hunner"
nav_order: 65
parent: PyCon US 2026
type: Video Note
description: "The speaker advocates for replacing string-based file paths with Python’s `pathlib` module to improve code readability, maintainability, and cross-platform compatibility."
resource: "https://www.youtube.com/watch?v=qU6mN3XENEY"
youtube_stats:
  view_count: 746
  like_count: 27
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

The speaker advocates for replacing string-based file paths with Python’s `pathlib` module to improve code readability, maintainability, and cross-platform compatibility.
Historically, path utilities were scattered across multiple standard library modules like `os`, `os.path`, `glob`, and `shutil`, making them difficult to locate and use consistently.
Representing paths as strings often leads to "stringly typed" code that is prone to bugs, particularly regarding operating system-specific separators, and makes it hard to distinguish paths from other string data.
In contrast, `pathlib` provides a unified, object-oriented interface with intuitive methods and attributes that simplify common operations such as joining paths, reading files, and creating directories.
The speaker notes that `pathlib` objects are widely supported by modern Python libraries and built-in functions, allowing for seamless integration without the need for manual string conversion.
While acknowledging that `pathlib` may have a slight performance overhead in specific high-volume scenarios, the speaker argues that the significant gains in code clarity and reduced error potential make it the superior choice for most development tasks.

# Main Points

|   # | Main point                                                                                                                                                                      |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | File paths should be represented using pathlib.Path objects instead of strings to improve code quality and maintainability.                                                     |
|   2 | Historically, path utilities were scattered across os, os.path, glob, and shutil modules, making them difficult to find and use.                                                |
|   3 | Representing paths as strings is error-prone because manual string manipulation can lead to bugs, especially regarding cross-platform separator differences.                    |
|   4 | Stringly typed code makes it difficult to distinguish file paths from other strings, reducing type safety and code clarity.                                                     |
|   5 | Pathlib.Path objects support chained method calls and attribute access, which is more readable than nested function calls required by string-based approaches.                  |
|   6 | The pathlib module provides convenient methods like read_text, glob, and mkdir that simplify common file operations compared to legacy modules.                                 |
|   7 | Since Python 3.6, the built-in open function and most standard library utilities accept pathlib.Path objects directly, eliminating the need for string conversion.              |
|   8 | Most modern third-party libraries, including Django, pandas, and Pillow, support pathlib.Path objects, ensuring broad compatibility.                                            |
|   9 | When creating path objects, forward slashes can be used in string literals for cross-platform compatibility, as pathlib normalizes separators automatically.                    |
|  10 | Path components can be joined using the join_path method, the slash operator, or by passing multiple arguments to the Path constructor.                                         |
|  11 | Pathlib.Path methods and attributes, such as name, parent, and suffix, are better named and more intuitive than their os.path counterparts.                                     |
|  12 | Custom path classes can be created by inheriting from pathlib.Path, allowing for specialized functionality and metadata preservation via with_segments.                         |
|  13 | The pathlike protocol defined in PEP 519 allows any object with a **fspath** method to be used anywhere a path is expected, enabling duck typing.                               |
|  14 | Users should avoid using the Path.open method, as it is a legacy feature; the built-in open function is the preferred and standard approach.                                    |
|  15 | Converting path objects to strings should be avoided unless necessary for display or logging, as most operations accept path objects directly.                                  |
|  16 | While pathlib may have a slight performance penalty in tight loops involving many files, readability and maintainability are generally more important than micro-optimizations. |
|  17 | Pathlib represents a proper data type for file paths, acknowledging their importance and providing a dedicated, well-designed API for path operations.                          |

# Video

[![Video thumbnail](https://img.youtube.com/vi/qU6mN3XENEY/hqdefault.jpg)](https://www.youtube.com/watch?v=qU6mN3XENEY)

[Watch on YouTube](https://www.youtube.com/watch?v=qU6mN3XENEY)
