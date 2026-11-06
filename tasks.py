"""RetainIQ task runner (standard library only).

Usage:
    uv run python tasks.py <target>

Every Python tool is invoked as `uv run python -m <tool>` because Windows
Application Control on the development machine blocks the generated .exe
console-script launchers. The Makefile is only a thin wrapper around this file.
"""

from __future__ import annotations

import argparse
import shlex
import subprocess
import sys
from collections.abc import Callable, Sequence

Command = Sequence[str]

UV_PY: tuple[str, ...] = ("uv", "run", "python", "-m")

TEST: Command = (*UV_PY, "pytest")
LINT: Command = (*UV_PY, "ruff", "check", ".")
FORMAT: Command = (*UV_PY, "ruff", "format", ".")
FORMAT_CHECK: Command = (*UV_PY, "ruff", "format", "--check", ".")
TYPECHECK: Command = (*UV_PY, "mypy")


def run(commands: Sequence[Command]) -> int:
    """Run commands in order, printing each first. Stop at the first failure."""
    for command in commands:
        print(f"$ {shlex.join(command)}", flush=True)
        code = subprocess.call(list(command))
        if code != 0:
            print(f"FAILED (exit {code}): {shlex.join(command)}", file=sys.stderr, flush=True)
            return code
    return 0


def not_implemented(target: str, phase: int) -> Callable[[], int]:
    def _target() -> int:
        print(f"{target}: not implemented yet — phase {phase}", flush=True)
        return 1

    return _target


TARGETS: dict[str, Callable[[], int]] = {
    "setup": lambda: run([("uv", "sync")]),
    "test": lambda: run([TEST]),
    "lint": lambda: run([LINT]),
    "format": lambda: run([FORMAT]),
    "typecheck": lambda: run([TYPECHECK]),
    "all-checks": lambda: run([TEST, LINT, FORMAT_CHECK, TYPECHECK]),
    "data": not_implemented("data", 1),
    "train": not_implemented("train", 2),
    "evaluate": not_implemented("evaluate", 2),
    "serve": not_implemented("serve", 4),
}


def main(argv: Sequence[str] | None = None) -> int:
    # Windows consoles default to a legacy code page; force UTF-8 so output is not garbled.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="RetainIQ task runner")
    parser.add_argument("target", choices=sorted(TARGETS), help="task to run")
    args = parser.parse_args(argv)
    return TARGETS[args.target]()


if __name__ == "__main__":
    sys.exit(main())
