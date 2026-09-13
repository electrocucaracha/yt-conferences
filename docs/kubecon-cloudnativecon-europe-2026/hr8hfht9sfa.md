---
type: Video Note
title: "How to Build a European Cloud Orchestration Platform From With... Maximilian Techritz & Johannes Ott"
description: "In this presentation, Johannes and Max from SAP share their three-year journey building a European cloud orchestration platform within their enterprise, which has now been open sourced and donated to the Neonos Foundation under the Linux Fo..."
resource: https://www.youtube.com/watch?v=hR8hFht9sFA
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this presentation, Johannes and Max from SAP share their three-year journey building a European cloud orchestration platform within their enterprise, which has now been open sourced and donated to the Neonos Foundation under the Linux Foundation Europe.
They identified the complexity and inefficiency caused by disparate tools and manual processes in cloud configuration, especially across diverse environments and teams with varying Kubernetes expertise.
Their solution was to unify orchestration using the Kubernetes resource model and open source tools like Crossplane, External Secrets Operator, and Flux, culminating in the creation of Open Control Plane—a self-service, extensible control plane as a service that simplifies adoption for all engineers.
To drive adoption, they invested heavily in community building, enablement materials, workshops, and contribution guides, fostering a collaborative culture that empowered teams to contribute and extend the platform.
As a result, they have seen significant improvements in rollout speed and operational confidence, and they invite others to join their growing community to further develop and benefit from this open ecosystem.
# Main Points

|   # | Main point                                                                                                                                                                          |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation on building a European cloud orchestration platform within an enterprise                                                                                               |
|   2 | Project originated at SAP, now open sourced and donated to the Neonos Foundation (Linux Foundation Europe)                                                                          |
|   3 | Team of ~45 engineers, serving 500+ stakeholders and 100+ contributors                                                                                                              |
|   4 | Identified problem: excessive complexity and tool fragmentation in cloud landscape orchestration                                                                                    |
|   5 | Common issues: multiple tools (Kubernetes, GitHub Actions, Jenkins, Terraform, ClickOps), lack of alignment, high error rates, wasted engineering time                              |
|   6 | Goal: unify engineering teams under a single methodology for orchestration                                                                                                          |
|   7 | Solution: leverage Kubernetes resource model for all aspects of application stack                                                                                                   |
|   8 | Utilized open source tools: Crossplane (manage databases, DNS, storage), External Secrets Operator (sync secrets), Open Policy Agent/Cyano (custom policies), GitOps (Flux, ArgoCD) |
|   9 | Encouraged teams to adopt these tools, resulting in increased automation and satisfaction                                                                                           |
|  10 | Remaining challenge: onboarding users with limited/no Kubernetes experience and handling proprietary/internal APIs without existing operators/providers                             |
|  11 | Developed Open Control Plane: open source, extensible control plane as a service, pre-installs/configures key tools, supports major cloud providers and local setups                |
|  12 | Open Control Plane enables self-service, supports internal Kubernetes operators, and is available for demo                                                                          |
|  13 | Focused on people and culture: monthly informal sessions, beginner-friendly enablement materials, workshops, hackathons, reusable code samples, and contribution guides             |
|  14 | Emphasis on community building and shared problem-solving across the organization                                                                                                   |
|  15 | Adoption led to significant reduction in cloud rollout time and increased operational confidence                                                                                    |
|  16 | Key takeaways: address relevant pain points, enable users with zero Kubernetes experience, foster a community of practice, never build a platform without user involvement          |
|  17 | Invitation to join community calls, access documentation, and participate in the proj                                                                                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=hR8hFht9sFA)