---
layout: default
title: "Logs, Tears, and Feature Flags: Coding Stories in Survival Mode - Laura Meng"
nav_order: 10
parent: PyCon US 2026
type: Video Note
description: "Laura, a former Android developer and new mother, shares her experience of losing trust in technology after a baby-tracking app crashed and deleted critical data at 3 a.m."
resource: "https://www.youtube.com/watch?v=oYflWdKpXUE"
youtube_stats:
  view_count: 149
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

Laura, a former Android developer and new mother, shares her experience of losing trust in technology after a baby-tracking app crashed and deleted critical data at 3 a.m.
Drawing a parallel between the unpredictability of raising a child and managing production systems, she decided to build her own simple application using Python and the Streamlit framework.
To ensure reliability, she made key architectural decisions, such as decoupling the user interface from data storage to prevent data loss during session changes and implementing feature flags via Launch Darkly to manage optional features like graphs and external API calls.
She demonstrates the power of runtime configuration by using a "survival mode" context that acts as a kill switch, instantly disabling non-essential features to maintain core functionality when external dependencies fail.
Ultimately, Laura argues that the goal of software engineering is not to prevent all failures, but to design systems that can gracefully recover and remain resilient, much like preparing for the inevitable challenges of motherhood.

# Main Points

|   # | Main point |
| --: | ---------- |
|   1 | The speaker lost trust in technology when a baby tracking app froze and deleted critical data at 3 AM. |
|   2 | She decided to build her own application to reliably track her baby's sleep and feeding times. |
|   3 | The speaker has nine years of experience as an Android developer but no formal training in Python. |
|   4 | She chose Python and the Streamlit framework to build the app quickly without needing frontend knowledge. |
|   5 | Launch Darkly was used to manage feature flags and allow runtime changes without code redeployment. |
|   6 | The initial app design used Streamlit session state, which was rejected because data would not persist across devices or sessions. |
|   7 | A key architectural decision was made to separate the UI from data storage to ensure reliability. |
|   8 | Data persistence was handled via JSON storage, representing a database in larger applications. |
|   9 | Optional features like graphs and celebratory emojis were placed behind feature flags. |
|  10 | An external API dependency for sleep prediction was added and controlled by a feature flag. |
|  11 | When the external dependency failed, the feature could be disabled instantly without a code change or redeploy. |
|  12 | A "survival mode" was implemented using feature flag contexts to disable all optional features during failures. |
|  13 | Contexts allow feature flags to evaluate on or off status based on specific user or session attributes. |
|  14 | The kill switch concept acts as an emergency brake to stop non-critical features and stabilize the system. |
|  15 | The core principle is that the UI should not control critical data, and systems must be designed to fail gracefully. |
|  16 | Resilience in software is comparable to parenting, where one cannot prevent all issues but must prepare for recovery. |
|  17 | The goal is to ensure critical functionality remains available even when optional components fail. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/oYflWdKpXUE/hqdefault.jpg)](https://www.youtube.com/watch?v=oYflWdKpXUE)

[Watch on YouTube](https://www.youtube.com/watch?v=oYflWdKpXUE)
