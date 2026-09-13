---
type: Video Note
title: "Policy Engines for Kubernetes: Picking One Without Losing Your Mind - Nabarun Pal, Broadcom"
description: "In this talk, Nabarun discusses the complexities of policy enforcement in Kubernetes, emphasizing that while it may seem simple, real-world scenarios—such as compliance, cost control, and operational reliability—make it challenging, especia..."
resource: https://www.youtube.com/watch?v=y5rrfSZBm1A
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Nabarun discusses the complexities of policy enforcement in Kubernetes, emphasizing that while it may seem simple, real-world scenarios—such as compliance, cost control, and operational reliability—make it challenging, especially at scale.
He reviews several policy enforcement solutions in the cloud native ecosystem: Kubernetes native validating admission policies (which are simple, require no extra components, but have limitations in complexity and features), Kyverno (YAML-based, easy to adopt, supports validation, mutation, generation, and image verification, but is Kubernetes-specific), and Gatekeeper/Open Policy Agent (OPA), which uses the Rego language for highly expressive, cross-resource, and cross-platform policies, though it comes with a steeper learning curve and higher resource requirements.
He also briefly mentions Kubewarden, which leverages WebAssembly for language flexibility and distribution but is more specialized and less mature.
Nabarun provides practical advice on selecting a policy engine based on needs such as mutation, image verification, and cross-platform support, and recommends starting with audit mode, planning for exceptions, and treating policy engines as critical infrastructure.
He concludes that there is no universal best choice; teams should start simple, grow as needed, and always consider operational realities and future migration paths.
# Main Points

|   # | Main point                                                                                                                                                                   |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Policy enforcement in Kubernetes is complex, especially at scale.                                                                                                            |
|   2 | Different teams and products may handle policy enforcement differently, leading to inconsistencies.                                                                          |
|   3 | Compliance requirements (HIPAA, PCI, GDPR) necessitate audit logs and audit trails, not just policy declarations.                                                            |
|   4 | Policy enforcement helps with cost control, operational sanity, and reduces on-call incidents.                                                                               |
|   5 | Key parameters for selecting a policy engine: policy language expressiveness, ease of adoption, operational overhead, failure modes, integration with CI/CD, auditability.   |
|   6 | Failure modes: Start with ignore mode, prove stability, then move to blocking mode; be aware of Kubernetes webhook 30-second timeout.                                        |
|   7 | Integration: Policy engines should support pre-deployment validation and fit into CI/CD workflows.                                                                           |
|   8 | Auditability: Audit logs are essential for compliance and proving policy enforcement.                                                                                        |
|   9 | Kubernetes native validating admission policy uses Common Expression Language (CEL), requires no extra components, and is suitable for simple checks.                        |
|  10 | Limitations of native policies: cannot perform complex data operations, HTTP calls, or image verification; mutation support is coming in Kubernetes 1.36.                    |
|  11 | Kyverno: YAML-based, easy to adopt, supports validate, mutate, generate, and image verification policies; supports background scanning and compliance reporting.             |
|  12 | Kyverno is Kubernetes-only and not suitable for non-Kubernetes resources.                                                                                                    |
|  13 | Open Policy Agent (OPA) and Gatekeeper: OPA is general-purpose, Gatekeeper is Kubernetes-specific; uses Rego language for expressive policies and cross-resource validation. |
|  14 | Gatekeeper enables centralized governance with distributed control; memory usage increases with cross-resource syncing.                                                      |
|  15 | OPA is suitable for organizations needing unified policy across multiple platforms and clouds.                                                                               |
|  16 | Gatekeeper/OPA have a steeper learning curve and higher resource requirements.                                                                                               |
|  17 | Kubewarden: Uses WebAssembly, supports multiple languages, high security, but has higher comple                                                                              |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=y5rrfSZBm1A)