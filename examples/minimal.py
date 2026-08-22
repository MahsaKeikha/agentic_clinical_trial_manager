from orchestration.orchestrator import run_workflow

result = run_workflow({})
assert result["status"] == "review_required"
print(result["status"], result["blockers"][:3])
