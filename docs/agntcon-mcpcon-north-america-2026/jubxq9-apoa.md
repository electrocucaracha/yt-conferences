---
layout: default
title: "Interoperable Agent Discovery: AI Catalog, ARD... - Luca Muscariello, Cisco & Junjie Bu, Google"
nav_order: 19
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Jinjaipou and Luca from Google present a framework for discovering and verifying Agentic AI resources, addressing the scalability issues of manual installation and trust verification."
resource: "https://www.youtube.com/watch?v=JUBXq9-apOA"
tags:
  - agntcon-mcpcon-north-america-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-08T02:03:18+00:00
---

# Summary

Jinjaipou and Luca from Google present a framework for discovering and verifying Agentic AI resources, addressing the scalability issues of manual installation and trust verification.
They propose a common metadata model that includes resource name, type, and location, allowing clients to dynamically find tools like skills, plugins, and agents without needing to know them in advance.
To ensure security, the framework introduces a "trust manifest" that binds cryptographic attestations—such as provenance, compliance scans, and runtime evaluations—to the resource, enabling zero-trust verification by any party.
Luca illustrates this with a wine-selling agent example, demonstrating how clients can semantically search for services and verify their identity and integrity using standards like DID Web and Cosign before interaction.
The system supports both static catalogs and dynamic registries, allowing enterprises to manage policies and swap resources seamlessly while maintaining stable identifiers and automated discovery of new capabilities.

# Main Points

|   # | Main point                                                                                                                                                                         |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | (skills, plugins, agents) is largely manual, involving manual installation, location finding, and trust verification, which is not scalable.                                       |
|   2 | , focusing on simplicity with fields for name, type, and location.                                                                                                                 |
|   3 | "Trust Manifest" is defined to bind identity and attestation claims (compliance, security scans, provenance, runtime evaluations) to resources using cryptographic algorithms.     |
|   4 | , cryptography-verified validation where any party (registry, client, or third party) can independently verify resource claims without relying solely on a central authority.      |
|   5 | "well-known" files for small sets to dynamic registries for large-scale enterprise or public use, supporting natural language queries for capability search.                       |
|   6 | (supply chain security, provenance of components) and runtime discovery (verifying live agent identity and behavior).                                                              |
|   7 | : semantically searching for sellers, verifying their identity via DID Web identifiers and public keys, and confirming the specific running instance matches the published card.   |
|   8 | , using existing tools like Cosign and SLSA for software provenance and trust manifests for deployment identity.                                                                   |
|   9 | , allowing clients to find and securely bind to agents running in various environments (cloud, Kubernetes) using private identities like SPIFFE.                                   |
|  10 | (applying rules like HIPAA compliance or trust scores to any new resource), swappability (replacing agents while keeping stable identifiers), and automated discovery for clients. |
|  11 | (ARD) are community efforts involving partners like Google, Anthropic, AWS, and Cisco, aiming for compatible data models despite being in different working groups.                |
|  12 | , but the standard eliminates the need for manual configuration changes when new resources are published to a catalog or registry.                                                 |
|  13 | , verify, publish, and find Agentic AI resources, ensuring trust and scalability as capabilities grow.                                                                             |

# Video

[![Video thumbnail](https://img.youtube.com/vi/JUBXq9-apOA/hqdefault.jpg)](https://www.youtube.com/watch?v=JUBXq9-apOA)

[Watch on YouTube](https://www.youtube.com/watch?v=JUBXq9-apOA)
