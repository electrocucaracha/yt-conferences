---
layout: default
title: "Build, Deploy, Monetize: The Future of the Developer Economy (Sponsor : Apify)"
nav_order: 123
parent: PyCon US 2026
type: Video Note
description: "Saurabh and Jacob from Apify present a solution to the common challenges developers face when trying to monetize software, identifying infrastructure management, marketing, user authentication, and..."
resource: "https://www.youtube.com/watch?v=9VctQkHzU-Y"
youtube_stats:
  view_count: 417
  like_count: 2
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

Saurabh and Jacob from Apify present a solution to the common challenges developers face when trying to monetize software, identifying infrastructure management, marketing, user authentication, and billing as primary barriers.
They introduce Apify as a "code in, cash out" platform where developers can convert existing software into "Actors"—serverless cloud programs that take input, process it, and produce output—using a standardized structure defined by input and output schemas.
The presentation highlights the benefits of publishing on the Apify Store, which offers access to over 300,000 monthly sign-ups, built-in SEO advantages through dedicated landing pages, and a simplified monetization model using the `actor.charge` method to bill users for specific events without managing complex invoicing systems.
A live demo by Jacob showcases the practical application of these concepts, utilizing the Apify CLI to create a TypeScript-based scraper for UTMB running rankings, pushing it to the platform, and integrating it with AI tools via the Apify MCP to retrieve real-time data.
The session concludes with a Q&A addressing platform fees, resource configuration, and the growing role of LLMs in discovering and utilizing Apify actors for diverse tasks beyond simple web scraping.

# Main Points

|   # | Main point                                                                                                                                                                                                              |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The talk addresses the difficulty developers face in turning software into profitable products due to infrastructure management, marketing challenges, user authentication complexity, and billing system requirements. |
|   2 | Apify is presented as a platform that simplifies these barriers by allowing developers to focus on code while handling deployment, marketing, and monetization.                                                         |
|   3 | Apify actors are defined as serverless cloud programs that take input, process it, and produce output, similar to how human actors perform actions based on a script.                                                   |
|   4 | The actorization process involves creating a .actor folder with mandatory files like actor.json and Dockerfile, along with optional but recommended input and output schemas and a readme.                              |
|   5 | Existing open-source projects like Docling and Sherlock have successfully converted their repositories into Apify actors, making them accessible to non-coders via the Apify store.                                     |
|   6 | Developers can create actors using the Apify CLI, ready-made templates, or AI-assisted tools like Apify agent skills and Claude Code integrations.                                                                      |
|   7 | The Apify Store offers an unfair advantage for developers by providing access to over 300,000 new sign-ups monthly and 50,000 monthly active paying customers who are actively seeking solutions.                       |
|   8 | Publishing an actor on Apify generates a dedicated landing page under the Apify domain, which benefits from the platform's strong SEO to improve discoverability via search engines.                                    |
|   9 | Monetization is achieved through the actor.charge method, which allows developers to assign prices to specific events or items within their software, such as per-result charges.                                       |
|  10 | Apify handles payment collection, invoicing, and payouts to developers, who receive funds in the first week of the following month via bank transfer or PayPal.                                                         |
|  11 | The platform supports agentic payments experimentally through the X402 protocol, preparing for a future where AI agents directly pay for software services.                                                             |
|  12 | A live demo demonstrated creating a UTMB race scraper using the Apify CLI, pushing it to the platform, and running it to generate tabular data accessible via API.                                                      |
|  13 | The Apify MCP (Model Context Protocol) integration allows LLMs to discover and execute actors, providing real-time data to prevent hallucinations and enable complex workflows.                                         |
|  14 | Apify takes a 20% fee from developer earnings, with the remaining 80% going to the developer, and ensures that developers do not incur negative profits from platform resource usage.                                   |
|  15 | Actor quality scores, rated out of 100, influence ranking and visibility in the marketplace, with scores above 60 considered good for better placement.                                                                 |
|  16 | Developers can configure resource allocation such as CPU and RAM for their actors, which impacts pricing, and Apify protects developers from losses caused by platform resource consumption.                            |

# Video

[![Video thumbnail](https://img.youtube.com/vi/9VctQkHzU-Y/hqdefault.jpg)](https://www.youtube.com/watch?v=9VctQkHzU-Y)

[Watch on YouTube](https://www.youtube.com/watch?v=9VctQkHzU-Y)
