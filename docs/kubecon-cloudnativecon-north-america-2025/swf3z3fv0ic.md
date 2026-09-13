---
layout: default
title:
  "AdminNetworkPolicy: From Alpha To Beta... Dan Winship, Surya Seetharaman,
  Nadia Pinaeva & Bowei Du"
nav_order: 10
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  The video presents an overview of the evolution of Kubernetes cluster
  network policy, tracing its development from the initial admin network policy (ANP)
  and baseline admin network policy (BNP) APIs to the new unified cluster network
  policy...
resource: https://www.youtube.com/watch?v=SWf3Z3fV0ic
tags:
  - kubecon-cloudnativecon-north-america-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The video presents an overview of the evolution of Kubernetes cluster network policy, tracing its development from the initial admin network policy (ANP) and baseline admin network policy (BNP) APIs to the new unified cluster network policy (CNP) API.
The speakers explain that the original separation of ANP and BNP, which served similar purposes for administrators, led to unnecessary complexity, prompting their consolidation into a single CNP resource with an added "tier" field to distinguish between admin and baseline policies.
Key changes in the new API include support for multiple baseline policies with priorities, the extension of the "pass" action to both tiers, and a renaming of the "allow" action to "accept" for clarity.
The team highlights ongoing and future work, such as explicit allow/deny-all rules, improved ingress rule matching, and potential support for identity-based policies and additional tiers.
They encourage community involvement and feedback as the API moves toward beta status, emphasizing the importance of simplicity, extensibility, and clear governance in policy management.

# Main Points

|   # | Main point                                                                                                                                                             |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Introduction of speakers from Red Hat, Google, and Nvidia, all working on Kubernetes network policy APIs.                                                              |
|   2 | The talk covers the evolution from admin network policy (A&P) and baseline admin network policy (B&P) to cluster network policy (CNP).                                 |
|   3 | Admin network policy was created to allow cluster-wide, non-overridable policies for admins, supplementing tenant-focused network policies.                            |
|   4 | Use cases include isolating tenant workloads, enforcing policies for infrastructure services, always allowing DNS ingress, and delegating policy decisions to tenants. |
|   5 | Guardrail API enables default deny for the entire cluster.                                                                                                             |
|   6 | V1alpha1 used two APIs: A&P (admin) and B&P (baseline), both with similar fields.                                                                                      |
|   7 | Evaluation order: A&P rules first, then network policy (developer layer), then B&P as a singleton guardrail.                                                           |
|   8 | Multiple implementations exist: Antria CNI, Innoven Kubernetes CNI, Calico, Kubeovn, and Cilium (in progress).                                                         |
|   9 | Breaking changes: A&P and B&P merged into a single ClusterNetworkPolicy (CNP) API in v1alpha2.                                                                         |
|  10 | CNP uses a "tier" field (admin or baseline) instead of separate objects; both tiers now support multiple policies and priorities.                                      |
|  11 | The "pass" action is now available in both tiers, allowing delegation to lower tiers or default cluster disposition.                                                   |
|  12 | Actions renamed: "allow" is now "accept"; actions are accept, deny, and pass.                                                                                          |
|  13 | Port structure updated for future protocol extensions (e.g., ICMP).                                                                                                    |
|  14 | Next steps: v1beta1 release planned after two implementations; Kube Network Policies is the reference implementation.                                                  |
|  15 | Future features: explicit allow/deny all, ingress rule improvements, domain name matching, logging-only policies, tenancy support, and identity-based policies.        |
|  16 | Community encourages contributions, feedback, and participation via Slack and bi-weekly meetings.                                                                      |
|  17 | Q&A clarified that "pass" exits the current tier and delegates to the next; within-tier pass is not supported.                                                         |
|  18 | Discussion on potential for dynamic, programmable tiers in the future for more g                                                                                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=SWf3Z3fV0ic)
