---
layout: default
title: "Metaclasses Demystified - Jason C. McDonald"
nav_order: 114
parent: PyCon US 2025
type: Video Note
description: "In this presentation, speaker Jason explains Python metaclasses by defining them as templates that create classes, analogous to how classes serve as blueprints for objects."
resource: "https://www.youtube.com/watch?v=fEm0vi8SpkI"
youtube_stats:
  view_count: 3540
  like_count: 101
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

In this presentation, speaker Jason explains Python metaclasses by defining them as templates that create classes, analogous to how classes serve as blueprints for objects.
He outlines four primary functions managed by metaclasses: class instantiation, attribute storage, method resolution order (MRO), and inheritance checks.
The talk details practical use cases, including implementing singletons to ensure a single instance, enforcing class conventions by raising errors during class definition, customizing class namespaces as seen in Python’s `enum` module, and manipulating the MRO to alter attribute lookup behavior.
Additionally, the speaker demonstrates how metaclasses are necessary for overriding class-level dunder methods and how they power Abstract Base Classes (ABCs) through `__instancecheck__` and `__subclasscheck__`.
While acknowledging that metaclasses are complex and often unnecessary, the speaker emphasizes that they should be used sparingly and only when simpler solutions, such as decorators or standard inheritance, are insufficient to solve the specific problem at hand.

# Main Points

|   # | Main point                                                                                                                         |
| --: | ---------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Metaclasses are templates for creating classes, with `type` being the default metaclass in Python.                                 |
|   2 | A metaclass manages class instantiation, class attribute storage, method resolution order (MRO), and inheritance checks.           |
|   3 | The `__prepare__` method on a metaclass sets up the namespace for class attributes and methods before class creation.              |
|   4 | Singleton patterns can be implemented using metaclasses to ensure only one instance of a class is created.                         |
|   5 | Metaclasses can enforce class conventions by raising errors during class definition if specific methods or attributes are present. |
|   6 | The `__prepare__` method allows custom storage of class attributes, as seen in Python's `enum` implementation.                     |
|   7 | Metaclasses can manipulate the Method Resolution Order (MRO) to change how Python looks up methods and attributes.                 |
|   8 | Class-level dunder methods, such as `__getattr__`, must be defined on the metaclass to function correctly.                         |
|   9 | Abstract Base Classes (ABCs) use the `ABCMeta` metaclass to implement `__instancecheck__` and `__subclasscheck__`.                 |
|  10 | Inheriting from a class with a specific metaclass automatically applies that metaclass to subclasses.                              |
|  11 | Complex metaclass behaviors can often be replaced by simpler solutions like decorators or composition.                             |
|  12 | Real-world frameworks like Django, Flask, and Protocol Buffers utilize metaclasses to control class behavior.                      |
|  13 | Developers should evaluate whether a metaclass is necessary by first seeking the simplest solution to the problem.                 |
|  14 | Metaclasses are powerful but complex tools that should be used sparingly and only when standard Python features are insufficient.  |

# Video

[![Video thumbnail](https://img.youtube.com/vi/fEm0vi8SpkI/hqdefault.jpg)](https://www.youtube.com/watch?v=fEm0vi8SpkI)

[Watch on YouTube](https://www.youtube.com/watch?v=fEm0vi8SpkI)
