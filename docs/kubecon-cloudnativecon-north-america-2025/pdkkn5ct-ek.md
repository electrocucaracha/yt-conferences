---
type: Video Note
title: "Project Lightning Talk: Invisible FinOps and Compliance: Shift Left With Cloud Custodian - Sonny Shi"
description: 'Sonia, head of product at Stacklet and maintainer of the Cloud Custodian project, discusses the importance of addressing "invisible PHOPS," compliance, and shifting left in cloud resource management. She explains that while creating cloud r...'
resource: https://www.youtube.com/watch?v=PDkkn5ct_Ek
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Sonia, head of product at Stacklet and maintainer of the Cloud Custodian project, discusses the importance of addressing "invisible PHOPS," compliance, and shifting left in cloud resource management.
She explains that while creating cloud resources initially incurs minimal cost, misconfigurations and delayed optimizations can lead to significant waste in both time and money.
By implementing automated, enforceable policies—such as identifying and resizing underutilized resources—organizations can proactively optimize cloud spend and improve security and compliance.
These policies can also be applied to infrastructure as code, allowing issues to be detected and addressed even earlier in the development process.
Sonia advises starting with simple, sensible policies, socializing them within the organization, and ensuring they empower rather than hinder developers, ultimately promoting efficient and compliant cloud operations.
# Main Points

|   # | Main point                                                                                                                            |
| --: | ------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Sonia is head of product at Stacklet and a maintainer on the Cloud Custodian project.                                                 |
|   2 | Discussion focuses on invisible FinOps, compliance, and shifting left.                                                                |
|   3 | Creating cloud resources is initially inexpensive but can lead to high costs over time due to configuration choices.                  |
|   4 | Goal is to avoid high-spend, overutilized scenarios by finding optimization opportunities.                                            |
|   5 | Optimization actions often lag between detection and implementation, leading to waste in time and money.                              |
|   6 | Waste can amount to tens or hundreds of thousands of dollars annually.                                                                |
|   7 | Shifting left means addressing issues earlier in the process.                                                                         |
|   8 | Policies are declarative rules defining desired cloud environment states, enforced automatically and in real time.                    |
|   9 | Policies without enforcement are just suggestions and often result in inaction.                                                       |
|  10 | Implementing policies can shift optimization actions earlier, reducing waste.                                                         |
|  11 | Example policy: Identify resources with less than 10% CPU utilization over 30 days and resize them down.                              |
|  12 | Policies run automatically, optimizing and taking action invisibly for FinOps, security, and compliance.                              |
|  13 | Cloud Custodian policies can operate on live resources and infrastructure as code.                                                    |
|  14 | Policies can flag unapproved instance types in Terraform or Open Tofu configurations before deployment.                               |
|  15 | Early policy enforcement maximizes savings and detection.                                                                             |
|  16 | Recommendations for getting started:                                                                                                  |
|  17 | Start small with a set of policies and enforce sensible limits.                                                                       |
|  18 | Begin in lower environments, then adjust for production.                                                                              |
|  19 | Socialize policies by communicating clearly and often during rollout.                                                                 |
|  20 | Enable developers by starting with basic, obvious policies and avoid unnecessary roadblocks.                                          |
|  21 | Ensure policies are enforced through automation.                                                                                      |
|  22 | Invitation to check out Cloud Custodian, visit the booth at KubeCon, join the Slack channel, and attend bi-weekly community meetings. |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=PDkkn5ct_Ek)