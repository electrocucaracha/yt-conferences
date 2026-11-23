---
layout: default
title: "Scaling OpenStack to Save Lives: Operating 200+ Hypervisors and 10,000+ VMs for Medical Innovation"
nav_order: 55
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "The speaker outlines the mission of their organization, CGM, to provide secure medical data software across the healthcare chain, leveraging OpenStack and Vexxhost Atmosphere to build a multi-tenan..."
resource: "https://www.youtube.com/watch?v=AFHFaklVDHw"
youtube_stats:
  view_count: 143
  like_count: 2
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

The speaker outlines the mission of their organization, CGM, to provide secure medical data software across the healthcare chain, leveraging OpenStack and Vexxhost Atmosphere to build a multi-tenant private cloud infrastructure.
They detail their architectural decisions, including deploying the control plane in Kubernetes, utilizing Ceph for storage, and managing approximately 200 bare-metal servers to meet strict German compliance and multi-tenancy requirements.
A significant portion of the transcript focuses on the gap between user expectations and delivered capabilities, noting that customers anticipated a seamless, fully automated, self-service experience comparable to public clouds like AWS, whereas the team initially provided a more complex, manual environment requiring significant operational effort.
Key lessons learned include the critical importance of managing user expectations, the difficulty of finding the right monitoring metrics in OpenStack, and the challenges of defining clear success factors for performance.
Finally, the speaker discusses technical scaling challenges, such as API resilience, network separation, and the complexities of managing CPU flavors and hardware configurations, emphasizing the need to pay down technical debt and maintain robust CI/CD testing processes.

# Main Points

|   # | Main point                                                                                                                                                   |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | The company's mission is to provide medical data software across the healthcare chain, ensuring no one suffers from missing information.                     |
|   2 | The organization chose OpenStack as the foundation for their private cloud to offer a cost-effective alternative to VMware.                                  |
|   3 | VexxHost Atmosphere was selected for orchestration due to its native integration, lifecycle management, and vendor support.                                  |
|   4 | The architecture deploys nearly all components, including the control plane, in Kubernetes to ensure consistency.                                            |
|   5 | The compute plane operates approximately 200 large bare-metal servers with high core counts using Nova and Neutron.                                          |
|   6 | Storage is handled by Ceph, utilizing a setup with monitor nodes and containerized storage nodes on specialized hardware.                                    |
|   7 | A robust network layer is critical for managing bandwidth, latency, and distributed storage performance.                                                     |
|   8 | A key lesson learned is the need to manage user expectations, as customers often expect a fully automated, self-service experience similar to public clouds. |
|   9 | Users initially expected implicit features like autoscaling, live migration, and full backup solutions that were not immediately available.                  |
|  10 | The platform initially provided basic tools like Horizon, which some users found insufficient, leading to the development of custom UIs.                     |
|  11 | Governance and compliance features were added post-deployment after realizing they were required for certification and regulatory obligations.               |
|  12 | Resource scaling was managed through manual capacity planning and reserving spare capacity rather than true elastic autoscaling.                             |
|  13 | Skipping operational processes and monitoring during initial deployment led to user dissatisfaction and required significant remediation.                    |
|  14 | Finding the right metrics in an OpenStack environment is difficult due to the overwhelming number of technical services.                                     |
|  15 | Metric-based monitoring carries a risk of blind spots where dashboards show green status despite underlying configuration issues.                            |
|  16 | Defining success factors is challenging because different customers prioritize different performance metrics like latency or throughput.                     |
|  17 | Moving control plane components from Ceph to localStorage resolved major incidents caused by storage slowness and API flapping.                              |
|  18 | Separating the storage network from other networks early on prevented significant operational issues.                                                        |
|  19 | OpenStack APIs face scalability challenges, including slowness and bugs related to Neutron and database interactions.                                        |
|  20 | Keeping up with updates is a persistent challenge due to the large number of services and the need for rigorous testing and change management.               |
|  21 | Flavor management requires balance, as offering too many options can reduce efficiency and confuse users who expect more power from higher tiers.            |
|  22 | Maintaining consistent CPU types across hardware is crucial to enable live migration and avoid scheduling limitations.                                       |
|  23 | Hardware-level settings can significantly impact performance, but excessive tweaking complicates scheduling in large clusters.                               |
|  24 | Providing specialized nodes for specific workloads like databases or Kubernetes clusters improves resource allocation efficiency.                            |
|  25 | Technical debt should be addressed with a direct payback plan integrated into the development roadmap.                                                       |
|  26 | Regular architecture reviews help identify and resolve technical issues before they become critical.                                                         |
|  27 | CI/CD testing must include user-facing functionality to ensure the platform is usable, not just technically stable.                                          |

# Video

[![Video thumbnail](https://img.youtube.com/vi/AFHFaklVDHw/hqdefault.jpg)](https://www.youtube.com/watch?v=AFHFaklVDHw)

[Watch on YouTube](https://www.youtube.com/watch?v=AFHFaklVDHw)
