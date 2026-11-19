---
layout: default
title: "A Field Guide To Integrating CEL in the Kubernetes Codebase - Sreeram Venkitesh & Priyanka Saggu"
nav_order: 11
parent: "Maintainer Summit 2025 - Europe"
type: Video Note
description: "This presentation by Priyanka Sagu and Sria Menitesh serves as a field guide to integrating the Common Expression Language (CEL) into the Kubernetes codebase, tracing the speakers’ journey from nov..."
resource: "https://www.youtube.com/watch?v=ODI3KwDLKas"
tags:
  - maintainer-summit-2025-europe
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-15T22:30:54+00:00
---

# Summary

This presentation by Priyanka Sagu and Sria Menitesh serves as a field guide to integrating the Common Expression Language (CEL) into the Kubernetes codebase, tracing the speakers’ journey from novice learners to active contributors.
The talk outlines the evolution of CEL in Kubernetes, starting with its introduction in Kubernetes 1.23 for CRD schema validation, and expanding to its current role in admission control policies and the definition of custom data types like IP addresses and quantities.
The core focus is on KEP-4595, a proposal to add CEL support to CRD additional printer columns, which addresses the limitations of JSONPath by enabling complex conditional logic, array manipulation, and default value handling for custom resource displays.
Through a live demonstration, the speakers showcase how CEL expressions can be compiled and executed within the API server to generate dynamic table columns, such as checking for the presence of fields or calculating values based on resource attributes.
The session concludes with a review of useful learning resources, including the CEL language definition and Go code labs, while inviting community feedback on feature requests like array truncation functions and CEL-based field selectors for `kubectl`.

# Main Points

|   # | Main point                                                                                                                                                                                               |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The talk serves as a field guide to integrating CEL into the Kubernetes codebase, driven by the speakers' one-year journey from learning CEL to working on KEP-4595.                                     |
|   2 | CEL, or Common Expression Language, is a Turing-complete language originally developed by Google that is ideal for lightweight expressions with C-like syntax.                                           |
|   3 | In Kubernetes, CEL is used for validation rules, such as ensuring replica fields are ordered appropriately, and is available through libraries like the regular expression and URL libraries.            |
|   4 | Metrics indicate growing popularity of CEL in Kubernetes, with numerous KEPs, issues, and a dedicated Slack channel for discussions on using and developing CEL.                                         |
|   5 | A recent CVE related to Git repository volumes suggested using Validating Admission Policy, which utilizes CEL rules for native API server validation instead of webhooks.                               |
|   6 | The evaluation process involves defining an environment with variables, compiling the expression into an abstract syntax tree, and executing it as a program with specific inputs.                       |
|   7 | In Go, the CEL package allows creating environments, compiling expressions via `env.compile` (which handles parsing and type checking), and evaluating results using `program.eval`.                     |
|   8 | CEL was introduced to Kubernetes in version 1.23 via KEP-2876, which added CEL-based validation for CRD schemas by integrating the Google CEL Go repository.                                             |
|   9 | The initial integration allowed CEL to understand Kubernetes objects and types, enabling validation rules under the `x-kubernetes-validations` field in CRD specs.                                       |
|  10 | Subsequent work moved CEL logic from CRDs to the API server, making it a first-class citizen and enabling features like CEL for admission control and Validating Admission Policies.                     |
|  11 | Mutating Admission Policies, introduced in KEP-3962, use CEL expressions to check for missing fields and apply mutation patches to resources.                                                            |
|  12 | Kubernetes has extended CEL with custom types for IP addresses, CIDRs, quantities, and URLs, defined within the API server to support day-to-day Kubernetes operations.                                  |
|  13 | A CEL wish list issue exists in the Kubernetes repository to gather community feedback and requirements for future CEL-based solutions.                                                                  |
|  14 | KEP-4595 proposes adding CEL support to CRD additional printer columns to overcome the limitations of JSONPath, which cannot handle complex conditionals or array operations.                            |
|  15 | The proposal introduces a new `expression` field that is mutually exclusive with `jsonPath`, allowing users to define CEL expressions that use the CRD schema as input.                                  |
|  16 | These expressions are compiled and run natively in the kube-apiserver, similar to how JSONPath is currently executed, enabling complex logic like default values and conditional checks.                 |
|  17 | A demo using a "shirt" CRD showed that CEL expressions can check for the presence of arrays, calculate boolean values based on field contents, and handle optional fields more gracefully than JSONPath. |
|  18 | Useful resources for learning CEL include the CEL language definition Markdown, CEL Go code labs, an online playground, and the Kubernetes CEL wish list issue.                                          |
|  19 | The speakers highlighted the importance of the SIG API Machinery CEL Slack channel for community interaction and thanked Alex Sinsky for foundational support.                                           |
|  20 | Audience feedback included requests for specific CEL functions to handle list truncation and for CEL-based field selectors in kubectl, which the speakers acknowledged as valuable future enhancements.  |

# Video

[![Video thumbnail](https://img.youtube.com/vi/ODI3KwDLKas/hqdefault.jpg)](https://www.youtube.com/watch?v=ODI3KwDLKas)

[Watch on YouTube](https://www.youtube.com/watch?v=ODI3KwDLKas)
