---
layout: default
title: "Can GitOps Handle Delivery of 5G vRAN Orchestrators?"
nav_order: 135
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Masakina from NTT Docomo presented a case study on how his team introduced GitOps to automate the delivery of 5G network functions, addressing the critical issue that manual deployments previously ..."
resource: "https://www.youtube.com/watch?v=Z8Gj1VIFlOI"
youtube_stats:
  view_count: 28
  channel_subscriber_count: 46800
tags:
  - openinfra-summit-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T23:38:50+00:00
---

# Summary

Masakina from NTT Docomo presented a case study on how his team introduced GitOps to automate the delivery of 5G network functions, addressing the critical issue that manual deployments previously took up to eight hours.
The team utilized Argo CD and Argo Workflows to create a hybrid architecture that combines a declarative layer for streamlined installation with an imperative abstraction layer to accommodate operators who are not developers and require specific operational evidence.
Key implementation details included extending the Argo CD controller to reflect Helm hook statuses and creating nested application structures to install multiple components simultaneously.
A live demonstration showed that the new automated pipeline reduced the deployment time from eight hours to just eleven minutes while ensuring easy rollbacks and idempotency.
The presentation concluded with key takeaways emphasizing the importance of building a delivery pipeline first, avoiding direct translation of manual processes into automation, and using abstraction layers to bridge the gap between ideal technical architectures and practical business needs.

# Main Points

|   # | Main point                                                                                                                                                                                                                           |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | The speaker from NTT Docomo R&D presented efforts to introduce GitOps for delivering 5G orchestrators, noting that the largest telecom company in Japan was not always the most advanced in this area.                               |
|   2 | The project aimed to replace manual delivery processes, which took up to 8 hours and involved over 200 steps, with an automated pipeline to reduce time and improve reliability.                                                     |
|   3 | Key challenges included a fragmented organizational structure where R&D and operations were separate entities, preventing direct staff training, and operators who were not developers and required operational evidence like logs.  |
|   4 | The solution architecture consisted of two layers: a declarative layer using GitOps to reduce delivery time and an imperative layer using workflows to handle operator-specific needs like evidence collection.                      |
|   5 | Argo CD was used for continuous delivery, syncing application definitions from a Git repository to deploy workloads, while Argo Workflows managed imperative tasks such as deployment control and log collection.                    |
|   6 | To improve workload declarativeness, Helm hooks were implemented for post-installation steps like database user creation, and nested Argo CD applications were created to install multiple components simultaneously.                |
|   7 | A custom controller extension was developed to reflect the success or failure of Helm hooks in the Argo CD application status, ensuring accurate deployment feedback.                                                                |
|   8 | Operators were provided with simple workflows for deploying and rolling back applications, allowing them to control synchronization without needing to use complex command-line tools or understand underlying Kubernetes resources. |
|   9 | A dedicated workflow was built to collect operational evidence, such as logs and accessibility checks, satisfying the requirement for operational proof without making these simple tasks fully declarative.                         |
|  10 | The implementation reduced the operating time for deployment from 8 hours to 11 minutes, a significant improvement that serves as a strong metric for convincing decision-makers to adopt modern delivery pipelines.                 |
|  11 | The speaker emphasized that building a delivery pipeline first enforces structured workloads, and automation should not be a direct translation of manual processes but rather a re-architecting of the solution.                    |
|  12 | Clear responsibility definitions across layers were essential, leading to the use of an abstraction layer to bridge the gap between ideal declarative architectures and the practical, less flexible needs of business operations.   |
|  13 | The final takeaway is to use an imperative abstraction layer for specific tasks to bridge ideal architecture and business needs, rather than forcing everything into a declarative model upfront.                                    |

# Video

[![Video thumbnail](https://img.youtube.com/vi/Z8Gj1VIFlOI/hqdefault.jpg)](https://www.youtube.com/watch?v=Z8Gj1VIFlOI)

[Watch on YouTube](https://www.youtube.com/watch?v=Z8Gj1VIFlOI)
