---
type: Video Note
title: "From Scopes To Intent: Reimagining Authorization for Autonomou... Andres Aguiar & Abhishek Hingnikar"
description: "In this presentation, Andreas from Opta and Abishek from Octa discuss the challenges of authorizing autonomous agents, particularly as their autonomy and access to business tools increase potential risks. They illustrate how current industr..."
resource: https://www.youtube.com/watch?v=pQnsFT7BViE
tags: ["mcp-dev-summit-na-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this presentation, Andreas from Opta and Abishek from Octa discuss the challenges of authorizing autonomous agents, particularly as their autonomy and access to business tools increase potential risks.
They illustrate how current industry practices, such as OAuth scopes, often grant agents broad permissions, making it difficult to limit access to only what is necessary for a specific task and exposing systems to risks like prompt injection attacks.
Through demos, they showcase approaches for fine-grained, intent-based authorization, where permissions are dynamically granted per task rather than per agent, reducing the attack surface and improving security.
They highlight ongoing research and industry efforts, including projects like Open FGA and containment strategies, to address these issues, emphasizing that intent-based authorization alone is not sufficient and must be combined with other security layers.
The talk concludes by inviting further discussion and sharing resources for those interested in experimenting with these emerging authorization models.
# Main Points

|   # | Main point                                                                                                                                        |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Andreas leads Open FGA, an open-source authorization platform under CNCF and Linux Foundation.                                                    |
|   2 | Abishek is a product architect at Okta, focused on Osuro for AI agents.                                                                           |
|   3 | The talk addresses authorization challenges for autonomous agents, especially moving from scopes to intent-based models.                          |
|   4 | Increasing agent autonomy increases risk.                                                                                                         |
|   5 | Human understanding of intent allows nuanced task execution and discretion; agents lack this.                                                     |
|   6 | Current industry standard uses OAuth scopes for delegation, granting broad permissions to agents.                                                 |
|   7 | OAuth scopes provide permission, not fine-grained authorization.                                                                                  |
|   8 | Integrations often force users to grant all permissions, lacking granularity.                                                                     |
|   9 | IT and application policies can restrict agent actions, but limitations remain.                                                                   |
|  10 | Agents are vulnerable to prompt injection, a form of social engineering.                                                                          |
|  11 | Prompt injection can trick agents into unauthorized actions, such as sending sensitive data externally.                                           |
|  12 | Limiting agent access by defining fine-grained permissions or agent-specific scopes is possible but not scalable.                                 |
|  13 | The core problem: agents retain full access to all delegated resources, regardless of task.                                                       |
|  14 | Proposed solution: limit agent access per task, granting only necessary permissions at runtime.                                                   |
|  15 | Demo showcased intent-based authorization, where permissions are linked to specific tasks, not users or agents.                                   |
|  16 | The system infers required permissions from the prompt and grants them only for the task's duration.                                              |
|  17 | Prompt injection attempts can be blocked if the requested action falls outside the task's original intent.                                        |
|  18 | Open FGA is used to manage task-specific permissions.                                                                                             |
|  19 | Industry research shows intent inference works with few tools but struggles as tool count increases.                                              |
|  20 | Mission shaping and containment strategies are needed for robust agent security.                                                                  |
|  21 | Multiple layers—delegation, fine-grained authorization, intent-based controls, and containment—are necessary for safe autonomous agent operation. |
|  22 | Resources and demo code are av                                                                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=pQnsFT7BViE)