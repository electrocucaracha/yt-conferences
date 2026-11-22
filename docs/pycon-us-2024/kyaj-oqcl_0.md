---
layout: default
title: "Talks - Koudai Aono: Enhancing Decorators with Type Annotations: Techniques and Best Practices"
nav_order: 182
parent: PyCon US 2024
type: Video Note
description: "In this PyCon talk, a software engineer from Tokyo presents techniques for enhancing Python decorators with type annotations to prevent bugs and improve code clarity."
resource: "https://www.youtube.com/watch?v=Kyaj-oQcl_0"
youtube_stats:
  view_count: 510
  like_count: 6
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

In this PyCon talk, a software engineer from Tokyo presents techniques for enhancing Python decorators with type annotations to prevent bugs and improve code clarity.
The speaker introduces a custom logging decorator for HTTP clients, demonstrating how to use `typing.Protocol` to define flexible interfaces for response objects and `ParamSpec` to accurately type positional and keyword arguments without relying on `Any`.
The presentation further explores `Concatenate` to inject additional arguments, such as a logger instance, into the decorated function’s signature, allowing type checkers to verify the modified call structure.
Additionally, the talk covers modern Python 3.12 features, including the new `type` keyword for defining generics and `TypeVarTuple` for handling variable-length argument lists, which collectively reduce unnecessary imports and improve code readability.
The speaker concludes by recommending the use of type checkers like Pyright to validate these advanced typing patterns, noting that while MyPy may lack support for the newest syntax, Pyright effectively handles the demonstrated best practices.

# Main Points

|   # | Main point                                                                                                                                                                                  |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The talk focuses on enhancing Python decorators with type annotations to prevent and detect bugs while establishing best practices.                                                         |
|   2 | Type hinting is valuable but challenging for decorators, particularly regarding callable types with ellipses and flexible arguments.                                                        |
|   3 | The presentation uses a remote logger decorator for HTTP clients as a practical example to demonstrate these concepts.                                                                      |
|   4 | Keyword-only arguments, indicated by an asterisk in function signatures, help enforce argument usage and prevent runtime errors in libraries with many parameters.                          |
|   5 | Typing Protocol allows defining interfaces for duck typing, enabling decorators to accept different HTTP clients like requests or httpx if they share attributes like status_code.          |
|   6 | ParamSpec is a feature that allows defining positional and keyword arguments as type hints, replacing the generic Any type for better precision.                                            |
|   7 | Concatenate Type adjusts function signatures by adding or removing specific arguments, allowing decorators to inject objects like loggers without requiring them in the caller's arguments. |
|   8 | Python 3.12 introduces the type keyword for defining new types and generics, reducing the need to import TypeAlias and TypeVar from the typing module.                                      |
|   9 | The new syntax allows defining generics within the function scope, such as using T for return types and P for ParamSpec, improving code readability.                                        |
|  10 | TypeVarTuple enables defining tuple variable lengths and changing argument order, which is useful for complex generic typing scenarios.                                                     |
|  11 | The speaker recommends using Pyright for type checking because it supports newer Python typing features that MyPy may not yet support.                                                      |
|  12 | Example code and test cases are available on GitHub for further reference and contribution.                                                                                                 |

# Video

[![Video thumbnail](https://img.youtube.com/vi/Kyaj-oQcl_0/hqdefault.jpg)](https://www.youtube.com/watch?v=Kyaj-oQcl_0)

[Watch on YouTube](https://www.youtube.com/watch?v=Kyaj-oQcl_0)
