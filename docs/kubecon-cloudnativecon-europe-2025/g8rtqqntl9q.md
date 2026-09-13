---
type: Video Note
title: "Smooth Scaling With the OpAMP Supervisor: Managing Thousands of OpenTe... Evan Bradley & Andy Keller"
description: "The Open Agent Management Protocol (Opamp) is a network protocol for remote management of large fleets of observability agents. It allows for partial implementations of the protocol, making it extensible and agent-agnostic. Opamp enables fe..."
resource: https://www.youtube.com/watch?v=g8rtqqNTL9Q
tags: ["kubecon-cloudnativecon-europe-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The Open Agent Management Protocol (Opamp) is a network protocol for remote management of large fleets of observability agents.
It allows for partial implementations of the protocol, making it extensible and agent-agnostic.
Opamp enables features such as heartbeats to keep websocket connections alive, custom messages for implementing new features, and available components to determine compatibility between agents and servers.
The supervisor is a key component that manages collector configurations, sends updates to agents, and receives telemetry data from collectors.
It also supports remote configuration, binary upgrades, and hot reloading of collectors.
Opamp has the potential to simplify fleet management by providing a standardized way to configure and monitor large numbers of agents, but it poses challenges such as the thundering herd problem and ensuring consistency across multiple agents.
# Main Points

|   # | Main point                                                                                                                                                                |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | It supports both HTTP and websockets, with HTTP pulling updates periodically and websockets using a persistent connection to send messages directly.                      |
|   2 | The protocol allows for partial implementations and extensibility through custom capabilities and messages.                                                               |
|   3 | New features include heartbeats to keep websocket connections alive, custom messages for implementing new features without requiring support from all agents and servers. |
|   4 | Available components feature allows the server to know what components can be used in the collector.                                                                      |
|   5 | Supervisor is a tool that manages collectors and provides remote configuration capabilities.                                                                              |
|   6 | It supports hot reloading of configurations and can run multiple collectors with one supervisor.                                                                          |
|   7 | Future plans include increasing stability, refactoring, and implementing collector upgrades, enhanced telemetry configuration, and support for Java SDK and Kubernetes.   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=g8rtqqNTL9Q)