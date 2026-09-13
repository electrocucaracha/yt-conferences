---
layout: default
title:
  Challenges in Delivering Unstructured Content Efficiently Over... Kailas Krivanka
  & Fernando Cerenza
nav_order: 7
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  In this session, Fernando and Kyus from Box discuss their experience
  building the MCP server, focusing on the challenges of moving files and integrating
  AI agents with Box’s intelligent content platform. They explain that Box stores
  vast am...
resource: https://www.youtube.com/watch?v=HrfaijVcOf8
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

In this session, Fernando and Kyus from Box discuss their experience building the MCP server, focusing on the challenges of moving files and integrating AI agents with Box’s intelligent content platform.
They explain that Box stores vast amounts of unstructured data for over 120,000 companies, and the rise of AI presents opportunities for leveraging this data, but also introduces complexities in providing agents with the necessary context while maintaining security and governance.
The team outlines technical hurdles such as inefficient file handling, context window limitations, and the risk of data corruption or exfiltration when agents interact with unstructured content.
They explore solutions like using text-based representations, programmatic tool calling (code mode), and signed URLs to improve tool composability and security, while emphasizing the importance of admin controls, guardrails, and human-in-the-loop mechanisms to mitigate risks like prompt injection and unauthorized data sharing.
Ultimately, they stress the need to balance functionality and security, providing flexible controls for IT admins and users while acknowledging that some risks can only be mitigated, not eliminated.

# Main Points

|   # | Main point                                                                                                                                                        |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Box is an intelligent content platform trusted by over 120,000 companies across various industries.                                                               |
|   2 | Box stores diverse content types, including medical records, product specs, financial documents, and movie scripts.                                               |
|   3 | Customers have unlimited storage, with over an exabyte of data on the platform.                                                                                   |
|   4 | AI agents can leverage stored content to improve business processes, but require context to be effective.                                                         |
|   5 | 90% of enterprise data is unstructured, presenting a significant opportunity for AI-driven automation.                                                            |
|   6 | Box’s platform provides security, privacy, and governance for both human and AI agent workflows.                                                                  |
|   7 | Box supports robust APIs and allows customers to build custom integrations and white-labeled portals.                                                             |
|   8 | The challenge is securely connecting enterprise content to third-party AI agents.                                                                                 |
|   9 | MCP server enables agents to create, query, and edit files, but naive implementations have issues:                                                                |
|  10 | Large files in agent context cause slow performance, high resource usage, and potential data corruption.                                                          |
|  11 | LLMs cannot efficiently process binary content, degrading performance.                                                                                            |
|  12 | Lack of tool composability requires repeated LLM inference for simple operations.                                                                                 |
|  13 | Solutions explored:                                                                                                                                               |
|  14 | Use text or structured representations for read-only use cases.                                                                                                   |
|  15 | Use MCP resources and resource links for supported content types, but with payload and upload limitations.                                                        |
|  16 | Programmatic tool calling (code mode) allows direct tool composability and separation of LLM context from tool execution, but requires client support.            |
|  17 | Signed URLs enable secure file transfers outside the LLM context, but have security implications and require agent shell/network access.                          |
|  18 | Security risks include prompt injection and data exfiltration, especially when agents have access to sensitive data, untrusted input, and external communication. |
|  19 | LLMs cannot distinguish between data and instructions, making them vulnerable to malicious prompt injections.                                                     |
|  20 | Infinite exfiltration vectors exist; any state-chang Ratings (1-5): 3                                                                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=HrfaijVcOf8)
