---
layout: default
title: "Cython in Practice: A Deep Dive into Legacy C Integration and Debugging - Maryanne Wachter"
nav_order: 13
parent: PyCon US 2025
type: Video Note
description: "Maryanne Walker presents a deep dive into using Cython to integrate and debug legacy C code, specifically the Triangle library, to make it accessible via Python."
resource: "https://www.youtube.com/watch?v=rf_OJ2Egrj4"
youtube_stats:
  view_count: 1807
  like_count: 37
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

Maryanne Walker presents a deep dive into using Cython to integrate and debug legacy C code, specifically the Triangle library, to make it accessible via Python.
Motivated by the need for better control over dependencies for the `section properties` package, she developed an object-oriented wrapper that supports Python 3.10+ and multiple architectures, including Intel and Silicon Macs.
The project involved mapping C structures to Cython types and implementing memory management through `cinit` and `dealloc` methods, but testing revealed intermittent memory corruption errors on Windows that were not present on other platforms.
To resolve these issues, Walker utilized Valgrind within a Dockerized Linux environment, identifying three distinct bugs: a data type compatibility issue with `unsigned long`, insufficient memory allocation for holes, and a double-free error caused by pointer aliasing in the underlying C code when specific flags were used.
She successfully fixed these by modifying the legacy C source code and adopted a CI/CD pipeline using Poetry and GitHub Actions, noting that while UV offers modern tooling, it currently lacks robust support for Cython extension builds compared to standard tools.
Key takeaways include the importance of reviewing architecture-specific data type conventions, simplifying debugging environments by using tools like Valgrind in their native contexts, and the value of community engagement in open-source contributions.

# Main Points

|   # | Main point                                                                                                                                                                                                               |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Maryanne Walker presented a deep dive into using Cython to integrate and debug legacy C code, specifically the Triangle library, for Python accessibility.                                                               |
|   2 | The project originated from a request by maintainers of the section properties package to replace an unresponsive PyPI wrapper for the Triangle triangulation library.                                                   |
|   3 | Triangle is a C library from the early 2000s that generates triangular meshes without small angles, which is essential for finite element analysis in structural engineering.                                            |
|   4 | The primary goals were to create an object-oriented wrapper supporting Python 3.10+, ensure compatibility across all architectures including Intel and Silicon Macs, and enable knowledge transfer to other maintainers. |
|   5 | Cython conventions include using .pyx, .pxd, and .pxi files, along with cdef and cpdef function declarations to control accessibility between C and Python.                                                              |
|   6 | Memory views serve as stand-ins for arrays, and cimport statements are required for importing C functions into Cython files.                                                                                             |
|   7 | The integration process involved mapping C structs to Cython cdef structs, converting data types like reals to doubles, and handling pointers explicitly.                                                                |
|   8 | Cython classes require cinit for safe initialization of owned data structures and deallocation methods to prevent memory leaks by freeing allocated resources.                                                           |
|   9 | Property setters and getters were implemented to map C data structures to Python lists, using contiguous NumPy arrays for input to the C code.                                                                           |
|  10 | The core triangulate method required managing three separate instances of the Triangle object for input, output, and optional Voronoi output.                                                                            |
|  11 | Initial testing revealed non-reproducible memory corruption errors on Windows that did not occur on macOS or Linux.                                                                                                      |
|  12 | Runtime debugging with GDB was attempted but found to be fiddly and insufficient for detecting memory leaks, buffer overflows, or use-after-free errors.                                                                 |
|  13 | Valgrind was selected as the primary debugging tool due to its clear documentation and ability to identify memory corruption issues on Linux.                                                                            |
|  14 | The first issue identified was a data type compatibility problem where unsigned long was interpreted as four bytes instead of eight on Windows, requiring a macro change in the C source code.                           |
|  15 | Valgrind logs revealed invalid reads and writes caused by insufficient memory allocation for holes in the Cython setter functions.                                                                                       |
|  16 | A double-free memory error occurred because specific Triangle flags caused the input and output structs to share the same reference, leading to premature deallocation.                                                  |
|  17 | The double-free issue was resolved by modifying the underlying C code to copy data from the input struct to the output struct instead of using a shared reference.                                                       |
|  18 | Packaging was initially handled with Poetry and the core build backend, generating a setup.py file via build_ext.py.                                                                                                     |
|  19 | CI requirements included testing on Ubuntu, macOS, and Windows across multiple Python versions, with publishing to PyPI using Twine.                                                                                     |
|  20 | An attempt to switch to UV for packaging failed because the setuptools backend generated incorrect platform tags for Linux x86_64.                                                                                       |
|  21 | UV currently lacks robust support for Cython extension modules via scikit-build-core, so the workaround involved building wheels with CI build wheels and using UV for testing and publishing.                           |
|  22 | Key takeaways include reviewing architecture-specific data type conventions, simplifying the debugging environment, and leveraging Valgrind for low-level memory troubleshooting.                                        |
|  23 | The speaker emphasized the value of giving talks to find collaborators and the importance of supporting open source projects through low-level integration work.                                                         |

# Video

[![Video thumbnail](https://img.youtube.com/vi/rf_OJ2Egrj4/hqdefault.jpg)](https://www.youtube.com/watch?v=rf_OJ2Egrj4)

[Watch on YouTube](https://www.youtube.com/watch?v=rf_OJ2Egrj4)
