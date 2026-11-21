---
layout: default
title: "Debugging Python in Production: Practical Techniques Beyond Print Statements - Anshul Jannumahanti"
nav_order: 69
parent: PyCon US 2026
type: Video Note
description: "Anshul Jain Manti, a computer science student, presents a talk on debugging Python in production environments, arguing that simple print statements are insufficient for complex systems involving mu..."
resource: "https://www.youtube.com/watch?v=vXCQvD04gTE"
youtube_stats:
  view_count: 435
  like_count: 11
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

Anshul Jain Manti, a computer science student, presents a talk on debugging Python in production environments, arguing that simple print statements are insufficient for complex systems involving multiple users and servers.
He introduces modern debugging techniques, starting with logging, which acts as a digital diary to record timestamps, severity levels, and user IDs for optimized error tracking.
The presentation further explains how tracebacks and exceptions help identify the exact location and cause of crashes by displaying the sequence of function calls, while monitoring systems continuously track system health metrics like CPU and memory usage to alert engineers before failures occur.
Additionally, Manti discusses tracing, which allows engineers to follow requests across distributed services to pinpoint specific bottlenecks, and defines observability as the comprehensive understanding of these systems to investigate failures and detect unusual behaviors.
The session concludes with a Q&A where Manti addresses practical challenges, such as debugging memory leaks in production by clearing unused resources and the importance of logging every function call to facilitate effective traceback analysis.

# Main Points

|   # | Main point                                                                                                                                                  |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker, Anshul Jain Manti, is a computer science student interested in software engineering, Python, and backend systems.                              |
|   2 | The presentation focuses on debugging Python in production using practical techniques beyond simple print statements.                                       |
|   3 | Print statements are effective for small projects with single developers and small codebases but are insufficient for production systems.                   |
|   4 | Production systems involve multiple users, servers, and real money, making reliable debugging critical to prevent failures.                                 |
|   5 | Modern production debugging relies on a system comprising logging, tracking, tracing, and monitoring.                                                       |
|   6 | Logging acts as a digital diary that records important events, errors, application IDs, user IDs, and request IDs.                                          |
|   7 | Logs provide optimized output by saving time and displaying timestamps, severity levels, and server information.                                            |
|   8 | Tracebacks show the sequence of function calls leading to an error, identifying the exact location and cause of the crash.                                  |
|   9 | Exceptions are errors during execution that stop code execution, and handling them prevents program crashes and provides meaningful error messages.         |
|  10 | Common built-in Python exceptions include ZeroDivisionError, FileNotFoundError, TypeError, ValueError, IndexError, KeyError, and NameError.                 |
|  11 | Monitoring systems continuously track the health and performance of applications, such as CPU usage, memory usage, and server health.                       |
|  12 | Engineers use monitoring data to restart overloaded services, scale servers, roll back bad deployments, or optimize database queries.                       |
|  13 | Prometheus is a monitoring and alerting toolkit, while Grafana is an open-source web application that visualizes data through graphs.                       |
|  14 | Sentry is another popular tool mentioned for monitoring and error tracking.                                                                                 |
|  15 | Tracing helps engineers follow requests step-by-step through an application to identify where errors or slowdowns occur.                                    |
|  16 | In distributed systems, tracing is used at the application level to debug individual services, unlike tracebacks which operate at the code level.           |
|  17 | Observability is the understanding of system states that helps engineers investigate failures, understand performance issues, and detect unusual behaviors. |
|  18 | A typical debugging workflow involves monitoring alerts, checking logs, analyzing tracebacks, and using tracing to fix and redeploy services.               |
|  19 | When facing sudden memory spikes in production, engineers may need to clear unused resources to address potential memory leaks.                             |
|  20 | Effective traceback analysis requires logging every function call to capture detailed execution data for investigation.                                     |

# Video

[![Video thumbnail](https://img.youtube.com/vi/vXCQvD04gTE/hqdefault.jpg)](https://www.youtube.com/watch?v=vXCQvD04gTE)

[Watch on YouTube](https://www.youtube.com/watch?v=vXCQvD04gTE)
