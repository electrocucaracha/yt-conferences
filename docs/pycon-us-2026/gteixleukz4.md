---
layout: default
title: "Dungeons & Databases Build NPC agents to work with data in DocumentDB & Postgres (Sponsor:Microsoft)"
nav_order: 119
parent: PyCon US 2026
type: Video Note
description: "At PyCon US 2026, Marco and Patty presented a Microsoft-sponsored session on building AI agents using the Dungeons and Dragons metaphor to illustrate stateful, event-driven systems."
resource: "https://www.youtube.com/watch?v=gtEIxleukZ4"
youtube_stats:
  view_count: 365
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

At PyCon US 2026, Marco and Patty presented a Microsoft-sponsored session on building AI agents using the Dungeons and Dragons metaphor to illustrate stateful, event-driven systems.
They explained how non-player characters (NPCs) in the game parallel AI agents that require memory, context, and adaptive responses, highlighting the critical role of databases as memory systems for these applications.
The speakers detailed the Microsoft AI stack for Python developers, emphasizing the use of open-source databases like PostgreSQL and DocumentDB to support vector search, hybrid search, and semantic retrieval.
Patty demonstrated a local Python application where NPCs interact with users, utilizing DocumentDB to store character profiles, conversation history, and spell embeddings for accurate vector-based recommendations.
The session concluded by clarifying that DocumentDB is a fully open-source, MongoDB-compatible database that allows developers to store both relational and non-relational data, including vectors, in a single engine, offering a flexible alternative to traditional JSON extensions in PostgreSQL.

# Main Points

|   # | Main point                                                                                                                                                                                                           |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The session at PyCon US 2026 explores building NPC agents using DocumentDB and PostgreSQL, drawing parallels between Dungeons and Dragons mechanics and stateful, event-driven AI applications.                      |
|   2 | Dungeons and Dragons serves as a metaphor for AI agent architecture, where the Dungeon Master acts as an orchestrator applying business logic, and NPCs function as agents with memory, context, and specific roles. |
|   3 | Modern AI applications are complex to navigate due to rapidly evolving frameworks, prompting Microsoft to provide clarity through tools like Visual Studio Code, GitHub Copilot, and the Microsoft Agent Framework.  |
|   4 | Databases are evolving into memory systems for AI agents, supporting vector search, hybrid search, and semantic ranking to ground truth and maintain state across multi-agent interactions.                          |
|   5 | Microsoft offers several AI-optimized database options on Azure, including Azure Cosmos DB, Azure Database for PostgreSQL, Azure SQL Database, and Azure DocumentDB.                                                 |
|   6 | Open source is a core Microsoft strategy, allowing developers to build and deploy applications anywhere without vendor lock-in, supported by contributions to projects like PostgreSQL and DocumentDB.               |
|   7 | PostgreSQL is highlighted for its extensibility, supporting relational, JSON, spatial, and graph data, with Microsoft employing dedicated engineers to contribute to its open-source codebase.                       |
|   8 | DocumentDB is a fully open-source, MIT-licensed document database that is 100% compatible with the MongoDB API, enabling developers to use existing MongoDB skills without licensing fees.                           |
|   9 | DocumentDB is implemented as a PostgreSQL extension, allowing it to store BSON documents, vectors, and JSON data in a single engine while supporting the MongoDB wire protocol.                                      |
|  10 | Python developers can interact with DocumentDB using drivers like PyMongo and Motor, or ORMs like Beanie, facilitating seamless integration with frameworks such as FastAPI.                                         |
|  11 | A live demo showcased a Dungeons and Dragons-themed application where NPCs like a tavern keeper and a spell wizard retrieve data and maintain conversation memory using DocumentDB.                                  |
|  12 | The demo utilized vector search to accurately recommend spells based on semantic similarity, demonstrating how DocumentDB handles embeddings and retrieval for AI agents.                                            |
|  13 | DocumentDB supports storing both operational data and vector embeddings in one place, eliminating the need for separate vector databases like Pinecone in many scenarios.                                            |
|  14 | The project is supported by a growing ecosystem including AWS and Google Cloud, with deployment options via Kubernetes for production-scale high availability.                                                       |
|  15 | While the open-source version of DocumentDB does not yet support sharding, managed services like Azure DocumentDB provide enterprise features such as high availability and data replication.                        |
|  16 | Developers are encouraged to choose between PostgreSQL for relational integrity or DocumentDB for schema flexibility, depending on their application requirements and existing skills.                               |
|  17 | The Microsoft team at the expo offers interactive labs, demos, and resources for exploring GitHub Copilot, Azure AI Search, and other AI-ready database technologies.                                                |

# Video

[![Video thumbnail](https://img.youtube.com/vi/gtEIxleukZ4/hqdefault.jpg)](https://www.youtube.com/watch?v=gtEIxleukZ4)

[Watch on YouTube](https://www.youtube.com/watch?v=gtEIxleukZ4)
