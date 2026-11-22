---
layout: default
title: "Program Your Own Computer in Python - Glyph"
nav_order: 94
parent: PyCon US 2025
type: Video Note
description: Dr.
resource: "https://www.youtube.com/watch?v=ucWdfZoxsYo"
youtube_stats:
  view_count: 11226
  like_count: 269
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

Dr.
Cliff presents a compelling case for leveraging the raw computational power and unique capabilities of personal computers using Python, arguing that local machines are often faster and more capable than cloud-based alternatives for tasks like running test suites or serving web requests.
The talk demonstrates how Python can directly control desktop applications across different operating systems, such as extracting data from Keynote on macOS via AppleScript, interacting with Linux accessibility interfaces, and automating Windows applications using PyWinAuto or COM.
Beyond controlling existing software, the presentation highlights the benefits of building custom desktop GUIs for features like global hotkeys, system tray persistence, and native notifications, which are difficult to achieve with web or command-line tools.
It introduces accessible libraries like Tkinter, Toga, and Notify-Py to lower the barrier to entry for desktop development, emphasizing that modern Python tools make it easier than ever to bridge the gap between simple scripting and full platform integration.
Ultimately, the speaker encourages developers to overcome self-imposed limitations and utilize their local hardware’s full potential, noting that the necessary tools are free, well-documented, and readily available through standard package managers.

# Main Points

|   # | Main point                                                                                                                                                                                                           |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Personal computers possess significant computational power and functionality that are often underutilized by Python developers who default to cloud services.                                                        |
|   2 | Local machines can execute full test suites significantly faster than cloud runners, with one example showing a 70% to 80% reduction in latency compared to GitHub Actions.                                          |
|   3 | Desktop computers can handle high-load tasks, such as serving over 10,000 requests per second with a pure Python web server on a single core.                                                                        |
|   4 | Python can directly control desktop applications on macOS using the AppScript library to access AppleScript hooks, allowing for data extraction from apps like Keynote and Safari.                                   |
|   5 | On Linux, desktop automation is achievable through the AT-SPI accessibility interface using the pyatspi package or via the D-Bus system using the dasbus library.                                                    |
|   6 | Windows desktop automation can be performed using the PyWinAuto library for accessibility interfaces or through COM/OLE technologies via PyWin32, though the latter is more complex and less consistently supported. |
|   7 | Desktop GUIs offer advantages over web or command-line tools, including precise keyboard focus control, global hotkey registration, persistent background processes in system trays, and native notifications.       |
|   8 | Tkinter remains a viable, cross-platform option for simple GUIs with minimal code, though it lacks accessibility support and has packaging constraints.                                                              |
|   9 | The Toga toolkit provides a more modern, accessible, and cross-platform alternative to Tkinter with a streamlined build tool called Briefcase.                                                                       |
|  10 | Libraries like QuickMacHotkey and QuickMacApp facilitate global hotkey registration and status bar integration on macOS, while NotifyPy enables cross-platform native notifications.                                 |
|  11 | Geolocation APIs are accessible in Python via platform-specific wrappers, such as PyObjC for macOS Core Location and WinRT bindings for Windows.                                                                     |
|  12 | The barrier to entry for desktop development in Python is low, requiring only standard imports or pip installs rather than learning new languages or complex toolchains.                                             |
|  13 | Maintaining up-to-date documentation and community engagement is crucial for the health of desktop Python libraries, as outdated resources create high friction for new users.                                       |
|  14 | Python developers should leverage local machine capabilities for development and automation to regain control over their computing environment and reduce dependency on cloud infrastructure.                        |

# Video

[![Video thumbnail](https://img.youtube.com/vi/ucWdfZoxsYo/hqdefault.jpg)](https://www.youtube.com/watch?v=ucWdfZoxsYo)

[Watch on YouTube](https://www.youtube.com/watch?v=ucWdfZoxsYo)
