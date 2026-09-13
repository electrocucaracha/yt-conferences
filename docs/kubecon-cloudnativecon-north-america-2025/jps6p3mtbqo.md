---
type: Video Note
title: "Securing Data Applications at Pinterest With Finer Grained Access Cont... Soam Acharya & William Tom"
description: "In this talk at CubeCon, Pinterest’s data engineering team discusses how they secured data applications by implementing fine-grained access control (FGAC) on their Kubernetes-based big data platform, Mocha, which runs Spark on AWS EKS. They..."
resource: https://www.youtube.com/watch?v=jPS6P3mTbqo
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk at CubeCon, Pinterest’s data engineering team discusses how they secured data applications by implementing fine-grained access control (FGAC) on their Kubernetes-based big data platform, Mocha, which runs Spark on AWS EKS.
They describe the transition from Hadoop to Kubernetes for improved security, scalability, and cost efficiency, highlighting the limitations of Hadoop’s security controls and the advantages of Kubernetes and AWS services.
The FGAC system ensures that each user and workload has a unique identity, with access to S3 data sets controlled through a combination of pod-level annotations, certificates, and a custom credential vending service that issues scoped, temporary AWS STS tokens based on LDAP group mappings.
The architecture uses components like Archer, Drum, and Volance to intercept and manage credential requests transparently, requiring no application-specific security logic and supporting both human and service identities.
The team emphasizes that their approach is designed for transparency and compatibility with standard AWS libraries, and they plan to extend FGAC to more applications and finer data access levels in the future.
# Main Points

|   # | Main point                                                                                                                                                                                 |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Presentation focused on securing data applications at Pinterest with fine-grained access control (FGAC) on Kubernetes.                                                                     |
|   2 | Pinterest’s data platform processes user activities, third-party data, and merchant catalogs via APIs, CDC, and Apache Kafka, storing data in S3 and processing it in a big data platform. |
|   3 | Transitioned from Hadoop-based batch processing to Spark on EKS (Mocha) for improved security, cost efficiency, and future-proofing.                                                       |
|   4 | Mocha handles ~12,000 EKS nodes, ~30,000 Spark jobs/day, ~1 exabyte of S3 data, ~80 petabytes processed daily, and ~350,000 pods at peak.                                                  |
|   5 | Users submit jobs via Airflow, Jupyter, or Querybook; Archer acts as the job submission gateway, creating Spark application CRDs for EKS clusters.                                         |
|   6 | Spark Operator and Apache Unicorn manage job scheduling and resource allocation; jobs consume and output data to S3.                                                                       |
|   7 | FGAC ensures users and workloads have unique identities, mapped to access policies, controlling S3 dataset access.                                                                         |
|   8 | Identities are securely transmitted via MTLS and certificates; Archer injects pod annotations with identity info into Spark/Flink/Ray CRDs.                                                |
|   9 | Standard AWS IMDS credential flow is bypassed; Pinterest uses an internal identity access management proxy and credential vending service (CVS) to issue scoped STS tokens.                |
|  10 | Drum (daemonset) intercepts credential requests at the node level, checks pod metadata, and forwards to Volance (centralized security service) if needed.                                  |
|  11 | Volance authenticates requests, fetches credentials from AWS or CVS, and returns them to the pod.                                                                                          |
|  12 | CVS maps LDAP users/service accounts to S3 policies, issues scoped STS tokens after code-reviewed policy mapping.                                                                          |
|  13 | Kubernetes annotations and scoped-down service accounts enable FGAC; X.509 certificates are issued at pod level for service-to-service communication.                                      |
|  14 | FGAC is transparent to applications; no app-specific logic required; supports both human and non-human identities via LDAP.                                                                |
|  15 | Future plans: onboard all Spark/Flink jobs, expand to Ray/PyTo                                                                                                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=jPS6P3mTbqo)