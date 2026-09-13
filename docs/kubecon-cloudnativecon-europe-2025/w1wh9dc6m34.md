---
type: Video Note
title: "A Practical Guide To Kubernetes Policy as Code - Jim Bugwadia, Rita Zhang, Andy Suderman & Joe Betz"
description: "The Kubernetes policy as code guide focuses on using code to manage and enforce rules in a Kubernetes cluster. The goal is to simplify policy management and make it more accessible to developers, operators, and security teams. Three key too..."
resource: https://www.youtube.com/watch?v=w1wh9dc6m34
tags: ["kubecon-cloudnativecon-europe-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The Kubernetes policy as code guide focuses on using code to manage and enforce rules in a Kubernetes cluster.
The goal is to simplify policy management and make it more accessible to developers, operators, and security teams.
Three key tools are discussed: Kivero, Gatekeeper, and OPA (Open Policy Agent).
Kivero extends validating admission policies with additional features like image validation and background scanning.
Gatekeeper provides a dynamic, flexible, and multi-language policy engine that can be used for both Kubernetes and external targets.
OPA is a popular rule engine that has been integrated into Gatekeeper.
The tools are designed to work together to provide a comprehensive policy as code solution for Kubernetes.
# Main Points

|   # | Main point                                                                                                                                                                                                                                |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Policy is code is a way to manage and apply rules and conditions in Kubernetes.                                                                                                                                                           |
|   2 | There are many types of policies, including validating admission policy, mutating admission policy, network policy, cublet configurations, quotas, limit ranges, and resource quotas.                                                     |
|   3 | Policy as code has several benefits, including being more maintainable, efficient, and allowing for code review and inspection.                                                                                                           |
|   4 | Kubernetes provides a lot of different patterns for policy enforcement points, including admission web hooks and cell expressions.                                                                                                        |
|   5 | Cell is a programming language designed to be embedded into things like YAML, with properties such as being designed for single-line expressions, having a relatively unsurprising C-style syntax, and having low overhead for execution. |
|   6 | Validating admission policy allows for the use of cell expressions to enforce policies, while mutating admission policy returns a patch that mutates the object.                                                                          |
|   7 | Gatekeeper is a dynamic flexible emission and mutation web hook that can be used to enforce policies, with support for multiple languages including Rego and cell.                                                                        |
|   8 | Kivero is a project that aims to simplify policy management for Kubernetes, making it available to non-Kubernetes environments and providing standard life cycle management wherever possible.                                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=w1wh9dc6m34)