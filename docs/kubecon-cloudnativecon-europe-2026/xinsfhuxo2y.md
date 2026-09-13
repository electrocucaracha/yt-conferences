---
type: Video Note
title: "From Logs to Decisions: Autonomous AI Agents for Real-Time Kubernetes Threat R... Willem Berroubache"
description: "In this session, William Burbash, a security architect at Orange in Paris, discusses the challenges and solutions related to securing Kubernetes environments using AI and agentic approaches. He highlights the gap between perceived and actua..."
resource: https://www.youtube.com/watch?v=XiNsfhUxO2Y
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this session, William Burbash, a security architect at Orange in Paris, discusses the challenges and solutions related to securing Kubernetes environments using AI and agentic approaches.
He highlights the gap between perceived and actual security, emphasizing that audits alone are insufficient and that real-time monitoring and automated detection are essential to protect customer data and infrastructure.
Burbash describes a multi-agent system that collects and correlates data from various sources, uses machine learning to detect abnormal behaviors, and coordinates responses, while keeping humans involved in approving remediation actions.
Through a demonstration of a vulnerable web application, he illustrates how these agents can detect and respond to attacks such as command injection and crypto mining, applying network policies and blocking vulnerable images.
He concludes by stressing the importance of combining agentic AI for scalable, context-aware defense with human judgment to ensure robust and ethical security operations.
# Main Points

|   # | Main point                                                                                                                                           |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Session focuses on AA agent security in Kubernetes and protecting clusters, environments, and customers from threats.                                |
|   2 | William Burbash, architect at Orange in Paris, designs security monitoring solutions and trains on Kubernetes and cloud native solutions.            |
|   3 | Security expectations often differ from reality; legacy stacks and vulnerabilities (CVEs) are common despite claims of being secure or cloud native. |
|   4 | Security audits are useful but insufficient; runtime monitoring is essential to prove real security in production.                                   |
|   5 | Hackers can exploit applications even if audits pass; runtime events reflect the real-world situation.                                               |
|   6 | Full stack observability is present, but automated detection and immediate remediation need improvement.                                             |
|   7 | Security operations can be overwhelmed by logs, events, and alarms, leading to alert fatigue and missed threats.                                     |
|   8 | AI and agentic solutions are proposed to learn from noise, understand signals, and automate responses.                                               |
|   9 | Multiple agents are used: coordinator agent, threat analyst agent, remediation agent, and notify agent.                                              |
|  10 | Data is collected from logs, metrics, and observability tools (e.g., Elastic, Prometheus, Falco).                                                    |
|  11 | Machine learning models (e.g., isolation forest) are used to detect abnormal behavior and correlate events.                                          |
|  12 | Coordinator agent communicates with other agents to analyze threats, suggest remediation, and notify teams.                                          |
|  13 | Human approval remains important for remediation to avoid errors and maintain a feedback loop.                                                       |
|  14 | Three main axes: feedback loop, training pipeline, and real-time inference for improved detection and decision-making.                               |
|  15 | Demonstration shows detection of command injection and crypto miner attacks in a vulnerable web application.                                         |
|  16 | Remediation includes network isolation (Cilium policy) and blocking vulnerable images (Kyverno policy).                                              |
|  17 | Solution provides contextual fidelity, reduces operational noise, and assists teams in defense and forensic investigation.                           |
|  18 | Risks include hallucination, cascading errors, model                                                                                                 |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=XiNsfhUxO2Y)