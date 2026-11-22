---
layout: default
title: "Talks - Koushik Krishnan: Rest Easy with Jupyrest: Deploy notebooks as web services"
nav_order: 177
parent: PyCon US 2024
type: Video Note
description: "In this presentation, Kaik, a Site Reliability Engineer at Microsoft, introduces Jupyrest, an open-source library designed to convert Jupyter notebooks into REST APIs."
resource: "https://www.youtube.com/watch?v=EVSJxMnXoJk"
youtube_stats:
  view_count: 183
  like_count: 4
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

In this presentation, Kaik, a Site Reliability Engineer at Microsoft, introduces Jupyrest, an open-source library designed to convert Jupyter notebooks into REST APIs.
The tool addresses the common challenge of transitioning from notebook-based prototyping to production web services by allowing developers to define input and output schemas within a configuration file, thereby preserving the interactive benefits of notebooks while enabling serverless deployment.
Jupyrest supports complex data structures by allowing Python classes to be referenced in JSON schemas, which are automatically instantiated within the notebook during execution, ensuring that the underlying code remains pure Python without manual serialization.
The library is particularly well-suited for incident response automation, data science workflows, and custom dashboarding, where it provides robust debugging capabilities through detailed HTML execution logs and reproducible notebook artifacts.
However, the speaker advises against using Jupyrest for performance-critical services requiring low latency or high throughput, as notebook execution times are generally slower than traditional web frameworks.

# Main Points

|   # | Main point                                                                                                                                                         |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Jupyrest is an open-source library that converts Jupyter notebooks into REST APIs by defining input and output contracts.                                          |
|   2 | The tool addresses the limitation of notebooks remaining in prototype stages by enabling direct deployment as web services.                                        |
|   3 | A notebook function requires a unique ID, an input schema, and an output schema defined in a configuration file matching the notebook name.                        |
|   4 | Inputs are tagged with a parameters code cell, and outputs are returned using a save_output function similar to a standard return statement.                       |
|   5 | The library supports serverless deployments, including FastAPI and Azure Functions, handling scaling, authentication, and monitoring automatically.                |
|   6 | Execution results include JSON data, an HTML report of the notebook execution, and the raw IPYNB file for local debugging and reproduction.                        |
|   7 | Invalid input schemas are rejected, ensuring API integrity, while successful executions inject parameters as code cells before running the notebook top to bottom. |
|   8 | Python classes can be used as input schemas, allowing Jupyrest to convert JSON inputs into Python object instantiations within the notebook.                       |
|   9 | This approach enables modular API design where notebooks interact with native Python objects rather than serialized JSON data.                                     |
|  10 | The library is not suitable for performance-critical services requiring low latency or high throughput due to notebook execution times.                            |
|  11 | Primary use cases include incident response automation, data science workflows, custom dashboards, and reporting.                                                  |
|  12 | Jupyrest helps structure and maintain legacy script directories by converting them into documented, parameterized notebook functions.                              |
|  13 | Interactive widgets requiring a live Python kernel do not work in the static HTML output, but libraries like Plotly can provide interactivity if data is embedded. |
|  14 | Deployment mechanisms involve generating FastAPI applications for local use or Azure Functions applications for cloud environments.                                |
|  15 | The project is maintained under an MIT license with resources available on GitHub and a dedicated site.                                                            |

# Video

[![Video thumbnail](https://img.youtube.com/vi/EVSJxMnXoJk/hqdefault.jpg)](https://www.youtube.com/watch?v=EVSJxMnXoJk)

[Watch on YouTube](https://www.youtube.com/watch?v=EVSJxMnXoJk)
