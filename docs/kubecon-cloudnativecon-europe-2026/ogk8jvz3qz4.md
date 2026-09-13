---
type: Video Note
title: "From Alert Fatigue To Self-Healing: Building AI-Enabled Control Planes... Nuno Guedes & Yury Tsarev"
description: "In this session, Nunu from Millennium BCP and Yuri from Abound discuss how they are leveraging AI-enabled control planes, specifically using Crossplane v2, to address operational challenges in banking such as alert fatigue, regulatory compl..."
resource: https://www.youtube.com/watch?v=oGk8jVz3qZ4
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this session, Nunu from Millennium BCP and Yuri from Abound discuss how they are leveraging AI-enabled control planes, specifically using Crossplane v2, to address operational challenges in banking such as alert fatigue, regulatory compliance, and the need for auditability and controlled change.
They demonstrate how AI can be intentionally and safely injected into control plane operations to automate low-risk, repetitive tasks like diagnosing and remediating issues or optimizing costs, all while maintaining strict boundaries, schema-based actions, and evidence trails for regulators.
The approach allows for read-only AI recommendations before enabling automated actions, ensuring operators remain in control and can gradually build trust in the system.
By using label-based filtering and watch operations, they ensure AI interventions are explicit and auditable, and the system is designed to scale efficiently across multi-tenant environments.
The presenters emphasize that this method improves efficiency, supports regulatory reporting, and allows organizations to adopt AI at their own pace, starting with deterministic workflows and expanding as confidence grows.
# Main Points

|   # | Main point                                                                                                                             |
| --: | -------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation focuses on building AI-enabled control planes in banking, specifically at Millennium BCP in Portugal.                     |
|   2 | Regulatory compliance, operational resiliency, auditability, controlled change, and predictable remediation are critical in banking.   |
|   3 | Manual incident handling does not scale with platform complexity and volume of signals.                                                |
|   4 | Too much observability leads to alert fatigue and pressure on operators.                                                               |
|   5 | Adopted a control plane approach using Crossplane v2 to automate day-2 operations and reduce operator workload.                        |
|   6 | Multi-tenant patterns implemented: workload equals namespace, namespace equals service level, service level equals operation patterns. |
|   7 | AI is injected into control plane operations via watch operations, only on explicitly labeled resources.                               |
|   8 | Demonstrated AI-enabled diagnosis: AI analyzes stuck caches, provides diagnosis annotations, and recommends fixes.                     |
|   9 | Auto-remediation can be triggered by labels, allowing AI to patch issues automatically.                                                |
|  10 | Cost optimization demonstrated: AI analyzes resource specs, recommends downscaling, and can automate the change.                       |
|  11 | All AI actions are under operator control, with schema-bound prompts and explicit enablement.                                          |
|  12 | Emphasis on audit trails, evidence logging, and regulatory reporting.                                                                  |
|  13 | AI operations start in read-only mode; after validation, can be promoted to active remediation.                                        |
|  14 | Efficiency improved by reacting to events rather than polling.                                                                         |
|  15 | Automates low-risk, repetitive tasks; operators can review and act on AI recommendations.                                              |
|  16 | Not all tasks are automated; critical decisions remain with people.                                                                    |
|  17 | Prefer watch pattern over polling; consider local models for data sovereignty.                                                         |
|  18 | Design ensures clear boundaries, policy constraints, and evidence for regulated environments.                                          |
|  19 | Approach is scalable to other resources beyond caches, e.g., databases and messaging.                                                  |
|  20 | Namespace-by-namespace adoption allows controlled rollout.                                                                             |
|  21 | In multi-tenant environments, label changes are tracked; human intervention can im                                                     |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=oGk8jVz3qZ4)