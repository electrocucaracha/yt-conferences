---
layout: default
title: "[Session] Typed Composition with MCP - Solomon Hykes from Dagger"
nav_order: 4
parent: Mcp Dev Summit Na 2025
type: Video Note
description:
  The speaker, co-founder of Dagger.io, introduces their build engine designed
  to generalize and orchestrate software delivery workflows using a container-based,
  DAG-oriented system. They describe how Dagger enables users to compose repeatabl...
resource: https://www.youtube.com/watch?v=1NFfkIEVJbQ
tags:
  - mcp-dev-summit-na-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The speaker, co-founder of Dagger.io, introduces their build engine designed to generalize and orchestrate software delivery workflows using a container-based, DAG-oriented system.
They describe how Dagger enables users to compose repeatable, portable workflows by chaining function calls that manipulate containers, and highlight the system’s compatibility with LLMs due to its immutable, snapshot-based execution model.
The talk demonstrates Dagger’s interactive shell, showing how both users and LLMs can dynamically build and manipulate containers, and discusses the challenges of exposing Dagger’s object-oriented API to LLMs via tool calling, particularly over the MCP protocol, which expects a flat namespace rather than object composition.
The speaker explains their solution of adding an indirection layer to map object methods for LLMs and MCP clients, and invites collaboration on improving object composition and evaluation strategies in this context.
The presentation concludes by emphasizing Dagger’s extensibility and the ongoing work to make complex object composition seamless for LLM orchestration over MCP.

# Main Points

|   # | Main point                                                                                                                           |
| --: | ------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Presenter is co-founder of Dagger.io, a company building a programmable build engine for software delivery workflows.                |
|   2 | Dagger engine is built from first principles using containers, specifically designed for Directed Acyclic Graphs (DAGs).             |
|   3 | The system allows chaining of container operations, similar to Buildkit, but more general and not limited by Dockerfile syntax.      |
|   4 | Dagger provides an API for orchestrating containers and composing repeatable, ephemeral functions into workflows.                    |
|   5 | The platform helps teams make CI/CD workflows more repeatable and portable, enabling local and server-side consistency.              |
|   6 | Open source community has started embedding agentic (LLM-based) functions inside Dagger workflows.                                   |
|   7 | Users requested exposing Dagger’s function composition system over MCP (Model Control Protocol) for integration with external LLMs.  |
|   8 | Dagger supports multiple SDKs (TypeScript, Python, Go, Java) and a command-line interface for interacting with the engine.           |
|   9 | The system returns object references (not just text), enabling further function chaining and object-oriented workflow composition.   |
|  10 | Operations are content-addressed and cached by default, leveraging DAG immutability for efficiency.                                  |
|  11 | Dagger’s execution model aligns with LLM context building, as both are immutable and compositional.                                  |
|  12 | The platform provides sandboxed, ephemeral containers for secure LLM interaction with the environment.                               |
|  13 | Introduced "prompt mode" in the shell, allowing LLMs to use Dagger’s API as tool calls.                                              |
|  14 | All Dagger API functions are automatically exposed to LLMs as tool calls, but tool namespace is flat, posing composition challenges. |
|  15 | Added a layer of indirection (e.g., select methods, list methods) to map object-oriented APIs to MCP’s flat tool namespace.          |
|  16 | Tracing is built-in, allowing users to inspect LLM actions and workflow execution in detail.                                         |
|  17 | Dagger’s MCP integration is functional but not yet documented; uses clients like Goose for MCP compatibility.                        |
|  18 | Main discussion topics: obj                                                                                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=1NFfkIEVJbQ)
