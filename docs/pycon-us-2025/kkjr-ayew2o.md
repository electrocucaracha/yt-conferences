---
layout: default
title: "Metaprogramming with Decorators, Metaclasses, and Dynamic Code Generation - Aditya Mehra"
nav_order: 21
parent: PyCon US 2025
type: Video Note
description: "Adita Mera, a software architect and Python Software Foundation member, presents a practical guide to unlocking Python’s power through meta programming, which involves writing code that manipulates..."
resource: "https://www.youtube.com/watch?v=kKJR-aYew2o"
youtube_stats:
  view_count: 2328
  like_count: 35
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

Adita Mera, a software architect and Python Software Foundation member, presents a practical guide to unlocking Python’s power through meta programming, which involves writing code that manipulates other code by treating functions, classes, and code itself as data.
The talk explains that Python’s flexibility, where everything is an object, enables the use of decorators to wrap and modify function or class behavior, such as adding logging or handling authentication in frameworks like Django and Flask.
Mera further details the role of metaclasses, which serve as blueprints for creating classes and allow developers to enforce patterns or inject behaviors automatically during class creation, a technique heavily utilized in Django’s model management.
Additionally, the presentation covers dynamic code generation using the `exec` function to create and execute code at runtime, while emphasizing critical security considerations, such as avoiding raw user input and using safe evaluation methods to prevent dangerous system command execution.

# Main Points

|   # | Main point                                                                                                                                                                         |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Meta programming involves writing code that manipulates code, treating functions, classes, and code itself as data to automate patterns and build expressive APIs.                 |
|   2 | Python supports meta programming because everything is an object, including classes, which allows for dynamic creation of classes, functions, and attribute injection.             |
|   3 | Functions in Python are first-class objects that can be assigned to variables, passed as arguments, and returned from other functions.                                             |
|   4 | Decorators are a primary entry point for meta programming, allowing developers to wrap and modify the behavior of functions or classes without changing their source code.         |
|   5 | Function decorators use the at-sign syntax to apply a wrapper function that can add logging, authentication, or other behaviors around the original function.                      |
|   6 | Class-based decorators are used when a decorator needs to maintain state, requiring the implementation of the dunder call method to handle function calls.                         |
|   7 | Decorators are widely used in production frameworks like Django, Flask, and FastAPI for tasks such as logging, authentication, routing endpoints, and dependency injection.        |
|   8 | Metaclasses serve as blueprints for creating classes, defining how classes themselves behave, similar to how classes define the behavior of their instances.                       |
|   9 | In Python, the default metaclass is type, meaning every class is an instance of type, while objects are instances of their respective classes.                                     |
|  10 | Custom metaclasses can be created by inheriting from type and defining methods like dunder new to control class creation and enforce patterns or inject behaviors.                 |
|  11 | The dunder new method in a metaclass is where the class is built, allowing developers to validate attributes or raise errors if required components are missing.                   |
|  12 | Frameworks like Django and SQLAlchemy utilize metaclasses to manage model creation, enforce contracts, and provide flexible, expressive APIs.                                      |
|  13 | Dynamic code generation in Python is achieved using the exec function, which allows code to be generated as strings and executed at runtime.                                       |
|  14 | Dynamic code generation is useful for scripting engines, code templating, and creating classes or functions on the fly, such as defining a function that did not previously exist. |
|  15 | Security considerations are critical when using meta programming, especially with user input, as uncontrolled exec or eval can lead to dangerous system command execution.         |
|  16 | Best practices for safe dynamic code execution include avoiding raw user input, using ast.literal_eval for safe evaluation, and using restrictive namespaces in exec.              |

# Video

[![Video thumbnail](https://img.youtube.com/vi/kKJR-aYew2o/hqdefault.jpg)](https://www.youtube.com/watch?v=kKJR-aYew2o)

[Watch on YouTube](https://www.youtube.com/watch?v=kKJR-aYew2o)
