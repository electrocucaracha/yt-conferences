---
layout: default
title: "NLP para la preservación del lenguaje indígena Quechua - Carla Marcela Florida Román"
nav_order: 15
parent: PyCon US 2025
type: Video Note
description: "Carla, an AI engineer and educator, presented a project aimed at preserving the Quechua language in Bolivia by leveraging Retrieval-Augmented Generation (RAG) technology."
resource: "https://www.youtube.com/watch?v=rE5Ct1vVYPQ"
youtube_stats:
  view_count: 409
  like_count: 5
  channel_subscriber_count: 34500
tags:
  - pycon-us-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T01:39:37+00:00
---

# Summary

Carla, an AI engineer and educator, presented a project aimed at preserving the Quechua language in Bolivia by leveraging Retrieval-Augmented Generation (RAG) technology.
She explained that Quechua is a vital but endangered indigenous language with a distinct grammatical structure, such as subject-object-verb order, and is deeply embedded in Bolivian culture through common words like "papa" and "choclo." To address the scarcity of digital resources, she built a workflow using the no-code platform N8N to vectorize four PDF books written by Bolivian authors, creating a specialized knowledge base.
This system utilizes Google Gemini’s free LLM to process user queries via a webhook, retrieving specific contextual information from the vector store rather than relying on general translation models that often struggle with Quechua’s nuances.
The project was deployed with a Streamlit interface to allow users to interact with the bot, demonstrating how accessible AI tools can help preserve indigenous languages and bridge the digital divide for native speakers.

# Main Points

|   # | Main point                                                                                                                                      |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Carla is an AI researcher at the Universidad Privada Boliviana, an AI Engineer at NBITS, a professor at Platzi, and co-founder of Ment Academy. |
|   2 | She is an ambassador for Woman Tech Maker and creates content on TikTok and Instagram through her community Carly Code to teach Python and AI.  |
|   3 | The presentation focuses on using a RAG system to help learn the Quechua language, which is at risk of disappearing in Bolivia.                 |
|   4 | Quechua is one of three main languages in Bolivia, alongside Aymara and Guaraní, with approximately 2.8 million speakers.                       |
|   5 | The language is transmitted orally within families, and many Bolivians understand it even if they do not speak it fluently.                     |
|   6 | Common Spanish words in Bolivia, such as papa, chompa, carpa, choclo, quinoa, and yapa, originate from Quechua.                                 |
|   7 | Quechua grammar differs from Spanish, using a Subject-Object-Verb structure and specific suffixes for conjugation.                              |
|   8 | In Bolivia, schools are legally required to teach one of the native languages, and medical students must learn them to serve rural communities. |
|   9 | The RAG system was built using N8N, a no-code workflow automation tool, to facilitate the creation of AI agents.                                |
|  10 | The system utilizes four PDF books by Bolivian authors as the knowledge base, which were vectorized for semantic search.                        |
|  11 | Google Gemini was selected as the Large Language Model to process queries and generate responses based on the vector store.                     |
|  12 | A webhook in N8N receives JSON input, processes it through the agent with memory, and returns the response.                                     |
|  13 | Streamlit was used to create a simple user interface for the chatbot, allowing users to interact with the bot easily.                           |
|  14 | The bot provides explanations and translations based on the specific Bolivian dialect of Quechua found in the source books.                     |
|  15 | Challenges include the lack of standardized digital resources and the existence of different dialects across countries like Peru and Bolivia.   |
|  16 | Potential solutions for expanding data include converting multimedia content from native speakers into text for model training.                 |
|  17 | RAG is preferred over fine-tuning for this project because it retrieves direct information from sources without requiring structured datasets.  |
|  18 | There is a digital divide, as many native Quechua speakers do not use mobile phones, limiting their direct access to digital tools.             |
|  19 | Existing solutions like university bots and real-time translators exist but are often unpublished or inaccessible to the target demographic.    |
|  20 | The project aims to preserve cultural heritage and support the survival of indigenous languages through accessible AI technology.               |

# Video

[![Video thumbnail](https://img.youtube.com/vi/rE5Ct1vVYPQ/hqdefault.jpg)](https://www.youtube.com/watch?v=rE5Ct1vVYPQ)

[Watch on YouTube](https://www.youtube.com/watch?v=rE5Ct1vVYPQ)
