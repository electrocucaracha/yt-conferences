---
layout: default
title: 'Talks - Riva Quiroga: "But it works on my computer!" How to make our data analysis...'
nav_order: 81
parent: PyCon US 2024
type: Video Note
description: "Riva Quiroga, a computational linguist and research software engineer, presents on the critical importance of reproducibility in data analysis, using the retracted Duke University study as a cautio..."
resource: "https://www.youtube.com/watch?v=06KsKm_C_O0"
youtube_stats:
  view_count: 173
  like_count: 2
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

Riva Quiroga, a computational linguist and research software engineer, presents on the critical importance of reproducibility in data analysis, using the retracted Duke University study as a cautionary tale about how poor documentation and data handling can lead to invalid scientific results and real-world harm.
She argues that reproducibility extends beyond merely running code on a single machine; it requires robust communication, clear documentation, and standardized practices to ensure that analyses are reliable, auditable, and buildable upon by others.
To achieve this, Quiroga recommends adopting specific technical best practices, such as using virtual environments, version control with strategic releases, and cross-platform compatible file paths to manage dependencies and environment inconsistencies.
She emphasizes the necessity of intuitive directory structures and human-readable, parsable filenames to prevent errors, facilitate efficient data import, and allow team members to quickly identify and use the correct files without opening them.
Finally, she stresses the importance of testing data integrity to catch unexpected transformations, automating workflows where possible, and writing documentation that accounts for the onboarding needs of new team members, while also advocating for flexibility in adapting these best practices to existing organizational contexts.

# Main Points

|   # | Main point                                                                                                                                                                              |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Riva Quiroga, a computational linguist and fellow at the Software Sustainability Institute, presented on making data analysis reproducible.                                             |
|   2 | The presentation highlighted the Duke University case, where a retracted Nature article led to clinical trial failures and lawsuits due to poor documentation and data handling errors. |
|   3 | Reproducibility is defined as the ability to run the same analysis on the same data to reach the same results, ensuring reliability and allowing others to build upon previous work.    |
|   4 | Practitioners must assume they have no control over the operating systems or software versions used by their collaborators, necessitating robust environment management.                |
|   5 | Using virtual environments and requirements files in Python helps isolate dependencies and ensures consistent execution across different machines.                                      |
|   6 | Version control is essential for recording project history, but commit messages vary in granularity, making strategic use of releases helpful for marking significant milestones.       |
|   7 | A clear and intuitive directory structure is recommended, separating raw data from consolidated data, code, and results to facilitate understanding and rebuilding.                     |
|   8 | File paths should be constructed using OS or Pathlib libraries to ensure compatibility across Windows, Linux, and macOS operating systems.                                              |
|   9 | Writing good filenames is crucial for time optimization; names should be readable by both humans and computers to avoid encoding errors and facilitate batch processing.                |
|  10 | Filenames should avoid special characters and spaces, use padding for sequential numbering, and follow parsable patterns to allow easy filtering and variable extraction.               |
|  11 | Human-readable filenames enable quick identification of specific files, such as charts or datasets, without needing to open each one individually.                                      |
|  12 | Data validation is as important as code testing; analysts should verify that data values, categories, and dates are within expected ranges to prevent silent errors.                    |
|  13 | Automation tools like Make can streamline repetitive processes, while documentation should be written to onboard new team members effectively.                                          |
|  14 | Documentation must account for the tools and context a new user needs, rather than just providing instructions, to ensure the team can effectively utilize the project.                 |
|  15 | When data cannot be published due to privacy concerns, best practices include sharing anonymized data samples or mockups to demonstrate that the analysis code is correct.              |
|  16 | Teams should adapt to existing workflows while introducing best practices, balancing flexibility with the need for standardized, reproducible methods.                                  |
|  17 | Recommended resources for further learning include the book "Research Software Engineering with Python" and the online handbook "The Turing Way."                                       |

# Video

[![Video thumbnail](https://img.youtube.com/vi/06KsKm_C_O0/hqdefault.jpg)](https://www.youtube.com/watch?v=06KsKm_C_O0)

[Watch on YouTube](https://www.youtube.com/watch?v=06KsKm_C_O0)
