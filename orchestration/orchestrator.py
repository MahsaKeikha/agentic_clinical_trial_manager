from __future__ import annotations

from copy import deepcopy
from typing import Any

from AGENTS.data_quality_agent import DataQualityAgent
from AGENTS.deviation_reviewer_agent import DeviationReviewerAgent
from AGENTS.protocol_planner_agent import ProtocolPlannerAgent
from AGENTS.recruitment_tracker_agent import RecruitmentTrackerAgent
from AGENTS.reporting_agent import ReportingAgent
from AGENTS.site_coordinator_agent import SiteCoordinatorAgent


AGENTS = [
    ProtocolPlannerAgent(),
    SiteCoordinatorAgent(),
    RecruitmentTrackerAgent(),
    DataQualityAgent(),
    DeviationReviewerAgent(),
    ReportingAgent(),
]


def run_workflow(context: dict[str, Any]) -> dict[str, Any]:
    state = _normalize(context)
    analyses = {agent.name: agent.run(state) for agent in AGENTS}
    blockers = _blockers(state)
    if blockers:
        status = "review_required"
    elif state["human_approval"]:
        status = "approved_for_trial_operations"
    else:
        status = "awaiting_human_approval"
    return {
        "system_id": "F52",
        "system_name": "Clinical Trial Manager",
        "version": "1.0.0",
        "maturity": "L3 Gold Standard",
        "scope": "research-operations decision support only",
        "analyses": analyses,
        "state": state,
        "blockers": blockers,
        "status": status,
        "human_authority": "Qualified investigators, sponsors, IRBs/ethics committees, DSMBs where applicable, and authorized site personnel retain decision authority.",
    }


def _normalize(context: dict[str, Any]) -> dict[str, Any]:
    state = deepcopy(context)
    defaults = {
        "protocol_version_current": False,
        "irb_or_ethics_approval_current": False,
        "informed_consent_complete": False,
        "eligibility_verified": False,
        "privacy_review_complete": False,
        "source_data_traceable": False,
        "audit_trail_enabled": False,
        "adverse_event_review_complete": False,
        "serious_adverse_event_escalated": True,
        "protocol_deviations_reviewed": False,
        "site_training_current": False,
        "investigational_product_accountability_complete": False,
        "data_quality_checks_passed": False,
        "monitoring_findings_resolved": False,
        "safety_committee_review_complete": True,
        "unresolved_conflicts": [],
        "unresolved_questions": [],
        "open_risks": [],
        "human_approval": False,
    }
    for key, value in defaults.items():
        state.setdefault(key, value)
    return state


def _blockers(state: dict[str, Any]) -> list[str]:
    checks = {
        "protocol_not_current": state["protocol_version_current"],
        "ethics_approval_not_current": state["irb_or_ethics_approval_current"],
        "consent_incomplete": state["informed_consent_complete"],
        "eligibility_not_verified": state["eligibility_verified"],
        "privacy_review_incomplete": state["privacy_review_complete"],
        "source_data_not_traceable": state["source_data_traceable"],
        "audit_trail_missing": state["audit_trail_enabled"],
        "adverse_event_review_incomplete": state["adverse_event_review_complete"],
        "protocol_deviation_review_incomplete": state["protocol_deviations_reviewed"],
        "site_training_not_current": state["site_training_current"],
        "ip_accountability_incomplete": state["investigational_product_accountability_complete"],
        "data_quality_checks_failed": state["data_quality_checks_passed"],
        "monitoring_findings_unresolved": state["monitoring_findings_resolved"],
        "safety_committee_review_incomplete": state["safety_committee_review_complete"],
    }
    blockers = [name for name, passed in checks.items() if not passed]
    if state.get("serious_adverse_event_present") and not state["serious_adverse_event_escalated"]:
        blockers.append("serious_adverse_event_not_escalated")
    if state["unresolved_conflicts"]:
        blockers.append("unresolved_conflict")
    if state["unresolved_questions"]:
        blockers.append("unresolved_question")
    if state["open_risks"]:
        blockers.append("open_trial_risk")
    return blockers
