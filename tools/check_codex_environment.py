#!/usr/bin/env python3
"""Report local tools required by the selected Codex workflow stage."""

import argparse
import json
import shutil
import sys
from pathlib import Path


STAGES = {
    "profile": (),
    "application": ("lualatex", "xelatex", "pdfinfo", "pdftotext", "pdftoppm"),
    "pdf": ("pdfinfo", "pdftotext", "pdftoppm"),
    "search": ("bun",),
}
REQUIRED_FILES = (
    "AGENTS.md",
    "CLAUDE.md",
    ".claude/commands/setup.md",
    ".claude/commands/apply.md",
    ".claude/commands/outcome.md",
)


def check_environment(root, stage, *, which=shutil.which, version=None):
    """Return a report without running discovered programs or changing the workspace."""
    root = Path(root).resolve()
    version = sys.version_info[:3] if version is None else version
    tools = {name: which(name) for name in STAGES[stage]}
    missing_files = [name for name in REQUIRED_FILES if not (root / name).is_file()]
    missing_tools = [name for name, executable in tools.items() if executable is None]
    supported_python = tuple(version[:2]) >= (3, 10)
    return {
        "stage": stage,
        "root": str(root),
        "python": ".".join(map(str, version)),
        "supported_python": supported_python,
        "tools": tools,
        "missing_tools": missing_tools,
        "missing_files": missing_files,
        "ready": supported_python and not missing_files and not missing_tools,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage", choices=STAGES, default="application")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--json", action="store_true", help="print a machine-readable report")
    args = parser.parse_args(argv)
    report = check_environment(args.root, args.stage)
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(f"Stage: {report['stage']}")
        print(f"Python: {report['python']}")
        for name, executable in report["tools"].items():
            print(f"{name}: {executable or 'missing'}")
        for name in report["missing_files"]:
            print(f"Missing repository file: {name}")
        if not report["supported_python"]:
            print("Python 3.10 or later is required.")
        print("Ready" if report["ready"] else "Not ready")
    return 0 if report["ready"] else 1


if __name__ == "__main__":
    sys.exit(main())
