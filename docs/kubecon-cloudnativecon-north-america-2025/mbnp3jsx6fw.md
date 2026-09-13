---
layout: default
title: The Enterprise Is Ready for gRPC - Alex Van Boxel, Collibra
nav_order: 305
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  In this talk, Alex, a principal architect at Calibra, discusses the benefits
  of using gRPC and its ecosystem for enterprise solutions, focusing on its compact
  binary format, extensibility, and robust versioning. He explains how gRPC, built...
resource: https://www.youtube.com/watch?v=mbnP3jSx6fw
tags:
  - kubecon-cloudnativecon-north-america-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

In this talk, Alex, a principal architect at Calibra, discusses the benefits of using gRPC and its ecosystem for enterprise solutions, focusing on its compact binary format, extensibility, and robust versioning.
He explains how gRPC, built on Protocol Buffers (proto), efficiently encodes data using tags and wire types, enabling compact storage and easy evolution of data contracts through unknown fields and descriptors.
Alex highlights the advantages of proto’s domain-specific language for contract definition, inline documentation, and deprecation management, making it accessible even to less technical users and supporting smooth versioning.
He emphasizes the reuse of messages across RPC and messaging systems, the canonical conversion from proto to JSON, and the ability to generate REST interfaces via tools like gRPC Gateway and Envoy.
Finally, Alex notes that adopting gRPC can help modularize monolithic systems and facilitate future scalability, underscoring the unified approach to data contracts as a key selling point for enterprises.

# Main Points

|   # | Main point                                                                                                                                                    |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Speaker is Alex, principal architect at Calibra, a data governance company using cloud-native technologies and Kubernetes.                                    |
|   2 | Focus of talk is on gRPC and its ecosystem, especially for enterprise solutions.                                                                              |
|   3 | gRPC is a high-performance, open-source framework built on Protocol Buffers (proto).                                                                          |
|   4 | Binary format in gRPC is compact, using continuation bits and variable-length encoding for efficient storage.                                                 |
|   5 | Uses TLV (Tag, Length, Value) system; tags are numbers instead of names, making messages smaller and aiding compatibility.                                    |
|   6 | Six wire types exist; two deprecated; main types are length-delimited, fixed32, and fixed64.                                                                  |
|   7 | Unknown fields are supported, allowing forward and backward compatibility and contract evolution without breaking consumers or producers.                     |
|   8 | Proto definitions can be stored as descriptors, enabling server reflection and unified parsing across languages.                                              |
|   9 | Server reflection allows clients to discover services and methods dynamically.                                                                                |
|  10 | gRPC offers more compact and cost-effective data transfer compared to JSON, especially for network traffic.                                                   |
|  11 | Domain-specific language (DSL) for proto is user-friendly and more approachable than YAML for non-technical users.                                            |
|  12 | Strong versioning strategy: copy all definitions for new versions, avoid importing from previous versions, and use tags for evolution.                        |
|  13 | Inline documentation and deprecation flags are supported and included in descriptors.                                                                         |
|  14 | Renaming fields is possible without breaking binary compatibility.                                                                                            |
|  15 | Google and Uber API design guidelines are recommended; tools like buf help validate and enforce rules.                                                        |
|  16 | Proto and gRPC enable strong reuse of messages and contracts for both RPC and messaging, using the same tooling and data objects.                             |
|  17 | Canonical way to convert proto to JSON is provided; gRPC JSON gateway and tools like Go Gateway and Envoy can generate REST interfaces from gRPC definitions. |
|  18 | gRPC can help modularize monoliths and ease future system breakups without changing interfaces.                                                               |
|  19 | Unified RPC/message                                                                                                                                           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=mbnP3jSx6fw)
