---
layout: default
title:
  "The Good, the Bad, and the Ugly: Hacking 3 Cloud Native AI Service... Hillai
  Ben-Sasson & Nir Ohfeld"
nav_order: 309
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  In this talk, researchers from Whiz detailed their discovery of a critical
  container escape vulnerability in the Nvidia Container Toolkit, a component widely
  used across cloud-native AI services. By exploiting this vulnerability, they demon...
resource: https://www.youtube.com/watch?v=ZTiWXqYg97U
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

In this talk, researchers from Whiz detailed their discovery of a critical container escape vulnerability in the Nvidia Container Toolkit, a component widely used across cloud-native AI services.
By exploiting this vulnerability, they demonstrated how attackers could gain full host access from within a container, potentially compromising entire cloud environments.
The team tested the exploit on three platforms—Azure Container Instances, Replicate, and Digital Ocean's Paperspace—revealing varying levels of risk and defense: Azure's virtual API server effectively contained the attack, Replicate's monitoring detected and flagged the intrusion, while Digital Ocean's environment allowed for full service takeover and exposure of customer secrets.
The researchers emphasized the importance of layered security measures beyond containerization, responsible disclosure, and ongoing vigilance, announcing an open-source competition to encourage further research into foundational cloud infrastructure vulnerabilities.

# Main Points

|   # | Main point                                                                                                                                                                          |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Discovered a critical container escape vulnerability in Nvidia Container Toolkit, used by most AI cloud providers.                                                                  |
|   2 | Vulnerability allows full file system access and code execution on the host from a compromised container.                                                                           |
|   3 | Attack works by manipulating mount operations during container initialization, bypassing existing mitigations.                                                                      |
|   4 | Tested exploit on three cloud AI services: Azure Container Instances, Replicate, and DigitalOcean Paperspace.                                                                       |
|   5 | Azure Container Instances:                                                                                                                                                          |
|   6 | Exploit granted host access, but strong isolation (virtual API server) prevented cross-tenant attacks and lateral movement.                                                         |
|   7 | Replicate:                                                                                                                                                                          |
|   8 | Exploit enabled escape to host, revealing plaintext Redis database credentials.                                                                                                     |
|   9 | Redis database is shared across customers, allowing access to all prompts and predictions, and the ability to interfere in real time.                                               |
|  10 | Security team detected suspicious activity and responded quickly.                                                                                                                   |
|  11 | DigitalOcean Paperspace:                                                                                                                                                            |
|  12 | Exploit enabled access to node-level Kubernetes credentials.                                                                                                                        |
|  13 | Credentials allowed access to over 700 nodes, including other customer pods and sensitive secrets (e.g., AWS credentials).                                                          |
|  14 | Attack could lead to full service takeover and compromise of customer environments.                                                                                                 |
|  15 | All issues were responsibly disclosed and patched by vendors.                                                                                                                       |
|  16 | Key takeaway: Relying solely on containerization for tenant isolation is insufficient; multiple guardrails (e.g., virtualization, network rules, credential hygiene) are essential. |
|  17 | Strong security posture and layered defenses can prevent zero-day attacks even when vulnerabilities exist.                                                                          |
|  18 | Announced open source resource "Peach" for building secure multi-tenant environments.                                                                                               |
|  19 | Launched zeroday.cloud hacking competition with major cloud providers to improve open source cloud security.                                                                        |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=ZTiWXqYg97U)
