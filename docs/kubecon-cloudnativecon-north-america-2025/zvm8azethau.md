---
layout: default
title:
  "Confidential Observability on Kubernetes: Protecting Telemetry End-to-End-
  Jitendra Singh, Microsoft"
nav_order: 44
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  Jitendra Singh introduces the topic of confidential observability on
  Kubernetes, highlighting the limitations of traditional observability methods in
  protecting sensitive data during processing. He explains that while data at rest
  and in tr...
resource: https://www.youtube.com/watch?v=ZVM8azeTHAU
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

Jitendra Singh introduces the topic of confidential observability on Kubernetes, highlighting the limitations of traditional observability methods in protecting sensitive data during processing.
He explains that while data at rest and in transit can be encrypted, data is vulnerable when it is decrypted for use, exposing sensitive information such as user IDs and tokens.
To address this, Singh discusses confidential computing, which uses hardware-based isolation (like Intel TDX and AMD technologies) to secure data even while it is being processed.
He describes the implementation of confidential containers in Kubernetes, where workloads run inside secure environments that prevent unauthorized access, ensuring end-to-end encryption from data collection to storage.
Singh concludes by emphasizing that confidential observability is particularly valuable for organizations handling sensitive data, as it provides comprehensive protection for data in use, not just at rest or in transit.

# Main Points

|   # | Main point                                                                                                                                                                |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Jitendra Singh, serverless software engineer at Microsoft, presents on computational observability in Kubernetes.                                                         |
|   2 | Agenda includes: current observability challenges, confidential computing, confidential containers, proposed solution, architecture, and key takeaways.                   |
|   3 | Traditional observability involves applications generating logs, agents collecting and processing logs, storage in Elasticsearch, and visualization in Kibana.            |
|   4 | Sensitive data in logs (user IDs, tokens, internal metadata) can be exposed during processing when data is decrypted.                                                     |
|   5 | Data at rest and data in transit are encrypted, but data in use (during processing) is vulnerable.                                                                        |
|   6 | Traditional encryption does not protect data in use; exposure can occur in RAM during processing.                                                                         |
|   7 | Confidential computing introduces hardware-based isolation to protect data in use.                                                                                        |
|   8 | Trusted Execution Environments (TEEs) like Intel TDX and AMD solutions provide hardware-backed secure boundaries.                                                         |
|   9 | Key management services handle key exchange within TEEs.                                                                                                                  |
|  10 | Confidential containers run workloads inside VMs aligned with TEEs, ensuring data remains encrypted and isolated during processing.                                       |
|  11 | In Kubernetes, confidential containers ensure all data from hardware to observability pipeline is protected.                                                              |
|  12 | End-to-end encryption is enforced; even admins cannot access logs without proper authorization via key broker and attestation services.                                   |
|  13 | Only authorized requests, validated by attestation services, can decrypt and access data.                                                                                 |
|  14 | Comparison: Traditional observability exposes sensitive data during processing; confidential observability secures data at rest, in transit, and in use.                  |
|  15 | Confidential observability is especially beneficial for organizations handling sensitive data (government, healthcare, finance, banks) and needing regulatory compliance. |
|  16 | Key takeaways:                                                                                                                                                            |
|  17 | Data in transit and at rest encryption is not sufficient; data in use must also be protected.                                                                             |
|  18 | Data outside secure boundaries cannot be accessed, ensuring end-to-                                                                                                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=ZVM8azeTHAU)
