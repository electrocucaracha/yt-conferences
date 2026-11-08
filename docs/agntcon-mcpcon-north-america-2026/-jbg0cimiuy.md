---
layout: default
title: "A2A v1 Deep Dive: The Specification,... - Luca Muscariello, Cisco & Darrel Miller, Microsoft"
nav_order: 80
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Daryl Miller and Luca present an overview of the A2A protocol, focusing on its extensibility through custom data models, operations, and protocol bindings."
resource: "https://www.youtube.com/watch?v=-jBG0cIMiuY"
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

Daryl Miller and Luca present an overview of the A2A protocol, focusing on its extensibility through custom data models, operations, and protocol bindings.
They demonstrate a live workflow where a buyer agent interacts with seller agents to purchase wine, initially using natural language via GitHub Copilot, which results in slower response times due to multiple LLM calls.
To optimize performance, they showcase the use of structured content and custom media types, reducing the end-to-end latency from over 700 seconds to just 25 milliseconds by bypassing natural language processing for agreed-upon data formats.
Luca further illustrates the protocol’s network capabilities by deploying agents in the cloud and utilizing SLIM (Secure Low Latency Interactive Messaging), a custom protocol binding that enables secure, multicast RPC calls over a relay node without exposing public endpoints.
Finally, they preview upcoming features in A2A 1.1, including a more granular task timeline and full bi-directional streaming support for sending and receiving artifacts and messages.

# Main Points

|   # | Main point                                                                                                                                                                                                                                                                             |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | : Daryl Miller (Microsoft) and Luca (Cisco) presented on extending the A2A (Agent-to-Agent) protocol, a Linux Foundation project with a mascot named Ada.                                                                                                                              |
|   2 | : The protocol consists of three layers:                                                                                                                                                                                                                                               |
|   3 | : Includes tasks, agent cards, messages, parts, and artifacts, extensible via mechanisms or custom media types.                                                                                                                                                                        |
|   4 | : Supports sending messages, subscribing to streams, and retrieving tasks; extensions can inject signals to alter workflows.                                                                                                                                                           |
|   5 | : Allows changing the underlying transport mechanism (e.g., JSON-RPC, HTTP+JSON) for specific use cases.                                                                                                                                                                               |
|   6 | : Buyer/Seller Agents**:                                                                                                                                                                                                                                                               |
|   7 | (via GitHub Copilot) discovered a seller agent using an AI Catalog and a custom CLI skill, as native coding harness support for A2A is not yet available.                                                                                                                              |
|   8 | , resulting in high latency (~762 seconds) due to multiple LLM calls for translation and processing.                                                                                                                                                                                   |
|   9 | : By advertising structured media types (Request for Quote, Purchase Order) in the agent card, the system switched to structured data transmission. This reduced end-to-end latency to 25 milliseconds by eliminating LLM translation overhead.                                        |
|  10 | : If API structures change or break, the system can fall back to natural language/AI processing to maintain functionality.                                                                                                                                                             |
|  11 | : A community-submitted extension required the buyer to prove they are over 21 via a QR code credential on a mobile device before completing the wine purchase.                                                                                                                        |
|  12 | : A2A supports streaming, polling, and webhooks; the demo used polling to confirm task completion.                                                                                                                                                                                     |
|  13 | (SLIM Protocol)**:                                                                                                                                                                                                                                                                     |
|  14 | , deployed by Cisco and other customers.                                                                                                                                                                                                                                               |
|  15 | (Secure Low Latency Interactive Messaging)**: A custom protocol binding enabling multicast RPC calls. It allows a buyer agent to send a single request to multiple seller agents simultaneously.                                                                                       |
|  16 | : Uses a relay node for encrypted message forwarding. Agents join virtual channels secured by MLS (Message Layer Security). This prevents seller agents from exposing public web endpoints, enhancing security and simplifying deployment in Kubernetes environments using SPIFFE IDs. |
|  17 | : SLIM supports agents joining transactions dynamically without pre-exposed servers, similar to group chat mechanics.                                                                                                                                                                  |
|  18 | : Protocols can be switched per message (e.g., from SLIM to HTTP+JSON) based on availability or requirements.                                                                                                                                                                          |
|  19 | :                                                                                                                                                                                                                                                                                      |
|  20 | : Replaces the vague "history" concept with a granular timeline tracking specific events, inputs, and status changes within a task.                                                                                                                                                    |
|  21 | : Enables streaming of inputs (not just outputs), allowing agents to send chunks of artifacts (e.g., meeting transcripts, document parts) in real-time.                                                                                                                                |
|  22 | : The team encourages developers to visit the A2A project site and propose new extensions.                                                                                                                                                                                             |

# Video

[![Video thumbnail](https://img.youtube.com/vi/-jBG0cIMiuY/hqdefault.jpg)]("https://www.youtube.com/watch?v=-jBG0cIMiuY")

[Watch on YouTube](https://www.youtube.com/watch?v=-jBG0cIMiuY)
