from __future__ import annotations

from dataclasses import dataclass

from rich.console import Console

from ..tools import runner as t_run
from ..tools import search as t_search
from .planner import PlanStep, make_plan

console = Console()


@dataclass
class Orchestrator:
    repo_root: str

    def run_goal(self, goal: str) -> list[PlanStep]:
        steps = make_plan(goal)
        console.rule(f"Plan for: {goal}")
        for idx, s in enumerate(steps, 1):
            console.print(f"[bold]{idx}. {s.description}[/bold]")
        # demo: execute limited subset deterministically
        for s in steps:
            if s.description.startswith("search"):
                out = t_search.ripgrep(goal.split()[0], root=self.repo_root)
                console.print(f"Search result (truncated):\n{out[:500]}")
            elif s.description.startswith("run tests") or "build" in s.description:
                code, out, err = t_run.run(["pytest", "-q"], cwd=self.repo_root)
                console.print(f"tests exit={code}\n{out}\n{err}")
                break
        return steps
