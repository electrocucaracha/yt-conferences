---
layout: default
title: "Pruebas E2E automatizadas con Playwright y Python - Joan Alejandro Esquivel Montero"
nav_order: 54
parent: PyCon US 2025
type: Video Note
description: "Juan Esquivel Montero, a QA engineer with over seven years of experience, presents a talk on automated testing using Playwright and Python."
resource: "https://www.youtube.com/watch?v=G7SzmAO_JbA"
youtube_stats:
  view_count: 225
  like_count: 9
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

Juan Esquivel Montero, a QA engineer with over seven years of experience, presents a talk on automated testing using Playwright and Python.
He explains that while Selenium is a traditional tool that connects code to browsers via drivers, Playwright is a comprehensive open-source framework that utilizes its own browser engines for Chromium, Firefox, and WebKit, offering greater flexibility and built-in features.
The presentation highlights Playwright’s advantages, including its support for multiple programming languages, integration with pytest for structured testing, and advanced capabilities such as device emulation, automatic screenshot and video generation, and detailed trace analysis for debugging.
Esquivel demonstrates a simple test case for a todo application, showcasing how Playwright simplifies code readability through fixtures and the Page Object Model pattern, while also discussing its integration with CI/CD pipelines.
In response to audience questions, he clarifies that Playwright does not require browser extensions but uses proprietary engine installations, and he advises that while Selenium may be more reliable for real-browser interactions, Playwright offers faster execution and modern features, making it a strong choice for contemporary test automation strategies.

# Main Points

|   # | Main point                                                                                                                                                                          |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Playwright is an open-source tool designed to automate software testing in browsers, supporting UI actions and HTTP request interception.                                           |
|   2 | Software testing involves static activities like documentation review and dynamic activities where tools like Playwright exercise the software to discover defects.                 |
|   3 | QA engineers have evolved into technical profiles who integrate with developers, use CI/CD, cloud, and containers, and test various areas including web, API, mobile, and AI.       |
|   4 | Python is a versatile language used across frontend, backend, data, and AI, making it a strong connection between business and technology for testing.                              |
|   5 | Selenium is a library that connects code to browsers via drivers and is not a full framework, whereas Playwright is a complete automation framework.                                |
|   6 | Playwright uses proprietary browser engines like WebKit, Firefox, and Chromium instead of external drivers, allowing for more controlled and consistent testing environments.       |
|   7 | Playwright is supported by Microsoft and has high download volumes, particularly in JavaScript, while Selenium relies more on community support and is evolving with new protocols. |
|   8 | The Playwright architecture uses contexts as isolated environments within a browser, similar to apartments in a building, each with independent storage and pages.                  |
|   9 | Installing Playwright requires dependencies like pytest and pytest-playwright, followed by the playwright install command to download the necessary browser engines.                |
|  10 | The pytest.ini file allows configuration of base URLs, tracing, and target browsers, enabling easy switching between different environments and browsers.                           |
|  11 | Writing tests in Playwright is straightforward, using fixtures like page to perform actions such as visiting URLs, filling inputs, and pressing keys.                               |
|  12 | Playwright provides built-in features for capturing screenshots, videos, and trace files, which can be analyzed using the playwright show trace command for detailed debugging.     |
|  13 | The Page Object Model is a recommended design pattern in Playwright documentation to maintain organized and readable test code by encapsulating page interactions.                  |
|  14 | Test data can be managed using JSON files and pytest fixtures to load specific data sets, improving test scalability and reducing code repetition.                                  |
|  15 | Playwright integrates easily with CI/CD pipelines, allowing for automated execution and the generation of JUnit reports and trace artifacts.                                        |
|  16 | Device emulation is supported in Playwright, allowing tests to simulate specific devices like iPhone 15 Pro Max by adjusting user agents and viewports.                             |
|  17 | While Selenium is considered more reliable for real browser interactions, Playwright offers faster execution and a more comprehensive framework experience.                         |
|  18 | Users should be aware of minor limitations in Playwright's browser engines compared to real browsers, requiring occasional manual verification to ensure accuracy.                  |

# Video

[![Video thumbnail](https://img.youtube.com/vi/G7SzmAO_JbA/hqdefault.jpg)](https://www.youtube.com/watch?v=G7SzmAO_JbA)

[Watch on YouTube](https://www.youtube.com/watch?v=G7SzmAO_JbA)
