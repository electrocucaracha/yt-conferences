---
layout: default
title: "Executive Report: MCP Dev Summit EU 2025"
parent: "Mcp Dev Summit Eu 2025"
nav_order: 1
type: "Executive Report"
okf_version: "0.2"
description: "Executive report and summary of the MCP Dev Summit EU 2025 conference."
tags:
  - mcp-dev-summit-eu-2025
  - executive-report
status: stable
---

# Executive Report: MCP Dev Summit EU 2025

## Executive Overview

The MCP Dev Summit EU 2025 in London brought together AI architects, protocol maintainers, enterprise developers, and platform leaders to examine the rapid maturation of the Model Context Protocol (MCP).
Featuring keynotes and technical sessions from Anthropic, Bloomberg, Amazon Web Services, Google Chrome DevTools, Shopify, Block, WorkOS, Grafana Labs, Hugging Face, Platformatic, and Tetrate, the conference highlighted MCP's transition from a novel open-source specification into a foundational infrastructure layer for enterprise AI.
As the ecosystem reaches over 10,000 public and private MCP servers, community attention has turned toward production readiness, enterprise security, protocol standardization, and rich interactive user experiences.
Organizations are moving beyond basic API wrappers toward stateful, workflow-driven MCP agents, native asynchronous execution (SEP 1391), zero-trust authentication gateways, and dynamic UI component rendering (MCP-UI).
Simultaneously, enterprise leaders in financial services, retail, and travel are embedding MCP into core operations to ground generative AI in real-time context while maintaining strict compliance, observability, and data entitlements.

## Terminology

- **Model Context Protocol (MCP)**:
  An open standard enabling large language models and autonomous agents to securely access digital tools, enterprise databases, and interactive UI components.

- **Asynchronous Tool Calling (SEP 1391)**:
  A protocol extension introducing native task tokens and RPC methods for non-blocking, long-running agent workflows like code migration and molecular analysis.

- **MCP Profiles**:
  Server-declared policy configurations identified by unique URLs that mandate specific authentication, token durations, or enterprise compliance requirements.

- **MCP-UI**:
  An open protocol permitting MCP servers to transmit sandboxed, interactive UI components directly into AI chat environments.

- **MCP Registry (`server.json`)**:
  A community-driven, decentralized specification and REST API for publishing, discovering, and federating MCP server capabilities across organizations.

- **Layered Tool Pattern**:
  An agent tool architecture that condenses complex multi-API domains into three structured phases: discovery, planning, and execution.

- **Sampling & Elicitation**:
  Core protocol capabilities allowing agent-to-agent context requests (sampling) and agent-to-human clarification prompts (elicitation).

- **Dynamic MCPs (DMCPs) & Serlets**:
  Context-aware virtual servers that dynamically inject or revoke tools based on active tasks to prevent context window bloat and tool overload.

## Key Themes & Trends

- **Enterprise Security, Authorization, and Zero-Trust Gateways**:
  Transitioning MCP from developer local desktops to corporate networks requires robust authorization.
  Industry leaders are implementing zero-trust AI gateways (Pomerium, HyperMCP, Amboy) and adopting client metadata specifications (SEP 9991) to replace fragile Dynamic Client Registration (DCR).
  Financial leaders (Bloomberg, Saxo Bank, Evergreen Wealth) emphasized enforcing granular data entitlements, audit logging, and step-up authentication across automated agent interactions.

- **Protocol Scalability, Asynchronous Execution, and Stateless Transports**:
  Synchronous tool calls introduce significant latency and operational bottlenecks for complex tasks.
  The introduction of native asynchronous tool semantics (SEP 1391) enables tools to run in the background while returning progress tokens.
  Additionally, production deployments at Hugging Face and Platformatic highlight a shift toward default stateless HTTP streamable transport and server-side state persistence (e.g. Redis) to ensure multi-threaded scaling.

- **Workflow-Centric Agents and Multi-Agent Collaboration**:
  Exposing raw, fine-grained REST endpoints directly to LLMs causes decision fatigue and prompt bloat.
  Engineers from Square, Tomorrow AI, and Obot AI advocated for layered tool patterns and workflow-centric agent design.
  Leveraging protocol primitives like sampling and elicitation allows autonomous agents (MAMU, Nanobot) to coordinate multi-user workspaces, execute complex multi-step pipelines, and request human-in-the-loop approvals when required.

