---
layout: default
title:
  "Wasm't That Easy: Securing MCP With Wasm Sandboxes - Jiaxiao Zhou, Microsoft
  & Taylor Thomas, Akuity"
nav_order: 18
parent: Cloud Native Kubernetes Ai Day 2025 Na
type: Video Note
description:
  In this talk, Joe from Microsoft Azure and Taylor from Acuy discuss the
  security risks associated with running MCP (Machine Control Protocol) servers and
  tools, particularly when users copy and run arbitrary binaries or scripts from untrust...
resource: https://www.youtube.com/watch?v=fSSjxqx7cCg
tags:
  - cloud-native-kubernetes-ai-day-2025-na
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

In this talk, Joe from Microsoft Azure and Taylor from Acuy discuss the security risks associated with running MCP (Machine Control Protocol) servers and tools, particularly when users copy and run arbitrary binaries or scripts from untrusted sources.
Through live demonstrations, they show how both direct execution and containerization can still lead to secret exfiltration due to issues like tool poisoning and insufficient sandboxing, even when best practices are followed.
They introduce WebAssembly (WASM) and its component model as a more secure alternative, highlighting its strong typing, introspectability, and deny-by-default sandboxing, which allows for granular permission controls and easier static analysis of components.
Their open source project, Waset, leverages these WASM features to securely run MCP tools, blocking unauthorized network access and exfiltration attempts by default.
The presenters encourage the community to try out Waset, contribute to the WASM ecosystem, and join discussions on improving security practices for MCP and related tooling.

# Main Points

|   # | Main point                                                                                                                                                      |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Many users copy-paste MVX or UVX commands from MCP readmes without reviewing them.                                                                              |
|   2 | AI agents can easily leak secrets if tools are run without proper sandboxing.                                                                                   |
|   3 | The talk demonstrates how to lock down MCP tools in a Wen sandbox with a deny-by-default policy.                                                                |
|   4 | Common practice: running MCP servers or tools with "dangerously skip permissions" (YOLO mode), which skips approval and increases risk.                         |
|   5 | Demo 1: Running an MCP server with YOLO mode can lead to SSH key exfiltration by arbitrary binaries.                                                            |
|   6 | Demo 2: Running MCP in a container with best practices (read-only, non-root) still allows secret exfiltration via tool poisoning, exploiting LLM's file access. |
|   7 | Tool poisoning: Malicious tool descriptions can trick LLMs into leaking secrets, even if the server is locked down.                                             |
|   8 | WASM (WebAssembly) and the component model offer a strongly-typed, portable, and introspectable alternative for running tools.                                  |
|   9 | WASM components use WIT (WebAssembly Interface Types) for defining types and functions, enabling static analysis and sandboxing.                                |
|  10 | WASM components can be denied capabilities (e.g., network access) at runtime, blocking malicious behavior.                                                      |
|  11 | The component model allows granular permission control, including allow-lists for network access.                                                               |
|  12 | Waset is an open-source project that wraps WASM components for MCP, providing deny-by-default sandboxing and granular policies.                                 |
|  13 | WASM components can be distributed as OCI artifacts, leveraging existing supply chain security tools.                                                           |
|  14 | Static typing and introspection in WASM components help prevent common exfiltration and access issues.                                                          |
|  15 | The approach encourages moving from arbitrary binaries to composable, sandboxed tools.                                                                          |
|  16 | Adoption of the component model requires some effort but enables cross-language tool composition and safer execution.                                           |
|  17 | Community involvement is encouraged; users can try Waset, contribute to the WASM ecosystem, and join the MCP security group.                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=fSSjxqx7cCg)
