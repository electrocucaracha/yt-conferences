---
layout: default
title: "GopherCon 2025: Building a Decentralized Social Media App with Go and ATProto - Gautam Dey"
nav_order: 15
parent: GopherCon 2025
type: Video Note
description: "Gotham, a Go developer at Scout Red, presents an overview of the AT Protocol, the decentralized architecture behind Bluesky, which he finds exciting for its potential to foster new applications."
resource: "https://www.youtube.com/watch?v=7ZbefJSvdQ0"
youtube_stats:
  view_count: 1309
  like_count: 25
  channel_subscriber_count: 41100
tags:
  - gophercon-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-21T05:22:37+00:00
---

# Summary

Gotham, a Go developer at Scout Red, presents an overview of the AT Protocol, the decentralized architecture behind Bluesky, which he finds exciting for its potential to foster new applications.
The protocol distinguishes itself from federated systems like Mastodon by using Personal Data Servers (PDS) to store all user actions, such as posts and likes, ensuring that users retain ownership of their data and social graph when switching services.
Data flows from these PDSs through relays, which aggregate information into a "fire hose" that app views consume to build user interfaces, while labelers and feed generators provide moderation and custom timeline capabilities.
Identity is managed via DNS-based handles that resolve to Decentralized Identifiers (DIDs), allowing for verifiable ownership and organizational affiliation, though the current DID method relies on a centralized directory service.
Gotham demonstrates the practical application of these concepts by building a simple live app view in Go that displays a user’s image feed and allows for authenticated interactions like liking posts, highlighting the ease of development using standard HTTP libraries and showcasing the ecosystem’s growing capabilities.

# Main Points

|   # | Main point                                                                                                                                          |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker, Gotham, has been coding in Go since 2012 and works at Scout Red, an open-source tile server project.                                   |
|   2 | Interest in AT Proto was sparked by Blue Sky's architecture, which aims to create a decentralized social network.                                   |
|   3 | AT Proto stands for Authenticated Protocol, where every data object is authenticated to verify the author.                                          |
|   4 | The architecture consists of three core components: Personal Data Servers (PDS), Relays, and App Views.                                             |
|   5 | PDS stores all user actions, such as posts and likes, ensuring users retain their data and network when switching services.                         |
|   6 | Unlike Mastodon, liking a post creates a new record in the user's PDS that points to the original post rather than modifying it.                    |
|   7 | Relays aggregate data from multiple PDSs into a fire hose for App Views to consume and analyze.                                                     |
|   8 | Current PDS data is public, with ongoing community discussions about implementing private and protected data features.                              |
|   9 | Two types of relays exist: standard websockets using Cbor format and Jetstream, which allows filtered JSON data streams.                            |
|  10 | App Views listen to the fire hose, aggregate data, and write user actions back to specific PDSs.                                                    |
|  11 | Data objects are structured blobs defined by a schema called a Lexicon, based on JSON Schema.                                                       |
|  12 | Labelers are Blue Sky-specific moderation tools that listen to the fire hose and assign labels to content for filtering or blocking.                |
|  13 | Feed generators create custom timelines by listening to the fire hose and organizing posts based on specific criteria.                              |
|  14 | Handles in AT Proto are DNS names, allowing organizational verification and ownership, but they are aliases for Decentralized Identifiers (DIDs).   |
|  15 | DIDs are hashes that link to a DID document, which contains the location of the user's PDS server.                                                  |
|  16 | Resolving a handle to a PDS involves checking DNS records or well-known URLs to find the DID, then querying the PLC directory for the DID document. |
|  17 | The DID document must be verified by matching the ID field and ensuring the handle is listed in the alsoKnownAs field.                              |
|  18 | The PLC directory is currently the only supported DID method, representing a point of centralization, while web-based DIDs are under development.   |
|  19 | Documentation is transitioning from XRPC terminology (queries and procedures) to standard HTTP methods (GET and POST).                              |
|  20 | A live demo was built using standard Go HTTP libraries to create a simple App View that displays a user's image feed.                               |
|  21 | The OAuth process in AT Proto involves exchanging credentials between App Views and PDSs without pre-registration.                                  |
|  22 | The demo application allows users to view a gallery of images from a handle and interact by liking or commenting on posts.                          |
|  23 | Several advanced applications have been built on AT Proto, including Streamplace for live streaming, Tangled for Git repositories, and Payabn.      |
|  24 | The speaker encourages developers to explore these tools and build new applications to improve the internet through decentralized protocols.        |

# Video

[![Video thumbnail](https://img.youtube.com/vi/7ZbefJSvdQ0/hqdefault.jpg)](https://www.youtube.com/watch?v=7ZbefJSvdQ0)

[Watch on YouTube](https://www.youtube.com/watch?v=7ZbefJSvdQ0)
