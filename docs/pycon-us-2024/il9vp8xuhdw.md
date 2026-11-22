---
layout: default
title: "Tutorials - Felipe, Amanda: 🌐 Building Your First API with Django and Django Rest Framework"
nav_order: 13
parent: PyCon US 2024
type: Video Note
description: "In this tutorial, Amanda and Felipe guide participants through building a music API using Django and Django REST Framework (DRF)."
resource: "https://www.youtube.com/watch?v=iL9vp8xuHDw"
youtube_stats:
  view_count: 1529
  like_count: 25
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

In this tutorial, Amanda and Felipe guide participants through building a music API using Django and Django REST Framework (DRF).
The session begins with an introduction to the instructors and their organization, AFR Python, followed by a live setup process where they address common issues such as cloning repositories, creating virtual environments, and resolving dependency conflicts for different Python versions.
The core of the workshop involves implementing a "Music" app by defining models for artists, albums, and songs, creating serializers to handle data translation, and configuring view sets and routers to expose CRUD endpoints.
The instructors demonstrate both high-level approaches using `ModelViewSet` and `HyperlinkedModelSerializer` for rapid development, and lower-level implementations using `ViewSet` and `Serializer` to provide deeper insight into DRF’s internal mechanics.
Throughout the session, they troubleshoot live errors related to migrations, URL configurations, and database connections, ensuring the audience understands how to debug and manage the application lifecycle.
The tutorial concludes with a review of the working API, a discussion on extending the project with custom validations and complex relationships, and recommendations for further study using the official DRF documentation.

# Main Points

|   # | Main point                                                                                                                                               |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The tutorial guides participants through building a music API using Django and Django REST Framework (DRF).                                              |
|   2 | The presenters are Amanda and Felipe, founders of AFR Python, a company focused on increasing Black representation in IT.                                |
|   3 | An API acts as an interface, similar to a waiter in a restaurant, facilitating communication between the client and the server.                          |
|   4 | Django models represent the data structure, with each model typically mapping to a single database table.                                                |
|   5 | Serializers are responsible for translating between JSON data and Python objects, enabling data validation and representation.                           |
|   6 | ViewSets define how to handle specific actions like list, create, retrieve, update, and destroy for API resources.                                       |
|   7 | Routers automatically generate URLs for ViewSets, simplifying the mapping between endpoints and views.                                                   |
|   8 | The tutorial uses a self-paced online resource accessible via a QR code or URL provided during the session.                                              |
|   9 | Participants must set up a Python virtual environment to isolate project dependencies from the global system.                                            |
|  10 | The project requires specific versions of Django and DRF, with adjustments needed for older Python versions like 3.9.                                    |
|  11 | The initial setup involves cloning the GitHub repository and installing dependencies using the requirements.txt file.                                    |
|  12 | A common issue encountered was the 'music' app already existing in the repository, requiring a switch to a specific branch or tag to start from scratch. |
|  13 | Creating a new Django app involves using the startapp command and registering it in the settings.py file.                                                |
|  14 | Models for Artist, Album, and Song are defined in models.py, establishing the core data structure for the API.                                           |
|  15 | Migrations are created using makemigrations to generate database schema changes and applied using migrate.                                               |
|  16 | The Artist endpoint is implemented first using ModelViewSet and HyperlinkedModelSerializer for simplicity.                                               |
|  17 | The Album endpoint demonstrates a more complex implementation using a plain ViewSet and Serializer to show manual handling of actions.                   |
|  18 | Nested serializers allow complex fields, such as an Artist object within an Album, to be represented in the API response.                                |
|  19 | The browsable API feature in DRF provides a web interface for testing and interacting with the API endpoints directly.                                   |
|  20 | Troubleshooting steps include checking import statements, verifying app registration in settings, and ensuring migrations are applied.                   |
|  21 | The tutorial emphasizes understanding the flow from URL to View to Serializer to Model to resolve common development errors.                             |
|  22 | Participants are encouraged to consult the official DRF documentation for advanced topics like custom routers and validators.                            |

# Video

[![Video thumbnail](https://img.youtube.com/vi/iL9vp8xuHDw/hqdefault.jpg)](https://www.youtube.com/watch?v=iL9vp8xuHDw)

[Watch on YouTube](https://www.youtube.com/watch?v=iL9vp8xuHDw)
