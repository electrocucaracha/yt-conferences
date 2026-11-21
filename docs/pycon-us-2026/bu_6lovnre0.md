---
layout: default
title: "No More Spreadsheets! Building PyLadiesCon Infrastructure with Python and Django - Mariatta"
nav_order: 53
parent: PyCon US 2026
type: Video Note
description: "Mariatta, a nine-time conference organizer and PyLadies Con co-organizer, shares her journey from attending PyCon US to leading a fully online, multilingual, and free conference that serves the glo..."
resource: "https://www.youtube.com/watch?v=bU_6lovnre0"
youtube_stats:
  view_count: 439
  like_count: 10
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

Mariatta, a nine-time conference organizer and PyLadies Con co-organizer, shares her journey from attending PyCon US to leading a fully online, multilingual, and free conference that serves the global Python community.
She highlights the significant operational challenges of managing such an event with a small core team and limited budget, noting that traditional tools like spreadsheets became a bottleneck due to their lack of security, poor accessibility, and the inefficient manual data entry they required.
Recognizing that this administrative burden wasted the valuable time and skills of volunteers who are often from underrepresented groups, the team decided to build a custom, open-source web portal using Python, Django, and PostgreSQL.
This infrastructure, hosted on PSF infrastructure, replaced spreadsheets with a secure database, enabling automated email workflows, granular access control, and real-time public dashboards for sponsorship and volunteer data.
The result was a more efficient and transparent operation that raised over $55,000 in sponsorships in 2025, demonstrating how investing in proper technical infrastructure can better support community missions and enable meaningful open-source contributions.

# Main Points

|   # | Main point |
| --: | ---------- |
|   1 | Mariatta is a nine-time conference organizer who previously ran PyCon US, PyCascades, and PyLadies Con. |
|   2 | PyLadies Con is a free, fully online, 24-hour conference serving the global PyLadies community with multilingual support. |
|   3 | The conference relies heavily on volunteers who speak various languages and cover different time zones to provide 24-hour programming. |
|   4 | Organizers initially managed operations using spreadsheets, which caused issues with data duplication, access control, and readability. |
|   5 | Spreadsheets created a bottleneck where skilled volunteers spent time on administrative copy-pasting rather than high-impact contributions. |
|   6 | The team decided to build a custom web portal to replace spreadsheets, aiming for better data management and volunteer enablement. |
|   7 | The PyLadies Con portal is built with Python, Django, and Postgres, featuring 100% test coverage and Dockerized local development. |
|   8 | The portal is hosted on PSF infrastructure, specifically on Cabochon, the same platform that hosts PyPI. |
|   9 | Django Allauth was used to handle user authentication, including login, logout, and email verification. |
|  10 | MailDev is used during local development to test automated emails sent to volunteers and sponsors. |
|  11 | The portal allows for granular access control, restricting specific data fields and pages based on user roles. |
|  12 | Volunteer management was improved by automating invitation emails and tracking status without context switching between spreadsheets and email clients. |
|  13 | Sponsorship management was streamlined by enabling one-click data sharing with the PSF for contract preparation. |
|  14 | The portal provides meaningful, stable URLs for sharing data, replacing long, confusing spreadsheet links. |
|  15 | In 2025, the conference raised $55,000 in sponsorships, more than double the combined total of the first two years. |
|  16 | Public dashboards were created to display real-time sponsorship and attendance data, enhancing transparency and accountability. |
|  17 | The system supports multi-language features, including Brazilian Portuguese, to better serve the global community. |
|  18 | Integrations with ticketing systems allow for live data updates on attendee numbers without manual spreadsheet entry. |
|  19 | Future plans include replacing remaining spreadsheets with dedicated modules for speaker tracking and financial auditing. |
|  20 | The project emphasizes open source principles, allowing community members to contribute code and fix issues via pull requests. |
|  21 | The decision to build a custom tool was driven by the need to own data, avoid third-party dependencies, and utilize developer skills effectively. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/bU_6lovnre0/hqdefault.jpg)](https://www.youtube.com/watch?v=bU_6lovnre0)

[Watch on YouTube](https://www.youtube.com/watch?v=bU_6lovnre0)
