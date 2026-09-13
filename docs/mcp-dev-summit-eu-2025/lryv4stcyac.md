---
type: Video Note
title: "[Session] Lessons Learned Building the Chrome DevTools MCP Server"
description: "Jack, a member of the Google Chrome DevTools team, introduces the newly released official Chrome DevTools MCP server, inviting feedback from users as it is still in early development. He discusses the team's journey in building AI tooling f..."
resource: https://www.youtube.com/watch?v=lRYv4STCYAc
tags: ["mcp-dev-summit-eu-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Jack, a member of the Google Chrome DevTools team, introduces the newly released official Chrome DevTools MCP server, inviting feedback from users as it is still in early development.
He discusses the team's journey in building AI tooling for DevTools, highlighting the shift from creating tools for human users to designing for AI agents, which required rethinking value propositions and adapting data formats for efficiency.
Initial attempts at high-level, niche tools proved less effective, leading to the current approach of exposing granular, composable actions that better support diverse debugging workflows and simplify setup.
Jack outlines ongoing challenges, such as managing the non-determinism of AI, ensuring compatibility across various clients and models, and developing robust evaluation methods for AI-driven features.
He also notes the need to support richer outputs like images and to adapt to the rapidly evolving AI and MCP landscape, concluding with a call for community feedback to help improve the server.
# Main Points

|   # | Main point                                                                                                                                        |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Jack from Google Chrome Tools presented on the Chrome DevTools MCP server.                                                                        |
|   2 | The official Chrome DevTools MCP server was released recently; feedback is encouraged.                                                            |
|   3 | The talk covered the journey, challenges, and learnings from building AI tooling in DevTools.                                                     |
|   4 | Shifted focus from human users to AI agents as primary consumers of DevTools outputs.                                                             |
|   5 | Early experiments showed LLMs could often solve problems without custom tools, prompting a focus on unique value DevTools can provide.            |
|   6 | Identified value in providing runtime browser data, source maps, and debugging capabilities to AI agents.                                         |
|   7 | Shipped the AI assistance panel in DevTools last year, allowing chat-style AI debugging.                                                          |
|   8 | Learned the importance of prompt engineering, adapting to new features like function calling, and managing context window limitations.            |
|   9 | Developed more efficient data representations (e.g., compressed call trees) to reduce token usage without losing quality.                         |
|  10 | Initial MCP server exposed high-level, niche tools, which proved inflexible and complex to set up.                                                |
|  11 | New MCP server exposes granular, composable actions (e.g., clicking, filling forms, resizing, recording traces) for flexible debugging workflows. |
|  12 | Setup is now simplified; the server manages Chrome instances automatically.                                                                       |
|  13 | Challenges include non-determinism in AI, wide variance across clients and models, and difficulty in consistent evaluation.                       |
|  14 | Testing and evaluation now require automated suites and representative datasets; exploring LLM-as-judge approaches for output quality.            |
|  15 | Considering richer outputs (e.g., images) in MCP responses, but unsure how clients and users will handle them.                                    |
|  16 | Rapid evolution of MCP spec, clients, and AI models requires ongoing adaptation.                                                                  |
|  17 | UX best practices for integrating AI into DevTools are still emerging.                                                                            |
|  18 | Users are encouraged to try the MCP server, provide feedback, and help improve the tool.                                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=lRYv4STCYAc)