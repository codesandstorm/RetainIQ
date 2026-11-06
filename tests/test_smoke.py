"""Smoke test: the package imports and exposes a version."""

import retainiq


def test_package_imports() -> None:
    assert retainiq.__version__ == "0.1.0"
