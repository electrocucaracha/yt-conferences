---
layout: default
title: "Lightning Talks - Saturday May 16, 2026 PM"
nav_order: 116
parent: PyCon US 2026
type: Video Note
description: "Keith opens the session by encouraging attendees to find Python communities through local meetups, user groups, and hobbies, using birding as an example of how Python tools like computer vision are..."
resource: "https://www.youtube.com/watch?v=VA3O7UxuZO4"
youtube_stats:
  view_count: 836
  like_count: 9
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

Keith opens the session by encouraging attendees to find Python communities through local meetups, user groups, and hobbies, using birding as an example of how Python tools like computer vision are embedded in everyday interests.
Chris Arisa introduces "Feder," a Rust-based security tool that uses CVSS scores to identify the most vulnerable Python packages on a system, allowing users to audit, search, and purge compromised dependencies with a single command.
Simon provides a rapid overview of recent LLM advancements, highlighting the November 2025 model surge, the rise of "claws" as personal digital assistants, and the emergence of high-performance open-weight models like Gemma 4 and GLM 5.1.
Ned Bachelder advocates for the "Pac-Man rule" applied to time, urging speakers to leave silences in conversations to create inclusive space for quieter voices to participate.
Eric presents "GH Profiler," a tool that analyzes GitHub user profiles and activity patterns to help maintainers distinguish between genuine human contributors and spam bots or AI-driven entities.
Guhan makes a humorous plea for financial support for the Python Software Foundation, emphasizing the economic importance of Python across various industries and the tax benefits of donations.
Sophia demonstrates the "daisy operator," a Python unpacking quirk that converts iterators into lists without explicit casting, showcasing its utility in simplifying code for dictionaries and custom iterables.
Jason shares his hobby of 3D printing, detailing how he used Python and GitHub workflows to process CAD files, generate exploded views, and create animated GIFs of mechanical assemblies.
Jared describes building an autonomous underwater vehicle for the RoboSub competition, utilizing Python’s serial and struct libraries to communicate with sonar and thrusters for navigation.
Gabriel explains his use of statistical methods and LSTM models to predict the arrival of baby opossums at a wildlife center, successfully winning a bet against colleagues by accurately forecasting the date.
Slot discusses using Python as a domain-specific language for tabletop RPGs, leveraging first-class objects to simplify rule calculations and avoid the complexity of writing custom parsers.
Finally, Ariel Ortiz presents a compiler for the esoteric HQ9+ programming language, demonstrating how it transpiles simple instructions into C code to produce executable programs for tasks like printing "Hello World" or generating quines.

# Main Points

|   # | Main point |
| --: | ---------- |
|   1 | Keith presented a guide to finding Python communities, noting that aggregators and conference lists often become outdated. |
|   2 | The Python ecosystem includes continental conferences like PyCon LatAm, country-level events, regional meetups, and topical or identity-based groups. |
|   3 | The Python Software Foundation maintains a pro network that aggregates meetups and can process fees for participating groups. |
|   4 | Keith emphasized that Python is ubiquitous in hobbies, using birding and the Merlin app's sound ID feature as an example of Python-based computer vision. |
|   5 | He encouraged attendees to find Python in their personal hobbies and bring those projects and creators back to local communities. |
|   6 | Chris Arisa introduced Feder, a multi-threaded Rust tool for finding the most vulnerable Python packages on a system. |
|   7 | Feder uses a bottom-up approach to scan all site-packages directories, including those in abandoned virtual environments, rather than relying on lock files. |
|   8 | The tool utilizes the Common Vulnerability Scoring System (CVSS) to rank risks, with scores ranging from one to ten. |
|   9 | Feder can identify packages with high CVSS scores, such as an old version of PyTorch with a score of 9.8, and provide links for remediation. |
|  10 | Users can filter results by minimum CVSS score and use Feder's search and purge commands to locate and remove vulnerable packages. |
|  11 | Simon discussed the rapid evolution of large language models, using the generation of an SVG of a pelican riding a bicycle as a benchmark. |
|  12 | He highlighted the November inflection point where coding agents like Codeex and Claude Code became significantly more capable. |
|  13 | The project OpenClaw, initially a small codebase, grew rapidly into a popular personal digital assistant, causing Mac Minis to sell out in Silicon Valley. |
|  14 | Google released Gemma 4, an open-weight model that runs on laptops, while Chinese labs released massive open-weight models like GLM 5.1. |
|  15 | Ned Bachelder discussed the "Pac-Man rule" applied to time, suggesting that leaving silence in conversations allows new voices to participate. |
|  16 | He argued that maintaining silence is crucial for inclusion and ensuring that Python remains a community for everyone. |
|  17 | Eric presented GH Profiler, a tool designed to analyze GitHub user profiles to distinguish between human contributors and spam bots. |
|  18 | The tool checks account age, profile information, and recent PR and issue activity to flag suspicious behavior, such as identical issues opened across multiple repositories. |
|  19 | GH Profiler can be run via the command line or integrated into GitHub Actions to automatically profile new contributors. |
|  20 | Guhan discussed the financial needs of the Python ecosystem, emphasizing that learning and maintaining Python infrastructure requires funding. |
|  21 | He encouraged donations to the Python Software Foundation and local organizations, noting that US tax law changes allow for tax deductions on donations. |
|  22 | Sophia introduced the "daisy operator," a Python quirk where star unpacking into a single variable creates a list without explicit casting. |
|  23 | This technique works with any object implementing the iterator protocol and can simplify code by directly converting dictionary keys to lists. |
|  24 | Jason shared his hobby of 3D printing, showing a business card with rotating gears designed using CAD software. |
|  25 | He used Python tools to process STEP files, generating exploded views and animated GIFs of the gear mechanisms via GitHub workflows. |
|  26 | Jared described building a 150-pound autonomous submarine for the RoboSub competition using Python. |
|  27 | The submarine uses a camera for obstacle detection and sonar for distance measurement, with Python's serial and struct libraries handling hardware communication. |
|  28 | Gabriel used statistical methods and LSTM models to predict the arrival of baby opossums at a wildlife center. |
|  29 | His model predicted the first arrival within one day of the actual date, winning a bet against colleagues who relied on intuition. |
|  30 | A speaker demonstrated using Python as a domain-specific language for tabletop RPGs, defining dice rolls and rules as first-class objects. |
|  31 | This approach eliminates the need for complex parsers and allows rules to be written directly as executable Python code. |
|  32 | Ariel Ortiz presented a compiler for the esoteric programming language HQ9 Plus, which supports only four specific instructions. |
|  33 | The compiler transpiles HQ9 Plus code into C, which is then compiled into an executable, demonstrating a full compilation pipeline for a joke language. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/VA3O7UxuZO4/hqdefault.jpg)](https://www.youtube.com/watch?v=VA3O7UxuZO4)

[Watch on YouTube](https://www.youtube.com/watch?v=VA3O7UxuZO4)
