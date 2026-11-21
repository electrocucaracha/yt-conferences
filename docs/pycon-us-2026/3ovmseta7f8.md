---
layout: default
title: "PEP 750 - T-strings: safer and smarter string processing - Vinícius Gubiani Ferreira"
nav_order: 72
parent: PyCon US 2026
type: Video Note
description: "Vines, a Python specialist from Brazil, presented on T-strings, a new feature introduced in Python 3.14 that extends f-strings by returning a `Template` object rather than a final string."
resource: "https://www.youtube.com/watch?v=3OvmsETa7f8"
youtube_stats:
  view_count: 461
  like_count: 8
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

Vines, a Python specialist from Brazil, presented on T-strings, a new feature introduced in Python 3.14 that extends f-strings by returning a `Template` object rather than a final string.
This design allows for lazy interpolation, enabling developers to inspect static and dynamic parts of the string before processing, which facilitates custom logic such as security sanitization, formatting, and debugging.
The presentation highlighted key use cases, including preventing SQL injection and cross-site scripting (XSS) through centralized libraries, improving template debugging compared to Jinja2, and creating structured logging outputs like JSON.
While T-strings offer enhanced security and flexibility, they come with trade-offs, including a performance cost due to extra object allocation and the requirement for explicit processing methods to convert the template into a usable string.
The speaker emphasized that while T-strings are not a mandatory replacement for all string operations, they provide a standardized, secure foundation for library maintainers and developers who need robust input validation and output control.

# Main Points

|   # | Main point |
| --: | ---------- |
|   1 | T-strings are a new feature introduced in Python 3.14 that provide lazy string interpolation and enhanced security capabilities. |
|   2 | The speaker, Vines from Brazil, is a Python specialist at Azium Technologies and previously translated Python documentation to Brazilian Portuguese. |
|   3 | Python has historically used multiple string formatting methods, including percent syntax, old templates, dot format, and f-strings, which lack standardization for security and transformation. |
|   4 | T-strings differ from f-strings by returning a Template object rather than a direct string, allowing for inspection and processing before final output. |
|   5 | The string module became a package in Python 3.14, including a new template_lib.py module, which may complicate backward compatibility for language-level modifications. |
|   6 | Key attributes of T-strings include strings for static parts and interpolations for dynamic parts, enabling developers to access and manipulate these components separately. |
|   7 | T-strings support lazy evaluation, allowing developers to check string content before and after conversion, unlike f-strings which immediately produce a string. |
|   8 | Processing T-strings requires a custom method to iterate over static and dynamic parts, applying logic such as case conversion or sanitization. |
|   9 | T-strings can be concatenated using the plus sign, combining static and dynamic parts into a single template object. |
|  10 | Security is a primary motivation for T-strings, addressing vulnerabilities like SQL injection and cross-site scripting by allowing safe HTML or SQL escaping during processing. |
|  11 | Libraries such as html-ntd and sqlstring already utilize T-strings for sanitization, with some backporting support to Python 3.13. |
|  12 | T-strings are useful for breaking down complex Jinja templates into smaller, testable, and debuggable components, improving code maintainability. |
|  13 | T-strings can be integrated with logging to produce both human-readable text and machine-readable formats like JSON or CSV. |
|  14 | A significant drawback of T-strings is the lack of automatic string output, requiring boilerplate processing methods that may lead to code repetition. |
|  15 | Performance costs are higher than f-strings due to extra checks and memory allocation, trading speed for security and flexibility. |
|  16 | Complexity and user experience challenges include learning a new string type, potential confusion with legacy templates, and inconsistent error messages. |
|  17 | Partial standardization means the PEP defines capabilities but leaves implementation details to developers, leading to varied approaches across libraries. |
|  18 | T-strings are particularly beneficial for library maintainers seeking a centralized, mainstream approach to security and string handling. |
|  19 | Future developments include PEP 787 for using T-strings in subprocess calls to enhance security, and an early draft PEP for indented code alignment. |
|  20 | The PEP authors are available for open space sessions and sprints to discuss further ideas and implementations related to T-strings. |
|  21 | While T-strings offer significant advantages in security and flexibility, developers should weigh the performance and complexity costs against their specific use cases. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/3OvmsETa7f8/hqdefault.jpg)](https://www.youtube.com/watch?v=3OvmsETa7f8)

[Watch on YouTube](https://www.youtube.com/watch?v=3OvmsETa7f8)
