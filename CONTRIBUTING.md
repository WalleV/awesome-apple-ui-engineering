# Contributing

Thank you for helping improve Awesome Apple UI Engineering. This project is curated rather than exhaustive: every entry should help an engineer make a production UI decision, not merely point to a popular project.

## Ways to Contribute

- Suggest a resource that closes a clear coverage gap.
- Correct a description, requirement, platform, or license.
- Report a broken link, archived project, or superseded recommendation.
- Improve the contribution process or validation tooling.

Use the repository's issue forms for suggestions and corrections. A pull request is welcome when the proposed wording and supporting evidence are already clear.

## Selection Criteria

Before proposing a resource, read the [Selection Policy](README.md#selection-policy) and confirm that the resource:

- solves a specific SwiftUI, UIKit, AppKit, or Apple-platform UI engineering problem;
- has authoritative documentation or a first-party project page;
- provides an identifiable license when code is distributed;
- remains usable with current Apple-platform development;
- adds a distinct engineering decision, rather than duplicating an existing entry; and
- is not being proposed solely because of stars, novelty, or visual appeal.

Stable, finished projects do not need frequent commits. Conversely, recent activity alone is not evidence that a resource belongs in the guide.

## Entry Format

Use the existing README format:

```md
- [Resource Name](https://example.com) — A concise description.
  - **Use when:** The concrete engineering situation it fits.
  - **Watch for:** The main trade-off, constraint, or availability caveat.
  - **Metadata:** `Frameworks: SwiftUI, UIKit` · `Platforms: iOS, iPadOS` · `Requirements: iOS 17+` · `License: MIT`
```

Metadata fields must remain in this order: **Frameworks → Platforms → Requirements → License**. Omit a field when it does not apply or cannot be verified. Topics, resource formats, publication years, and provenance such as “Apple Sample Code” belong in the prose, not in the license field.

## Evidence and Licensing

- Use canonical first-party URLs whenever possible.
- For distributed code, name the exact upstream license and link to its license file or official licensing page in the issue or pull request.
- Do not infer a license from repository visibility or from a package registry alone.
- Disclose if you, your employer, or a client maintains or benefits from the proposed resource.
- By contributing original text, you agree that it may be distributed under this repository's [CC BY 4.0 license](LICENSE).

## Pull Requests

Prefer one resource per pull request so its purpose and evidence remain easy to review. Related corrections or coordinated editorial updates may be grouped when separating them would make the change harder to understand.

A pull request should:

1. explain the engineering gap or factual problem;
2. include canonical source and license evidence where applicable;
3. preserve the entry structure and metadata order;
4. avoid duplicate URLs and overlapping recommendations; and
5. pass all repository checks.

Do not add maintenance-only audit fields, dates, candidate labels, or internal lists to the README. Maintenance decisions belong in issue and pull-request discussion, not in user-facing entries.
