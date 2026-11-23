---
layout: default
title: "Executive Report: OpenInfra Summit Europe 2025"
parent: OpenInfra Summit Europe 2025
nav_order: 1
type: Executive Report
okf_version: "0.2"
description: Executive report and summary of the OpenInfra Summit Europe 2025 conference.
tags:
  - openinfra-summit-europe-2025
  - executive-report
status: stable
---

# Executive Report: OpenInfra Summit Europe 2025

## Executive Overview

The OpenInfra Summit Europe 2025 marked a decisive strategic pivot within the open infrastructure ecosystem, transitioning from simple adoption to a focus on deep operational resilience, security, and AI-readiness.
A dominant theme across keynotes and technical sessions was the urgent imperative to decouple from proprietary vendor lock-in, particularly in response to the VMware-Broadcom acquisition.
This was validated through multiple live migration showcases where organizations successfully transitioned workloads to OpenStack using tools like Coriolis, Ansible, and Zikcom, establishing OpenStack as a robust, zero-downtime alternative.
Simultaneously, the summit highlighted the maturation of OpenStack’s networking and storage layers to support high-performance AI workloads.
Technical deep dives revealed significant architectural advancements, including the transition to Layer 3 BGP-based networking for scalability, the optimization of RabbitMQ queue management to resolve production instability, and the integration of Ceph with NVMe/TCP to eliminate I/O bottlenecks.
These improvements are critical as the industry addresses growing demand for high-throughput data processing, with Ceph’s new erasure coding optimizations doubling sustainable IOPS capacity.
Security and confidentiality emerged as the second major pillar, driven by the need to protect intellectual property in AI-driven environments.
Presentations detailed the use of Confidential Containers, Kata Containers, and trusted execution environments to secure AI agents and large language models, ensuring sensitive data remains protected even in multi-tenant or hybrid cloud scenarios.
This focus on "resilience over sovereignty" was reinforced by the Open Infra Foundation’s push for policy advocacy and the integration of open standards like Linux, OpenStack, and Kubernetes.
Furthermore, the summit showcased the increasing automation of infrastructure operations, with demonstrations of AI agents using Retrieval-Augmented Generation (RAG) and Model Context Protocol (MCP) to automate OpenStack resource management and root cause analysis.
The event also highlighted the critical role of open infrastructure in critical sectors, with case studies from CERN, ECMWF, and BMW illustrating how OpenStack supports massive-scale scientific research, weather forecasting, and automotive software development.
The summit also underscored a pivotal shift toward digital sovereignty, with a consensus that open-source stacks are essential for maintaining data control, reducing total cost of ownership, and meeting emerging government mandates for technological independence.
This sovereign imperative is being realized through advanced architectural innovations, such as KT Cloud’s unified networking layer using OVN for both Kubernetes and OpenStack, and CERN’s phased migration to OVN to modernize its high-performance computing environment.
Additionally, the summit showcased significant progress in multi-architecture support, with Graphcore and StackHPC demonstrating how to achieve feature parity between x86 and ARM64 fleets, thereby expanding the hardware ecosystem available to open-infrastructure users.
The industry is also actively working to address hardware fragmentation in the AI sector, with initiatives like FlagOS and China Mobile’s Kana platform aiming to create an "Android for AI," enabling seamless migration across diverse accelerators including NVIDIA, AMD, Intel, and Huawei to eliminate "CUDA lock-in." Operational maturity and sustainability were key takeaways, with insights from StackHPC on managing over 100 OpenStack upgrades and the introduction of a new Rust-based CLI for improved performance.
Energy efficiency emerged as a critical operational concern, with proposals for a "Cloud Green Brain" to dynamically manage hardware states and reduce idle power consumption, reflecting a broader industry commitment to sustainable computing.
GreenOps methodologies, exemplified by the Cartel application, demonstrate how DevOps practices can reduce carbon emissions by approximately 13% through temporal shifting of workloads to periods of high renewable energy availability.
Despite these advancements, the industry faces a persistent challenge in the form of a skilled talent shortage, prompting a collective call for stronger community collaboration, improved documentation, and standardized training to sustain the growth of open infrastructure globally.
The Open Infra Foundation is actively fostering community engagement through initiatives like the VMware migration working group and the sponsorship of ROI surveys, aiming to secure long-term investment and governance improvements.
Looking ahead, the industry is poised for further integration of AI-native features, including holistic resource optimization, carbon footprint monitoring, and the expansion of open-source standards for non-terrestrial networks and industrial-grade AI.
The consensus is clear: success in this evolving landscape depends on a collaborative approach that prioritizes upstream development, robust security practices, and the continuous adaptation of open infrastructure to meet the demands of next-generation computing.
The summit concluded with a strong emphasis on community collaboration, as seen in the Open Infra for AI working group’s plans to standardize AI gateways and the Model Pack specification, which leverages OCI standards to treat LLMs as first-class citizens in cloud-native environments.
Collectively, these developments signal a maturing open infrastructure ecosystem that is increasingly capable of meeting the rigorous demands of AI, security, and sovereignty, positioning it as a viable and resilient alternative to proprietary cloud solutions.
The emphasis on sensible defaults, as advocated by Open Telekom Cloud, suggests a move away from overwhelming configuration choices toward streamlined, reliable platforms that allow developers to