- **Tool Overload Mitigation and Graph-Based Discovery**:
  As available tools expand into thousands, static tool injection degrades LLM reasoning and inflates token costs.
  Solutions like MCPZ "serlets", graph-based tool selection algorithms, and dynamic MCPs (DMCPs) filter tools based on centrality, cost, and active context.
  Concurrently, the open-source MCP Registry (`server.json`) enables federated, decentralized server discovery across public and enterprise subregistries.

- **Interactive User Interfaces and Embedded Components (MCP-UI)**:
  Text-only chat responses are insufficient for complex domains like ecommerce, travel, and developer tooling.
  Shopify, Postman, and Goose demonstrated MCP-UI, sending sandboxed, brand-consistent HTML/React widgets directly to chat clients.
  Users can browse products, manage shopping carts, inspect DevTools, and authorize transactions interactively inside the agent interface.

- **Observability, Vetting, and Quality Assurance**:
  Operating enterprise agent fabrics demands comprehensive monitoring and security vetting.
  Platforms like Numa Labs/Natoma perform automated static analysis to detect prompt injection and tool poisoning before servers are published.
  Furthermore, Grafana Labs demonstrated protocol-level performance testing using K6, enabling continuous integration pipelines to simulate soak and spike tests across MCP connections.

## Key Takeaways & Strategic Insights

- **Architect for Workflows, Not Raw Endpoints**:
  Avoid exposing raw database tables or hundreds of API endpoints directly to models.
  Implement the layered tool pattern (discovery, planning, execution) or workflow servers to streamline model reasoning and lower execution costs.

- **Adopt Zero-Trust Identity and Gateway Architecture**:
  Centralize authentication, rate limiting, and observability using identity-aware AI gateways (Pomerium, HyperMCP).
  Decouple authentication logic from individual MCP server implementations to ensure enterprise compliance.

- **Implement Dynamic Context and Graph-Based Tool Routing**:
  Utilize dynamic toolboxes (serlets) or graph-based tool selection to inject only relevant tools into the active context window, reducing token expense by up to 95%.

- **Prepare for Asynchronous and Stateless Operations**:
  Design new MCP tools around asynchronous task tokens (SEP 1391) and stateless HTTP transports to support long-running enterprise processes and horizontal scaling.

- **Enhance User Engagement with Interactive UI (MCP-UI)**:
  Integrate MCP-UI to deliver rich, domain-specific UI components within chat clients, transforming text assistants into interactive applications.

## Sessions & Talks Summary

