---
type: Video Note
title: "Models as Microservices, Platforms as Partners: Collaboratively Building ML Inf... Stephanie Pavlick"
description: "Stephanie Pavick, a machine learning platform engineer at Hinge, presented an overview of how Hinge has developed its ML platform from the ground up, emphasizing both technical and organizational evolution. Initially, ML engineers built ad..."
resource: https://www.youtube.com/watch?v=6H88ez69VmQ
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Stephanie Pavick, a machine learning platform engineer at Hinge, presented an overview of how Hinge has developed its ML platform from the ground up, emphasizing both technical and organizational evolution.
Initially, ML engineers built ad hoc infrastructure, but as the company scaled, this approach led to inefficiencies and bottlenecks.
The platform team, established two years ago, first built generalized solutions that saw low adoption, prompting a pivot to embedding with product teams and building tools tailored to real user needs.
The resulting Hinge AI platform, "high," now supports diverse training, serving, feature storage, and generative AI needs, leveraging open-source tools and custom SDKs to streamline model deployment and observability.
This new approach has reduced model time to production by 40% and ensured comprehensive SLOs for all online models.
Key lessons include starting with user pain points, baking reliability into defaults, treating ML engineers as partners, and iterating solutions with a willingness to pivot when necessary.
# Main Points

|   # | Main point                                                                                                                                                                                        |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Stephanie Pavick is a machine learning platform engineer at Hinge, focused on model serving and observability.                                                                                    |
|   2 | The talk covers AI at Hinge, platform evolution, serving platform details, and key lessons learned.                                                                                               |
|   3 | AI at Hinge powers matching algorithms, profile improvement features (e.g., prompt feedback, top photo), trust and safety (scammer/bot detection, "are you sure" model), and growth/monetization. |
|   4 | The AI platform core team builds infrastructure enabling all AI models at Hinge.                                                                                                                  |
|   5 | The platform team is about 2 years old; previously, ML engineers built ad hoc infra, leading to inefficiencies and tech debt.                                                                     |
|   6 | Initial platform approach ("ivory tower") built generalized solutions with low adoption; pivoted to embedding with product teams and solving specific problems first.                             |
|   7 | Four main components of the Hinge AI platform ("high"):                                                                                                                                           |
|   8 | Training platform (local/distributed, built on Ray Train)                                                                                                                                         |
|   9 | Serving platform (batch/async/online, batch on Databricks, online on RayServe)                                                                                                                    |
|  10 | Feature store (offline on Databricks Unity Catalog, online on ElastiCache)                                                                                                                        |
|  11 | Generative AI platform (using TensorZero, Arise, LLM as a judge)                                                                                                                                  |
|  12 | Online model serving moved from Databricks endpoints to RayServe with a custom SDK for better scalability, flexibility, and observability.                                                        |
|  13 | Tech stack includes Grafana, Ray, MLflow, Helm, Argo CD, Prometheus, Kubernetes.                                                                                                                  |
|  14 | Model serving workflow: templated project creation, custom SDK, MLflow integration, CLI deployment, out-of-the-box observability.                                                                 |
|  15 | Observability stack: sloth for SLOs, Grafana dashboards, boilerplate SLOs (latency, availability, error rates) auto-created per deployment.                                                       |
|  16 | Achieved 40% reduction in model time to production; 100% of online models now have comprehensive SLOs and observability.                                                                          |
|  17 | Key learnings:                                                                                                                                                                                    |
|  18 | Start with real user pain points.                                                                                                                                                                 |
|  19 | Bake reliability and observability into defaults.                                                                                                                                                 |
|  20 | Treat ML engineers as partners, not customers.                                                                                                                                                    |
|  21 | Deliver iteratively and be willing to pivot.                                                                                                                                                      |
|  22 | Embedding with product team                                                                                                                                                                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=6H88ez69VmQ)