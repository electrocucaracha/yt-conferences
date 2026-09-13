---
type: Video Note
title: "Lessons Learned Building Intelligent UIs With MCP Apps - Riley Scheid, Reboot (reboot.dev)"
description: "Riley presents lessons learned from building MCP apps over the past two months, focusing on emerging patterns and best practices. He explains that MCP apps now support returning real UI components, which is especially valuable when a graphi..."
resource: https://www.youtube.com/watch?v=aRSO4yfCLxQ
tags: ["mcp-dev-summit-na-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Riley presents lessons learned from building MCP apps over the past two months, focusing on emerging patterns and best practices.
He explains that MCP apps now support returning real UI components, which is especially valuable when a graphical interface is superior to plain text, such as for data visualization or branded experiences.
Riley discusses the challenges of implementing real-time and asynchronous communication, noting that while MCP is fundamentally request-response, developers can leverage iframes and websockets for real-time updates, though this is not officially supported in the spec.
He emphasizes the importance of managing state carefully, recommending the use of an authoritative state server to avoid inconsistencies between the UI, context, and model, and warns about potential pitfalls with tools like updateModelContext and sendMessage.
Riley also highlights the significance of clear API schemas and descriptions, the need to account for client-specific behaviors (such as session handling), and introduces the Reboot framework, which simplifies building scalable, reactive, and multiplayer MCP apps with strong state management and declarative interfaces.
The talk concludes with a Q&A covering topics like multi-user interactions, framework compatibility, authorization flows, client differences, and tool composition strategies.
# Main Points

|   # | Main point                                                                                                                          |
| --: | ----------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Riley has been building MCP apps for two months and shares lessons learned and emerging patterns.                                   |
|   2 | MCP apps now support returning real UI components, not just text.                                                                   |
|   3 | MCP apps are most useful when UI is significantly better than text, e.g., displaying graphs instead of CSVs or branded experiences. |
|   4 | Secure portals are preferred for sensitive data like credit card information.                                                       |
|   5 | MCP allows AI to access and mutate state, enabling stateful interactions.                                                           |
|   6 | Real-time and asynchronous communication are key concerns for MCP apps.                                                             |
|   7 | MCP is fundamentally request-response; no built-in real-time (websockets) support.                                                  |
|   8 | App bridge connects the app to the host and MCP server but lacks real-time facilities.                                              |
|   9 | Resource notifications exist but are not a replacement for websockets.                                                              |
|  10 | Real-time can be achieved by leveraging the iframe and using websockets via the connect domains allow list.                         |
|  11 | Polling is possible but not ideal; websockets provide immediate server updates.                                                     |
|  12 | Use caution: off-label usage of websockets may not be future-proof unless specified.                                                |
|  13 | Async operations use tasks (SE 1686): tool returns a task ID, which can be polled for completion.                                   |
|  14 | Avoid requiring users to refresh for updates; let the UI monitor task completion.                                                   |
|  15 | Use send message to notify users when tasks complete, but experiences vary by client.                                               |
|  16 | State can exist in multiple places: authoritative state server, context, iframe (React state), and messages.                        |
|  17 | Prefer keeping state in an authoritative state server to avoid split-brain scenarios.                                               |
|  18 | Be careful with update model context and send message to prevent inconsistent states.                                               |
|  19 | Descriptions and schemas are crucial for both humans and AIs; be explicit in tool descriptions.                                     |
|  20 | Session handling varies by client; test across clients or use user IDs instead of session IDs.                                      |
|  21 | Reboot is an open-source framework for building MCP apps, focusing on clear schemas, declarative interfaces, and durable state.     |
|  22 | Reboot supports multiplayer, reactive, and scalable apps                                                                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=aRSO4yfCLxQ)