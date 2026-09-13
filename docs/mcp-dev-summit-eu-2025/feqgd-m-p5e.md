---
type: Video Note
title: "Multi-Agent Multi-User Collab thru MCP: Enabling Asynchronous Human-Agent Agent-Human Workflows"
description: "In this presentation, Andrew Culverson and Mun Burid introduce MAMU, a prototype application developed over several weeks that enables multi-agent, multi-user workspaces using the Model Context Protocol (MCP) for multiplayer AI collaboratio..."
resource: https://www.youtube.com/watch?v=FEqgD_m-p5E
tags: ["mcp-dev-summit-eu-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this presentation, Andrew Culverson and Mun Burid introduce MAMU, a prototype application developed over several weeks that enables multi-agent, multi-user workspaces using the Model Context Protocol (MCP) for multiplayer AI collaboration.
Unlike traditional single-user AI assistants, MAMU allows users’ agents to interact and collaborate with other specialized agents in a shared workspace, streamlining workflows such as onboarding or task management by leveraging collective agent expertise.
The system consists of a MAMU MCP server, which facilitates agent-to-agent communication and shared tools, and a desktop client that supports chat, context sharing, scheduled tasks, and access control.
Key underutilized MCP features—sampling (agent-to-agent requests) and elicitation (agent-to-human requests)—enable dynamic, context-rich interactions, such as daily standups, automated task creation, and human-in-the-loop approvals.
The demo showcases how agents can coordinate tasks, access resources, and escalate queries to humans when needed, with future plans including enhanced context management and resource sharing to further improve collaborative AI workspaces.
# Main Points

|   # | Main point                                                                                                                                                                          |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | MAMU is an application built over 3-4 weeks, standing for Multi-Agent Multi-User workspaces.                                                                                        |
|   2 | MAMU enables multiplayer AI, allowing users and agents to collaborate in a shared space.                                                                                            |
|   3 | Agents can reach out to other specialized agents to solve user requests collaboratively.                                                                                            |
|   4 | MCP (Model Context Protocol) acts as a universal connector, providing a common interface and communication method for agents.                                                       |
|   5 | MCP simplifies networking and shared context among multiple agents.                                                                                                                 |
|   6 | MAMU consists of two parts: MAMU MCP server (enables agent collaboration and tool access) and MAMU MCP desktop client (chat interface, productivity utilities, context management). |
|   7 | The desktop client allows viewing all chats, setting daily context (standup questions), and managing tool access (ARBAC).                                                           |
|   8 | MAMU leverages underutilized MCP features: sampling (server asks agent for response) and elicitation (server asks human for response).                                              |
|   9 | Sampling use cases: asynchronous tool follow-ups, event-based interactions, borrowing intelligence, multiplayer agent interactions.                                                 |
|  10 | Elicitation use cases: setup forms, human-in-the-loop approvals, borrowing human intelligence, agent-to-human interactions.                                                         |
|  11 | Daily context check-ins allow agents to aggregate and share user status and blockers.                                                                                               |
|  12 | Scheduled tasks (e.g., daily standups) can be automated across agents.                                                                                                              |
|  13 | Agents can interact to perform actions like creating GitHub issues or Jira tasks.                                                                                                   |
|  14 | Security is managed via ARBAC, allowing control over tool execution permissions for owners and non-owners.                                                                          |
|  15 | Agents can escalate requests to humans when lacking context, enabling agent-to-human communication.                                                                                 |
|  16 | Plans include enhanced context management and autonomous resource sharing among agents.                                                                                             |
|  17 | MAMU is an early prototype with more features planned and a newsletter available for updates.                                                                                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=FEqgD_m-p5E)