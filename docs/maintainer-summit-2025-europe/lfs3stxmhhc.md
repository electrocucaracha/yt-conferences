---
layout: default
title: "A Project Maintainers Guide To TAG Security - Marina Moore, Edera & Andres Aguiar, Okta"
nav_order: 8
parent: "Maintainer Summit 2025 - Europe"
type: Video Note
description: Marina Moore and Andre present a case study on how the OpenFGA project collaborated with the CNCF TAG Security group to enhance its security posture during its transition from Sandbox to Incubation.
resource: "https://www.youtube.com/watch?v=LFs3STxmhHc"
tags:
  - maintainer-summit-2025-europe
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-15T22:30:54+00:00
---

# Summary

Marina Moore and Andre present a case study on how the OpenFGA project collaborated with the CNCF TAG Security group to enhance its security posture during its transition from Sandbox to Incubation.
The speakers detail their participation in the Security Slam, where OpenFGA achieved all five security badges by improving repository hygiene, completing self-assessments, and integrating with tools like the OpenSSF Scorecard.
They also discuss the value of joint security assessments, which provided deep, collaborative reviews of the project’s security architecture and helped the team navigate complex decisions, such as determining whether to issue a CVE for a specific experimental flag.
The presentation highlights that TAG Security’s role is primarily to guide projects in establishing robust security processes and best practices rather than acting as a blocker, emphasizing the importance of continuous improvement and community engagement.
Finally, the speakers encourage other maintainers to utilize available resources, such as white papers and community meetings, to proactively manage their projects' security and prepare for future CNCF level advancements.

# Main Points

|   # | Main point                                                                                                                                                                                              |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | TAG Security is a CNCF group dedicated to improving the security of cloud-native and open-source projects through direct interaction, guidance, and white papers.                                       |
|   2 | OpenFGA is an authorization system based on Relationship-Based Access Control, inspired by Google's Zanzibar research, and is currently in the CNCF Sandbox awaiting incubation evaluation.             |
|   3 | The CNCF incubation process requires projects to meet specific criteria across governance, maintainers, community, engineering, security, and ecosystem categories.                                     |
|   4 | Security requirements for incubation include completing self-assessments, achieving a 100% Scorecard score, generating Software Bills of Materials, and conducting joint assessments with TAG Security. |
|   5 | The Security Slam is a metric-driven hackathon initiative where projects earn badges by completing actionable security tasks such as documentation, monitoring, and SBOM creation.                      |
|   6 | OpenFGA successfully earned all five Security Slam badges in 2023, which helped identify and address previously unknown security gaps in the project.                                                   |
|   7 | TAG Security offers two types of assessments: self-assessments for internal reflection and joint assessments involving collaborative reviews with TAG Security members.                                 |
|   8 | Joint assessments provide in-depth security analysis and threat modeling, helping projects understand their security posture and identify areas for improvement.                                        |
|   9 | Projects can consult TAG Security for specific security decisions, such as whether to issue a CVE for experimental features that may have security implications.                                        |
|  10 | TAG Security hosts community demos and longer-form presentations to allow projects to share work and discuss security practices with the community.                                                     |
|  11 | Publications from TAG Security include the Cloud Native Security White Paper, Software Supply Chain Best Practices, and the Cloud Native Controls Catalog.                                              |
|  12 | TAG Security maintains a catalog of software supply chain compromises and provides resources for compliance, automated governance, and threat modeling.                                                 |
|  13 | Engaging with TAG Security is recommended before formal security audits to establish proper processes and best practices, making subsequent audits more effective.                                      |
|  14 | The goal of TAG Security is to provide guidance and resources rather than act as a blocker, focusing on process improvement and security hygiene.                                                       |
|  15 | Tools like OpenSSF Scorecard and Best Practices badges help projects quickly assess their security posture and identify basic hygiene issues.                                                           |
|  16 | For authorization systems like OpenFGA, bugs often have direct security implications, requiring rigorous testing automation to cover complex policy combinations.                                       |
|  17 | AI-driven fuzzing and test generation are being explored to handle the complexity of authorization models, though manual verification of generated tests remains necessary.                             |
|  18 | Projects are encouraged to participate in TAG Security community meetings across different time zones and to engage with the team on GitHub or CNCF Slack.                                              |

# Video

[![Video thumbnail](https://img.youtube.com/vi/LFs3STxmhHc/hqdefault.jpg)](https://www.youtube.com/watch?v=LFs3STxmhHc)

[Watch on YouTube](https://www.youtube.com/watch?v=LFs3STxmhHc)
