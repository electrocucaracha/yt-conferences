---
layout: default
title:
  "Beyond Stateless: Distributed Transactions with Autoscaling and Consistency
  on K... Jumpei Nishitani"
nav_order: 26
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this CubeCom session, Jere Nishani, a software engineer at Hitachi,
  challenges the long-held belief that strong consistency and scalability are mutually
  exclusive in distributed systems. He explains the fragility of traditional online
  tr...
resource: https://www.youtube.com/watch?v=Lq-nQ8iTnrQ
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

In this CubeCom session, Jere Nishani, a software engineer at Hitachi, challenges the long-held belief that strong consistency and scalability are mutually exclusive in distributed systems.
He explains the fragility of traditional online transaction processing (OLTP) systems, particularly their vulnerability to failures and the complexity that arises when scaling state machines across multiple nodes.
Nishani introduces a new approach based on contract law principles, mapping them to technical properties like consistency, atomicity, and durability, and presents the Paxos Commit Transaction Orchestrator (PCT), a cloud-native transaction monitor designed for Kubernetes.
This architecture separates transaction management from business logic, uses distributed consensus for robust and scalable coordination, and leverages reactive processing to maintain low response times regardless of the number of microservices.
Through this design, Nishani demonstrates that it is possible to achieve both strong consistency and seamless autoscaling, offering a practical solution for modern, resilient distributed systems.

# Main Points

|   # | Main point                                                                                                                                                                                 |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Traditional belief: strong consistency and scalability are mutually exclusive in distributed systems.                                                                                      |
|   2 | Goal: Achieve both distributed transactions and seamless autoscaling on Kubernetes.                                                                                                        |
|   3 | Presenter: Jere Nishani, software engineer at Hitachi, specializing in distributed systems and transaction processing.                                                                     |
|   4 | Agenda: 1. Deep dive into online transaction needs and state machine pain points. 2. Reframe the state machine scaling problem. 3. Present the Paxoscom transaction orchestrator solution. |
|   5 | Online transaction processing (OLTP) is fragile and vulnerable to failures and network delays.                                                                                             |
|   6 | Typical enterprise architecture: presentation layer, application layer (often microservices on Kubernetes), and data layer (databases/mainframes).                                         |
|   7 | High switching cost for stateful components leads to monolithic systems.                                                                                                                   |
|   8 | State machines are natural for transaction logic but have weaknesses:                                                                                                                      |
|   9 | Single state machine is vulnerable to failures.                                                                                                                                            |
|  10 | Distributed state machines can become inconsistent due to message loss.                                                                                                                    |
|  11 | Scaling increases complexity and points of failure.                                                                                                                                        |
|  12 | Distributed stateful parts can cause combinatorial explosion and loss of system understanding.                                                                                             |
|  13 | Consensus algorithms (e.g., Paxos, Raft) and tools like etcd help but introduce latency and scalability issues.                                                                            |
|  14 | Atomic broadcast is slow and limits microservice scalability.                                                                                                                              |
|  15 | Solution: Redesign transaction model based on contract law principles (consistency, atomicity, durability).                                                                                |
|  16 | Generalize business state machines into technical state machines for cloud-native systems.                                                                                                 |
|  17 | Introduce a modern, cloud-native transaction monitor as an abstract component.                                                                                                             |
|  18 | Core technology: Paxos Commit Transaction Orchestrator (PCT), a lightweight, scalable transaction coordinator.                                                                             |
|  19 | Transaction management is decoupled from middleware, enabling independent scaling.                                                                                                         |
|  20 | Sequence: Transaction begins, services vote, coordinators reach distributed consensus, commit/abort decision is made.                                                                      |
|  21 | Coordinators are autoscaled independe                                                                                                                                                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Lq-nQ8iTnrQ)
