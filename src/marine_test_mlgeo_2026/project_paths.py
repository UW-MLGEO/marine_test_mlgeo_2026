"""Helpers for repository path conventions."""


def project_layout() -> tuple[str, str, str]:
    """Return required top-level directories for this project."""
    return ("data", "src", "outputs")
