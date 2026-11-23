---
layout: default
title: "Building OpenDev: A Zuul for Operations Story"
nav_order: 110
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Clark Boyan, an OpenDev CI/CD administrator and Zuul maintainer, presents how OpenDev utilizes Zuul to empower a small operations team by treating it as a robust deployment and testing tool rather ..."
resource: "https://www.youtube.com/watch?v=D62BnYDgUkc"
youtube_stats:
  view_count: 55
  channel_subscriber_count: 46800
tags:
  - openinfra-summit-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T23:38:50+00:00
---

# Summary

Clark Boyan, an OpenDev CI/CD administrator and Zuul maintainer, presents how OpenDev utilizes Zuul to empower a small operations team by treating it as a robust deployment and testing tool rather than just a software development platform.
By leveraging Zuul’s gating capabilities and multi-node testing, OpenDev eliminates the need for separate staging environments, allowing them to deploy directly to production with high confidence that changes will function correctly.
The workflow relies heavily on Ansible for configuration management, using identical playbooks and bastion hosts in both test and production environments to ensure consistency and reduce the risk of deployment failures.
Additionally, Zuul’s speculative testing allows the team to validate complex interactions between independent components, such as Gerrit and Zuul, before committing to upgrades, thereby preventing regressions and ensuring system stability.
Boyan concludes by encouraging other operations teams to adopt Zuul, highlighting its flexibility for various infrastructure setups and the benefits of community-driven development for maintaining reliable, open-source tooling.

# Main Points

|   # | Main point                                                                                                                                                               |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | OpenDev is a collaborative platform for open source software development that relies entirely on open source tools for its infrastructure.                               |
|   2 | The core message is that Zuul is a powerful tool for operations teams, not just software development, enabling small teams to manage production deployments effectively. |
|   3 | OpenDev uses Zuul for CI/CD, Ansible for configuration management, and various communication tools like Mailman, Etherpad, and GigaMeet.                                 |
|   4 | The organization practices "eating its own dog food" by hosting Zuul on OpenDev and using OpenDev tools to manage OpenDev itself.                                        |
|   5 | Key reasons for using Zuul include Ansible integration, project gating, multi-node testing, and speculative testing of artifacts like Git commits and container images.  |
|   6 | OpenDev has eliminated staging environments by using Zuul's gating capabilities to test changes thoroughly before merging directly to production.                        |
|   7 | Test environments are modeled to mimic production, including bastion nodes and the same Ansible versions and playbooks used in live deployments.                         |
|   8 | Speculative testing allows independent components like Gerrit, Git, and Zuul to be tested together before any single upgrade is committed.                               |
|   9 | The workflow involves pushing changes to Gerrit, running check tests for early feedback, and then gating tests before merging.                                           |
|  10 | Test-in-for-tests are used for systems-level checks, such as verifying service ports, package installation, and file existence after deployment.                         |
|  11 | Selenium integration allows for web service screenshot testing to catch rendering issues, such as UTF-8 problems in Etherpad.                                            |
|  12 | Production deployment dynamically modifies the Zuul job inventory to include a bastion host, using project-specific SSH keys for secure access.                          |
|  13 | The same Ansible playbooks used in testing are executed in production, ensuring consistency between test and live environments.                                          |
|  14 | Deployment jobs are organized by service to avoid unnecessary work, using file matchers to select relevant jobs based on code changes.                                   |
|  15 | Daily periodic jobs run to catch up on any missed deployments and ensure system consistency across the board.                                                            |
|  16 | A bootstrap bridge job runs first to configure the bastion host, followed by parallel execution of other jobs to speed up deployments.                                   |
|  17 | Build sets are serialized to maintain a clear sequence of changes, preventing debugging complexity from mixed deployments.                                               |
|  18 | Zuul upgrades are handled via a weekly cron job to avoid the chicken-and-egg problem of shutting down executors while Zuul is running.                                   |
|  19 | The approach is flexible and can be adapted for Kubernetes or bare metal environments by adjusting how Zuul interacts with the infrastructure.                           |
|  20 | Rollbacks are generally handled by rolling forward with new changes and regression tests, or by manual intervention on the bastion host for urgent issues.               |
|  21 | Zuul does not currently support manual dispatches for job triggering, requiring changes to be pushed through the Git review system.                                      |
|  22 | Monitoring is achieved through Zuul reporters like Elasticsearch, email, and MQTT, or via a Prometheus stats exporter for status metrics.                                |
|  23 | The community encourages involvement and learning by contributing to OpenDev, providing a low-risk environment to practice operations skills.                            |

# Video

[![Video thumbnail](https://img.youtube.com/vi/D62BnYDgUkc/hqdefault.jpg)](https://www.youtube.com/watch?v=D62BnYDgUkc)

[Watch on YouTube](https://www.youtube.com/watch?v=D62BnYDgUkc)
