from __future__ import annotations

from dataclasses import dataclass


@dataclass
class PlanStep:
    description: str
    files: list[str] | None = None


def make_plan(goal: str) -> list[PlanStep]:
    steps: list[PlanStep] = []
    # extremely simple heuristic planner
    if any(k in goal.lower() for k in ["test", "fix", "build", "run"]):
        steps.append(PlanStep("search codebase for related symbols"))
        steps.append(PlanStep("run tests/build to reproduce"))
        steps.append(PlanStep("apply minimal edits"))
        steps.append(PlanStep("re-run tests and lint"))
    else:
        steps.append(PlanStep("search codebase for relevant modules"))
        steps.append(PlanStep("create or edit files to implement feature"))
        steps.append(PlanStep("add/adjust tests"))
        steps.append(PlanStep("run tests and lint"))
    return steps
