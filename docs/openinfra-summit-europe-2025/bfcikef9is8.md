---
layout: default
title: The Invisible Work Behind OpenStack
nav_order: 102
parent: OpenInfra Summit Europe 2025
type: Video Note
description: 'Jay Faulner, an open source developer and OpenStack contributor, defines "invisible work" as essential tasks that often lack community recognition or proper prioritization, leading to significant t...'
resource: "https://www.youtube.com/watch?v=bfCiKEf9iS8"
youtube_stats:
  view_count: 61
  like_count: 1
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

Jay Faulner, an open source developer and OpenStack contributor, defines "invisible work" as essential tasks that often lack community recognition or proper prioritization, leading to significant technical and structural debt.
He illustrates this concept with two contrasting case studies: the successful, coordinated effort to remove the unmaintained Eventlet library from OpenStack to ensure Python compatibility, and the critical failure to maintain the Murano project, which resulted in a severe security vulnerability that could not be patched due to a lack of active contributors.
Faulner argues that these issues stem from structural misalignments in open source incentives, such as the preference for visible product features over invisible maintenance, time erosion, and the reliance on individual heroics rather than sustainable community processes.
To address these challenges, he emphasizes the need for better governance, such as implementing project inactivity frameworks and ensuring diverse geographic representation in security and funding, to protect digital sovereignty and fulfill support promises to operators.
Ultimately, Faulner urges the community to move away from a "do it eventually" mindset by making invisible work visible, creating strong business cases for its resolution, and actively investing in code review and new contributor development to prevent systemic failures.

# Main Points

|   # | Main point                                                                                                                                                                                                            |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Invisible work in OpenStack consists of essential tasks that lack community respect or visibility, often leading to accumulated technical and non-technical debt.                                                     |
|   2 | Identifying invisible work requires asking when the debt will come due, who it is invisible to, and why it remains unseen, acknowledging that all individuals have blind spots.                                       |
|   3 | The status quo of ignoring invisible work is incorrect; the community must either perform the work, make it visible to prioritize it, or discard the component entirely.                                              |
|   4 | Communication is critical for addressing structural issues, requiring a clear audience identification and a business case that highlights the risks of inaction to secure committed organizational resources.         |
|   5 | The removal of Eventlet from OpenStack serves as a success story, where the community identified maintenance risks, created a business case, and dedicated resources to migrate projects to modern Python standards.  |
|   6 | Specific actions for the Eventlet removal included recruiting experts, securing access to the repository, providing compatibility shims, and setting a hard deadline for project completion to enforce urgency.       |
|   7 | The Murano security vulnerability (OSSN 93) illustrates a failure where a critical bug went unfixed due to a lack of active contributors, highlighting the danger of invisible maintenance gaps.                      |
|   8 | Governance processes failed to identify Murano's risk because there was no one in the community to raise the alarm, allowing the project to remain in a state where it could not fulfill support promises.            |
|   9 | Structural pressures such as supply and demand dynamics favor visible, product-impacting work over invisible maintenance, leading to neglect of tasks that are only noticed when they fail.                           |
|  10 | Time erosion and burnout accelerate when unappreciated work is performed by individuals without systemic support, often resulting in downstream priorities overriding long-term maintenance needs.                    |
|  11 | Inconsistent contribution patterns, where developers focus on specific features rather than recurring maintenance, add to the invisible workload and prevent steady, tortoise-like progress.                          |
|  12 | Most invisible work falls into the "important but not urgent" category, often labeled as "eventually," which rarely materializes without deliberate prioritization and scheduling.                                    |
|  13 | Key areas needing attention include maintaining compatible library versions, diversifying the Vulnerability Management Team geographically, and improving quality assurance infrastructure like DevStack and Tempest. |
|  14 | Code review is a critical invisible task that requires both new contributors to engage and senior leaders to mentor, ensuring a sustainable pipeline of core reviewers.                                               |
|  15 | Governance diversity is essential to prevent single-company dominance in the Technical Committee, protecting the project's multi-vendor integrity and perception.                                                     |
|  16 | Foundation funding is heavily skewed toward US dollars despite EU code contributions, creating a sovereignty vulnerability that requires broader financial support.                                                   |
|  17 | Individuals should prevent "code rot" by making business cases for maintenance work, dedicating time to unblock others, or retiring projects that cannot be properly maintained.                                      |

# Video

[![Video thumbnail](https://img.youtube.com/vi/bfCiKEf9iS8/hqdefault.jpg)](https://www.youtube.com/watch?v=bfCiKEf9iS8)

[Watch on YouTube](https://www.youtube.com/watch?v=bfCiKEf9iS8)
