---
layout: default
title:
  "Sponsored Keynote: Scaling Platform Ops with AI Agents: Troubleshooting...
  Jorge Palma & Natan Yellin"
nav_order: 344
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The video discusses the growing integration of AI into daily workflows,
  highlighting the challenges of using multiple tools and the benefits of more fluid,
  integrated solutions. George explains how Acast customers commonly use tools like
  He...
resource: https://www.youtube.com/watch?v=Apha61UYfLY
tags:
  - kubecon-cloudnativecon-europe-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The video discusses the growing integration of AI into daily workflows, highlighting the challenges of using multiple tools and the benefits of more fluid, integrated solutions.
George explains how Acast customers commonly use tools like Headlamp, Home GPT, and GitOps flows with Flux to manage Kubernetes clusters and troubleshoot issues efficiently.
A real-world example is given where an on-call engineer uses Headlamp and Home GPT to quickly diagnose and resolve a typo in a service name, leveraging tools like Inspector Gadget and automating the fix through a pull request and Flux sync.
The process, which previously required manual intervention, is now streamlined and can be completed in about two minutes, including generating a root cause analysis.
The discussion concludes with the introduction of Home GPT's new operator mode, which proactively monitors environments, detects issues as they occur, and promises even greater automation and integration in the future, including potential self-mutating agents and expanded connectivity.

# Main Points

|   # | Main point                                                                                                                        |
| --: | --------------------------------------------------------------------------------------------------------------------------------- |
|   1 | AI is becoming pervasive and is recommended for productivity.                                                                     |
|   2 | Current workflows can be cumbersome due to switching between tools and contexts.                                                  |
|   3 | Common tools among Acast customers include Headlamp (Kubernetes UI), Home GPT (operations/SRE agent), and GitOps flows with Flux. |
|   4 | Example scenario: Contoso pet store user encounters an issue during checkout.                                                     |
|   5 | User opens a ticket; on-call engineer uses Headlamp and Home GPT to investigate.                                                  |
|   6 | Home GPT leverages tools like kubectl and Inspector Gadget to run a TCP dump.                                                     |
|   7 | Issue identified: application calls a non-existent "order-service" instead of the correct "orders-service."                       |
|   8 | AI assistant suggests the fix and prepares a pull request (PR) with a description for incident management.                        |
|   9 | Hotfix is merged; deployment is managed via Flux using the Headlamp Flux plugin.                                                  |
|  10 | The new PR resolves the typo issue and is synced to production.                                                                   |
|  11 | The entire diagnosis, mitigation, and root cause analysis took about 2 minutes.                                                   |
|  12 | AI is used to write the root cause analysis for stakeholders and users.                                                           |
|  13 | Root cause: developer submitted a PR with a typo due to environment mismatch.                                                     |
|  14 | AI is effective at troubleshooting but previously required human intervention to notice issues.                                   |
|  15 | Home GPT now has "operator mode," monitoring the entire cloud environment and connected data sources.                             |
|  16 | Operator mode detects and fixes production issues automatically, often before customers notice.                                   |
|  17 | Home GPT supports connections to MCP servers, HTTP APIs, and databases via generic connectors.                                    |
|  18 | Roadmap includes self-mutating agents and potential integrations, such as with Uber for on-call engineer transport.               |
|  19 | Development of new integrations is streamlined using coding agents and shipped to customers.                                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Apha61UYfLY)
