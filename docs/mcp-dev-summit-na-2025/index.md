---
layout: default
title: "Mcp Dev Summit Na 2025"
has_children: true
nav_order: 13
---

# Mcp Dev Summit Na 2025

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

| Talk Title                                                                                        | Speaker & Organization                                 | Core Thesis & Strategic Insight                                                                                                                                                  |
| :------------------------------------------------------------------------------------------------ | :----------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [MCP Registry: Designing For Server Discovery](ji9ntvx68t0.md)                                    | Tadas A. (PulseMCP), Alex H. (Block), Toby P. (GitHub) | Unveils the official centralized MCP server registry using `server.json` to solve discovery fragmentation and standardize client installation.                                   |
| [[Keynote] MCP201: The Protocol in Depth](c-nqawhsldo.md)                                         | David Soria Parra (Anthropic)                          | Keynote detailing core MCP primitives (prompts, resources, tools, sampling, roots) and outlining the roadmap for remote transport, authorization, and async tasks.               |
| [[Session] Building Protected MCP Servers with MCP](jwdhkwz6v3u.md)                               | Den Delimarsky (Microsoft)                             | Introduces a draft authorization specification and C# SDK that decouples resource and auth servers, enabling off-the-shelf OAuth 2.1 integration.                                |
| [[Session] Building a MCP Server for Agentic Commerce](zkagb-zknni.md)                            | Brenden Lane & Nitin Sharma (PayPal)                   | Demonstrates an MCP server for agentic commerce that enables AI agents to handle end-to-end shopping, payment, MFA, and order tracking securely.                                 |
| [[Session] Building and Deploying Remote MCP Servers](gj2k7tikhxg.md)                             | Dina Kozlov (Cloudflare)                               | Explores serverless deployment of remote MCP servers using Cloudflare Durable Objects, maintaining persistent state and context per user across client apps.                     |
| [[Session] From Experiment to Enterprise: How Block Operationalized MCP at Scale](idwqwdlesgy.md) | Angie Jones (Block)                                    | Shares how Block deployed its Goose agent and 60+ internal MCP servers to 12,000 employees in 2 months, saving engineers 8-10 hours/week and empowering non-engineers.           |
| [[Session] Generating Use Case Specific MCP Servers](hbm5mnoyu7w.md)                              | Josh Dzielak (Postman)                                 | Advocates for generating tailored MCP servers with only necessary API endpoints rather than monolithic servers, reducing token costs and improving LLM performance.              |
| [[Session] Intro to OAuth for MCP Servers](mykmwzcgynw.md)                                        | Aaron Parecki (Okta)                                   | Explains applying OAuth 2.1, protected resource metadata, and dynamic client registration to secure remote MCP servers without compromising client simplicity.                   |
| [[Session] MCP Project Update](emkybhlqam4.md)                                                    | Jerome Swannack (Anthropic)                            | Provides core protocol updates including streamable HTTP transport, upcoming elicitation, tool output schemas, and plans for community-driven open governance.                   |
| [[Session] MCP vs ACP vs A2A: Comparing Agent Protocols](kqb-xml1sfa.md)                          | Laurie Voss (LlamaIndex)                               | Compares 13 agent communication protocols, distinguishing context-oriented protocols like MCP from inter-agent protocols like A2A, highlighting MCP's market leadership.         |
| [[Session] Multi Agent Collaboration in MCP](xrekuebkpaa.md)                                      | Nicholas Aldridge (AWS)                                | Examines modeling multi-agent collaboration over MCP using Spring AI, proposing enhancements for async workflows, stateful resource sharing, and capability discovery.           |
| [[Session] Next Generation Agent Architectures with MCP](z4vgc3lfmym.md)                          | Darren Shepherd (Acorn Labs)                           | Demonstrates how MCP standardizes model-tool connections to simplify complex agent architectures, using declarative prompt/tool definitions and sampling.                        |
| [[Session] Please Make Jarvis So I Don't Have To](sie1xizia4m.md)                                 | Kent C. Dodds (EpicAI.pro)                             | Outlines a vision for seamless, proactive, multimodal personal AI assistants ("Jarvis") powered by MCP, calling for auto-discovery, background tasks, and zero user friction.    |
| [[Session] Pragmatic Scaling of Enterprise GenAI with MCP](usc2xrstxbw.md)                        | Sambhav Kothari (Bloomberg)                            | Details Bloomberg's enterprise GenAI journey, standardizing on MCP to allow 9,000+ engineers to build tools and reducing productionization time from weeks to minutes.           |
| [[Session] Resources: Building the Next Wave of MCP Apps](2jy3z05mspy.md)                         | Shaun Smith (LLMindset)                                | Emphasizes MCP resources and URI schemes over excessive tool calling to optimize token consumption, provide rich MIME-typed semantics, and enable dynamic context updates.       |
| [[Session] Scaling MCP](9t-bbseymy8.md)                                                           | Antje Barth (AWS)                                      | Presents practical AWS architecture patterns for scaling MCP servers from local prototypes to serverless Lambda and Fargate environments using streamable HTTP and SSE.          |
| [[Session] Securing MCP in an Agentic World](w9y-a2zoati.md)                                      | Arjun Sambamoorthy (Cisco)                             | Analyzes MCP security attack vectors—including tool poisoning, hijacking, rugpulls, and indirect prompt injection—advocating for registries, sandboxing, and runtime monitoring. |
| [[Session] Typed Composition with MCP](1nffkievjbq.md)                                            | Solomon Hykes (Dagger)                                 | Discusses bridging Dagger's containerized, object-oriented DAG execution model with MCP's flat tool namespace to enable repeatable, secure workflow composition for LLMs.        |
| [[Session] What MCP Middleware Could Look Like](0wgzne9fcak.md)                                   | Yoko Li (a16z)                                         | Proposes an MCP middleware layer between clients and servers to centralize routing, authentication, rate limiting, error normalization, PII scrubbing, and logging.              |

## Concepts

- [MCP Developers Summit Highlights - May 23, 2025](riiunamm-zy.md) - The speaker expresses enthusiasm about staying current with advancements in MTP, anticipating significant adoption and simplified implementation in the next six months. They highlight the international nature of the conference, noting atten...
- [MCP Registry: Designing For Server Discovery Tadas A. (PulseMCP) Alex H.(Block), and Toby P.(GitHub)](ji9ntvx68t0.md) - The video introduces the official MCP server registry, aiming to consolidate the fragmented ecosystem of MCP server registries by providing a centralized, community-driven solution. The presenters, members of the steering committee from var...
- [[Keynote] MCP201: The Protocol in Depth with David Soria Parra at Anthropic](c-nqawhsldo.md) - In this talk, David, a technical staff member at Anthropic and co-creator of MCP, provides an in-depth overview of the MCP 2011 protocol, highlighting its core primitives—prompts, resources, and tools—and how they enable richer user experie...
- [[Session] Building Protected MCP Servers with MCP - Den Delimarsky from Microsoft](jwdhkwz6v3u.md) - The speaker, a Microsoft engineer, introduces a new draft authorization specification for the Model Context Protocol (MCP), developed collaboratively with the MCP community and partners like Okta and AWS. This specification separates the re...
- [[Session] Building a MCP Server for Agentic Commerce with Brenden Lane and Nitin Sharma from PayPal](zkagb-zknni.md) - In this presentation, Brendan and Nitten from PayPal introduce the MCP server developed for Agentic Commerce, explaining how it enables agents to handle the entire online shopping process—from product discovery and price comparison to check...
- [[Session] Building and Deploying Remote MCP Servers with Dina Kozlov from Cloudflare](gj2k7tikhxg.md) - Dina Coslov, a product manager at Cloudflare, shares her experience working with the engineering team to simplify building MCP (Multi-Client Platform) servers, emphasizing how easy it has become to create remote MCP servers that retain user...
- [[Session] From Experiment to Enterprise: How Block Operationalized MCP at Scale - Angie Jones, Block](idwqwdlesgy.md) - Angie Jones, head of developer relations at Block, describes how the company rapidly scaled its AI-powered agent, Goose, across its 12,000-person workforce in just two months. Initially developed for engineers to automate complex developmen...
- [[Session] Generating Use Case Specific MCP Servers with Josh Dzielak at Postman](hbm5mnoyu7w.md) - Josh Jelik, a staff engineer at Postman, introduces himself and shares his enthusiasm for science fiction and AI agents, leading into a demonstration of building a "time travel agent" using Postman's tools. He discusses three approaches to...
- [[Session] Intro to OAuth for MCP Servers with Aaron Parecki, Okta](mykmwzcgynw.md) - Aaron Pari from Octa discusses the complexities and evolution of OAuth, particularly its application within MCP (Modular Component Platform) servers and clients. He explains that OAuth, originally designed to allow applications to access us...
- [[Session] MCP Project Update with Jerome Swannack, Member of Technical Staff at Anthropic](emkybhlqam4.md) - Jerome Swanik, a member of the core engineering team at Anthropic, introduces himself and shares his journey from aerospace engineering to working on the MCP protocol, motivated by the transformative potential of large language models. He r...
- [[Session] MCP vs ACP vs A2A: Comparing Agent Protocols with Laurie Voss from LlamaIndex](kqb-xml1sfa.md) - Lori, VP of Developer Relations at Llama Index, introduces a rapid overview of agent-to-agent communication protocols, noting that while she initially knew of only three, her research uncovered 13 in total. She distinguishes between context...
- [[Session] Multi Agent Collaboration in MCP with Nicholas Aldridge from AWS](xrekuebkpaa.md) - Nick Aldridge, a principal engineer at AWS, shares his frustrating experience with airline booking systems to illustrate the need for better automation and agent-based interactions. He introduces the concept of inter-agent communication usi...
- [[Session] Next Generation Agent Architectures with MCP with Darren Shepherd from Acorn Labs](z4vgc3lfmym.md) - The speaker, a co-founder at Acorn Labs with a background in automation and orchestration, discusses the challenges of building AI agents and how the MCP (Message Control Protocol) architecture simplifies the process. He explains that while...
- [[Session] Please Make Jarvis So I Don't Have To with Kent C. Dodds from EpicAI.pro](sie1xizia4m.md) - Katy Dods introduces herself as a teacher focused on building MCP servers and shares her vision for the future of AI assistants, inspired by the fictional Jarvis from Iron Man. She emphasizes the importance of a seamless, proactive, and mul...
- [[Session] Pragmatic Scaling of Enterprise GenAI with MCP with Sambhav Kothari at Bloomberg](usc2xrstxbw.md) - Sambukqari, head of AI productivity at Bloomberg, discusses the company's journey in scaling enterprise generative AI (GenAI) development. He outlines Bloomberg's vast operational scale and longstanding AI expertise, noting that the main ch...
- [[Session] Resources: Building the Next Wave of MCP Apps with Shaun Smith, LLMindset](2jy3z05mspy.md) - The speaker discusses their experience integrating with MCP (Modular Communication Protocol), highlighting how MCP servers and tools enable large language models (LLMs) to combine tool calls and generate valuable outputs with minimal coordi...
- [[Session] Scaling MCP with Antje Barth from AWS](9t-bbseymy8.md) - Auntie, a principal developer advocate at AWS, discusses practical approaches to scaling MCP (Model Coordination Protocol) from local prototyping to cloud-scale deployments, focusing on MCP servers. She highlights the growing list of availa...
- [[Session] Securing MCP in an Agentic World with Arjun Sambamoorthy from Cisco](w9y-a2zoati.md) - Arjun, head of R&D for Cisco's AI security product, discusses the security challenges associated with MCP (Model-Connected Plugins) and their intersection with AI. He outlines the primary attack surfaces in MCP, including the supply chain...
- [[Session] Typed Composition with MCP - Solomon Hykes from Dagger](1nffkievjbq.md) - The speaker, co-founder of Dagger.io, introduces their build engine designed to generalize and orchestrate software delivery workflows using a container-based, DAG-oriented system. They describe how Dagger enables users to compose repeatabl...
- [[Session] What MCP Middleware Could Look Like with Yoko Li from A16Z](0wgzne9fcak.md) - Yoko, a partner at Andre and Horwood and an active developer, introduces her work on MCP (Machine Control Protocol) middleware, explaining its role as a horizontal layer between clients and services that centralizes functionalities like aut...
