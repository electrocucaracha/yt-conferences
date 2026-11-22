---
layout: default
title: "Why `len('😶‍🌫️') == 4` and other weird things you should know about strings in Python"
nav_order: 11
parent: PyCon US 2025
type: Video Note
description: "Marie Råål and Ingvar Moe present a detailed exploration of Python string handling, emphasizing that Unicode complexity arises from the need to represent diverse global languages using binary data."
resource: "https://www.youtube.com/watch?v=np-xKVMIKcY"
youtube_stats:
  view_count: 2415
  like_count: 76
  channel_subscriber_count: 34500
tags:
  - pycon-us-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T01:39:37+00:00
---

# Summary

Marie Råål and Ingvar Moe present a detailed exploration of Python string handling, emphasizing that Unicode complexity arises from the need to represent diverse global languages using binary data.
They explain how encoding standards like UTF-8 and Python’s internal 8-, 16-, and 32-bit encodings allow for efficient storage, while highlighting that simple operations like comparison and slicing are often misleading due to underlying code point structures.
The speakers advise against using the `is` operator for string equality, recommending the `==` operator instead, and suggest using `casefold` rather than `lower` for robust case-insensitive comparisons to handle linguistic nuances like the German sharp S.
Furthermore, they demonstrate that characters such as accented letters and emojis are often composed of multiple code points, including zero-width joiners and variant selectors, which can cause unexpected results in length calculations and slicing.
To address these issues, the presentation recommends utilizing Unicode normalization forms like NFC and NFKC, and employing libraries such as `regex` or `PyICU` to correctly process extended grapheme clusters, ensuring that text manipulation aligns with visual character boundaries rather than raw code point counts.

# Main Points

|   # | Main point                                                                                                                                                |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Strings in Python are Unicode strings that require understanding of encoding, comparison, and slicing complexities.                                       |
|   2 | Computers store text as bits, leading to standardized encodings like ASCII, which supports only 128 characters and fails for many languages.              |
|   3 | Unicode standardizes character representation, using variable-length UTF-8 encoding to balance storage efficiency and compatibility.                      |
|   4 | Python uses 8-bit, 16-bit, or 32-bit internal encodings depending on the maximum code point width required by the string.                                 |
|   5 | The `is` operator checks object identity rather than text equality, making it unreliable for string comparison despite string interning optimizations.    |
|   6 | Case-insensitive comparison should use `casefold` instead of `lower` or `upper` to correctly handle complex Unicode characters like the German sharp s.   |
|   7 | Unicode normalization forms such as NFC, NFD, NFKC, and NFKD standardize text representation, with compatibility forms useful for search and identifiers. |
|   8 | Homographs and confusables are visually similar but distinct characters that pose security risks and cannot be normalized to identical code points.       |
|   9 | Locale-dependent casing, such as in Turkish, is not fully implemented in Python, requiring external handling for correct case conversion.                 |
|  10 | Some code points map to multiple glyphs depending on font selection, meaning code points alone do not always determine visual appearance.                 |
|  11 | String length in Python counts code points, not visual characters, causing emojis and accented letters to have lengths greater than one.                  |
|  12 | Emojis are constructed using zero-width joiners and variant selectors, which can result in unexpected slicing behavior and backward compatibility issues. |
|  13 | Extended grapheme clusters represent single visual characters composed of multiple code points, which are not natively supported in Python.               |
|  14 | Libraries like `regex` and `PyICU` provide support for handling extended grapheme clusters and advanced Unicode features.                                 |
|  15 | Limiting input by code point count or grapheme clusters may still allow excessive visual length due to unlimited code points per cluster.                 |
|  16 | Developers should use UTF-8 for sharing content, apply case folding for comparisons, normalize strings, and consider Unicode security implications.       |
|  17 | Unicode is an evolving standard that does not cover every linguistic nuance, and Python does not implement all Unicode features.                          |

# Video

[![Video thumbnail](https://img.youtube.com/vi/np-xKVMIKcY/hqdefault.jpg)](https://www.youtube.com/watch?v=np-xKVMIKcY)

[Watch on YouTube](https://www.youtube.com/watch?v=np-xKVMIKcY)
