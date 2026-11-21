---
layout: default
title: "Using Python Biopharm to Help Cure Cancer - Sushant Singh"
nav_order: 24
parent: PyCon US 2026
type: Video Note
description: "Sushant Singh presents a framework for transforming disparate data in complex domains like cancer research and algorithmic trading into actionable insights using FastAPI, Neo4j, and AI."
resource: "https://www.youtube.com/watch?v=iZUIaGjzFTs"
youtube_stats:
  view_count: 189
  like_count: 2
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

Sushant Singh presents a framework for transforming disparate data in complex domains like cancer research and algorithmic trading into actionable insights using FastAPI, Neo4j, and AI.
He argues that the primary challenge is not just data collection but contextualization, emphasizing that teams must ingest only the data they need to avoid creating unmanageable "data swamps" or spaghetti code.
The proposed solution involves a three-phase approach: capturing structured and unstructured data, contextualizing it through domain-driven design and event storming workshops to build a robust knowledge graph, and finally enabling collaboration via low-latency APIs and conversational interfaces.
By leveraging Neo4j’s semantic property graph and Pydantic for strict schema validation, the system ensures consistent, reliable data delivery that bridges the gap between technical infrastructure and scientific or business users.
Singh demonstrates how this architecture supports an AI-driven chatbot that allows users to query production data in natural language, significantly reducing the time spent on manual reporting and enabling scientists to focus on high-impact research rather than data retrieval.

# Main Points

|   # | Main point                                                                                                                                               |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker, Sushant, emphasizes that data often contains answers to unknown questions, particularly in cancer research and algorithmic trading.         |
|   2 | The presentation focuses on using FastAPI by Gantec and Neo4j to connect disparate data sources.                                                         |
|   3 | Users range from those wanting simple PDF downloads to scientists building machine learning models in Jupyter notebooks.                                 |
|   4 | A key lesson is the failure of isolated conceptual data models that do not integrate with business needs or solve real problems.                         |
|   5 | The workflow is divided into three phases: capture, contextualization, and collaboration.                                                                |
|   6 | Data capture must handle structured internal databases, feed files, external data graphs, and unstructured data like PDFs and handwritten notes.         |
|   7 | Scalability is critical, and systems should not attempt to reinvent the data lake but rather build a "fishing rod" for specific use cases.               |
|   8 | Contextualizing data is the primary goal, requiring the ingestion of necessary data rather than all available data.                                      |
|   9 | Event storming is recommended as a physical, in-person activity using sticky notes to map business processes and domain models.                          |
|  10 | Passion for the domain, such as curing orphan diseases or understanding trading strategies, is essential for developers to succeed in contextualization. |
|  11 | Solid principles and old-school patterns help create pure, strong, and consistent models that can be easily installed and used by others.                |
|  12 | Collaboration is powered by FastAPI's asynchronous performance and Pydantic's strict schema validation.                                                  |
|  13 | Knowledge graphs drive cross-functional collaboration by providing a centralized, consistent data model for all users.                                   |
|  14 | Ubiquitous language is crucial; for example, "API" means Active Pharmaceutical Ingredient in a lab context, not Application Programming Interface.       |
|  15 | The system must deliver low-latency, highly reliable data relevant to the user's specific world, such as linking formulations to indications.            |
|  16 | Conversational interfaces allow users to query scientific data using natural language, reducing the need for complex SQL or Cypher queries.              |
|  17 | NeoDash and similar tools enable zero-training adoption, allowing users to build dashboards and share insights intuitively.                              |
|  18 | A practical example shows scientists saving weeks of time by collaborating on shared dashboards instead of preparing PowerPoint presentations.           |
|  19 | An experimental AI chatbot was built using two AI calls: one to generate Cypher queries and another to process context and data.                         |
|  20 | Users began regression testing the system by asking questions they already knew the answers to, validating the reliability of the knowledge graph.       |
|  21 | The success of the chatbot led to users asking new, deep questions about animal studies and other complex topics.                                        |
|  22 | The speaker warns that applications relying on unstructured models without proper data curation will eventually collapse.                                |
|  23 | Teams should continue to evolve their technology stack, adapting to new tools like Dagster or Prefect for better performance.                            |
|  24 | Deep understanding of the domain is required to create good models, avoiding "parlor tricks" that lack foundational data integrity.                      |

# Video

[![Video thumbnail](https://img.youtube.com/vi/iZUIaGjzFTs/hqdefault.jpg)](https://www.youtube.com/watch?v=iZUIaGjzFTs)

[Watch on YouTube](https://www.youtube.com/watch?v=iZUIaGjzFTs)
