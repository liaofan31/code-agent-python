from __future__ import annotations

import subprocess
from pathlib import Path


def ripgrep(
    pattern: str, root: str | Path = ".", globs: list[str] | None = None, head: int = 2000
) -> str:
    cmd = ["rg", "--line-number", "--no-heading", "--color", "never", pattern, str(root)]
    if globs:
        for g in globs:
            cmd.extend(["--glob", g])
    try:
        out = subprocess.run(cmd, check=False, capture_output=True, text=True)
        text = out.stdout.strip()
        return "\n".join(text.splitlines()[:head])
    except FileNotFoundError:
        return "ripgrep (rg) not installed"
