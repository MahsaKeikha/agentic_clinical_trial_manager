# Agentic Clinical Trial Manager

F52 standalone multi-agent clinical trial operations support system.

## Agents

- [`protocol_planner_agent.py`](AGENTS/protocol_planner_agent.py)
- [`site_coordinator_agent.py`](AGENTS/site_coordinator_agent.py)
- [`recruitment_tracker_agent.py`](AGENTS/recruitment_tracker_agent.py)
- [`data_quality_agent.py`](AGENTS/data_quality_agent.py)
- [`deviation_reviewer_agent.py`](AGENTS/deviation_reviewer_agent.py)
- [`reporting_agent.py`](AGENTS/reporting_agent.py)

## Tools

- [`protocol_checker.py`](TOOLS/protocol_checker.py)
- [`site_status_tool.py`](TOOLS/site_status_tool.py)
- [`recruitment_metrics.py`](TOOLS/recruitment_metrics.py)
- [`data_quality_checker.py`](TOOLS/data_quality_checker.py)
- [`deviation_log.py`](TOOLS/deviation_log.py)

## Skills

- [`protocol_planning.py`](SKILLS/protocol_planning.py)
- [`site_coordination.py`](SKILLS/site_coordination.py)
- [`recruitment_tracking.py`](SKILLS/recruitment_tracking.py)
- [`data_review.py`](SKILLS/data_review.py)
- [`deviation_review.py`](SKILLS/deviation_review.py)

Supporting layers include orchestration, memory, state, schemas, prompts, config, safety, observability, evals, benchmarks, examples, tests, docs, and CI.

This system supports operations and documentation. It does not replace investigators, IRBs, sponsors, regulators, or required clinical oversight.
