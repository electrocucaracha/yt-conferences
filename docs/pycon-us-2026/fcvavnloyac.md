---
layout: default
title: "When data doesn't speak: Python as an interpreter of... - Joyce Beatriz Ferreira da Costa Silva"
nav_order: 127
parent: PyCon US 2026
type: Video Note
description: "Joice, a Brazilian software engineering student and GDG organizer, presented a project analyzing large-scale biological data to overcome CPU processing bottlenecks by leveraging GPU parallel comput..."
resource: "https://www.youtube.com/watch?v=fCVAvNLoYac"
youtube_stats:
  view_count: 413
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

Joice, a Brazilian software engineering student and GDG organizer, presented a project analyzing large-scale biological data to overcome CPU processing bottlenecks by leveraging GPU parallel computing capabilities.
The study utilized a raw, unlabeled dataset of 400 time instants containing 2,000 populations, applying the DBSCAN clustering algorithm to identify species groups based on density and connectivity rather than predefined quantities.
By using a Tesla T4 GPU via Google Colab, the team normalized the data and executed the clustering process, which allowed for detailed analyses of lineage, extinction patterns, and species resilience that would be significantly slower on a CPU.
The results were validated using quality metrics such as silhouette scores and Calinski-Harabasz indices, confirming the effectiveness of the GPU-accelerated approach for handling complex biological data.
Although the species were not explicitly labeled in the dataset, the methodology successfully tracked individual emergence, survival, and adaptation rates, demonstrating the potential for accelerating scientific research in biological sciences.

# Main Points

|   # | Main point |
| --: | ---------- |
|   1 | The speaker is a software engineering student and GDG organizer working on a health project at their university. |
|   2 | Large-scale biological data processing on CPUs faces bottlenecks due to processing time, prompting the exploration of GPUs. |
|   3 | CPUs are designed for complex logic and serial execution with few powerful cores, ideal for system management and dependent processes. |
|   4 | GPUs are designed for parallel computing with thousands of cores, making them ideal for clustering tasks like DBSCAN. |
|   5 | The CPU is faster for short tasks, while the GPU processes large volumes of data simultaneously. |
|   6 | The research project involved a dataset with 400 time instants and 2,000 populations per instant, provided by the Institute of Biological Sciences. |
|   7 | The raw data contains 12 columns, including features like temperature and population IDs for tracking individuals. |
|   8 | Unsupervised learning with DBSCAN clustering is used to group populations and identify species without labeled data. |
|   9 | DBSCAN is preferred over K-Means because it automatically determines cluster numbers and handles noise in raw, unlabeled data. |
|  10 | Key DBSCAN parameters include epsilon (maximum distance for neighbors, set to 0.3) and minimum samples (minimum density, set to 10). |
|  11 | Data normalization is essential to avoid errors when working with different data types before GPU processing. |
|  12 | The workflow involves loading data, normalizing it, detecting clusters on the GPU, and saving the results for further analysis. |
|  13 | Post-processing analyses include lineage analysis, quality metrics, dimensional visualizations, and extinction patterns. |
|  14 | Lineage analysis tracks mass births, species resilience, new species detection, and genealogical trees. |
|  15 | In one example, 47 species were identified in a specific time frame using data from instant 180. |
|  16 | Analysis can track species emergence and disappearance between periods, such as between instants 80 and 81. |
|  17 | Quality metrics include the silhouette score (0.178, within the -1 to 1 range) and Calinski-Harabasz index. |
|  18 | Dimensional reduction techniques like projection translate 10 dimensions into a 2D map to reveal data structure. |
|  19 | The project used Google Colab with a Tesla T4 GPU (16 GB) to make the process accessible and verify performance. |
|  20 | The primary goal was to analyze extinction and survival processes and compare CPU versus GPU acceleration. |
|  21 | The data is not labeled with specific species names, so individuals are tracked by ID for lineage and adaptation analysis. |
|  22 | The research results were presented at the university and a conference, with positive feedback from the biological sciences institute. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/fCVAvNLoYac/hqdefault.jpg)](https://www.youtube.com/watch?v=fCVAvNLoYac)

[Watch on YouTube](https://www.youtube.com/watch?v=fCVAvNLoYac)
