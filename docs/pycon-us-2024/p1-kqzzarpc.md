---
layout: default
title: "Keynote Speaker - Simon Willison"
nav_order: 118
parent: PyCon US 2024
type: Video Note
description: 'At PyCon US, Simon Willison delivered a keynote exploring the practical applications and limitations of Large Language Models (LLMs), arguing that they function as "Imitation Intelligence" rather t...'
resource: "https://www.youtube.com/watch?v=P1-KQZZarpc"
youtube_stats:
  view_count: 17507
  like_count: 477
  channel_subscriber_count: 34500
tags:
  - pycon-us-2024
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T10:18:11+00:00
---

# Summary

At PyCon US, Simon Willison delivered a keynote exploring the practical applications and limitations of Large Language Models (LLMs), arguing that they function as "Imitation Intelligence" rather than true artificial intelligence.
He demonstrated how LLMs can be harnessed for productive tasks through techniques like Retrieval Augmented Generation (RAG) and function calling, showcasing real-world examples such as building a live speech-recognition counter and extracting structured data from unstructured text for journalism.
Willison emphasized the critical security challenge of prompt injection, warning that mixing untrusted data with tool access creates significant vulnerabilities that currently lack robust solutions.
He also addressed the ethical implications of AI, urging developers to avoid publishing low-quality "slop," to never commit code they cannot explain, and to use these tools to enhance human capabilities rather than replace critical thinking.
Ultimately, he expressed optimism that LLMs will democratize programming by lowering the barrier to entry, allowing a wider audience to automate tasks and build software without requiring a traditional computer science degree.

# Main Points

|   # | Main point                                                                                                                                                                                                                                                |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The term artificial intelligence was coined in 1956 by John McCarthy and colleagues, who optimistically predicted significant advances in machine language and problem-solving within a single summer.                                                    |
|   2 | Large language models are better described as imitation intelligence because they function as statistical autocomplete systems that predict the next word based on vast training data rather than possessing true understanding or planning capabilities. |
|   3 | Training data for models like Llama 1 includes web crawls, GitHub, Wikipedia, and pirated ebooks, totaling approximately 4.5 terabytes, which is substantial but not unfathomably large compared to modern storage capacities.                            |
|   4 | Evaluating model performance often relies on subjective "vibes" and community voting systems like the LMSys Arena, which ranks models based on user preference for responses to various prompts.                                                          |
|   5 | Openly licensed models such as Llama 3 and Mistral are increasingly competitive with proprietary systems, allowing developers to run high-quality AI on local hardware and reducing dependence on large vendors.                                          |
|   6 | Mobile devices can now run local language models, as demonstrated by the MLC Chat app on iPhones, enabling offline tasks like code generation without an internet connection.                                                                             |
|   7 | Prompt engineering involves building software around models using specific tricks, including treating chat interactions as screenplay completion tasks where the model fills in the assistant's response.                                                 |
|   8 | Retrieval augmented generation allows models to answer questions about private or new data by searching external sources and pasting the results into the prompt, eliminating the need for expensive retraining.                                          |
|   9 | Function calling enables models to use external tools like calculators or search engines by interpreting tool calls in their output, allowing them to perform arithmetic and look up information they cannot process internally.                          |
|  10 | Prompt injection is a critical security vulnerability where untrusted text mixed with instructions can manipulate the model into performing malicious actions, such as forwarding private emails to attackers.                                            |
|  11 | There is currently no robust solution to prevent prompt injection, making it difficult to securely build personal digital assistants that have access to sensitive user data and tools.                                                                   |
|  12 | ChatGPT's code interpreter allows users to upload files and iterate on code generation, enabling rapid prototyping of complex tasks like converting GeoJSON data into polygons in minutes.                                                                |
|  13 | Using AI to build a live speech recognition counter for the word "AI" took only six minutes to prototype, demonstrating how these tools enable quick creation of side projects that would otherwise be too time-consuming.                                |
|  14 | Datasette integrates LLM features to extract structured data from unstructured text, such as converting PSF board resolutions into a filterable database, which speeds up data journalism workflows.                                                      |
|  15 | The speaker prefers the term "transformative AI" over "generative AI" to emphasize the utility of processing and evaluating large amounts of text rather than just generating content.                                                                    |
|  16 | Ethical guidelines for using AI include avoiding the publication of "slop" (unwanted AI-generated content) and ensuring that any code generated by AI is fully understood and explainable by the developer.                                               |
|  17 | Language models are particularly effective at generating code because programming languages have simpler grammar rules than human languages and allow for immediate fact-checking through execution.                                                      |
|  18 | The Python community is well-positioned to leverage these tools to lower the barrier to entry for programming, enabling non-experts to automate tasks and learn coding through natural language interfaces.                                               |

# Video

[![Video thumbnail](https://img.youtube.com/vi/P1-KQZZarpc/hqdefault.jpg)](https://www.youtube.com/watch?v=P1-KQZZarpc)

[Watch on YouTube](https://www.youtube.com/watch?v=P1-KQZZarpc)
