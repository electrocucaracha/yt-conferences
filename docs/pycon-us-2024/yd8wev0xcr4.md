---
layout: default
title: "Talks - Tuana Celik: Everything is a graph, including LLM Applications (and that’s handy)"
nav_order: 206
parent: PyCon US 2024
type: Video Note
description: "Tuana Chik, from Deepset, presents a framework for building AI applications by conceptualizing workflows as graphs, arguing that this approach is essential for managing the complexity of modern LLM..."
resource: "https://www.youtube.com/watch?v=Yd8weV0xCr4"
youtube_stats:
  view_count: 590
  like_count: 11
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

Tuana Chik, from Deepset, presents a framework for building AI applications by conceptualizing workflows as graphs, arguing that this approach is essential for managing the complexity of modern LLM interactions.
She explains that while large language models are versatile, effective applications like Retrieval-Augmented Generation (RAG) require distinct steps for retrieval and generation, which can be modeled as nodes in a graph that pass data to one another.
The talk introduces the Haystack framework, which allows developers to create pipelines using modular components that handle specific tasks, such as embedding, classification, or prompt building, and supports advanced features like branching and cyclic loops for agentic behaviors.
Chik demonstrates this by building several live examples, including a web-based QA pipeline, a Hacker News summarizer, and a Notion QA system, highlighting how custom components can be easily integrated to solve specific use cases.
She further illustrates the power of cyclic graphs by showing how pipelines can validate structured outputs against schemas and retry generation upon failure, ultimately encouraging developers to build custom, efficient AI workflows rather than relying solely on monolithic LLM calls.

# Main Points

|   # | Main point                                                                                                                                                                                                         |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | The speaker, Tuana Chik from Deepset, presents the concept that AI applications, including LLMs, can be effectively modeled as graphs.                                                                             |
|   2 | A significant shift occurred in 2022 with the rise of performant Large Language Models, allowing models to act as chameleons that perform various tasks like summarization or translation via simple instructions. |
|   3 | Retrieval Augmented Generation (RAG) involves two main steps: retrieving relevant information from a database and generating a response using that information to augment the prompt.                              |
|   4 | Embedding data represents it in vector form, which is useful for semantic search and comparing the similarity of text vectors.                                                                                     |
|   5 | Building AI pipelines involves small, sequential tasks such as cleaning, splitting, and embedding data, which naturally form a graph structure.                                                                    |
|   6 | Graphs allow for branching, enabling different preprocessing steps for various file types like text and PDFs before writing them to a database.                                                                    |
|   7 | Haystack, an open-source AI framework, was released in 2020 with a focus on retrieval and semantic search, evolving to support cyclic pipelines in version 2.0.                                                    |
|   8 | Cyclic pipelines allow for agentic behavior where an LLM component decides which branch of the graph to invoke based on the incoming task.                                                                         |
|   9 | In Haystack, pipelines consist of components, each responsible for a specific task and forwarding results to the next component.                                                                                   |
|  10 | Custom components can be created by defining a class with a component decorator and a run method that accepts inputs and returns a dictionary of results.                                                          |
|  11 | Components must have matching input and output types to ensure valid connections within the pipeline graph.                                                                                                        |
|  12 | The speaker demonstrates building a web QA pipeline using components for fetching content, converting formats, building prompts, and generating responses.                                                         |
|  13 | Haystack provides error handling for pipeline connections, identifying type mismatches between components to help users fix graph structures.                                                                      |
|  14 | A Hacker News summary pipeline was built using a custom fetcher component and Streamlit for the user interface, allowing users to select the number of articles to summarize.                                      |
|  15 | A Notion QA pipeline was created by converting a community-contributed extractor for Haystack 1.x into a component compatible with Haystack 2.0.                                                                   |
|  16 | Looping pipelines are effective for generating structured outputs, where an LLM retries generation until it satisfies a specific schema, such as a Pydantic model.                                                 |
|  17 | An auto-quiz application was demonstrated where separate graphs work together to generate quizzes from web pages and then answer them using either internal knowledge or retrieval augmentation.                   |
|  18 | The speaker emphasizes that not every task requires an LLM; simpler tasks like classification or translation should be offloaded to specific components to improve efficiency.                                     |
|  19 | Users are encouraged to build custom components for unique use cases, as the framework is designed to be extensible rather than a finished product.                                                                |
|  20 | Progress tracking in pipelines is handled by outputting the number of processed documents and providing progress bars, with options to wrap components for custom behavior.                                        |

# Video

[![Video thumbnail](https://img.youtube.com/vi/Yd8weV0xCr4/hqdefault.jpg)](https://www.youtube.com/watch?v=Yd8weV0xCr4)

[Watch on YouTube](https://www.youtube.com/watch?v=Yd8weV0xCr4)
