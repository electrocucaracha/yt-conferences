---
layout: default
title: "MCP Live: Streaming Context To AI Agents - Harshit Kohli, Amazon Web Services"
nav_order: 56
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  In this presentation, Harshit Kohli from Amazon Web Services discusses
  extending the traditional MCP (Message Control Protocol) request-response model
  to a real-time, streaming architecture for AI agents. By integrating event sources
  like l...
resource: https://www.youtube.com/watch?v=V7JceTECVO0
tags:
  - mcp-dev-summit-na-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

In this presentation, Harshit Kohli from Amazon Web Services discusses extending the traditional MCP (Message Control Protocol) request-response model to a real-time, streaming architecture for AI agents.
By integrating event sources like log simulators with a message bus (such as Kafka or Kinesis), and using a streaming MCP server, AI agents can receive and interact with live data feeds, enabling immediate anomaly detection and remediation.
The architecture includes features like bounded queues to manage back pressure, granular authorization using Sedar policies, and a hybrid protocol that supports both real-time streaming and interactive queries.
The demo illustrates how this setup allows for rapid detection and handling of anomalies, which is especially valuable in mission-critical domains like finance and healthcare.
The solution is designed to be flexible, decoupling the streaming platform from the AI agents, and can be enhanced with advanced AI models for smarter analysis and automated responses.

# Main Points

|   # | Main point                                                                                                                      |
| --: | ------------------------------------------------------------------------------------------------------------------------------- |
|   1 | AI agents can receive real-time data feeds for immediate anomaly detection and response.                                        |
|   2 | Traditional MCPs use a request-response model, leading to delays and stale context.                                             |
|   3 | Streaming MCP architecture streams context to AI agents, enabling real-time monitoring and interaction.                         |
|   4 | Event sources (e.g., log simulators, applications) produce logs sent to a message bus (Kafka, Kinesis, etc.).                   |
|   5 | Streaming MCP server consumes events, detects anomalies, and uses websockets for real-time, interactive feeds to agents.        |
|   6 | Sedar policy engine provides granular, per-request authorization for agents.                                                    |
|   7 | AI agents subscribe to real-time feeds, detect anomalies, and can interact with incoming data.                                  |
|   8 | Bounded queue (default 500 events) manages back pressure; slow agents are dropped to maintain pipeline integrity.               |
|   9 | Dead letter queues can be used for failed events, allowing replay and recovery.                                                 |
|  10 | Hybrid protocol supports both real-time streaming and query-based interactions.                                                 |
|  11 | Anomaly detection uses a sliding window (e.g., 100 events, 30% failure threshold); rules are customizable.                      |
|  12 | Selective anomaly rule definition is recommended to avoid alert fatigue.                                                        |
|  13 | Streaming MCP enables real-time incident detection and auto-remediation, critical for domains like finance and healthcare.      |
|  14 | Sedar authorization is preferred for its granular, per-request control over agent actions.                                      |
|  15 | Architecture is decoupled; changing the streaming platform does not affect AI agent code.                                       |
|  16 | Consumer groups and partitioning in Kafka help manage multiple agents and topics.                                               |
|  17 | Exponential backoff and context snapshots help manage slow agents and ensure data integrity.                                    |
|  18 | Integration with LLMs can enhance anomaly detection and root cause analysis.                                                    |
|  19 | Demo showcased real-time log simulation, anomaly detection, and interactive querying.                                           |
|  20 | Agents stop processing if their event buffer exceeds the threshold; in production, slow agents should be fixed and reconnected. |
|  21 | Kafka’s durability and replay features prevent data lo                                                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=V7JceTECVO0)
