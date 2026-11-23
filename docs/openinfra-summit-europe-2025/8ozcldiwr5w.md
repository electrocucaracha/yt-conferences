---
layout: default
title: "Hands On: Infrastructure Provision with Terraform or OpenTOFU"
nav_order: 30
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "This transcript documents a Terraform workshop held at the Open Infra Summit, led by N Magnos, a Principal Cloud Architect, and Anton, a Tools Developer at Open Telecom Cloud."
resource: "https://www.youtube.com/watch?v=8ozcLdiwr5w"
youtube_stats:
  view_count: 211
  like_count: 3
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

This transcript documents a Terraform workshop held at the Open Infra Summit, led by N Magnos, a Principal Cloud Architect, and Anton, a Tools Developer at Open Telecom Cloud.
The session introduces Terraform as the industry standard for cloud-agnostic infrastructure provisioning, explaining its advantages over tools like Ansible due to its parallel execution capabilities and stateful nature.
The presenters guide attendees through hands-on demos using Open Telecom Cloud credentials, covering fundamental concepts such as provider configuration, resource creation, variable management, and the use of data sources.
They also explore advanced topics, including the integration of Terraform with Ansible via provisioners, the use of modules for code reusability, and alternative tools like OpenTofu and Pulumi.
The workshop addresses practical challenges such as configuration drift, state locking, and the licensing differences between Terraform and OpenTofu, while emphasizing best practices for team collaboration using tools like Atlantis.
The session concludes with a Q&A segment where attendees discuss migration strategies from other management tools and methods for maintaining infrastructure consistency, with the presenters offering advice on using import features and restricting direct access to prevent unauthorized changes.

# Main Points

|   # | Main point                                                                                                                                                   |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | The workshop focuses on system provisioning using Terraform, which is considered the industry standard for cloud-independent automation.                     |
|   2 | Attendees are provided with live demo credentials via a shared spreadsheet to practice on Open Telecom Cloud domains.                                        |
|   3 | The recommended network for the session is the guest network due to poor signal strength on the official Open Infra network.                                 |
|   4 | The presenters are a Principal Cloud Architect and a Tools Developer from Open Telecom Cloud, the latter responsible for maintaining the Terraform provider. |
|   5 | Terraform is preferred over Ansible for provisioning because it operates in parallel, is faster, and avoids version compatibility issues during OS updates.  |
|   6 | HashiCorp changed Terraform's license to BSL, making it no longer strictly open source, which has led to the adoption of OpenTofu as an alternative.         |
|   7 | OpenTofu is functionally nearly identical to Terraform but remains under an open-source license and offers better S3 backend support.                        |
|   8 | The Open Telecom Cloud provider is a fork of the OpenStack provider, extended to support additional services not available in vanilla OpenStack.             |
|   9 | Terraform configurations require an initialization block to specify versions and a provider block to define credentials and endpoints.                       |
|  10 | The state file is a JSON document that tracks the current state of resources, enabling Terraform to determine necessary changes during apply operations.     |
|  11 | Resources are used to create new infrastructure, while data sources are used to fetch information about existing resources.                                  |
|  12 | Variables can be defined with types, defaults, and validations, and can be overridden via environment variables or command-line arguments.                   |
|  13 | The `terraform init` command downloads required providers, and `terraform apply` executes the configuration plan.                                            |
|  14 | To destroy resources, users can remove them from the configuration file and apply, or use the `terraform destroy` command for all resources.                 |
|  15 | The `terraform graph` command visualizes the dependency graph between resources to understand the execution order.                                           |
|  16 | Null resources with provisioners can be used to handle post-creation tasks, such as waiting for SSH connectivity before running Ansible playbooks.           |
|  17 | Terraform supports looping constructs like `count` and `for_each` to iterate over lists or maps for resource creation.                                       |
|  18 | Conditional logic can be implemented using the ternary operator to manage high availability across multiple availability zones.                              |
|  19 | Local values allow for computed values during execution, such as transforming lists into maps for iteration.                                                 |
|  20 | Remote state storage with locking features is recommended for team collaboration to prevent conflicts and enable versioning.                                 |
|  21 | Existing cloud resources can be imported into Terraform state using the `import` command to manage them as code.                                             |
|  22 | Terraform workspaces allow managing multiple environments with a single codebase, though folder-based separation is often preferred for isolation.           |
|  23 | Modules help avoid code duplication by encapsulating reusable infrastructure components with defined inputs and outputs.                                     |
|  24 | Atlantis is introduced as a tool for CI/CD integration, providing folder locking and approval workflows for Terraform changes.                               |
|  25 | Pulumi is presented as an alternative that allows writing infrastructure code in general-purpose languages like Python or Go.                                |
|  26 | Configuration drift, caused by manual changes outside of Terraform, can be mitigated by restricting direct access and using import features to resync state. |
|  27 | Best practices include using protected GitHub workflows to ensure all infrastructure changes are reviewed and tracked.                                       |
|  28 | The workshop concludes with a reminder that demo accounts will be deleted by the end of the month, encouraging users to save their work locally.             |

# Video

[![Video thumbnail](https://img.youtube.com/vi/8ozcLdiwr5w/hqdefault.jpg)](https://www.youtube.com/watch?v=8ozcLdiwr5w)

[Watch on YouTube](https://www.youtube.com/watch?v=8ozcLdiwr5w)
