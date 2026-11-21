---
layout: default
title: "The Terminal is the New Browser: Building Rich TUIs with Textual - Andres Pineda"
nav_order: 40
parent: PyCon US 2026
type: Video Note
description: "Andre Benedetta presents a talk arguing that the terminal is evolving into a primary interface for modern development, offering superior performance and automation capabilities compared to resource..."
resource: "https://www.youtube.com/watch?v=xYRDhr8zv4I"
youtube_stats:
  view_count: 1714
  like_count: 23
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

Andre Benedetta presents a talk arguing that the terminal is evolving into a primary interface for modern development, offering superior performance and automation capabilities compared to resource-heavy browser-based tools.
He distinguishes between stateless Command Line Interfaces (CLIs) and stateful Terminal User Interfaces (TUIs), highlighting the Python ecosystem’s Rich and Textual libraries as key tools for building these applications.
While Rich enhances CLI output with colors and formatting, Textual serves as a comprehensive framework for creating full-featured, interactive applications with features like reactive state management, CSS-like styling, and built-in widgets.
The presentation demonstrates how Textual simplifies complex UI tasks, such as list virtualization and screen navigation, by providing a component-based architecture similar to React or Flutter.
Benedetta concludes that Textual enables developers to build accessible, cross-platform, and visually appealing terminal applications that can even be deployed remotely or as web applications, making the terminal a viable and efficient alternative to traditional graphical interfaces.

# Main Points

|   # | Main point                                                                                                                                                                          |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The terminal is evolving into a primary interface, replacing browser-based tools due to superior performance and reduced resource consumption.                                      |
|   2 | Context switching is considered expensive in computer science, making terminal-based workflows more efficient for developers and non-developers alike.                              |
|   3 | The terminal is the most automation-friendly UI, allowing users to instruct computers to perform tasks without memorizing complex command-line flags.                               |
|   4 | A distinction is made between CLI (Command Line Interface), which is stateless and executes single commands, and TUI (Terminal User Interface), which is stateful and event-driven. |
|   5 | The Python ecosystem offers libraries like Rich and Textual, both maintained by the same team, to build beautiful terminal applications.                                            |
|   6 | Rich is a library that enhances terminal output with colors, formatting, tables, and progress bars without adding significant complexity.                                           |
|   7 | Textual is a full framework for building TUIs, providing classes, services, widgets, and events to create feature-rich applications.                                                |
|   8 | Textual includes a CSS-like styling system that separates styling from logic, supporting selectors, IDs, and classes similar to web development.                                    |
|   9 | The framework is cross-platform, supports remote applications via SSH, and includes built-in accessibility features.                                                                |
|  10 | Textual's architecture is comparable to React or Flutter, utilizing widgets as fundamental building blocks and reactive attributes for data binding.                                |
|  11 | Reactive attributes allow variables to be bound to UI widgets, automatically updating the interface when the variable changes without manual refreshes.                             |
|  12 | The framework provides a screen-level API where the App manages the lifecycle, Screens represent individual pages, and Modals handle floating dialogs.                              |
|  13 | Built-in widgets include common UI elements like buttons, checkboxes, and list views, with the list view handling complex memory management and virtualization.                     |
|  14 | Events are triggered by user actions or application lifecycle changes and are handled using Python decorators to attach logic to specific interactions.                             |
|  15 | Textual supports complex layouts, multiple screen navigations, rich text, Markdown, and database integration for local or remote synchronization.                                   |
|  16 | The framework enables keyboard-first UX, composable widgets, and testable logic, making it suitable for professional application development.                                       |
|  17 | Textual applications can be deployed as web applications, expanding their reach beyond the traditional terminal environment.                                                        |

# Video

[![Video thumbnail](https://img.youtube.com/vi/xYRDhr8zv4I/hqdefault.jpg)](https://www.youtube.com/watch?v=xYRDhr8zv4I)

[Watch on YouTube](https://www.youtube.com/watch?v=xYRDhr8zv4I)
