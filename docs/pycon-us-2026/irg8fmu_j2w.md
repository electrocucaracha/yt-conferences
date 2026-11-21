---
layout: default
title: "Building a New Approach to Enterprise Python Libraries (Sponsor: Capital One)"
nav_order: 105
parent: PyCon US 2026
type: Video Note
description: "At PyCon, Capital One engineers Dan and David presented a strategy for optimizing enterprise Python development in the age of AI, arguing that traditional internal wrapper SDKs often hinder rather ..."
resource: "https://www.youtube.com/watch?v=iRg8fMu_j2w"
youtube_stats:
  view_count: 734
  like_count: 1
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

At PyCon, Capital One engineers Dan and David presented a strategy for optimizing enterprise Python development in the age of AI, arguing that traditional internal wrapper SDKs often hinder rather than help LLM performance.
They explained that because AI models are trained primarily on open-source libraries and natural language, they struggle to understand proprietary, deeply nested internal abstractions, leading to hallucinations and inefficient token usage.
To address this, the speakers advocated for replacing heavy SDKs with lightweight middleware extensions that preserve the context of standard open-source tools like FastAPI, allowing AI to generate code more accurately while still enforcing enterprise governance and security standards.
They also outlined a process for "context wrangling" in legacy repositories, where teams recursively document dependency trees and create context files to teach AI models how to navigate and maintain complex internal codebases effectively.
Ultimately, the talk emphasized that by aligning software architecture with AI capabilities—favoring open-source standards and transparent middleware—enterprises can maximize their AI investments, reduce technical debt, and ensure that AI agents focus their computational power on delivering genuine business value rather than deciphering opaque internal libraries.

# Main Points

|   # | Main point |
| --: | ---------- |
|   1 | Capital One uses Python for roughly 40% of its code and 30% of production applications, making it a primary language for enterprise development. |
|   2 | The presentation argues that excessive internal wrappers and SDKs create "spaghetti dependencies" that hinder AI model performance and increase maintenance overhead. |
|   3 | AI models perform best with languages and libraries that have abundant training data, such as Python and popular open-source packages, rather than obscure or internal tools. |
|   4 | Internal SDKs often lack the training data available to LLMs, leading to hallucinations and reduced accuracy compared to using standard open-source libraries. |
|   5 | The speakers recommend replacing heavy internal wrappers with lightweight middleware or extension modules that preserve the context of the underlying open-source library. |
|   6 | Middleware allows for mandatory governance, such as enforcing headers or authentication, without creating opaque black-box dependencies that AI models cannot understand. |
|   7 | Context retention is critical for AI success; teams should document internal dependencies and create dependency graphs to help models understand complex enterprise codebases. |
|   8 | A recursive approach to documenting legacy code involves working from bottom-level dependencies upward, generating markdown documentation to link context for the AI. |
|   9 | Contributing internal improvements back to open-source projects ensures that AI models can learn from the code, reducing the need for custom internal abstractions. |
|  10 | The "virtuous circle" of development involves using AI to generate code, documenting the changes in release notes, and feeding that context back into future AI interactions. |
|  11 | Enforcing middleware usage can be achieved through CI/CD pipeline checks, deprecation warnings, and automated code audits that detect missing or outdated components. |
|  12 | AI models are pattern matchers rather than true reasoners, so they rely heavily on existing documentation and code patterns to generate accurate solutions. |
|  13 | Teams should prioritize writing code that is AI-consumable, ensuring that interfaces and implementations are clear, documented, and aligned with open-source standards. |
|  14 | The distinction between an SDK and middleware is significant; middleware integrates with existing frameworks like FastAPI, while SDKs often create isolated, hard-to-maintain ecosystems. |
|  15 | Developers should use AI to identify and remove deprecated libraries or unnecessary wrappers, leveraging the model's ability to suggest refactoring opportunities. |
|  16 | Effective AI integration requires providing the model with precise, relevant context, avoiding the waste of context windows on explaining internal proprietary structures. |
|  17 | The goal is to maximize AI investment by focusing the model's capabilities on business-specific logic rather than basic infrastructure tasks that open-source libraries already handle. |
|  18 | Organizations should adopt an AI-first development strategy that treats code as ephemeral and intent as enduring, using behavior-driven testing to validate AI-generated solutions. |
|  19 | Collaboration between humans and AI is essential; humans must provide oversight, verify tests, and ensure that AI-generated code meets security and compliance standards. |
|  20 | The presentation concludes that reducing abstraction layers and embracing open-source middleware leads to more maintainable, secure, and AI-friendly enterprise software. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/iRg8fMu_j2w/hqdefault.jpg)](https://www.youtube.com/watch?v=iRg8fMu_j2w)

[Watch on YouTube](https://www.youtube.com/watch?v=iRg8fMu_j2w)
