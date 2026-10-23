#!/usr/bin/env python3
"""Validate local documentation links and the 30-milestone learning graph.

This is a structural check. It does not evaluate scientific truth, pedagogical
quality, external websites, or the contents of the cryptographic assumption.
"""

from __future__ import annotations

import argparse
from collections import Counter
import html
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


REPOSITORY = Path(__file__).resolve().parent.parent
MILESTONE_HEADING = re.compile(r"^### M(\d{2})\b[^\n]*", re.MULTILINE)


def without_fences(text):
    lines = []
    fence = None
    for line in text.splitlines():
        match = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if match:
            marker = match.group(1)
            if fence is None:
                fence = marker[0]
            elif marker[0] == fence:
                fence = None
            lines.append("")
        else:
            lines.append(line if fence is None else "")
    return "\n".join(lines)


def heading_anchors(text):
    """GitHub-style slugs for the simple headings used in this repository."""
    anchors = set(re.findall(r'<a\s+(?:[^>]*?\s)?id=["\']([^"\']+)["\']', text))
    duplicates = Counter()
    for line in without_fences(text).splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if not match:
            continue
        title = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", match.group(1))
        title = re.sub(r"<[^>]*>", "", html.unescape(title)).lower()
        slug = re.sub(r"[^\w\- ]", "", title, flags=re.UNICODE).replace(" ", "-")
        number = duplicates[slug]
        duplicates[slug] += 1
        anchors.add(slug if number == 0 else f"{slug}-{number}")
    return anchors


def local_links(text):
    text = without_fences(text)
    # All repository link paths use plain filenames without parentheses.
    # External URL content is deliberately outside this check's scope.
    for match in re.finditer(r"\[[^\]\n]*\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+[^)]*)?\)", text):
        yield match.group(1).strip("<>")
    for match in re.finditer(r"^\s*\[[^\]]+\]:\s*(<[^>]+>|\S+)", text, re.MULTILINE):
        yield match.group(1).strip("<>")


def check_repository(root=REPOSITORY):
    root = root.resolve()
    documents = sorted(path for path in root.rglob("*.md") if ".git" not in path.parts)
    if (root / "llms.txt").exists():
        documents.append(root / "llms.txt")
    text_by_path = {path: path.read_text(encoding="utf-8") for path in documents}
    anchors = {path: heading_anchors(text) for path, text in text_by_path.items()}
    errors = []
    local_count = anchor_count = 0
    for source, text in text_by_path.items():
        for target in local_links(text):
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            if parsed.path.startswith("/"):
                destination = (root / unquote(parsed.path).lstrip("/")).resolve()
            else:
                destination = (source.parent / unquote(parsed.path)).resolve() if parsed.path else source
            local_count += 1
            origin = str(source.relative_to(root))
            if not destination.is_relative_to(root):
                errors.append(f"{origin}: local link escapes repository: {target}")
            elif not destination.exists():
                errors.append(f"{origin}: missing local target: {target}")
            elif parsed.fragment and destination.suffix.lower() == ".md":
                anchor_count += 1
                fragment = unquote(parsed.fragment)
                if destination not in anchors:
                    anchors[destination] = heading_anchors(destination.read_text(encoding="utf-8"))
                if fragment not in anchors[destination]:
                    errors.append(f"{origin}: missing Markdown section anchor: {target}")

    milestone_file = root / "learning" / "MILESTONES.md"
    milestone_count = dependency_count = 0
    background_count = narrative_count = 0
    if not milestone_file.exists():
        errors.append("learning/MILESTONES.md is missing")
    else:
        text = without_fences(milestone_file.read_text(encoding="utf-8"))
        headings = list(MILESTONE_HEADING.finditer(text))
        numbers = [int(match.group(1)) for match in headings]
        milestone_count = len(numbers)
        if numbers != list(range(1, 31)):
            errors.append("Milestone headings must be exactly M01 through M30, once each and in order")
        phase_two = re.search(r"^## Phase II\b", text, flags=re.MULTILINE)
        if phase_two is None:
            errors.append("The narrative phase heading is missing")
        else:
            background_count = sum(heading.start() < phase_two.start() for heading in headings)
            narrative_count = len(headings) - background_count
            if (background_count, narrative_count) != (15, 15):
                errors.append("The learning map must contain 15 background and 15 narrative milestones")
        for index, heading in enumerate(headings):
            number = int(heading.group(1))
            stop = headings[index + 1].start() if index + 1 < len(headings) else len(text)
            body = text[heading.end():stop]
            dependency_line = re.search(
                r"^\s*\*\*Dependencies and story role\.\*\*\s*(.*)$", body,
                flags=re.MULTILINE | re.IGNORECASE)
            if dependency_line is None:
                errors.append(f"M{number:02d} has no Dependencies and story role field")
                continue
            field = dependency_line.group(1)
            dependencies = {int(value) for value in re.findall(r"\bM(\d{2})\b", field)}
            for lower, upper in re.findall(r"\bM(\d{2})\s*[–—-]\s*(?:M)?(\d{2})\b", field):
                lower, upper = int(lower), int(upper)
                if lower > upper:
                    errors.append(f"M{number:02d} has a descending dependency range M{lower:02d}–M{upper:02d}")
                else:
                    dependencies.update(range(lower, upper + 1))
            dependency_count += len(dependencies)
            for dependency in sorted(dependencies):
                if dependency not in numbers:
                    errors.append(f"M{number:02d} refers to nonexistent dependency M{dependency:02d}")
                elif dependency >= number:
                    errors.append(f"M{number:02d} has a non-earlier dependency M{dependency:02d}")

    return {"status": "PASS" if not errors else "FAIL",
            "scope": "Local documentation structure only; no external URL fetch or scientific claim validation.",
            "markdown_documents_checked": sum(path.suffix == ".md" for path in documents),
            "llms_document_checked": (root / "llms.txt").exists(),
            "local_links_checked": local_count, "section_anchors_checked": anchor_count,
            "milestone_count": milestone_count, "background_milestones": background_count,
            "narrative_milestones": narrative_count, "earlier_dependency_edges": dependency_count,
            "errors": errors}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="also write the JSON report to this path")
    args = parser.parse_args()
    report = check_repository()
    payload = json.dumps(report, indent=2) + "\n"
    if args.output is not None:
        args.output.write_text(payload, encoding="utf-8")
    print(payload, end="")
    raise SystemExit(0 if report["status"] == "PASS" else 1)


if __name__ == "__main__":
    main()
