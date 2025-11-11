#!/usr/bin/env python3
"""Basic checks to ensure the static electricity learning hub loads expected content."""
from __future__ import annotations

import sys
from pathlib import Path


def main() -> int:
    project_root = Path(__file__).resolve().parents[1]
    html_path = project_root / "index.html"

    if not html_path.exists():
        print("::error::index.html not found at repository root", file=sys.stderr)
        return 1

    content = html_path.read_text(encoding="utf-8")

    checks = {
        "page title": "<title>IGCSE Physics - Electricity Interactive Learning Hub</title>" in content,
        "navigation tabs": "class=\"nav-tabs\"" in content,
        "calculator script": "function performCalculation()" in content,
        "quiz data": "const quizQuestions" in content,
        "window onload hook": "window.onload" in content,
    }

    failed = False
    for name, passed in checks.items():
        if passed:
            print(f"::notice::{name} check passed")
        else:
            failed = True
            print(f"::error::{name} check failed", file=sys.stderr)

    return 0 if not failed else 2


if __name__ == "__main__":
    raise SystemExit(main())
