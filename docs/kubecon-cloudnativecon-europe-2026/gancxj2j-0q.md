---
type: Video Note
title: "Why Security of Kubernetes Comes Down to Linux Security - Marina Moore, Edera"
description: "Marina, head of research at ADA and co-chair of CNCF’s security group, presents on Kubernetes security, emphasizing that it fundamentally relies on Linux security due to containers sharing a single kernel. She traces the evolution of contai..."
resource: https://www.youtube.com/watch?v=gaNCXj2j-0Q
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Marina, head of research at ADA and co-chair of CNCF’s security group, presents on Kubernetes security, emphasizing that it fundamentally relies on Linux security due to containers sharing a single kernel.
She traces the evolution of container technology from early concepts like chroot and FreeBSD jails, through Solaris containers and Open Virtuoso, to modern Linux containers that use namespaces and cgroups for process isolation and resource control.
However, she stresses that these mechanisms were designed for resource management, not as strict security boundaries, which is why container escapes—where processes break out of their isolated environments—remain a real risk, as demonstrated by several recent vulnerabilities.
Through a live demo, Marina illustrates how containers can access information about the host system, reinforcing the point that the underlying kernel is always present and influential.
She concludes by discussing emerging technologies aimed at stronger isolation, such as microVMs and WebAssembly, and highlights the importance of understanding Linux internals for both security and performance, especially as new use cases like AI agent sandboxing demand robust containment strategies.
# Main Points

|   # | Main point                                                                                                                                                    |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Marina, head of research at ADA and CNCF TAG Security & Compliance co-chair, presents on Kubernetes security as Linux security.                               |
|   2 | Containers run on a shared kernel; mechanisms like namespaces and cgroups provide isolation but not true security boundaries.                                 |
|   3 | Container escape occurs when isolation fails, allowing unauthorized operations on the host, such as code execution, privilege escalation, and data tampering. |
|   4 | Real-world container escape vulnerabilities include issues in Docker Desktop, NVIDIA container toolkit, runc, and buildkit.                                   |
|   5 | The container boundary was designed for resource control, not security.                                                                                       |
|   6 | Early OS virtualization began with chroot (1979), which isolated file systems but not system calls or network functionality.                                  |
|   7 | FreeBSD jails (1999) provided more complete isolation, partitioning systems into independent environments.                                                    |
|   8 | Solaris containers/zones (2004-2005) combined resource control and boundary separation but lacked privilege modes.                                            |
|   9 | Open Virtuoso allowed multiple OS instances on one server, sharing the Linux kernel.                                                                          |
|  10 | Linux containers (2008) combined cgroups (resource limits) and namespaces (environment isolation), defining modern containers.                                |
|  11 | Docker initially used Linux containers, then switched to libcontainer (2015), which later split into runc and containerd.                                     |
|  12 | Modern containers rely on Linux kernel features: namespaces, cgroups, capabilities, security profiles, and network interfaces.                                |
|  13 | Container security depends on Linux kernel security; kernel vulnerabilities can lead to container escapes.                                                    |
|  14 | Namespaces and cgroups only isolate user space resources; kernel-level access can bypass these protections.                                                   |
|  15 | Demo showed that unprivileged containers can access host system information (CPU, memory, kernel modules, network traffic).                                   |
|  16 | Newer technologies aim for stronger isolation: multi-kernel, sysbox, gVisor, user namespaces, microVMs (kata containers, firecracker), and WebAssembly.       |
|  17 | Understanding Linux kernel internals is crucial for contain                                                                                                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=gaNCXj2j-0Q)