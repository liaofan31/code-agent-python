from __future__ import annotations

import subprocess
from typing import Sequence


def run(cmd: Sequence[str], cwd: str | None = None, timeout: int = 600) -> tuple[int, str, str]:
    proc = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout)
    return proc.returncode, proc.stdout, proc.stderr
