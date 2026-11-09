"""Command-line entry point for the release demo."""

import platform

from hello.greeting import VERSION, build_info, greeting


def main() -> None:
    """Print greeting and application build details."""
    print(greeting())
    print(build_info(VERSION, platform.system(), platform.machine()))


if __name__ == "__main__":
    main()
