---
type: Video Note
title: "Project Lightning Talk: Catch Up With Crossplane v2 - Scott Rosenberg, Contributor"
description: "In this talk, Scott Rosenberg introduces Crossplane v2, highlighting its role as a cloud-native control plane that extends Kubernetes' capabilities to manage any resource with an API, including public cloud, on-premises, and application res..."
resource: https://www.youtube.com/watch?v=mr_zhO2lV2w
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Scott Rosenberg introduces Crossplane v2, highlighting its role as a cloud-native control plane that extends Kubernetes' capabilities to manage any resource with an API, including public cloud, on-premises, and application resources.
He explains that Crossplane v1 introduced complexity through its use of claims and cluster-scoped resources, which created awkward isolation boundaries and made debugging difficult.
Crossplane v2 simplifies this by allowing composite resources to be either namespaced or cluster-scoped, improving flexibility and reducing complexity.
The new version also enhances application support by enabling the composition of any resource, not just infrastructure, and addresses the issue of excessive CRDs by allowing selective installation of only needed resources.
Additional improvements include better provider generation with upjet, Terraform plan-like diff capabilities, enhanced observability, and improved documentation, all while maintaining backward compatibility except for deprecated features.
# Main Points

|   # | Main point                                                                                                                                        |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Crossplane v2 is the new major version of Crossplane.                                                                                             |
|   2 | Crossplane is a cloud-native control plane that enables provisioning and management of resources using Kubernetes paradigms.                      |
|   3 | Allows composition of resources via XRDs and compositions to create user-facing APIs.                                                             |
|   4 | Enables self-service for end users.                                                                                                               |
|   5 | Extends Kubernetes control plane concepts to any API, including public cloud, vSphere, on-prem solutions, and more.                               |
|   6 | Crossplane democratizes control plane creation, allowing users to build their own platform APIs.                                                  |
|   7 | In Crossplane v1, XRDs created both namespace-scoped claims and cluster-scoped resources, leading to complexity and awkward isolation boundaries. |
|   8 | Debugging was difficult due to cluster-level access requirements.                                                                                 |
|   9 | Claim-to-XR mapping added excessive complexity.                                                                                                   |
|  10 | Crossplane v2 simplifies the model with a single composite resource, which can be namespace or cluster scoped.                                    |
|  11 | Composites can deploy both managed and non-crossplane resources.                                                                                  |
|  12 | Users can choose the scope (namespace or cluster) for their APIs.                                                                                 |
|  13 | V1 had poor application support, focusing mainly on infrastructure and requiring wrapper providers for non-crossplane resources.                  |
|  14 | V2 allows composing any resource, including deployments, services, or any CRD, making application control planes easier to build.                 |
|  15 | V1 suffered from excessive CRDs, causing API server issues.                                                                                       |
|  16 | V2 introduces managed resource activation policies (maps) to limit CRD installation to only those needed, reducing API server load.               |
|  17 | New features include generating Crossplane providers from almost any Terraform provider using Upjet.                                              |
|  18 | Upjet now supports Terraform protov6 and OpenTofu providers.                                                                                      |
|  19 | Crossplane v2 introduces Terraform plan-like capabilities with crossplane diff and improved reconciliation observability.                         |
|  20 | Backwards compatibility is maintained unless deprecated features are used.                                                                        |
|  21 | Documentation has been revamped for easier use.                                                                                                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=mr_zhO2lV2w)