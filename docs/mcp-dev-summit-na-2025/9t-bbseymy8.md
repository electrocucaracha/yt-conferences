---
layout: default
title: "[Session] Scaling MCP with Antje Barth from AWS"
nav_order: 6
parent: Mcp Dev Summit Na 2025
type: Video Note
description:
  Auntie, a principal developer advocate at AWS, discusses practical approaches
  to scaling MCP (Model Coordination Protocol) from local prototyping to cloud-scale
  deployments, focusing on MCP servers. She highlights the growing list of availa...
resource: https://www.youtube.com/watch?v=9T_BBseYmY8
tags:
  - mcp-dev-summit-na-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Auntie, a principal developer advocate at AWS, discusses practical approaches to scaling MCP (Model Coordination Protocol) from local prototyping to cloud-scale deployments, focusing on MCP servers.
She highlights the growing list of available MCP servers on GitHub and demonstrates how existing public APIs, such as AWS documentation, can be wrapped as MCP servers for easy integration.
Auntie explains deployment options on AWS, comparing serverless solutions like AWS Fargate for persistent connections and AWS Lambda for flexible, scalable compute without persistent connections.
She presents a demo of deploying an MCP server as a Lambda function, using a D&D dice-rolling tool as an example, and introduces the open-source Strands SDK for building agents that interact with MCP servers.
The talk concludes with resources for further exploration, including code repositories, a blog post on inter-agent communication, and an invitation to provide feedback for AWS credits.

# Main Points

|   # | Main point                                                                                                                                                |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Auntie is a principal developer advocate at AWS, working closely with Nick and the product team on MCP.                                                   |
|   2 | Focus of the talk is on practical aspects of scaling MCP from local environments to cloud-scale deployments, specifically MCP servers.                    |
|   3 | MCP servers are available at GitHub AWSLAB/MCP, with the list growing frequently.                                                                         |
|   4 | Example: AWS documentation MCP server wraps existing public APIs (search, recommendations, navigation) as tools in an MCP server.                         |
|   5 | Demonstration using Amazon Q dev command-line tool to interact with the AWS docs MCP server via natural language requests.                                |
|   6 | Local environments are good for prototyping, but scaling requires decoupling and running MCP servers remotely.                                            |
|   7 | MCP spec has evolved from standard IO and SSE to supporting streamable HTTP.                                                                              |
|   8 | Currently, only Python and TypeScript SDKs support streamable HTTP; client app support is still catching up.                                              |
|   9 | SSE uses persistent connections; streamable HTTP uses request-response patterns without persistent connections.                                           |
|  10 | For serverless deployments on AWS:                                                                                                                        |
|  11 | Use AWS Fargate for ECS if SSE/persistent connections are needed.                                                                                         |
|  12 | Use AWS Lambda for non-persistent connections; scales automatically and integrates with AWS services.                                                     |
|  13 | Best practice: Place API Gateway in front of Lambda MCP servers; use an authorizer function for security.                                                 |
|  14 | Demo: Lambda function MCP server for rolling dice (D&D example), session state stored in DynamoDB, code available on GitHub.                              |
|  15 | New open source SDK "strands" released for building agents; supports multiple model providers (Amazon Bedrock, Meta Llama, Anthropic, Light LLM, OpenAI). |
|  16 | MCP Lambda handler is a prototype; production use should implement stronger authorization (e.g., Cognito).                                                |
|  17 | Reference to a blog post on inter-agent communication using MCP.                                                                                          |
|  18 | Links provided for code repository, strand agents, and a survey for $25 AWS credit.                                                                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=9T_BBseYmY8)
