---
layout: default
title: Right-sized Access Control & Pull with Proof - Stanislav Láznička & Lucas Käldström
nav_order: 310
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this presentation, Stlaznichka and Lucas Chastra discuss recent enhancements
  in Kubernetes, focusing on improvements to image pulling and authorization mechanisms.
  The first part details changes to how Kubernetes handles private image pu...
resource: https://www.youtube.com/watch?v=7aRWwlU_ewE
tags:
  - kubecon-cloudnativecon-europe-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

In this presentation, Stlaznichka and Lucas Chastra discuss recent enhancements in Kubernetes, focusing on improvements to image pulling and authorization mechanisms.
The first part details changes to how Kubernetes handles private image pulls, introducing a system where the kubelet can use service account tokens with credential providers, and a new mechanism to securely track which credentials were used to pull images.
This addresses a security issue where previously pulled private images could be accessed without credentials under certain policies, and introduces configurable verification policies for preloaded and pulled images.
The second part introduces a new conditional authorization model, allowing more fine-grained access control by enabling policies that can express conditions (such as allowing actions only on specific resources or fields), and propagating these conditions through the authorization and admission phases.
This unified approach aims to make Kubernetes authorization more flexible and expressive, with ongoing work and community feedback encouraged for future improvements.

# Main Points

|   # | Main point                                                                                                                                                              |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation covers enhancements in Sig O, focusing on two main features.                                                                                               |
|   2 | First feature: Changes to image pulling in Kubernetes.                                                                                                                  |
|   3 | Previous image pulling methods (image pull secrets, credential providers, clusterwide credentials) were inflexible.                                                     |
|   4 | Introduced service account tokens for kubelet credential providers to improve authentication.                                                                           |
|   5 | Kubelet can now request audience-scoped service account tokens and send them to credential providers.                                                                   |
|   6 | Credential providers can use these tokens to pull images or exchange for cloud-specific tokens.                                                                         |
|   7 | Identified security issue: "IfNotPresent" and "Never" image pull policies can allow unauthorized access to private images already present on a node.                    |
|   8 | Existing solution: "AlwaysPullImages" admission controller, but it is not enabled by default and has drawbacks (network overhead, unnecessary authentications).         |
|   9 | Developed a credential mapping system to track which credentials were used to pull each image.                                                                          |
|  10 | Persisted credential records between kubelet restarts; two types of records: pulling (in-progress) and pulled (completed).                                              |
|  11 | Introduced four verification policies for preloaded images: always verify, never verify preloaded images (default), never verify allow-listed images, and never verify. |
|  12 | User interface includes "imagePullCredentialsVerification" and "preLoadedImagesVerificationAllowList" fields in kubelet config.                                         |
|  13 | Users can view credential records in kubelet's image manager directory.                                                                                                 |
|  14 | Second feature: Authorization enhancements in Kubernetes.                                                                                                               |
|  15 | Current RBAC system can lead to over-granting permissions and is hard to fine-tune.                                                                                     |
|  16 | New approach allows expressing precise permission slices and supports constrained impersonation.                                                                        |
|  17 | Introduced "maybe" mode in authorization, enabling conditional access based on request metadata and object state.                                                       |
|  18 | Partial evaluation allows authorizer to defer decisions until more information is available.                                                                            |
|  19 | Unified policy model using conditions (expressed in CEL, Cedar, OPA, etc.) for mor                                                                                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=7aRWwlU_ewE)
