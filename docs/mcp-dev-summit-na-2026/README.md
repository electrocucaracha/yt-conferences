---
layout: default
title: "Executive Report: MCP Dev Summit NA 2026"
parent: "Mcp Dev Summit Na 2026"
nav_order: 1
type: "Executive Report"
okf_version: "0.2"
description: "Executive report and summary of the MCP Dev Summit NA 2026 conference."
tags:
  - mcp-dev-summit-na-2026
  - executive-report
status: stable
---

# Executive Report: MCP Dev Summit NA 2026

## Executive Overview

The Model Context Protocol Developer Summit North America 2026 (MCP Dev Summit NA 2026) represented a milestone event for the open agentic AI ecosystem.
Organized under the Agentic AI Foundation (AAIF) and Linux Foundation, the summit gathered engineers, architects, security researchers, and technology executives from Anthropic, Docker, AWS, Google Cloud, Microsoft, Prefect, Obot AI, Cloudflare, Datadog, Block, and numerous high-growth startups.
The core focus shifted from initial client-server experimentation to establishing production-grade architectures, enterprise control planes, security patterns, interactive agent interfaces (MCP Apps), and asynchronous task execution models (MCP Tasks).
Keynotes and technical sessions demonstrated how MCP has grown into an industry standard powering over 110 million monthly SDK downloads, driving interoperability across autonomous agents, tools, cloud infrastructure, and enterprise workflows.

## Terminology

- **Model Context Protocol (MCP)**:
  An open standard protocol that standardizes how AI applications and agents connect to context, tools, prompts, and resources across heterogeneous systems.

- **MCP Apps**:
  An extension to the MCP specification that enables servers to return interactive UI components rather than plain text responses, transforming chat interfaces into dynamic graphical workflows.

- **MCP Tasks**:
  An asynchronous execution primitive (defined via SEP-1686) enabling agents to initiate, monitor, and manage long-running, durable background processes across distributed systems.

- **MCP Gateways**:
  Control plane middleware that aggregates, composes, authenticates, and routes requests between agents and multiple backend MCP servers.

- **Context Middleware**:
  Intermediate processing layers that filter, transform, re-rank, or govern the context provided to LLMs to prevent context window saturation and security leaks.

- **Code Mode**:
  An agent operational paradigm where LLMs write and execute scripts locally or in a sandbox to interact with APIs and system resources instead of calling individual granular tools.

- **Agentic Discovery**:
  Mechanisms and registries (such as OCI-based packages or Kubernetes CRDs) that allow agents to dynamically discover and configure MCP servers and skills at runtime.

- **URL Elicitation**:
  A protocol pattern allowing MCP tools to return secure external interaction links for user tasks like OAuth authorization or payment confirmation without exposing credentials to LLMs.

- **Interceptors**:
  Standardized middleware components operating between MCP clients and servers to enforce security policies, audit logging, rate limiting, and context governance.

## Key Themes & Trends

- **Transition to Enterprise Control & Data Planes**:
  Organizations are moving beyond point-to-point local MCP connections toward centralized control planes, enterprise gateways, and data planes.
  These architectures enforce identity management, access delegation, policy control, and auditability across distributed multi-agent systems.

- **Evolution Beyond Static Tools to Interactive UIs (MCP Apps)**:
  Text-only walls are being replaced by rich, embedded UI components returned directly by MCP servers.
  This allows users to review graphics, interact with forms, confirm actions, and collaborate in real-time within environments like Visual Studio Code, ChatGPT, and cloud consoles.

- **Asynchronous & Long-Running Execution (MCP Tasks)**:
  The introduction of MCP Tasks and SEP-1686 solves a fundamental limitation of synchronous HTTP/stdio requests.
  Agents can now dispatch long-running workflows, detach, and asynchronously poll or receive notifications upon completion using engines like Prefect, Temporal, and Obot AI.

- **Security, Identity, and Authorization Re-imagined**:
  Delegated agentic access introduces complex security challenges, including multi-issuer mix-up attacks, shadow MCP deployments, and confused deputy vulnerabilities.
  Practitioners are implementing 4-legged identity frameworks, URL elicitation, OCI container image packaging, and granular interceptors to protect enterprise data.

- **Context Optimization & Progressive Discovery**:
  As tool counts scale into the thousands, passing full API schemas exhausts context windows and degrades model accuracy.
  Engineering teams are utilizing progressive tool discovery, dynamic filtering, RPC-to-MCP abstractions, and context middleware to keep prompts focused and lightweight.

