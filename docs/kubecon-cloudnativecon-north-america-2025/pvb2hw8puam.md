---
type: Video Note
title: "Simplifying Advanced AI Model Serving on Kubernetes Using Helm... Ajay Vohra & Tianlu Caron Zhang"
description: "In this session, Karen John from Apple and AJ Vora from AWS discuss the complexities of serving advanced AI models on Kubernetes and present a solution using Helm charts. They outline the typical AI model serving stack, highlighting challen..."
resource: https://www.youtube.com/watch?v=PVB2hW8PuAM
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this session, Karen John from Apple and AJ Vora from AWS discuss the complexities of serving advanced AI models on Kubernetes and present a solution using Helm charts.
They outline the typical AI model serving stack, highlighting challenges such as managing diverse configurations for different inference servers, backends, and models, especially as model sizes and context lengths increase, necessitating multi-node setups.
The speakers explain that embedding configurations in container images hampers rapid development, while externalizing them reduces reproducibility, and propose using declarative packaging with Helm charts to templatize and version configurations efficiently.
They demonstrate how Helm charts, combined with Kubernetes APIs like deployments, leader-worker sets, and Ray service APIs, can flexibly support both single-node and multi-node inference scenarios, enabling rapid experimentation and reproducibility.
The session concludes with a demo showing how AI can help generate Helm values for new models, and a Q&A addressing choices around Helm versus custom operators, scaling mechanisms, and the open-ended nature of their templating approach.
# Main Points

|   # | Main point                                                                                                                                                                                       |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Karen John (Apple) and AJ Vora (AWS) presented on simplifying advanced AI model serving on Kubernetes using Helmcharts.                                                                          |
|   2 | Serving diverse AI models (LLMs, multimodal, stable diffusion, etc.) on Kubernetes is challenging.                                                                                               |
|   3 | The talk covers common challenges, proposes a solution, and includes a demo and GitHub QR code.                                                                                                  |
|   4 | Typical AI model serving stack on Kubernetes has three layers: hardware clusters, deployment orchestration workflows, and inference servers/backends/models/frameworks.                          |
|   5 | Focus is on efficiently managing and deploying diverse AI/ML frameworks in Kubernetes, especially the inference stack.                                                                           |
|   6 | Inference stack components: service pod (inference server, backend, model), AI/ML frameworks (e.g., PyTorch, TensorFlow), runtime (e.g., CUDA), and collective communication (e.g., all-reduce). |
|   7 | Kubernetes constructs: daemon sets, device drivers, network drivers.                                                                                                                             |
|   8 | Model serving setups range from single GPU to multi-node, multi-GPU (tensor and pipeline parallelism).                                                                                           |
|   9 | Example: Serving DeepSeek R1 (671B parameters) may require multi-node, multi-GPU setup for large models and context windows.                                                                     |
|  10 | Compatibility matrix between runtime and device driver (e.g., CUDA version) is crucial.                                                                                                          |
|  11 | Open-source/vendor container images help, but configuration diversity (server, backend, model) is a core challenge.                                                                              |
|  12 | Embedding configs in images slows development; externalizing configs breaks reproducibility.                                                                                                     |
|  13 | Solution: Use declarative packaging tool (Helmcharts) to templatize configs, enabling rapid iteration and reproducibility.                                                                       |
|  14 | Kubernetes API objects for inference: deployment, horizontal pod scaler, config map, service, persistent volume claim, leader worker set, Ray service API.                                       |
|  15 | Helmcharts allow packaging, versioning, and templatization of Kubernetes API objects and configs.                                                                                                |
|  16 | Less than five Helmcharts can cover most inference scenarios; only Helm values need to be supplied.                                                                                              |
|  17 | Demo: Using AI to generate Helm values for new models, running a Jupyter notebook to deploy, and leve                                                                                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=PVB2hW8PuAM)