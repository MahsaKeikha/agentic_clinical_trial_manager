import json
from pathlib import Path

from orchestration.orchestrator import run_workflow


def healthy(**updates):
    case = {
        "protocol_version_current": True,
        "irb_or_ethics_approval_current": True,
        "informed_consent_complete": True,
        "eligibility_verified": True,
        "privacy_review_complete": True,
        "source_data_traceable": True,
        "audit_trail_enabled": True,
        "adverse_event_review_complete": True,
        "serious_adverse_event_escalated": True,
        "protocol_deviations_reviewed": True,
        "site_training_current": True,
        "investigational_product_accountability_complete": True,
        "data_quality_checks_passed": True,
        "monitoring_findings_resolved": True,
        "safety_committee_review_complete": True,
        "unresolved_conflicts": [],
        "unresolved_questions": [],
        "open_risks": [],
        "human_approval": True,
    }
    case.update(updates)
    return case


SCENARIOS = [
    ("healthy_trial", healthy(), "approved_for_trial_operations"),
    ("awaiting_approval", healthy(human_approval=False), "awaiting_human_approval"),
    ("consent_gap", healthy(informed_consent_complete=False), "review_required"),
    ("ethics_gap", healthy(irb_or_ethics_approval_current=False), "review_required"),
    ("sae_not_escalated", healthy(serious_adverse_event_present=True, serious_adverse_event_escalated=False), "review_required"),
    ("data_integrity_gap", healthy(source_data_traceable=False, audit_trail_enabled=False), "review_required"),
    ("deviation_gap", healthy(protocol_deviations_reviewed=False), "review_required"),
    ("open_risk", healthy(open_risks=["unresolved safety signal"]), "review_required"),
]


def main():
    rows = []
    for name, payload, expected in SCENARIOS:
        actual = run_workflow(payload)["status"]
        rows.append({"scenario": name, "expected": expected, "actual": actual, "passed": actual == expected})
    passed = sum(row["passed"] for row in rows)
    result = {
        "system_id": "F52",
        "version": "1.0.0",
        "scenario_count": len(rows),
        "passed": passed,
        "pass_rate": passed / len(rows),
        "scenarios": rows,
    }
    Path("benchmarks/heldout_results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if result["pass_rate"] != 1.0:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
