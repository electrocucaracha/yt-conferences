---
type: Video Note
title: "Project Lightning Talk: Blocking Vulnerable Workloads Out (And Catching What Got I... Alessio Greggi"
description: "In this presentation, Alessio introduces a new integration for Cube Warden, a universal policy engine that allows users to write custom policies in various programming languages and compile them into OCI artifacts using Wasm. The integratio..."
resource: https://www.youtube.com/watch?v=0ItI-HaO7do
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this presentation, Alessio introduces a new integration for Cube Warden, a universal policy engine that allows users to write custom policies in various programming languages and compile them into OCI artifacts using Wasm.
The integration combines Cube Warden with a new SBOM scanner component, which leverages Trivy to scan container images in a registry for vulnerabilities and produces vulnerability reports as CRDs.
The main feature demonstrated is the "image CV policy," which enforces a maximum number of vulnerabilities allowed in an image before it can be applied to a Kubernetes cluster.
This policy is context-aware, requiring vulnerability reports from the SBOM scanner, and can be configured to specify severity thresholds and behaviors for missing reports.
The workflow ensures that only images meeting the defined security criteria are deployed, enhancing cluster security.
# Main Points

|   # | Main point                                                                                                                                                                                                               |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Introduction of Alessio presenting a new integration using a policy for Cube Warden to block workloads with a specified number of CVEs.                                                                                  |
|   2 | Cube Warden is a universal policy engine allowing custom policies in various languages via provided SDKs.                                                                                                                |
|   3 | Policies can be compiled into OCI artifacts using Wasm and pushed to registries.                                                                                                                                         |
|   4 | SBOM scanner is a new component of Cube Warden, acting as an SBOM-centric security scanner.                                                                                                                              |
|   5 | SBOM scanner currently uses Trivy but plans to support additional scanners for enriched vulnerability reports.                                                                                                           |
|   6 | SBOM scanner can be configured to scan specific registries and filter images as needed.                                                                                                                                  |
|   7 | The scanner produces vulnerability reports for all scanned images in the configured registry.                                                                                                                            |
|   8 | The integration combines Cube Warden and SBOM scanner through a new image CV policy.                                                                                                                                     |
|   9 | The image CV policy enforces a maximum number of vulnerabilities allowed in an image before it is applied to the cluster.                                                                                                |
|  10 | The policy is context-aware and requires vulnerability report CRDs from the SBOM scanner.                                                                                                                                |
|  11 | To apply the policy, a cluster administration policy is needed, referencing the policy module stored as an OCI artifact.                                                                                                 |
|  12 | Cube Warden uses the policy in protect mode to block resources that exceed vulnerability thresholds.                                                                                                                     |
|  13 | The policy context must include the vulnerability report CRD from SBOM scanner.                                                                                                                                          |
|  14 | Policy configuration allows specifying behaviors such as ignoring missing vulnerability reports.                                                                                                                         |
|  15 | The max severity field lets users define the allowed number of vulnerabilities by severity (critical, high, low).                                                                                                        |
|  16 | Example given: setting zero critical vulnerabilities allowed in images.                                                                                                                                                  |
|  17 | Workflow: SBOM scanner scans registries, produces vulnerability reports, Cube Warden checks the image CV policy and vulnerability report when applying resources, and enforces the policy based on vulnerability counts. |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=0ItI-HaO7do)