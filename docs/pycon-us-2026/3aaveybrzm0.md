---
layout: default
title: "Preflight Your Data: Catch Hidden Issues Before Handoff - Jennifer Slotnick"
nav_order: 25
parent: PyCon US 2026
type: Video Note
description: "The speaker, a software professional with a background in bioinformatics, presents a tool called \"Ferry\" designed to validate research data against FAIR standards before submission to repositories."
resource: "https://www.youtube.com/watch?v=3aavEybRzM0"
youtube_stats:
  view_count: 182
  like_count: 6
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

The speaker, a software professional with a background in bioinformatics, presents a tool called "Ferry" designed to validate research data against FAIR standards before submission to repositories.
The talk highlights common hidden data issues, such as placeholder coordinates, swapped dates, and duplicate IDs, which often survive manual handoffs because they appear superficially correct.
To address this, Ferry implements a pre-flight validation workflow that uses declarative YAML rule packs to check for specific errors, generating both machine-readable JSON and human-readable Markdown reports.
These reports include severity levels, specific row references, and actionable fix instructions, allowing non-technical users to efficiently resolve issues and rerun validations until the data meets submission requirements.
By starting with a small set of rules and focusing on clear, human-optimized feedback, the tool streamlines the data preparation process and reduces the inefficiencies associated with back-and-forth communication with repository reviewers.

# Main Points

|   # | Main point |
| --: | ---------- |
|   1 | The speaker has a background in software and bioinformatics and developed a tool called Ferry based on FAIR data standards to ensure research data is findable, accessible, interoperable, and reproducible. |
|   2 | Broken datasets often appear correct on the surface but contain hidden issues such as placeholder coordinates, taxonomy naming errors, swapped dates, duplicate IDs, and missing cross-references that only become apparent during handoff or repository review. |
|   3 | These data quality issues persist because the submission process remains largely manual, involving spreadsheets, email exchanges, and human review, which creates inefficiencies and delays known as repository purgatory. |
|   4 | The pre-flight validation workflow involves running checks for required fields and formulas, reviewing findings with human-readable explanations, previewing necessary fixes, and packaging deterministic outputs for submission. |
|   5 | The system uses a small set of rules, typically five to ten, to validate data, including checks for occurrence IDs, duplicate entries, suspicious coordinates, invalid ISO dates, and inconsistent country codes. |
|   6 | Validation rules include severity levels such as fails and warnings, where fails prevent submission to repositories while warnings allow for manual review and bypass if the data is verified as correct. |
|   7 | The technical architecture utilizes YAML files to define declarative rules that are processed by Python to generate both machine-readable JSON findings and human-readable Markdown reports. |
|   8 | Findings are structured as objects with specific codes, severity levels, and detailed explanations of where and why issues occur, allowing for configurable and reusable validation logic. |
|   9 | Human-readable reports are critical for collaboration, providing clear instructions on which rows to fix and prioritizing actions by resolving fail findings before addressing warnings. |
|  10 | The system tracks changes between runs to show what has been resolved since the last validation, helping teams manage long-running experiments and file sharing across different personnel. |
|  11 | Starting with local, basic rules and optimizing for human readability helps catch issues earlier in the process, making the validation workflow faster and more effective for research teams. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/3aavEybRzM0/hqdefault.jpg)](https://www.youtube.com/watch?v=3aavEybRzM0)

[Watch on YouTube](https://www.youtube.com/watch?v=3aavEybRzM0)
