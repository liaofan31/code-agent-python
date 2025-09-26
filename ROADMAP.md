# Roadmap (Next Iterations)

## 1) Retrieval & Context
- Add AST + ctags index; cross-ref (defs/uses) search
- Hybrid retrieval: ripgrep + embeddings (optional) with re-ranking
- Context packer: chunking by symbols; trimmed diffs for LLM prompts

## 2) Minimal, Safe Edits
- Structured edit API: locate-span -> apply -> format -> verify
- Generate unified diffs and change summaries
- Guardrails: edit budget per file; block secrets /.env; path allowlist

## 3) Execution & Verification
- Build/Test gates per language (py, js/ts, go); command registry
- Automatic error parsing and fix-loop (2–3 iterations)
- Flaky test isolate & rerun policy

## 4) Git Workflow Automation
- Branch naming + conventional commits
- Auto PR creation with template body and checklist
- Risk notes & rollback steps

## 5) Observability & UX
- Rich TUI progress; timing + step logs
- Telemetry toggle; run-id artifacts (logs, diffs, reports)

## 6) Advanced Planning
- Task graph (parallelizable vs. sequential)
- Cost/benefit estimator; fallback strategies
- Memory: per-file synopsis + PR history recall

## 7) Optional Integrations
- GitHub App (checks + comments)
- Issue/PR templates and labels
- Anthropic/OpenAI provider adapter (pluggable)
