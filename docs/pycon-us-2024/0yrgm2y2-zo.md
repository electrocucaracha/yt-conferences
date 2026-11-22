---
layout: default
title: "Tutorials - Aya Elsayed, Rhythm Patel: No More Raw SQL: SQLAlchemy, ORMs & asyncio"
nav_order: 25
parent: PyCon US 2024
type: Video Note
description: "This hands-on tutorial, presented by an engineer from Bloomberg, demonstrates how to use SQLAlchemy to simplify, secure, and optimize database interactions in Python services."
resource: "https://www.youtube.com/watch?v=0YrGM2y2-Zo"
youtube_stats:
  view_count: 2421
  like_count: 43
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

This hands-on tutorial, presented by an engineer from Bloomberg, demonstrates how to use SQLAlchemy to simplify, secure, and optimize database interactions in Python services.
The session begins by refactoring a synchronous FastAPI microservice that initially uses raw SQL queries with the `sqlite3` library.
The presenter guides the audience through creating an engine, managing connections with context managers, and implementing parameter binding to prevent SQL injection.
The tutorial then progresses to using SQLAlchemy’s Object-Relational Mapping (ORM) and SQL expression language to replace raw strings with readable, object-oriented code, covering key concepts such as defining ORM classes, managing relationships, and applying optimization techniques like lazy loading and hybrid properties to address performance issues like the N+1 problem.
The second half of the workshop focuses on adapting these practices for asynchronous services using `asyncio`.
The presenter explains the fundamentals of cooperative multitasking and demonstrates how to use `async def`, `await`, and task groups to handle I/O-bound operations efficiently.
The code is updated to use SQLAlchemy’s asynchronous engine and session makers, ensuring that database connections, queries, and commits are properly awaited to yield control to the event loop.
By the end of the session, the service utilizes asynchronous ORM patterns, including `AsyncSession` and `awaitable` attribute access, to achieve a robust, high-performance, and Pythonic database layer.

# Main Points

|   # | Main point                                                                                                                                    |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker is from Bloomberg and will present a hands-on tutorial on using SQLAlchemy to make Python code more readable and maintainable.    |
|   2 | The tutorial covers both synchronous and asynchronous services, utilizing SQLite for the database to minimize network load.                   |
|   3 | SQLAlchemy consists of a core layer for connection pooling and SQL expression language, and an ORM layer for object-relational mapping.       |
|   4 | The example service is a FastAPI microservice managing a marketplace with customers, orders, and items, initially using raw SQL queries.      |
|   5 | Participants are instructed to fork the repository and use GitHub Codespaces or a local environment with a Python virtual environment.        |
|   6 | The core layer engine is created using `create_engine` with the SQLite dialect and a specific DB API, enabling connection management.         |
|   7 | Connections are managed using context managers (`with` blocks) to ensure proper cleanup and closure after query execution.                    |
|   8 | The `connection.execute` method returns a result object that behaves like a namedtuple, allowing access to row data by column name.           |
|   9 | Parameter binding is emphasized to prevent SQL injection attacks, using dictionaries for key-value pairs in raw SQL queries.                  |
|  10 | Two commitment styles are introduced: "commit as you go" for individual transactions and "begin once" for batching multiple operations.       |
|  11 | The ORM layer involves creating classes that map to database tables, inheriting from a declarative base to define columns and relationships.  |
|  12 | Relationships between tables, such as one-to-one and one-to-many, are defined using the `relationship` construct to enable object navigation. |
|  13 | The SQL expression language replaces raw SQL strings with Pythonic constructs like `select` and `where` clauses for better readability.       |
|  14 | Optimization techniques include choosing between eager and lazy loading to avoid the N+1 query problem based on access patterns.              |
|  15 | Hybrid properties and expressions allow defining reusable SQL logic within ORM classes to simplify complex calculations.                      |
|  16 | Asynchronous programming in Python uses cooperative multitasking via `async def` and `await` to handle I/O-bound tasks efficiently.           |
|  17 | Asyncio.gather` and task groups are used to schedule multiple coroutines concurrently, improving performance over sequential awaiting.        |
|  18 | Asynchronous generators allow yielding results one at a time, enabling other tasks to run while waiting for I/O operations.                   |
|  19 | The asynchronous version of SQLAlchemy uses `create_async_engine` with an async DB API like `aiosqlite`.                                      |
|  20 | Async sessions are created using `async_sessionmaker` and managed with `async with` statements to handle connections properly.                |
|  21 | In async ORM usage, the `AsyncAttrs` mixin is added to the base class to allow awaiting lazy loaded attributes.                               |
|  22 | Specific operations like `session.execute` and `session.commit` must be awaited in async code, while `session.add` does not require it.       |

# Video

[![Video thumbnail](https://img.youtube.com/vi/0YrGM2y2-Zo/hqdefault.jpg)](https://www.youtube.com/watch?v=0YrGM2y2-Zo)

[Watch on YouTube](https://www.youtube.com/watch?v=0YrGM2y2-Zo)
