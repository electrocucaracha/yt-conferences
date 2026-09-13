---
type: Video Note
title: "Reflections on Context Engineering Via MCP Servers - Till Döhmen, MotherDuck"
description: "Till, from Mother Duck, discusses the company's development of a cloud data warehouse built on DuckDB, emphasizing its compute isolation model that ensures each user has a dedicated compute instance, thus preventing inefficient queries from..."
resource: https://www.youtube.com/watch?v=BJYiOKgnKaQ
tags: ["mcp-dev-summit-na-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Till, from Mother Duck, discusses the company's development of a cloud data warehouse built on DuckDB, emphasizing its compute isolation model that ensures each user has a dedicated compute instance, thus preventing inefficient queries from affecting others.
He describes the evolution of their MCP server, which enables agentic access to data and supports tools for schema exploration and documentation, culminating in the creation of "dives"—interactive, shareable data visualizations that can be built and embedded by users without coding expertise.
Till highlights the challenges of context engineering within agent-client interactions, such as tool discovery, workflow chaining, and the variability of client support for features like initial instructions.
He expresses a wish for better feedback mechanisms from clients, improved workflow support, and more robust client-specific testing and observability.
Finally, he notes that dives fill a gap between static dashboards and ad hoc business questions, allowing flexible, user-driven visualizations and potentially serving as a foundation for more reliable, vetted analytics within organizations.
# Main Points

|   # | Main point                                                                                                                                         |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Till works at Mother Duck, a cloud data warehouse company based on DuckDB.                                                                         |
|   2 | Each user gets their own compute instance, ensuring compute isolation.                                                                             |
|   3 | Agent-generated inefficient queries do not impact other users due to this isolation.                                                               |
|   4 | DuckDB enables fast query execution, making agent-driven analytics responsive.                                                                     |
|   5 | Mother Duck developed an MCP server to integrate agents with their database.                                                                       |
|   6 | Initial MCP server had issues with agents sending Postgres-style queries; additional tools were added for schema exploration.                      |
|   7 | A sub-agent tool was introduced to answer documentation-related questions and provide context.                                                     |
|   8 | The "get dive guide" tool was added to enhance agent context and guide SDK usage.                                                                  |
|   9 | Users began creating and sharing "dives," which are visual cloud artifacts for insights.                                                           |
|  10 | Early dives were static React code with hardcoded data; later, live queries were enabled via a TypeScript/React SDK.                               |
|  11 | Agents can now save dives in Mother Duck, turning them into embeddable React apps with live querying.                                              |
|  12 | Non-developers have created complex visualizations and even games using the MCP server.                                                            |
|  13 | MCP app spec extension enabled interactive, live-query visualizations in chat interfaces like Claude and ChatGPT.                                  |
|  14 | MCP offers smooth authentication and native distribution; users can add Madak directly in app directories.                                         |
|  15 | MCP apps allow UI elements like dives to be integrated into chat clients, reducing reliance on the web UI.                                         |
|  16 | There are challenges with tool discovery, tool chaining, and context engineering due to client differences and lack of back-channel communication. |
|  17 | Wish list includes better client identification, improved tool chaining, client-specific UX testing, and enhanced observability.                   |
|  18 | Dives fill the gap between static dashboards and ad hoc questions, allowing flexible, shareable visualizations.                                    |
|  19 | Trust systems for dives are being considered, such as vetting and stamping queries.                                                                |
|  20 | Automated evaluation of MCP servers is influenced by the specific agent ha                                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=BJYiOKgnKaQ)