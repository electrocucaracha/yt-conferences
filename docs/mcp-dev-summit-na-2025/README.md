---
layout: default
title: "Executive Report: MCP Dev Summit NA 2025"
parent: "Mcp Dev Summit Na 2025"
nav_order: 1
type: "Executive Report"
okf_version: "0.2"
description: "Executive report and summary of the MCP Dev Summit NA 2025 conference."
tags:
  - mcp-dev-summit-na-2025
  - executive-report
status: stable
---

# Executive Report: MCP Dev Summit NA 2025

## Executive Overview

The MCP Developers Summit NA 2025 brought together protocol co-creators, enterprise leaders, cloud providers, and open-source maintainers to advance the Model Context Protocol (MCP).
Featuring contributions from Anthropic, AWS, Microsoft, Block, Cloudflare, Bloomberg, PayPal, Cisco, Okta, Postman, Dagger, LlamaIndex, a16z, and EpicAI.pro, the summit marked MCP's shift from local developer prototyping to an enterprise-wide standard for agentic systems.
Key milestones unveiled at the summit include the official community-driven MCP Server Registry, a draft OAuth 2.1 authorization specification, streamable HTTP transport, and emerging protocol primitives like elicitation and tool output schemas.
Presentations from Bloomberg and Block demonstrated how standardizing on MCP enables thousands of engineers and non-technical staff to deploy AI tools safely, reducing production integration time from weeks to minutes.
As machine-initiated workloads expand, summit participants emphasized the need for robust security controls against tool poisoning, cloud-native remote deployments, and horizontal middleware to support the next generation of AI agent applications.

## Terminology

- **MCP (Model Context Protocol)**:
  An open standard connecting LLM applications and AI agents to external tools, data resources, and prompt templates.

- **MCP Primitives**:
  The core foundational building blocks of the protocol, comprising user-invoked prompts, application-driven resources, model-invoked tools, client sampling, and workspace roots.

- **Streamable HTTP**:
  The modern HTTP transport protocol replacing Server-Sent Events (SSE) to deliver bidirectional, progressive request-response communication between clients and remote MCP servers.

- **Official MCP Server Registry**:
  A centralized, community-driven registry defined by a `server.json` schema that standardizes server discovery, metadata, and automated client installation.

- **Remote MCP Server**:
  An MCP server hosted on cloud infrastructure (e.g., AWS Lambda, Cloudflare Workers/Durable Objects) accessible over HTTP endpoints with remote token authentication.

- **Tool Poisoning**:
  A class of security attacks (including parameter abuse, tool hijacking, tool shadowing, and rugpulls) where malicious tool descriptions or outputs manipulate LLMs into executing unauthorized actions.

- **MCP Middleware**:
  An infrastructural horizontal layer situated between clients and servers that centralizes routing, authentication, logging, rate-limiting, error normalization, and PII scrubbing.

## Key Themes & Trends

- **Ecosystem Consolidation & Standard Discovery**:
  The launch of the official MCP Server Registry and `server.json` specification addresses fragmenting registries by establishing a single source of truth for server metadata and installation instructions across client applications like Visual Studio Code, Goose, and Raycast.

- **Enterprise Scaling & Operationalization**:
  Major enterprises are scaling MCP internally at impressive volume—Bloomberg has onboarded 9,000+ engineers with plug-and-play tool integration, while Block deployed its Goose agent and 60+ bundled MCP servers to 12,000 employees in two months, saving engineers 8-10 hours weekly.

- **Robust Authorization & Identity Integration**:
  Addressing remote security, the community introduced a draft authorization specification separating resource servers from authorization servers, enabling seamless OAuth 2.1 integration, protected resource metadata, and dynamic client registration with identity providers like Entra ID, Okta, and AWS.

- **Cloud Infrastructure & Serverless Deployments**:
  Remote MCP deployments are moving toward serverless architectures, with Cloudflare leveraging Durable Objects for per-user state retention and AWS providing Lambda and Fargate deployment patterns paired with API Gateways and the Strands agent SDK.

