---
layout: default
title: "From MCP Tool-call to Motor Command: Giving Agents Fleet-scale... - Alexander Tsyplikhin, Arm"
nav_order: 132
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Alex from ARM presents Device Connect, an open-source framework designed to bridge the gap between AI agents and physical devices like robots and sensors."
resource: "https://www.youtube.com/watch?v=7-1R77IkbmQ"
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

Alex from ARM presents Device Connect, an open-source framework designed to bridge the gap between AI agents and physical devices like robots and sensors.
The technology addresses the complexity of integrating diverse hardware by providing a vendor-neutral, model-agnostic foundation that simplifies discovery, event subscription, and function invocation across large fleets.
Device Connect utilizes a pub/sub mesh with pluggable transports to enable secure, low-latency communication, even in offline or air-gapped environments, while abstracting away complex authentication and transport code for developers.
The presentation highlights several demos, including agents controlling distributed robotic arms, managing thousands of simulated phones, and optimizing inference routing in smart buildings, demonstrating the system's ability to handle dynamic, multi-device tasks efficiently.
By leveraging existing technologies like MCP and ROS, Device Connect aims to unlock the value of physical AI by making it easier to deploy intelligent, collaborative systems at scale.

# Main Points

|   # | Main point                                                                                                                                                     |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | "Device Connect," an open-source technology designed to connect AI agents to physical devices like robots, sensors, and cameras.                               |
|   2 | "physical AI" to unlock value in dynamic environments such as warehouses and research labs, moving beyond data-center-based MCP servers.                       |
|   3 | , which makes scaling to large fleets difficult and creates exponential integration work for agents.                                                           |
|   4 | , model-agnostic framework that allows devices to collaborate even when offline or partitioned from the cloud.                                                 |
|   5 | : Discovery (identifying available devices and status), Subscription (agents subscribing to device events), and Invoke (calling procedures across devices).    |
|   6 | , NATS, and MQTT.                                                                                                                                              |
|   7 | (as a gateway for device fleets) and ROS (for internal robot component management), acting as the "connecting tissue" between agents and hardware.             |
|   8 | , status (sent via heartbeats), and functions/events, which is LLM-friendly for agent interpretation.                                                          |
|   9 | (KV store) to restore system context if orchestrator scripts fail.                                                                                             |
|  10 | , abstracting away authentication, authorization, and transport complexities.                                                                                  |
|  11 | , on-premise deployments and allows for direct device-to-device communication without a central broker if connectivity is lost.                                |
|  12 | , allowing agents to react via expensive LLM inference, low-latency decision models, or simple rules based on the event's complexity.                          |
|  13 | , with the design aiming to make insecure deployment difficult and secure deployment easy.                                                                     |
|  14 | , controlling robots across continents via AWS, and coordinating real and simulated robotic arms based on visual cues.                                         |
|  15 | ,400 simulated phones to create patterns, showcasing the ability to issue commands to many devices simultaneously.                                             |
|  16 | , Device Connect bridges Matter devices to agents and routes inference tasks to the best available local device (e.g., MacBook, Jetson) to reduce cloud costs. |
|  17 | , allowing agents to discover new tools and execute complex tasks in unfamiliar environments without extensive pre-training.                                   |
|  18 | , with the team actively seeking feedback to inform future versions of the technology.                                                                         |

# Video

[![Video thumbnail](https://img.youtube.com/vi/7-1R77IkbmQ/hqdefault.jpg)](https://www.youtube.com/watch?v=7-1R77IkbmQ)

[Watch on YouTube](https://www.youtube.com/watch?v=7-1R77IkbmQ)
