#!/usr/bin/env python3
"""Safely scaffold a modular project documentation tree from bundled templates."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import sys


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", type=Path, help="Project directory to receive documentation")
    parser.add_argument("--project-name", required=True, help="Human-facing project name")
    parser.add_argument("--summary", default="TBD: describe the project purpose.")
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        help="Leave existing destination files unchanged instead of failing",
    )
    return parser.parse_args()


def render(text: str, args: argparse.Namespace) -> str:
    return (
        text.replace("{{PROJECT_NAME}}", args.project_name)
        .replace("{{PROJECT_SUMMARY}}", args.summary)
        .replace("{{DATE}}", date.today().isoformat())
    )


def main() -> int:
    args = parse_args()
    source = Path(__file__).resolve().parent.parent / "assets" / "project-docs-template"
    if not source.is_dir():
        print(f"Template directory not found: {source}", file=sys.stderr)
        return 2

    # Finder may leave binary metadata files in the bundled template. They are
    # neither documentation nor valid UTF-8 input for the rendering step.
    files = sorted(
        path
        for path in source.rglob("*")
        if path.is_file() and path.name != ".DS_Store"
    )
    conflicts = [args.target / path.relative_to(source) for path in files]
    conflicts = [path for path in conflicts if path.exists()]
    if conflicts and not args.skip_existing:
        print("Refusing to overwrite existing files:", file=sys.stderr)
        for path in conflicts:
            print(f"- {path}", file=sys.stderr)
        print("Inspect conflicts, then rerun with --skip-existing if appropriate.", file=sys.stderr)
        return 1

    created = 0
    skipped = 0
    for source_file in files:
        destination = args.target / source_file.relative_to(source)
        if destination.exists():
            skipped += 1
            continue
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(render(source_file.read_text(encoding="utf-8"), args), encoding="utf-8")
        created += 1

    print(f"Created {created} files; skipped {skipped} existing files in {args.target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
