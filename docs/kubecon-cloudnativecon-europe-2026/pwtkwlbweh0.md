---
layout: default
title:
  "The Developer’s Nightmare: How To Survive Compliance Che... Alexandra Hou
  Aldershaab & Thomas Vitale"
nav_order: 355
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this talk, Alexandra and Thomas discuss the challenges developers
  face with compliance checklists when trying to ship new features quickly. They demonstrate
  how manual compliance processes—such as license approvals, vulnerability waivers...
resource: https://www.youtube.com/watch?v=PWtkwLbwEH0
tags:
  - kubecon-cloudnativecon-europe-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

In this talk, Alexandra and Thomas discuss the challenges developers face with compliance checklists when trying to ship new features quickly.
They demonstrate how manual compliance processes—such as license approvals, vulnerability waivers, and audit trails—can be overwhelming and slow down development.
By leveraging tools like SBOMs, Dependency Track, automated GitHub integrations, commit and image signing, and frameworks like SLSA, they show how much of the compliance burden can be automated within CI/CD pipelines.
This automation not only ensures that legal and security requirements are met but also allows developers to focus on building features rather than paperwork.
Ultimately, they advocate for embedding compliance into developer platforms, enabling teams to deliver secure, compliant software efficiently while fostering collaboration between developers and compliance stakeholders.

# Main Points

|   # | Main point                                                                                                                                                          |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation topic: Surviving compliance checklists while shipping software fast                                                                                    |
|   2 | Speakers: Alexandra (DevOps consultant at Fode, Friends of Dorothy community) and Thomas Vitali (Senior Software Architect at Systematic, Java/cloud native expert) |
|   3 | Compliance is a major bottleneck for developers wanting to release features to production                                                                           |
|   4 | Common compliance hurdles: change approval boards, license checks, tickets, meetings, waivers, vulnerabilities, checklists                                          |
|   5 | Manual compliance processes are slow, error-prone, and demotivating                                                                                                 |
|   6 | Solution: Automate compliance steps using tools and integrations                                                                                                    |
|   7 | Use SBOMs (Software Bill of Materials) to track application components; generate SBOMs with plugins (e.g., CycloneDX for Java/Gradle)                               |
|   8 | Dependency Track used to manage and audit licenses and vulnerabilities; legal teams approve licenses once, benefiting all projects                                  |
|   9 | Automate license compliance: create GitHub issues or emails for non-compliant licenses via Dependency Track API                                                     |
|  10 | Vulnerability management: not all CVEs are relevant; contextualize and document waivers for non-exploitable vulnerabilities                                         |
|  11 | Use Dependency Track to check for vulnerabilities, outdated components, and integrity issues                                                                        |
|  12 | Automate dependency updates with Renovate; integrates with CI/CD to create pull requests for new versions                                                           |
|  13 | SBOMs must be published to Dependency Track as part of CI/CD workflow                                                                                               |
|  14 | Define development environments as code (e.g., with Flux/Nix) for consistency between local and CI environments                                                     |
|  15 | Git alone does not provide a secure audit trail; enforce signed commits for authentication                                                                          |
|  16 | Sign container images with cosign (Sigstore) in CI pipelines; add attestations for traceability (SLSA framework)                                                    |
|  17 | Use Kubernetes policies (e.g., Kyverno) to enforce compliance before deploying to production                                                                        |
|  18 | Automate compliance checks in pipelines to block non-compliant releases                                                                                             |
|  19 | Platform teams can provide developer-friendly APIs (e.g., with Crossplane) to automate compliance as a service                                                      |
|  20 | Develop                                                                                                                                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=PWtkwLbwEH0)
