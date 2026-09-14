---
layout: default
title: "Cloud Native Kubernetes Ai Day 2025 Na"
has_children: true
nav_order: 3
---

# Cloud Native Kubernetes Ai Day 2025 Na

## Executive Overview

The Cloud Native + Kubernetes AI Day 2025 North America brought together cloud-native maintainers, infrastructure architects, hardware providers, and enterprise engineering teams to address the operational realities of running AI/ML workloads at scale.
Featuring presentations from CERN, Broadcom, Red Hat, Nvidia, Bloomberg, IBM, Google, Intuit, Uber, Microsoft, Datadog, Solo.io, Confluent, and emerging GPU cloud providers like Lambda and Nebius, the conference highlighted a major industry transition from basic GPU provisioning to intelligent, AI-aware cloud orchestration.
Organizations are moving beyond traditional microservice scheduling toward specialized inference gateways, disaggregated prefill/decode serving, prefix-aware KV cache management, and dynamic device allocation.
Simultaneously, autonomous AI agents are being integrated directly into Kubernetes environments for on-call debugging and cluster operations, driving the need for strict WebAssembly-based sandboxing and OpenTelemetry-based verification.
To achieve sustainable AI ROI and operational reliability, industry leaders emphasized the necessity of aligning data locality with compute, eliminating hardware silos, and adopting declarative, cloud-native standards across the entire AI lifecycle.

## Terminology

- **KV Cache**:
  The runtime memory of a Large Language Model (LLM) that stores key-value attention tensors to avoid recomputing prompt tokens across multi-turn queries.

- **Gateway API Inference Extension**:
  A Kubernetes project extending traditional gateways to route inference requests based on model parameters, SLA objectives, and real-time backend metrics.

- **Prefix-Aware Routing**:
  An intelligent routing mechanism that directs LLM prompt requests to model servers holding matching prompt prefixes in their local KV cache.

- **Device Resource Allocation (DRA)**:
  A Kubernetes framework providing fine-grained, dynamic allocation and sharing of hardware accelerators like GPUs without static pre-configuration.

- **Disaggregated Serving**:
  An LLM inference architecture that physically separates prompt prefill nodes from token decode nodes to optimize compute utilization and latency.

- **Declarative AI Agent**:
  An autonomous software worker defined via Kubernetes Custom Resource Definitions (CRDs) that executes operational tasks using model configs and tool integrations.

- **WebAssembly (Wasm) Sandbox**:
  A lightweight, deny-by-default execution environment that restricts external tool capabilities and network access when AI agents run untrusted binaries.

- **GraphRAG**:
  Retrieval-Augmented Generation that connects enterprise documents and metadata into a graph database to supply structured logical context to LLMs.

## Key Themes & Trends

- **Intelligent LLM Serving and Prefix-Aware Caching**:
  Inference platform maintainers are replacing round-robin load balancers with smart inference gateways (LLMD, KServe, Gateway API Inference Extension).
  By tracking KV cache state and prompt prefixes across pods, these platforms dramatically reduce first-token latency, increase request throughput, and lower GPU compute costs.

- **Granular Accelerator Allocation and Topology Scheduling**:
  Standard Kubernetes pod readiness probes and device plugins are insufficient for complex AI workloads.
  Innovations like Device Resource Allocation (DRA) consumable capacity and topology-aware schedulers (Kai, Q) enable fine-grained GPU memory partitioning, rack-aware network placement, and fair-share queue preemption.

- **Kubernetes-Native Infrastructure Agents**:
  AI agents are evolving from external chatbots into declarative Kubernetes workloads (Kagent, Intuit On-Call Agent).
  These agents interact directly with cluster resources, Argo, and GitHub to diagnose system incidents, fix misconfigurations, and automate operational runbooks.

- **Security, Isolation, and Telemetry Verification**:
  Autonomous agent tool usage presents security risks like secret exfiltration and tool poisoning.
  Projects like Waset utilize WebAssembly component sandboxes with deny-by-default policies, while OpenTelemetry instrumentation ensures AI agents make decisions based on real-time execution traces rather than hallucinated assumptions.

- **Enterprise Hardware Scale and Multi-Cloud Resiliency**:
  Hyperscalers and neoclouds (Lambda, Nebius, Uber, Loft Labs) are building automated operator frameworks to handle high GPU failure rates.
  By combining virtual clusters (vCluster), Karpenter autoscaling, and automated power drains, organizations maintain cluster health across hybrid and multi-cloud environments.

