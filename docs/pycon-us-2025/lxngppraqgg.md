---
layout: default
title: "Lightning Talks - Sunday, May 18th, 2025 AM"
nav_order: 8
parent: PyCon US 2025
type: Video Note
description: "The video transcript captures a lively session of lightning talks at a Python conference, featuring diverse topics ranging from technical best practices to community insights."
resource: "https://www.youtube.com/watch?v=lXngPPRaqGg"
youtube_stats:
  view_count: 1750
  like_count: 27
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

The video transcript captures a lively session of lightning talks at a Python conference, featuring diverse topics ranging from technical best practices to community insights.
Speakers discuss practical solutions for handling phone numbers using the E164 standard and the `phonenumbers` package, as well as the benefits of using keyword arguments in Python 3.13 to prevent human error in function calls.
Other presentations highlight the use of `uv` for faster Docker builds, the integration of cat emojis into Sphinx documentation, and a personal account of the New York Times tech strike, emphasizing the challenges and rewards of unionization.
The session also includes personal stories about overcoming ADHD through hardware projects, a decade of contributions to the Python Korea community, and an introduction to PEP 750 template strings for safer and more flexible string processing.
The event concludes with a series of announcements for upcoming regional Python conferences worldwide, including PyCon Africa, PyCon Brazil, and EuroPython, alongside a sneak peek at a documentary on the history of Python.

# Main Points

|   # | Main point                                                                                                                                            |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Phone numbers are local and difficult to validate without regional context, so use the E164 standard for global representation.                       |
|   2 | The `phonenumbers` package parses free-text phone numbers into E164 format if provided with the correct country code or regional context.             |
|   3 | Web forms should include a country dropdown to resolve ambiguity in phone number validation and storage.                                              |
|   4 | Python 3.13 deprecates passing optional arguments as positional arguments in `re.sub` to prevent errors where flags are mistaken for counts.          |
|   5 | Using keyword arguments makes code self-documenting, prevents argument order errors, and simplifies refactoring.                                      |
|   6 | Linters can automatically enforce keyword argument usage or check that positional argument names match parameter names to reduce human error.         |
|   7 | Python can be embedded in Windows batch files by base64-encoding the distribution, allowing execution without a standard installation.                |
|   8 | Uv`is a fast Python package manager that supports`pyproject.toml` and generates lockfiles for reproducible Docker builds.                             |
|   9 | Using `uv` with locked requirements in Docker improved build times by 70% and reduced image size by 30% due to default bytecode compilation behavior. |
|  10 | Sphinx-nechan` is a Sphinx extension that allows adding cat emojis to documentation and slides using markdown-style syntax.                           |
|  11 | The New York Times engineering team went on strike, learning that unionizing is hard and management may hire contractors to replace striking workers. |
|  12 | Strike outcomes included converting at-will employment to just-cause, securing remote work guarantees, and providing overtime pay for on-call work.   |
|  13 | A developer with ADHD and anxiety built a Raspberry Pi marquee sign to manage focus and learn hardware skills like wiring and dimming.                |
|  14 | The Python Korea community has grown over ten years, evolving from basic talks to complex asyncio optimizations and enterprise scaling.               |
|  15 | PEP 750 introduces T-strings in Python 3.14, which are like f-strings but evaluate to a `Template` object for safer and more flexible processing.     |
|  16 | T-strings help prevent SQL injection and XSS vulnerabilities by allowing libraries to inspect static and interpolated parts separately.               |
|  17 | Python communities in Africa are passionate and resource-constrained, fostering strong local skills and close-knit support networks.                  |
|  18 | Numerous regional Python conferences are scheduled for 2025, including events in Europe, Asia, the Americas, and Africa.                              |
|  19 | A documentary about the history of Python will have its world premiere at EuroPython 2025.                                                            |

# Video

[![Video thumbnail](https://img.youtube.com/vi/lXngPPRaqGg/hqdefault.jpg)](https://www.youtube.com/watch?v=lXngPPRaqGg)

[Watch on YouTube](https://www.youtube.com/watch?v=lXngPPRaqGg)
