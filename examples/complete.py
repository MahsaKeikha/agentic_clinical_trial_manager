from orchestration.orchestrator import run_workflow

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
result = run_workflow(case)
assert result["status"] == "approved_for_trial_operations"
print(result["status"], result["analyses"].keys())
