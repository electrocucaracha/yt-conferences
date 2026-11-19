---
layout: default
title: "Beyond Chat: Lessons Learned Building Intelligent UIs with... - Riley Scheid, Reboot (reboot.dev)"
nav_order: 31
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Riley, ingeniero de software con más de una década de experiencia, presenta los desafíos de crear aplicaciones MCP (Model Context Protocol) que funcionen en tiempo real y en múltiples plataformas."
resource: "https://www.youtube.com/watch?v=qd3W4iAUv0E"
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

Riley, ingeniero de software con más de una década de experiencia, presenta los desafíos de crear aplicaciones MCP (Model Context Protocol) que funcionen en tiempo real y en múltiples plataformas.
Explica que desarrolló una aplicación MCP que replica un panel de control web de Reboot, una plataforma para crear aplicaciones seguras y escalables, destacando las complejidades de hacer que funcione tanto en entornos web como en clientes de Claude y ChatGPT.
El principal obstáculo es que MCP es fundamentalmente un protocolo de solicitud-respuesta que no soporta comunicaciones en tiempo real de forma nativa, lo que requiere soluciones alternativas como túneles públicos o WebSockets.
Riley recomienda usar AppBridge para aplicaciones simples que no necesiten datos reactivos, pero advierte que lograr actualizaciones en tiempo real requiere configuraciones complejas, especialmente en desarrollo local donde no se pueden usar conexiones directas a localhost en ciertos clientes.
Concluye pidiendo a los mantenedores de MCP que implementen comunicaciones estilo WebSocket de forma nativa para resolver estos problemas fundamentales.

# Main Points

|   # | Main point                                                                                                                     |
| --: | ------------------------------------------------------------------------------------------------------------------------------ |
|   1 | # Key Points                                                                                                                   |
|   2 | • Speaker Riley has been creating MCP applications for approximately one year                                                  |
|   3 | • Reboot is a programming framework for building secure and scalable applications                                              |
|   4 | • A Reboot dashboard web application was converted into an MCP application over two weeks                                      |
|   5 | • MCP applications must work across multiple hosts: web, Claude, ChatGPT, cloud code, desktop code, Codex, and chat.openai.com |
|   6 | • Subtle differences exist between different MCP environments, similar to the "user agent era" of web development              |
|   7 | • Design requirements: dashboard must work on web and MCP, function across all hosts, and remain real-time updated             |
|   8 | • React can be used for both web and MCP applications, allowing shared components                                              |
|   9 | • AppBridge enables MCP tool calls but cannot stream data                                                                      |
|  10 | • MCP is fundamentally a request-response protocol without native real-time capabilities                                       |
|  11 | • Resource notifications exist but require redesigning the system to represent all data as resources                           |
|  12 | • WebSockets cannot be used on localhost in ChatGPT due to Content Security Policy restrictions                                |
|  13 | • WebSockets work in production but not in local development environments                                                      |
|  14 | • Tunneling solutions expose user data to the internet and introduce complexity                                                |
|  15 | • Long polling over AppBridge would require re-implementing WebSockets and has significant limitations                         |
|  16 | • The MCP Tasks API does not solve real-time update problems                                                                   |
|  17 | • Recommended solution: use tunnels for real-time applications, but native WebSocket-style communication in MCP is needed      |
|  18 | • For non-reactive applications that don't change, AppBridge is recommended as it works on localhost and in production         |
|  19 | • QA testing across different MCP clients is currently manual                                                                  |
|  20 | • Web-based apps benefit most from real-time updates when server state changes                                                 |

# Video

[![Video thumbnail](https://img.youtube.com/vi/qd3W4iAUv0E/hqdefault.jpg)](https://www.youtube.com/watch?v=qd3W4iAUv0E)

[Watch on YouTube](https://www.youtube.com/watch?v=qd3W4iAUv0E)
