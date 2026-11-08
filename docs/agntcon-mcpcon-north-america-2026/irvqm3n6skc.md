---
layout: default
title: "Universal Commerce Protocol:... - Ilya Grigorik, Shopify, Amit Handa, Google & Greg Smith, Google"
nav_order: 17
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "The Universal Commerce Protocol (UCP) is an open, machine-to-machine standard designed to provide a shared language for consumer agents and businesses, addressing the complexity of commerce workflo..."
resource: "https://www.youtube.com/watch?v=IRVqm3N6SKc"
tags:
  - agntcon-mcpcon-north-america-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-08T02:03:18+00:00
---

# Summary

The Universal Commerce Protocol (UCP) is an open, machine-to-machine standard designed to provide a shared language for consumer agents and businesses, addressing the complexity of commerce workflows beyond simple payment forms.
Launched approximately ten months ago, UCP has achieved rapid adoption by major platforms including Shopify, Google, Meta, and TikTok, with millions of stores enabling the protocol by default.
A core design principle is transport agnosticism, allowing UCP to function over various interfaces such as REST, MCP, and Web MCP, which facilitates reliable agent interactions within browser environments.
The protocol emphasizes openness and extensibility by defining a minimal common core that partners can extend without requiring central ratification, similar to HTTP headers, while also ensuring compliance with regulatory requirements like privacy disclosures and subscription laws.
Looking ahead, UCP is expanding beyond shopping into new verticals such as lodging, food, and B2B services, leveraging its foundational primitives to reduce integration costs and improve the reliability of agentic commerce experiences.

# Main Points

|   # | Main point                                                                                                                                                                                                              |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | (Universal Commerce Protocol) was initiated to establish a shared, machine-to-machine language for consumer agents and businesses, addressing inconsistent definitions of commerce constructs like carts and checkouts. |
|   2 | , moving from initial checkout and order releases to a full-funnel representation covering catalog, cart, and checkout.                                                                                                 |
|   3 | , designed to model the commerce domain independently of the underlying protocol, allowing implementation via REST, MCP, or JSON-RPC.                                                                                   |
|   4 | ; UCP provides the structured domain schema and workflow logic, while MCP serves as a transport layer, including Web MCP for browser-based agent interactions.                                                          |
|   5 | , such as split shipping, gift cards, and subscriptions, which are difficult to handle with simple browser actuation or unstructured data.                                                                              |
|   6 | , aiming to define a smallest common core (e.g., basic product shapes) that allows partners to add custom extensions without requiring central ratification.                                                            |
|   7 | , such as Prop 65 disclosures, subscription laws, and allergen warnings, as structured objects to ensure reliable agent behavior and reduce merchant liability.                                                         |
|   8 | , supporting both agent-driven and human-driven interactions, including escalation flows via "continue URLs" for cases where agents cannot complete a task.                                                             |
|   9 | , such as payment handlers and 3DS authentication, by defining generic primitives like "actions" to interrupt flows for user attention, rather than creating new standards.                                             |
|  10 | , with millions of Shopify stores enabled by default, and integration by major platforms including Google, Meta, TikTok, and Muse.                                                                                      |
|  11 | , lodging, and B2B services through dedicated technical councils that reuse core UCP primitives.                                                                                                                        |
|  12 | , including SDKs, conformance tests, and adoption resources available at ucp.dev, with a focus on making implementation easier for merchants and developers.                                                            |

# Video

[![Video thumbnail](https://img.youtube.com/vi/IRVqm3N6SKc/hqdefault.jpg)]("https://www.youtube.com/watch?v=IRVqm3N6SKc")

[Watch on YouTube](https://www.youtube.com/watch?v=IRVqm3N6SKc)