- **Evolving Security & Attack Surface Defense**:
  As tool exposure grows, security researchers identified critical vulnerabilities like tool poisoning, rugpulls, and indirect prompt injection, advocating for registry verification, tool description analysis, sandboxing, and runtime input/output monitoring.

- **Middleware & Architectural Composition**:
  The ecosystem is introducing middleware layers for horizontal concerns (PII reduction, error normalization, rate limiting) and compositional engines like Dagger that map complex object-oriented DAG execution pipelines into MCP tool namespaces.

## Key Takeaways & Strategic Insights

- **Standardize Remote Deployments on Streamable HTTP & OAuth 2.1**:
  Transition remote MCP servers from legacy SSE or STDIO to streamable HTTP and adopt the draft authorization spec to decouple auth servers from resource servers.

- **Optimize Context with Resources and Tailored Tool Bundles**:
  Avoid context bloat and token waste by embedding MIME-typed resources/URIs rather than exposing monolithic tool suites, generating use-case-specific MCP servers for targeted workflows.

- **Implement Defenses Against Tool Poisoning & Supply Chain Attacks**:
  Enforce trusted registry checks, analyze tool descriptions for indirect prompt injection, isolate MCP execution in sandboxes, and monitor runtime tool changes.

- **Prepare Infrastructure for MCP Middleware**:
  Invest in horizontal middleware services to handle cross-cutting requirements—such as token handling, rate limiting, audit logging, PII scrubbing, and error normalization—before scaling agentic workloads.

- **Empower Non-Technical Workforce with Agentic Workflows**:
  Follow enterprise blueprints from Block and Bloomberg by bundling domain-specific MCP tools, providing desktop client interfaces, and simplifying SSO authentication to drive company-wide AI productivity.

## Sessions & Talks Summary

