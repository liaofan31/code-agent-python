from agent.core.planner import make_plan


def test_make_plan_generates_steps():
    steps = make_plan("add tests for login")
    assert len(steps) >= 3
    assert any("search" in s.description for s in steps)
