---
layout: default
title: "Time Zones in Python: Everything You Wish You Didn't Need to Know - Paul Ganssle"
nav_order: 16
parent: PyCon US 2026
type: Video Note
description: "The speaker, a developer with over a decade of experience, presents a comprehensive overview of time zone complexities, arguing that simple rules do not exist and that developers must deeply unders..."
resource: "https://www.youtube.com/watch?v=Evrrzmo_ZMs"
youtube_stats:
  view_count: 204
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

The speaker, a developer with over a decade of experience, presents a comprehensive overview of time zone complexities, arguing that simple rules do not exist and that developers must deeply understand the underlying abstractions.
The talk clarifies fundamental concepts such as the distinction between UTC offsets and time zones, warns against relying on ambiguous abbreviations like CST, and highlights real-world irregularities, including non-hourly offsets, unusual daylight saving transitions in Morocco, and historical date line shifts in Kiribati.
A significant portion of the presentation focuses on Python’s time zone model, explaining the limitations of the `datetime` interface and the `pytz` library, particularly regarding ambiguous and imaginary times.
The speaker details the introduction of the `fold` attribute in Python 3.6 as a more robust solution for handling these edge cases and discusses the implementation of `zoneinfo` in Python 3.9, which relies on the IANA database to provide accurate, up-to-date time zone data.
Finally, the talk addresses subtle bugs in datetime comparison and arithmetic operations, recommending that developers convert times to UTC before performing calculations to ensure consistent and predictable results.

# Main Points

|   # | Main point                                                                                                                                                                         |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | UTC is the reference zone at zero offset, but it includes leap seconds which complicate its monotonic nature.                                                                      |
|   2 | There is a critical distinction between time offsets (like UTC-6) and time zones (like America/Chicago), which are sets of rules for how offsets change over time.                 |
|   3 | Time zone abbreviations like CST are context-dependent and ambiguous, so they should never be used to derive specific time zones in code.                                          |
|   4 | Time zone offsets are not limited to whole hours; some regions use half-hour or 15-minute offsets, and historical data includes non-whole minute offsets.                          |
|   5 | Standard offsets can change for reasons other than daylight saving time, such as Portugal's 1992 shift to Central European Time.                                                   |
|   6 | Daylight saving time transitions are not always seasonal; Morocco adjusted its DST schedule in 2012 to accommodate Ramadan.                                                        |
|   7 | Clock changes can occur at any time of day or year, as seen when Kiribati skipped December 31, 1994, to cross the International Date Line.                                         |
|   8 | Location does not always determine the time zone; in China, the observed offset in Xinjiang can depend on ethnic identity rather than just geography.                              |
|   9 | UTC is not a natural abstraction for human activities, which are organized around local solar time, so local time abstractions are necessary for representing wall-clock time.     |
|  10 | Storing local times as UTC is problematic because the mapping between local time and UTC is not stable across offset changes, leading to incorrect local time representations.     |
|  11 | Python's time zone model relies on the tzinfo abstract base class, which provides methods for UTC offset, name, and DST, though the DST method is often misused.                   |
|  12 | Python 2 required manual implementation of time zone rules, but Python 3.2 added support for fixed offsets, leaving local and IANA zones complex.                                  |
|  13 | Ambiguous times occur when clocks are set back, causing the same local time to happen twice, while imaginary times occur when clocks are set forward, creating non-existent times. |
|  14 | The datetime object in Python lacks sufficient information to distinguish between ambiguous times, a flaw not present in libraries like Pytz which store fixed tzinfo eagerly.     |
|  15 | Pytz's approach has ergonomic issues, such as requiring explicit localization and normalization after arithmetic, which can lead to subtle bugs.                                   |
|  16 | Python 3.6 introduced the fold attribute to resolve ambiguous times by indicating whether to use the offset before or after a transition, simplifying implementation.              |
|  17 | Naive datetimes in Python now represent local time, and converting them to UTC requires explicit methods like timestamp or astimezone.                                             |
|  18 | The zoneinfo module provides access to IANA time zone data by searching system locations or using a pip package, avoiding the need to bundle frequently updated data in Python.    |
|  19 | Equality comparisons in Python depend on whether datetimes share the exact same tzinfo object; if they do, clock time is compared, otherwise absolute UTC time is used.            |
|  20 | Arithmetic operations on datetimes in the same time zone preserve clock time, while operations across different time zones result in absolute time calculations.                   |
|  21 | To avoid confusion with Python's time zone semantics, it is recommended to convert operands to UTC before performing arithmetic or comparisons.                                    |
|  22 | There are no simple universal rules for time zones, so developers must deeply understand the specific abstractions and behaviors of the tools they use.                            |

# Video

[![Video thumbnail](https://img.youtube.com/vi/Evrrzmo_ZMs/hqdefault.jpg)](https://www.youtube.com/watch?v=Evrrzmo_ZMs)

[Watch on YouTube](https://www.youtube.com/watch?v=Evrrzmo_ZMs)
