---
type: Video Note
title: "Project Lightning Talk: The Kyverno Five: New Policy Types And What You Can Do... Cortney Nickerson"
description: "Courtney Nickerson introduces Kyverno, a Kubernetes-native policy engine, and highlights its new policy types based on the Common Expression Language (CEL). She uses a concert metaphor to explain how Kubernetes acts as the stage and Kyverno..."
resource: https://www.youtube.com/watch?v=1WvHD-ihyfI
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Courtney Nickerson introduces Kyverno, a Kubernetes-native policy engine, and highlights its new policy types based on the Common Expression Language (CEL).
She uses a concert metaphor to explain how Kubernetes acts as the stage and Kyverno as the performer, with CEL-based policies providing enhanced capabilities through cleaner syntax, compiled expressions, and greater logical range.
The main policy types—validating, mutating, generating, image validating, and deleting—are described as band members, each with specific roles such as enforcing validations, modifying requests, creating resources, ensuring supply chain security, and cleaning up stale resources.
Additionally, Kyverno now includes CEL libraries, enabling advanced operations like querying resources and validating image metadata directly within policies.
The adoption of CEL aligns Kyverno with Kubernetes, resulting in improved performance and security, and the project welcomes new contributors and community engagement.
# Main Points

|   # | Main point                                                                                                                                                                                                         |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Kyverno is a Kubernetes-native policy engine.                                                                                                                                                                      |
|   2 | New policy types use Common Expression Language (CEL).                                                                                                                                                             |
|   3 | CEL-based policies offer cleaner syntax, compiled expressions for faster performance, and more logical operators/functions.                                                                                        |
|   4 | Kubernetes has adopted CEL, enabling better integration.                                                                                                                                                           |
|   5 | Kyverno policy types:                                                                                                                                                                                              |
|   6 | Validating Policy: Extends Kubernetes validating admission policy; supports Kyverno-specific features like spec evaluation, background scans, and arbitrary JSON payloads; uses CEL expressions to enforce labels. |
|   7 | Mutating Policy: Modifies requests using CEL-driven patches; supports declarative merges and JSON patch arrays; can inject sidecars or enforce resource limits.                                                    |
|   8 | Generating Policy: Creates supporting resources (e.g., config maps, secrets, network policies); can clone objects across namespaces; uses generator apply function; supports synchronization to mirror changes.    |
|   9 | Image Validating Policy: Enforces software supply chain security; restricts usage to trusted registries; requires attestations and signatures from services like SIGstore or cosign.                               |
|  10 | Deleting Policy: Handles cleanup of stale resources; runs on a schedule; deletes resources not matching CEL conditions.                                                                                            |
|  11 | CEL libraries are available, enabling queries on Kubernetes resources, image metadata validation, and time-based operations within CEL expressions.                                                                |
|  12 | CEL integration improves performance and communication between Kubernetes and Kyverno.                                                                                                                             |
|  13 | Collaboration between Kubernetes (conductor), Kyverno (performer), and CEL (score) enhances security and efficiency.                                                                                               |
|  14 | Kyverno welcomes contributions and engagement at the project pavilion, kiosk 13b.                                                                                                                                  |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=1WvHD-ihyfI)