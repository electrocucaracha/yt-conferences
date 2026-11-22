---
layout: default
title: "Talks - Naveed Mahmud: Hybrid Quantum-Classical Machine Learning using Qiskit"
nav_order: 153
parent: PyCon US 2024
type: Video Note
description: "Navid Mahmud, an assistant professor at Florida Institute of Technology, presented his research on quantum-classical machine learning using the open-source KKit SDK."
resource: "https://www.youtube.com/watch?v=03Yf4KDMVAo"
youtube_stats:
  view_count: 564
  like_count: 16
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

Navid Mahmud, an assistant professor at Florida Institute of Technology, presented his research on quantum-classical machine learning using the open-source KKit SDK.
The talk introduced fundamental quantum concepts such as qubits, superposition, and entanglement, explaining how these properties enable faster convergence for specific operations compared to classical deterministic computing.
Mahmud detailed a proposed framework for sentiment analysis that processes English and Bengali text datasets by combining classical preprocessing techniques, such as PCA and Haar wavelet transforms, with quantum models like the Quantum Support Vector Classifier and Variational Quantum Classifier.
Experimental results demonstrated that these hybrid quantum-classical models achieved test accuracies comparable to purely classical methods, with the Variational Quantum Classifier offering the shortest training time.
Furthermore, the study revealed that applying Haar transform compression significantly degraded classical model accuracy, whereas the quantum models maintained stable performance, suggesting that quantum-classical approaches are more robust for handling compressed large-scale datasets.

# Main Points

|   # | Main point                                                                                                                                                                                          |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Navid Mahmud, an assistant professor at Florida Institute of Technology, presented research on quantum-classical machine learning using the open-source KKit SDK.                                   |
|   2 | The research group focuses on developing efficient quantum algorithms and applications, including verification and benchmarking via GPU and FPGA hardware platforms.                                |
|   3 | Quantum computing offers advantages in specific probabilistic operations like quantum simulation, cryptography, optimization, and machine learning by leveraging superposition and entanglement.    |
|   4 | Fundamental quantum concepts include qubits represented on the Bloch sphere, superposition allowing exponential state spaces, and entanglement creating strong correlations between qubits.         |
|   5 | Key quantum gates used in the models include Hadamard for superposition, CNOT for entanglement, and rotation gates for state manipulation.                                                          |
|   6 | The study applied quantum machine learning to sentiment analysis using English Twitter data and Bengali news portal data.                                                                           |
|   7 | The proposed framework combines classical preprocessing and dimension reduction with quantum classification methods.                                                                                |
|   8 | Classical preprocessing involved text splitting, word embedding using CountVectorizer, and dimension reduction via Principal Component Analysis (PCA) and Haar wavelet transform.                   |
|   9 | The quantum feature map encodes classical data into the quantum domain using a parameterized circuit with poly-rotations and entanglement.                                                          |
|  10 | Two quantum classifiers were implemented: the Quantum Support Vector Classifier (QSVC) using a fidelity-based kernel, and the Variational Quantum Classifier (VQC) using trainable ansatz circuits. |
|  11 | Experimental results showed that quantum models achieved test accuracies of approximately 70-72%, comparable to purely classical SVM implementations.                                               |
|  12 | The Variational Quantum Classifier demonstrated the shortest training time among the tested quantum implementations.                                                                                |
|  13 | When combining Haar wavelet compression with quantum models, test accuracy remained stable around 71% even as data points were significantly reduced.                                               |
|  14 | In contrast, classical model accuracy dropped sharply from 85% to 29% under the same high-level Haar compression conditions.                                                                        |
|  15 | The research indicates that quantum-classical methods are more robust to data compression than purely classical methods, suggesting potential for handling large datasets.                          |
|  16 | The experiments were conducted at the simulation level using KKit version 1.0.2, with future plans to migrate to newer APIs for quantum hardware execution.                                         |
|  17 | The framework is applicable to circuit-based quantum computers, such as superconducting and ion-trap systems, but not necessarily to topological quantum computers.                                 |

# Video

[![Video thumbnail](https://img.youtube.com/vi/03Yf4KDMVAo/hqdefault.jpg)](https://www.youtube.com/watch?v=03Yf4KDMVAo)

[Watch on YouTube](https://www.youtube.com/watch?v=03Yf4KDMVAo)
