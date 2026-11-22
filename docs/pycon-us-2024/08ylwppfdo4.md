---
layout: default
title: "Talks - Michael Chow, Richard Iannone: Making Beautiful, Publication Quality Tables in Python..."
nav_order: 144
parent: PyCon US 2024
type: Video Note
description: "In this session from Ballroom BC, software engineers Michael Chow and Rich Ian from Posit PBC demonstrate how to create beautiful, publication-quality tables in Python using the `great_tables` libr..."
resource: "https://www.youtube.com/watch?v=08yLWPpFdo4"
youtube_stats:
  view_count: 991
  like_count: 29
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

In this session from Ballroom BC, software engineers Michael Chow and Rich Ian from Posit PBC demonstrate how to create beautiful, publication-quality tables in Python using the `great_tables` library.
They argue that tables are a powerful, often overlooked form of data visualization that can be generated entirely within a reproducible Python workflow, eliminating the need to export data to Excel or design software.
The presentation outlines three key ingredients for effective table design: structure (adding titles and column spanners), formatting (customizing numbers, dates, and currencies to meet industry standards), and styling (applying colors and bold text to highlight insights).
Additionally, they showcase advanced features such as nanoplots (sparklines) for visualizing trends, heatmaps via data color, and the ability to embed images directly into table cells.
The speakers emphasize that `great_tables` supports both Polars and Pandas data frames, offering a comprehensive API that allows users to maintain a consistent, code-driven pipeline from analysis to final reporting.

# Main Points

|   # | Main point                                                                                                                                       |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Making publication-quality tables in Python is achievable in 2024 using the Great Tables (GT) library.                                           |
|   2 | Tables for display are distinct from raw data frames, focusing on communication, styling, and insight extraction for human readers.              |
|   3 | Key goals of table visualization include clear titles, column spanners, highlighted rows, and visual elements like bar charts to aid comparison. |
|   4 | The Great Tables API is based on concepts from the 1949 US Census Manual of Tabular Presentation to formalize table structure.                   |
|   5 | Using GT allows for a reproducible workflow entirely within Python, avoiding the need to export data to Excel or design software.                |
|   6 | The three key ingredients for creating presentation-quality tables are structure, formatting, and styling.                                       |
|   7 | Structure involves adding titles, column spanners, and relabeling columns to manage information hierarchy.                                       |
|   8 | Formatting methods allow customization of numbers, percentages, and currencies to meet specific industry or business requirements.               |
|   9 | Styling uses the `tab_style` method with `loc` for location and `style` for visual attributes like background colors and bold text.              |
|  10 | Polars selectors and lazy expressions facilitate easy column selection and row filtering for styling and formatting.                             |
|  11 | Advanced features include `format_nanoplot` for adding interactive sparklines that reveal trends and allow value inspection on hover.            |
|  12 | The `data_color` method enables heat maps to emphasize value differences and reveal patterns across rows and columns.                            |
|  13 | Comprehensive formatting methods exist for numbers, integers, scientific notation, percentages, currencies, and byte sizes.                      |
|  14 | Great Tables supports both Polars and Pandas as input, with Pandas using lambdas for row selection where Polars uses lazy expressions.           |
|  15 | Output formats include HTML and various image types such as PDF, PNG, and TIFF, though JPEG is not currently supported.                          |
|  16 | Interactive features like pagination for large datasets are planned but not yet available in the current version.                                |
|  17 | Accessibility features are being improved for HTML output to better support screen readers, though color-based accessibility is limited.         |
|  18 | Summary rows and subtotals are a common use case that the team aims to support more robustly in future updates.                                  |
|  19 | For email compatibility, particularly with Outlook, inlining CSS styles is recommended to prevent formatting breakage.                           |
|  20 | The library is installed via `pip install great-tables` and includes a site with examples and a blog for further learning.                       |

# Video

[![Video thumbnail](https://img.youtube.com/vi/08yLWPpFdo4/hqdefault.jpg)](https://www.youtube.com/watch?v=08yLWPpFdo4)

[Watch on YouTube](https://www.youtube.com/watch?v=08yLWPpFdo4)
