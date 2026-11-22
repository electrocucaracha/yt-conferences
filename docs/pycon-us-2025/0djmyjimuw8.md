---
layout: default
title: "Usando Python y Gemini para visualizar alertas sanitarias en una web accesible- Lía Da Silva - Rojas"
nav_order: 60
parent: PyCon US 2025
type: Video Note
description: "Lía da Silva Rojas presented a solution to improve the accessibility of health alerts in Chile, addressing the critical issue where defective contraceptives have led to unintended pregnancies with ..."
resource: "https://www.youtube.com/watch?v=0dJmYjiMUw8"
youtube_stats:
  view_count: 134
  like_count: 2
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

Lía da Silva Rojas presented a solution to improve the accessibility of health alerts in Chile, addressing the critical issue where defective contraceptives have led to unintended pregnancies with inadequate government compensation.
The current official system relies on inaccessible, scanned PDF documents that exclude individuals with cognitive or visual impairments, so Lía developed a web application using Python, Flask, and Google Gemini to parse this data.
By sending screenshots of the official alert pages to Gemini with specific prompts, the system extracts key information such as alert status, dates, and lot numbers, presenting it in a clear, accessible format with visual indicators for safety.
During the Q&A, Lía acknowledged that while her initial approach was basic, she is now refining the tool using Pydantic for better structured data handling and discussing potential improvements like adding user reporting forms and analyzing transparency data to measure the broader impact of these pharmaceutical failures.

# Main Points

|   # | Main point                                                                                                                                                              |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Lía da Silva Rojas presented her first talk on using Python and Gemini to visualize health alerts in an accessible web interface.                                       |
|   2 | The project addresses a critical issue in Chile where defective contraceptives caused unintended pregnancies, with inadequate compensation for affected women.          |
|   3 | The current government health alert system is inaccessible, relying on unselectable PDFs and complex dropdowns that exclude users with cognitive or visual impairments. |
|   4 | The solution uses Flask to display information and Gemini to process data by taking screenshots of the ISP site and sending them to the AI for analysis.                |
|   5 | Specific prompts instruct Gemini to return a binary status (0 or 1) and the most recent alert date if a record exists for a queried medication.                         |
|   6 | The system extracts lot numbers and specific reasons for alerts from PDF documents to provide clear, structured information to users.                                   |
|   7 | The final interface displays commercial medication names with visual indicators, such as red warnings for active alerts and green tickets for safe products.            |
|   8 | The presenter acknowledged that using Pydantic would simplify the workflow by allowing direct web access via tools, eliminating the need for screenshots.               |
|   9 | Challenges included handling security certificates required by the ISP site and managing ambiguous responses from large language models.                                |
|  10 | The application currently focuses on Western medicine with active ingredients, making it difficult to integrate traditional or natural remedies.                        |
|  11 | Future improvements include adding a form for users to report issues to CERNAC and conducting data analysis on alert frequency and medication types.                    |
|  12 | The system queries the web in real-time to ensure the most current alert status is provided, rather than relying on a static database.                                  |
|  13 | Using commercial names instead of chemical compounds helps accurately identify specific defective lots among medications with similar compositions.                     |
|  14 | The data source is limited to the ISP health alerts site, which lacks an API, though transparency requests could potentially yield more detailed impact data.           |
|  15 | The presenter suggested using MCP servers to automate browser interactions and bypass security certificate barriers for more robust data extraction.                    |

# Video

[![Video thumbnail](https://img.youtube.com/vi/0dJmYjiMUw8/hqdefault.jpg)](https://www.youtube.com/watch?v=0dJmYjiMUw8)

[Watch on YouTube](https://www.youtube.com/watch?v=0dJmYjiMUw8)