| Talk Title                                                                                           | Speaker & Organization                  | Document                                                                                 | Core Thesis & Strategic Insight                                                                                                                               |
| :--------------------------------------------------------------------------------------------------- | :-------------------------------------- | :--------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Highlights from MPC Dev Summit EU 2025 - London - 2 Oct 2025                                         | Community Presenter                     | [docs/mcp-dev-summit-eu-2025/rojxsfwkftw.md](docs/mcp-dev-summit-eu-2025/rojxsfwkftw.md) | Summarizes developer community growth, note-taking features, and the expected transition toward client-side specification stability.                          |
| Multi-Agent Multi-User Collab thru MCP: Enabling Asynchronous Human-Agent Agent-Human Workflows      | Andrew Culverson & Mun Burid            | [docs/mcp-dev-summit-eu-2025/feqgd-m-p5e.md](docs/mcp-dev-summit-eu-2025/feqgd-m-p5e.md) | Demonstrates MAMU, leveraging sampling and elicitation for multi-agent, multi-user workspaces with asynchronous collaboration and human approvals.            |
| [Session] Scaling MCP Observability: How Natoma Monitors Thousands of MCP Servers                    | Capil (Numa Labs)                       | [docs/mcp-dev-summit-eu-2025/09orzbzc3au.md](docs/mcp-dev-summit-eu-2025/09orzbzc3au.md) | Outlines enterprise observability, static code vetting for prompt injection, and detailed activity logging across thousands of hosted MCP servers.            |
| [Session] Asynchronous Tool Calling with Nick Aldridge - Amazon Web Services                         | Nick Aldridge (AWS)                     | [docs/mcp-dev-summit-eu-2025/2q6o1b-lcew.md](docs/mcp-dev-summit-eu-2025/2q6o1b-lcew.md) | Introduces SEP 1391 for native asynchronous tool calling, establishing task tokens and RPC methods for non-blocking enterprise workflows.                     |
| [Session] What are Profiles? A Proposed Foundational Feature of MCP Servers                          | Standards Working Group                 | [docs/mcp-dev-summit-eu-2025/5hasfiwob2g.md](docs/mcp-dev-summit-eu-2025/5hasfiwob2g.md) | Proposes MCP Profiles to allow organizations to declare and negotiate specific authentication, security, and compliance requirements during connection setup. |
| [Session] From Embeddings to Edges: A Graph Based Approach to Tool Selection                         | Tooling Architecture Team               | [docs/mcp-dev-summit-eu-2025/5nfohwawvgm.md](docs/mcp-dev-summit-eu-2025/5nfohwawvgm.md) | Presents a graph-based tool selection framework representing tools as nodes and edges to improve selection accuracy and reduce context bloat.                 |
| [Session] Improving Agentic Search with MCP Sessions with Matt Dailey - Ref                          | Matt Dailey (Ref)                       | [docs/mcp-dev-summit-eu-2025/cgki4v11sps.md](docs/mcp-dev-summit-eu-2025/cgki4v11sps.md) | Demonstrates stateful MCP sessions for document search, achieving up to 95% token savings through prefetching and context chunking.                           |
| [Session] One Test a Day Keeps the Issues Away with Oleksandr Kotov - Grafana Labs                   | Oleksandr Kotov (Grafana Labs)          | [docs/mcp-dev-summit-eu-2025/d3peufcbhqq.md](docs/mcp-dev-summit-eu-2025/d3peufcbhqq.md) | Details performance testing for MCP servers using K6 and Grafana to simulate load, identify bottlenecks, and enforce CI quality thresholds.                   |
| [Session] MCP Registry: The Path To (De-)Centralizing Discovery                                      | Tatis & Toby (MCP Registry Maintainers) | [docs/mcp-dev-summit-eu-2025/dqnolgpndq4.md](docs/mcp-dev-summit-eu-2025/dqnolgpndq4.md) | Explains the open-source `server.json` specification and subregistry architecture enabling federated server discovery across organizations.                   |
| [Keynote] Building an AI Voice Agent to Automate a Robot Cafe with Google Gemini Live and MCP        | Gerard Sans (Google Developer Expert)   | [docs/mcp-dev-summit-eu-2025/eqrdy42vwma.md](docs/mcp-dev-summit-eu-2025/eqrdy42vwma.md) | Demonstrates building a real-time multilingual AI voice agent integrating Google Gemini Live and MCP to automate robot cafe operations.                       |
| [Session] Building Scalable MCP Servers with Node with Matteo Colina - Platformatic.dev              | Matteo Colina (Platformatic.dev)        | [docs/mcp-dev-summit-eu-2025/eresuo6n5zq.md](docs/mcp-dev-summit-eu-2025/eresuo6n5zq.md) | Introduces `@platformatic/mcp` for stateful, Redis-backed Node.js MCP servers supporting session resumability and OAuth 2.1 integration.                      |
| [Session] Tools, Not Endpoints: The Layered MCP Pattern for Task‑Centric Agents                      | Square Platform Engineering             | [docs/mcp-dev-summit-eu-2025/fuloflb7bzk.md](docs/mcp-dev-summit-eu-2025/fuloflb7bzk.md) | Proposes the layered tool pattern (discovery, planning, execution) to distill extensive API catalogs into intuitive agent capabilities.                       |
| [Roundtable] Why Financial Services Companies are Investing in MCP                                   | Evergreen Wealth, Bloomberg, Saxo Bank  | [docs/mcp-dev-summit-eu-2025/gkpr538mjd0.md](docs/mcp-dev-summit-eu-2025/gkpr538mjd0.md) | Discusses enterprise MCP adoption in financial services, focusing on regulatory compliance, data entitlements, and structured outputs.                        |
| [Session] Too Many Tools: Surviving the MCP Tool Overload with Shalev Shalit - Webrix                | Shalev Shalit (Webrix)                  | [docs/mcp-dev-summit-eu-2025/hjy04dv-o7u.md](docs/mcp-dev-summit-eu-2025/hjy04dv-o7u.md) | Evaluates strategy patterns for mitigating tool overload, including dynamic MCPs (DMCPs), search-and-call methods, and role-tailored toolkits.                |
| [Session] Moving Past Simple MCP Tools to MCP Agents with Darren Shepherd - Obot AI                  | Darren Shepherd (Obot AI)               | [docs/mcp-dev-summit-eu-2025/irgmqmjwdna.md](docs/mcp-dev-summit-eu-2025/irgmqmjwdna.md) | Introduces Nanobot, encapsulating MCP hosts as conversational agents within servers to deliver controlled, multimodal user experiences.                       |
| [Session] Do You Need an AI Gateway with Ignasi Barrera - Tetrate                                    | Ignasi Barrera (Tetrate)                | [docs/mcp-dev-summit-eu-2025/jbehnvunf2m.md](docs/mcp-dev-summit-eu-2025/jbehnvunf2m.md) | Presents the Amboy AI Gateway for managing security, policy enforcement, rate limiting, and observability across LLM and MCP traffic.                         |
| [Session] Let's dream big for MCP Auth with Tobin South - WorkOS                                     | Tobin South (WorkOS)                    | [docs/mcp-dev-summit-eu-2025/jpee-ge5olm.md](docs/mcp-dev-summit-eu-2025/jpee-ge5olm.md) | Explores authorization architecture for autonomous agents, covering backchannel auth, step-up prompts, and enterprise SSO/SAML integration.                   |
| [Session] Beyond API Wrappers: Workflow-Based MCP Servers with Elicitation and Sampling              | Tom McLolin (Tomorrow AI)               | [docs/mcp-dev-summit-eu-2025/jupodqwmymu.md](docs/mcp-dev-summit-eu-2025/jupodqwmymu.md) | Recommends workflow-oriented MCP servers leveraging progressive disclosure, elicitation, and sampling to guide complex user tasks.                            |
| [Keynote] Revolutionizing Travel with AI How We Built the Turkish Airlines MCP                       | Turkish Airlines Technology Team        | [docs/mcp-dev-summit-eu-2025/kwvkpfnhwlm.md](docs/mcp-dev-summit-eu-2025/kwvkpfnhwlm.md) | Details Turkish Airlines' enterprise MCP server implementation for conversational flight booking, promotions, and frequent flyer OAuth 2.1 auth.              |
| [Session] Lessons Learned Building the Chrome DevTools MCP Server                                    | Jack (Google Chrome DevTools)           | [docs/mcp-dev-summit-eu-2025/lryv4stcyac.md](docs/mcp-dev-summit-eu-2025/lryv4stcyac.md) | Shares lessons from Google's official Chrome DevTools MCP server, advocating for granular composable actions over rigid high-level tools.                     |
| [Keynote] MCP Project Update with David Soria Parra - Anthropic                                      | David Soria Parra (Anthropic)           | [docs/mcp-dev-summit-eu-2025/oaebrdfuhi.md](docs/mcp-dev-summit-eu-2025/oaebrdfuhi.md)   | Delivers Anthropic's state of the MCP project update, highlighting ecosystem scale (10,000+ servers), async tasks, and client metadata specs.                 |
| [Session] Effortless User Onboarding with MCP with Pedro Rodrigues - SingleStore                     | Pedro Rodrigues (SingleStore)           | [docs/mcp-dev-summit-eu-2025/ojglgebvdbs.md](docs/mcp-dev-summit-eu-2025/ojglgebvdbs.md) | Shows how SingleStore uses remote MCP servers with Markdown guides and prompt templates to accelerate developer onboarding for LLMs.                          |
| [Session] Streams, Sessions, Stats Transport and Client Behaviour in Practice                        | Sean Smith (Hugging Face)               | [docs/mcp-dev-summit-eu-2025/osoex7jy0m4.md](docs/mcp-dev-summit-eu-2025/osoex7jy0m4.md) | Analyzes streamable HTTP transport production traffic at Hugging Face, advising default statelessness for reliable horizontal scaling.                        |
| [Keynote] Engineering the Future-Making MCP Enterprise Ready for Finance - Shawn Edwards, Bloomberg  | Shawn Edwards (Bloomberg)               | [docs/mcp-dev-summit-eu-2025/p9xcmpmuam4.md](docs/mcp-dev-summit-eu-2025/p9xcmpmuam4.md) | Details Bloomberg's adoption of agentic AI and MCP to ground financial applications in trusted, real-time market data with enterprise governance.             |
| [Session] MCP & Contextual Smart Tooling with Jason Kneen - BouncingFish                             | Jason Kneen (BouncingFish)              | [docs/mcp-dev-summit-eu-2025/s413hw1hxou.md](docs/mcp-dev-summit-eu-2025/s413hw1hxou.md) | Introduces MCPZ CLI and "serlets" to generate task-specific virtual servers that dynamically load tools and eliminate prompt bloat.                           |
| [Session] MCP-UI: Next-gen Agentic Experiences                                                       | MCP-UI Core Team                        | [docs/mcp-dev-summit-eu-2025/sixtarbvl5w.md](docs/mcp-dev-summit-eu-2025/sixtarbvl5w.md) | Introduces MCP-UI, an open protocol for embedding sandboxed, interactive UI components directly into AI chat environments.                                    |
| [Keynote] Scaling Commerce Interactivity Lessons from Shopify's Implementation of MCP UI             | Samuel & Brett (Shopify)                | [docs/mcp-dev-summit-eu-2025/t8bgeuoqbh4.md](docs/mcp-dev-summit-eu-2025/t8bgeuoqbh4.md) | Demonstrates Shopify's integration of MCP UI into AI agents, enabling interactive product browsing, cart rendering, and checkout in chat.                     |
| [Session] OAuth Everywhere: What I Learned Building MCP Clients, Servers, & the Gateway Between Them | Donnie Adams (OTO AI)                   | [docs/mcp-dev-summit-eu-2025/ujmywi-tkp0.md](docs/mcp-dev-summit-eu-2025/ujmywi-tkp0.md) | Shares lessons from multi-tenant MCP gateway deployment, addressing OAuth scope challenges, token refresh, and WWW-Authenticate improvements.                 |
| [Session] Why Clients Matter: The Other Side of MCP                                                  | Angie Jones (Block)                     | [docs/mcp-dev-summit-eu-2025/vkhi8-kanoy.md](docs/mcp-dev-summit-eu-2025/vkhi8-kanoy.md) | Highlights the role of open-source MCP clients like Goose in driving agentic AI adoption, preventing lock-in, and enabling custom workflows.                  |
| [Session] Hidden powers of MCP Gateways: Solving OAuth and Analytics Challenges                      | Philip Mlinsy (Glass Cube)              | [docs/mcp-dev-summit-eu-2025/wibqp0rjj78.md](docs/mcp-dev-summit-eu-2025/wibqp0rjj78.md) | Introduces HyperMCP, an open-source gateway for simplifying server setup, centralized OAuth management, and request-response analytics.                       |
| [Session] Secure from Day One Building Production Ready MCP Servers with Nick Taylor - Pomerium      | Nick Taylor (Pomerium)                  | [docs/mcp-dev-summit-eu-2025/wtjzdf068w.md](docs/mcp-dev-summit-eu-2025/wtjzdf068w.md)   | Explains applying zero-trust principles and identity-aware proxies to secure production MCP servers without manual OAuth implementation.                      |
| [Session] Why is MCP Auth Hard and What Are We Planning to Do About It                               | Paul (Anthropic)                        | [docs/mcp-dev-summit-eu-2025/wvtglur2sdi.md](docs/mcp-dev-summit-eu-2025/wvtglur2sdi.md) | Outlines authentication challenges in dynamic MCP environments and introduces SEP 9991 for client metadata documents to replace DCR.                          |
