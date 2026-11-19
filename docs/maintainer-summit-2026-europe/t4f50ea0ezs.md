---
layout: default
title: "Building Secure Package Pipelines - André Silva, LexisNexis Risk Solutions"
nav_order: 20
parent: "Maintainer Summit 2026 - Europe"
type: Video Note
description: "Andre Silva, a maintainer of OpenFeature and software engineer at Nexus Risk Solutions, presents a comprehensive strategy for securing the software supply chain against recent high-profile attacks ..."
resource: "https://www.youtube.com/watch?v=t4F50Ea0EZs"
tags:
  - maintainer-summit-2026-europe
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-16T15:59:05+00:00
---

# Summary

Andre Silva, a maintainer of OpenFeature and software engineer at Nexus Risk Solutions, presents a comprehensive strategy for securing the software supply chain against recent high-profile attacks like the DJ Actions exploit.
He emphasizes the critical importance of pinning GitHub Actions to specific commit SHAs and utilizing CodeQL to detect misconfigurations, while also advocating for the use of Dependabot and Renovate to automatically manage and patch vulnerable dependencies.
To ensure build integrity and traceability, Silva recommends implementing Sigstore Attestations, which cryptographically sign builds to link artifacts back to their exact source commits, thereby preventing tampering.
Furthermore, he highlights the transition from long-lived personal access tokens to short-lived, scoped OIDC tokens for cloud provider interactions, significantly reducing the risk of credential theft.
The presentation concludes by urging developers to adopt a zero-trust pipeline that combines these practices, ensuring that consumers can verify package authenticity and that all stakeholders share the responsibility of maintaining a secure and trustworthy open-source ecosystem.

# Main Points

|   # | Main point                                                                                                                         |
| --: | ---------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The DJ Actions exploit demonstrated how malicious code injection via release tags can compromise pipeline credentials.             |
|   2 | Major supply chain incidents like the Shock Debug issue and the ShyHul worm highlight the severity of package vulnerabilities.     |
|   3 | Pinning GitHub Actions to exact commit SHAs rather than mutable tags is a critical first line of defense against tampering.        |
|   4 | Configuring least-privilege permissions for workflows prevents attackers from accessing broad repository secrets.                  |
|   5 | Enabling CodeQL for GitHub Actions helps automatically detect bad configurations and missing security controls.                    |
|   6 | Using Dependabot or Renovate ensures automated updates for dependencies to prevent known vulnerabilities from reaching production. |
|   7 | SLSA (Supply-chain Levels for Software Artifacts) provides a framework for attesting build provenance and integrity.               |
|   8 | Attestations cryptographically sign builds to link artifacts back to specific source commits, preventing forgery.                  |
|   9 | Generating Software Bills of Materials (SBOMs) is essential for tracking dependencies, licenses, and potential CVEs.               |
|  10 | Transitioning from long-lived personal access tokens to OIDC tokens reduces risk by using short-lived, scoped credentials.         |
|  11 | OIDC tokens are single-use and tied to specific identities, making stolen tokens useless if they expire quickly.                   |
|  12 | GitHub Environments allow for granular control over secret access, restricting them to specific branches or scenarios.             |
|  13 | Consumers can verify package integrity using the GitHub CLI to check attestations before installation.                             |
|  14 | A zero-trust pipeline strategy involves not trusting the registry, actions, or network, but relying on cryptographic verification. |
|  15 | Combining pinned actions, OIDC, and attestations creates a robust defense against token theft and malicious packages.              |
|  16 | Open source maintainers should prioritize OIDC where available, always pin actions, and use provenance for consumer security.      |
|  17 | Free tools like GitHub OIDC, built-in attestations, and CodeQL facilitate these security practices without additional cost.        |
|  18 | Trust is the most valuable asset in open source, and breaking it with consumers is difficult to repair.                            |
|  19 | Security responsibility is shared between providers and consumers to maintain a safe ecosystem.                                    |

# Video

[![Video thumbnail](https://img.youtube.com/vi/t4F50Ea0EZs/hqdefault.jpg)](https://www.youtube.com/watch?v=t4F50Ea0EZs)

[Watch on YouTube](https://www.youtube.com/watch?v=t4F50Ea0EZs)
