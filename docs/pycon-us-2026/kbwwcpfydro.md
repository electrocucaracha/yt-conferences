---
layout: default
title: "Understanding Python's logging Combine components like Lego blocks - nikkie"
nav_order: 129
parent: PyCon US 2026
type: Video Note
description: "This presentation explains Python’s standard library logging module by comparing its components—loggers, handlers, formatters, and filters—to simple LEGO blocks that can be combined to build comple..."
resource: "https://www.youtube.com/watch?v=KbwwcPFyDRo"
youtube_stats:
  view_count: 819
  like_count: 4
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

This presentation explains Python’s standard library logging module by comparing its components—loggers, handlers, formatters, and filters—to simple LEGO blocks that can be combined to build complex logging systems.
The speaker emphasizes that understanding the concepts of "not set" logger levels and propagation allows developers to centralize logging configuration at the root logger, enabling library users to control output destinations and formats without modifying library code.
A key best practice highlighted is that library authors should only use loggers to record events and must avoid calling `logging.basicConfig` or directly configuring the root logger, as this prevents users from customizing their own logging setup.
The talk also addresses common pitfalls, such as using `print` instead of loggers or libraries inadvertently overriding root logger configurations, and introduces alternative tools like Loguru and structlog for those seeking different logging paradigms.
Ultimately, the goal is to empower developers to use Python’s logging module with confidence by leveraging its compositional simplicity and ensuring that logging remains flexible and user-controlled.

# Main Points

|   # | Main point                                                                                                                |
| --: | ------------------------------------------------------------------------------------------------------------------------- |
|   1 | Python's logging module components function like LEGO blocks, allowing simple pieces to be combined into complex systems. |
|   2 | The four core components are loggers, handlers, formatters, and filters.                                                  |
|   3 | Library authors use loggers to record events with specific levels and messages, while users configure visibility.         |
|   4 | Loggers have five standard levels: debug, info, warning, error, and critical.                                             |
|   5 | A logger records messages whose severity is at or above its own level, ignoring lower severity messages.                  |
|   6 | Handlers dispatch log records to destinations such as streams or files.                                                   |
|   7 | Formatters apply a specific format to log records before output.                                                          |
|   8 | Filters can be attached to loggers or handlers to restrict which records pass through.                                    |
|   9 | New loggers are created with a level of "not set" by default.                                                             |
|  10 | If a logger's level is not set, the system traverses ancestor loggers to find an effective level.                         |
|  11 | Logger names create a hierarchy where dot-separated names define parent-child relationships.                              |
|  12 | All loggers ultimately descend from the root logger, which has a default level of warning.                                |
|  13 | Changing the root logger's level changes the effective level of descendant loggers with "not set" levels.                 |
|  14 | Loggers have a propagate attribute that is true by default.                                                               |
|  15 | When propagate is true, log records are passed to handlers of ancestor loggers.                                           |
|  16 | During propagation, the parent logger's level and filters are not checked.                                                |
|  17 | Attaching handlers to the root logger allows centralized logging for all descendant loggers.                              |
|  18 | Filters attached to root logger handlers can isolate logs from specific libraries.                                        |
|  19 | The root logger pattern allows users to control format and destination in one place.                                      |
|  20 | Multiple handlers can be attached to the root logger to route different levels to different destinations.                 |
|  21 | Formatters can be swapped to change output representation, such as converting logs to JSON.                               |
|  22 | Libraries should not use print for logging events, as print lacks level control and configurability.                      |
|  23 | Libraries must not call logging.basicConfig or touch the root logger directly.                                            |
|  24 | Calling logging.basicConfig in a library can prevent users from configuring logging later.                                |
|  25 | The force argument in basicConfig can override existing configurations but is not ideal for users.                        |
|  26 | A last resort handler outputs warning-level messages to the console if no other handlers are configured.                  |
|  27 | Attaching a null handler to a library's top-level logger prevents duplicate output from the last resort handler.          |
|  28 | DictConfig and fileConfig provide alternatives to code-based logging configuration.                                       |
|  29 | DictConfig accepts dictionaries from YAML, TOML, or JSON sources.                                                         |
|  30 | Loguru and structlog are alternative logging libraries with different configuration paradigms.                            |
|  31 | The happy-python-logging package provides a linter to detect basicConfig usage in libraries.                              |
|  32 | Library authors should limit themselves to calling loggers to record events.                                              |
|  33 | Library users should configure the final format and output destination.                                                   |
|  34 | Centralizing logging configuration at the root logger is a recommended best practice.                                     |

# Video

[![Video thumbnail](https://img.youtube.com/vi/KbwwcPFyDRo/hqdefault.jpg)](https://www.youtube.com/watch?v=KbwwcPFyDRo)

[Watch on YouTube](https://www.youtube.com/watch?v=KbwwcPFyDRo)
