---
type: Video Note
title: "How To Break Multi-Tenancy Again and Again ...and What We Can Learn F... Lorin Lehawany & Sven Nobis"
description: "In this talk, security analysts Lauren Lehavani and Sven Nois from a German security consultancy share their research on breaking namespace-based multi-tenancy in Kubernetes clusters, highlighting that industry best practices are often insu..."
resource: https://www.youtube.com/watch?v=PEU4uDzurvc
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, security analysts Lauren Lehavani and Sven Nois from a German security consultancy share their research on breaking namespace-based multi-tenancy in Kubernetes clusters, highlighting that industry best practices are often insufficient for true tenant isolation.
They present three real-world exploits: insecure cross-namespace references in custom resource definitions (demonstrated with Kubeflow), annotation-based privilege escalation (shown with Traefik), and data plane attacks via service mesh misconfigurations (using Istio), each allowing attackers to compromise tenant boundaries and access sensitive resources.
The speakers detail their responsible disclosures and note that while some issues were fixed, others remain due to design trade-offs.
They introduce a three-step methodology for organizations to assess and mitigate multi-tenancy risks: identifying multi-tenancy usage, evaluating potential weaknesses, and applying targeted controls such as policy enforcement or migration to the Gateway API.
The talk concludes by urging practitioners to thoroughly assess namespace-based multi-tenancy implications, use the provided methodology as a guideline, and remain vigilant, as these vulnerabilities are subtle and widespread.
# Main Points

|   # | Main point                                                                                                                                                             |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Lauren Lehavani and Sven Nois, security analysts at Companyw, present research on breaking namespace-based multi-tenancy.                                              |
|   2 | Namespace-based multi-tenancy is widely used for cost savings but is challenging to secure.                                                                            |
|   3 | Research question: Is industry best practice hardening enough to isolate namespace-based multi-tenancy?                                                                |
|   4 | Multiple, under-studied security problems were found.                                                                                                                  |
|   5 | Three exploits demonstrated: two on the control plane, one on the data plane. **Exploit 1: Insecure Cross-Namespace References in Custom Resource Definitions (CRDs)** |
|   6 | Example: Kubeflow, a machine learning platform on Kubernetes.                                                                                                          |
|   7 | Users have service accounts with permissions to create virtual services.                                                                                               |
|   8 | Users can reference resources (e.g., gateways) in other namespaces.                                                                                                    |
|   9 | Attacker can create a virtual service referencing the Kubeflow gateway, route requests to their own pod, and steal user cookies, allowing session hijacking.           |
|  10 | Issue fixed in Kubeflow by removing the problematic permission.                                                                                                        |
|  11 | Similar issues exist in other projects. **Exploit 2: Insecure Cross-Namespace References via Annotations**                                                             |
|  12 | Example: Traefik, an HTTP reverse proxy and load balancer.                                                                                                             |
|  13 | Attackers can reference victim resources (e.g., service transport) via annotations and forward requests to their own pods.                                             |
|  14 | Attackers can use secrets from victim resources without direct access.                                                                                                 |
|  15 | Traefik updated documentation and recommends using Gateway API.                                                                                                        |
|  16 | Cross-namespace annotation issues can also affect cloud provider resources. **Exploit 3: Data Plane Attack via Istio Service Mesh**                                    |
|  17 | Attackers deploy a virtual service claiming a host (e.g., example.com).                                                                                                |
|  18 | Istio sidecar routes victim traffic to attacker’s pod, enabling man-in-the-middle attacks.                                                                             |
|  19 | Some limitations exist; full mutual TLS is not always broken.                                                                                                          |
|  20 | Istio considers this expected behavior; recommends Gateway API for secure multi-tenancy. **Methodology for Assessing Multi-Tenancy Security**                          |
|  21 | Step 1: Identify if namespace-based multi-tenancy is used.                                                                                                             |
|  22 | Step 2:                                                                                                                                                                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=PEU4uDzurvc)