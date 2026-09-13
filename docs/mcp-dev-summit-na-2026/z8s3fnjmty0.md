---
layout: default
title:
  "Interceptors for MCP: A Production-Tested Standard for Agentic Middl... Kurt
  Degiorgio & Cannis Chan"
nav_order: 39
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  In this presentation, Kurt and Canis from Bloomberg introduce "interceptors,"
  a proposed extension to the Model Context Protocol (MCP) designed to address the
  need for standardized context governance in agentic AI systems, particularly in
  h...
resource: https://www.youtube.com/watch?v=z8s3fNjMtY0
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

In this presentation, Kurt and Canis from Bloomberg introduce "interceptors," a proposed extension to the Model Context Protocol (MCP) designed to address the need for standardized context governance in agentic AI systems, particularly in highly regulated environments like financial services.
They explain that while MCP has enabled standardized connections between agents and tools, it lacks built-in mechanisms for verifying and controlling data as it moves across trust boundaries, leading to fragmented, custom solutions.
Interceptors elevate middleware to a protocol-level primitive, allowing for standardized validation (validators) and transformation (mutators) of context both on the client and server sides.
Practical examples include using validators to ensure AI-generated responses are properly cited and mutators to inject real-time market context into user queries, thereby enhancing trust, transparency, and relevance in Bloomberg’s conversational AI interface, ASPI.
The presenters emphasize that interceptors provide a plug-and-play framework for enforcing governance and shaping context throughout the agentic lifecycle, and invite the community to contribute to the ongoing development and standardization of this approach.

# Main Points

|   # | Main point                                                                                                                                                                     |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Interceptors are a proposed extension to the model context protocol (MCP) to provide verification and control between models and data.                                         |
|   2 | Bloomberg operates in a highly regulated financial environment where compliance and governance are essential.                                                                  |
|   3 | Current MCP standardizes context operations but lacks standardized context governance.                                                                                         |
|   4 | Enterprises need control points to verify and enforce policies when AI acts across trusted and untrusted environments.                                                         |
|   5 | Existing solutions for context governance are fragmented and non-reusable, leading to integration complexity.                                                                  |
|   6 | Interceptors elevate middleware to a first-class MCP primitive, alongside tools, prompts, and resources.                                                                       |
|   7 | Interceptors can hook into any standardized event, are discoverable, and invocable via JSON RPC.                                                                               |
|   8 | Interceptors can be executed by both client and server for requests and responses.                                                                                             |
|   9 | Two types of interceptors: validators (non-mutating, inspect and decide) and mutators (transform payloads).                                                                    |
|  10 | Validators answer: "Is this safe?" and can block or allow requests based on policy checks.                                                                                     |
|  11 | Mutators answer: "Make this safe," transforming data to comply with policies before crossing trust boundaries.                                                                 |
|  12 | Validators and mutators can be composed to protect both ends of the trust boundary.                                                                                            |
|  13 | Execution order: sending data—mutate, validate, send; receiving data—validate, mutate, process.                                                                                |
|  14 | Mutations are atomic; if any mutator fails, all changes are rolled back.                                                                                                       |
|  15 | Bloomberg uses interceptors in their conversational AI interface (ASPI) on the Bloomberg Terminal.                                                                             |
|  16 | Validator interceptors ensure LLM outputs are backed by real citations and valid data before being shown to users.                                                             |
|  17 | Mutator interceptors enrich user queries with real-time context before LLM processing, ensuring timely and relevant responses.                                                 |
|  18 | Interceptors support transparency, trust, and compliance in AI-powered workflows.                                                                                              |
|  19 | Community is encouraged to review SE 1764, try implementations, join discussions, and contribute.                                                                              |
|  20 | Validators and mutators are co Notes: - Interceptors are a proposed extension to the model context protocol (MCP) to provide verification and control between models and data. |
|  21 | Two types of interceptors: validators (non-mutating, inspect and decide) and mutators (transform payloads).                                                                    |
|  22 | Validators answer: "Is this safe?" and can block or allow requests based on policy checks.                                                                                     |
|  23 | Mutators answer: "Make this safe," transforming data to comply with policies before crossing trust boundaries. Ratings (1-5): 4                                                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=z8s3fNjMtY0)
