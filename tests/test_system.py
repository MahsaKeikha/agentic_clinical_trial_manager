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


def test_healthy_trial_operation_requires_human_authority():
    result = run_workflow(healthy())
    assert result["status"] == "approved_for_trial_operations"
    assert result["blockers"] == []
    assert len(result["analyses"]) == 6


def test_human_approval_required_after_gates_clear():
    result = run_workflow(healthy(human_approval=False))
    assert result["status"] == "awaiting_human_approval"


def test_consent_and_ethics_fail_closed():
    result = run_workflow(healthy(informed_consent_complete=False, irb_or_ethics_approval_current=False))
    assert result["status"] == "review_required"
    assert "consent_incomplete" in result["blockers"]
    assert "ethics_approval_not_current" in result["blockers"]


def test_serious_adverse_event_requires_escalation():
    result = run_workflow(healthy(serious_adverse_event_present=True, serious_adverse_event_escalated=False))
    assert result["status"] == "review_required"
    assert "serious_adverse_event_not_escalated" in result["blockers"]


def test_data_and_audit_integrity_fail_closed():
    result = run_workflow(healthy(source_data_traceable=False, audit_trail_enabled=False, data_quality_checks_passed=False))
    assert "source_data_not_traceable" in result["blockers"]
    assert "audit_trail_missing" in result["blockers"]
    assert "data_quality_checks_failed" in result["blockers"]


def test_human_approval_cannot_override_open_risk():
    result = run_workflow(healthy(open_risks=["unresolved safety signal"], human_approval=True))
    assert result["status"] == "review_required"
    assert "open_trial_risk" in result["blockers"]
