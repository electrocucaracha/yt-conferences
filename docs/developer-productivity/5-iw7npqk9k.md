---
layout: default
title: You're Testing WHAT? • Gojko Adzic • GOTO 2021
nav_order: 150
parent: Developer Productivity
type: Video Note
description:
  The speaker discusses how advances in technology and cloud computing
  are changing best practices in automated testing, challenging the traditional testing
  pyramid that emphasizes fast, isolated unit tests. They argue that as software increa...
resource: https://www.youtube.com/watch?v=5_IW7npQk9k
tags:
  - developer-productivity
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The speaker discusses how advances in technology and cloud computing are changing best practices in automated testing, challenging the traditional testing pyramid that emphasizes fast, isolated unit tests.
They argue that as software increasingly relies on third-party services and cloud deployments, the greatest risks now lie in the integration points and moving parts that can only be tested after deployment.
The talk highlights the importance of testing where the risk is, leveraging cloud capabilities for massively parallel testing environments, and designing automated tests to assist humans rather than replace them—especially for non-deterministic or complex outputs like visuals or videos.
The speaker shares examples from their own projects, such as using visual diff tools and approval testing to make tests resilient to change and easier to maintain, and stresses the value of separating the "what" from the "how" in test definitions.
Ultimately, they advocate for rethinking automation to optimize human time, facilitate change, and focus on testing what the system actually does, not just how it does it.

# Main Points

|   # | Main point                                                                                                                                                                           |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Speaker discusses experimenting with new technology and automated testing, challenging traditional best practices.                                                                   |
|   2 | Traditional testing pyramid emphasizes many fast, isolated unit tests, fewer integrated/component tests, and very few end-to-end tests.                                              |
|   3 | Best practices have focused on avoiding slow, brittle, non-deterministic, and frequently changing tests.                                                                             |
|   4 | Cloud deployments shift risk from code units to integration points and third-party services, which can't be fully tested before deployment.                                          |
|   5 | Testing in the cloud enables massively parallel testing environments, making it easier to run tests after deployment.                                                                |
|   6 | Suggests focusing on testing where the risk is, often in the deployed, integrated system rather than just code units.                                                                |
|   7 | Cloud services (e.g., AWS Lambda) allow for multiple parallel environments and gradual traffic shifting during deployment, enabling safer rollouts and automated rollback on errors. |
|   8 | Real user metrics (e.g., conversion rates, sales) can be monitored post-deployment to catch issues not detectable by pre-deployment tests.                                           |
|   9 | Automation should assist humans, not just replace them; automate setup, cleanup, and alerting even for non-deterministic tests.                                                      |
|  10 | Example: No Man’s Sky game used automated probes to surface issues for human review, reducing manual testing burden.                                                                 |
|  11 | Don’t sacrifice test perspective for ease of automation; tests should provide meaningful feedback and facilitate change.                                                             |
|  12 | Visual regression testing (e.g., screenshot comparisons) is used to validate UI changes, making it easier to approve or reject changes and maintain documentation.                   |
|  13 | Automated tests should be designed to facilitate change, not cement code and make it hard to update.                                                                                 |
|  14 | Optimize the diff: invest in tooling that highlights differences for human review, making it easy to spot and act on changes.                                                        |
|  15 | Separate test definition (what the system should do) from test automation (how it does it) to make tests more resilient to change.                                                   |
|  16 | Focus on testing what the sys                                                                                                                                                        |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=5_IW7npQk9k)
