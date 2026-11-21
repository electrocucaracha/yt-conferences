---
layout: default
title: "Thinking of Topic Modeling as Search - Kas Stohr"
nav_order: 70
parent: PyCon US 2026
type: Video Note
description: "The speaker from Unified, a social network for activists, presents a system for discovering trending conversations by leveraging semantic search and topic modeling."
resource: "https://www.youtube.com/watch?v=jtva4oiJ-lk"
youtube_stats:
  view_count: 151
  like_count: 5
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

The speaker from Unified, a social network for activists, presents a system for discovering trending conversations by leveraging semantic search and topic modeling.
Initially, the project aimed to build a real-time topic model to help users identify news-driven political discussions, utilizing Elasticsearch’s native support for dense vectors to store and query text embeddings.
The core pipeline involves preprocessing posts, converting them into embeddings, and using a topic model to generate representative topic embeddings that retrieve relevant posts via cosine similarity.
During evaluation, the speaker discovered that using the mean of all documents in a cluster to create a topic embedding resulted in poor precision, retrieving irrelevant posts because it captured the entire topic area rather than its core.
To resolve this, the approach was refined to use localized embeddings derived from semantically similar keywords, which significantly improved the relevance of search results.
Key lessons learned include the critical importance of rigorous preprocessing to remove noise like numbers and PII, the need to carefully define what the search embedding represents, and the utility of using dual time windows (long-term for stable topics and short-term for emergent trends) to effectively track evolving conversations.
The speaker concludes that semantic search offers a flexible and performant alternative to traditional tagging, encouraging creative applications of embeddings for information retrieval.

# Main Points

|   # | Main point                                                                                                                                                                                         |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker works at Unified, a social network for activists, and developed a real-time topic modeling system to help users discover trending conversations.                                       |
|   2 | The project leverages Elasticsearch, which natively stores dense vectors, allowing text embeddings to be used directly for semantic search and retrieval.                                          |
|   3 | Text embeddings are generated using a small sentence transformer model with 384 dimensions, mapping text to high-dimensional space where similar concepts are positioned closer together.          |
|   4 | The system pipeline involves pre-processing posts, converting them to embeddings, storing them in a vector database, and retrieving relevant posts using cosine similarity.                        |
|   5 | Initial evaluation revealed poor precision because using the mean of all topic documents for search queries captured too broad a range of unrelated content.                                       |
|   6 | A key improvement was creating localized search embeddings using only the most semantically similar keywords to the topic, which significantly improved the relevance of retrieved posts.          |
|   7 | Pre-processing is critical for accuracy; the team removed numbers, personally identifiable information, and short, low-information replies to reduce noise in the topic clusters.                  |
|   8 | Keyword selection for topic labeling was refined by comparing representative documents to the topic embedding rather than using TF-IDF, which surfaced rare and unrepresentative terms.            |
|   9 | To handle different types of trends, the system uses two models: a long-window model (180 days) for stable, evergreen topics and a short-window model (7 days) for emergent, breaking news topics. |
|  10 | Named entity recognition is used to structure unstructured text, allowing for hybrid search that combines semantic similarity with specific entity filters like location or organization.          |
|  11 | The topic model outputs are passed to a large language model with specific keywords and representative posts to generate human-readable labels for users.                                          |
|  12 | Tracking topics over time is achieved by storing generated topics from each run and measuring the cosine similarity between them to monitor changes and stability.                                 |
|  13 | The speaker recommends the Python package 'word topic' for conventional topic modeling, noting its strong documentation and evaluation tools.                                                      |
|  14 | Semantic search implementations are versatile and can be applied to other domains, such as comparing medical records or finding similar user-generated characters in games.                        |
|  15 | The final system allows users to search for custom topics by converting their search terms into embeddings and retrieving the most semantically similar posts from the vector store.               |

# Video

[![Video thumbnail](https://img.youtube.com/vi/jtva4oiJ-lk/hqdefault.jpg)](https://www.youtube.com/watch?v=jtva4oiJ-lk)

[Watch on YouTube](https://www.youtube.com/watch?v=jtva4oiJ-lk)
