---
layout: default
title: "Rust for CPython: Making Python Safer and More Robust for Everyone - Emma Smith"
nav_order: 85
parent: PyCon US 2026
type: Video Note
description: "Emma Smith, a CPython core developer and Nvidia engineer, presented a compelling case for integrating Rust into the CPython codebase to address critical security and reliability issues inherent in C."
resource: "https://www.youtube.com/watch?v=42kibVnUHYE"
youtube_stats:
  view_count: 1044
  like_count: 33
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

Emma Smith, a CPython core developer and Nvidia engineer, presented a compelling case for integrating Rust into the CPython codebase to address critical security and reliability issues inherent in C.
She highlighted that CPython contains over a million lines of C code, which is susceptible to undefined behaviors such as data races, buffer overflows, and use-after-free errors, particularly as the project undergoes major changes like free-threading and JIT compilation.
While existing mitigations like fuzzing and sanitizers help, they do not prevent these issues, and the volume of security reports is increasing, placing a heavy burden on volunteer maintainers.
Smith proposed an experimental introduction of Rust in Python 3.16, starting with the zlib module, leveraging the highly optimized zlib-rs crate to provide significant performance improvements and enhanced memory safety.
The proposal includes strict constraints, such as maintaining C fallbacks for platforms where Rust is unavailable and ensuring that Rust code is only used where it offers clear benefits, aiming to reduce vulnerabilities by orders of magnitude as demonstrated by the Android project’s experience.

# Main Points

|   # | Main point |
| --: | ---------- |
|   1 | Emma Smith is a CPython core developer, MyPy core team member, and open source engineer at Nvidia who co-leads the Rust for CPython working group. |
|   2 | CPython contains over one million lines of C code, which provides speed and portability but is susceptible to undefined behavior such as data races, buffer overflows, and use-after-free errors. |
|   3 | Undefined behavior in C can lead to crashes, corrupted data, and security vulnerabilities, and it is difficult to reliably detect in large codebases. |
|   4 | Major CPython changes like free-threading, sub-interpreters, and JIT have modified over 500,000 lines of C code, increasing the risk of bugs in newer code. |
|   5 | Current mitigations like fuzzing, sanitizers, and LLM analysis only partially address undefined behavior and increase the maintenance load on volunteer core developers. |
|   6 | Rust is proposed to improve reliability through compile-time correctness checks, preventing spatial and temporal memory errors and making data races impossible by default. |
|   7 | The Android project reported a more than 1,000x reduction in memory safety vulnerabilities and increased engineer productivity after adopting Rust. |
|   8 | The proposal for Python 3.16 involves introducing an experimental private Rust API to implement the zlib module using the zlib-rs crate, which is significantly faster than standard zlib. |
|   9 | Rust code in CPython will require a C fallback to ensure compatibility with platforms where Rust is not available or supported. |
|  10 | Platform support concerns are addressed by identifying unsupported users and potentially using the GCC backend for Rust to support platforms not covered by LLVM. |
|  11 | The core team will focus on areas where members are comfortable with Rust and will incrementally migrate code only where Rust provides sufficient benefit. |
|  12 | Unsafe Rust usage will be strictly limited, carefully reviewed, and supported by well-tested libraries to minimize the risk of undefined behavior. |
|  13 | Future plans include expanding Rust usage to modules handling untrusted input like IO, JSON, and the parser, and potentially stabilizing an official Python Rust API. |
|  14 | The Rust Python project is slower than CPython because it lacks decades of interpreter loop optimization, making it less suitable for replacing the core interpreter. |
|  15 | Quality assurance for Rust implementations will rely on differential fuzzing and property-based testing to ensure they match existing C implementations. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/42kibVnUHYE/hqdefault.jpg)](https://www.youtube.com/watch?v=42kibVnUHYE)

[Watch on YouTube](https://www.youtube.com/watch?v=42kibVnUHYE)
