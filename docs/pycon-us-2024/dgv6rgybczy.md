---
layout: default
title: "Talks - Mia Bajić: Combining Django ORM & FastAPI in a Single App"
nav_order: 204
parent: PyCon US 2024
type: Video Note
description: "Mia, a software engineer based in Prague, presents a technical session on the unconventional integration of Django ORM and FastAPI within a single application."
resource: "https://www.youtube.com/watch?v=dgV6RgybczY"
youtube_stats:
  view_count: 750
  like_count: 17
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

Mia, a software engineer based in Prague, presents a technical session on the unconventional integration of Django ORM and FastAPI within a single application.
She contrasts the two frameworks, noting that while Django offers a rich ecosystem, an admin panel, and ease of use for CRUD applications, FastAPI provides superior performance through asynchronous capabilities, automatic documentation, and dependency injection.
The talk highlights the significant challenges of this hybrid setup, including the complexity of managing mixed synchronous and asynchronous code, frequent runtime exceptions, and the lack of compatible third-party tools or online resources for troubleshooting.
Mia demonstrates the implementation process, covering configuration, endpoint creation using `sync_to_async` decorators, and testing strategies, while recommending a module-based project structure for maintainability.
Ultimately, she advises that while this combination is viable for specific legacy or migration scenarios, developers starting new projects should consider Django Ninja, pure Django, or FastAPI with SQLAlchemy to avoid the inherent friction of mixing these distinct technologies.

# Main Points

|   # | Main point                                                                                                                              |
| --: | --------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The session explores combining Django ORM and FastAPI in a single application, highlighting advantages, struggles, and lessons learned. |
|   2 | Django ORM is preferred over SQLAlchemy for its high-level abstraction, easier session management, and simpler migrations.              |
|   3 | Django offers a rich ecosystem with over 10,000 packages, a built-in admin panel, and strong community support.                         |
|   4 | FastAPI provides superior performance through asynchronous capabilities and automatically generates interactive OpenAPI documentation.  |
|   5 | FastAPI’s dependency injection feature simplifies testing by allowing easy mocking of external services.                                |
|   6 | FastAPI is noted for its simplicity and lack of "magic," making troubleshooting easier compared to Django.                              |
|   7 | Mixing synchronous Django code with asynchronous FastAPI code frequently causes runtime exceptions and adds complexity.                 |
|   8 | Django’s asynchronous support is still ongoing, with features like async transactions not yet fully implemented.                        |
|   9 | Many Django ecosystem tools, such as pytest-django, do not work out of the box with FastAPI due to different test clients.              |
|  10 | Limited online resources and examples exist for this specific combination, requiring developers to experiment independently.            |
|  11 | Initial setup requires configuring Django settings separately and launching the application before integrating FastAPI.                 |
|  12 | Deployment typically involves using Docker and Uvicorn to serve the FastAPI application.                                                |
|  13 | Database calls in FastAPI routes often require the sync_to_async decorator unless using Django versions above 4.2.                      |
|  14 | Testing involves setting up Django migrations and fixtures to manage database state for each test run.                                  |
|  15 | A module-based project structure is recommended for predictability and extensibility in larger projects.                                |
|  16 | For new projects, Django Ninja is suggested as it bridges Django and FastAPI features with asynchronous capabilities.                   |
|  17 | FastAPI is ideal for performance-critical applications, while Django is better for standard CRUD apps needing out-of-the-box tools.     |
|  18 | Dependency conflicts are rare because the frameworks operate in separate layers, but connection management requires custom decorators.  |
|  19 | Unconventional setups like this require significant tweaking to resolve issues that standard configurations handle automatically.       |

# Video

[![Video thumbnail](https://img.youtube.com/vi/dgV6RgybczY/hqdefault.jpg)](https://www.youtube.com/watch?v=dgV6RgybczY)

[Watch on YouTube](https://www.youtube.com/watch?v=dgV6RgybczY)
