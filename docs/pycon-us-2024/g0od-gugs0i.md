---
layout: default
title: "Talks - William Woodruff: Building a Rusty path validation library for PyCA Cryptography"
nav_order: 170
parent: PyCon US 2024
type: Video Note
description: "William Wra, from Trail of Bits, presented the development of a new X.509 path validation library for the Python cryptography package, written entirely in Rust to eliminate dependencies on OpenSSL ..."
resource: "https://www.youtube.com/watch?v=g0oD-gUGs0I"
youtube_stats:
  view_count: 129
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

William Wra, from Trail of Bits, presented the development of a new X.509 path validation library for the Python cryptography package, written entirely in Rust to eliminate dependencies on OpenSSL and its associated security baggage.
The project was motivated by the critical role of X.509 in securing internet communications and the numerous vulnerabilities, such as denial-of-service attacks and memory safety bugs, found in legacy implementations.
To ensure correctness and performance, the team adopted design principles focused on minimality, strict adherence to RFC 5280 and CA/B Forum profiles, and efficient graph traversal algorithms that handle complex constraints like name and path length limits.
A key innovation was the creation of "X.509 Limbo," a comprehensive test suite that compares their implementation against others, which successfully identified bugs in existing validators, including a memory corruption issue in GnuTLS.
The resulting library offers a safer, faster, and more user-friendly API for Python developers, significantly improving the security of the Python ecosystem while maintaining compatibility with real-world certificate chains.

# Main Points

|   # | Main point                                                                                                                                                                             |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | William WRA presented the development of a Rust-based X509 path validation library for the Python cryptography package.                                                                |
|   2 | The new implementation is pure Rust, contains approximately 25,000 lines of code, and avoids OpenSSL dependencies to eliminate legacy security baggage.                                |
|   3 | X509 validation is critical for HTTPS security but is complex, involving graph traversal, dynamic constraint accumulation, and rejection encoding during search.                       |
|   4 | Design principles include minimality, correctness, and speed, focusing only on RFC 5280 and CA/B Forum profiles to reject legacy and insecure key types.                               |
|   5 | The implementation treats path validation as a dynamic depth-first search over a cyclic graph, correctly handling name constraints and avoiding premature rejection of invalid chains. |
|   6 | Performance was improved by 60% over OpenSSL by replacing external SPKI parsing with a native Rust parser and aggressively caching parsed keys and extensions.                         |
|   7 | A new test suite called X509 Limbo was created to compare implementations, identify bugs in other libraries like Go and GnuTLS, and ensure 100% test coverage.                         |
|   8 | The public API enforces domain separation between server and client validation to prevent user errors and uses distinct data types for trust roots and intermediates.                  |
|   9 | Lessons learned include discrepancies between RFCs and real-world implementations, such as ignoring subject fields and failing to enforce serial number checks.                        |
|  10 | Specific bugs found in other implementations include false negatives in name constraint handling and memory corruption issues triggered by specific test vectors.                      |
|  11 | Future work includes supporting additional profiles like Intel SGX, adding revocation APIs for CRL and OCSP, and integrating X509 Limbo into upstream projects.                        |
|  12 | The work was funded by the Sovereign Tech Fund and developed by Trail of Bits in collaboration with Python cryptography maintainers.                                                   |
|  13 | The library is available immediately via pip install cryptography and serves as a secure alternative to legacy OpenSSL-based validation methods.                                       |

# Video

[![Video thumbnail](https://img.youtube.com/vi/g0oD-gUGs0I/hqdefault.jpg)](https://www.youtube.com/watch?v=g0oD-gUGs0I)

[Watch on YouTube](https://www.youtube.com/watch?v=g0oD-gUGs0I)
