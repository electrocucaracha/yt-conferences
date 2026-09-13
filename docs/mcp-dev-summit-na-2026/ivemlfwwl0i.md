---
type: Video Note
title: "The Anatomy of a Meltdown: A Deep-Dive into MCP via Selective Sabotage - Joey Stout, Spacelift"
description: "Joey Stout, a solutions architect at Spacelift, presents an interactive talk on the anatomy of a meltdown, focusing on the Model Context Protocol (MCP) and its six core components: notifications, subscriptions, resources, prompts, tools, an..."
resource: https://www.youtube.com/watch?v=IvemlFwwl0I
tags: ["mcp-dev-summit-na-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Joey Stout, a solutions architect at Spacelift, presents an interactive talk on the anatomy of a meltdown, focusing on the Model Context Protocol (MCP) and its six core components: notifications, subscriptions, resources, prompts, tools, and logging.
Throughout the session, Joey demonstrates a custom web app and MCP server, allowing the audience to interact in real time and observe how changes—such as enabling or disabling features—affect both the AI agent (Claude) and the system’s behavior.
He illustrates how notifications inform agents of backend changes, how resources provide read-only data, and how prompts and tools shape agent capabilities, highlighting the importance of proper implementation and logging for observability.
Joey also discusses the variability in agent behavior depending on SDKs and the necessity for developers to fully implement MCP features, as some failures may be silent or misleading.
The talk concludes with a Q&A, emphasizing that MCP’s effectiveness relies on thoughtful integration and that some features may not be universally supported across agents.
# Main Points

|   # | Main point                                                                                                                                  |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Joey Stout, solutions architect at Spacelift, presented on the anatomy of a meltdown.                                                       |
|   2 | Interactive demo using a custom web app and MCP server; audience could participate via web app.                                             |
|   3 | AI agent (Claude) connected to the MCP server, reading audience reactions and questions in real time.                                       |
|   4 | MCP protocol components covered: notifications, subscriptions, resources, prompts, tools, and logging.                                      |
|   5 | Notifications inform agents of changes (e.g., tools added/removed); disabling notifications causes agents to be unaware of backend changes. |
|   6 | Resources provide readonly information to agents; disabling resources prevents agents from accessing this data.                             |
|   7 | Prompts give context or skills to agents; disabling prompts or improper SDK implementation can result in missing or default context.        |
|   8 | Tools enable specific actions; disabling tools prevents agents from performing those actions.                                               |
|   9 | Logging is essential for observability; disabling logging means maintainers can't see what's happening.                                     |
|  10 | Subscriptions allow agents to be notified of resource changes; not all agents implement subscriptions.                                      |
|  11 | Demonstrated fallback between resources and tools for getting audience summaries.                                                           |
|  12 | MCP requires explicit implementation of all components for full functionality.                                                              |
|  13 | Some features (like resources and subscriptions) are not universally adopted or implemented in all agents.                                  |
|  14 | MCP uses standard input/output or HTTPS as transport; logging and observability must be handled differently than traditional programming.   |
|  15 | Key takeaways: MCP has six components, failures can be silent or misleading, and logging is critical.                                       |
|  16 | Joey may open source the demo code but warns of bad practices in the current version.                                                       |
|  17 | Audience Q&A covered tool availability, open sourcing, and MCP protocol basics.                                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=IvemlFwwl0I)