## Key Takeaways & Strategic Insights

- **Adopt Open Standards for Model Serving**:
  Standardize inference infrastructure around CNCF projects like KServe and the Gateway API Inference Extension to decouple routing logic from specific model runtimes.

- **Optimize Memory and Cache Reuse**:
  Implement cross-pod KV cache offloading and prefix-aware routing (LMCache, LLMD) to maximize GPU utilization and reduce time-to-first-token in long-context applications.

- **Evolve Workload Schedulers for AI Topologies**:
  Transition from generic pod scheduling to topology-aware and resource-fair schedulers (Kai, Q, DRA) that account for interconnect bandwidth, rack placement, and GPU memory sharing.

- **Enforce Strict Tool Sandboxing for Agents**:
  Isolate autonomous agents and Model Context Protocol (MCP) integrations using WebAssembly sandboxes (Waset) to prevent credential theft and unauthorized network egress.

- **Bridge Infrastructure Telemetry and Application Health**:
  Instrument workloads with OpenTelemetry and pre-flight connectivity checks to ensure Kubernetes reports running status only when AI applications are actively making progress.

| Talk Title                                                                                                  | Speaker & Organization                                   | Core Thesis & Strategic Insight                                                                                                                     |
| :---------------------------------------------------------------------------------------------------------- | :------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Fit-to-Serve: How a New DRA Capability for Dynamic Device...](j6zkgxrxm6o.md)                              | Sunyanan Choochotkaew & Tatsuhiro Chiba (IBM Research)   | Demonstrates Device Resource Allocation (DRA) consumable capacity for fine-grained GPU slicing and dynamic memory allocation in inference serving.  |
| [KServe Next: Advancing Generative AI Model Serving](vbrpeudn4tq.md)                                        | Yuan Tang (Red Hat) & Dan Sun (Bloomberg)                | Presents KServe 0.16 evolution as a CNCF incubating project unifying predictive and generative AI inference with disaggregated serving.             |
| [LMCache: Lower LLM Performance Costs in the Enterprise](v4cnylxt9da.md)                                    | Martin Hickey (IBM / PyTorch) & Junchen Jiang (UChicago) | Introduces LMCache for offloading, sharing, and persistently storing KV caches across GPU, CPU, and remote storage backends.                        |
| [Lightning Talk: Mind the Topology: Smarter Scheduling for AI Workloads on Kubernetes](o5i7ptwzjfo.md)      | Roman Baron (Nvidia)                                     | Details the Kai scheduler for topology-aware placement of multi-pod AI workloads across racks and zones based on interconnect bandwidth.            |
| [Lightning Talk: My Job Says 'Running' but Nothing's Running: Kubernetes Status Reality...](ahjzvt3vpac.md) | Ron Kahn (Nvidia)                                        | Highlights the gap between K8s readiness probes and true AI training progress, advocating pre-flight connectivity checks and continuous validation. |
| [Lightning Talk: Resource Fairness and Utilization for Heterogeneous Batch/M...](dkhf-hzi7ci.md)            | Yuki Iwai (CyberAgent) & Gabe Saba (Google)              | Explains Q, a secondary Kubernetes scheduler using Dominant Resource Share (DRS) and usage penalties for fair GPU queue allocation and preemption.  |
| [On-Call the Easy Way With Agents](odli4cbkky8.md)                                                          | Ryan Tay & Kartikeya Pharasi (Intuit)                    | Shows Intuit's AI on-call agent system leveraging RAG and automated runbooks to analyze telemetry and reduce incident MTTR at enterprise scale.     |
| [Panel: AI Infra Best Practices: Enterprise Do’s and Don’ts](ketngeleq-k.md)                                | Madhuri Yechuri & Andrew Leung (Uber)                    | Shares Uber's AI infrastructure journey, emphasizing multi-cloud strategy, compute/data locality, and CPU/GPU workload disaggregation.              |
| [Sponsored Keynote: Autoscaling GPU Clusters Anywhere — Hyperscalers, Neoclouds & Ba...](lgoelo-ah30.md)    | Lukas Gentele (Loft Labs)                                | Presents vCluster and AWS Karpenter integration for cost-effective virtual cluster isolation and dynamic GPU autoscaling.                           |
| [Sponsored Keynote: Cloud-Native GraphRAG: AI’s Logical Edge](flldxr68nsi.md)                               | Stephen Chin (Neo4j)                                     | Demonstrates GraphRAG for enhancing model accuracy and logical reasoning by structuring enterprise documents in graph databases.                    |
| [Sponsored Keynote: From Open Source to Real-World Scale](co6uottp-oy.md)                                   | Aleksandr Patrushev (Nebius)                             | Outlines Nebius's vertically integrated AI cloud platform combining Kubernetes, Slurm operators, and custom virtualization for physical GPU speed.  |
| [Sponsored Keynote: Kubernetes Challenges at Lambda](7ldbcsobej4.md)                                        | Andrew Godwin (Lambda Labs)                              | Examines GPU hardware failure rates and Lambda's automated remediation framework using K8s operators and bare-metal Cluster API.                    |
| [The Hidden Foundation: How Effective Data Management Determines AI System Success](fidcxetnfho.md)         | Keith McClellan (Splunk)                                 | Addresses data integration hurdles in AI adoption, advocating OpenTelemetry, ABAC, and in-place data processing to prevent project failures.        |
| [This Lying Has To Stop: Keeping AI Honest with OpenTelemetry](rwu7jxzboq8.md)                              | Whitney Lee (Datadog)                                    | Demonstrates feeding development-time OpenTelemetry traces to AI coding assistants to validate runtime assumptions and eliminate hallucinations.    |
| [Wasm't That Easy: Securing MCP With Wasm Sandboxes](fssjxqx7ccg.md)                                        | Jiaxiao Zhou (Microsoft) & Taylor Thomas (Akuity)        | Details secret exfiltration risks in MCP tool usage and introduces Waset, an open-source WebAssembly sandbox for deny-by-default execution.         |
| [You Got a Match! LLM Prefix Aware Routing With Kubernetes](8m6ucxlki2c.md)                                 | Ricardo Noriega (Red Hat) & Cong Liu                     | Details the Gateway API Inference Extension and LLMD for prefix-aware routing based on KV cache state to maximize throughput.                       |

## Concepts

- [Beyond Chat: Bringing Agents To Kubernetes - Nimisha Mehta, Confluent & Nina Polshakova, Solo.io](9ea4qk2ranq.md) - In this presentation, Nimisha and Nina introduce Kagent, a Kubernetes-native framework for building, running, and managing AI agents, emphasizing its declarative, cloud-native design and integration with Kubernetes features like security, s...
- [Cloud Native + Kubernetes AI Day | Closing Remarks - Yuzhui Lui & Yuan Tang](kzjtr-caiby.md) - The event concluded with expressions of gratitude to all attendees, platinum sponsors, diamond sponsors, and the startup sponsor, highlighting the event's popularity and strong support. Organizers reminded participants about a reception with.
- [Cloud Native + Kubernetes AI Day | Welcome + Opening Remarks - Ricardo Rocha & Rajas Kakodkar](lxxxfjwuqxc.md) - The speakers, Ricardo from CERN and Rajas from Broadcom, welcomed attendees to the Cloud Native and Kubernetes AI Day, expressing gratitude to participants, content submitters, and event sponsors. They emphasized the importance of the code...
- [Fit-to-Serve: How a New DRA Capability for Dynamic Device... Sunyanan Choochotkaew & Tatsuhiro Chiba](j6zkgxrxm6o.md) - The presentation discusses optimizing distributed AI model inference serving, focusing on resource allocation and scheduling challenges in Kubernetes environments. The speakers highlight the complexity of balancing workloads due to varying...
- [KServe Next: Advancing Generative AI Model Serving - Yuan Tang, Red Hat & Dan Sun, Bloomberg](vbrpeudn4tq.md) - The video features Yan Tan from Red Hat and Dan from Bloomberg introducing Queserve (Queso), a distributed, scalable, and standardized model inference platform for Kubernetes, supporting both generative and predictive AI workloads. They tra...
- [LMCache: Lower LLM Performance Costs in the Enterprise - Martin Hickey & Junchen Jiang](v4cnylxt9da.md) - The speakers at CubeCon Atlanta discuss the evolution of cloud infrastructure and AI workloads, highlighting the shift from concerns about virtual machines to the current focus on deploying and optimizing AI inference, particularly large la...
- [Lightning Talk: Mind the Topology: Smarter Scheduling for AI Workloads on Kubernetes - Roman Baron](o5i7ptwzjfo.md) - Roman Baron, a senior software engineer at Nvidia and maintainer of Sky Kaiuler, introduces the Kai scheduler, a Kubernetes-native scheduling framework optimized for AI workloads. He discusses the challenges of topology-aware scheduling, em...
- [Lightning Talk: My Job Says 'Running' but Nothing's Running: Kubernetes Status Reality... Ron Kahn](ahjzvt3vpac.md) - Ron, a senior software developer at Nvidia, discusses a common issue faced by AI researchers when running training jobs on Kubernetes: jobs appear to be running smoothly, but underlying network or connectivity errors can cause GPUs to sit i...
- [Lightning Talk: Resource Fairness and Utilization for Heterogeneous Batch/M... Yuki Iwai & Gabe Saba](dkhf-hzi7ci.md) - In this talk, Yuki from CyberAgent and Gabe from Google introduce Q, an AI workload scheduler designed to optimize resource allocation and fair sharing for heterogeneous batch machine learning platforms. Q operates as a secondary scheduler...
- [On-Call the Easy Way With Agents - Ryan Tay & Kartikeya Pharasi, Intuit](odli4cbkky8.md) - In this talk, Karthik and Ryan from Intuit’s service mesh team discuss their efforts to reduce the workload of on-call engineers by leveraging AI agents. They describe the scale at which Intuit operates—over 350 Kubernetes clusters and 16 b...
- [Panel: AI Infra Best Practices: Enterprise Do’s and Don’ts - Madhuri Yechuri & Andrew Leung](ketngeleq-k.md) - The discussion centers on Uber’s extensive experience building and operating AI infrastructure, particularly on Kubernetes, for both predictive models and emerging LLM-based use cases. Andrew Le Young from Uber explains that Uber’s AI power...
- [Sponsored Keynote: Autoscaling GPU Clusters Anywhere — Hyperscalers, Neoclouds & Ba... Lukas Gentele](lgoelo-ah30.md) - The speaker discusses the challenges of providing Kubernetes access on GPUs to engineering teams, highlighting the significantly higher costs compared to CPUs and the need for efficient resource allocation. To address this, the speaker intr...
- [Sponsored Keynote: Cloud-Native GraphRAG: AI’s Logical Edge - Stephen Chin, Neo4j](flldxr68nsi.md) - The speaker, who is VP at Neo Forj and content chair at the AI LFN Data Foundation, introduces a session focused on improving AI model quality and accuracy using graph RAG (Retrieval-Augmented Generation). After highlighting the importance...
- [Sponsored Keynote: From Open Source to Real-World Scale - Aleksandr Patrushev, Nebius](co6uottp-oy.md) - The speaker introduces Nibbus, a NASDAQ-listed, engineering-led company building AI cloud infrastructure designed to empower innovators of all sizes. Nibbus is a strategic Nvidia partner and is vertically integrated, handling everything from.
- [Sponsored Keynote: Kubernetes Challenges at Lambda - Andrew Godwin, Lambda Labs](7ldbcsobej4.md) - The speaker, Lambda’s lead software architect, provides an overview of the company’s approach to running GPU clouds and managing Kubernetes workloads. Lambda is an emerging hyperscaler that owns its hardware and infrastructure, running both...
- [The Hidden Foundation: How Effective Data Management Determines AI System Success - Keith McClellan](fidcxetnfho.md) - Ke Mlan, Field CTO for Splunk, discusses the challenges and best practices in preparing organizational data for successful AI adoption. He notes that most AI projects fail to deliver ROI, often due to issues in data integration and preparat...
- [This Lying Has To Stop: Keeping AI Honest with OpenTelemetry - Whitney Lee, Datadog](rwu7jxzboq8.md) - The speaker introduces Commit Story, an automated engineering journal app built with Cloud Code that uses AI to document code changes, commit messages, and developer-AI conversations triggered by Git commits. The app is heavily instrumented...
- [Wasm't That Easy: Securing MCP With Wasm Sandboxes - Jiaxiao Zhou, Microsoft & Taylor Thomas, Akuity](fssjxqx7ccg.md) - In this talk, Joe from Microsoft Azure and Taylor from Acuy discuss the security risks associated with running MCP (Machine Control Protocol) servers and tools, particularly when users copy and run arbitrary binaries or scripts from untrust...
- [You Got a Match! LLM Prefix Aware Routing With Kubernetes - Ricardo Noriega & Cong Liu](8m6ucxlki2c.md) - The presentation discusses the Gateway API Inference Extension, a Kubernetes project that enables AI-aware routing for inference workloads by transforming traditional gateways into smart proxies, known as inference gateways. This extension...
