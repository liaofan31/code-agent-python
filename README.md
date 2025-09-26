# code-agent-python

A minimal Python code agent proof-of-concept:
- Plan tasks from a natural language goal
- Search repository via ripgrep
- Optionally run tests
- Typer CLI, Ruff/Black, Pytest, CI

## Quickstart
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m agent.cli run "add unit tests" --repo /path/to/repo
```
