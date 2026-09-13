---
type: Video Note
title: "Emissary-ingress: Version 4 and What Comes Next - Flynn, Buoyant"
description: "Flynn from Buoyant led a session discussing the release of Emissary 4.0.1, emphasizing the importance of upgrading from version 3.10 due to known bugs and security flaws in the older Envoy version, as no further Emissary 3 releases will occ..."
resource: https://www.youtube.com/watch?v=LIlW-iYpB1k
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Flynn from Buoyant led a session discussing the release of Emissary 4.0.1, emphasizing the importance of upgrading from version 3.10 due to known bugs and security flaws in the older Envoy version, as no further Emissary 3 releases will occur.
He highlighted that Emissary 4 makes it much easier to update dependencies and track the evolving ecosystem, and thanked contributors for their help in testing and development.
Flynn encouraged community involvement to sustain the project, noting that only a small team currently maintains it, and outlined future improvements for Emissary 5, such as migrating to Go and updating API groups.
He addressed concerns about the conversion webhook and storage version migration, mentioning plans to simplify these processes.
The session concluded with a discussion on the project's transition from company to community stewardship, improvements in the release process, and a reaffirmation of the project's commitment to timely security updates.
# Main Points

|   # | Main point                                                                                                                                  |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Emissary 4.0.1 is released; 4.0.0 had a CID glitch but binaries are identical.                                                              |
|   2 | Users are encouraged to upgrade to Emissary V4 due to known bugs and security flaws in 3.10; no further Emissary 3 releases will occur.     |
|   3 | Thanks given to Mark S, Phil Pevler, and Jeremy Dental for their contributions and production testing.                                      |
|   4 | Emissary 4 development has been slow due to a small contributor base; more help is needed.                                                  |
|   5 | Main goal of Emissary V4 is to simplify consuming new Envoy releases, dependency updates, and building new releases.                        |
|   6 | Emissary’s version of controller-gen includes custom code not yet upstreamed; a conversation with API machinery maintainers is anticipated. |
|   7 | Upgrading Emissary to the latest Envoy version for 4.1 will be straightforward.                                                             |
|   8 | Emissary V5 may include switching to Go-only, moving CRDs to the emissary.ingress.dev API group, and removing the conversion webhook.       |
|   9 | V4 defaults to not installing the conversion webhook; users should be aware when upgrading.                                                 |
|  10 | The Kubernetes storage version migrator is not stable or functional; a simpler migration tool may be released.                              |
|  11 | Feedback indicates users appreciate Emissary’s input language simplicity and developer setup.                                               |
|  12 | Project sustainability depends on increased community contributions.                                                                        |
|  13 | Communication has moved to CNCF Slack; Datawire Slack is discontinued.                                                                      |
|  14 | Emissary originated at Datawire, which became Ambassador Labs, now acquired by Gravity.                                                     |
|  15 | Security updates are a primary concern for users; V4 addresses this by making releases and updates easier.                                  |
|  16 | Building and releasing Emissary is now much simpler and faster than before.                                                                 |
|  17 | An Envoy upgrade is planned for the next Emissary release.                                                                                  |
|  18 | The session concluded with an invitation for questions and appreciation for attendees.                                                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=LIlW-iYpB1k)