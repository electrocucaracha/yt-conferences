---
type: Video Note
title: "Operators in Action: Making Kubernetes Work for You - Verena Traub, b'nerd GmbH"
description: "The speaker begins by introducing themselves and their background, then outlines the focus of the talk: how Kubernetes operators can help manage complex applications, using a recent case from their company as an example. The application in..."
resource: https://www.youtube.com/watch?v=V8fTE-SeVmg
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The speaker begins by introducing themselves and their background, then outlines the focus of the talk: how Kubernetes operators can help manage complex applications, using a recent case from their company as an example.
The application in question was not originally designed for Kubernetes and required handling multiple instances, dependencies, and custom configurations for different user packages.
The speaker explains the basics of Kubernetes operators, custom resource definitions (CRDs), and the reconciliation loop, then details how their team addressed challenges such as managing app dependencies, automating naming and credential generation, supporting different user profiles, reducing startup time with pre-warmed instance pools, integrating DNS, and coordinating with external services.
They emphasize the importance of carefully designing CRDs, leveraging existing operators and tools, modularizing logic, and documenting from the start.
The talk concludes with lessons learned about resource cleanup, testing, and debugging operators, and the speaker answers a question about deploying operators, noting their use of Flux for managing deployments and CRDs.
# Main Points

|   # | Main point                                                                                                                                           |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Speaker introduces talk on Kubernetes operators, sharing a recent case from their company.                                                           |
|   2 | Speaker's background: former tech/recruiting manager, web developer, AWS/cloud consultant at Berd, a managed service provider focused on Kubernetes. |
|   3 | Case involves deploying a legacy application not built for Kubernetes, with complex specifics and dependencies.                                      |
|   4 | Client wanted to offer the app as a service with different packages (basic, premium, ultimate) and expected high user volume.                        |
|   5 | Manual deployment with Helm was previously manageable but not scalable for hundreds of instances.                                                    |
|   6 | Operators chosen to automate deployment, configuration, and management of app instances.                                                             |
|   7 | Operators extend the Kubernetes API with custom resource definitions (CRDs), custom resources, and controller logic.                                 |
|   8 | Three main components for an operator: CRD (new API type), custom resource (desired state), operator (controller logic).                             |
|   9 | Example given of a simple CRD for a hello world app.                                                                                                 |
|  10 | Operator reconciliation loop ensures cluster state matches desired state in custom resources.                                                        |
|  11 | App-specific milestones addressed:                                                                                                                   |
|  12 | Handling dependencies (e.g., Redis, database, persistent volumes, ingress) by integrating existing operators.                                        |
|  13 | Automatic name and credential generation using random/haiku-style naming and secrets for passwords.                                                  |
|  14 | Supporting different profiles (basic, premium, ultimate) via separate CRDs for flexibility.                                                          |
|  15 | Managing long startup times with pre-warmed instance pools (pool CRD, cluster-scoped).                                                               |
|  16 | DNS integration handled via external DNS and cert-manager projects.                                                                                  |
|  17 | Managing external components (e.g., backends on VMs) via a control API for operator communication.                                                   |
|  18 | Operator manages pools, assigns instances to users, adapts configuration, and maintains pool size.                                                   |
|  19 | Learnings:                                                                                                                                           |
|  20 | Plan CRDs and logic structure early; splitting CRDs by logic is beneficial.                                                                          |
|  21 | Leverage existing operators and tools where possible.                                                                                                |
|  22 | Cleaning up resources is complex; use finalizers and plan                                                                                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=V8fTE-SeVmg)