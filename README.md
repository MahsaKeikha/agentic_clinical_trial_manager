# Agentic Clinical Trial Manager

F52 in the Agentic AI Library.

A multi-agent clinical trial operations support system with separate agents, tools, skills, orchestration, memory, state, schemas, prompts, configuration, safety, observability, evaluation, benchmarks, examples, tests, and CI.

This system supports trial operations and documentation. It does not replace investigators, IRBs, sponsors, regulators, clinical judgment, or required oversight.

## Agents

- [`protocol_planner_agent.py`](AGENTS/protocol_planner_agent.py)
- [`site_coordinator_agent.py`](AGENTS/site_coordinator_agent.py)
- [`recruitment_tracker_agent.py`](AGENTS/recruitment_tracker_agent.py)
- [`data_quality_agent.py`](AGENTS/data_quality_agent.py)
- [`deviation_reviewer_agent.py`](AGENTS/deviation_reviewer_agent.py)
- [`reporting_agent.py`](AGENTS/reporting_agent.py)

## Architecture

See [`AGENTS/`](AGENTS/), [`TOOLS/`](TOOLS/), [`SKILLS/`](SKILLS/), [`orchestration/`](orchestration/), [`memory/`](memory/), [`state/`](state/), [`schemas/`](schemas/), [`prompts/`](prompts/), [`config/`](config/), [`safety/`](safety/), [`observability/`](observability/), [`evals/`](evals/), [`benchmarks/`](benchmarks/), [`examples/`](examples/), [`tests/`](tests/), and [`docs/`](docs/).
