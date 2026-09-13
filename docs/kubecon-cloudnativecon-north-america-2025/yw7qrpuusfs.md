---
type: Video Note
title: "SIG API Machinery and AI: What Comes Next? - Joe Betz, Google & David Eads, Red Hat"
description: "The presentation discusses using AI to interact with Kubernetes, focusing on interacting directly with the cluster API rather than building AI systems on top of Kubernetes. The speakers identify common use cases for AI in Kubernetes, includ..."
resource: https://www.youtube.com/watch?v=yW7QRpUUSFs
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The presentation discusses using AI to interact with Kubernetes, focusing on interacting directly with the cluster API rather than building AI systems on top of Kubernetes.
The speakers identify common use cases for AI in Kubernetes, including triage and diagnostics, cost optimization, proactive planning, reactive analysis, and ensuring data security.
They propose ideas to improve the interaction between AI and Kubernetes, such as formalizing implicit relationships in the Kubernetes API, developing relationship-aware querying mechanisms, and implementing attenuation to limit AI access to sensitive data.
The speakers also explore the challenges of creating a filtered list of resources that an AI can see, highlighting the need for a solution that balances granularity with scalability.
# Main Points

|   # | Main point                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Specifying relationships between resources in CRDs                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|   2 | Using HTTP content types to provide filtered lists                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|   3 | Tracking sensitive resources and marking them as such • The problem of ensuring that AI systems don't get too much access to sensitive data is discussed. • A potential solution involves having a way for users to request only the necessary information, with options for filtering by namespace or other criteria. • The idea of attenuation (limiting the lifespan of a token) is proposed as a way to improve security and auditing. • The importance of auditability and logging is emphasized. |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=yW7QRpUUSFs)