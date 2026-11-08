---
layout: default
title: "Your Agent Sandbox Is Built Backwards - Dan Fernandez, Edera & Ariadne Conill, Edera, Inc."
nav_order: 36
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: 'The presentation, titled "Your Agent Sandbox is Built Backwards," argues that current AI agent sandboxes rely on insecure "subtractive" security models, where broad permissions are granted and then...'
resource: "https://www.youtube.com/watch?v=RPy2bI72lD8"
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

The presentation, titled "Your Agent Sandbox is Built Backwards," argues that current AI agent sandboxes rely on insecure "subtractive" security models, where broad permissions are granted and then manually removed, leading to frequent escape incidents.
Speakers Dan Fernandez and Ariadne advocate for an "additive" approach based on object capabilities, which starts with zero permissions and grants only the specific, unforgeable references required for a task.
This model integrates policy, identity, and runtime enforcement into a single mechanism, allowing for precise, per-call scoping of actions such as API calls or file access.
The talk highlights that while micro-VMs provide strong isolation boundaries, they must be paired with this capability-based authorization to effectively manage egress and prevent token theft.
By adopting this paradigm, organizations can shift from approving every individual action to approving the overall task, thereby reducing the attack surface and improving the security of MCP servers and agentic workloads.

# Main Points

|   # | Main point                                                                                                                     |
| --: | ------------------------------------------------------------------------------------------------------------------------------ |
|   1 | # Key Points                                                                                                                   |
|   2 | : "Your test environment for agents is built backwards"                                                                        |
|   3 | : Product manager at Aderra, instruction associate at Georgia Tech cybersecurity program, former product leader at CrowdStrike |
|   4 | : Main maintainer of Alpine, creator of Wolfi, contributor to Debian and FreeBSD                                               |
|   5 | : demystifying sandboxes and deep dive on object capabilities                                                                  |
|   6 | , especially in runC and Kubernetes namespace-based sandboxes                                                                  |
|   7 | "Sandbox" is an overloaded term conflating policy controls, identity security, and runtime                                     |
|   8 | : self-hosted development, managed development, managed production, and Kubernetes-based                                       |
|   9 | , Firecracker, Kata Containers                                                                                                 |
|  10 | : start from zero and add exactly what agent needs                                                                             |
|  11 | : policy framework, identity, and runtime                                                                                      |
|  12 | , SELinux, cloud allowlists                                                                                                    |
|  13 | : SPIFFE, Wasm, OAuth 2.1, ID Jag                                                                                              |
|  14 | : start with high authority and remove permissions                                                                             |
|  15 | : start from zero using object capability injection pattern                                                                    |
|  16 | : Multics, Hydra, KeyKOS, Eros, seL4, Capsicum, Fuchsia, Gnome                                                                 |
|  17 | : one token per server                                                                                                         |
|  18 | : one capability per tool call with limited scope and task-duration expiration                                                 |
|  19 | : per-call scope, limited scopes per call, tokens expire after task completion                                                 |
|  20 | , not direct egress                                                                                                            |
|  21 | : need more tokens with better delimitation, quick generation, good tool annotations                                           |

# Video

[![Video thumbnail](https://img.youtube.com/vi/RPy2bI72lD8/hqdefault.jpg)]("https://www.youtube.com/watch?v=RPy2bI72lD8")

[Watch on YouTube](https://www.youtube.com/watch?v=RPy2bI72lD8)
