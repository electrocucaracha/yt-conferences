---
type: Video Note
title: "[Session] Streams, Sessions, Stats Transport and Client Behaviour in Practice"
description: "Sean Smith from Hugging Face introduces his work on the MCP server and discusses various options for deploying streamable HTTP transport, focusing on session management, client behavior, and server configuration. He demonstrates how simple..."
resource: https://www.youtube.com/watch?v=OSoEX7jY0m4
tags: ["mcp-dev-summit-eu-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Sean Smith from Hugging Face introduces his work on the MCP server and discusses various options for deploying streamable HTTP transport, focusing on session management, client behavior, and server configuration.
He demonstrates how simple request-response setups can be enhanced with features like progress notifications and bidirectional communication, highlighting the importance of associating responses with the correct streams and managing session IDs effectively, especially in multi-threaded or load-balanced environments.
Smith shares statistics from the Hugging Face server, noting a significant drop in traffic due to changes in client behavior and emphasizing the chatty nature of the MCP protocol, with many overhead calls compared to valuable tool calls.
He advises caution when deploying advanced features like server-initiated requests in public environments due to challenges with connection management and timeout handling.
Finally, Smith encourages participation in the MCP transports working group, mentioning ongoing efforts to make the protocol stateless by default for improved reliability and scalability.
# Main Points

|   # | Main point                                                                                                         |
| --: | ------------------------------------------------------------------------------------------------------------------ |
|   1 | Sean Smith from Hugging Face presented on deploying streamable HTTP with MCP servers.                              |
|   2 | Hugging Face server provides access to trending models, datasets, and thousands of ML applications.                |
|   3 | In late August, a sudden and significant traffic drop was observed on the server.                                  |
|   4 | MCP servers are popular due to easy plug-and-play setup.                                                           |
|   5 | Streamable HTTP offers multiple configuration options for deployment.                                              |
|   6 | Simplest setup: HTTP request/response with JSON RPC; requires enabling JSON response in SDK.                       |
|   7 | For progress notifications, use SSE streams to send updates and final responses.                                   |
|   8 | Progress notifications help keep users informed and reset timeout counters.                                        |
|   9 | MCP is bidirectional: servers can also send requests to hosts (e.g., elicitation forms).                           |
|  10 | Elicitation involves server sending a request, host filling a form, and posting results back.                      |
|  11 | Server-initiated communications use a "get channel" for unsolicited messages and pings.                            |
|  12 | Keeping the get channel alive is crucial to avoid silent disconnections.                                           |
|  13 | Session ID is allocated during initialization and is tied to the HTTP transport layer.                             |
|  14 | Session ID acts as a connection ID, not a chat ID; managing state across threads and servers is complex.           |
|  15 | Load-balanced environments require careful handling of session and request IDs.                                    |
|  16 | MCP protocol is chatty: for every tool call, there are many overhead calls (e.g., initializes, resource requests). |
|  17 | Clients often do not send deletes or tidy up after themselves.                                                     |
|  18 | Only 1% of clients support sampling, but 22% of tool uses come from hosts that do.                                 |
|  19 | Usage of MCP remote has dropped significantly.                                                                     |
|  20 | Hugging Face MCP server is open source and can be deployed statelessly or statefully.                              |
|  21 | SDK experience varies depending on desired server statefulness.                                                    |
|  22 | Handling get connections and connection breakages at scale is challenging.                                         |
|  23 | Timeout handling is difficult if hosts do not reset timeout windows on progress notifications.                     |
|  24 | Transports working group is considering making MCP stateless by                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=OSoEX7jY0m4)