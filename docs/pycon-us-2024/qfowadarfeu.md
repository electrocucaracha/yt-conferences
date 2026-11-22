---
layout: default
title: "Talks - Alynne Ferreira: Graphs and Vogue Dance: using data structures to create choreographies"
nav_order: 178
parent: PyCon US 2024
type: Video Note
description: "Alena, a Brazilian computer engineer and dancer, presents a talk on using graph data structures to create choreographies for the VOG dance style."
resource: "https://www.youtube.com/watch?v=QfOWAdarfEU"
youtube_stats:
  view_count: 158
  like_count: 3
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

Alena, a Brazilian computer engineer and dancer, presents a talk on using graph data structures to create choreographies for the VOG dance style.
She explains the historical context of VOG, highlighting its origins in New York as a form of expression and community for Black and LGBTQ+ individuals excluded from mainstream beauty pageants.
The presentation covers fundamental graph concepts, including connected, complete, and directed graphs, as well as binary trees, using Python libraries like NetworkX and Matplotlib for visualization.
To solve the specific problem of mapping dance poses into a coherent sequence, Alena introduces deterministic finite automata (DFA) to model transitions between states, effectively treating dance moves as input symbols that determine the flow of the choreography.
In the Q&A session, she acknowledges the potential for integrating machine learning for pose detection and expresses interest in exploring automated pose recognition and multi-person choreography in future work.

# Main Points

|   # | Main point                                                                                                                                                                     |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | The speaker, Alena, is a Brazilian computer engineer, backend developer, and dancer who chose voguing to illustrate graph concepts.                                            |
|   2 | Voguing originated in New York in the 1970s and 1980s as a response to exclusion in beauty pageants, creating a supportive community known as "houses" for LGBTQ+ individuals. |
|   3 | A graph is defined as an abstract representation of objects and relationships, consisting of vertices, edges, and functions associating edges with vertex pairs.               |
|   4 | The presentation uses Python libraries Matplotlib and NetworkX to visualize various graph types, including trivial, connected, disconnected, complete, and incomplete graphs.  |
|   5 | A trivial graph contains a single node without edges, while a connected graph allows traversal from any node to any other node via edges.                                      |
|   6 | A complete graph requires every node to have the maximum possible degree, meaning it is connected to all other nodes.                                                          |
|   7 | Directed graphs are used when the direction of relationships is important, such as in city traffic patterns, and are visualized using arrow-style edges.                       |
|   8 | Binary trees are a specific type of tree structure with a root and leaves, where each node has at most two children, similar to the logic used in the "20 Questions" game.     |
|   9 | The speaker mapped dance poses to graph nodes using images loaded via PIL, allowing for the visualization of possible transitions between poses.                               |
|  10 | Finite Automata, specifically Deterministic Finite Automata (DFA), were introduced as a solution to model choreography sequences with defined start and end states.            |
|  11 | A DFA is a directed graph with input symbols that accepts or rejects strings of symbols based on transitions between states.                                                   |
|  12 | The speaker implemented a custom DFA using the visualDFA library to represent dance moves as states and transitions, demonstrating accepted and rejected sequences.            |
|  13 | The application of automata allows for the validation of choreography paths, ensuring that a sequence of moves starts and ends at designated states.                           |
|  14 | Audience questions suggested integrating machine learning for pose detection to automatically monitor and validate dance movements against the graph model.                    |
|  15 | The speaker expressed interest in future developments, including automatic pose extraction and organizing multiple dancers as nodes in a graph for complex choreographies.     |
|  16 | References included a GitHub repository with the code, the film "Paris Is Burning," and the series "Pose" for further context on voguing culture.                              |

# Video

[![Video thumbnail](https://img.youtube.com/vi/QfOWAdarfEU/hqdefault.jpg)](https://www.youtube.com/watch?v=QfOWAdarfEU)

[Watch on YouTube](https://www.youtube.com/watch?v=QfOWAdarfEU)
