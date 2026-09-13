---
type: Video Note
title: "Straight Into the Deep End! Learning Kubernetes and Cloud Native From... Éamon Ryan & Ayah Elshaikh"
description: "In this talk, Aean Ryan and Ya Alshik from Grafana Labs share their experiences learning Kubernetes and cloud-native technologies from scratch, highlighting the challenges and complexities faced by newcomers, especially given Kubernetes' ma..."
resource: https://www.youtube.com/watch?v=Ctm0jjPZV1M
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Aean Ryan and Ya Alshik from Grafana Labs share their experiences learning Kubernetes and cloud-native technologies from scratch, highlighting the challenges and complexities faced by newcomers, especially given Kubernetes' maturity and evolving feature set.
They discuss the steep learning curve, noting that while basic concepts like pods, nodes, and deployments seem straightforward at first, deeper exploration reveals significant nuance and confusion, particularly around constructs like stateful sets, replica sets, daemon sets, Helm charts, operators, and ingress, which often behave differently across cloud providers.
Ya emphasizes the difficulty of finding resources that don't assume prior knowledge, and describes how hands-on tools like K9s, real development environments, and interactive tutorials (such as those from CodeCloud) were more effective for learning than verbose documentation or lengthy videos.
The speakers also point out that while the abundance of documentation and community support can be overwhelming, it ultimately benefits learners by providing answers to nearly any problem.
They conclude by recommending a practical, hands-on approach to certification preparation, leveraging CodeCloud courses and official practice exams, and encourage learners to fill in knowledge gaps as needed.
# Main Points

|   # | Main point                                                                                                                                                                                                                                                     |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The talk is titled "Straight into the deep end: learning Kubernetes and cloud native from scratch in late 2024."                                                                                                                                               |
|   2 | Speakers: Aean Ryan (Senior Principal Field Engineer, Grafana Labs, 5.5 years experience, metrics/infrastructure/Kubernetes) and Ya Alshik (Senior Field Engineer, Grafana Labs, 1 year 3 months, traces/infrastructure, prior embedded software/simulations). |
|   3 | Kubernetes v1.0 released July 21, 2015; latest minor version is 1.34 (August 2025); 1.35 in alpha.                                                                                                                                                             |
|   4 | Kubernetes has evolved significantly, adding features like custom resource definitions, policy management, CoreDNS, storage improvements (CSIs), improved metrics, and direct log access via API server.                                                       |
|   5 | Grafana Labs must both learn new Kubernetes features and update their tools accordingly.                                                                                                                                                                       |
|   6 | Ya started learning Kubernetes in August 2024, with no prior container orchestration experience.                                                                                                                                                               |
|   7 | Initial Kubernetes concepts (pods, nodes, clusters, deployments, namespaces) seemed simple but proved more complex in practice.                                                                                                                                |
|   8 | The smallest unit in Kubernetes is a pod, but containers are smaller; the distinction is nuanced.                                                                                                                                                              |
|   9 | Advanced concepts (stateful sets, daemon sets, replica sets, deployments) are confusing and have subtle differences.                                                                                                                                           |
|  10 | "Set" objects (stateful set, daemon set, replica set) are only loosely related; each has unique behavior and use cases.                                                                                                                                        |
|  11 | Helm charts, operators, and service meshes add further complexity; ingress differs across cloud providers.                                                                                                                                                     |
|  12 | Helm is described as a package manager but is more like a YAML builder; operators simplify some tasks but add complexity elsewhere.                                                                                                                            |
|  13 | Stateful sets vs deployments with PVCs: stateful sets maintain pod identity and ordered deployment; deployments do not.                                                                                                                                        |
|  14 | Learning Kubernetes is hindered by assumptions of prior knowledge in documentation and tutorials.                                                                                                                                                              |
|  15 | Verbose documentation, long videos, and reading manifest files alone were not effective learning methods for Ya.                                                                                                                                               |
|  16 | Effective learning methods included using K9s, hands-on experimentation in dev en                                                                                                                                                                              |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Ctm0jjPZV1M)