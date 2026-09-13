---
type: Video Note
title: "Quantum-Resistant Kubernetes: Realities, Risks & (Versioning) Pitfalls - Fabian Kammel, ControlPlane"
description: "Fabian, a principal security consultant at Control Plane, introduces the topic of quantum-resistant Kubernetes, focusing on the risks and pitfalls associated with transitioning to post-quantum cryptography. He explains the basics of quantum..."
resource: https://www.youtube.com/watch?v=3yOwAIpbuQ0
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Fabian, a principal security consultant at Control Plane, introduces the topic of quantum-resistant Kubernetes, focusing on the risks and pitfalls associated with transitioning to post-quantum cryptography.
He explains the basics of quantum computing and its implications for current cryptographic algorithms, highlighting that while symmetric algorithms like AES can be secured by increasing key sizes, asymmetric algorithms such as RSA and ECC are vulnerable to quantum attacks, particularly through Shor’s algorithm.
Fabian outlines the ongoing standardization efforts led by NIST, which have produced new quantum-resistant algorithms, notably ML-KEM for key exchange and several signature schemes, though the latter still face challenges with key and signature sizes and performance.
He discusses the practical impacts of adopting these algorithms, such as version mismatches in Kubernetes and increased data transmission during TLS handshakes, and notes that while key exchange mechanisms are ready for deployment, post-quantum signatures require further research and optimization.
Fabian concludes by emphasizing the importance of staying informed, synchronizing software versions during migration, and preparing organizations for a transition by 2030–2035, as well as sharing resources for continued learning on post-quantum cryptography.
# Main Points

|   # | Main point                                                                                                                                               |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation covers quantum-resistant Kubernetes, focusing on risks and versioning pitfalls.                                                             |
|   2 | Fabian is a principal security consultant at Control Plane, with experience in Kubernetes and container security.                                        |
|   3 | Control Plane is a security consultancy specializing in postquantum crypto and Kubernetes.                                                               |
|   4 | Quantum computers use superposition, inference, and entanglement, excelling at simulating nature and breaking current cryptography via Shor’s algorithm. |
|   5 | Shor’s algorithm can break RSA and ECC, threatening internet security.                                                                                   |
|   6 | Grover’s algorithm speeds up brute-force attacks on symmetric cryptography but only requires doubling key sizes for equivalent security.                 |
|   7 | For symmetric cryptography (e.g., AES), doubling key sizes (e.g., AES-256) maintains security against quantum attacks.                                   |
|   8 | NSA recommends aligning cryptographic strengths; ML-KEM (MLCM) is the new default for key exchange, with security similar to AES-192.                    |
|   9 | NIST began standardizing postquantum algorithms in 2016; four winners were announced in 2023, mainly using lattice-based math.                           |
|  10 | ML-KEM is the new key exchange mechanism, replacing Diffie-Hellman; key sizes are larger (1.5 KB), causing some compatibility issues.                    |
|  11 | Hybrid schemes combine current and postquantum algorithms for added security.                                                                            |
|  12 | Go language quickly adopted hybrid schemes; version mismatches between Go 1.23 and 1.24 can revert to classic cryptography.                              |
|  13 | Kubernetes versions built on different Go versions can cause quantum security issues if not upgraded together.                                           |
|  14 | Browsers (Chrome, Firefox), OpenSSL, and OpenSSH have adopted hybrid postquantum schemes; Rust support is limited.                                       |
|  15 | Postquantum signatures face challenges: large keys, large signatures, slow operations, and multiplied costs in certificate chains.                       |
|  16 | No postquantum signature support in Go yet; Cloudflare Go and Circle library offer experimental support.                                                 |
|  17 | TLS handshakes with postquantum signatures can require up to 40 KB of data, compared to 600 bytes today.                                                 |
|  18 | Postquantum crypto tra                                                                                                                                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=3yOwAIpbuQ0)