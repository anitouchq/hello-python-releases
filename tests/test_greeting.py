"""Tests for the greeting helpers."""

from hello.greeting import VERSION, build_info, greeting


def test_greeting_is_not_empty() -> None:
    assert "Python" in greeting()


def test_build_info_contains_version_and_platform() -> None:
    result = build_info(VERSION, "Linux", "x86_64")

    assert "Version: 1.0.0" in result
    assert "OS: Linux" in result
    assert "Architecture: x86_64" in result
