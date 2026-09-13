---
layout: default
title:
  "Bridging Kernel Space and AI: Building an MCP Server for Linux Scheduler Observabil...
  Daniel Hodges"
nav_order: 2
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  The talk discusses building powerful analysis tools using BPF (Berkeley
  Packet Filter) and MCP (Machine Control Protocol), focusing on simplifying the steep
  learning curve of BPF tooling and enabling conversational, hypothesis-driven invest...
resource: https://www.youtube.com/watch?v=_eMGiEQbSjM
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

The talk discusses building powerful analysis tools using BPF (Berkeley Packet Filter) and MCP (Machine Control Protocol), focusing on simplifying the steep learning curve of BPF tooling and enabling conversational, hypothesis-driven investigations into system performance.
The speaker outlines a step-by-step process for creating a simple MCP tool that captures scheduler events via BPF, aggregates the data in user space, and exposes it through a JSON-based MCP server, highlighting considerations like security, scalability, and permissions.
The presentation then delves into SCXTOP, an advanced MCP tool for analyzing BPF schedulers, which features a modular architecture with multiple ring buffers, event processing layers, and various user interfaces for real-time and trace-based analysis.
Key challenges addressed include handling high-frequency events, tracking tasks reliably, dynamic tracing, and managing permissions, with solutions such as per-CPU counters, task storage maps, and ring buffer sharding.
The speaker concludes by emphasizing best practices for MCP tool development, such as clear BPF lifecycle management, discoverability, topology awareness, and appropriate data storage strategies, and suggests that these approaches can be generalized for broader applications in security, observability, and debugging.

# Main Points

|   # | Main point                                                                                                  |
| --: | ----------------------------------------------------------------------------------------------------------- |
|   1 | Perf events enable advanced analysis and conversational querying of system performance.                     |
|   2 | MCP provides a human-friendly interface for interacting with performance data.                              |
|   3 | BPF tooling has a steep learning curve and requires kernel data model understanding.                        |
|   4 | BPF allows hypothesis-driven investigation and complex, AI-assisted analysis.                               |
|   5 | BPF runs inside the kernel, is JIT-compiled, verified for safety, and offers near-native execution.         |
|   6 | BPF supports core data structures for cross-kernel compatibility.                                           |
|   7 | BPF enables custom kernel instrumentation without modules or reboots.                                       |
|   8 | Plan: build a BPF MCP tool, discuss SCXTOP, address BPF tool challenges and best practices.                 |
|   9 | Simple MCP tool: uses a single tracepoint, one ring buffer, five tools, JSON over stdio, libbpfrs.          |
|  10 | Five steps: define BPF events, write BPF program, set up ring buffers, aggregate data, expose as MCP tools. |
|  11 | Example event: sched_switch, capturing process context switches.                                            |
|  12 | Ring buffer used for kernel-to-user space communication.                                                    |
|  13 | User space consumes ring buffer, aggregates data in a hashmap, exposes via MCP server with endpoints.       |
|  14 | Enable/disable methods load/unload BPF programs to manage overhead.                                         |
|  15 | Security concerns: avoid unsafe AI-generated BPF code; consider permissions and deployment scale.           |
|  16 | SCXTOP aggregates scheduler events, supports TUI, MCP, and trace modes.                                     |
|  17 | Event processing layer decouples TUI, MCP, and trace; supports multiple ring buffers for scalability.       |
|  18 | Advanced views show queue latency, process stats, and context switches.                                     |
|  19 | SCXTOP can generate Perfetto traces for advanced analysis.                                                  |
|  20 | MCP tools support dynamic profiling, live analysis, trace loading, hardware/topology exposure.              |
|  21 | Generic event struct with type field allows multiple event types over one ring buffer.                      |
|  22 | High-frequency events handled with per-CPU counters and map types.                                          |
|  23 | Task storage maps enable per-task tracking; task pointers used for stable identification.                   |
|  24 | Dynamic tracing supported via generic kprobes.                                                              |
|  25 | BPF                                                                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=_eMGiEQbSjM)
