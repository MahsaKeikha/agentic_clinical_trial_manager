from AGENTS.protocol_planner_agent import ProtocolPlannerAgent
from AGENTS.site_coordinator_agent import SiteCoordinatorAgent
from AGENTS.recruitment_tracker_agent import RecruitmentTrackerAgent
from AGENTS.data_quality_agent import DataQualityAgent
from AGENTS.deviation_reviewer_agent import DeviationReviewerAgent
from AGENTS.reporting_agent import ReportingAgent

def run_workflow(c: dict) -> dict:
    agents=[ProtocolPlannerAgent(),SiteCoordinatorAgent(),RecruitmentTrackerAgent(),DataQualityAgent(),DeviationReviewerAgent(),ReportingAgent()]
    return {a.name:a.run(c) for a in agents}
