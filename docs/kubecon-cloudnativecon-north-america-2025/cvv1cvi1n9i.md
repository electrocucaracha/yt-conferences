---
type: Video Note
title: "The Myth of Portability: Why Your Cloud Native App Is Married To Your Provider - Corey Quinn"
description: "In this talk, Corey Quinn critiques the common practice of over-engineering for cloud portability, likening it to preppers obsessively preparing bugout bags for disasters that never match reality. He argues that many organizations invest he..."
resource: https://www.youtube.com/watch?v=cvv1cVi1n9I
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Corey Quinn critiques the common practice of over-engineering for cloud portability, likening it to preppers obsessively preparing bugout bags for disasters that never match reality.
He argues that many organizations invest heavily in cloud-agnostic architectures—using Kubernetes, avoiding managed services, and maintaining complex migration plans—only to end up with expensive, inefficient systems that fail to deliver the promised flexibility.
Quinn contends that true lock-in is not to a specific cloud provider’s APIs, but to the expertise and operational knowledge teams develop over time, making switching providers far more costly and disruptive than anticipated.
He warns that pursuing multicloud redundancy often doubles operational burdens and failure points without real benefit, and that the real disaster is burning out engineers with unnecessary complexity.
Ultimately, Quinn advises choosing a primary cloud, leveraging managed services, and optimizing for team well-being and operational simplicity rather than chasing the myth of effortless portability.
# Main Points

|   # | Main point                                                                                                                                                |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Preppers meticulously prepare bugout bags but often fail to use them in real disasters due to mismatched threat models.                                   |
|   2 | Many organizations similarly prepare for the wrong cloud disaster, focusing on portability over practical needs.                                          |
|   3 | The cloud native ecosystem promotes portability and freedom from vendor lock-in, often via Kubernetes and abstraction.                                    |
|   4 | In practice, Kubernetes and cloud abstraction promise portability but rarely deliver it in production environments.                                       |
|   5 | Startups often over-engineer with Kubernetes and microservices, solving problems they don’t actually have.                                                |
|   6 | The common playbook: use Kubernetes, avoid managed services, run your own databases and observability, and stay on foundational services for portability. |
|   7 | This approach leads to high costs, operational complexity, and untested disaster recovery plans.                                                          |
|   8 | Organizations end up building expensive, unreliable data centers in the cloud, losing the benefits of managed services.                                   |
|   9 | Portability is rarely exercised; switching clouds is difficult, time-consuming, and requires relearning everything.                                       |
|  10 | Attempting active-active multicloud increases failure points, operational burden, attack surface, and cognitive load without true redundancy.             |
|  11 | Teams are typically only experts in one cloud; outages in secondary clouds are harder to resolve.                                                         |
|  12 | The real lock-in is team expertise, not APIs or services; switching clouds means losing accumulated knowledge.                                            |
|  13 | You must choose your lock-in: managed services or self-managed infrastructure—either way, you’re on call.                                                 |
|  14 | Managed services align better with competitive advantage and reduce toil.                                                                                 |
|  15 | Using different clouds for different apps or services is practical; this is not true multicloud.                                                          |
|  16 | The myth of portability distracts from the real risk: burning out engineers with unnecessary complexity.                                                  |
|  17 | Optimize for reliability and team well-being, not theoretical portability.                                                                                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=cvv1cVi1n9I)