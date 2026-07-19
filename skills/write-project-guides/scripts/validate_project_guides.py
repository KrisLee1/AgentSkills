#!/usr/bin/env python3
"""Validate release-facing Markdown guides without third-party dependencies."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlsplit


SKIP_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".tox",
    ".venv",
    "build",
    "coverage",
    "dist",
    "node_modules",
    "target",
    "vendor",
}

LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
LINK_DEFINITION_RE = re.compile(r"^\s*\[[^\]]+\]:\s*(\S+)", re.MULTILINE)
FENCE_RE = re.compile(r"^\s*(```|~~~)")
PLACEHOLDER_PATTERNS = (
    ("double-brace template marker", re.compile(r"\{\{[^{}\n]+\}\}")),
    ("TODO template marker", re.compile(r"\[(?:TODO|FIXME)(?::[^\]]*)?\]", re.I)),
    ("replacement marker", re.compile(r"\b(?:REPLACE_ME|YOUR_[A-Z0-9_]+)\b")),
    ("angle-bracket template marker", re.compile(r"<[A-Z][A-Z0-9_-]{2,}>")),
)
SECRET_PATTERNS = (
    ("AWS access key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("GitHub token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b")),
    ("private key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
    ("possible OpenAI-style secret", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b")),
    (
        "possible assigned secret",
        re.compile(
            r"(?i)\b(?:api[_-]?key|access[_-]?token|client[_-]?secret|password)\b"
            r"\s*[:=]\s*[\"']?[A-Za-z0-9_./+=-]{16,}"
        ),
    ),
)
PERSONAL_PATH_RE = re.compile(r"(?:/Users/[^/\s`]+|/home/[^/\s`]+)(?:/[^\s`]*)?")


@dataclass(frozen=True)
class Finding:
    severity: str
    path: Path
    line: int
    message: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check project Markdown for broken local links, template markers, and likely sensitive values."
    )
    parser.add_argument("project_root", type=Path, help="Project root containing the guides")
    parser.add_argument(
        "--allow-placeholders",
        action="store_true",
        help="Report unresolved template markers as warnings instead of errors",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Return a failure status when warnings are present",
    )
    return parser.parse_args()


def markdown_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*.md"):
        try:
            relative_parts = path.relative_to(root).parts
        except ValueError:
            continue
        if any(part in SKIP_DIRS for part in relative_parts):
            continue
        if path.is_file():
            files.append(path)
    return sorted(files)


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def strip_fenced_code(text: str) -> str:
    output: list[str] = []
    fence: str | None = None
    for line in text.splitlines(keepends=True):
        match = FENCE_RE.match(line)
        if match:
            marker = match.group(1)
            if fence is None:
                fence = marker
            elif marker == fence:
                fence = None
            output.append("\n")
        elif fence is None:
            output.append(line)
        else:
            output.append("\n")
    return "".join(output)


def split_link_destination(raw: str) -> str:
    value = raw.strip()
    if value.startswith("<") and ">" in value:
        return value[1 : value.index(">")]
    # Markdown permits an optional title after whitespace. Project paths with
    # spaces should use angle brackets, so the first token is the destination.
    return value.split(maxsplit=1)[0] if value else ""


def local_link_target(source: Path, root: Path, destination: str) -> tuple[Path | None, str]:
    parsed = urlsplit(destination)
    if parsed.scheme or parsed.netloc or destination.startswith(("mailto:", "data:")):
        return None, ""
    fragment = unquote(parsed.fragment)
    path_text = unquote(parsed.path)
    if not path_text:
        return source, fragment
    if path_text.startswith("/"):
        return root / path_text.lstrip("/"), fragment
    return source.parent / path_text, fragment


def github_slug(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value.strip().lower())
    value = re.sub(r"[^\w\- ]", "", value, flags=re.UNICODE)
    return re.sub(r"[\s-]+", "-", value).strip("-")


def heading_anchors(path: Path) -> set[str]:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return set()
    counts: dict[str, int] = {}
    anchors: set[str] = set()
    in_fence = False
    fence = ""
    for line in text.splitlines():
        match = FENCE_RE.match(line)
        if match:
            marker = match.group(1)
            if not in_fence:
                in_fence, fence = True, marker
            elif marker == fence:
                in_fence, fence = False, ""
            continue
        if in_fence:
            continue
        heading = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if not heading:
            continue
        base = github_slug(heading.group(1))
        if not base:
            continue
        count = counts.get(base, 0)
        anchors.add(base if count == 0 else f"{base}-{count}")
        counts[base] = count + 1
    return anchors


def inspect_file(path: Path, root: Path, allow_placeholders: bool) -> list[Finding]:
    findings: list[Finding] = []
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return [Finding("ERROR", path, 1, "file is not valid UTF-8")]
    except OSError as exc:
        return [Finding("ERROR", path, 1, f"could not read file: {exc}")]

    prose = strip_fenced_code(text)
    for label, pattern in PLACEHOLDER_PATTERNS:
        for match in pattern.finditer(text):
            severity = "WARN" if allow_placeholders else "ERROR"
            findings.append(Finding(severity, path, line_number(text, match.start()), label))

    for label, pattern in SECRET_PATTERNS:
        for match in pattern.finditer(text):
            findings.append(Finding("WARN", path, line_number(text, match.start()), label))
    for match in PERSONAL_PATH_RE.finditer(text):
        findings.append(
            Finding("WARN", path, line_number(text, match.start()), "possible personal absolute path")
        )

    link_matches = [(match, match.group(1)) for match in LINK_RE.finditer(prose)]
    link_matches.extend((match, match.group(1)) for match in LINK_DEFINITION_RE.finditer(prose))
    for match, raw_destination in link_matches:
        destination = split_link_destination(raw_destination)
        if not destination:
            continue
        target, fragment = local_link_target(path, root, destination)
        if target is None:
            continue
        resolved = target.resolve(strict=False)
        try:
            resolved.relative_to(root)
        except ValueError:
            findings.append(
                Finding(
                    "WARN",
                    path,
                    line_number(prose, match.start()),
                    f"local link points outside project: {destination}",
                )
            )
            continue
        if not resolved.exists():
            findings.append(
                Finding(
                    "ERROR",
                    path,
                    line_number(prose, match.start()),
                    f"broken local link: {destination}",
                )
            )
            continue
        if fragment and resolved.is_file() and resolved.suffix.lower() == ".md":
            anchors = heading_anchors(resolved)
            normalized = github_slug(fragment)
            if normalized and normalized not in anchors:
                findings.append(
                    Finding(
                        "WARN",
                        path,
                        line_number(prose, match.start()),
                        f"heading anchor was not found: {destination}",
                    )
                )
    return findings


def main() -> int:
    args = parse_args()
    root = args.project_root.expanduser().resolve()
    if not root.is_dir():
        print(f"ERROR: project root is not a directory: {root}", file=sys.stderr)
        return 2

    files = markdown_files(root)
    if not files:
        print(f"ERROR: no Markdown files found under {root}", file=sys.stderr)
        return 2

    findings: list[Finding] = []
    for path in files:
        findings.extend(inspect_file(path, root, args.allow_placeholders))

    for finding in findings:
        relative = finding.path.relative_to(root)
        print(f"{finding.severity}: {relative}:{finding.line}: {finding.message}")

    errors = sum(item.severity == "ERROR" for item in findings)
    warnings = sum(item.severity == "WARN" for item in findings)
    print(f"Checked {len(files)} Markdown file(s): {errors} error(s), {warnings} warning(s).")
    if errors or (args.strict and warnings):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
