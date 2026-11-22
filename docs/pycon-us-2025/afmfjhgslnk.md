---
layout: default
title: "Evolving Django: What We Learned by Integrating MongoDB (Sponsor: MongoDB)"
nav_order: 66
parent: PyCon US 2025
type: Video Note
description: "Annayia Ray Singani, a developer advocate at MongoDB, presents the new official Django MongoDB backend library, a fully supported integration that allows developers to use Django’s Object-Relationa..."
resource: "https://www.youtube.com/watch?v=AfmfJhgSlnk"
youtube_stats:
  view_count: 591
  like_count: 14
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

Annayia Ray Singani, a developer advocate at MongoDB, presents the new official Django MongoDB backend library, a fully supported integration that allows developers to use Django’s Object-Relational Mapper (ORM) with MongoDB’s flexible document-based database.
The library addresses the limitations of previous third-party solutions, which often relied on hacky SQL-to-NoSQL translations or sidecar patterns, by providing a native backend that supports Django models, forms, authentication, and the admin panel while preserving the scalability and schema flexibility of MongoDB.
The presentation highlights key technical achievements, including comprehensive testing against Django’s test suite, efficient query generation using MongoDB’s aggregation pipeline, and custom field implementations that bridge relational and document data structures.
Singani demonstrates the library’s capabilities through a live demo of a Dublin pub finder application, showcasing features like Atlas Search with fuzzy matching and vector search integration using Voyage AI and LangChain for advanced semantic queries.
With the package currently in public preview, MongoDB outlines a roadmap for General Availability later this year, promising additional features such as programmatic management of vector search, geospatial indices, and database transactions, while inviting the community to provide feedback and contribute to the project’s development.

# Main Points

|   # | Main point                                                                                                                                                    |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker introduced a new official MongoDB backend library for Django, announced for public preview in February.                                           |
|   2 | A demo application called Dublin City Center Pubfinder was built to showcase the integration, allowing users to search for pubs based on specific queries.    |
|   3 | MongoDB is described as a NoSQL document-based database that stores flexible JSON-like documents, enabling horizontal scaling without costly join operations. |
|   4 | Django is an open-source web framework designed for relational databases, but the new library allows it to use MongoDB as a backend.                          |
|   5 | Historical attempts to integrate Django and MongoDB failed due to maintenance issues, poor performance, and hacky SQL-to-MongoDB query translations.          |
|   6 | The new library was developed using code from the Django nonrel project as a starting point to support Django models and query sets.                          |
|   7 | MongoDB usage among Django developers grew from 0% in 2021 to 8% in 2023, driving the motivation for this official integration.                               |
|   8 | The library supports Django models, forms, validation, authentication, and the Django admin panel with full migration support.                                |
|   9 | Configuration is simplified by installing the package via pip and using provided starter templates that handle settings and primary key types.                |
|  10 | The integration replaces traditional SQL joins with MongoDB aggregation stages and dollar lookup operators for better performance.                            |
|  11 | Developers can use raw aggregation pipelines and MongoDB-specific query optimizations within the Django framework.                                            |
|  12 | The library supports AI applications by integrating with frameworks like LangChain and LlamaIndex for vector search and semantic search.                      |
|  13 | A demo showed how Atlas Search with fuzzy matching allows users to find results even with misspelled search terms.                                            |
|  14 | Future features planned for General Availability include vector search management, queryable encryption, and database transactions.                           |
|  15 | The acquisition of Voyage AI enables native embedding models and multimodal retrieval directly within the MongoDB database layer.                             |
|  16 | The Dublin Pubfinder project used Google Places API data, Voyage AI for embeddings, and LangChain for semantic search workflows.                              |
|  17 | Creating an Atlas vector search index is required for vector search, involving specifying the embedding path and dimensions.                                  |
|  18 | The speaker encouraged the community to test the library, provide feedback, and submit pull requests to help shape its development.                           |
|  19 | Resources, including a full tutorial and code repository, are available on the speaker's Dev.to account and GitHub.                                           |

# Video

[![Video thumbnail](https://img.youtube.com/vi/AfmfJhgSlnk/hqdefault.jpg)](https://www.youtube.com/watch?v=AfmfJhgSlnk)

[Watch on YouTube](https://www.youtube.com/watch?v=AfmfJhgSlnk)
