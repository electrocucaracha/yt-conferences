---
type: Video Note
title: "From Laptop to Cluster: Running AI Workloads Seamlessly from Podman... Ashley Cui & Urvashi Mohnani"
description: "In this talk, Roishi Manani and Ashley from Red Hat discuss how to seamlessly run AI workloads from a laptop to a Kubernetes cluster using container technologies. They outline the recent evolution of AI, from the rise of chatbots like ChatG..."
resource: https://www.youtube.com/watch?v=6DkdGa2G7W0
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Roishi Manani and Ashley from Red Hat discuss how to seamlessly run AI workloads from a laptop to a Kubernetes cluster using container technologies.
They outline the recent evolution of AI, from the rise of chatbots like ChatGPT to the current trend of agentic AI, which can autonomously execute tasks.
To address the challenges of securely and easily deploying custom-tuned AI models, they introduce tools such as Ramal Lama, which packages AI models as OCI artifacts for easy sharing and deployment, and Podman, a rootless container engine that emphasizes security and can run both locally and in production.
Through a live demo, they show how to use Ramal Lama and Podman to containerize an LLM and an agentic AI, run them together in a pod, and then migrate the workload to Kubernetes by converting the model into a suitable image and generating the necessary YAML configuration.
They also demonstrate how Quadlet can be used to manage these containers as systemd services for edge or single-node environments, highlighting the flexibility and reusability of container-based workflows for AI applications.
# Main Points

|   # | Main point                                                                                                                                                       |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Speakers: Roishi Manani (Principal Software Engineer, Red Hat, container technologies/OpenShift) and Ashley (Software Engineer, Red Hat, container tools/Podman) |
|   2 | Talk topic: Seamless AI workload deployment from laptop to cluster, using Podman and Kubernetes                                                                  |
|   3 | AI timeline:                                                                                                                                                     |
|   4 | 2022: ChatGPT released, sparking AI interest                                                                                                                     |
|   5 | 2023: AI race with Llama, Claude, Gemini entering the scene                                                                                                      |
|   6 | 2024: Industry-wide AI adoption and integration                                                                                                                  |
|   7 | 2025: Shift toward agentic AI (AIs that execute tasks, not just chatbots)                                                                                        |
|   8 | Agentic AI: Moves from chatbot Q&A to AIs performing actions; increases risk and need for secure deployment                                                      |
|   9 | Custom-tuned LLMs: Growing need to share and deploy proprietary, fine-tuned models securely                                                                      |
|  10 | Key tools introduced:                                                                                                                                            |
|  11 | **Ramal Lama**:                                                                                                                                                  |
|  12 | Simplifies AI model management using familiar container commands                                                                                                 |
|  13 | Pulls AI models as OCI artifacts                                                                                                                                 |
|  14 | Enables sharing, fine-tuning, and running LLMs in container environments                                                                                         |
|  15 | Supports GPU discovery and usage                                                                                                                                 |
|  16 | **Podman**:                                                                                                                                                      |
|  17 | Rootless, daemonless, multiplatform container manager                                                                                                            |
|  18 | Emphasizes security; runs containers and pods locally                                                                                                            |
|  19 | Used by Ramal Lama to run containerized LLMs                                                                                                                     |
|  20 | Supports running agentic AI in isolated containers/pods                                                                                                          |
|  21 | CNCF sandbox project since 2024                                                                                                                                  |
|  22 | Bridges local development to Kubernetes                                                                                                                          |
|  23 | **Quadlet**:                                                                                                                                                     |
|  24 | Runs containers as systemd services for automatic start, updates, and restarts                                                                                   |
|  25 | Uses Kubernetes YAML for configuration                                                                                                                           |
|  26 | Demo workflow:                                                                                                                                                   |
|  27 | Use Ramal Lama to pull and prepare LLM as OCI artifact or car image                                                                                              |
|  28 | Run LLM and agentic AI (Goose) in Podman pods locally                                                                                                            |
|  29 | Generate Kubernetes YAML with `podman generate kube`                                                                                                             |
|  30 | Deploy to Kubernetes (e.g., Minikube), with necessary YAML tweaks                                                                                                |
|  31 | Use Quadlet for single-node/edge deployments as systemd services                                                                                                 |
|  32 | Same Kubernetes YAML can be used across Podman, Kubernetes, and Quadlet deployments                                                                              |
|  33 | Resources and demo scripts provided at end                                                                                                                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=6DkdGa2G7W0)