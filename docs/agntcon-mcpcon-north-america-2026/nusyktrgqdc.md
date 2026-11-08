---
layout: default
title: "The Model Proposes, the Server Decides:... - Antoni Kozelski, Vstorm & Bartosz Gonczarek, VStorm"
nav_order: 27
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Bartosz Gonczarek, CTO de Vstorm, presenta las lecciones aprendidas al desarrollar un sistema complejo de pedidos de impresión para Renow que utiliza modelos de IA en ambos lados: un asistente del ..."
resource: "https://www.youtube.com/watch?v=nuSYKTrgQdc"
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

Bartosz Gonczarek, CTO de Vstorm, presenta las lecciones aprendidas al desarrollar un sistema complejo de pedidos de impresión para Renow que utiliza modelos de IA en ambos lados: un asistente del usuario y agentes en el servidor.
El equipo identificó cuatro problemas principales: los anfitriones (hosts) no leen completamente las guías de usuario, existe variabilidad en cómo diferentes plataformas utilizan las herramientas disponibles, el catálogo de productos es enorme y continuará creciendo, y el servidor no puede ver las conversaciones del usuario con su asistente de IA.
Para resolverlos, Vstorm propone cinco reglas fundamentales: mantener la lógica crítica dentro de las definiciones de herramientas en lugar de instrucciones generales, incluir información necesaria en el contenido de texto, requerir confirmación adicional del usuario para acciones irreversibles, usar características básicas soportadas por todos los hosts, y probar exhaustivamente en cada plataforma.
Vstorm está desarrollando Agentic OS, un entorno de código abierto que incorpora estas lecciones para simplificar futuros proyectos con agentes.

# Main Points

|   # | Main point                                                                                                                                                                                                                                                                   |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | # Key Points                                                                                                                                                                                                                                                                 |
|   2 | • Bartosz Gonczarek is CTO of Vstorm, presenting lessons from a complex print ordering system project using models on both user and host sides                                                                                                                               |
|   3 | • Project started in 2024 with Mixam creating an AI agent for print orders on their site, launched mid-2025 with significant revenue increase                                                                                                                                |
|   4 | • Success led to M&A activity; Cimpress and Mixam created Renow spin-off to focus on advanced scenario where AI assistants communicate with agents instead of users directly using sites                                                                                     |
|   5 | • Created MCP server supporting Claude AI, ChatGPT, Claude Code, and Codex with model-based functionalities: product configuration, quoting, ordering, and design generation                                                                                                 |
|   6 | • Four main problems identified: (1) Hosts cut user guide content; (2) Variability in how different hosts use tools; (3) Enormous growing catalog; (4) Server cannot see user-AI assistant conversations                                                                     |
|   7 | • Guide discovery rates: Claude reads ~4,000 characters; ChatGPT reads beginning only; Claude AI omits it entirely; Codex reads full guide after model searches it                                                                                                           |
|   8 | • Different hosts load tools differently; Claude shows only tool names until searched; Claude Code indicates out-of-scope items; Codex assumes capability to generate designs instead of using tool                                                                          |
|   9 | • Solution: Include instructions within tool definitions rather than relying on external guides; error messages return to model each time                                                                                                                                    |
|  10 | • Catalog contains 122 products with thousands of options each (up to 1 million combinations per product); exposing one tool per product costs too many tokens                                                                                                               |
|  11 | • System uses small language models as configuration agents to validate and fill order forms based on user intent                                                                                                                                                            |
|  12 | • Critical issue: Model can misinterpret user correction as approval, potentially sending invalid print orders                                                                                                                                                               |
|  13 | • Solution: Force host to reformulate user intent before executing irreversible steps like sending print plans                                                                                                                                                               |
|  14 | • Five rules for building similar MCP servers: (1) Keep fundamental rules outside server instructions; (2) Put needed model content in text; (3) Require user confirmation for irreversible steps; (4) Send base that each host supports; (5) Test on all implementing hosts |
|  15 | • Vstorm created Agentic OS open-source environment with layers for communication channels, memory/knowledge, and models                                                                                                                                                     |
|  16 | • Goal: Simplify future custom agent systems by incorporating learnings from production projects                                                                                                                                                                             |

# Video

[![Video thumbnail](https://img.youtube.com/vi/nuSYKTrgQdc/hqdefault.jpg)]("https://www.youtube.com/watch?v=nuSYKTrgQdc")

[Watch on YouTube](https://www.youtube.com/watch?v=nuSYKTrgQdc)
