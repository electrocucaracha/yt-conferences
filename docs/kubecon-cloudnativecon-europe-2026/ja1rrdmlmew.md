---
type: Video Note
title: "Tutorial: AI on Kubernetes Without the Chaos: Building Reproducible ML Environmen... Nourhan Mohamed"
description: "Norhan Muhammad introduces a talk focused on achieving reproducible and reliable AI workflows on Kubernetes, aiming to reduce chaos in machine learning operations. She explains the importance of reproducibility in ML, using an analogy of tw..."
resource: https://www.youtube.com/watch?v=JA1rrdMLmew
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Norhan Muhammad introduces a talk focused on achieving reproducible and reliable AI workflows on Kubernetes, aiming to reduce chaos in machine learning operations.
She explains the importance of reproducibility in ML, using an analogy of two chefs making cupcakes with the same ingredients but yielding different results, highlighting issues like data leakage and the inability to compare model runs without proper tracking.
Norhan outlines common problems in traditional ML workflows, such as manual tracking, lack of versioning, and environment drift, and presents a framework for reproducibility that includes versioning inputs, pipelines, and artifacts, as well as tracking lineage and automating validation.
She demonstrates a practical MLOps pipeline using open-source tools like Kubeflow, Argo Workflows, MLflow, MinIO, and GitOps, guiding participants through a hands-on lab that automates model training, validation, containerization, and deployment while ensuring traceability and rollback capabilities.
The session concludes with key takeaways—pinning dependencies, tracking lineage, using GitOps, validating before deployment, and maintaining immutable artifacts—and a Q&A addressing hardware reproducibility, centralized tool hosting, and GPU scheduling in Kubernetes environments.
# Main Points

|   # | Main point                                                                                                                                                                                                                                                               |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Norhan Muhammad, DevOps lead at CodeCloud, specializes in virtualization, containerization, and Kubernetes.                                                                                                                                                              |
|   2 | Emphasizes the challenge of chaos and reproducibility in AI/ML workflows, especially on Kubernetes.                                                                                                                                                                      |
|   3 | 300 machine learning papers in 2023 were affected by data leakage and reproducibility issues.                                                                                                                                                                            |
|   4 | Reproducibility is critical to ensure reliable, comparable, and efficient machine learning models.                                                                                                                                                                       |
|   5 | Traditional ML workflows using Jupyter notebooks face issues: loss of work, manual tracking errors, version confusion, lack of rollback, and "it worked on my laptop" problems.                                                                                          |
|   6 | Deploying ML on Kubernetes introduces further chaos: version/environment drift, broken/non-automated pipelines, lack of lineage tracking.                                                                                                                                |
|   7 | Key framework for reproducibility:                                                                                                                                                                                                                                       |
|   8 | Version all inputs, pipelines, and artifacts.                                                                                                                                                                                                                            |
|   9 | Track metrics and lineage from start to finish.                                                                                                                                                                                                                          |
|  10 | Automate validation gates before deployment.                                                                                                                                                                                                                             |
|  11 | Audit and monitor cluster state to detect drift and enable rollback.                                                                                                                                                                                                     |
|  12 | Proposed automated MLOps pipeline:                                                                                                                                                                                                                                       |
|  13 | Train, register, validate, build, and deploy models.                                                                                                                                                                                                                     |
|  14 | Use open-source, cloud-native tools: Kubeflow (orchestrator), Argo Workflows (pipeline execution), ML Metadata (lineage), MLflow (tracking/serving), MinIO (artifact storage), Kaniko (container builds), Git (version control), Argo CD (GitOps/deployment monitoring). |
|  15 | Demo uses a fitness dataset with 39 features and 20,000 records; anomaly detection model with validation gate (3-8% anomaly rate).                                                                                                                                       |
|  16 | Pipeline stages: train model, register model, validate, build/push container, deploy via GitOps.                                                                                                                                                                         |
|  17 | Each pipeline step runs in a separate, version-pinned container to prevent data leakage and ensure reproducibility.                                                                                                                                                      |
|  18 | MLflow and Kubeflow enable experiment comparison, artifact versioning, and rollback.                                                                                                                                                                                     |
|  19 | GitOps with Argo CD ensures desired state is maintained and monitored in production.                                                                                                                                                                                     |
|  20 | Key takeaways:                                                                                                                                                                                                                                                           |
|  21 | Pin all dependencies and environments.                                                                                                                                                                                                                                   |
|  22 | Track full lineage.                                                                                                                                                                                                                                                      |
|  23 | Use GitOps for deployment.                                                                                                                                                                                                                                               |
|  24 | Valida                                                                                                                                                                                                                                                                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=JA1rrdMLmew)