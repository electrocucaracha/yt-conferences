---
layout: default
title: "GopherCon 2025: The Go Cryptography State of the Union - Filippo Valsorda"
nav_order: 21
parent: GopherCon 2025
type: Video Note
description: "Filippo Valsorda presented an annual performance review of the Go cryptography standard library at GopherCon New York, highlighting significant advancements in security, compliance, and performance."
resource: "https://www.youtube.com/watch?v=YnyeAQblUyA"
youtube_stats:
  view_count: 2529
  like_count: 85
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

Filippo Valsorda presented an annual performance review of the Go cryptography standard library at GopherCon New York, highlighting significant advancements in security, compliance, and performance.
The team successfully shipped post-quantum key exchanges using the ML-KEM algorithm, which is now enabled by default in Go 1.24’s `crypto/tls` and SSH implementations to protect against future quantum threats, while intentionally delaying post-quantum digital signatures due to protocol complexity and size constraints.
A major milestone was the introduction of a native Go FIPS 140-3 cryptographic module, eliminating the need for unsupported cgo-based solutions like BoringCrypto and ensuring compliance across multiple platforms without altering existing application behavior.
The team also maintained an excellent security track record, evidenced by the absence of severe vulnerabilities since 2019 and a clean audit by Trail of Bits, while implementing rigorous new testing methodologies such as mutation testing for assembly code and accumulated test vectors to catch subtle bugs.
Additionally, the year saw substantial performance improvements, including faster SHA-3 and AES-CTR implementations, the removal of `math/big` from RSA operations, and the migration of packages like `crypto/hkdf` and `crypto/sha3` into the standard library, all supported by the new Geomys company and the addition of Daniel McCartney as a permanent maintainer.

# Main Points

|   # | Main point                                                                                                                                                                                 |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | The Go cryptography team shipped post-quantum key exchanges, solved FIPS 140 compliance, and maintained an excellent security track record.                                                |
|   2 | Vulnerability severity is graded using the "Filippo's unhappiness score" (shrug, oof, ouch), with no "ouch" incidents since 2019 and no Go-specific "oof" since 2021.                      |
|   3 | Trail of Bits conducted the first professional security audit of the Go cryptography standard library primitives and found no vulnerabilities in the core code.                            |
|   4 | Post-quantum key exchange using ML-KEM is available in Go 1.24 and is enabled by default in crypto/tls as a hybrid with X25519 to mitigate future quantum threats.                         |
|   5 | The hybrid approach combines classical and post-quantum algorithms to ensure security even if one method is broken, and this is also supported in x/crypto/SSH starting from version 0.38. |
|   6 | Post-quantum digital signatures are intentionally delayed because they are less urgent than key exchange and require protocol redesigns to handle larger signature sizes.                  |
|   7 | FIPS 140-3 compliance is now achieved through a native Go cryptographic module, eliminating the need for unsupported GOEXPERIMENT flags and cgo dependencies on BoringCrypto.              |
|   8 | The FIPS 140 module is tested across multiple platforms, including FreeBSD, macOS, and Windows, with costs covered by Geomys to ensure broad compliance for the community.                 |
|   9 | The team maintained higher security standards than required by FIPS 140, such as using hedged ECDSA and kernel-derived entropy for randomness, despite these not being strictly mandated.  |
|  10 | New packages crypto/hkdf, crypto/pbkdf, and crypto/sha3 were moved from x/crypto to the standard library, with SHA-3 becoming faster and allocation-free.                                  |
|  11 | Performance improvements include a 2 to 9 times speedup for AES-CTR and faster RSA key generation by removing math/big usage in favor of constant-time code.                               |
|  12 | Support for RSA keys smaller than 1024 bits was removed to prevent the use of insecure keys that cannot be distinguished by code inspection alone.                                         |
|  13 | Mutation testing was introduced to verify assembly code coverage for carry operations, ensuring that edge cases in low-level implementations are properly tested.                          |
|  14 | Accumulated test vectors use rolling hashes to efficiently test large input spaces without storing massive amounts of test data in the repository.                                         |
|  15 | Integration of external test suites like BoringSSL's BoGo and Let's Encrypt's Pebble has made crypto/tls and ACME implementations more spec-compliant.                                     |
|  16 | Assembly code has been cleaned up to remove raw machine code encodings and obsolete optimizations for CPUs lacking AVX2, improving maintainability.                                        |
|  17 | Server-side TLS Encrypted Client Hello support was added, and crypto/rand.Read was implemented to never fail, with rigorous testing of failure scenarios.                                  |
|  18 | Geomys, the company leading the Go cryptography effort, has hired Daniel McCartney as a permanent maintainer to support the FIPS 140 and general maintenance work.                         |
|  19 | Future plans include implementing TLS profiles to simplify configuration for specific goals like FIPS compliance or modern security, and exploring passkey support.                        |

# Video

[![Video thumbnail](https://img.youtube.com/vi/YnyeAQblUyA/hqdefault.jpg)](https://www.youtube.com/watch?v=YnyeAQblUyA)

[Watch on YouTube](https://www.youtube.com/watch?v=YnyeAQblUyA)
