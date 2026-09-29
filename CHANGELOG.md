<!-- Markdownlint-disable MD024 -->

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [4.1.2] - 2026-09-29

### Changed

- Upgraded the reusable workflow to version v9.3.3 to leverage recent bugfixes and workflow enhancements from the upstream repository. [2aa3a7d8](https://github.com/electrocucaracha/yt-conferences/commit/2aa3a7d8e83976ec4071e6ee4e0bd2bdc38c91d2)

## [4.1.1] - 2026-09-29

### Changed

- clarified the context of reusable workflows and sub-actions sharing repository tags by repositioning the relevant comment above the commit hash lookup. [25aed81e](https://github.com/electrocucaracha/yt-conferences/commit/25aed81e9dffc2c8701919b02637e6f0f19bbb0b)

## [4.1.0] - 2026-09-28

### Added

- Enabled improved documentation for the main function by adding a docstring describing its purpose. [c132fa5e](https://github.com/electrocucaracha/yt-conferences/commit/c132fa5e1ab96e96e573236a8f2f6e95013a996f)

## [4.0.5] - 2026-09-28

### Fixed

- The GitHub Actions update process has been stabilized to correctly version reusable workflows and composite actions residing in subfolders. [802a40de](https://github.com/electrocucaracha/yt-conferences/commit/802a40ded06da682b890cb87404b4bb98c9af75c)

## [4.0.4] - 2026-09-28

### Changed

- Updated the link checker in the documentation workflow to version 2.9.0, enabling improved link detection and bugfixes. [d028ec38](https://github.com/electrocucaracha/yt-conferences/commit/d028ec3869304b5efd0b70e723d95f11447bd12d)

## [4.0.3] - 2026-09-28

### Changed

- Optimized GitHub Actions workflow token handling to prevent default token usage for subsequent Git commands and introduced a personal access token for authentication in the push step. [8192e3d7](https://github.com/electrocucaracha/yt-conferences/commit/8192e3d73d3719bf792fae4e8236d326ba30f053)

## [4.0.2] - 2026-09-28

### Changed

- Optimized the pre-commit workflow by upgrading the ai-prepare-commit-msg hook to v19.2.4, ensuring the latest improvements and fixes are incorporated into commit message preparation functionality and compatibility. [fc909b68](https://github.com/electrocucaracha/yt-conferences/commit/fc909b6855de5c4971eb227e206863e8bfcc491f)

## [4.0.1] - 2026-09-28

### Changed

- Automatically updated Markdown notes now reflect the unavailability of YouTube videos, reducing manual maintenance and ensuring documentation remains current for users. [a24697dd](https://github.com/electrocucaracha/yt-conferences/commit/a24697dd85dc0e47feb952d3678941a83590585f)

## [4.0.0] - 2026-09-28

### Removed

- Stabilized documentation by removing unavailable and placeholder content, including talks, sessions, and videos no longer available or missing, which reduces confusion and improves overall documentation integrity. [e002195d](https://github.com/electrocucaracha/yt-conferences/commit/e002195db729ab6017160b29c6c9c6e85aa7b0d3)

## [3.3.3] - 2026-09-27

### Changed

- Escaped the asterisk in `package*.json` filenames to prevent Markdown formatting issues and improve changelog readability. [201b2699](https://github.com/electrocucaracha/yt-conferences/commit/201b26996cdf42ba7f247f3afaca8b0385946f35)

## [3.3.2] - 2026-09-27

### Changed

- Modernized GitHub Pages and documentation workflows to use the "main" branch and specified target files for the link checker, ensuring consistency and reproducibility. [3278feb4](https://github.com/electrocucaracha/yt-conferences/commit/3278feb4c5c83b1c106deb30011c0bfd208c2eb4)

## [3.3.1] - 2026-09-27

### Fixed

- Stabilized documentation rendering by escaping pipe characters in Markdown link titles, allowing for consistent display of literal pipe characters without unintended table formatting. [9860ff60](https://github.com/electrocucaracha/yt-conferences/commit/9860ff60663e3952b1f61eb91f8674d573cc9c70)

## [3.3.0] - 2026-09-27

### Added

- Enabled documentation workflow automation through the transition to Kiso in version 3.2.7, and included dependency upgrades and user experience enhancements in versions 3.2.0 through 3.2.8. [159dd861](https://github.com/electrocucaracha/yt-conferences/commit/159dd8618a4958f1466292b1f8d2455f2532b039)

## [3.2.8] - 2026-09-27

### Changed

- Updated the ai-prepare-commit-msg pre-commit hook to v19.0.0, integrating the latest features and fixes for improved commit message preparation and better tooling support. [fa575063](https://github.com/electrocucaracha/yt-conferences/commit/fa575063939116b65031703533fc164f4a9de772)

## [3.2.7] - 2026-09-27

### Changed

- Simplified the documentation workflow by transitioning to Kiso for site generation and validation, enabling standardized tooling and improved local preview capabilities. [517f5da5](https://github.com/electrocucaracha/yt-conferences/commit/517f5da5584284ec8c17c262af9fcdebf544eab2)

## [3.2.6] - 2026-09-27

### Changed

- Simplified the scheduled versions update workflow to reuse a shared workflow from electrocucaracha/gh-workflows, enabling consistency across repositories and concurrent updates without overlapping runs. [933bfb1c](https://github.com/electrocucaracha/yt-conferences/commit/933bfb1c71f281a3d8c94fe5d811a35908d99465)

## [3.2.5] - 2026-09-27

### Changed

- Simplified the documentation for several sessions by introducing video thumbnails and a consistent timestamp format, resulting in an improved user experience. [406516cd](https://github.com/electrocucaracha/yt-conferences/commit/406516cdcf53a5908792e7633a84e00805d56cde)

## [3.2.4] - 2026-09-27

### Fixed

- Stabilized the fmt target's verbosity by suppressing prettier command output during execution. [d123da67](https://github.com/electrocucaracha/yt-conferences/commit/d123da67f02afe087789bf923a7e282201960b43)

## [3.2.3] - 2026-09-27

### Changed

- Upgraded setup-uv and ai-prepare-commit-msg dependencies to v10.2.0 and v18.1.0 respectively, enabling improved features and bugfixes in the build and docs workflows with no breaking changes. [d063a4ac](https://github.com/electrocucaracha/yt-conferences/commit/d063a4ac07ce1ce2ab71ce77a41cac5b8f4bc8f8)

## [3.2.2] - 2026-09-18

### Changed

- Updated the ai-prepare-commit-msg pre-commit hook to version 17.0.1 to incorporate the latest features and bugfixes, keeping development tools current and aligned with upstream updates. [a180d6cc](https://github.com/electrocucaracha/yt-conferences/commit/a180d6cc90a063d992ddfc1ef1a872e7e93b3e32)

## [3.2.1] - 2026-09-18

### Changed

- Excluded `node_modules/` and `package*.json` files from version control to prevent repository noise and reduce unnecessary tracking. [85540ba2](https://github.com/electrocucaracha/yt-conferences/commit/85540ba2526a45c0aadc4ebdf10ced28c37bc709)

## [3.2.0] - 2026-09-15

### Added

- Enabled clearer tracking of project evolution for users and maintainers by introducing a structured changelog following Keep a Changelog and Semantic Versioning conventions, which records notable changes, features, and fixes for each release. [3a5d67d8](https://github.com/electrocucaracha/yt-conferences/commit/3a5d67d855b57c5efc4d203d1ef42a83f04c14d2)

## [3.1.3] - 2026-09-14

### Changed

- Streamlined event documentation navigation by unifying documentation for conferences and reports under a single index.md file with enhanced summaries. [a9ede86f](https://github.com/electrocucaracha/yt-conferences/commit/a9ede86f9605736090fd2ce2243713844e178950)

## [3.1.2] - 2026-09-13

### Fixed

- Resolved broken links in documentation to ensure accurate references to specific documents. [9b680b6e](https://github.com/electrocucaracha/yt-conferences/commit/9b680b6e8d8b8b37c3b8b4c037cf13f060156cba)

## [3.1.1] - 2026-09-13

### Changed

- Enhanced the readme with a project structure diagram to improve clarity and navigation for users. [5d47b1bd](https://github.com/electrocucaracha/yt-conferences/commit/5d47b1bd120c795bcfd76a7aba1985fbcccc9e5d)

## [3.1.0] - 2026-09-13

### Added

- Simplified the linter workflow to exclude spell checking during automated validation, reducing noise from non-critical spelling errors in CI runs. [70d52edc](https://github.com/electrocucaracha/yt-conferences/commit/70d52edcfd5aa2e242f2cef56e29d25289ff7781)

## [3.0.2] - 2026-09-13

### Fixed

- Improved error handling and CLI usability by ignoring README.md files during bundle validation and setting default values for the root argument in the main function. [06958aaa](https://github.com/electrocucaracha/yt-conferences/commit/06958aaabbebfc08ab290ac7c17d6d6e09f23dd6)

## [3.0.1] - 2026-09-13

### Changed

- Standardized documentation terminology and corrected typographical errors to enhance the clarity and searchability of Kubernetes, LLM, leadership, and MCP-related documentation. [702a4409](https://github.com/electrocucaracha/yt-conferences/commit/702a4409f80043ab08c491c62c1d8100aca3c10a)

## [3.0.0] - 2026-09-13

### Removed

- Simplified the formatting step by removing the requirement for Prettier formatting during the fmt target execution, allowing other tools to manage formatting instead. [224c0d7c](https://github.com/electrocucaracha/yt-conferences/commit/224c0d7ccdfb9e340d460c12c6e9f9caa434eddb)

## [2.3.0] - 2026-09-13

### Added

- Enabled spell checking tools to ignore Spanish forum documentation by adding a configuration file to skip Markdown files under the specified directory. [046d37b3](https://github.com/electrocucaracha/yt-conferences/commit/046d37b395bc893d681ef177d2da2d20c36549cc)

## [2.2.3] - 2026-09-13

### Changed

- Optimized shell scripts to use tabs consistently for improved readability and standard indentation style. [0d76ada9](https://github.com/electrocucaracha/yt-conferences/commit/0d76ada99bc8ed24a0fb76fea939fe933a4afe0a)

## [2.2.2] - 2026-09-13

### Fixed

- Simplified the truncation of Markdown titles and prose on conference session and summary pages to ensure they always end on complete words, and standardized punctuation at the end of titles and summary lines for improved readability and a more professional documentation structure. [0b98cc00](https://github.com/electrocucaracha/yt-conferences/commit/0b98cc00a98cad7789563fd6aafc509b2553b351)

## [2.2.1] - 2026-09-13

### Changed

- Clarified the project description to accurately reflect that conference videos are fetched from YouTube, ensuring users and maintainers have precise information about the project's purpose and operation. [d82b92a7](https://github.com/electrocucaracha/yt-conferences/commit/d82b92a7e7a528c0658a8d4c26c7b8b8a0b89a8f)

## [2.2.0] - 2026-09-13

### Added

- Enabled discoverability, reference, and executive-level understanding of conferences and skills documentation with the addition of executive report readme files and skill documentation for executive report generation workflow. [2f598148](https://github.com/electrocucaracha/yt-conferences/commit/2f5981486b22e7c8fe4ea2e074fb4b5167c07d15)

## [2.1.0] - 2026-09-13

### Added

- Enabled users to request conference summarization via a YouTube playlist URL by introducing a new issue template that collects necessary information and checks for playlist availability and duplicate requests. [f598b931](https://github.com/electrocucaracha/yt-conferences/commit/f598b9316d8acd58ce0276ebc6b5301098fdd1e1)

## [2.0.1] - 2026-09-13

### Changed

- Standardized documentation terminology and formatting for improved readability and consistency throughout the project. [c47880ed](https://github.com/electrocucaracha/yt-conferences/commit/c47880eda5a1304542088798b228de3cf20b3dad)

## [2.0.0] - 2026-09-13

### Removed

- Eliminated the persistence of editor-specific configuration in version control to ensure that user preferences do not impact project collaboration. [ba444eea](https://github.com/electrocucaracha/yt-conferences/commit/ba444eea0bc0c661682d7e4796144388eadf8412)

## [1.1.1] - 2026-09-13

### Changed

- `configure_qmd.sh` can now be directly invoked without manual permission changes. [24777751](https://github.com/electrocucaracha/yt-conferences/commit/24777751b598771d3b37a986832a952d49b50ef6)

## [1.1.0] - 2026-09-12

### Added

- Introduced standardized YAML front matter to all documentation files, enabling improved navigation, automated doc tooling, and better maintainability for the documentation set. [aba17b20](https://github.com/electrocucaracha/yt-conferences/commit/aba17b20f20e16ddf3935dfceea461f9789678b0)

## [1.0.3] - 2026-09-12

### Changed

- Normalized linter configurations and workflow files to support tables and semantic line breaks in Markdown, allow multiple top-level headings and sequential ordered list numbering, and ensure consistent line endings in YAML and workflow files. [15b5a44a](https://github.com/electrocucaracha/yt-conferences/commit/15b5a44a7277551fe203c7a70f93db5ca49926a3)

## [1.0.2] - 2026-09-12

### Changed

- Improved error messages and formatting are now provided for OKF documents through enhanced parsing and reformatting of frontmatter and summary content. [647f026f](https://github.com/electrocucaracha/yt-conferences/commit/647f026f8ffc34674addbd42123626f9e1c6e15a)

## [1.0.1] - 2026-09-12

### Fixed

- Stabilized compatibility with POSIX tools and text utilities by ensuring the .pre-commit-config.yaml file now consistently ends with a newline character. [cc9817e5](https://github.com/electrocucaracha/yt-conferences/commit/cc9817e59b16356e068c85325bda0b1e74b1f76e)

## [1.0.0] - 2026-09-12

### Added

- Established a structured knowledge base for the YouTube Conference Knowledge project, utilizing Open Knowledge Format (OKF) v0.2, with content organized by conference and subject areas. [632af56f](https://github.com/electrocucaracha/yt-conferences/commit/632af56f219491f5223d4e5070b06b77691bcbf1)
