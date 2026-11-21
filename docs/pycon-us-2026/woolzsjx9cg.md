---
layout: default
title: "Zero Trust in 200ms: Implementing Identity-Per-Transaction with Python & Serverless-Tristan McKinnon"
nav_order: 74
parent: PyCon US 2026
type: Video Note
description: "Tristan McKinnon presents an identity-per-transaction architecture designed to mitigate the security risks of broad service account credentials in enterprise data pipelines."
resource: "https://www.youtube.com/watch?v=WOOlzsJx9cg"
youtube_stats:
  view_count: 225
  like_count: 2
  channel_subscriber_count: 34500
tags:
  - pycon-us-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-20T08:08:06+00:00
---

# Summary

Tristan McKinnon presents an identity-per-transaction architecture designed to mitigate the security risks of broad service account credentials in enterprise data pipelines.
By leveraging AWS STS to issue ephemeral, single-file scoped credentials that expire within 900 seconds, the system ensures that even if a credential is compromised, the attacker gains access to only one specific object rather than the entire data lake.
The solution, packaged in an open-source library called Mayfly, operates within a three-zone architecture consisting of a dirty zone for ingestion, an isolated airlock for processing, and a clean zone for governed data, with data flowing strictly in one direction.
Within the airlock, the system uses Microsoft Presidio and Python generators to de-identify data in stream, maintaining flat memory usage while quarantining records with low confidence scores to prevent PHI leakage.
This approach satisfies strict compliance requirements like FedRAMP High by logging credential lifecycles rather than sensitive data content, thereby avoiding the creation of new attack surfaces through audit logs.
The implementation demonstrates a negligible performance overhead of approximately 0.1% while structurally eliminating configuration drift and reducing the potential blast radius of a breach by six orders of magnitude compared to traditional models.

# Main Points

|   # | Main point                                                                                                                                                                                         |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker, Tristan McKinnon, presents an identity-per-transaction architecture for secure data pipelines, published at the IEEE Big Data Security Conference.                                    |
|   2 | Traditional enterprise data pipelines often use a single service account with broad access to the entire data lake, creating a significant security risk if compromised.                           |
|   3 | The proposed solution replaces long-lived credentials with ephemeral, scoped credentials generated for each individual file transaction.                                                           |
|   4 | Each credential is built on AWS STS, allowing access to only one specific S3 object for a maximum duration of 900 seconds before expiring.                                                         |
|   5 | The architecture is validated against FedRAMP High standards, the US federal government's strictest cloud security baseline, but is applicable to other compliance frameworks like HIPAA and GDPR. |
|   6 | The data flow consists of three zones: a dirty zone (encrypted S3 bucket), an airlock (isolated VPC for processing), and a clean zone (destination for de-identified data).                        |
|   7 | Data flows strictly from left to right through these zones, with the airlock containing no internet gateway to prevent external communication.                                                     |
|   8 | An identity broker provisions scoped credentials just-in-time, ensuring the processing function can only touch the specific file it is assigned.                                                   |
|   9 | The open-source library "Mayfly" implements this pattern, using a decorator to inject scoped credentials into processing functions.                                                                |
|  10 | The underlying mechanism uses an inline IAM policy with a single resource ARN, intersecting with the role's permissions to restrict access to one file.                                            |
|  11 | Session names embed a trace ID to ensure every credential is traceable back to the exact invocation that created it for auditability.                                                              |
|  12 | The overhead of generating these credentials is approximately 120 milliseconds for warm calls, representing about 0.1% of total processing time for typical files.                                 |
|  13 | De-identification is performed in-stream using Microsoft Presidio to analyze PII entities without loading the full dataset into memory.                                                            |
|  14 | A confidence threshold of 0.95 is used for de-identification; records below this threshold are quarantined for human review to prevent false negatives.                                            |
|  15 | Audit logging records the credential lifecycle, including creation, resource ARN, and duration, but never logs sensitive data content to avoid creating new attack surfaces.                       |
|  16 | Logs are shipped to S3 with object lock in compliance mode, ensuring they are immutable and cannot be deleted or overwritten.                                                                      |
|  17 | This approach reduces the blast radius from the entire data lake to a single file, effectively reducing risk by six orders of magnitude for large datasets.                                        |
|  18 | Ephemeral compute is used, resulting in zero idle costs and eliminating configuration drift associated with persistent infrastructure.                                                             |
|  19 | The system shifts the trust floor to the identity broker, which is monitored for behavioral anomalies to prevent misuse.                                                                           |
|  20 | Access to the clean zone is restricted, requiring re-authentication per query and potentially using graph neural networks to detect re-identification attacks.                                     |
|  21 | The speaker recommends stopping key rotation in favor of ephemeral credentials, scrubbing data before storage, and logging only the lifecycle of access rather than the data itself.               |

# Video

[![Video thumbnail](https://img.youtube.com/vi/WOOlzsJx9cg/hqdefault.jpg)](https://www.youtube.com/watch?v=WOOlzsJx9cg)

[Watch on YouTube](https://www.youtube.com/watch?v=WOOlzsJx9cg)
