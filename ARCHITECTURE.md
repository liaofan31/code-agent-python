# Architecture Overview

- CLI (Typer) → Orchestrator → Tools
- Tools: search (rg), fs (read/write/edit), runner (subprocess), git (wrappers)
- Planner: heuristic step generator → produces ordered steps
- Orchestrator executes: show plan → search → optional test run

Next: retrieval index, structured edits, gates, PR automation.
