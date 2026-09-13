---
layout: default
title:
  "Project Lightning Talk: Linkerd, mTLS, and Bungled Bundles - Flynn, Technical
  Evangelist"
nav_order: 228
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  Flynn from the Linkerd project discusses the challenges of managing MTLS
  certificates within a service mesh, focusing on a user incident where expired certificates
  caused system failures. He explains that Linkerd relies on trust anchors wit...
resource: https://www.youtube.com/watch?v=PpV8tAbBvsU
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

Flynn from the Linkerd project discusses the challenges of managing MTLS certificates within a service mesh, focusing on a user incident where expired certificates caused system failures.
He explains that Linkerd relies on trust anchors within trust bundles to validate certificates and describes the correct process for rotating these anchors to avoid disruptions.
A key issue arose from outdated documentation that recommended an incorrect rotation method, which, combined with changes in cert-manager’s rotation policy in version 1.18, led to compatibility problems and outages.
Flynn emphasizes that these problems highlight the complexities of certificate management and the importance of coordination between different tools in the ecosystem.
He concludes by encouraging collaboration to improve integration and invites feedback and engagement from the community.

# Main Points

|   # | Main point                                                                                                                                |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Flynn from the Linkerd project discusses Linkerd mTLS and certificate management issues.                                                  |
|   2 | Linkerd is a service mesh providing security, reliability, and observability at the platform level without requiring application changes. |
|   3 | Linkerd injects mTLS into all meshed communications using lightweight Rust microproxies.                                                  |
|   4 | mTLS identity is based on certificates, which must be derived from a trust anchor in a trust bundle.                                      |
|   5 | Certificates and trust anchors require rotation or renewal to prevent expiration.                                                         |
|   6 | Proper rotation involves introducing a new trust anchor, rotating certificates, and eventually removing the old anchor.                   |
|   7 | Old Linkerd documentation described an incorrect rotation method, leading to expired certificates and failures.                           |
|   8 | Linkerd relies on external tools like Venafi cert-manager for certificate management.                                                     |
|   9 | Prior to version 1.18, cert-manager’s default rotation policy only updated certificate validity dates without changing the private key.   |
|  10 | In cert-manager 1.18, the default policy changed to always generate a new key during rotation, improving security.                        |
|  11 | The old documentation worked with cert-manager versions before 1.18 due to the previous rotation behavior.                                |
|  12 | Upgrading to cert-manager 1.18 caused failures when following the old documentation.                                                      |
|  13 | The main lesson is the importance of ecosystem compatibility and collaboration between projects.                                          |
|  14 | Linkerd is working on streamlining processes and welcomes feedback and ideas from users.                                                  |
|  15 | Linkerd recently introduced support for MCP.                                                                                              |
|  16 | Flynn is available for further discussion on Slack or at the Linkerd kiosk.                                                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=PpV8tAbBvsU)
