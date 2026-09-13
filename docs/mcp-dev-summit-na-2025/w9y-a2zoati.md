---
layout: default
title: "[Session] Securing MCP in an Agentic World with Arjun Sambamoorthy from Cisco"
nav_order: 19
parent: Mcp Dev Summit Na 2025
type: Video Note
description:
  Arjun, head of R&D for Cisco's AI security product, discusses the security
  challenges associated with MCP (Model-Connected Plugins) and their intersection
  with AI. He outlines the primary attack surfaces in MCP, including the supply chain...
resource: https://www.youtube.com/watch?v=W9y_a2ZOatI
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

Arjun, head of R&D for Cisco's AI security product, discusses the security challenges associated with MCP (Model-Connected Plugins) and their intersection with AI.
He outlines the primary attack surfaces in MCP, including the supply chain, client-server connections, and the protection of resources.
Arjun details several types of supply chain attacks such as tool poisoning, malicious MCP servers, and compromised setup tools, providing demonstrations of how attackers can exploit tool descriptions and parameters to exfiltrate sensitive data or hijack legitimate tools.
He also explains advanced attack techniques like tool hijacking, shadowing, rugpull attacks, and indirect prompt injection, highlighting the risks of both malicious and accidental data leaks.
To mitigate these threats, Arjun recommends establishing a trusted MCP registry, validating servers, analyzing tool descriptions, monitoring runtime changes, and implementing sandboxes and gateways to enforce security policies and isolate MCP servers.

# Main Points

|   # | Main point                                                                                                                        |
| --: | --------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Arjun heads R&D for Cisco Defense, focusing on AI security products.                                                              |
|   2 | Previously co-founded Autoblocks, acquired by Cisco; background in threat research and security product development.              |
|   3 | The talk covers MCP (Multi-Client Protocol) security challenges and securing MCP.                                                 |
|   4 | MCP introduces new attack surfaces: supply chain, client-server connections, and protection of clients, servers, and resources.   |
|   5 | Supply chain attacks exploit third-party software; SolarWinds cited as a major example.                                           |
|   6 | Three main MCP supply chain attacks:                                                                                              |
|   7 | Tool poisoning: injecting malicious prompts via tool descriptions.                                                                |
|   8 | Malicious MCP servers: installing untrusted or compromised servers.                                                               |
|   9 | Compromised setup tools: installation/configuration tools with injected malicious code.                                           |
|  10 | Tool poisoning is a form of indirect prompt injection, tricking LLMs into unsafe actions.                                         |
|  11 | Tool poisoning tactics include parameter abuse, tool hijacking, tool shadowing, and rugpull attacks.                              |
|  12 | Parameter abuse: exfiltrates LLM data (model name, history, prompts) via tool parameters.                                         |
|  13 | Tool hijacking: malicious tools override legitimate ones, causing data exfiltration or malware downloads.                         |
|  14 | Accidental data leaks can occur if LLMs select the wrong tool due to similar descriptions.                                        |
|  15 | Tool shadowing: malicious tools manipulate legitimate tool behavior (e.g., BCC emails to attacker).                               |
|  16 | Rugpull attack: trusted tools become malicious after approval via server-initiated updates.                                       |
|  17 | Indirect poisoning: malicious web content injects instructions, causing LLMs to perform unintended actions.                       |
|  18 | Sampling feature allows MCP servers to interact with LLMs, increasing risk of prompt injection; human approval is a weak defense. |
|  19 | MCP security recommendations:                                                                                                     |
|  20 | Use a trusted MCP registry for clients and servers.                                                                               |
|  21 | Analyze tool descriptions for poisoning.                                                                                          |
|  22 | Review tool scopes, permissions, and conflicts.                                                                                   |
|  23 | Monitor runtime inputs/outputs and tool list changes.                                                                             |
|  24 | Sandbox and isolate MCP servers.                                                                                                  |
|  25 | Centralized MCP regist                                                                                                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=W9y_a2ZOatI)
