<!-- Markdownlint-disable MD024 -->

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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

- configure_qmd.sh can now be directly invoked without manual permission changes. [24777751](https://github.com/electrocucaracha/yt-conferences/commit/24777751b598771d3b37a986832a952d49b50ef6)

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
