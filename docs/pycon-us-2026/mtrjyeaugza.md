---
layout: default
title: "Python and the JVM - A Love Story - Shir Havron"
nav_order: 30
parent: PyCon US 2026
type: Video Note
description: "This presentation by Sheir, a Python tech lead at Hunters, explores the integration of Python and the Java Virtual Machine (JVM) using the Py4J library to combine Python’s readability with the JVM’..."
resource: "https://www.youtube.com/watch?v=mtRjYEAuGZA"
youtube_stats:
  view_count: 177
  like_count: 3
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

This presentation by Sheir, a Python tech lead at Hunters, explores the integration of Python and the Java Virtual Machine (JVM) using the Py4J library to combine Python’s readability with the JVM’s superior performance.
The speaker explains that while Python is favored for its simplicity and broad accessibility, JVM-based languages like Scala offer up to ten times faster execution speeds, which is critical for data-intensive frameworks like Apache Spark.
Py4J facilitates this interoperability by establishing a gateway server on the JVM side and a corresponding client on the Python side, allowing Python code to access JVM objects and class paths as if they were native Python references.
This mechanism relies on passing object references rather than data values, utilizing socket-based RPC and custom serialization to maintain high performance without becoming a bottleneck.
A real-world application discussed involves using Py4J to expose a Scala-based Spark job as a simple, complete object to Python developers, enabling them to build a FastAPI interface for on-demand data simulation without needing to understand complex Scala internals.
The talk concludes by distinguishing Py4J from Jython, noting that it keeps both languages pure and separate, and clarifies its relationship with PySpark, which is built upon similar architectural principles to separate client and server components for scalable data processing.

# Main Points

|   # | Main point |
| --: | ---------- |
|   1 | The speaker, a Python tech lead at Hunters, presents a method to bridge Python and the JVM using the Py4J package. |
|   2 | Python is valued for its readability and ease of use, while the JVM offers superior performance, potentially up to 10 times faster for certain tasks. |
|   3 | The JVM supports multiple languages including Java, Scala, and Kotlin, with Scala being the primary language for Apache Spark. |
|   4 | Py4J enables communication between Python and the JVM by treating all objects as references rather than passing data directly. |
|   5 | On the JVM side, a gateway server is initialized to allow Python to access the JVM classpath. |
|   6 | The classpath functions similarly to Python's global namespace, organizing classes and objects for runtime access. |
|   7 | Direct access to JVM objects in Python can be cumbersome, so the `jvm.import` function allows importing specific references into the Python namespace. |
|   8 | A gateway object can be passed from the JVM to Python to provide a direct, simplified entry point to specific application objects. |
|   9 | Py4J operates locally using socket-based RPC with custom serialization to maintain performance and avoid bottlenecks. |
|  10 | A real-world application at Hunters uses Py4J to run on-demand Spark jobs via a REST API for data simulation. |
|  11 | This approach allows Python teams to interact with Scala-based Spark infrastructure without requiring deep JVM expertise. |
|  12 | The design principle is to expose a complete, simple object from the JVM that encapsulates business logic, minimizing complexity on the Python side. |
|  13 | Developers should import trivial JVM references into Python but leave confusing or name-colliding references as direct gateway calls. |
|  14 | Py4J supports remote server configurations, allowing Python clients to run locally while heavy processing occurs on powerful cloud servers. |
|  15 | Unlike Jython, which compiles Python to run on the JVM, Py4J keeps Python and JVM as separate processes communicating via references. |
|  16 | PySpark is built upon Py4J, and its newer Spark Connect architecture follows a similar client-server separation model. |
|  17 | Scala classes on the JVM classpath are distinguished from Java classes by a trailing dollar sign in their bytecode references. |
|  18 | Accessing Scala modules from Python requires retrieving the internal `module` field to get the correct object reference. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/mtRjYEAuGZA/hqdefault.jpg)](https://www.youtube.com/watch?v=mtRjYEAuGZA)

[Watch on YouTube](https://www.youtube.com/watch?v=mtRjYEAuGZA)
