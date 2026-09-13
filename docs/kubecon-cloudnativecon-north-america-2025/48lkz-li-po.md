---
type: Video Note
title: "Lightning Talk: Threat Modeling Kubernetes: Fast, Practical, and LLM-Driven - Maxime Coquerel"
description: "In this talk, Maxim Cochril, a principal cloud security architect at the Royal Bank of Canada, discusses the challenges and solutions in threat modeling for cloud security teams. He explains that traditional threat modeling is essential for..."
resource: https://www.youtube.com/watch?v=48LKZ-lI_po
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Maxim Cochril, a principal cloud security architect at the Royal Bank of Canada, discusses the challenges and solutions in threat modeling for cloud security teams.
He explains that traditional threat modeling is essential for identifying risks and misconfigurations at both the infrastructure and application levels, but it is often time-consuming, difficult to scale, and quickly becomes outdated as systems evolve.
To address these issues, he proposes leveraging a small language model (SLM) with retrieval-augmented generation (RAG) to automate and streamline the process.
By building a knowledge base from previous threat models and benchmarks, and using tools like FIFO and Open Web UI, teams can generate consistent, prioritized threat models more efficiently, reducing the process from weeks to days and enabling easier updates and traceability.
Cochril emphasizes that this solution serves as an assistant to cloud security architects, not a replacement, and invites further discussion and exploration of the approach.
# Main Points

|   # | Main point                                                                                                                                                |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presenter: Maxim Cochril, Principal Cloud Security Architect at Royal Bank of Canada                                                                      |
|   2 | Topic: Threat modeling, specifically fast prototyping and LLM-driven approaches                                                                           |
|   3 | Disclaimer: Opinions expressed are personal, not representative of employer                                                                               |
|   4 | Threat modeling is performed at the design stage to review architecture with stakeholders                                                                 |
|   5 | Goal: Identify potential risks and misconfigurations at the architecture level                                                                            |
|   6 | Uses methodologies such as STRIDE, DREAD, and PASTA                                                                                                       |
|   7 | Purpose: Enables proactive security, focuses efforts on biggest weaknesses, identifies security gaps, and helps prioritize security control development   |
|   8 | Example: Threat modeling in Kubernetes architecture at both infrastructure and application levels                                                         |
|   9 | Major challenge: Cloud security teams struggle to scale threat modeling due to time constraints (often takes 2-3 weeks)                                   |
|  10 | Threat models quickly become outdated as infrastructure evolves                                                                                           |
|  11 | Proposed solution: Lightweight, scalable approach using small language models (SLMs) with retrieval-augmented generation (RAG)                            |
|  12 | Requirements: Ability to inject YAML/JSON/architecture documents, perform threat enumeration, risk prioritization, and provide mitigation recommendations |
|  13 | Consistency in risk scoring and prioritization is important due to varying specialties among architects                                                   |
|  14 | Solution steps:                                                                                                                                           |
|  15 | Build a knowledge base from previous threat models, benchmarks, and guides                                                                                |
|  16 | Expose knowledge base via web UI (e.g., Open Web UI)                                                                                                      |
|  17 | Store information in a vector database (e.g., ChromaDB)                                                                                                   |
|  18 | Chunk documents and run a small language model (e.g., FIFO on Olama)                                                                                      |
|  19 | Expose answers via web UI                                                                                                                                 |
|  20 | Importance of defining a proper system prompt (role, mission, goals, scope, taxonomy)                                                                     |
|  21 | System prompt is open source and available on GitHub                                                                                                      |
|  22 | Knowledge base can scale to thousands of documents                                                                                                        |
|  23 | Cloud security architects can use the system to generate first drafts of threat models, then refine them                                                  |
|  24 | Solution acts as an assistant, not a replacement for architects                                                                                           |
|  25 | Outpu                                                                                                                                                     |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=48LKZ-lI_po)