from __future__ import annotations

from .runner import run


def current_branch(cwd: str) -> str:
    code, out, _ = run(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=cwd)
    return out.strip() if code == 0 else ""


def create_branch(name: str, cwd: str) -> bool:
    code, _, _ = run(["git", "checkout", "-b", name], cwd=cwd)
    return code == 0


def commit_all(message: str, cwd: str) -> bool:
    code, _, _ = run(["git", "add", "."], cwd=cwd)
    if code != 0:
        return False
    code, _, _ = run(["git", "commit", "-m", message], cwd=cwd)
    return code == 0
