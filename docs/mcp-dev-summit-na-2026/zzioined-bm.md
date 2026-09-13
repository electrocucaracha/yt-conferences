---
layout: default
title:
  "OCI Images as MCP Packaging: Supply Chain Security for AI Tools - Juan Antonio
  Osorio, Stacklok"
nav_order: 68
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  The speaker, Juan Antonio (Oz), discusses the importance of using OCI
  (Open Container Initiative) images as a secure packaging format for MCP servers
  and AI tooling, emphasizing the security risks of running tools directly with commands
  lik...
resource: https://www.youtube.com/watch?v=zzIoinEd_bM
tags:
  - mcp-dev-summit-na-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The speaker, Juan Antonio (Oz), discusses the importance of using OCI (Open Container Initiative) images as a secure packaging format for MCP servers and AI tooling, emphasizing the security risks of running tools directly with commands like npx or through unmanaged virtual environments.
He highlights recent security incidents, such as malicious MCP servers and critical vulnerabilities, to illustrate the evolving threat landscape and the need for better practices.
OCI images, which are essentially standardized Docker containers, allow for improved transparency, vulnerability scanning, provenance tracking, and enforcement of security policies by leveraging tools like SBOMs (Software Bill of Materials), digital signatures (using projects like Sigstore and Cosign), and attestations (such as SLSA provenance).
Through a live demo, Oz demonstrates building, scanning, signing, and attesting an OCI image, showing how these steps can be automated and integrated into existing infrastructure.
While OCI images are not a complete solution to all security challenges, they provide a strong foundation for defense in depth, enabling organizations to systematically manage and secure their software supply chain.

# Main Points

|   # | Main point                                                                                                                          |
| --: | ----------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation focuses on OCI images as packaging for MCP servers and AI tooling.                                                     |
|   2 | Warns against running npx directly due to security risks.                                                                           |
|   3 | Highlights the emergence of malicious MCP servers and critical vulnerabilities (e.g., CVE 2025606514).                              |
|   4 | Emphasizes the need for security awareness, not just fear.                                                                          |
|   5 | Introduces key security questions for MCP servers:                                                                                  |
|   6 | What is in the package?                                                                                                             |
|   7 | Who built it?                                                                                                                       |
|   8 | How was it built?                                                                                                                   |
|   9 | Is it vulnerable?                                                                                                                   |
|  10 | Can enforcement be applied?                                                                                                         |
|  11 | Notes that package managers have improved auditing but gaps remain, especially regarding OS-level dependencies.                     |
|  12 | OCI images are vendor-neutral, standardized (like Docker files), and widely supported (DockerHub, GitHub Container Registry, Quay). |
|  13 | OCI images are content-addressable and support attaching metadata, attestations, and SBOMs.                                         |
|  14 | SBOM (Software Bill of Materials) provides a list of all libraries and dependencies in the image.                                   |
|  15 | Signing images is important; recommends using Sigstore/cosign for signing with existing identities (e.g., GitHub, Google).          |
|  16 | Attestations (e.g., SLSA provenance) describe the build environment and process.                                                    |
|  17 | Enforcement policies can ensure only trusted, signed, and scanned images are run.                                                   |
|  18 | Demonstrates building, scanning (with Grype), generating SBOMs (with Syft), signing (with cosign), and attaching attestations.      |
|  19 | OCI images facilitate systematic security processes and can be used for packaging skills as well as servers.                        |
|  20 | Existing infrastructure (registries, scanners) can be leveraged without extra setup.                                                |
|  21 | OCI images are not a complete security solution; defense in depth is necessary.                                                     |
|  22 | Tool poisoning, tool shadowing, and rockpools are risks that OCI images alone cannot fully mitigate.                                |
|  23 | Recommendations: run vulnerability scanners, use cosign, validate sources, establish policies, and stay informed.                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=zzIoinEd_bM)
