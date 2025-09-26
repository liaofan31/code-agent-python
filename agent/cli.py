from __future__ import annotations

import typer
from rich.console import Console

from .core.orchestrator import Orchestrator

app = typer.Typer(help="Code Agent - minimal Python agent for code tasks")
console = Console()


@app.command()
def run(goal: str, repo: str = typer.Option(".", help="Path to repository")):
    orch = Orchestrator(repo_root=repo)
    orch.run_goal(goal)


if __name__ == "__main__":
    app()
