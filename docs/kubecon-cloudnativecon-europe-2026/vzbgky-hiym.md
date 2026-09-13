---
type: Video Note
title: "Cert-manager – Project Update: Beyond 2026 - Tim Ramlot & Maël Valais, Palo Alto Networks"
description: "The presentation provides an overview of the cert-manager project, its recent developments, and future plans. Cert-manager is a CNCF-graduated open-source project focused on managing X.509 certificates within Kubernetes, offering controller..."
resource: https://www.youtube.com/watch?v=vzBGkY_HIyM
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The presentation provides an overview of the cert-manager project, its recent developments, and future plans.
Cert-manager is a CNCF-graduated open-source project focused on managing X.509 certificates within Kubernetes, offering controllers that automate certificate issuance and distribution, with nearly a million daily users and a diverse, growing maintainer base.
Recent milestones include project graduation, improved governance, and the addition of new maintainers to enhance diversity and long-term viability.
Key updates cover new features such as support for listener sets, improvements to Helm charts, Azure private DNS zones, and enhanced security practices, including automated pipelines, centralized dependency management, and regular security audits.
The team is also addressing migration challenges from Ingress to Gateway API, improving developer self-service, and planning future enhancements like moving internal issuers out of the core project, optimizing the ACME issuer, and introducing features such as renewal windows and server-side apply.
# Main Points

|   # | Main point                                                                                                                                                            |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation covers updates and vision for cert-manager project.                                                                                                      |
|   2 | Cert-manager is a CNCF graduated project focused on X.509 certificates in Kubernetes.                                                                                 |
|   3 | Community consists of nearly 500 contributors; project is used by almost a million people daily.                                                                      |
|   4 | Main controller issues certificates for Kubernetes workloads (pods, ingresses, gateways, service meshes) by interacting with CAs like Let's Encrypt, Vault, CyberArk. |
|   5 | Trust-manager is another project for distributing trust bundles (certificates) across Kubernetes workloads using secrets and config maps.                             |
|   6 | Project recently added its 10th maintainer, improving diversity and long-term viability.                                                                              |
|   7 | Cert-manager is not built into Kubernetes; must be installed separately.                                                                                              |
|   8 | Recent releases include:                                                                                                                                              |
|   9 | Support for ListenerSets (enables self-service certificate management with Gateway API)                                                                               |
|  10 | Improved Helm chart experience, especially for custom registries                                                                                                      |
|  11 | Azure private DNS zone support                                                                                                                                        |
|  12 | Fixes for large certificates                                                                                                                                          |
|  13 | Trust-manager improvements: skip non-CA certificates, CRD updates                                                                                                     |
|  14 | ListenerSet resource allows developers to manage certificates without editing sensitive Gateway objects, aiding migration from Ingress to Gateway API.                |
|  15 | Security measures include:                                                                                                                                            |
|  16 | Defending against supply chain and direct attacks                                                                                                                     |
|  17 | Trust on first use, fast security updates, minimal dependencies                                                                                                       |
|  18 | Centralized automation and scripts via makefile-modules repository                                                                                                    |
|  19 | Renovate for dependency updates                                                                                                                                       |
|  20 | Code scanning, linting, vulnerability scanning, license checks, and CRD best practices enforcement                                                                    |
|  21 | Fully automated, signed release pipelines                                                                                                                             |
|  22 | Regular security audits and published hardening guides                                                                                                                |
|  23 | Future plans:                                                                                                                                                         |
|  24 | Move entry issuers out of cert-manager core                                                                                                                           |
|  25 | Develop reusable webhook-cert libraries                                                                                                                               |
|  26 | Improve ACME issuer performance and support ACME renewal info extension                                                                                               |
|  27 | Add image digests to Helm charts                                                                                                                                      |
|  28 | Migrate to server-side apply                                                                                                                                          |
|  29 | Renewal window support for certificate renewals during specific times                                                                                                 |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=vzBGkY_HIyM)