| Talk Title                                                                      | Speaker & Organization                                 | Document                         | Core Thesis & Strategic Insight                                                                                                                                                  |
| :------------------------------------------------------------------------------ | :----------------------------------------------------- | :------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MCP Developers Summit Highlights - May 23, 2025                                 | Conference Highlights                                  | [riiunamm-zy.md](riiunamm-zy.md) | Highlights rapid global momentum, attendance from 30+ countries, and the shift toward simplified auto-generated MCP implementations.                                             |
| MCP Registry: Designing For Server Discovery                                    | Tadas A. (PulseMCP), Alex H. (Block), Toby P. (GitHub) | [ji9ntvx68t0.md](ji9ntvx68t0.md) | Unveils the official centralized MCP server registry using `server.json` to solve discovery fragmentation and standardize client installation.                                   |
| [Keynote] MCP201: The Protocol in Depth                                         | David Soria Parra (Anthropic)                          | [c-nqawhsldo.md](c-nqawhsldo.md) | Keynote detailing core MCP primitives (prompts, resources, tools, sampling, roots) and outlining the roadmap for remote transport, authorization, and async tasks.               |
| [Session] Building Protected MCP Servers with MCP                               | Den Delimarsky (Microsoft)                             | [jwdhkwz6v3u.md](jwdhkwz6v3u.md) | Introduces a draft authorization specification and C# SDK that decouples resource and auth servers, enabling off-the-shelf OAuth 2.1 integration.                                |
| [Session] Building a MCP Server for Agentic Commerce                            | Brenden Lane & Nitin Sharma (PayPal)                   | [zkagb-zknni.md](zkagb-zknni.md) | Demonstrates an MCP server for agentic commerce that enables AI agents to handle end-to-end shopping, payment, MFA, and order tracking securely.                                 |
| [Session] Building and Deploying Remote MCP Servers                             | Dina Kozlov (Cloudflare)                               | [gj2k7tikhxg.md](gj2k7tikhxg.md) | Explores serverless deployment of remote MCP servers using Cloudflare Durable Objects, maintaining persistent state and context per user across client apps.                     |
| [Session] From Experiment to Enterprise: How Block Operationalized MCP at Scale | Angie Jones (Block)                                    | [idwqwdlesgy.md](idwqwdlesgy.md) | Shares how Block deployed its Goose agent and 60+ internal MCP servers to 12,000 employees in 2 months, saving engineers 8-10 hours/week and empowering non-engineers.           |
| [Session] Generating Use Case Specific MCP Servers                              | Josh Dzielak (Postman)                                 | [hbm5mnoyu7w.md](hbm5mnoyu7w.md) | Advocates for generating tailored MCP servers with only necessary API endpoints rather than monolithic servers, reducing token costs and improving LLM performance.              |
| [Session] Intro to OAuth for MCP Servers                                        | Aaron Parecki (Okta)                                   | [mykmwzcgynw.md](mykmwzcgynw.md) | Explains applying OAuth 2.1, protected resource metadata, and dynamic client registration to secure remote MCP servers without compromising client simplicity.                   |
| [Session] MCP Project Update                                                    | Jerome Swannack (Anthropic)                            | [emkybhlqam4.md](emkybhlqam4.md) | Provides core protocol updates including streamable HTTP transport, upcoming elicitation, tool output schemas, and plans for community-driven open governance.                   |
| [Session] MCP vs ACP vs A2A: Comparing Agent Protocols                          | Laurie Voss (LlamaIndex)                               | [kqb-xml1sfa.md](kqb-xml1sfa.md) | Compares 13 agent communication protocols, distinguishing context-oriented protocols like MCP from inter-agent protocols like A2A, highlighting MCP's market leadership.         |
| [Session] Multi Agent Collaboration in MCP                                      | Nicholas Aldridge (AWS)                                | [xrekuebkpaa.md](xrekuebkpaa.md) | Examines modeling multi-agent collaboration over MCP using Spring AI, proposing enhancements for async workflows, stateful resource sharing, and capability discovery.           |
| [Session] Next Generation Agent Architectures with MCP                          | Darren Shepherd (Acorn Labs)                           | [z4vgc3lfmym.md](z4vgc3lfmym.md) | Demonstrates how MCP standardizes model-tool connections to simplify complex agent architectures, using declarative prompt/tool definitions and sampling.                        |
| [Session] Please Make Jarvis So I Don't Have To                                 | Kent C. Dodds (EpicAI.pro)                             | [sie1xizia4m.md](sie1xizia4m.md) | Outlines a vision for seamless, proactive, multimodal personal AI assistants ("Jarvis") powered by MCP, calling for auto-discovery, background tasks, and zero user friction.    |
| [Session] Pragmatic Scaling of Enterprise GenAI with MCP                        | Sambhav Kothari (Bloomberg)                            | [usc2xrstxbw.md](usc2xrstxbw.md) | Details Bloomberg's enterprise GenAI journey, standardizing on MCP to allow 9,000+ engineers to build tools and reducing productionization time from weeks to minutes.           |
| [Session] Resources: Building the Next Wave of MCP Apps                         | Shaun Smith (LLMindset)                                | [2jy3z05mspy.md](2jy3z05mspy.md) | Emphasizes MCP resources and URI schemes over excessive tool calling to optimize token consumption, provide rich MIME-typed semantics, and enable dynamic context updates.       |
| [Session] Scaling MCP                                                           | Antje Barth (AWS)                                      | [9t-bbseymy8.md](9t-bbseymy8.md) | Presents practical AWS architecture patterns for scaling MCP servers from local prototypes to serverless Lambda and Fargate environments using streamable HTTP and SSE.          |
| [Session] Securing MCP in an Agentic World                                      | Arjun Sambamoorthy (Cisco)                             | [w9y-a2zoati.md](w9y-a2zoati.md) | Analyzes MCP security attack vectors—including tool poisoning, hijacking, rugpulls, and indirect prompt injection—advocating for registries, sandboxing, and runtime monitoring. |
| [Session] Typed Composition with MCP                                            | Solomon Hykes (Dagger)                                 | [1nffkievjbq.md](1nffkievjbq.md) | Discusses bridging Dagger's containerized, object-oriented DAG execution model with MCP's flat tool namespace to enable repeatable, secure workflow composition for LLMs.        |
| [Session] What MCP Middleware Could Look Like                                   | Yoko Li (a16z)                                         | [0wgzne9fcak.md](0wgzne9fcak.md) | Proposes an MCP middleware layer between clients and servers to centralize routing, authentication, rate limiting, error normalization, PII scrubbing, and logging.              |
