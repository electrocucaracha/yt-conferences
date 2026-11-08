---
layout: default
title: "Leveraging A2A Protocol to Build Framework Agnostic Multi-Agent System - Sohil Shah, PayPal"
nav_order: 53
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Sohil, a staff engineer at PayPal, presents a session on leveraging the A2A protocol to build scalable multi-agent frameworks in enterprise environments."
resource: "https://www.youtube.com/watch?v=qoCn-lbQwCY"
tags:
  - agntcon-mcpcon-north-america-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-08T02:03:18+00:00
---

# Summary

Sohil, a staff engineer at PayPal, presents a session on leveraging the A2A protocol to build scalable multi-agent frameworks in enterprise environments.
He clarifies that while MCP is designed for agents to connect to tools with bounded contracts and binary outcomes, A2A facilitates open-ended conversations between agents, allowing for states such as requesting clarification, pausing, or resuming sessions.
To demonstrate the protocol’s framework-agnostic nature, he showcases a demo involving 16 agents built on different frameworks, including Google ADK, LangGraph, and CrewAI, which collaborate to handle a complex travel booking scenario.
The demo illustrates how a root agent delegates tasks to specialized sub-agents for inspiration, flight and hotel booking, payment processing, and pre-trip planning, effectively managing context and user preferences across the workflow.
The session concludes with a discussion on the importance of A2A for interoperability between disparate agent stacks, as well as the challenges of managing latency and governance in multi-agent systems.

# Main Points

|   # | Main point                                                                                                                                                                                                                                                                                                                     |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | : The session, led by Sohil (Staff Engineer at PayPal), focuses on leveraging the Agent-to-Agent (A2A) protocol to build multi-agent frameworks, facilitate context sharing, and scale in enterprise environments.                                                                                                             |
|   2 | :                                                                                                                                                                                                                                                                                                                              |
|   3 | (Model Context Protocol)**: Designed for agents to connect to tools. It features a bounded contract with a defined schema and only two outcomes: task completion or error.                                                                                                                                                     |
|   4 | (Agent-to-Agent)**: Enables agents to converse with other agents. It is open-ended, supporting multiple states such as requesting clarification, pausing, resuming, or waiting for human input.                                                                                                                                |
|   5 | : MCP and A2A are not mutually exclusive; they coexist in the same ecosystem. Use MCP for bounded tool calls and A2A for negotiation, clarification, or complex agent interactions.                                                                                                                                            |
|   6 | :                                                                                                                                                                                                                                                                                                                              |
|   7 | : A JSON-formatted message containing agent discovery information, communication protocols, and capabilities.                                                                                                                                                                                                                  |
|   8 | : The caller agent uses the Agent Card to establish communication, sends a task, and the specialist agent processes it and returns results.                                                                                                                                                                                    |
|   9 | : Agents communicate via JSON-RPC. Context transfer is flexible; developers can choose to send the entire context or compact it to relevant information before passing it to another agent.                                                                                                                                    |
|  10 | : A2A allows interoperability between different agent frameworks. The demo utilized agents built on Google ADK, LangGraph, and Crew AI, all running within Google’s Agent Runtime. This solves the problem of vertical stacks where capabilities cannot be easily shared between different organizational teams or frameworks. |
|  11 | : Booking Concierge ("Aura")**:                                                                                                                                                                                                                                                                                                |
|  12 | : A root agent orchestrates 16 sub-agents (e.g., inspiration, planning, flight search, hotel booking, payments, pre-trip, interop) to handle a travel booking workflow.                                                                                                                                                        |
|  13 | : The system stores user facts (e.g., vegetarian, window seats, luxury hotels) in a memory bank to tailor future itineraries.                                                                                                                                                                                                  |
|  14 | :                                                                                                                                                                                                                                                                                                                              |
|  15 | : Agents collaborate to suggest destinations (e.g., Machu Picchu) based on user preferences.                                                                                                                                                                                                                                   |
|  16 | & Booking**: Agents search for flights and hotels, negotiate options, and present a detailed itinerary with costs.                                                                                                                                                                                                             |
|  17 | : The system attempts payment via Apple Pay (which failed in the demo) and successfully processes via Google Pay, demonstrating error handling and course correction.                                                                                                                                                          |
|  18 | : A specialist agent provides a tailored packing checklist, visa requirements, and health advice based on the destination and weather.                                                                                                                                                                                         |
|  19 | : Agents provide real-time transit options (e.g., taxi/Uber) from the airport to the hotel, maintaining context of the entire itinerary.                                                                                                                                                                                       |
|  20 | : Post-trip, users can save new preferences (e.g., oxygen-enriched rooms) to the memory bank for future personalization.                                                                                                                                                                                                       |
|  21 | & Challenges**:                                                                                                                                                                                                                                                                                                                |
|  22 | : Agents can be containerized and deployed to Agent Runtime, pulling images from a registry. This allows for a unified platform regardless of the underlying framework.                                                                                                                                                        |
|  23 | & Governance**: Managing latency in multi-agent systems requires building a governance layer on top of A2A. This involves monitoring traces, events, token counts, and feedback cycles to detect issues, fix trajectories, and prevent infinite loops.                                                                         |
|  24 | : The demo used a custom UI (built with Gemini) to visualize agent interactions and communication streams, as standard ADK UIs may not support all runtime environments.                                                                                                                                                       |
|  25 | : A2A enables decentralized, cross-framework agent collaboration in enterprises, allowing different departments (e.g., HR, SRE, Payments) to share domain knowledge and delegate tasks without integrating all capabilities into a single monolithic agent.                                                                    |

# Video

[![Video thumbnail](https://img.youtube.com/vi/qoCn-lbQwCY/hqdefault.jpg)]("https://www.youtube.com/watch?v=qoCn-lbQwCY")

[Watch on YouTube](https://www.youtube.com/watch?v=qoCn-lbQwCY)
