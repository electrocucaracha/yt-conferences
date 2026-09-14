---
layout: default
title: "Executive Report: Cloud Native + Kubernetes AI Day 2025 NA"
parent: "Cloud Native Kubernetes Ai Day 2025 Na"
nav_order: 1
type: "Executive Report"
okf_version: "0.2"
description: "Executive report and summary of the Cloud Native + Kubernetes AI Day 2025 NA conference."
tags:
  - cloud-native-kubernetes-ai-day-2025-na
  - executive-report
status: stable
---

# Executive Report: Cloud Native + Kubernetes AI Day 2025 NA

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

## Sessions & Talks Summary

| Talk Title                                                                                | Speaker & Organization                                   | Document                         | Core Thesis & Strategic Insight                                                                                                                     |
| :---------------------------------------------------------------------------------------- | :------------------------------------------------------- | :------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cloud Native + Kubernetes AI Day \| Welcome + Opening Remarks                             | Ricardo Rocha (CERN) & Rajas Kakodkar (Broadcom)         | [lxxxfjwuqxc.md](lxxxfjwuqxc.md) | Opens the conference, detailing CNCF AI working group initiatives, white papers, community working groups, and event logistics.                     |
| Beyond Chat: Bringing Agents To Kubernetes                                                | Nimisha Mehta (Confluent) & Nina Polshakova (Solo.io)    | [9ea4qk2ranq.md](9ea4qk2ranq.md) | Introduces Kagent, a declarative framework for running autonomous infrastructure AI agents with RBAC, CRDs, and MCP integration.                    |
| Fit-to-Serve: How a New DRA Capability for Dynamic Device...                              | Sunyanan Choochotkaew & Tatsuhiro Chiba (IBM Research)   | [j6zkgxrxm6o.md](j6zkgxrxm6o.md) | Demonstrates Device Resource Allocation (DRA) consumable capacity for fine-grained GPU slicing and dynamic memory allocation in inference serving.  |
| KServe Next: Advancing Generative AI Model Serving                                        | Yuan Tang (Red Hat) & Dan Sun (Bloomberg)                | [vbrpeudn4tq.md](vbrpeudn4tq.md) | Presents KServe 0.16 evolution as a CNCF incubating project unifying predictive and generative AI inference with disaggregated serving.             |
| LMCache: Lower LLM Performance Costs in the Enterprise                                    | Martin Hickey (IBM / PyTorch) & Junchen Jiang (UChicago) | [v4cnylxt9da.md](v4cnylxt9da.md) | Introduces LMCache for offloading, sharing, and persistently storing KV caches across GPU, CPU, and remote storage backends.                        |
| Lightning Talk: Mind the Topology: Smarter Scheduling for AI Workloads on Kubernetes      | Roman Baron (Nvidia)                                     | [o5i7ptwzjfo.md](o5i7ptwzjfo.md) | Details the Kai scheduler for topology-aware placement of multi-pod AI workloads across racks and zones based on interconnect bandwidth.            |
| Lightning Talk: My Job Says 'Running' but Nothing's Running: Kubernetes Status Reality... | Ron Kahn (Nvidia)                                        | [ahjzvt3vpac.md](ahjzvt3vpac.md) | Highlights the gap between K8s readiness probes and true AI training progress, advocating pre-flight connectivity checks and continuous validation. |
| Lightning Talk: Resource Fairness and Utilization for Heterogeneous Batch/M...            | Yuki Iwai (CyberAgent) & Gabe Saba (Google)              | [dkhf-hzi7ci.md](dkhf-hzi7ci.md) | Explains Q, a secondary Kubernetes scheduler using Dominant Resource Share (DRS) and usage penalties for fair GPU queue allocation and preemption.  |
| On-Call the Easy Way With Agents                                                          | Ryan Tay & Kartikeya Pharasi (Intuit)                    | [odli4cbkky8.md](odli4cbkky8.md) | Shows Intuit's AI on-call agent system leveraging RAG and automated runbooks to analyze telemetry and reduce incident MTTR at enterprise scale.     |
| Panel: AI Infra Best Practices: Enterprise Do’s and Don’ts                                | Madhuri Yechuri & Andrew Leung (Uber)                    | [ketngeleq-k.md](ketngeleq-k.md) | Shares Uber's AI infrastructure journey, emphasizing multi-cloud strategy, compute/data locality, and CPU/GPU workload disaggregation.              |
| Sponsored Keynote: Autoscaling GPU Clusters Anywhere — Hyperscalers, Neoclouds & Ba...    | Lukas Gentele (Loft Labs)                                | [lgoelo-ah30.md](lgoelo-ah30.md) | Presents vCluster and AWS Karpenter integration for cost-effective virtual cluster isolation and dynamic GPU autoscaling.                           |
| Sponsored Keynote: Cloud-Native GraphRAG: AI’s Logical Edge                               | Stephen Chin (Neo4j)                                     | [flldxr68nsi.md](flldxr68nsi.md) | Demonstrates GraphRAG for enhancing model accuracy and logical reasoning by structuring enterprise documents in graph databases.                    |
| Sponsored Keynote: From Open Source to Real-World Scale                                   | Aleksandr Patrushev (Nebius)                             | [co6uottp-oy.md](co6uottp-oy.md) | Outlines Nebius's vertically integrated AI cloud platform combining Kubernetes, Slurm operators, and custom virtualization for physical GPU speed.  |
| Sponsored Keynote: Kubernetes Challenges at Lambda                                        | Andrew Godwin (Lambda Labs)                              | [7ldbcsobej4.md](7ldbcsobej4.md) | Examines GPU hardware failure rates and Lambda's automated remediation framework using K8s operators and bare-metal Cluster API.                    |
| The Hidden Foundation: How Effective Data Management Determines AI System Success         | Keith McClellan (Splunk)                                 | [fidcxetnfho.md](fidcxetnfho.md) | Addresses data integration hurdles in AI adoption, advocating OpenTelemetry, ABAC, and in-place data processing to prevent project failures.        |
| This Lying Has To Stop: Keeping AI Honest with OpenTelemetry                              | Whitney Lee (Datadog)                                    | [rwu7jxzboq8.md](rwu7jxzboq8.md) | Demonstrates feeding development-time OpenTelemetry traces to AI coding assistants to validate runtime assumptions and eliminate hallucinations.    |
| Wasm't That Easy: Securing MCP With Wasm Sandboxes                                        | Jiaxiao Zhou (Microsoft) & Taylor Thomas (Akuity)        | [fssjxqx7ccg.md](fssjxqx7ccg.md) | Details secret exfiltration risks in MCP tool usage and introduces Waset, an open-source WebAssembly sandbox for deny-by-default execution.         |
| You Got a Match! LLM Prefix Aware Routing With Kubernetes                                 | Ricardo Noriega (Red Hat) & Cong Liu                     | [8m6ucxlki2c.md](8m6ucxlki2c.md) | Details the Gateway API Inference Extension and LLMD for prefix-aware routing based on KV cache state to maximize throughput.                       |
| Cloud Native + Kubernetes AI Day \| Closing Remarks                                       | Yuzhui Lui & Yuan Tang                                   | [kzjtr-caiby.md](kzjtr-caiby.md) | Concludes the event with acknowledgments to attendees, sponsors, and community organizers.                                                          |
