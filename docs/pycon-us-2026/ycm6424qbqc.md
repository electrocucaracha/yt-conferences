---
layout: default
title: "Beyond Optional in Real-World Projects: Missing, None, and Unset - Koudai Aono"
nav_order: 126
parent: PyCon US 2026
type: Video Note
description: "The speaker, a Python developer and PEP co-author, addresses a common bug in API development where distinguishing between a missing key, an explicit `None` value, and an omitted argument is difficu..."
resource: "https://www.youtube.com/watch?v=ycm6424qbqc"
youtube_stats:
  view_count: 602
  like_count: 3
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

The speaker, a Python developer and PEP co-author, addresses a common bug in API development where distinguishing between a missing key, an explicit `None` value, and an omitted argument is difficult using standard typing.
To solve this, the talk introduces the use of `NotRequired` for boundary payloads and the new `Sentinel` feature (available in Python 3.15 and `typing_extensions`) to safely handle partial updates without conflating these states.
The presentation recommends using `TypedDict` for external JSON payloads to enforce strict typing at the boundary, while converting them into lightweight `dataclasses` for internal business logic and database operations.
This approach ensures that omitted fields retain their existing values rather than being overwritten by defaults, providing a robust pattern for safe data model updates.
The session concludes with a discussion on the ergonomics of sentinels and the potential integration of these features into libraries like Pydantic.

# Main Points

|   # | Main point                                                                                                                                          |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | An HTTP PATCH endpoint bug occurs when a missing key and an explicit null value are both treated as null, causing unintended data overwrites.       |
|   2 | The core issue is conflating three distinct states: missing key, null value, and omitted argument, which require different handling logic.          |
|   3 | The speaker advocates for using typing.TypedDict to define payload shapes, distinguishing between required and NotRequired fields.                  |
|   4 | NotRequired allows keys to be omitted from the payload, while Optional allows a key to be present with a null value.                                |
|   5 | Read-only fields in TypedDict prevent accidental mutation of payload data, enforcing type safety at the boundary.                                   |
|   6 | Using None as a default argument is problematic because it cannot distinguish between an explicitly sent null and an omitted argument.              |
|   7 | Python 3.15 introduces the sentinel function, and typing_extensions provides backport support for older Python versions.                            |
|   8 | The sentinel object serves as a unique marker to represent an "unset" state, allowing type checkers to distinguish it from None.                    |
|   9 | A helper function can be created to check if a value is unset and return the existing database value or the new update value.                       |
|  10 | Type guards using the type is statement provide runtime validation and narrow types for type checkers in complex payload scenarios.                 |
|  11 | Dataclasses are recommended for internal business logic because all fields must exist, unlike TypedDicts which support optional keys.               |
|  12 | A conversion pattern should be used to transform boundary TypedDict payloads into internal dataclass models for domain logic.                       |
|  13 | This separation keeps wire-format concerns out of business code and ensures all dataclass fields are explicitly initialized.                        |
|  14 | Pydantic currently lacks full support for the unset sentinel pattern, making standard library typing solutions more portable.                       |
|  15 | The recommended workflow is to use TypedDict for external payloads, convert to dataclasses for internal use, and use sentinels for partial updates. |
|  16 | This approach ensures safe partial updates by explicitly handling missing keys, null values, and omitted arguments.                                 |

# Video

[![Video thumbnail](https://img.youtube.com/vi/ycm6424qbqc/hqdefault.jpg)](https://www.youtube.com/watch?v=ycm6424qbqc)

[Watch on YouTube](https://www.youtube.com/watch?v=ycm6424qbqc)
