from __future__ import annotations

from pathlib import Path


def read(path: str | Path) -> str:
    p = Path(path)
    return p.read_text(encoding="utf-8")


def write(path: str | Path, content: str) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")


def apply_edit(path: str | Path, find: str, replace: str) -> int:
    """Replace first occurrence; return number of changes (0/1)."""
    text = read(path)
    if find not in text:
        return 0
    write(path, text.replace(find, replace, 1))
    return 1
