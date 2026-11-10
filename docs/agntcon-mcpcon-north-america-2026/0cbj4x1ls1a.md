---
layout: default
title: "Building an Agentic Eval Pipeline: Battle-Tested Lessons... - Kurtis Van Gent & Haoyu Wang, Google"
nav_order: 2
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: Curtis y Howie de Google Cloud Databases presentan un canal de evaluación agentic enfocado en evaluar herramientas MCP (Model Context Protocol) para bases de datos.
resource: "https://www.youtube.com/watch?v=0cBJ4X1LS1A"
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

Curtis y Howie de Google Cloud Databases presentan un canal de evaluación agentic enfocado en evaluar herramientas MCP (Model Context Protocol) para bases de datos.
Explican que Google Cloud ha desarrollado más de 50 servidores MCP gestionados y herramientas personalizadas a través del marco MCP Toolbox for Databases, lo que ha generado cientos de herramientas cuya calidad necesita medirse.
Presentan la evaluación basada en CUJ (Critical User Journey) como solución superior a las pruebas unitarias, ya que mide si los agentes usan correctamente las herramientas en contextos realistas, evaluando no solo la respuesta final sino todo el proceso, incluida la verificación del estado de los recursos en la nube.
Destacan tres características clave de una buena evaluación: múltiples turnos con simulación de usuarios, calificación de ruta y resultado, y uso cuidadoso de jueces LLM con puntuaciones deterministas.
Finalmente, comparten lecciones aprendidas sobre optimización de tokens, selección de habilidades adecuadas y manejo de operaciones de larga duración, presentando Eval Bench, una herramienta de código abierto disponible en GitHub para implementar estas evaluaciones.

# Main Points

|   # | Main point                                                                                                                                                                                                                               |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | # Key Points                                                                                                                                                                                                                             |
|   2 | ; contributed to stateless protocol transition                                                                                                                                                                                           |
|   3 | , BigQuery queries                                                                                                                                                                                                                       |
|   4 | , credentials, telemetry, and pooling                                                                                                                                                                                                    |
|   5 | ; challenge: determining tool quality                                                                                                                                                                                                    |
|   6 | (Critical User Journey) evaluation measures end-to-end user tasks, not just individual tool functionality                                                                                                                                |
|   7 | : multi-turn conversations, user simulation with adaptive responses, evaluation of route and results (not just final answer), deterministic scoring when possible, LLM judges with scorecard approach, calibration with human evaluators |
|   8 | , easy agent/tool swapping, various scoring metrics, AB comparison dashboards, CI/CD compatibility                                                                                                                                       |
|   9 | ; lazy loading and tool search help reduce initial consumption                                                                                                                                                                           |
|  10 | : compare same experiment with skill enabled/disabled to measure real impact                                                                                                                                                             |
|  11 | ; MCP tasks better handle asynchronous operations                                                                                                                                                                                        |
|  12 | (open-source, GitHub: Google Cloud Platform/eval-bench) implements described evaluation framework                                                                                                                                        |

# Video

[![Video thumbnail](https://img.youtube.com/vi/0cBJ4X1LS1A/hqdefault.jpg)](https://www.youtube.com/watch?v=0cBJ4X1LS1A)

[Watch on YouTube](https://www.youtube.com/watch?v=0cBJ4X1LS1A)