## Key Takeaways & Strategic Insights

- **Standardize on Enterprise MCP Gateways**:
  Deploy centralized MCP gateways to manage tool routing, rate limiting, identity propagation, and observability across internal teams and third-party integrations.

- **Adopt MCP Apps for Complex Workflows**:
  Leverage MCP Apps to embed interactive forms and visualizations directly into agent flows, improving user trust, decision accuracy, and human-in-the-loop control.

- **Implement Asynchronous Architecture with MCP Tasks**:
  Incorporate MCP Tasks (SEP-1686) into workflow engines to decouple agent decision-making from execution time limits, supporting resilient background automation.

- **Enforce Granular Security and Identity Guardrails**:
  Mitigate agent-based security threats by shifting from broad service accounts to user-delegated OAuth patterns, sandboxed OCI runtime environments, and real-time interceptors.

## Sessions & Talks Summary

| Talk Title                                                                              | Speaker & Organization                                 | Document                         | Core Thesis & Strategic Insight                                                                                 |
| :-------------------------------------------------------------------------------------- | :----------------------------------------------------- | :------------------------------- | :-------------------------------------------------------------------------------------------------------------- |
| Keynote: Opening Remarks                                                                | Jim Zemlin                                             | [ittmkatsbfu.md](ittmkatsbfu.md) | Welcomes attendees and celebrates the rapid community expansion around open AI standards and interoperability.  |
| Keynote: Welcome Remarks from the AAIF Governing Board Chair                            | David Nalley                                           | [p-plv187bw.md](p-plv187bw.md)   | Details the milestone growth of the Agentic AI Foundation to 170+ members advancing open governance.            |
| MCP Creator Reveals the 2026 Roadmap for AI Agents                                      | David (Anthropic)                                      | [kavrfygcpg0.md](kavrfygcpg0.md) | Highlights over 110M monthly SDK downloads and outlines future protocol extensions for agentic scale.           |
| Keynote: Building a Unified Control Plane for MCP Across Servers, Clients, and Teams    | Cecilia Liu (Docker)                                   | [en8tvf2h6g0.md](en8tvf2h6g0.md) | Highlights real-world risks of unmanaged MCP servers and proposes centralized enterprise control planes.        |
| Keynote: Context is More Than Tools - Why the "C" in MCP is More Relevant Than Ever     | Ryan Cooke (WorkOS)                                    | [685yfog3aeo.md](685yfog3aeo.md) | Demonstrates leveraging protocol primitives beyond tool calling to optimize contextual intelligence for agents. |
| Keynote: Enterprise MCP - The Data Plane for Autonomous Agents                          | Adam Seligman & Zayne Turner (Workato)                 | [zsqjouecvrc.md](zsqjouecvrc.md) | Advocates for data plane architectures to safely govern enterprise data flow across autonomous agent networks.  |
| Keynote: Lessons Learned from Driving Enterprise MCP Adoption                           | Sheng Liang (Obot AI)                                  | [m5ymjzx-cfs.md](m5ymjzx-cfs.md) | Shares experiences from early enterprise adoption and community growth over the initial summit cycle.           |
| Keynote: MCP @ Amazon Scale                                                             | James Hood (AWS)                                       | [1rogvapmow.md](1rogvapmow.md)   | Explores the evolution of agentic chat, reasoning models, and internal MCP adoption across Amazon.              |
| Keynote: MCP Apps: Extending the Frontier                                               | Ido Salomon & Liad Yosef                               | [e6sspa7wpwc.md](e6sspa7wpwc.md) | Introduces MCP Apps as an open standard enabling interactive graphical UIs to replace static text.              |
| Keynote: Navigating Primitives for Agent Collaboration                                  | Nick Aldridge (Mousecat)                               | [1hhffkfqrn8.md](1hhffkfqrn8.md) | Reviews the progression from basic Q&A models to sophisticated multi-agent collaborative primitives.            |
| Keynote: One-To-Many: Enabling MCP, Agents, and Intelligent Systems...                  | Ola Hungerford & Sandeep Bhat (Nordstrom)              | [4rmvn-d8uy.md](4rmvn-d8uy.md)   | Details enterprise architecture foundations required to scale AI integration across retail domains.             |
| Keynote: Using MCP for Skills Orchestration and Enterprise Integration                  | Jacob Wilson (PwC)                                     | [30wu-6-wplc.md](30wu-6-wplc.md) | Explores applying modern orchestration and skills management to transform enterprise procurement.               |
| Call Now, Fetch Later: MCP Tasks and SEP-1686                                           | Adam Azzam (Prefect)                                   | [iskuhxrf6wm.md](iskuhxrf6wm.md) | Explains SEP-1686 for decoupling task invocation from execution in long-running agent workflows.                |
| Durable, Asynchronous, and Tricky: Implementing MCP Tasks in Practice                   | Cornelia Davis (Temporal)                              | [cd0dlpavdn8.md](cd0dlpavdn8.md) | Addresses implementation details and reliability patterns for asynchronous task workflows.                      |
| Building a Workflow Engine on MCP: Orchestrating Processes With Tasks                   | Donnie Adams (Obot AI)                                 | [f8vpmlm0mai.md](f8vpmlm0mai.md) | Explores building task-based workflow engines leveraging Kubernetes-inspired declarative primitives.            |
| Beyond the Sandbox: Security at the Host Layer                                          | Lorenzo Verna & Pietro Valfrè (Denied)                 | [jtkkznut1fw.md](jtkkznut1fw.md) | Proposes host-layer behavioral authorization models to secure autonomous agent execution.                       |
| Bridging Kernel Space and AI: Building an MCP Server for Linux Scheduler Observabil...  | Daniel Hodges                                          | [emgieqbsjm.md](emgieqbsjm.md)   | Demonstrates using BPF and MCP for conversational, hypothesis-driven kernel scheduling analysis.                |
| Building ChatGPT Apps: Principles for a New Kind of Interface                           | Elliot Garreffa (Ghost Team)                           | [km4zzw0aohc.md](km4zzw0aohc.md) | Outlines design principles for shifting from traditional web layouts to intent-driven conversational apps.      |
| Building MARVIN: What Teaching a Non-Technical Marketer To Use MCP Taught Me About...   | Sterling Chin                                          | [g1zzxm-6bx8.md](g1zzxm-6bx8.md) | Highlights user experience lessons and long-term context retention when onboarding non-technical users to MCP.  |
| Challenges in Delivering Unstructured Content Efficiently Over...                       | Kailas Krivanka & Fernando Cerenza (Box)               | [hrfaijvcof8.md](hrfaijvcof8.md) | Shares architecture solutions for streaming unstructured content and connecting agents with cloud storage.      |
| Clients? Servers? Agents? The Beautiful Asymmetry of the MCP Spec                       | Rohit Ganguly (Descope)                                | [gmqcxe1zrwy.md](gmqcxe1zrwy.md) | Analyzes protocol asymmetry and dynamic client-server-agent relationships in modern implementations.            |
| Code Mode Is Best Served in the Shell                                                   | Jan Curn (Apify)                                       | [z5c9lspqryw.md](z5c9lspqryw.md) | Compares structured protocol calls against shell-based CLI execution for agent efficiency.                      |
| Code Mode Without the Code                                                              | Bob Dickinson (TeamSpark)                              | [ttcnnsapx5q.md](ttcnnsapx5q.md) | Introduces MCP Graph, a no-code visual workflow orchestration engine for MCP servers.                           |
| Combine Skills and MCP To Close the Context Gap                                         | Pedro Rodrigues (Supabase)                             | [rk9y-27dpko.md](rk9y-27dpko.md) | Clarifies complementary roles between protocol integrations (MCP) and instructional skill folders.              |
| Context Middleware for MCP: From Enterprise Needs To Protocol Extension                 | Peder Holdgaard Pedersen (Saxo Bank)                   | [x5lx3iou7m.md](x5lx3iou7m.md)   | Examines middleware patterns for governing context quality and enforcing enterprise accuracy.                   |
| Datadog Built 100 AI Agents. Here's What Broke.                                         | Datadog Speaker                                        | [naty-iftitm.md](naty-iftitm.md) | Reviews real-world lessons and failure modes when scaling agent fleets in production.                           |
| Declarative MCP Servers for Secure, Specialized AI Agents                               | Josh Reini & Reetika Roy (Snowflake)                   | [lo4nyyuersy.md](lo4nyyuersy.md) | Recommends domain-focused declarative servers over monolithic agents with excessive privileges.                 |
| Demistifying Client ID Metadata Documents in MCP                                        | Den Delimarsky (Anthropic)                             | [yrlpr3o9fni.md](yrlpr3o9fni.md) | Explains standardized client registration and metadata document specs for robust authorization.                 |
| Deploying MCP at Scale Without Skipping Compliance                                      | Becky Brooks (Usercentrics)                            | [cjsr-hkizok.md](cjsr-hkizok.md) | Outlines compliance strategies and regulatory alignment under frameworks like the EU AI Act.                    |
| Distributing MCP Servers With OCI To Power Agent Skills                                 | Bobby House (Docker)                                   | [y4pmgop4ryg.md](y4pmgop4ryg.md) | Demonstrates using OCI image registries for secure packaging and distribution of server dependencies.           |
| Dynamic MCPs: Agentic Discovery, Configuration, and Management of MCP Workloads         | Jim Clark (Docker)                                     | [3imd6g6nm2s.md](3imd6g6nm2s.md) | Compares MCP development to LSP and details dynamic agentic server discovery mechanisms.                        |
| Enabling Agentic Cloud Workflows                                                        | Santhosh Misro & Mayur Deshpande (Google)              | [9tkkmvgqhqo.md](9tkkmvgqhqo.md) | Presents Google Storage Intelligence MCP server for goal-driven cloud resource management.                      |
| Enterprise-Ready MCP: Security Patterns and the "4-Legged" Identity Challenge           | Paulina Xu (Aentic Fabric)                             | [pjpocx9-kt8.md](pjpocx9-kt8.md) | Addresses complex identity delegation challenges across multi-tier agent and service topologies.                |
| Evaluate What You Can't See: Measure the Probabilistic Nature of MCP                    | P. Patel & M.J. Rocabado (MCP Jam)                     | [xqjockeusrq.md](xqjockeusrq.md) | Introduces evaluation frameworks to measure user value and server performance probabilistically.                |
| Every API Is a Tool for Agents                                                          | Matt Carey (Cloudflare)                                | [2cndqvkogaw.md](2cndqvkogaw.md) | Shares strategies for handling large API specifications without exhausting model context windows.               |
| Evolution, Not Revolution: How MCP Is Reshaping OAuth                                   | Aaron Parecki (Okta)                                   | [zsocfseyvkc.md](zsocfseyvkc.md) | Explores updates to authorization standards tailored for autonomous agent delegation.                           |
| From 60 Minutes To 60 Seconds: Production MCP Workflows for Healthcare Billing          | Andrew Espira (Custod)                                 | [1lowizbnbsg.md](1lowizbnbsg.md) | Case study showing how MCP orchestration reduces healthcare billing workflows from 60 minutes to 60 seconds.    |
| From Benchmarks To Business Value: Building a Use-Case Specific Agen...                 | Gaurav Saxena & Matvey Kukuy                           | [o7l6-myoct0.md](o7l6-myoct0.md) | Discusses real-world evaluation methodologies for complex telemetry and incident response agents.               |
| From Chaos To Clarity: How MCP Transforms Incident Response                             | Sebastian Villanelo & Rocío Bayon                      | [t8sx0-jp1dm.md](t8sx0-jp1dm.md) | Shows how MCP apps reduce engineer context switching during high-pressure incident triage.                      |
| From Cypher to Conversation: MCP at WestJet                                             | Anton Lysov (WestJet)                                  | [l8m0ypnf4xi.md](l8m0ypnf4xi.md) | Illustrates replacing complex graph queries with conversational MCP interfaces for airline flight scheduling.   |
| From One MCP Server To an Ecosystem: When MCP Stops Being a Server and Becomes a Pla... | Vaibhav Tupe (Equinix)                                 | [7ifljwmwexk.md](7ifljwmwexk.md) | Details scaling MCP from single automation tools to a platform-wide enterprise ecosystem.                       |
| From Scopes To Intent: Reimagining Authorization for Autonomou...                       | Andres Aguiar & Abhishek Hingnikar (Okta)              | [pqnsft7bvie.md](pqnsft7bvie.md) | Re-imagines access control models by transitioning from static scopes to intent-based authorization.            |
| Golem To Murderbot: Challenges With Agentic Security Delegation Via MCP                 | Michael Schwartz (Gluu)                                | [ixqorhltcfw.md](ixqorhltcfw.md) | Analyzes risks of intent deviation and delegation control using literary metaphors.                             |
| Goose as a Proving Ground for New MCP Features, and How To Use Them                     | Alex Hancock (Block)                                   | [0nnuor6gvbk.md](0nnuor6gvbk.md) | Demonstrates open-source testing of new MCP capabilities within the Goose agent project.                        |
| Hooks, Not Hacks: Modular Enforcement for MCP Agents                                    | Fred Araujo & Ian Molloy (IBM)                         | [9lnfch7egxq.md](9lnfch7egxq.md) | Proposes modular security enforcement hooks treating agents as potential insider threats.                       |
| How Duolingo Built an AI Slackbot With 180+ MCP Tools                                   | Aaron (Duolingo)                                       | [5sb9ia2v78g.md](5sb9ia2v78g.md) | Shares architecture and lessons from connecting an internal Slackbot to 180+ MCP tools.                         |
| Human in the Loop, Agent in the Flow                                                    | Harald Kirschner & Connor Peet (Microsoft)             | [chjb-bbe050.md](chjb-bbe050.md) | Explores building rich interactive agent experiences in Visual Studio Code through MCP primitives.              |
| If You Can Secure It Here, You Can Secure It Anywhere                                   | Milan Williams & Katrina Liu (Semgrep)                 | [iyouii6qbn8.md](iyouii6qbn8.md) | Details securing MCP servers within static analysis security platforms.                                         |
| If the LLM Can't Find You, You Don't Exist: Discoverability for MCP-Apps and Chat...    | Vincent McLeese (Ghost Team)                           | [mtlfhstd3ve.md](mtlfhstd3ve.md) | Discusses discoverability mechanics and ranking strategies for MCP apps in AI marketplaces.                     |
| Intent Engineering: The Death of the Mono-Directional Prompt                            | Rizel Scarlett (Block, Inc.)                           | [v2rlapqnk4i.md](v2rlapqnk4i.md) | Explores the evolution from single static prompt engineering to bidirectional intent engineering.               |
| Interceptors for MCP: A Production-Tested Standard for Agentic Middl...                 | Kurt Degiorgio & Cannis Chan (Bloomberg)               | [z8s3fnjmty0.md](z8s3fnjmty0.md) | Introduces standardized interceptor middleware for governance, auditing, and context control.                   |
| Kubernetes-Native Agent Discovery: A Unified Registry for MCP Servers and Skills        | Carlos Santana (AWS)                                   | [dkzysomojtq.md](dkzysomojtq.md) | Uses Kubernetes CRDs as a control plane for modeling and discovering agent workloads.                           |
| Lessons Learned Building Intelligent UIs With MCP Apps                                  | Riley Scheid (Reboot)                                  | [arso4yfclxq.md](arso4yfclxq.md) | Best practices for building UI components returned by MCP apps in complex workflows.                            |
| MCP Apps Best Practices: Patterns and Pitfalls                                          | Olivier Chafik & Anton Pidkuiko (Anthropic)            | [xh-6gtirhm.md](xh-6gtirhm.md)   | Demonstrates interoperability patterns and UX pitfalls when developing MCP apps.                                |
| MCP Gateways: The Control Plane for Agentic Integration                                 | Alex Salazar (Arcade.dev)                              | [dxz4mlsrcoc.md](dxz4mlsrcoc.md) | Identifies key enterprise requirements for gateways, including authentication and observability.                |
| MCP Live: Streaming Context To AI Agents                                                | Harshit Kohli (AWS)                                    | [v7jcetecvo0.md](v7jcetecvo0.md) | Proposes extending request-response models to real-time event streaming for AI agents.                          |
| MCP Meets Java: Engineering the MCP Java SDK                                            | Dariusz Jędrzejczyk (Broadcom)                         | [sexqcwklork.md](sexqcwklork.md) | Introduces the official Java MCP SDK for enterprise integration on the JVM.                                     |
| MCP Servers in the Wild: Managing Tool Complexity at Scale                              | Arnav Balyan (Concierge AI)                            | [ek3fbc0-04.md](ek3fbc0-04.md)   | Presents techniques to manage large tool schemas without overwhelming context limits.                           |
| MCP Traffic Handling at Scale: Stateless Design, Proxies, and the Roa...                | Erica Hughberg & Boteng Yao                            | [vmlyp862lb8.md](vmlyp862lb8.md) | Discusses proxying, session affinity, and stateless transport design for high-volume MCP traffic.               |
| MCP Vs CLIs: Why Agents Need Purpose-Built Interfaces                                   | Sam Morrow (GitHub)                                    | [ideydmjkuje.md](ideydmjkuje.md) | Compares purpose-built MCP tool protocols against general CLI wrappers for agent safety.                        |
| MCP at 18 Months: Protocols, Patterns, and What We Didn't See Coming                    | Shaun Smith (Hugging Face)                             | [dw1hgjxrndy.md](dw1hgjxrndy.md) | Reflects on the evolution, ecosystem trends, and unexpected shifts in agent adoption.                           |
| MCP for Autonomous Storefronts: Building Self-Healing Agent Loops                       | Guilherme Rodrigues (decocms.com)                      | [nctyh0nrxvm.md](nctyh0nrxvm.md) | Case study on self-healing agent loops managing high-volume e-commerce storefronts.                             |
| MCP: The Gateway to Real-Time Human–AI Collaboration in Jupyter at Scale                | Jake Diamond-Reivich (Jupyter)                         | [npcy4ccny7e.md](npcy4ccny7e.md) | Introduces Jupyter AI v3 and Agent Client Protocol integration for interactive data science.                    |
| MCPwned: Hacking MCP Servers With One Skeleton Key Vulnerability                        | Jonathan Leitschuh                                     | [baardvgg3v0.md](baardvgg3v0.md) | Discloses security vulnerabilities in local MCP servers and browser origin risks.                               |
| Mental Reset: How To Rethink Your User Flow in the Age of MCP & ChatGPT Apps            | Erica Beavers (Alpic)                                  | [d2l4tvt6onq.md](d2l4tvt6onq.md) | Redefines UX design flows for agent-first applications across industries.                                       |
| Mix-Up Attacks in MCP: Multi-Issuer Confusion and Mitigations                           | Emily Lauber (Microsoft)                               | [nb9g3bj3uk.md](nb9g3bj3uk.md)   | Analyzes multi-issuer mix-up attack vectors in multi-tenant agent integrations and mitigations.                 |
| My MCP Server Code Works, but the Agent Fails: The Case for MCP-specif...               | Calum Murray & Wesley Chun (Red Hat)                   | [r-otbm1fzmm.md](r-otbm1fzmm.md) | Introduces MCP Checker, an evaluation tool for testing agent-server semantic interface reliability.             |
| OCI Images as MCP Packaging: Supply Chain Security for AI Tools                         | Juan Antonio Osorio (Stacklok)                         | [zzioined-bm.md](zzioined-bm.md) | Recommends OCI container packaging for supply chain security and tool distribution.                             |
| One Spec, Ten SDKs, Zero Excuses: Conformance Testing MCP                               | Paul Carleton (Anthropic)                              | [2zurqpsjzi.md](2zurqpsjzi.md)   | Addresses specification ambiguities and introduces automated conformance suites across SDKs.                    |
| Operating MCP in the Enterprise: From Protocol To Production                            | Amar Deep Singh & Neelabh Tripathi                     | [0doyliqioxy.md](0doyliqioxy.md) | Shares practical architecture patterns for promoting AI protocols from lab pilots to production.                |
| Path to V2 for MCP SDKs                                                                 | Max Isbey (Anthropic)                                  | [sfdrrela93s.md](sfdrrela93s.md) | Outlines upcoming breaking updates, transport improvements, and multi-language SDK convergence.                 |
| Patterns for Building MCP-powered Agent Systems                                         | Jiquan Ngiam (MintMCP)                                 | [vkj3zt8gx0y.md](vkj3zt8gx0y.md) | Explores patterns for organizing fleets of AI agents collaborating alongside human teams.                       |
| Progressive Tool Discovery: Using MCP Notifications To Manage C...                      | Billy Hickman & Lilia Abaibourova (Amazon Prime Video) | [mfl5crtbux0.md](mfl5crtbux0.md) | Leverages notifications for dynamic tool discovery to avoid overwhelming model context limits.                  |
| Protocol Evolution: Adapting the Model Context Protocol for SLMs and the Edge           | Kierra Dotson                                          | [zqimtpjo0aq.md](zqimtpjo0aq.md) | Discusses protocol adaptations needed to run MCP efficiently on small language models and edge nodes.           |
| Putting the Single Back in Single Sign-On: Cross-App Access for MCP                     | Paul Carleton & Max Gerber                             | [hrrzzorvy84.md](hrrzzorvy84.md) | Addresses OAuth consent fatigue and proposes seamless cross-app single sign-on mechanisms.                      |
| RPC & MCP: Turning a Decade of APIs Into Agentic Tools                                  | Ze'ev Klapow (HubSpot)                                 | [7520metfn94.md](7520metfn94.md) | Demonstrates transforming existing RPC service frameworks into agentic tools at scale.                          |
| Reflections on Context Engineering Via MCP Servers                                      | Till Döhmen (MotherDuck)                               | [bjyiokgnkaq.md](bjyiokgnkaq.md) | Shares insights on context engineering for cloud data warehousing and DuckDB queries.                           |
| Rules Are Not Suggestions: A History of MCP Non-Compliance                              | Sterling Dreyer (Arcade.dev)                           | [ecgymy4euto.md](ecgymy4euto.md) | Recounts real-world non-compliance issues and ecosystem friction during rapid specification changes.            |
| Schema To Insight: Architecting Production-Grade Database MCP Tools                     | Kurtis Van Gent & Wenxin Du (Google)                   | [9u3zlfqxyqu.md](9u3zlfqxyqu.md) | Presents patterns for building secure, scalable database query tools for AI agents.                             |
| Securing MCP at Scale: From Principles To Production                                    | Peter Smulovics (Morgan Stanley)                       | [e515s-ewf9m.md](e515s-ewf9m.md) | Analyzes security challenges in highly regulated banking environments including prompt injection.               |
| Securing the MCP Ecosystem: Production Patterns for Transparency...                     | Lisa Tagliaferri & Trevor Dunlap (Chainguard)          | [8egmt6fzfgk.md](8egmt6fzfgk.md) | Addresses supply chain threats, tool poisoning, and exfiltration risks across agent toolchains.                 |
| Shadow MCP: Finding the MCPs Nobody Approved                                            | Aidan Sochowski & Alexander Frazer (Runlayer)          | [mpmv-t-i0k8.md](mpmv-t-i0k8.md) | Examines security risks of unapproved shadow MCP servers operating without IT oversight.                        |
| Skills Vs. MCP Vs. Code Mode: Cutting Through the Hype (and the Rage)                   | Nikolay Rodionov (Alpic)                               | [doedeqfi6hg.md](doedeqfi6hg.md) | Clarifies boundaries and synergies between agent skills, MCP protocols, and code mode.                          |
| Sponsored Session: Agents and MCP @ Google Scale                                        | Alan Blount & Vaibhav Katkade (Google Cloud)           | [jcj3lfqyhy4.md](jcj3lfqyhy4.md) | Overview of Google Cloud's extensive use of MCP across products and cloud infrastructure.                       |
| Sponsored Session: Future-Proofing AI Agents: The Strategic Role of MCP                 | Don Murray (Safe Software)                             | [fp-31qaw1pq.md](fp-31qaw1pq.md) | Highlights the strategic role of MCP endpoints in enterprise data integration.                                  |
| Sponsored Session: Model Context Pragmatism                                             | Jeremiah Lowin (Prefect)                               | [vfoe10ww6s0.md](vfoe10ww6s0.md) | Discusses FastMCP and opinionated frameworks designed to absorb protocol complexity.                            |
| Sponsored Session: The Self-Improving MCP Server: Agents in a Live Development Loop     | Enrico Toniato                                         | [xmpoyrgclxe.md](xmpoyrgclxe.md) | Demonstrates live development loops for continuously testing and self-improving MCP servers.                    |
| Sponsored Session: Who's Driving? Delegation and the Confused Deput...                  | Vitor Balocco & Alvaro Inckot (Runlayer)               | [cmwjs-eal0w.md](cmwjs-eal0w.md) | Addresses confused deputy vulnerability risks when agents execute delegated tasks.                              |
| Stateless: The Future of MCP Transports                                                 | Shaun Smith & Kurtis Van Gent                          | [oguryxwyr70.md](oguryxwyr70.md) | Outlines transport shifts toward stateless designs for improved reliability and horizontal scaling.             |
| The Anatomy of a Meltdown: A Deep-Dive into MCP via Selective Sabotage                  | Joey Stout (Spacelift)                                 | [ivemlfwwl0i.md](ivemlfwwl0i.md) | Interactive deep-dive sabotaging the six core MCP primitives to demonstrate failure points.                     |
| The Boring Attack That Will Actually Get You                                            | Craig Jellick (Obot AI)                                | [6tn4ykrcr-e.md](6tn4ykrcr-e.md) | Warns against supply chain attacks like typosquatting and dependency compromise on MCP servers.                 |
| The MCP Gateway Pattern: Aggregation, Composition, and Beyond                           | Juan Antonio Osorio (Stacklok)                         | [kf8exmglzks.md](kf8exmglzks.md) | Details gateway architectural patterns for aggregating and composing multiple MCP servers.                      |
| The Seven Deadly Sins With MCP                                                          | Ricardo Ferreira (Redis)                               | [qgh5mosqw64.md](qgh5mosqw64.md) | Highlights common implementation antipatterns and performance bottlenecks in MCP servers.                       |
| The Tool Abstraction Problem: Lessons Learned Building 1000+ MCP Tools                  | Sam Partee (Arcade.dev)                                | [ddvdusjggzy.md](ddvdusjggzy.md) | Shares lessons on designing tool abstractions specifically optimized for LLM reasoning.                         |
| Threat Modeling Authorization in MCP                                                    | Sarah Cecchetti (OpenID Foundation)                    | [adi8zrdmn-4.md](adi8zrdmn-4.md) | Uses delegation metaphors to threat-model multi-agent permission delegation.                                    |
| Title not found                                                                         | Video Resource                                         | [g1etzkqyh1i.md](g1etzkqyh1i.md) | Session video record without summary content.                                                                   |
| Title not found                                                                         | Video Resource                                         | [gpd4owmbmni.md](gpd4owmbmni.md) | Session video record without summary content.                                                                   |
| Title not found                                                                         | Video Resource                                         | [hw668yuvkao.md](hw668yuvkao.md) | Session video record without summary content.                                                                   |
| Title not found                                                                         | Video Resource                                         | [ypn8gvndqg4.md](ypn8gvndqg4.md) | Session video record without summary content.                                                                   |
| Title not found                                                                         | Video Resource                                         | [zthbtfn8pby.md](zthbtfn8pby.md) | Session video record without summary content.                                                                   |
| Towards Building Safe & Secure Agentic AI                                               | Dawn Song & Matt White (Linux Foundation)              | [zrrvijvb4ay.md](zrrvijvb4ay.md) | Presents research frameworks for ensuring safety, alignment, and security in agentic AI.                        |
| UI in the Age of AI                                                                     | Adam Cowley (Neo4j)                                    | [byiyl20qazq.md](byiyl20qazq.md) | Discusses UI design shifts as non-technical users increasingly interact with AI graph tools.                    |
| URL Elicitation Deep Dive: Third-party OAuth Solved (and More!)                         | Nate Barbettini (Arcade.dev)                           | [sxiw3xztvz0.md](sxiw3xztvz0.md) | Introduces URL elicitation for handling OAuth and payments without exposing secrets to LLMs.                    |
| What if MCP was Symmetric?                                                              | Jerome Swannack (Anthropic)                            | [jfwiwfw0nfs.md](jfwiwfw0nfs.md) | Proposes symmetric MCP where servers and clients interact bidirectionally for composable systems.               |
| When MCP Becomes a Product                                                              | Gautam Baghel & Roy Derks (IBM & HashiCorp)            | [rjowgzovw-u.md](rjowgzovw-u.md) | Shares experience transitioning internal MCP demos into production product offerings.                           |
| When MCP Isn’t Enough: Product Decisions Behind Scalable Agent Systems                  | Cansu Berkem (Datadog)                                 | [7q7e-ziocea.md](7q7e-ziocea.md) | Details turning agent prototypes into enterprise production products like Datadog Bits AI.                      |
| Your MCP Server Will Probably Be Abandoned...Or Not                                     | Lahari Chowtoori (AWS)                                 | [062abr355-c.md](062abr355-c.md) | Discusses community health, maintenance, and long-term sustainability across the MCP server ecosystem.          |
| YouTube Video Reference (9kwcnf9dnk4)                                                   | Video Resource                                         | [9kwcnf9dnk4.md](9kwcnf9dnk4.md) | Reference notes for YouTube video session.                                                                      |
