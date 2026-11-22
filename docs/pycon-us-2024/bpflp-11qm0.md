---
layout: default
title: "Talks - Henry Fredrick Schreiner III: Modern binary build systems"
nav_order: 196
parent: PyCon US 2024
type: Video Note
description: "The presentation outlines the modernization of Python binary package building, highlighting the transition from legacy tools like `setuptools` and `distutils` to standardized PEP 517 backends."
resource: "https://www.youtube.com/watch?v=bPflP-11qM0"
youtube_stats:
  view_count: 448
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

The presentation outlines the modernization of Python binary package building, highlighting the transition from legacy tools like `setuptools` and `distutils` to standardized PEP 517 backends.
The speaker details the capabilities of `cibuildwheel`, a tool for building redistributable binary wheels across various platforms, noting its support for Python 3.13, Apple Silicon, and upcoming free-threaded Python features.
Significant attention is given to `scikit-build-core`, a CMake-based backend that simplifies configuration through declarative data classes, dynamic metadata plugins, and an override mechanism for platform-specific settings, which has been adopted by major projects like CMake and RAPIDS AI.
Additionally, the talk covers `maturin` for Rust-based extensions, emphasizing its efficient cross-compilation and ability to build packages without a Python interpreter, as well as `meson-python` for projects like SciPy and NumPy.
The session concludes with a discussion on the ecosystem's evolution, including the use of these tools for shipping executables, integrating with Conda, and the ongoing efforts to standardize dynamic metadata and improve support for complex scientific computing dependencies.

# Main Points

|   # | Main point                                                                                                                                                                  |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Building Python binary packages involves three components: writing bindings, build configuration, and tools to build wheels across platforms.                               |
|   2 | CI Build Wheel is a Python tool that builds redistributable binary wheels for Mac, Linux, and Windows, supporting Python 3.13 and Apple Silicon runners.                    |
|   3 | CI Build Wheel can run locally via pipx and supports installing the built wheel to run tests, with upcoming support for free-threaded Python and UV.                        |
|   4 | Traditional setup.py and distutils are fragile, lack public APIs, and require extensive custom code, as seen in NumPy's 13,000 lines of patching code.                      |
|   5 | PEP 517 introduced a standardized API for build backends, allowing dynamic dependency installation and separating build logic from the frontend.                            |
|   6 | Modern build backends like Flit, Poetry, PDM, and Hatchling emerged after 2017, with binary package adoption growing through tools like Maturin and Meson Python.           |
|   7 | Meson Python, developed by SciPy and NumPy, reduced NumPy's build code from 13,000 to 2,000 lines by using the Meson build tool and pybind11.                               |
|   8 | Meson Python requires a pyproject.toml, a pybind11 file, and a meson.build file, supporting editable installs and free-threaded Python.                                     |
|   9 | Pythia Build Core is a CMake-based build backend that supports free-threaded Python, editable installs, and automatic CMake installation if missing.                        |
|  10 | Pythia Build Core features over 40 configuration options, dynamic metadata plugins, and an override mechanism for platform-specific settings.                               |
|  11 | Pythia Build Core is used by projects like CMake, Ninja, and RAPIDS AI, and supports building executables by targeting the bin folder.                                      |
|  12 | Maturin is a Rust-based build tool that can build Python packages without Python, leveraging Cargo's cross-compilation capabilities and stable ABI support.                 |
|  13 | Maturin integrates with CI Build Wheel and GitHub Actions, enabling efficient cross-compilation and building wheels for multiple Python versions.                           |
|  14 | The Scientific Python Development Guide provides resources and templates for using Pythia Build Core, Meson Python, and Maturin.                                            |
|  15 | Dynamic metadata plugins in Pythia Build Core allow generating metadata like version from source code, with plans to standardize this across backends.                      |
|  16 | Building executables with Pythia Build Core is straightforward for CMake projects, while non-CMake projects may require writing a CMake wrapper or using Hatchling plugins. |
|  17 | Future developments include replacing the Pythia Build backend with Pythia Build Core and improving support for unconventional binary differences and CUDA.                 |

# Video

[![Video thumbnail](https://img.youtube.com/vi/bPflP-11qM0/hqdefault.jpg)](https://www.youtube.com/watch?v=bPflP-11qM0)

[Watch on YouTube](https://www.youtube.com/watch?v=bPflP-11qM0)
