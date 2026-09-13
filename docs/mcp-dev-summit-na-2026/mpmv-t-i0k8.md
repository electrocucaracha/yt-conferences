---
layout: default
title:
  "Shadow MCP: Finding the MCPs Nobody Approved - Aidan Sochowski & Alexander
  Frazer, Runlayer"
nav_order: 82
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  In this talk, Alex and Aiden discuss the security challenges posed by
  "shadow MCPs"—unapproved Model Control Protocol servers and AI tools proliferating
  within organizations without oversight. They explain that these tools, often configured...
resource: https://www.youtube.com/watch?v=mpmV_t-i0K8
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

In this talk, Alex and Aiden discuss the security challenges posed by "shadow MCPs"—unapproved Model Control Protocol servers and AI tools proliferating within organizations without oversight.
They explain that these tools, often configured by end users and stored as unencrypted text files or embedded in codebases, are largely invisible to traditional security and inventory systems, making them difficult to detect and govern.
The speakers outline several attack vectors, including rugpulls, tool poisoning, supply chain compromises, and context or skill injection, all of which are exacerbated by the lack of visibility and control over shadow MCPs.
Existing security tools like EDR and network monitoring are insufficient for detecting these threats, as they lack the necessary granularity and are easily evaded.
The presenters advocate for device-level scanning and classification, risk scoring, and behavioral analysis to identify and manage shadow MCPs, emphasizing the need for organizational policies, managed infrastructure, and ongoing vigilance to balance security with user productivity.
They conclude by noting that while technical solutions exist, the problem is complex and evolving, requiring both technical and organizational responses.

# Main Points

|   # | Main point                                                                                                                                                                      |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation titled "Shadow MCP, finding the MCPs Nobody approved"                                                                                                              |
|   2 | Agenda: problem breakdown (Aiden), attacks/discovery/classification (Alex), response/summary (Aiden)                                                                            |
|   3 | Speakers' backgrounds: security engineering, AI security tooling, product engineering, experience with AI models and infrastructure                                             |
|   4 | Enterprises are rapidly adopting AI tools and MCP servers, often without oversight or governance                                                                                |
|   5 | Shadow MCPs and AI tools are often unmanaged, invisible to inventory tools, and stored as unencrypted text files                                                                |
|   6 | Risks are higher due to AI automation, lack of auditability, and difficulty in detection                                                                                        |
|   7 | Credentials for MCP servers are often overprovisioned and stored insecurely, increasing risk of compromise                                                                      |
|   8 | Common attack patterns:                                                                                                                                                         |
|   9 | Rugpulls: trusted MCP servers become malicious after approval                                                                                                                   |
|  10 | Tool poisoning: prompt injection via data sources (e.g., GitHub issues)                                                                                                         |
|  11 | Supply chain attacks: compromised packages (e.g., Axios, light LLM) distribute malware                                                                                          |
|  12 | Data exfiltration: agents instructed to leak sensitive data                                                                                                                     |
|  13 | Context poisoning, persistence, and skill injection: corrupting agent context, adding hidden persistence, or modifying skills for malicious purposes                            |
|  14 | Shadow MCPs are under-prioritized in security rankings; lack of observability is a core issue                                                                                   |
|  15 | Existing security tools (network monitoring, EDR/XDR) are insufficient for detecting shadow MCPs and skills due to encryption, lack of file monitoring, and distributed storage |
|  16 | Effective detection requires scanning devices directly, collecting and classifying config and skill files at scale and frequently                                               |
|  17 | Classification and risk scoring are necessary due to volume and complexity of files                                                                                             |
|  18 | Response strategies:                                                                                                                                                            |
|  19 | Bring shadow MCPs under management rather than banning                                                                                                                          |
|  20 | Evaluate tool prevalence and risk, set policies, and balance security with user friction                                                                                        |
|  21 | Use version pinning, managed infrastructure (gateways/proxies), and credential rotation                                                                                         |
|  22 | Observe and classify all tools and client                                                                                                                                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=mpmV_t-i0K8)
