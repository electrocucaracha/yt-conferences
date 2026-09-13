---
layout: default
title: "[Session] Tools, Not Endpoints: The Layered MCP Pattern for Task‑Centric Agents"
nav_order: 14
parent: Mcp Dev Summit Eu 2025
type: Video Note
description:
  The speaker introduces the concept of the "layered tool pattern" in API
  and agent design, using Square's platform as a case study. Faced with the challenge
  of enabling an LLM to navigate over 30 APIs and 200 endpoints, the team distilled
  th...
resource: https://www.youtube.com/watch?v=fulofLB7bZk
tags:
  - mcp-dev-summit-eu-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The speaker introduces the concept of the "layered tool pattern" in API and agent design, using Square's platform as a case study.
Faced with the challenge of enabling an LLM to navigate over 30 APIs and 200 endpoints, the team distilled their approach into three core tools: discovery (finding available services), planning (mapping intent to structured requests), and execution (making the API call).
This pattern, demonstrated through a live demo, allowed an agent to autonomously complete complex tasks from a simple prompt by iteratively discovering, planning, and executing actions.
The speaker observes that this layered approach mirrors processes in fields like medicine and the scientific method, emphasizing that simplifying tools to align with human workflows makes agents more effective.
Ultimately, the talk encourages designing tools that reflect how people naturally solve problems, advocating for observation, curiosity, and user-centered design.

# Main Points

|   # | Main point                                                                                                                      |
| --: | ------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Few attendees had read the blog post on the layered tool pattern.                                                               |
|   2 | Emphasized the importance of observation and noticing overlooked details.                                                       |
|   3 | Presenter has been at Block for over eight years, focusing on API design and AI adoption.                                       |
|   4 | Square processes payments and offers business tools; launched APIs in 2015, now has 30+ APIs and 200+ endpoints.                |
|   5 | Faced challenges building an MCP server for the entire platform due to API complexity and overlapping endpoints.                |
|   6 | Creating a tool for each endpoint was unsuccessful; individualized workflows were too complex to analyze.                       |
|   7 | Adopted an approach to create tools to explore the OpenAPI spec, leading to improved task completion with low error rates.      |
|   8 | Developed the layered tool pattern: three main tools—discovery, planning, and execution.                                        |
|   9 | Discovery tool ("get service info") lets the LLM find relevant services and methods.                                            |
|  10 | Planning tool ("get type info") provides type information and request formulation, allowing iterative discovery and planning.   |
|  11 | Execution tool simply makes the API request.                                                                                    |
|  12 | Demo showed the agent using these tools to create and send an invoice from a vague prompt, handling dependencies automatically. |
|  13 | The layered tool pattern mirrors processes in other fields, such as the SOAP method in medicine and the scientific method.      |
|  14 | Similar patterns observed in context engineering, research/planning/execution phases, and developer workflows.                  |
|  15 | The pattern appears in various tech systems, including Goose's extension system, databases, and GitHub's tool segmentation.     |
|  16 | Discovery makes the invisible visible; planning transforms intent into structure; execution performs the action.                |
|  17 | Simpler tools made agents more effective.                                                                                       |
|  18 | Advocated designing APIs for human workflows, as agents mimic human navigation.                                                 |
|  19 | Great tools reflect how people work, not just how things function.                                                              |
|  20 | Encouraged focusing on observation, curiosity, and the discovery-plan-execution cycle.                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=fulofLB7bZk)
