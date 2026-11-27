#!/usr/bin/env python3
"""Validate the workflow-first-app-ui skill repository using the standard library."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = (
    ".github/workflows/validate.yml",
    "AGENTS.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "README.md",
    "SECURITY.md",
    "SKILL.md",
    "VERSION",
    "agents/openai.yaml",
    "references/component-sources.md",
    "references/design-guide.md",
    "references/development-standard.md",
    "references/existing-system-research.md",
    "references/portable-bootstrap.md",
    "references/source-audit.md",
    "references/tool-routing.md",
    "references/verification.md",
    "scripts/bootstrap_project.py",
    "scripts/install.ps1",
    "scripts/install.sh",
    "templates/CODEX_HANDOFF.md",
    "templates/PROJECT_BRIEF.md",
)

MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
SECRET_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
    "OpenAI key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "AWS access key": re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"),
}


def markdown_files() -> list[Path]:
    return sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)


def validate_required(errors: list[str]) -> None:
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")


def validate_skill(errors: list[str]) -> None:
    path = ROOT / "SKILL.md"
    if not path.is_file():
        return
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        errors.append("SKILL.md must start with YAML frontmatter")
        return
    frontmatter = match.group(1)
    if not re.search(r"^name:\s*workflow-first-app-ui\s*$", frontmatter, re.MULTILINE):
        errors.append("SKILL.md frontmatter must preserve name: workflow-first-app-ui")
    if not re.search(r"^description:\s*\S.+$", frontmatter, re.MULTILINE):
        errors.append("SKILL.md frontmatter must contain a description")
    required_links = (
        "references/development-standard.md",
        "references/existing-system-research.md",
        "references/design-guide.md",
        "references/verification.md",
        "references/portable-bootstrap.md",
        "references/tool-routing.md",
    )
    for target in required_links:
        if target not in text:
            errors.append(f"SKILL.md must route to {target}")


def validate_canonical_guidance(errors: list[str]) -> None:
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    if len(agents) > 2_000:
        errors.append("AGENTS.md must remain lightweight (2000 characters or fewer)")
    if "references/development-standard.md" not in agents:
        errors.append("AGENTS.md must point to the canonical development standard")

    standard = (ROOT / "references/development-standard.md").read_text(encoding="utf-8")
    research = (ROOT / "references/existing-system-research.md").read_text(encoding="utf-8")
    combined = f"{standard}\n{research}".lower()
    for phrase in ("before greenfield", "license", "baseline", "bounded donor"):
        if phrase not in combined:
            errors.append(f"canonical guidance is missing required research concept: {phrase}")
    for phrase in ("explicit authorization", "production deployment", "merge"):
        if phrase not in standard.lower():
            errors.append(f"canonical standard is missing release boundary: {phrase}")


def validate_links(errors: list[str]) -> None:
    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK.findall(text):
            target = raw_target.strip().split()[0].strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            relative_target = unquote(target.split("#", 1)[0])
            if relative_target and not (path.parent / relative_target).resolve().exists():
                errors.append(f"broken local link in {path.relative_to(ROOT)}: {raw_target}")


def validate_version(errors: list[str]) -> None:
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        errors.append("VERSION must contain a semantic version such as 2.0.0")
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    if f"## [{version}]" not in changelog:
        errors.append(f"CHANGELOG.md does not contain the current version {version}")


def validate_source_review(errors: list[str]) -> None:
    text = (ROOT / "references/component-sources.md").read_text(encoding="utf-8")
    if not re.search(r"Last reviewed:\s*\d{4}-\d{2}-\d{2}", text):
        errors.append("component sources must include a YYYY-MM-DD review date")


def validate_bootstrap_reference(errors: list[str]) -> None:
    bootstrap = (ROOT / "scripts/bootstrap_project.py").read_text(encoding="utf-8")
    for phrase in (
        "<!-- workflow-first-app-ui:start -->",
        "--check",
        "$workflow-first-app-ui",
    ):
        if phrase not in bootstrap:
            errors.append(f"bootstrap helper is missing required project reference: {phrase}")

    metadata = (ROOT / "agents/openai.yaml").read_text(encoding="utf-8")
    if not re.search(r"^\s*allow_implicit_invocation:\s*true\s*$", metadata, re.MULTILINE):
        errors.append("agents/openai.yaml must allow implicit invocation")


def validate_secrets(errors: list[str]) -> None:
    text_suffixes = {".md", ".ps1", ".py", ".sh", ".yaml", ".yml"}
    text_files = sorted(
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and ".git" not in path.parts
        and (path.suffix in text_suffixes or path.name == "VERSION")
    )
    for path in text_files:
        text = path.read_text(encoding="utf-8")
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                errors.append(f"possible {label} in {path.relative_to(ROOT)}")


def main() -> int:
    errors: list[str] = []
    validate_required(errors)
    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    validate_skill(errors)
    validate_canonical_guidance(errors)
    validate_links(errors)
    validate_version(errors)
    validate_source_review(errors)
    validate_bootstrap_reference(errors)
    validate_secrets(errors)

    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
