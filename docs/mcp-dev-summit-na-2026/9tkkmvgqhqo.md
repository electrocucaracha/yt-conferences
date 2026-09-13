---
type: Video Note
title: "Enabling Agentic Cloud Workflows - Santhosh Misro & Mayur Deshpande, Google"
description: "In this presentation, Santo and Mayor from Google Cloud Storage discuss the development of the Storage Intelligence MCP server, which aims to bridge AI agents and cloud storage to enable autonomous, goal-driven storage management. They desc..."
resource: https://www.youtube.com/watch?v=9TkKmvgqHQo
tags: ["mcp-dev-summit-na-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this presentation, Santo and Mayor from Google Cloud Storage discuss the development of the Storage Intelligence MCP server, which aims to bridge AI agents and cloud storage to enable autonomous, goal-driven storage management.
They describe how traditional storage administration is manual and script-heavy, and their solution allows AI agents to analyze and act on metadata from billions of objects using natural language queries that are translated into SQL, leveraging tools like Gemini CLI.
The MCP server is structured with an insights toolset for analysis and an operations toolset for executing actions, ensuring snapshot consistency and reducing friction for users.
They detail optimizations such as tool chaining reduction, smart caching of static metadata, and performance tuning, which led to significant reductions in token usage and latency.
The team also addresses challenges in productionizing these agents, including workflow definition, cache management, and the potential for dynamic skill-based workflows in the future.
# Main Points

|   # | Main point                                                                                                                                  |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation covers storage intelligence MCP server bridging AI agents and cloud storage.                                                   |
|   2 | Goal is to reduce friction in storage management and enable autonomous storage management.                                                  |
|   3 | Traditional storage management involves manual, script-based tasks by admins.                                                               |
|   4 | Cloud Storage (GCS) customers have billions of objects globally.                                                                            |
|   5 | Introduced organization-wide data indexing for lightweight metadata extraction.                                                             |
|   6 | MCP server allows agents to query metadata and activity data for complex analysis.                                                          |
|   7 | Supports integration with agents like Gemini CLI and Cloud Code for goal-driven workflows.                                                  |
|   8 | MCP server has two toolsets: storage intelligence (analysis) and operations (execution).                                                    |
|   9 | Index creation uses a BigQuery-linked dataset, enabling SQL queries on metadata.                                                            |
|  10 | Developed NL-to-SQL toolset for agents to analyze and act using GCS APIs.                                                                   |
|  11 | Ensures snapshot consistency so agents act on complete, up-to-date data.                                                                    |
|  12 | Insights toolset includes index creation and metadata schema tools to reduce LLM hallucinations.                                            |
|  13 | Operations toolset manages actions like creating buckets and moving objects, with adjustable permissions.                                   |
|  14 | Demo example: using natural language to find and archive specific files across billions of objects.                                         |
|  15 | MCP server translates NL queries to SQL, runs them on metadata, and executes actions via operations tools.                                  |
|  16 | Productionization required tuning, golden datasets, LLM judges, and continuous evaluation.                                                  |
|  17 | Instrumented over 20 data points per Gemini CLI session for deeper analysis.                                                                |
|  18 | Optimized tool chaining and caching, reducing token usage by 35%.                                                                           |
|  19 | Cached static metadata and session context, reducing latency and median session cost (~$0.09).                                              |
|  20 | Tuned agent reasoning depth and wait time for balance between autonomy and latency.                                                         |
|  21 | Caching uses TTLs and focuses on static metadata to avoid outdated information.                                                             |
|  22 | Workflow optimization involved reducing and merging tools, with potential for dynamic skill-based workflows in the future. Ratings (1-5): 3 |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=9TkKmvgqHQo)