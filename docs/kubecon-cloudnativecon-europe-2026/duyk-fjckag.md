---
type: Video Note
title: "Why Is It So Hard to Run a 5G Core on Kubernetes—And What Needs... Joel Studler & Ashan Senevirathne"
description: "The presentation discusses the challenges and progress of running 5G mobile core networks on Kubernetes, as experienced by operators Telstra and Swisscom. While 5G cores are now containerized and deployed on Kubernetes with some GitOps and..."
resource: https://www.youtube.com/watch?v=duYk-FjcKAg
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The presentation discusses the challenges and progress of running 5G mobile core networks on Kubernetes, as experienced by operators Telstra and Swisscom.
While 5G cores are now containerized and deployed on Kubernetes with some GitOps and CI/CD capabilities, the industry often fails to fully leverage Kubernetes’ native features due to legacy telco mindsets and operational habits, such as using static IPs, manual configurations, and external high-availability logic.
This results in bypassing Kubernetes’ strengths like declarative configuration, automated scaling, and self-healing, leading to increased complexity and operational bottlenecks.
Industry voices from Ericsson, Orange, and Vodafone highlight the need to move away from “lift and shift” approaches and legacy protocols like netconf, advocating for true cloud-native design, automation, and abstraction to realize the benefits of Kubernetes.
The speakers emphasize that while Kubernetes is not failing telco, the real transformation will come from adopting service-oriented, declarative, and resilient architectures—lessons that must be embraced for 6G, which should be cloud-native by design rather than retrofit.
The session concludes by encouraging collaboration across operators, vendors, and standards bodies, and highlights ongoing industry initiatives aimed at closing the gap between telco and cloud-native operations.
# Main Points

|   # | Main point                                                                                                                                                                     |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | 5G mobile core networks are increasingly running on Kubernetes.                                                                                                                |
|   2 | Mobile data traffic is predicted to triple by 2031, increasing network complexity.                                                                                             |
|   3 | Operators are expected to manage growing, complex networks with the same workforce.                                                                                            |
|   4 | 5G core consists of a distributed control plane (authentication, user data, sessions) and a user plane function (high-speed packet forwarding).                                |
|   5 | The system is highly standards-driven and requires carrier-grade reliability.                                                                                                  |
|   6 | 5G cores at Telstra and Swisscom are containerized, Kubernetes-based, mostly GitOps-driven, with some CI/CD capabilities.                                                      |
|   7 | Network engineers are beginning to operate workloads on Kubernetes, integrating Telco and cloud-native practices.                                                              |
|   8 | Industry feedback highlights the need for a more cloud-native operating model to fully realize Kubernetes benefits and reduce costs.                                           |
|   9 | Current deployments often containerize legacy applications without leveraging Kubernetes features, leading to mismatches in networking, lifecycle management, and reliability. |
|  10 | Networking: Telcos use static IPs, virtual NICs, and manual management, bypassing Kubernetes networking.                                                                       |
|  11 | Lifecycle: Configuration remains imperative and complex (e.g., netconf with 2,000+ parameters), not declarative.                                                               |
|  12 | Reliability: Failures trigger manual, slow recovery processes instead of Kubernetes self-healing.                                                                              |
|  13 | Example: UPF deployments bypass Kubernetes networking and orchestration for performance, losing auto-scaling and automation benefits.                                          |
|  14 | Recommendations: Leverage Kubernetes IPAM, load balancing, DNS, auto-scaling, declarative configuration; reduce reliance on netconf.                                           |
|  15 | Transition is ongoing: mix of physical, virtual, containerized, and cloud-native network functions.                                                                            |
|  16 | Operators are adopting GitOps, Kubernetes resource models, and automation platforms (e.g., Swisscom’s platform using NetBox, Flux CD).                                         |
|  17 | Vendors must provide true cloud-native APIs, not just appliance wrappers.                                                                                                      |
|  18 | Standards bodies (3GPP, ETSI) are moving slowly but in the right direction.                                                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=duYk-FjcKAg)