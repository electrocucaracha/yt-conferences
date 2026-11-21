---
layout: default
title: "Hash me if you can: let's talk about Python dictionaries! - Mia Bajić"
nav_order: 121
parent: PyCon US 2026
type: Video Note
description: "Python dictionaries achieve constant-time performance by converting keys into array indices using a hash function, followed by a modulo operation to map the result to a specific slot within a fixed..."
resource: "https://www.youtube.com/watch?v=kHtg-2JMEgk"
youtube_stats:
  view_count: 672
  like_count: 14
  channel_subscriber_count: 34500
tags:
  - pycon-us-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-20T08:08:06+00:00
---

# Summary

Python dictionaries achieve constant-time performance by converting keys into array indices using a hash function, followed by a modulo operation to map the result to a specific slot within a fixed-size table.
To handle inevitable collisions, Python employs open addressing with a sophisticated probing strategy that utilizes unused bits from the original hash to jump between slots, avoiding the clustering issues associated with simple linear probing.
This mechanism was historically vulnerable to hash-flooding denial-of-service attacks, where attackers crafted keys to force collisions; Python mitigated this by introducing randomized string hashing in version 3.3 and later adopting the cryptographic SipHash algorithm in version 3.4 to prevent secret key extraction.
Additionally, the internal structure of dictionaries was optimized in Python 3.6 with a compact layout that separates indices from entries, reducing memory usage and guaranteeing insertion order, while deleted keys are marked with "tombstones" to preserve the integrity of probe chains.
Finally, the talk highlights that hashing is a fundamental computer science concept extending beyond dictionaries to critical applications such as Bloom filters, consistent hashing for distributed systems, and Merkle trees used in Git and blockchain technologies.

# Main Points

|   # | Main point |
| --: | ---------- |
|   1 | Arrays provide constant-time access via direct indexing, which serves as the foundation for dictionary performance. |
|   2 | Python dictionaries convert keys into array indices using a hash function that returns a large integer. |
|   3 | The hash value is reduced to a valid slot index by taking the modulo of the table size. |
|   4 | CPython uses bitwise AND with table size minus one instead of modulo for faster index calculation. |
|   5 | Dictionary operations involve three constant-time steps: hashing the key, calculating the slot, and storing or retrieving data. |
|   6 | Python 3.6 introduced a compact dictionary layout using separate index and entry arrays to reduce memory usage by 20%. |
|   7 | This redesign also established insertion order as a language guarantee starting in Python 3.7. |
|   8 | Hash collisions occur frequently due to the birthday paradox, where the probability grows quadratically with item count. |
|   9 | Python handles collisions using open addressing rather than chaining to maintain CPU cache efficiency. |
|  10 | Linear probing creates clusters that degrade performance, so Python uses a perturb variable to mix unused hash bits into the probe sequence. |
|  11 | This perturb strategy ensures different keys follow different probe paths, keeping most lookups to one or two probes. |
|  12 | Hash collision attacks exploit predictable hash functions to force quadratic time complexity in web frameworks. |
|  13 | In 2011, researchers demonstrated denial-of-service attacks against PHP, Python, Ruby, Java, and Node.js using precomputed colliding keys. |
|  14 | Python 3.3 added random hash seeds to string hashing to prevent precomputation, but timing attacks could still leak the secret. |
|  15 | Python 3.4 adopted SipHash, a cryptographic hash function, which remains secure against key extraction attacks. |
|  16 | String hash randomization applies only to strings and bytes, as these are the types attackers control in HTTP requests. |
|  17 | The hash of integer -1 is -2 to avoid ambiguity with C error codes, causing -1 and -2 to collide in dictionaries. |
|  18 | Deleting a key leaves a tombstone marker to preserve probe chains, preventing unreachable entries during lookup. |
|  19 | Overriding __eq__ without __hash__ makes a class unhashable to prevent inconsistent dictionary behavior. |
|  20 | Hashing is a foundational concept used in Bloom filters, consistent hashing, Merkle trees, and HyperLogLog structures. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/kHtg-2JMEgk/hqdefault.jpg)](https://www.youtube.com/watch?v=kHtg-2JMEgk)

[Watch on YouTube](https://www.youtube.com/watch?v=kHtg-2JMEgk)
