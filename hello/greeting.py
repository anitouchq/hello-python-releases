"""Greeting and build information helpers."""

VERSION = "1.0.0"


def greeting() -> str:
    """Return the application greeting."""
    return "Hello from Python Releases! 🐍"


def build_info(version: str, operating_system: str, architecture: str) -> str:
    """Format version and target platform details."""
    return (
        f"Version: {version}\n"
        f"OS: {operating_system}\n"
        f"Architecture: {architecture}"
    )
