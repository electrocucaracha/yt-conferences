---
layout: default
title: Accelerating Bioinformatics AI use cases with Kubernetes
nav_order: 111
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Alexander Potti, a veteran IT professional with over 30 years of experience in OpenStack and Kubernetes but no prior background in biology or AI, shares his journey of transitioning into bioinforma..."
resource: "https://www.youtube.com/watch?v=v4tQ99khk8Q"
youtube_stats:
  view_count: 54
  channel_subscriber_count: 46800
tags:
  - openinfra-summit-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T23:38:50+00:00
---

# Summary

Alexander Potti, a veteran IT professional with over 30 years of experience in OpenStack and Kubernetes but no prior background in biology or AI, shares his journey of transitioning into bioinformatics to apply machine learning to biological problems.
He explains that unlike horizontal technologies like Kubernetes, AI requires vertical specialization, prompting him to pursue a Master of Research in bioinformatics at UCL to understand the domain-specific data.
The core of his presentation focuses on using transformer-based protein language models to solve two specific antibody-related problems: predicting antigen binding specificity and identifying paratope positions, which he frames as binary and token classification tasks, respectively.
To manage the complexity of these workflows, which involve hundreds of automated tasks, he built a robust pipeline using Apache Airflow and Kubernetes, leveraging GPU sharing techniques like MIG and DeepSpeed to optimize resource utilization across H100 GPUs.
Potti emphasizes the critical importance of preventing data leakage through rigorous dataset clustering and separation, demonstrating how his automated system processes data, fine-tunes models, and generates statistical reports to validate that the AI effectively identifies biologically relevant regions such as CDRs.

# Main Points

|   # | Main point                                                                                                                                                                                                   |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | The speaker, Alexander Potti, transitioned from a 30-year career in IT infrastructure to bioinformatics to address AI challenges that require vertical specialization rather than horizontal generalization. |
|   2 | He completed a Master of Research in bioinformatics at UCL to gain the necessary domain knowledge for applying AI to biological data.                                                                        |
|   3 | DNA is described as source code with an alphabet of four bases, while mRNA acts as an intermediate language similar to bytecode, and proteins are the executable outputs.                                    |
|   4 | The biological translation process involves RNA polymerase acting as a compiler and ribosomes as machines that translate codons into amino acids using a nearly universal instruction table.                 |
|   5 | Antibodies are Y-shaped proteins composed of heavy and light chains, with the variable regions responsible for binding specific antigens.                                                                    |
|   6 | The project utilizes transformer-based architectures, specifically protein language models (PLMs) and antibody language models (ALMs), to solve biological classification problems.                          |
|   7 | Two main problems were addressed: assessing antigen specificity as a binary classification task and predicting paratope positions as a token classification task.                                            |
|   8 | Data leakage is a critical risk in AI model evaluation, requiring strict separation of training and testing data, often achieved by clustering data by donor to prevent contamination.                       |
|   9 | The workflow consists of approximately 600 tasks automated using Apache Airflow to manage complex pipelines for data preparation, fine-tuning, and prediction.                                               |
|  10 | Kubernetes was selected as the orchestration platform for running these workloads, offering flexibility for managing both VMs and containers in a multi-tenant environment.                                  |
|  11 | GPU sharing strategies were compared, including MIG for hardware-level isolation, time slicing for high performance in single-user scenarios, and MPS as an experimental middle ground.                      |
|  12 | DeepSpeed was employed to optimize model training by splitting large models across multiple GPUs, enabling the handling of models with up to 15 billion parameters.                                          |
|  13 | The infrastructure supports multiple execution environments, including Slurm and SGE, through a wrapper that allows the same pipeline to run on different scheduling systems.                                |
|  14 | Performance results are generated using R for statistical analysis, with attention weights used to visualize model focus on specific antibody regions like CDRs.                                             |
|  15 | The final output includes automated reports and emails containing performance matrices and attention comparisons, demonstrating the model's ability to identify binding sites.                               |

# Video

[![Video thumbnail](https://img.youtube.com/vi/v4tQ99khk8Q/hqdefault.jpg)](https://www.youtube.com/watch?v=v4tQ99khk8Q)

[Watch on YouTube](https://www.youtube.com/watch?v=v4tQ99khk8Q)
