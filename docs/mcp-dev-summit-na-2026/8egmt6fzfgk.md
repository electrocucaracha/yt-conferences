---
layout: default
title:
  "Securing the MCP Ecosystem: Production Patterns for Transparency... Lisa Tagliaferri
  & Trevor Dunlap"
nav_order: 81
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  In this presentation, Lisa and Trevor from Changuard discuss the evolving
  security challenges in the Model Context Protocol (MCP) ecosystem, highlighting
  the shift from theoretical to real-world threats such as data exfiltration, toolchain...
resource: https://www.youtube.com/watch?v=8eGmT6fZfGk
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

In this presentation, Lisa and Trevor from Changuard discuss the evolving security challenges in the Model Context Protocol (MCP) ecosystem, highlighting the shift from theoretical to real-world threats such as data exfiltration, toolchain attacks, and prompt injection.
They note that existing security tools for MCPs are still maturing, often producing inconsistent or inaccurate results.
Trevor details their approach to securing infrastructure MCPs like MCP Grafana by rebuilding images from source, minimizing dependencies, continuously scanning for vulnerabilities, and providing verifiable provenance and signed artifacts.
Lisa explains the unique risks of content MCPs, where compromised documentation can influence AI assistants at scale, and describes their pipeline controls, including content sanitation, secret scanning, and provenance tracking.
Both emphasize the importance of minimal base images, signed and regularly rebuilt artifacts, and transparent, open-source workflows to strengthen security as the MCP ecosystem rapidly grows.

# Main Points

|   # | Main point                                                                                                                                                                 |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Lisa and Trevor from Changuard discuss securing the MCP ecosystem.                                                                                                         |
|   2 | MCP adoption is growing; major companies like Docker, Red Hat, Microsoft, and OpenAI have MCP catalogs.                                                                    |
|   3 | Security risks have shifted from theoretical to real, with incidents including:                                                                                            |
|   4 | Malicious MCP servers exfiltrating user emails via hidden headers.                                                                                                         |
|   5 | Crosstool data leaks from poisoned tool descriptions.                                                                                                                      |
|   6 | Parasitic tool chain attacks chaining legitimate tools into malicious workflows.                                                                                           |
|   7 | Security tooling is lagging; open-source MCP scanners disagree and generate false positives.                                                                               |
|   8 | Two real implementations are presented: infrastructure MCP (Graphfana) and content MCP (documentation server).                                                             |
|   9 | Docker images are commonly used to run MCP servers but often contain unnecessary dependencies, leading to many vulnerabilities.                                            |
|  10 | Scanning tools like Gripe reveal hundreds of vulnerabilities in base images.                                                                                               |
|  11 | Common threat models include OAuth misconfigurations, overly broad scopes, prompt injection, privilege escalation, and supply chain attacks.                               |
|  12 | Changuard’s approach:                                                                                                                                                      |
|  13 | Rebuild images from source, not trusting upstream binaries.                                                                                                                |
|  14 | Use minimal base images (Wolfi base) to reduce dependency bloat.                                                                                                           |
|  15 | Continuous CVE scanning with a 7-day SLA for critical patches.                                                                                                             |
|  16 | Provide software bill of materials (SBOM) and provenance with signatures.                                                                                                  |
|  17 | Graphfana MCP example: upstream images have 100+ vulnerabilities; Changuard’s rebuilt images have fewer due to direct source builds and patching.                          |
|  18 | Documentation MCP is built from scratch, serving over 2,000 guides, with a different threat profile focused on content influence.                                          |
|  19 | Pipeline: compile docs from four repos, authenticate via workload identity federation, no static credentials, build and sign container images, publish to GitHub registry. |
|  20 | Content MCP risks: malicious instructions in source repos can lead to prompt injection at scale.                                                                           |
|  21 | Defenses:                                                                                                                                                                  |
|  22 | Content sanitation during compilation.                                                                                                                                     |
|  23 | Secret scanning with tuned patterns.                                                                                                                                       |
|  24 | Provenance trac Ratings (1-5): 3                                                                                                                                           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=8eGmT6fZfGk)
