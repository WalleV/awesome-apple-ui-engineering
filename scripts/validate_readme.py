#!/usr/bin/env python3
"""Validate the public catalog structure in README.md."""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path


README_PATH = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("README.md")
AXIS_ORDER = ("Frameworks", "Platforms", "Requirements", "License")
NON_RESOURCE_SECTIONS = {"Contents", "Start Here", "Selection Policy", "License"}
PLACEHOLDER_RE = re.compile(r"^(?:TBD|TODO|Unknown|N/A|—)$", re.IGNORECASE)
RESOURCE_RE = re.compile(
    r"^- \[([^\]]+)\]\((https://[^)\s]+)\) — (\S.*)$"
)
FIELD_PATTERNS = {
    "Use when": re.compile(r"^  - \*\*Use when:\*\* (\S.*)$"),
    "Watch for": re.compile(r"^  - \*\*Watch for:\*\* (\S.*)$"),
    "Metadata": re.compile(r"^  - \*\*Metadata:\*\* (\S.*)$"),
}
MAINTENANCE_MARKERS = (
    re.compile(r"^#{1,6}\s+Watchlist\b", re.IGNORECASE),
    re.compile(
        r"^\s*(?:[-*]\s*)?\*\*(?:Status|Reviewed|Review date|Last reviewed):\*\*",
        re.IGNORECASE,
    ),
    re.compile(
        r"^\s*(?:Status|Reviewed|Review date|Last reviewed):",
        re.IGNORECASE,
    ),
    re.compile(r"\bv\d+(?:\.\d+)*\s+candidate\b", re.IGNORECASE),
)


@dataclass
class Entry:
    line: int
    section: str
    title: str
    url: str
    description: str
    body: list[tuple[int, str]] = field(default_factory=list)


def github_slug(heading: str) -> str:
    """Approximate GitHub's heading slug for the headings used by this guide."""
    value = re.sub(r"<[^>]+>", "", heading).strip().lower()
    value = re.sub(r"[^\w\- ]", "", value)
    return re.sub(r"\s+", "-", value)


def collect_entries(lines: list[str], errors: list[str]) -> list[Entry]:
    entries: list[Entry] = []
    current_section = ""
    current_entry: Entry | None = None

    for line_number, line in enumerate(lines, start=1):
        heading = re.match(r"^## (.+)$", line)
        if heading:
            current_section = heading.group(1).strip()
            current_entry = None
            continue

        resource = RESOURCE_RE.match(line)
        if resource and current_section not in NON_RESOURCE_SECTIONS:
            current_entry = Entry(
                line=line_number,
                section=current_section,
                title=resource.group(1).strip(),
                url=resource.group(2).strip(),
                description=resource.group(3).strip(),
            )
            entries.append(current_entry)
            continue

        if (
            current_section not in NON_RESOURCE_SECTIONS
            and re.match(r"^- \[[^\]]+\]\(https?://", line)
            and not resource
        ):
            errors.append(
                f"line {line_number}: malformed resource entry; use an HTTPS URL "
                "and an em dash before the description"
            )
            current_entry = None
            continue

        if current_entry is not None:
            current_entry.body.append((line_number, line))

    return entries


def validate_entry(entry: Entry, errors: list[str]) -> None:
    label = f"line {entry.line} ({entry.title})"
    if not entry.section:
        errors.append(f"{label}: resource is not inside a level-two section")
    if PLACEHOLDER_RE.fullmatch(entry.description):
        errors.append(f"{label}: description is a placeholder")

    values: dict[str, list[tuple[int, str]]] = {name: [] for name in FIELD_PATTERNS}
    for line_number, line in entry.body:
        for name, pattern in FIELD_PATTERNS.items():
            match = pattern.match(line)
            if match:
                values[name].append((line_number, match.group(1).strip()))

    for name, matches in values.items():
        if len(matches) != 1:
            errors.append(f"{label}: expected exactly one {name} field, found {len(matches)}")
        elif PLACEHOLDER_RE.fullmatch(matches[0][1]):
            errors.append(f"line {matches[0][0]} ({entry.title}): {name} is a placeholder")

    if len(values["Metadata"]) != 1:
        return

    metadata_line, metadata = values["Metadata"][0]
    fields = re.findall(r"`(Frameworks|Platforms|Requirements|License): ([^`]+)`", metadata)
    residue = re.sub(
        r"`(?:Frameworks|Platforms|Requirements|License): [^`]+`",
        "",
        metadata,
    )
    residue = re.sub(r"[·\s]", "", residue)

    if not fields or residue:
        errors.append(
            f"line {metadata_line} ({entry.title}): malformed metadata; "
            "use labeled code spans separated by ·"
        )
        return

    names = [name for name, _ in fields]
    positions = [AXIS_ORDER.index(name) for name in names]
    if positions != sorted(set(positions)):
        errors.append(
            f"line {metadata_line} ({entry.title}): metadata fields are duplicated "
            "or out of Frameworks → Platforms → Requirements → License order"
        )

    for name, value in fields:
        if not value.strip() or PLACEHOLDER_RE.fullmatch(value.strip()):
            errors.append(f"line {metadata_line} ({entry.title}): {name} has no value")


def validate_anchors(lines: list[str], errors: list[str]) -> None:
    headings = {
        github_slug(match.group(1))
        for line in lines
        if (match := re.match(r"^##+ (.+)$", line))
    }
    for line_number, line in enumerate(lines, start=1):
        for anchor in re.findall(r"\]\(#([^)]+)\)", line):
            if anchor not in headings:
                errors.append(f"line {line_number}: internal anchor #{anchor} has no heading")


def main() -> int:
    if not README_PATH.is_file():
        print("README.md was not found", file=sys.stderr)
        return 1

    lines = README_PATH.read_text(encoding="utf-8").splitlines()
    errors: list[str] = []

    required_headings = {
        "Contents",
        "Start Here",
        "Selection Policy",
        "License",
    }
    headings = {
        match.group(1).strip()
        for line in lines
        if (match := re.match(r"^## (.+)$", line))
    }
    for heading in sorted(required_headings - headings):
        errors.append(f"missing required section: {heading}")

    for line_number, line in enumerate(lines, start=1):
        for marker in MAINTENANCE_MARKERS:
            if marker.search(line):
                errors.append(
                    f"line {line_number}: maintenance-only audit metadata "
                    "must not appear in the public README"
                )
                break

    entries = collect_entries(lines, errors)
    if not entries:
        errors.append("README.md contains no catalog resources")

    seen_titles: dict[str, int] = {}
    seen_urls: dict[str, int] = {}
    for entry in entries:
        validate_entry(entry, errors)

        title_key = entry.title.casefold()
        if title_key in seen_titles:
            errors.append(
                f"line {entry.line} ({entry.title}): duplicate title; "
                f"first used on line {seen_titles[title_key]}"
            )
        else:
            seen_titles[title_key] = entry.line

        if entry.url in seen_urls:
            errors.append(
                f"line {entry.line} ({entry.title}): duplicate URL; "
                f"first used on line {seen_urls[entry.url]}"
            )
        else:
            seen_urls[entry.url] = entry.line

    validate_anchors(lines, errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"Validation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1

    print(f"Validated {len(entries)} resources across {len({e.section for e in entries})} sections.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
